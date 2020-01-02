from sqlwhat.State import State
from protowhat.failure import TestFail, InstructorError
from protowhat.Reporter import Reporter
from sqlwhat.sct_syntax import SCT_CTX


def test_exercise(
    sct,
    student_code,
    student_result,
    student_conn,
    solution_code,
    solution_result,
    solution_conn,
    pre_exercise_code,
    ex_type,
    error,
    force_diagnose=False,
    debug=False,  # currently unused
):
    """
    """

    reporter = Reporter(errors=error)

    state = State(
        student_code=student_code,
        solution_code=solution_code,
        pre_exercise_code=pre_exercise_code,
        student_conn=student_conn,
        solution_conn=solution_conn,
        student_result=student_result,
        solution_result=solution_result,
        reporter=reporter,
        force_diagnose=force_diagnose,
    )

    SCT_CTX["Ex"].root_state = state

    try:
        exec(sct, SCT_CTX)
    except (TestFail, InstructorError) as e:
        if isinstance(e, InstructorError):
            # TODO: decide based on context
            raise e
        return reporter.build_failed_payload(e.feedback)

    return reporter.build_final_payload()
