from unittest.mock import MagicMock

from sqlwhat.sct_syntax import Ex
from sqlwhat.State import State
from protowhat.Reporter import Reporter
from protowhat.Test import TestFail as TF
from tests.helper import Connection
import pytest


@pytest.fixture(params=["postgresql", "mssql"])
def conn(request):
    return Connection(request.param)


def test_pass(conn):
    state = State(
        student_code="SELECT * FROM company",
        solution_code="SELECT * FROM company",
        pre_exercise_code="",
        student_result={"id": [1], "name": ["greg"]},
        solution_result={"id": [1], "name": ["greg"]},
        student_conn=conn,
        solution_conn=None,
        reporter=Reporter(),
    )

    Ex.root_state = state

    assert Ex().check_result()


def test_fail(conn):
    state = State(
        student_code="SELECT * FROM company",
        solution_code="SELECT * FROM company",
        pre_exercise_code="",
        student_result={"id": [1], "name": ["greg"]},
        solution_result={"id": [0], "name": ["greg"]},
        student_conn=conn,
        solution_conn=None,
        reporter=Reporter(),
    )

    Ex.root_state = state

    with pytest.raises(TF):
        Ex().check_result()


def test_multiple_state_init(conn):
    state1 = State(
        student_code="SELECT * FROM company",
        solution_code="SELECT * FROM company",
        pre_exercise_code="",
        student_result={"id": [1], "name": ["greg"]},
        solution_result={"id": [0], "name": ["greg"]},
        student_conn=conn,
        solution_conn=None,
        reporter=Reporter(),
    )

    state2 = State(
        student_code="SELECT * FROM company",
        solution_code="SELECT * FROM company",
        pre_exercise_code="",
        student_result={"id": [1], "name": ["greg"]},
        solution_result={"id": [0], "name": ["greg"]},
        student_conn=conn,
        solution_conn=None,
        reporter=Reporter(),
    )


def test_get_dispatcher_oracle():
    # Given
    conn2 = MagicMock()
    dialect = MagicMock()
    conn2.dialect = dialect
    dialect.name = "oracle"
    state = State(
        student_code="SELECT * FROM company",
        solution_code="SELECT * FROM company",
        pre_exercise_code="",
        student_result={"id": [1], "name": ["greg"]},
        solution_result={"id": [1], "name": ["greg"]},
        student_conn=conn2,
        solution_conn=None,
        reporter=Reporter(),
    )

    # When
    output = state.get_dispatcher()

    # Then
    assert output.ast_mod.grammar.__spec__.name == 'antlr_plsql.antlr_py'
