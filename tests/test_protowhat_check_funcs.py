import importlib
import pytest

from protowhat.checks.check_funcs import (
    check_node,
    check_edge,
    has_equal_ast,
    has_code,
    has_parsed_ast,
)
from protowhat.selectors import Dispatcher
from sqlwhat.State import State, PARSER_MODULES
from protowhat.Reporter import Reporter
from protowhat.Test import TestFail as TF


@pytest.fixture
def ast_mod():
    return importlib.import_module(PARSER_MODULES["postgresql"])


@pytest.fixture(params=["postgresql", "mssql"])
def dialect_name(request):
    return request.param


def prepare_state(sol_code, stu_code, dialect="postgresql"):
    dispatcher = Dispatcher.from_module(PARSER_MODULES[dialect])
    return State(
        student_code=stu_code,
        solution_code=sol_code,
        reporter=Reporter(),
        # args below should be ignored
        pre_exercise_code="NA",
        student_result=[],
        solution_result=[],
        student_conn=None,
        solution_conn=None,
        ast_dispatcher=dispatcher,
    )


# has_equal_ast ---------------------------------------------------------------


@pytest.mark.parametrize(
    "sol, stu",
    [
        ("SELECT id, name FROM Trips", "SELECT id, name FROM Trips"),  # identical
        ("select id, name from Trips", "SELECT id, name FROM Trips"),  # clause caps
        ("SELECT id,name from Trips", "SELECT id, name FROM Trips"),  # spacing
        (
            "SELECT CURSOR (SELECT * FROM TRIPS) FROM Trips",
            "SELECT CURSOR (SELECT * FROM TRIPS) FROM Trips",
        ),  # unparsed
    ],
)
def test_has_equal_ast_pass(sol, stu):
    state = prepare_state(sol, stu)
    has_equal_ast(state=state)


def test_has_equal_ast_fail_quoted_column():
    state = prepare_state(
        'SELECT "id", "name" FROM "Trips"', "SELECT id, name FROM Trips"
    )
    with pytest.raises(TF):
        has_equal_ast(state=state)


def test_has_equal_ast_field_fail():
    state = prepare_state("SELECT id, name FROM Trips", "SELECT name FROM Trips")
    sel = check_node(state, "SelectStmt", 0)
    tl = check_edge(sel, "target_list", 0)
    with pytest.raises(TF):
        has_equal_ast(tl)


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
    with pytest.raises(TF):
        has_equal_ast(child, sql="id < 999", start="expression", exact=False)


# check_node ------------------------------------------------------------------


def test_check_node_pass(ast_mod):
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id FROM Trips")
    child = check_node(state, "SelectStmt", 0)
    assert isinstance(child.student_ast, ast_mod.SelectStmt)
    assert isinstance(child.solution_ast, ast_mod.SelectStmt)


def test_check_node_fail():
    state = prepare_state("SELECT id, name FROM Trips", "INSERT INTO Trips VALUES (1)")
    with pytest.raises(TF):
        check_node(state, "SelectStmt", 0)


def test_check_node_priority_pass(ast_mod):
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id FROM Trips")
    child = check_node(state, "Identifier", 0, priority=99)
    assert isinstance(child.student_ast, ast_mod.Identifier)
    assert isinstance(child.solution_ast, ast_mod.Identifier)


def test_check_node_priority_fail():
    state = prepare_state(
        "SELECT id + 1, name FROM Trips", "INSERT INTO Trips VALUES (1)"
    )
    with pytest.raises(TF):
        check_node(state, "SelectStmt", 0, priority=0)
    with pytest.raises(TF):
        check_node(state, "BinaryExpr", 0, priority=99)


def test_check_node_back_to_back():
    state = prepare_state("SELECT 1 + 2 + 3 FROM x", "SELECT 1 + 2 + 3 FROM x")
    sel = check_node(state, "SelectStmt", 0)
    bin1 = check_node(sel, "BinaryExpr", 0)
    bin2 = check_node(bin1, "BinaryExpr", 0)
    assert bin2.student_ast.left == "1"


def test_check_node_from_list():
    state = prepare_state("SELECT a, b, c FROM x", "SELECT a, b, c FROM x")
    sel = check_node(state, "SelectStmt", 0)
    tl = check_edge(sel, "target_list", None)
    check_node(tl, "Identifier")


