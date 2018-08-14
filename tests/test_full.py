import helper
import pytest
import os

db_path = os.path.join(os.path.dirname(__file__), 'create_sqlite_db.py')

@pytest.fixture
def pec():
    return open(db_path).read()

@pytest.mark.backend
@pytest.mark.parametrize('stu_code, passes', [
    ("SELECT * FROM company", True),
    ("SELECT id FROM company", False),
    ("SELECT * FROM company WHERE id > 1", False)
])
def test_check_result_fail(pec, stu_code, passes):
    sct_payload = helper.run({
        'DC_PEC': pec, 
        'DC_SOLUTION': "SELECT * FROM company",
        'DC_CODE': stu_code, 
        'DC_SCT': "Ex().check_result()"
    })
    assert sct_payload.get('correct') == passes

@pytest.mark.backend
@pytest.mark.parametrize('stu_code, passes', [
    ("SELECT id, NAME as name FROM company WHERE id > 1", True),
    ("SELECT id, NAME as name FROM company WHERE id = 3", True), # where exists, even if different
    ("SELECT id, NAME as name FROM company2", False)
])
def test_ex_check_edge_pass(pec, stu_code, passes):
    sct_payload = helper.run({
        'DC_PEC': pec, 
        'DC_SOLUTION': "SELECT * FROM company WHERE id > 1",
        'DC_CODE': stu_code,
        'DC_SCT': "Ex().check_node('SelectStmt', 0).check_edge('where_clause')"
    })
    assert sct_payload.get('correct') == passes

@pytest.mark.backend
def test_ex_check_edge_has_equal_ast_fail(pec):
    sct_payload = helper.run({
        'DC_PEC': pec, 
        'DC_SOLUTION': "SELECT * FROM company WHERE id > 1",
        'DC_CODE': "SELECT id, NAME as name FROM company2 WHERE id = 3",
        'DC_SCT': "Ex().check_node('SelectStmt', 0).check_edge('where_clause').has_equal_ast()"
        })

    assert sct_payload.get('correct') is False
