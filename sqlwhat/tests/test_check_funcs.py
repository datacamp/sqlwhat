from sqlwhat.checks.check_funcs import check_node, check_field, has_equal_ast
from sqlwhat.checks import check_funcs as cf
from sqlwhat.selectors import get_ast_parser, Dispatcher
from sqlwhat.State import State
from sqlwhat.Reporter import Reporter
from sqlwhat.Test import TestFail as TF
import pytest

def print_message(exc): print(exc.value.args[0].message)

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
    with pytest.raises(TF) as exc_info: has_equal_ast(state=state)
    print_message(exc_info)

def test_has_equal_ast_field_fail():
    state = prepare_state('SELECT id, name FROM Trips', "SELECT name FROM Trips")
    sel = cf.check_node(state, "SelectStmt", 0)
    tl = cf.check_field(sel, "target_list", 0)
    with pytest.raises(TF) as exc_info: has_equal_ast(tl)
    print_message(exc_info)

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

def test_has_equal_ast_not_exact_pass():
    query = "SELECT id, name FROM Trips WHERE id < 100 AND name = 'greg'"
    state = prepare_state(query, query)
    child = check_node(state, "SelectStmt")
    has_equal_ast(child, sql="id < 100", start="expression", exact=False)

def test_has_equal_ast_not_exact_fail():
    query = "SELECT id, name FROM Trips WHERE id < 100 AND name = 'greg'"
    state = prepare_state(query, query)
    child = check_node(state, "SelectStmt")
    with pytest.raises(TF) as exc_info:
        has_equal_ast(child, sql="id < 999", start="expression", exact=False)
    print_message(exc_info)

def test_check_node_pass(ast_mod):
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id FROM Trips")
    child = check_node(state, "SelectStmt", 0)
    assert isinstance(child.student_ast, ast_mod.SelectStmt)
    assert isinstance(child.solution_ast, ast_mod.SelectStmt)

def test_check_node_fail():
    state = prepare_state("SELECT id, name FROM Trips", "INSERT INTO Trips VALUES (1)")
    with pytest.raises(TF) as exc_info: check_node(state, "SelectStmt", 0)
    print_message(exc_info)

def test_check_node_priority_pass(ast_mod):
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id FROM Trips")
    child = check_node(state, "Identifier", 0, priority=99)
    assert isinstance(child.student_ast, ast_mod.Identifier)
    assert isinstance(child.solution_ast, ast_mod.Identifier)

def test_check_node_priority_fail():
    state = prepare_state("SELECT id + 1, name FROM Trips", "INSERT INTO Trips VALUES (1)")
    with pytest.raises(TF):             check_node(state, "SelectStmt", 0, priority=0)
    with pytest.raises(TF) as exc_info: check_node(state, "BinaryExpr", 0, priority = 99)
    print_message(exc_info)

def test_check_node_back_to_back():
    state = prepare_state("SELECT 1 + 2 + 3 FROM x", "SELECT 1 + 2 + 3 FROM x")
    sel = check_node(state, 'SelectStmt', 0)
    bin1 = check_node(sel, 'BinaryExpr', 0)
    bin2 = check_node(bin1, 'BinaryExpr', 0)
    assert bin2.student_ast.left == '1'

def test_check_node_from_list():
    state = prepare_state("SELECT a, b, c FROM x", "SELECT a, b, c FROM x")
    sel = check_node(state, "SelectStmt", 0)
    tl = check_field(sel, "target_list")
    check_node(tl, "Identifier")

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

def test_check_field_index_pass():
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id, name FROM Trips")
    select = check_node(state, "SelectStmt", 0)
    check_field(select, "target_list", 1)

def test_check_field_index_fail():
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id FROM Trips")
    select = check_node(state, "SelectStmt", 0)
    with pytest.raises(TF) as exc_info: check_field(select, "target_list", 1)
    print_message(exc_info)


def test_check_field_antlr_exception_skips(dialect_name):
    state = prepare_state("SELECT x FROM ___!", "SELECT x FROM ___!", dialect_name)
    assert isinstance(state.student_ast, state.ast_dispatcher.ast.AntlrException)
    select = check_field(state, "where", 0)   # should be skipped
    assert select is state


@pytest.fixture
def state_tst():
    return prepare_state("SELECT id FROM Trips", "SELECT id FROM Trips WHERE id > 4 AND name = 'greg'   ;")

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

def test_student_typed_upper_case_pass(state_tst):
    cf.test_student_typed(state_tst, "AND")

def test_student_typed_fixed_star_pass():
    state_tst = prepare_state("SELECT * FROM x", "SELECT * FROM x")
    cf.test_student_typed(state_tst, "*", fixed=True)

def test_student_typed_no_ast():
    state_tst = prepare_state("SELECT * FROM x!!", "SELECT * FROM x!!")
    cf.test_student_typed(state_tst, "*", fixed=True)

def test_verify_ast_parses_fail():
    state_tst = prepare_state("SELECT * FROM x!!!", "SELECT * FROM x!!!")
    with pytest.raises(TF):
        cf.verify_ast_parses(state_tst)

def test_check_field_index_none_fail():
    state = prepare_state("SELECT a, b FROM b WHERE a < 10", "SELECT a FROM b")
    sel = check_node(state, 'SelectStmt') 
    with pytest.raises(TF) as exc_info:
        from_field = check_field(sel, 'where_clause')
    print_message(exc_info)
