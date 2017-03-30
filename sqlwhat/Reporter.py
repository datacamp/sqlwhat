import re
import markdown2
from sqlwhat.Test import TestFail, Test, Feedback

"""
This file holds the reporter class.
"""

class Reporter(object):
    """Do reporting.

    This class holds the feedback- or success message and tracks whether there are failed tests
    or not. All tests are executed trough do_test() in the Reporter.
    """
    active_reporter = None

    def __init__(self, output = []):
        self.failed_test = False
        self.feedback = Feedback("Oh no, your solution is incorrect! Please, try again.")
        self.success_msg = "Great work!"
        self.errors_allowed = False
        self.output = output

        self.raise_ast_pos_errors = False

    def set_tag(self, *args, **kwargs): pass

    def do_test(self, testobj, highlight=None):
        """Do test.

        Execute a given test, unless some previous test has failed. If the test has failed,
        the state of the reporter changes and the feedback is kept.
        """

        if isinstance(testobj, Test):
            testobj.test()
            result = testobj.result
            if (not result):
                self.failed_test = True
                self.feedback = testobj.get_feedback()

                if highlight: 
                    self.feedback = Feedback(self.feedback.message, highlight)

                raise TestFail

        else: 
            result = None
            testobj()    # run function for side effects

        return result

    def get_error(self):
        # each entry of output should be a dict of form, type: 'error', payload: 'somepayload'
        return self.output[-1].get('payload') if self.output else None  # get last error

    @staticmethod
    def formatted_line_info(line_info):
        cpy = {**line_info}
        for k in ['column_start', 'column_end']:
            if k in cpy: cpy[k] += 1
        return cpy


    def build_payload(self, error=None):
        error = self.get_error() if not error else error

        if (error is not None and not self.failed_test and not self.errors_allowed):
            feedback_msg = "Your code contains an error: `%s`" % str(error)
            return {
                "correct": False,
                "message": Reporter.to_html(feedback_msg)
                }

        if self.failed_test:
            return {
                "correct": False,
                "message": Reporter.to_html(self.feedback.message),
                **self.formatted_line_info(self.feedback.line_info)
                }
            
        else:
            return {
                "correct": True,
                "message": Reporter.to_html(self.success_msg)
                }

    @staticmethod
    def to_html(msg):
        return(re.sub("<p>(.*)</p>", "\\1", markdown2.markdown(msg)).strip())

