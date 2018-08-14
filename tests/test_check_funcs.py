import importlib
import pytest

cr = importlib.import_module('sqlwhat.checks.check_funcs')
from protowhat.selectors import Dispatcher
from sqlwhat.State import State, PARSER_MODULES
from protowhat.Reporter import Reporter
from protowhat.Test import TestFail as TF
from helper import Connection

def prepare_state(sol_result, stu_result, error=None):
    conn = Connection('postgresql')
    return State(
        student_code = "",
        solution_code = "",
        reporter = Reporter(error),
        # args below should be ignored
        pre_exercise_code = "NA",
        student_result = stu_result, solution_result = sol_result,
        student_conn = conn, solution_conn = None)

def passes(x):
    assert isinstance(x, State)

def test_has_error():
    state = prepare_state({}, {}, ['an error'])
    with pytest.raises(TF): cr.has_error(state)
    state = prepare_state({'a': [1]}, {'a': [1]}, [])
    passes(cr.has_error(state))

@pytest.mark.parametrize('stu, errors, success', [
    ({}, ['an error'], False),
    ({}, [], False),
    ({'a': [1]}, ['an error'], False),
    ({'a': [1, 2, 3]}, [], True),
    ({'a': []}, [], True),
])
def test_has_result(stu, errors, success):
    state = prepare_state({'a': [1,2,3]}, stu, errors)
    if success:
        passes(cr.has_result(state))
    else:
        with pytest.raises(TF): cr.has_result(state)

def test_has_result_wrong_usage():
    state = prepare_state({}, {})
    with pytest.raises(NameError):
        cr.has_result(state)

@pytest.mark.parametrize('stu, success', [
    ({}, False),
    ({'a': []}, False),
    ({'b': [1, 2]}, False),
    ({'a': [1, 2, 3]}, True),
    ({'b': [1, 2, 3]}, True),
])
def test_has_nrows(stu, success):
    state = prepare_state({'a': [1,2,3]}, stu)
    if success:
        passes(cr.has_nrows(state))
    else:
        with pytest.raises(TF): cr.has_nrows(state)

@pytest.mark.parametrize('stu, success', [
    ({}, False),
    ({'a': []}, False),
    ({'b': [1, 2]}, False),
    ({'a': [1], 'b': [4], 'c': [7]}, False),
    ({'a': [1, 2, 3], 'b': [4, 5, 6]}, True),
    ({'a': [1], 'b': [4]}, True),
    ({'c': [1], 'd': [4]}, True),
])
def test_has_ncols(stu, success):
    state = prepare_state({'a': [1,2,3], 'b': [4, 5, 6]}, stu)
    if success:
        passes(cr.has_ncols(state))
    else:
        with pytest.raises(TF): cr.has_ncols(state)

@pytest.mark.parametrize('stu, stu_sub, success', [
    ({}, None, False),
    ({'a': [1]}, None, False),
    ({'a': [1, 2]}, {'a': [2]}, True),
    ({'b': [1, 2]}, {'b': [2]}, True),
    ({'a': [1, 2], 'b': [3, 4]}, {'a': [2], 'b': [4]}, True),
    ({'a': [1, 2, 3], 'b': [4, 5, 6]}, {'a': [2], 'b': [5]}, True),
])
def test_check_row(stu, stu_sub, success):
    state = prepare_state({'a': [1, 2, 3], 'b': [4, 5, 6]}, stu)
    if success:
        x = cr.check_row(state, 1)
        passes(x)
        assert x.solution_result == {'a': [2], 'b': [5]}
        assert x.student_result == stu_sub
    else:
        with pytest.raises(TF): cr.check_row(state, 1)

def test_check_row_wrong_usage():
    state = prepare_state({'a': [1]}, {'a': [1]})
    with pytest.raises(BaseException):
        cr.check_row(state, 1)

@pytest.mark.parametrize('stu, stu_sub, success', [
    ({}, None, False),
    ({'b': []}, None, False),
    ({'A': [1]}, None, False),
    ({'a': []}, {'a': []}, True),
    ({'a': [1]}, {'a': [1]}, True),
    ({'a': [1], 'b': [2]}, {'a': [1]}, True)
])
def test_check_col(stu, stu_sub, success):
    state = prepare_state({'a': [1]}, stu)
    if success:
        x = cr.check_col(state, 'a')
        passes(x)
        assert x.solution_result == {'a': [1]}
        assert x.student_result == stu_sub
    else:
        with pytest.raises(TF): cr.check_col(state, 'a')

def test_check_col_wrong_usage():
    state = prepare_state({'a': [1]}, {'a': [1]})
    with pytest.raises(BaseException):
        cr.check_col(state, 'b')

@pytest.mark.parametrize('stu, stu_sub, success', [
    ({}, None, False),
    ({'a': [1]}, None, False),
    ({'A': [1], 'b': [2]}, None, False),
    ({'a': [1], 'b': [2]}, {'a': [1], 'b': [2]}, True),
    ({'a': [4], 'b': [5]}, {'a': [4], 'b': [5]}, True),
    ({'a': [1], 'b': [2], 'c': [3]}, {'a': [1], 'b': [2]}, True),
])
def test_check_solution_cols(stu, stu_sub, success):
    state = prepare_state({'a': [1], 'b': [2]}, stu)
    if success:
        x = cr.check_solution_cols(state)
        passes(x)
        assert x.solution_result == {'a': [1], 'b': [2]}
        assert x.student_result == stu_sub
    else:
        with pytest.raises(TF): cr.check_solution_cols(state)

