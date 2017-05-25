import pytest
from sqlwhat.State import State
import importlib
cr = importlib.import_module('sqlwhat.checks.check_result')
from sqlwhat.Reporter import Reporter
from sqlwhat.Test import TestFail as TF
from helper import Connection

def prepare_state(sol_result, stu_result):
    conn = Connection('postgresql')
    return State(
        student_code = "",
        solution_code = "",
        reporter = Reporter(),
        # args below should be ignored
        pre_exercise_code = "NA",
        student_result = stu_result, solution_result = sol_result,
        student_conn = conn, solution_conn = None)

def test_test_has_columns_fail():
    state = prepare_state({'a': [1,2,3]}, {})
    with pytest.raises(TF): cr.test_has_columns(state)

def test_test_has_columns_pass_no_rows():
    state = prepare_state({'a': [1,2,3]}, {'a': []})
    cr.test_has_columns(state)

def test_test_nrows_fail():
    state = prepare_state({'a': [1,2,3]}, {'b': [1,2]})
    with pytest.raises(TF): cr.test_nrows(state)

def test_test_ncols_pass():
    state = prepare_state({'a': [1,2,3]}, {'b': [1,2,3]})
    cr.test_nrows(state)

def test_test_ncols_fail():
    state = prepare_state({'a': [1], 'b': [1]}, {'c': [1]})
    with pytest.raises(TF): cr.test_ncols(state)

def test_test_ncols_pass():
    state = prepare_state({'a': [1], 'b': [1]}, {'c': [1], 'd': [1]})
    cr.test_ncols(state)

def test_test_name_miscased_pass():
    state = prepare_state({'A': [1], 'b': [1]}, {'A': [2], 'd': [2]})
    cr.test_name_miscased(state, 'A')

def test_test_name_miscased_fail():
    state = prepare_state({'A': [1], 'b': [1]}, {'a': [2], 'd': [2]})
    with pytest.raises(TF):
        cr.test_name_miscased(state, 'A')
    print(state.reporter.build_payload())

def test_test_column_name_pass():
    state = prepare_state({'A': [1], 'b': [1]}, {'a': [2], 'd': [2]})
    cr.test_column_name(state, 'A')

def test_test_column_name_fail():
    state = prepare_state({'A': [1], 'b': [1]}, {'d': [2]})
    with pytest.raises(TF):
        cr.test_column_name(state, 'A')

def test_test_column_digits():
    state = prepare_state({'a': [1.1]}, {'a': [1.11]})
    cr.test_column(state, 'a', digits = 1)

def test_test_column_digits_incompat_fail():
    state = prepare_state({'a': [1.1]}, {'a': ['abc']})
    with pytest.raises(TF): cr.test_column(state, 'a', digits = 1)

def test_test_column_digits_incompat_pass():
    state = prepare_state({'a': [1.1]}, {'a': ['abc'], 'b': [1.11]})
    cr.test_column(state, 'a', digits = 1, match = 'any')


@pytest.mark.parametrize('match, stu_result', [
    [ 'any', {'b': [1]} ],
    [ 'any', {'b': [1], 'a': [2]} ],
    [ 'exact', {'a': [1]} ],
    [ 'exact', {'A': [1]} ]
    ])
def test_test_column_pass(match, stu_result):
    state = prepare_state({'a': [1]}, stu_result)
    cr.test_column(state, 'a', match=match)

def test_test_column_pass_uppercase():
    state = prepare_state({'A': [1]}, {'a': [1]})
    cr.test_column(state, 'A', match='exact')

@pytest.mark.parametrize('match, stu_result', [
    ( 'any', {'a': [2]} ),                     # wrong value for a
    ( 'exact', {'b': [1], 'a': [2]} ),         # b is what a should be
    ( 'exact', {'a': [1.1]} )                  # no rounding
    ])
def test_test_column_fail(match, stu_result):
    state = prepare_state({'a': [1]}, stu_result)
    with pytest.raises(TF): cr.test_column(state, 'a', match=match)

# cases:
#   same num cols
#   extra cols in student - pass
#   extra cols in solution - fail due to test_column_name
#   different casing, same lowercase - pass
#   no student results
#   no solution results
@pytest.mark.parametrize('sol_result,stu_result', [
    ( {'a': [2, 2, 1], 'b': [2, 1, 1]}, {'a': [2, 2, 1], 'b': [1, 2, 1]} ),
    ( {'A': [2, 2, 1], 'b': [2, 1, 1]}, {'a': [2, 2, 1], 'b': [1, 2, 1]} ),
    ( {'a': [2, 2, 1], 'b': [2, 1, 1]}, {'A': [2, 2, 1], 'b': [1, 2, 1]} ),
    ( {'a': [None, 2, 1], 'b': [2, 1, 1]},     {'a': [2, None, 1], 'b': [1, 2, 1]} ),
    ( {'a': [2, None, 1], 'b': [2, 1, 1]},     {'a': [None, 2, 1], 'b': [1, 2, 1]} ),
    ( {'a': [None, 'a', 'b'], 'b': [2, 1, 1]}, {'a': ['a', None, 'b'], 'b': [1, 2, 1]} ),
    ( {'a': [2, 2, 1], 'b': [2, 1, 1]}, {'a': [2, 2, 1], 'b': [1, 2, 1], 'c': [0, 0, 0]} ),
    ( {},                               {'a': [2, 2, 1], 'b': [1, 2, 1]} ),
    ])
def test_sort_rows_pass(sol_result, stu_result):
    state = prepare_state(sol_result, stu_result)
    child = cr.sort_rows(state)
    print(child.solution_result)
    print(child.student_result)
    assert all(k in child.solution_result for k in state.solution_result)
    assert all(k in child.student_result for k in state.student_result)
    if 'a' in state.solution_result and 'a' in state.student_result: 
        assert child.solution_result['a'] == child.student_result['a']

    

@pytest.mark.parametrize('sol_result,stu_result', [
    ( {'a': [2, 2, 1], 'b': [2, 1, 1]}, {'b': [1, 2, 1]} ),
    ( {'a': [2, 2, 1], 'b': [2, 1, 1]}, {} ),
    ])
def test_sort_rows_fail(sol_result, stu_result):
    state = prepare_state(sol_result, stu_result)
    with pytest.raises(TF):
        cr.sort_rows(state)
