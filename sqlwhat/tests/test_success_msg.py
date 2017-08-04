from sqlwhat.checks import success_msg
from sqlwhat.checks.check_logic import fail
from sqlwhat.sct_syntax import Ex
from sqlwhat.State import State
from protowhat.Reporter import Reporter
from protowhat.Test import TestFail as TF
import pytest

def prepare_state(student_code):
    return State(
        student_code = "",
        reporter = Reporter(),
        # args below should be ignored
        solution_code = "NA", pre_exercise_code = "NA", 
        solution_ast = "NA", student_ast = "NA",
        student_result = [], solution_result = [],
        student_conn = None, solution_conn = None,
        ast_dispatcher = "NA")

def test_success_msg_pass():
    state = prepare_state("")
    success_msg(state, "NEW SUCCESS MSG")

    sct_payload = state.reporter.build_payload()
    assert sct_payload['correct'] == True
    assert sct_payload['message'] == "NEW SUCCESS MSG"

def test_success_msg_fail():
    state = prepare_state("")
    child = success_msg(state, "NEW SUCCESS MSG")
    with pytest.raises(TF):
        fail(child)

    sct_payload = state.reporter.build_payload()
    assert sct_payload['message'] != "NEW SUCCESS MSG"

def test_success_msg_pass_ex():
    state = prepare_state("")
    Ex(state).success_msg("NEW SUCCESS MSG")

    sct_payload = state.reporter.build_payload()
    assert sct_payload['correct'] == True
    assert sct_payload['message'] == "NEW SUCCESS MSG"
