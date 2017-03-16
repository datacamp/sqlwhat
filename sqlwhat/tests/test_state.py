from sqlwhat.sct_syntax import Ex
from sqlwhat.State import State
from sqlwhat.Reporter import Reporter
from sqlwhat.Test import TestFail as TF
from helper import Connection
import pytest

@pytest.fixture(params = ['postgresql', 'mssql'])
def conn(request):
    return Connection(request.param)

def test_pass(conn):
    state = State(
        student_code = "SELECT * FROM company",
        solution_code = "SELECT * FROM company",
        pre_exercise_code = "",
        student_result =  {'id': [1], 'name': ['greg']},
        solution_result = {'id': [1], 'name': ['greg']},
        student_conn = Connection('postgresql'),
        solution_conn = None,
        reporter= Reporter())

    State.root_state = state

    assert Ex().check_result()

def test_fail(conn):
    state = State(
        student_code = "SELECT * FROM company",
        solution_code = "SELECT * FROM company",
        pre_exercise_code = "",
        student_result = {'id': [1], 'name': ['greg']},
        solution_result = {'id': [0], 'name': ['greg']},
        student_conn = Connection('postgresql'),
        solution_conn = None,
        reporter= Reporter())

    State.root_state = state

    with pytest.raises(TF):
        Ex().check_result()
