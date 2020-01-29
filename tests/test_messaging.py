import importlib
import pytest

from protowhat.selectors import Dispatcher
from sqlwhat.State import State, PARSER_MODULES
from protowhat.Reporter import Reporter
from protowhat.failure import TestFail as TF
from tests.helper import (
    Connection,
    has_result,
    has_nrows,
    has_ncols,
    check_row,
    has_equal_value,
    check_column,
    check_all_columns,
)


def prepare_state(sol_result, stu_result):
    conn = Connection("postgresql")
    return State(
        student_code="",
        solution_code="",
        reporter=Reporter(),
        # args below should be ignored
        pre_exercise_code="NA",
        student_result=stu_result,
        solution_result=sol_result,
        student_conn=conn,
        solution_conn=None,
    )


def test_has_result():
    state = prepare_state({"a": [1, 2, 3]}, {})
    with pytest.raises(TF, match="Your query did not return a result."):
        has_result(state)


# Check funcs -----------------------------------------------------------------


@pytest.mark.parametrize(
    "stu, patt", [({"a": [1]}, "1 row"), ({"a": [1, 2]}, "2 rows")]
)
def test_has_nrows(stu, patt):
    state = prepare_state({"a": [1, 2, 3]}, stu)
    with pytest.raises(
        TF,
        match="Your query returned a table with {} while it should return a table with 3 rows.".format(
            patt
        ),
    ):
        has_nrows(state)


@pytest.mark.parametrize(
    "stu, patt",
    [({"a": [1]}, "1 column"), ({"a": [1], "b": [1], "c": [1]}, "3 columns")],
)
def test_has_ncols(stu, patt):
    state = prepare_state({"a": [1], "b": [1]}, stu)
    with pytest.raises(
        TF,
        match="Your query returned a table with {} while it should return a table with 2 columns.".format(
            patt
        ),
    ):
        has_ncols(state)


@pytest.mark.parametrize(
    "stu, patt",
    [
        (
            {"a": [1]},
            "The system wants to verify row 2 of your query result, but couldn't find it. Have another look.",
        ),
        (
            {"a": [1, 3]},
            "Have another look at row 2 in your query result. Column `a` seems to be incorrect.",
        ),
    ],
)
def test_check_row(stu, patt):
    state = prepare_state({"a": [1, 2]}, stu)
    with pytest.raises(TF, match=patt):
        ss = check_row(state, 1)
        has_equal_value(ss)


@pytest.mark.parametrize(
    "stu, patt",
    [
        (
            {"b": [2]},
            "We expected to find a column named `a` in the result of your query, but couldn't.",
        ),
        (
            {"a": [2]},
            r"Have another look at your query result\. Column `a` seems to be incorrect\.$",
        ),
    ],
)
def test_check_column(stu, patt):
    state = prepare_state({"a": [1]}, stu)
    with pytest.raises(TF, match=patt):
        ss = check_column(state, "a")
        has_equal_value(ss)


@pytest.mark.parametrize(
    "stu, patt",
    [
        (
            {"b": [2]},
            "We expected to find a column named `a` in the result of your query, but couldn't.",
        ),
        (
            {"a": [2], "b": [1]},
            "Your query result contains the column `b` but shouldn't.",
        ),
        (
            {"a": [2]},
            r"Have another look at your query result\. Column `a` seems to be incorrect\.$",
        ),
    ],
)
def test_check_all_columns(stu, patt):
    state = prepare_state({"a": [1]}, stu)
    with pytest.raises(TF, match=patt):
        ss = check_all_columns(state, allow_extra=False)
        has_equal_value(ss)


def test_has_equal_value():
    state = prepare_state({"a": [1, 2]}, {"a": [2, 1]})
    with pytest.raises(
        TF,
        match="Have another look at your query result. Column `a` seems to be incorrect. Make sure you arranged the rows correctly.",
    ):
        has_equal_value(check_column(state, "a"), ordered=True)
