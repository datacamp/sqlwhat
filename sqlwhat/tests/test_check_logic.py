import pytest
from sqlwhat.State import State
from sqlwhat.checks import check_logic as cl
from protowhat.Reporter import Reporter
from protowhat.Test import TestFail as TF
from helper import Connection
from functools import partial

@pytest.fixture(scope="function")
def state():
    conn = Connection('postgresql')
    return State(
        student_code = "",
        solution_code = "",
        reporter = Reporter(),
        # args below should be ignored
        pre_exercise_code = "NA", 
        student_result = {'a': [1]}, solution_result = {'b': [2]},
        student_conn = conn, solution_conn = None)

def fails(state, msg=""): 
    state.reporter.feedback.msg = msg
    raise TF

def passes(state): return state

def childx(state): return state.to_child(student_code = state.student_code + 'x')

@pytest.mark.parametrize('arg1', ( passes, [passes, passes] ))
@pytest.mark.parametrize('arg2', ( passes, [passes, passes] ))
def test_test_multi_pass_one(state, arg1, arg2):
    cl.multi(state, arg1, arg2)

@pytest.mark.parametrize('arg1', ( fails, [passes, fails] ))
def test_test_multi_fail_arg1(state, arg1):
    with pytest.raises(TF): cl.multi(state, arg1)

@pytest.mark.parametrize('arg2', ( fails, [passes, fails] ))
def test_test_multi_fail_arg2(state, arg2):
    with pytest.raises(TF): cl.multi(state, passes, arg2)

@pytest.mark.parametrize('sct,stu_code,is_star_args', [
    (childx, 'x', False),
    ([childx, childx], 'xx', False),
    ([childx, childx], 'xx', True),
    ([[childx, childx], childx], 'xxx', True)
    ])
def test_extend(state, sct, stu_code, is_star_args):
    child = cl.extend(state, sct) if not is_star_args else cl.extend(state, *sct)
    assert child.student_code == stu_code

def test_extend_fail(state):
    with pytest.raises(TF): cl.extend(state, childx, lambda state: cl.fail(state))

def test_test_or_pass(state):
    cl.test_or(state, passes, fails)

def test_test_or_fail(state):
    with pytest.raises(TF): cl.test_or(state, fails, fails)

def test_test_correct_pass(state):
    cl.test_correct(state, passes, fails)

def test_test_correct_fail_msg(state):
    f1, f2 = partial(fails, msg="f1"), partial(fails, msg="f2")
    with pytest.raises(TF): 
        cl.test_correct(state, f1, f2)
        assert state.reporter.feedback.message == "f2"

def test_test_correct_fail_multi_msg(state):
    f1, f2, f3 = [partial(fails, msg="f%s"%ii) for ii in range(1, 4)]
    with pytest.raises(TF): 
        cl.test_correct(state, [f1, f3], [f2, f3])
        assert state.reporter.feedback.message == "f2"