def test_check_node_antlr_exception_skips(dialect_name):
    state = prepare_state("SELECT x FROM ___!", "SELECT x FROM ___!", dialect_name)
    assert isinstance(state.student_ast, state.ast_dispatcher.ast.ParseError)
    select = check_node(state, "SelectStmt", 2)  # should be skipped
    assert select is state


# check_edge -----------------------------------------------------------------


def test_check_edge_pass():
    state = prepare_state(
        "SELECT id FROM Trips WHERE id > 3", "SELECT id FROM Trips WHERE id>3"
    )
    select = check_node(state, "SelectStmt", 0)
    check_edge(select, "where_clause")


def test_check_edge_fail():
    state = prepare_state(
        "SELECT id FROM Trips WHERE id > 3", "SELECT id FROM Trips WHERE id>4"
    )
    select = check_node(state, "SelectStmt", 0)
    check_edge(select, "where_clause")


def test_check_edge_index_pass():
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id, name FROM Trips")
    select = check_node(state, "SelectStmt", 0)
    check_edge(select, "target_list", 1)


def test_check_edge_index_fail():
    state = prepare_state("SELECT id, name FROM Trips", "SELECT id FROM Trips")
    select = check_node(state, "SelectStmt", 0)
    with pytest.raises(TF):
        check_edge(select, "target_list", 1)


def test_check_edge_antlr_exception_skips(dialect_name):
    state = prepare_state("SELECT x FROM ___!", "SELECT x FROM ___!", dialect_name)
    assert isinstance(state.student_ast, state.ast_dispatcher.ast.ParseError)
    select = check_edge(state, "where", 0)  # should be skipped
    assert select is state


def test_check_edge_index_none_fail():
    state = prepare_state("SELECT a, b FROM b WHERE a < 10", "SELECT a FROM b")
    sel = check_node(state, "SelectStmt")
    with pytest.raises(TF):
        check_edge(sel, "where_clause")


# TODO this should be handled better in protowhat
def test_where_brackets_with_has_code():
    state = prepare_state(
        "SELECT a FROM b WHERE c AND d", "SELECT a FROM b WHERE (d AND c)"
    )
    sel = check_node(state, "SelectStmt")
    wc = check_edge(sel, "where_clause")
    has_code(wc, "d")
    with pytest.raises(TF):
        has_code(wc, "not_there")


# has_code --------------------------------------------------------------------


@pytest.fixture
def state_tst():
    return prepare_state(
        "SELECT id FROM Trips",
        "SELECT id FROM Trips WHERE id > 4 AND name = 'greg'   ;",
    )


def test_has_code_itself_pass(state_tst):
    has_code(state_tst, text=state_tst.student_code, fixed=True)


def test_has_code_fixed_subset_fail(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    # should fail because the select statement does not include ';'
    with pytest.raises(TF):
        has_code(select, state_tst.student_code, fixed=True)


def test_has_code_fixed_subset_pass(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    where = check_edge(select, "where_clause")
    has_code(where, "id > 4", fixed=True)


def test_has_code_fixed_subset_fail2(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    where = check_edge(select, "where_clause")
    with pytest.raises(TF):
        has_code(where, "WHERE id > 4", fixed=True)


def test_has_code_subset_re_pass(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    where = check_edge(select, "where_clause")
    has_code(where, "id > [0-9]")


def test_has_code_subset_re_pass2(state_tst):
    select = check_node(state_tst, "SelectStmt", 0)
    where = check_edge(select, "where_clause")
    with pytest.raises(TF):
        has_code(where, "id > [a-z]")


def test_has_code_upper_case_pass(state_tst):
    has_code(state_tst, "AND")


def test_has_code_fixed_star_pass():
    state_tst = prepare_state("SELECT * FROM x", "SELECT * FROM x")
    has_code(state_tst, "*", fixed=True)


def test_has_code_no_ast():
    state_tst = prepare_state("SELECT * FROM x!!", "SELECT * FROM x!!")
    has_code(state_tst, "*", fixed=True)


def test_has_parsed_ast():
    state_tst = prepare_state("SELECT * FROM x!!!", "SELECT * FROM x!!!")
    with pytest.raises(TF):
        has_parsed_ast(state_tst)
