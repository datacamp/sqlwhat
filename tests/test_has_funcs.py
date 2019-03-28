import pytest
from protowhat.Test import TestFail as TF

from sqlwhat import checks
from sqlwhat.checks.has_funcs import sort_rows
from tests.helper import prepare_state, passes


def test_has_no_error():
    state = prepare_state({}, {}, ["an error"])
    with pytest.raises(TF):
        checks.has_no_error(state)
    state = prepare_state({"a": [1]}, {"a": [1]}, [])
    passes(checks.has_no_error(state))


@pytest.mark.parametrize(
    "stu, errors, success",
    [
        ({}, ["an error"], False),
        ({}, [], False),
        ({"a": [1]}, ["an error"], False),
        ({"a": [1, 2, 3]}, [], True),
        ({"a": []}, [], True),
    ],
)
def test_has_result(stu, errors, success):
    state = prepare_state({"a": [1, 2, 3]}, stu, errors)
    if success:
        passes(checks.has_result(state))
    else:
        with pytest.raises(TF):
            checks.has_result(state)


def test_has_result_wrong_usage():
    state = prepare_state({}, {})
    with pytest.raises(NameError):
        checks.has_result(state)


@pytest.mark.parametrize(
    "stu, success",
    [
        ({}, False),
        ({"a": []}, False),
        ({"b": [1, 2]}, False),
        ({"a": [1, 2, 3]}, True),
        ({"b": [1, 2, 3]}, True),
    ],
)
def test_has_nrows(stu, success):
    state = prepare_state({"a": [1, 2, 3]}, stu)
    if success:
        passes(checks.has_nrows(state))
    else:
        with pytest.raises(TF):
            checks.has_nrows(state)


@pytest.mark.parametrize(
    "stu, success",
    [
        ({}, False),
        ({"a": []}, False),
        ({"b": [1, 2]}, False),
        ({"a": [1], "b": [4], "c": [7]}, False),
        ({"a": [1, 2, 3], "b": [4, 5, 6]}, True),
        ({"a": [1], "b": [4]}, True),
        ({"c": [1], "d": [4]}, True),
    ],
)
def test_has_ncols(stu, success):
    state = prepare_state({"a": [1, 2, 3], "b": [4, 5, 6]}, stu)
    if success:
        passes(checks.has_ncols(state))
    else:
        with pytest.raises(TF):
            checks.has_ncols(state)


@pytest.mark.parametrize(
    "stu, success",
    [
        ({"a": [1]}, False),
        ({"a": [1, 1]}, False),
        ({"a": [1.11, 1]}, False),
        ({"a": [1, 2]}, True),
        ({"a": [2, 1]}, True),
        ({"a": [1, 2], "b": [5, 6]}, True),
    ],
)
def test_has_equal_value_basic(stu, success):
    state = prepare_state({"a": [1, 2], "b": [3, 4]}, stu)
    child = checks.check_column(state, "a")
    if success:
        passes(checks.has_equal_value(child))
    else:
        with pytest.raises(TF):
            checks.has_equal_value(child)


@pytest.mark.parametrize(
    "stu, success",
    [
        ({"a": [1]}, False),
        ({"a": [1, 1]}, False),
        ({"a": [1, 2]}, True),
        ({"a": [2, 1]}, False),
        ({"a": [1, 2], "b": [5, 6]}, True),
    ],
)
def test_has_equal_value_ordered(stu, success):
    state = prepare_state({"a": [1, 2], "b": [3, 4]}, stu)
    child = checks.check_column(state, "a")
    if success:
        passes(checks.has_equal_value(child, ordered=True))
    else:
        with pytest.raises(TF):
            checks.has_equal_value(child, ordered=True)


@pytest.mark.parametrize(
    "stu, success",
    [({"a": [1.131]}, False), ({"a": ["abc"]}, False), ({"a": [1.121]}, True)],
)
def test_has_equal_value_ndigits(stu, success):
    state = prepare_state({"a": [1.124]}, stu)
    child = checks.check_column(state, "a")
    if success:
        passes(checks.has_equal_value(child, ndigits=2))
    else:
        with pytest.raises(TF):
            checks.has_equal_value(child, ndigits=2)


def test_has_equal_value_wrong_usage():
    state = prepare_state({}, {})
    with pytest.raises(ValueError):
        checks.has_equal_value(state)


@pytest.mark.parametrize(
    "sol_result,stu_result",
    [
        ({"a": [2, 2, 1], "b": [2, 1, 1]}, {"a": [2, 2, 1], "b": [1, 2, 1]}),
        ({"a": [None, 2, 1], "b": [2, 1, 1]}, {"a": [2, None, 1], "b": [1, 2, 1]}),
        ({"a": [2, None, 1], "b": [2, 1, 1]}, {"a": [None, 2, 1], "b": [1, 2, 1]}),
        (
            {"a": [None, "a", "b"], "b": [2, 1, 1]},
            {"a": ["a", None, "b"], "b": [1, 2, 1]},
        ),
        (
            {"a": [2, 2, 1], "b": [2, 1, 1]},
            {"a": [2, 2, 1], "b": [1, 2, 1], "c": [0, 0, 0]},
        ),
    ],
)
def test_sort_rows_pass(sol_result, stu_result):
    state = prepare_state(sol_result, stu_result)
    stu, sol = sort_rows(state)
    assert all(k in sol for k in state.solution_result)
    assert all(k in stu for k in state.student_result)
    if "a" in state.solution_result and "a" in state.student_result:
        assert sol["a"] == stu["a"]
