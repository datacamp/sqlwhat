from sqlwhat.checks.check_funcs import check_node, check_field, has_equal_ast
from sqlwhat.checks import check_funcs as cf
from sqlwhat.selectors import get_ast_parser, Dispatcher
from sqlwhat.State import State
from sqlwhat.Reporter import Reporter
from sqlwhat.Test import TestFail as TF
import pytest

@pytest.fixture
def ast_mod():
    return get_ast_parser('postgresql')

@pytest.fixture(params = ['postgresql', 'mssql'])
def dialect_name(request):
    return request.param

def prepare_state(solution_code, student_code, dialect='postgresql'):
    dispatcher = Dispatcher.from_dialect(dialect)
    return State(
        student_code = student_code,
        solution_code = solution_code,
        reporter = Reporter(),
        # args below should be ignored
        pre_exercise_code = "NA", 
        student_result = [], solution_result = [],
        student_conn = None, solution_conn = None,
        ast_dispatcher = dispatcher)

def test_has_equal_ast_pass_identical():
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id, name FROM Trips")
    has_equal_ast(state=state)

def test_has_equal_ast_pass_clause_caps():
    state = prepare_state("select id, name from Trips", "SELECT id, name FROM Trips")
    has_equal_ast(state=state)

def test_has_equal_ast_pass_spacing():
    state = prepare_state("SELECT id,name from Trips", "SELECT id, name FROM Trips")
    has_equal_ast(state=state)

def test_has_equal_ast_pass_unparsed():
    query = "SELECT CURSOR (SELECT * FROM TRIPS) FROM Trips"
    state = prepare_state(query, query)
    has_equal_ast(state=state)

def test_has_equal_ast_fail_quoted_column():
    state = prepare_state('SELECT "id", "name" FROM "Trips"', "SELECT id, name FROM Trips")
    with pytest.raises(TF): has_equal_ast(state=state)

def test_has_equal_ast_manual_fail():
    query = "SELECT id, name FROM Trips"
    state = prepare_state(query, query)
    with pytest.raises(TF): 
        child = check_node(state, "SelectStmt")
        has_equal_ast(child, sql="SELECT * FROM Trips", start="subquery")

def test_has_equal_ast_manual_pass():
    query = "SELECT id, name FROM Trips"
    state = prepare_state(query, query)
    child = check_node(state, "SelectStmt")
    has_equal_ast(child, sql=query, start="subquery")

def test_check_node_pass(ast_mod):
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id FROM Trips")
    child = check_node(state, "SelectStmt", 0)
    assert isinstance(child.student_ast, ast_mod.SelectStmt)
    assert isinstance(child.solution_ast, ast_mod.SelectStmt)

def test_check_node_fail():
    state = prepare_state("SELECT id, name FROM Trips", "INSERT INTO Trips VALUES (1)")
    with pytest.raises(TF): check_node(state, "SelectStmt", 0)

def test_check_node_antlr_exception_skips(dialect_name):
    state = prepare_state("SELECT x FROM ___!", "SELECT x FROM ___!", dialect_name)
    assert isinstance(state.student_ast, state.ast_dispatcher.ast.AntlrException)
    select = check_node(state, "SelectStmt", 2)   # should be skipped
    assert select is state

def test_check_field_pass():
    state = prepare_state("SELECT id FROM Trips WHERE id > 3", "SELECT id FROM Trips WHERE id>3")
    select = check_node(state, "SelectStmt", 0)
    check_field(select, "where_clause")

def test_check_field_fail():
    state = prepare_state("SELECT id FROM Trips WHERE id > 3", "SELECT id FROM Trips WHERE id>4")
    select = check_node(state, "SelectStmt", 0)
    check_field(select, "where_clause")

def test_check_field_antlr_exception_skips(dialect_name):
    state = prepare_state("SELECT x FROM ___!", "SELECT x FROM ___!", dialect_name)
    assert isinstance(state.student_ast, state.ast_dispatcher.ast.AntlrException)
    select = check_field(state, "where", 0)   # should be skipped
    assert select is state


@pytest.fixture
def state_tst():
    return prepare_state("SELECT id FROM Trips", "SELECT id FROM Trips WHERE id > 4   ;")

def test_student_typed_itself_pass(state_tst):
    cf.test_student_typed(state_tst, text=state_tst.student_code, fixed=True)

def test_student_typed_fixed_subset_fail(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    # should fail because the select statement does not include ';'
    with pytest.raises(TF):
        cf.test_student_typed(state_tst, state_tst.student_code, fixed=True)

def test_student_typed_fixed_subset_pass(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    where = check_field(select, "where_clause")
    cf.test_student_typed(where, "id > 4", fixed=True)

def test_student_typed_fixed_subset_fail(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    where = check_field(select, "where_clause")
    with pytest.raises(TF):
        cf.test_student_typed(where, "WHERE id > 4", fixed=True)

def test_student_typed_subset_re_pass(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    where = check_field(select, "where_clause")
    cf.test_student_typed(where, "id > [0-9]")

def test_student_typed_subset_re_pass(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    where = check_field(select, "where_clause")
    with pytest.raises(TF):
        cf.test_student_typed(where, "id > [a-z]")
