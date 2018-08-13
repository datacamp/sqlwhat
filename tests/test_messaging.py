import importlib
import pytest

cr = importlib.import_module('sqlwhat.checks.check_funcs')
from protowhat.selectors import Dispatcher
from sqlwhat.State import State, PARSER_MODULES
from protowhat.Reporter import Reporter
from protowhat.Test import TestFail as TF
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

def test_has_result():
    state = prepare_state({'a': [1,2,3]}, {})
    with pytest.raises(TF, match = 'Your query did not return a result.'):
        cr.has_result(state)

# Check funcs -----------------------------------------------------------------

@pytest.mark.parametrize('stu, patt', [
    ({'a': [1]}, '1 row'),
    ({'a': [1, 2]}, '2 rows'),
])
def test_has_nrows(stu, patt):
    state = prepare_state({'a': [1,2,3]}, stu)
    with pytest.raises(TF, match = "Your query returned a table with {} while it should return a table with 3 rows.".format(patt)):
        cr.has_nrows(state)

@pytest.mark.parametrize('stu, patt', [
    ({'a': [1]}, '1 column'),
    ({'a': [1], 'b': [1], 'c': [1]}, '3 columns'),
])
def test_has_ncols(stu, patt):
    state = prepare_state({'a': [1], 'b': [1]}, stu)
    with pytest.raises(TF, match = "Your query returned a table with {} while it should return a table with 2 columns.".format(patt)):
        cr.has_ncols(state)

@pytest.mark.parametrize('stu, patt', [
    ({'a': [1]}, "The system wants to verify row 2 of your query result, but couldn't find it. Have another look."),
    ({'a': [1, 3]}, "Have another look at row 2 in your query result. Column `a` seems to be incorrect.")
])
def test_check_row(stu, patt):
    state = prepare_state({'a': [1, 2] }, stu)
    with pytest.raises(TF, match = patt):
        ss = cr.check_row(state, 1)
        cr.is_equal(ss)

@pytest.mark.parametrize('stu, patt', [
    ({'b': [2]}, "We expected to find a column named `a` in the result of your query, but couldn't."),
    ({'a': [2]}, r"Have another look at your query result\. Column `a` seems to be incorrect\.$"),
])
def test_check_col(stu, patt):
    state = prepare_state({'a': [1] }, stu)
    with pytest.raises(TF, match = patt):
        ss = cr.check_col(state, 'a')
        cr.is_equal(ss)

@pytest.mark.parametrize('stu, patt', [
    ({'b': [2]}, "We expected to find a column named `a` in the result of your query, but couldn't."),
    ({'a': [2], 'b': [1]}, "Your query result contains the column `b` but shouldn't."),
    ({'a': [2]}, r"Have another look at your query result\. Column `a` seems to be incorrect\.$"),
])
def test_check_solution_cols(stu, patt):
    state = prepare_state({'a': [1] }, stu)
    with pytest.raises(TF, match = patt):
        ss = cr.check_solution_cols(state, allow_extra_cols=False)
        cr.is_equal(ss)

def test_is_equal():
    state = prepare_state({'a': [1, 2]}, {'a': [2, 1]})
    with pytest.raises(TF, match = "Have another look at your query result. Column `a` seems to be incorrect. Make sure you arranged the rows correctly."):
        cr.is_equal(cr.check_col(state, 'a'), ordered=True)
