from protowhat.Reporter import Reporter
from protowhat.sct_syntax import link_to_state

from sqlwhat.State import State
from sqlwhat.checks import (
    check_row,
    check_column,
    check_all_columns,
    check_result,
    lowercase,
    has_equal_value,
    has_no_error, has_result, has_nrows, has_ncols)

check_row = link_to_state(check_row)
check_column = link_to_state(check_column)
check_all_columns = link_to_state(check_all_columns)
check_result = link_to_state(check_result)
lowercase = link_to_state(lowercase)
has_equal_value = link_to_state(has_equal_value)


def get_sct_payload(output):
    output = [out for out in output if out["type"] == "sct"]
    if len(output) > 0:
        return output[0]["payload"]
    else:
        print(output)
        return None


class Connection:
    """Mock up conn.dialect.name"""

    def __init__(self, dialect_name):
        self.dialect = lambda: None
        self.dialect.name = dialect_name


def prepare_state(sol_result, stu_result, error=None):
    conn = Connection("postgresql")
    return State(
        student_code="",
        solution_code="",
        reporter=Reporter(errors=error),
        # args below should be ignored
        pre_exercise_code="NA",
        student_result=stu_result,
        solution_result=sol_result,
        student_conn=conn,
        solution_conn=None,
    )


def passes(x):
    assert isinstance(x, State)


has_no_error = link_to_state(has_no_error)
has_result = link_to_state(has_result)
has_nrows = link_to_state(has_nrows)
has_ncols = link_to_state(has_ncols)
