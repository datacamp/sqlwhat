from sqlwhat.test_exercise import test_exercise as te
from helper import Connection
import pytest

@pytest.fixture
def conn():
    return Connection('postgresql')

def test_pass(conn):
    result = {'id': [1], 'name': ['greg']}
    sct_payload = te(
        sct = "Ex().check_result()",
        student_code = "SELECT * FROM company",
        solution_code = "SELECT * FROM company",
        pre_exercise_code = "",
        student_conn = conn,
        solution_conn = None,
        student_result = result,
        solution_result = result,
        ex_type="NormalExercise",
        error=[]
        )

    assert sct_payload.get('correct') is True

def test_fail(conn):
    sol_result = {'id': [1], 'name': ['greg']}
    stu_result = {'id': [1, 2], 'name': ['greg', 'fred']}
    sct_payload = te(
        sct = "Ex().check_result()",
        student_code = "SELECT * FROM company",
        solution_code = "SELECT * FROM company",
        pre_exercise_code = "",
        student_conn = conn,
        solution_conn = None,
        student_result = stu_result,
        solution_result = sol_result,
        ex_type="NormalExercise",
        error=[]
        )

    assert sct_payload.get('correct') is False

xfail_def = pytest.mark.xfail(reason="implement deferrel")

@pytest.mark.parametrize('sct', [
    "Ex().check_node('SelectStmt')",
    "Ex().check_node('SelectStmt', priority=99)",
    "Ex().check_node('SelectStmt').check_edge('target_list')",
    "Ex().has_code('SELECT')",
    "Ex().has_equal_ast()",
    "Ex().multi(has_code('SELECT'))",
    "Ex().check_or(has_code('SELECT'))",
    "Ex().check_correct(has_code('SELECT'), has_code('SEL'))",
    "Ex().check_correct(has_code('SELECT'), has_code('SEL').has_code('SEL'))",
    "Ex().check_not(has_code('WHERE'), incorrect_msg='do not write WHERE')",
    "Ex().has_result()",
    "Ex().has_nrows()",
    "Ex().has_ncols()",
    "Ex().check_column('id')",
    "Ex().check_column('id').has_equal_value()"
])
def test_test_exercise_pass(conn, sct):
    result = {'id': [1], 'name': ['greg']}
    sct_payload = te(
        sct = sct,
        student_code = "SELECT * FROM company",
        solution_code = "SELECT * FROM company",
        pre_exercise_code = "",
        student_conn = conn,
        solution_conn = None,
        student_result =  result,
        solution_result = result,
        ex_type="NormalExercise",
        error=[]
        )

    assert sct_payload.get('correct') is True

@pytest.mark.parametrize('sct', [
    "Ex().check_node('SelectStmt').check_edge('target_list').has_equal_ast()",
    "Ex().has_code('id', fixed=True)",
    "Ex().has_equal_ast()",
    "Ex().multi(has_code('id'))",
    "Ex().check_or(has_code('id'))",
    "Ex().check_correct(has_code('id'), has_code('i'))",
    "Ex().has_nrows()",
    "Ex().has_ncols()",
    "Ex().check_column('id')",
    "Ex().check_column('name').has_equal_value()",
])
def test_test_exercise_fail(conn, sct):
    sol_result = {'id': [1], 'name': ['greg']}
    stu_result = {'id2': [1, 2], 'name': ['greg', 'fred'], 'c': [1,2]}
    sct_payload = te(
        sct = sct,
        student_code = "SELECT * FROM company",
        solution_code = "SELECT id FROM company",
        pre_exercise_code = "",
        student_conn = conn,
        solution_conn = None,
        student_result = stu_result,
        solution_result = sol_result,
        ex_type="NormalExercise",
        error=[]
    )

    assert sct_payload.get('correct') is False

@pytest.mark.parametrize('sct, passes, msg', [
    ('', False, 'Your code generated an error. Fix it and try again!'),
    ('Ex().has_no_error(incorrect_msg="wow")', False, 'wow'),
    ('Ex().allow_error()', True, None)
])
def test_error_handling(sct, passes, msg):
    sct_payload = te(
        sct = sct,
        student_code = "",
        solution_code = "",
        pre_exercise_code = "",
        student_conn = None,
        solution_conn = None,
        student_result = {},
        solution_result = {},
        ex_type="NormalExercise",
        error=['an error']
    )

    assert sct_payload.get('correct') == passes
    if msg: assert sct_payload.get('message') == msg
