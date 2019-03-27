import tests.helper as helper
import pytest
import os

db_path = os.path.join(os.path.dirname(__file__), "create_sqlite_db.py")


@pytest.fixture
def pec():
    return open(db_path).read()


@pytest.mark.backend
@pytest.mark.parametrize(
    "stu_code, passes",
    [
        ("SELECT * FROM company", True),
        ("SELECT id FROM company", False),
        ("SELECT * FROM company WHERE id > 1", False),
    ],
)
def test_check_result_fail(pec, stu_code, passes):
    sct_payload = helper.run(
        {
            "DC_PEC": pec,
            "DC_SOLUTION": "SELECT * FROM company",
            "DC_CODE": stu_code,
            "DC_SCT": "Ex().check_result()",
        }
    )
    assert sct_payload.get("correct") == passes


@pytest.mark.backend
@pytest.mark.parametrize(
    "stu_code, passes",
    [
        ("SELECT id, NAME as name FROM company WHERE id > 1", True),
        (
            "SELECT id, NAME as name FROM company WHERE id = 3",
            True,
        ),  # where exists, even if different
        ("SELECT id, NAME as name FROM company2", False),
    ],
)
def test_ex_check_edge_pass(pec, stu_code, passes):
    sct_payload = helper.run(
        {
            "DC_PEC": pec,
            "DC_SOLUTION": "SELECT * FROM company WHERE id > 1",
            "DC_CODE": stu_code,
            "DC_SCT": "Ex().check_node('SelectStmt', 0).check_edge('where_clause')",
        }
    )
    assert sct_payload.get("correct") == passes


@pytest.mark.backend
def test_ex_check_edge_has_equal_ast_fail(pec):
    sct_payload = helper.run(
        {
            "DC_PEC": pec,
            "DC_SOLUTION": "SELECT * FROM company WHERE id > 1",
            "DC_CODE": "SELECT id, NAME as name FROM company2 WHERE id = 3",
            "DC_SCT": "Ex().check_node('SelectStmt', 0).check_edge('where_clause').has_equal_ast()",
        }
    )

    assert sct_payload.get("correct") is False


# Tests for check_query (which needs the backend...) --------------------------


@pytest.mark.backend
@pytest.mark.parametrize(
    "stu, passes",
    [
        ("", False),
        ("INSERT INTO company VALUES (2, 'filip', 28, 'sql-lane', 42)", True),
        (
            "INSERT INTO company VALUES (2, 'filip', 28, 'sql-lane', 42), (3, 'machow', 27, 'sql-lan', 42)",
            False,
        ),
    ],
)
def test_ex_check_query(pec, stu, passes):
    sct_payload = helper.run(
        {
            "DC_PEC": pec,
            "DC_CODE": stu,
            "DC_SOLUTION": "INSERT INTO company VALUES (2, 'filip', 28, 'sql-lane', 42)",
            "DC_SCT": "Ex().check_query(query = 'SELECT COUNT(*) AS c FROM company').has_equal_value()",
        }
    )
    assert sct_payload.get("correct") == passes
    target = "The autograder verified the result of running <code>SELECT COUNT(*) AS c FROM company</code> against the database. Column <code>c</code> seems to be incorrect."
    if not passes:
        assert sct_payload.get("message") == target


@pytest.mark.backend
@pytest.mark.parametrize(
    "query, patt",
    [
        ("SELECT", "SELECT"),
        ("SELECT * FROM nonexisting", r"SELECT \* FROM nonexisting"),
    ],
)
def test_ex_check_query_wrong_usage(pec, query, patt):
    with pytest.raises(
        Exception,
        match=r"Solution failed: Running `%s` after your submission generated an error\."
        % patt,
    ):
        helper.run(
            {
                "DC_PEC": pec,
                "DC_SCT": "Ex().check_query(query = '%s')" % query,
                "DC_CODE": "",
                "DC_SOLUTION": "",
            }
        )