@pytest.mark.parametrize('stu, success', [
    ({'a': [1], 'b': [2]}, True),
    ({'a': [4], 'b': [5]}, True),
    ({'A': [1], 'b': [2]}, False)
])
def test_check_solution_cols_stricter(stu, success):
    state = prepare_state({'a': [1], 'b': [2]}, stu)
    if success:
        passes(cr.check_solution_cols(state, allow_extra_cols=False))
    else:
        with pytest.raises(TF): cr.check_solution_cols(state, allow_extra_cols=False)

@pytest.mark.parametrize('stu, success', [
    ({'a': [1]}, False),
    ({'a': [1, 1]}, False),
    ({'a': [1.11, 1]}, False),
    ({'a': [1, 2]}, True),
    ({'a': [2, 1]}, True),
    ({'a': [1, 2], 'b': [5, 6]}, True),
])
def test_is_equal_basic(stu, success):
    state = prepare_state({'a': [1, 2], 'b': [3, 4]}, stu)
    child = cr.check_col(state, 'a')
    if success:
        passes(cr.is_equal(child))
    else:
        with pytest.raises(TF):
            cr.is_equal(child)

@pytest.mark.parametrize('stu, success', [
    ({'a': [1]}, False),
    ({'a': [1, 1]}, False),
    ({'a': [1, 2]}, True),
    ({'a': [2, 1]}, False),
    ({'a': [1, 2], 'b': [5, 6]}, True),
])
def test_is_equal_ordered(stu, success):
    state = prepare_state({'a': [1, 2], 'b': [3, 4]}, stu)
    child = cr.check_col(state, 'a')
    if success:
        passes(cr.is_equal(child, ordered=True))
    else:
        with pytest.raises(TF):
            cr.is_equal(child, ordered=True)

@pytest.mark.parametrize('stu, success', [
    ({'a': [1.131]}, False),
    ({'a': ['abc']}, False),
    ({'a': [1.121]}, True),
])
def test_is_equal_ndigits(stu, success):
    state = prepare_state({'a': [1.124]}, stu)
    child = cr.check_col(state, 'a')
    if success:
        passes(cr.is_equal(child, ndigits = 2))
    else:
        with pytest.raises(TF):
            cr.is_equal(child, ndigits = 2)

def test_is_equal_wrong_usage():
    state = prepare_state({}, {})
    with pytest.raises(ValueError):
        cr.is_equal(state)

@pytest.mark.parametrize('sol_result,stu_result', [
    ( {'a': [2, 2, 1], 'b': [2, 1, 1]}, {'a': [2, 2, 1], 'b': [1, 2, 1]} ),
    ( {'a': [None, 2, 1], 'b': [2, 1, 1]},     {'a': [2, None, 1], 'b': [1, 2, 1]} ),
    ( {'a': [2, None, 1], 'b': [2, 1, 1]},     {'a': [None, 2, 1], 'b': [1, 2, 1]} ),
    ( {'a': [None, 'a', 'b'], 'b': [2, 1, 1]}, {'a': ['a', None, 'b'], 'b': [1, 2, 1]} ),
    ( {'a': [2, 2, 1], 'b': [2, 1, 1]}, {'a': [2, 2, 1], 'b': [1, 2, 1], 'c': [0, 0, 0]} ),
    ])
def test_sort_rows_pass(sol_result, stu_result):
    state = prepare_state(sol_result, stu_result)
    stu, sol = cr.sort_rows(state)
    assert all(k in sol for k in state.solution_result)
    assert all(k in stu for k in state.student_result)
    if 'a' in state.solution_result and 'a' in state.student_result: 
        assert sol['a'] == stu['a']

def test_lower_case():
    state = prepare_state({'a': [1]}, {'A': [1]})

    # fails if not using lowercase
    with pytest.raises(TF):
        cr.check_col(state, 'a')
    
    # passes if lowercase is being used
    child = cr.lowercase(state)
    child2 = cr.check_col(child, 'a')
    passes(child2)
    passes(cr.is_equal(child2))

@pytest.mark.parametrize('stu, success', [
    ({'a': [1]}, False),
    ({'a': [1, 1]}, False),
    ({'a': [1, 2]}, False),
    ({'a': [1, 2], 'b': [5, 6]}, False),
    ({'a': [1, 2, 3], 'b': [3, 4, 5]}, False),
    ({'a': [1, 2], 'b': [3, 4]}, True),
    ({'a': [1, 2], 'B': [3, 4]}, True),
    ({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}, True),
])
def test_check_result(stu, success):
    state = prepare_state({'a': [1, 2], 'b': [3, 4]}, stu)
    if success:
        passes(cr.check_result(state))
    else:
        with pytest.raises(TF):
            cr.check_result(state)
