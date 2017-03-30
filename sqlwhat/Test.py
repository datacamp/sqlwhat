import re
import _ast

class Feedback(object):

   def __init__(self, message, astobj = None, strict=False):
        self.message = message
        self.line_info = {}
        try:
            if astobj is not None:
                self.line_info = astobj._get_pos()
        except Exception as e:
            if strict: raise e

class TestFail(Exception):
    pass

class Test(object):
    """
    The basic Test. It should only contain a failure message, as all tests should result in
    a failure message when they fail.

    Note:
        This test should not be used by itself, subclasses should be used.

    Attributes:
        feedback (str): A string containing the failure message in case the test fails.
        result (bool): True if the test succeed, False if it failed. None if it hasn't been tested yet.
    """

    def __init__(self, feedback):
        """
        Initialize the standard test.

        Args:
            feedback: string or Feedback object
        """
        if (issubclass(type(feedback), Feedback)):
            self.feedback = feedback
        elif (issubclass(type(feedback), str)):
            self.feedback = Feedback(feedback)
        else:
           raise TypeError("When creating a test, specify either a string or a Feedback object")

        self.result = None

    def test(self):
        """
        Wrapper around specific tests. Tests only get one chance.
        """
        if self.result is None:
            try:
                self.specific_test()
                self.result = np.array(self.result).all()
            except:
                self.result = False

    def specific_test(self):
        """
        Perform the actual test. For the standard test, result will be set to False.
        """
        self.result = False

    def get_feedback(self):
        return(self.feedback)
