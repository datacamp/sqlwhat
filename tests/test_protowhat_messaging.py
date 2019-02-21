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


def print_message(exc):
    print(exc.value.payload["message"])


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


# get_ast_path ----------------------------------------------------------------


@pytest.mark.parametrize(
    "query, path, target_desc",
    [
        (
            "SELECT a as c FROM b",
            [[check_node, ["SelectStmt"]]],
            "first `SELECT` statement",
        ),
        (
            "SELECT a as c FROM b",
            [[check_node, ["SelectStmt"]], [check_node, ["AliasExpr", 0]]],
            "first alias expression",
        ),
        (
            "SELECT a FROM b",
            [[check_node, ["SelectStmt"]], [check_edge, ["from_clause"]]],
            "`FROM` clause of the `SELECT` statement",
        ),
        (
            "SELECT a FROM b",
            [[check_node, ["SelectStmt"]], [check_edge, ["target_list", 0]]],
            "first entry in the target list of the `SELECT` statement",
        ),
        (
            "SELECT a FROM b INNER JOIN c HAVING(d)",
            [
                [check_node, ["SelectStmt"]],
                [check_edge, ["from_clause"]],
                [check_edge, ["left"]],
            ],
            None,  # Doesn't generate anything for now!
        ),
        (
            "SELECT a FROM b INNER JOIN c HAVING(d)",
            [
                [check_node, ["SelectStmt"]],
                [check_node, ["JoinExpr"]],
                [check_edge, ["left"]],
            ],
            "left operand of the join expression",  # using check_node instead _does_ generate something
        ),
        (
            "SELECT a FROM b WHERE c BETWEEN 1 AND 2",
            [
                [check_node, ["SelectStmt"]],
                [check_edge, ["where_clause"]],
                [check_edge, ["left"]],
            ],
            None,  # Doesn't generate anything!
        ),
        (
            "SELECT a FROM b WHERE c BETWEEN 1 AND 2",
            [
                [check_node, ["SelectStmt"]],
                [check_node, ["BinaryExpr"]],
                [check_edge, ["left"]],
            ],
            "left operand of the binary expression `between`",  # using check_node instead _does_ generate something
        ),
    ],
)
def test_get_ast_path(query, path, target_desc):
    state = prepare_state(query, query)
    for step in path:
        state = step[0](state, *step[1])
    assert state.get_ast_path() == target_desc


# check_node - check_edge -----------------------------------------------------------------


@pytest.mark.parametrize(
    "stu, path, msg",
    [
        (
            "",
            [
                [check_node, ["SelectStmt"]],
                [check_node, ["JoinExpr"]],
                [check_edge, ["left"]],
                [has_equal_ast, []],
            ],
            "Check the Script. Could not find the first `SELECT` statement.",
        ),
        (
            "SELECT a FROM c",
            [
                [check_node, ["SelectStmt"]],
                [check_node, ["JoinExpr"]],
                [check_edge, ["left"]],
                [has_equal_ast, []],
            ],
            "Check the first `SELECT` statement. Could not find the first join expression.",
        ),
        (
            "SELECT a FROM c INNER JOIN b HAVING(d)",
            [
                [check_node, ["SelectStmt"]],
                [check_node, ["JoinExpr"]],
                [check_edge, ["left"]],
                [has_equal_ast, []],
            ],
            "Check the left operand of the join expression. The checker expected to find `b` in there.",
        ),
        (
            # using check_edge('from_clause') instead of check_node('JoinExpr')
            "SELECT a FROM c INNER JOIN b HAVING(d)",
            [
                [check_node, ["SelectStmt"]],
                [check_edge, ["from_clause"]],
                [check_edge, ["left"]],
                [has_equal_ast, []],
            ],
            "Check the highlighted code. The checker expected to find `b` in there.",
        ),
    ],
)
def test_check_messaging(stu, path, msg):
    state = prepare_state("SELECT a FROM b INNER JOIN c HAVING(d)", stu)
    with pytest.raises(TF, match=msg):
        for step in path:
            state = step[0](state, *step[1])


@pytest.mark.parametrize(
    "stu, path, msg",
    [
        (
            "SELECT a FROM b ORDER BY b",
            [
                [check_node, ["SelectStmt"]],
                [check_edge, ["order_by_clause"]],
                [has_equal_ast, []],
            ],
            "Check the `ORDER BY` clause of the `SELECT` statement. The checker expected to find `ORDER BY c` in there.",
        ),
        (
            "SELECT a FROM b ORDER BY b",
            [
                [check_node, ["SelectStmt"]],
                [check_edge, ["order_by_clause"]],
                [check_node, ["SortBy"]],
                [has_equal_ast, []],
            ],
            "Check the first sorting expression. The checker expected to find `c` in there.",
        ),
    ],
)
def test_check_messaging_2(stu, path, msg):
    state = prepare_state("SELECT a FROM b ORDER BY c", stu)
    with pytest.raises(TF, match=msg):
        for step in path:
            state = step[0](state, *step[1])
