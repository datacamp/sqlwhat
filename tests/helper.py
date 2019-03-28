from protowhat.Reporter import Reporter

from sqlwhat.State import State


def get_sct_payload(output):
    output = [out for out in output if out["type"] == "sct"]
    if len(output) > 0:
        return output[0]["payload"]
    else:
        print(output)
        return None


def run(data):
    from sqlbackend.Exercise import Exercise

    exercise = Exercise(data)
    output = exercise.runInit()
    if "backend-error" in str(output):
        print(output)
        raise (ValueError("Backend error"))
    output = exercise.runSubmit(data)
    return get_sct_payload(output)


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
        reporter=Reporter(error),
        # args below should be ignored
        pre_exercise_code="NA",
        student_result=stu_result,
        solution_result=sol_result,
        student_conn=conn,
        solution_conn=None,
    )


def passes(x):
    assert isinstance(x, State)
