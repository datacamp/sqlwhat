from protowhat.failure import Failure, InstructorError
from protowhat.Reporter import Reporter
from protowhat.sct_context import create_sct_context, get_checks_dict

from sqlwhat import checks
from sqlwhat.State import State


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

    try:
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

        # the available SCT methods
        sct_dict = get_checks_dict(checks)

        # the available global variables
        sct_context = create_sct_context(sct_dict, state)

        exec(sct, sct_context)

    except Failure as e:
        if isinstance(e, InstructorError):
            # TODO: decide based on context
            raise e
        return reporter.build_failed_payload(e.feedback)

    return reporter.build_final_payload()
