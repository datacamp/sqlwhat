import pytest

from protowhat.Test import TestFail as TF
from tests.helper import (
    prepare_state,
    passes,
    check_row,
    check_column,
    check_all_columns,
    check_result,
    lowercase,
    has_equal_value,
)


@pytest.mark.parametrize(
    "stu, stu_sub, success",
    [
        ({}, None, False),
        ({"a": [1]}, None, False),
        ({"a": [1, 2]}, {"a": [2]}, True),
        ({"b": [1, 2]}, {"b": [2]}, True),
        ({"a": [1, 2], "b": [3, 4]}, {"a": [2], "b": [4]}, True),
        ({"a": [1, 2, 3], "b": [4, 5, 6]}, {"a": [2], "b": [5]}, True),
    ],
)
def test_check_row(stu, stu_sub, success):
    state = prepare_state({"a": [1, 2, 3], "b": [4, 5, 6]}, stu)
    if success:
        x = check_row(state, 1)
        passes(x)
        assert x.solution_result == {"a": [2], "b": [5]}
        assert x.student_result == stu_sub
    else:
        with pytest.raises(TF):
            check_row(state, 1)


def test_check_row_wrong_usage():
    state = prepare_state({"a": [1]}, {"a": [1]})
    with pytest.raises(BaseException):
        check_row(state, 1)


@pytest.mark.parametrize(
    "stu, stu_sub, success",
    [
        ({}, None, False),
        ({"b": []}, None, False),
        ({"A": [1]}, None, False),
        ({"a": []}, {"a": []}, True),
        ({"a": [1]}, {"a": [1]}, True),
        ({"a": [1], "b": [2]}, {"a": [1]}, True),
    ],
)
def test_check_column(stu, stu_sub, success):
    state = prepare_state({"a": [1]}, stu)
    if success:
        x = check_column(state, "a")
        passes(x)
        assert x.solution_result == {"a": [1]}
        assert x.student_result == stu_sub
    else:
        with pytest.raises(TF):
            check_column(state, "a")


def test_check_column_wrong_usage():
    state = prepare_state({"a": [1]}, {"a": [1]})
    with pytest.raises(BaseException):
        check_column(state, "b")


@pytest.mark.parametrize(
    "stu, stu_sub, success",
    [
        ({}, None, False),
        ({"a": [1]}, None, False),
        ({"A": [1], "b": [2]}, None, False),
        ({"a": [1], "b": [2]}, {"a": [1], "b": [2]}, True),
        ({"a": [4], "b": [5]}, {"a": [4], "b": [5]}, True),
        ({"a": [1], "b": [2], "c": [3]}, {"a": [1], "b": [2]}, True),
    ],
)
def test_check_all_columns(stu, stu_sub, success):
    state = prepare_state({"a": [1], "b": [2]}, stu)
    if success:
        x = check_all_columns(state)
        passes(x)
        assert x.solution_result == {"a": [1], "b": [2]}
        assert x.student_result == stu_sub
    else:
        with pytest.raises(TF):
            check_all_columns(state)


@pytest.mark.parametrize(
    "stu, success",
    [
        ({"a": [1], "b": [2]}, True),
        ({"a": [4], "b": [5]}, True),
        ({"A": [1], "b": [2]}, False),
    ],
)
def test_check_all_columns_stricter(stu, success):
    state = prepare_state({"a": [1], "b": [2]}, stu)
    if success:
        passes(check_all_columns(state, allow_extra=False))
    else:
        with pytest.raises(TF):
            check_all_columns(state, allow_extra=False)


def test_lower_case():
    state = prepare_state({"a": [1]}, {"A": [1]})

    # fails if not using lowercase
    with pytest.raises(TF):
        check_column(state, "a")

    # passes if lowercase is being used
    child = lowercase(state)
    child2 = check_column(child, "a")
    passes(child2)
    passes(has_equal_value(child2))


@pytest.mark.parametrize(
    "stu, success",
    [
        ({"a": [1]}, False),
        ({"a": [1, 1]}, False),
        ({"a": [1, 2]}, False),
        ({"a": [1, 2], "b": [5, 6]}, False),
        ({"a": [1, 2, 3], "b": [3, 4, 5]}, False),
        ({"a": [1, 2], "b": [3, 4]}, True),
        ({"a": [1, 2], "B": [3, 4]}, True),
        ({"a": [1, 2], "b": [3, 4], "c": [5, 6]}, True),
    ],
)
def test_check_result(stu, success):
    state = prepare_state({"a": [1, 2], "b": [3, 4]}, stu)
    if success:
        passes(check_result(state))
    else:
        with pytest.raises(TF):
            check_result(state)
