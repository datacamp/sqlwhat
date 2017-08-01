from protowhat.Test import TestFail
from types import GeneratorType
from functools import partial

def fail(state, msg=""):
    """Always fails the SCT, with an optional msg."""
    state.do_test(msg)

    return state

def multi(state, *args):
    """Run multiple subtests. Return original state (for chaining).

    Args:
        state: State instance describing student and solution code. Can be omitted if used with Ex().
        args: one or more sub-SCTs to run.

    
    :Example:
        The SCT below runs run two test_student_typed cases.. ::

            Ex().multi(test_student_typed('SELECT'), test_student_typed('WHERE'))

        The SCT below checks that a SELECT statement has both a WHERE and LIMIT clause.. ::

            Ex().check_node('SelectStmt', 0) \
                .multi(check_field('where_clause'), check_field('limit_clause'))

    :Note:
        This function could be thought as an AND statement, since all tests it runs must pass

    """

    for arg in args:
        # when input is a single test, make iterable
        if callable(arg): arg = [arg]

        for test in arg:
            # assume test is function needing a state argument
            # partial state so reporter can test
            closure = partial(test, state)
            state.do_test(closure)

    # return original state, so can be chained
    return state

def extend(state, *args):
    for arg in args:
        # when input is a single test, make iterable
        if callable(arg): arg = [arg]

        for test in arg:
            # update state to be output of current test
            state = test(state)

    # return original state, so can be chained
    return state

def test_or(state, *tests):
    """Test whether at least one SCT passes.
    
    Args:
        state: State instance describing student and solution code. Can be omitted if used with Ex().
        tests: one or more sub-SCTs to run.

    :Example:
        The SCT below tests that the student typed either 'SELECT' or 'WHERE' (or both).. ::

            Ex().test_or(test_student_typed('SELECT'), test_student_typed('WHERE'))

        The SCT below checks that a SELECT statement has at least a WHERE or LIMIT clause.. ::

            Ex().check_node('SelectStmt', 0) \
                .test_or(check_field('where_clause'), check_field('limit_clause'))
    """

    rep = state.reporter

    success = False
    first_feedback = None
    for test in tests: 
        try: 
            multi(state, test)
            success = True
        except TestFail as e:
            if not first_feedback: first_feedback = rep.feedback
            rep.failed_test = False

        if success: 
            return
    
    rep.failed_test = True
    rep.feedback = first_feedback
    raise TestFail

def test_correct(state, check, diagnose):
    """Allows feedback from a diagnostic SCT, only if a check SCT fails. 

    Args:
        state: State instance describing student and solution code. Can be omitted if used with Ex().
        check: An sct (or list of SCTs) that must succeed.
        diagnose: An sct (or list of SCTs) to run if the check fails.

    :Example:
        The SCT below tests whether students query result is correct, before running diagnostic SCTs.. ::

            Ex().test_correct(check_result(), [
                    test_error("some message about an error"),
                    check_node('SelectStmt', missing_msg = "Did you forget your Select statement?")
                    ])

    """

    def diagnose_and_check(state):
        # use multi twice, since diagnose and check may be lists of tests
        multi(state, diagnose, check)

    test_or(state, diagnose_and_check, check)
