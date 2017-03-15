from copy import copy
import inspect

from sqlwhat.selectors import Dispatcher

class State:
    def __init__(self,
                 student_code,
                 solution_code,
                 pre_exercise_code,
                 student_conn,
                 solution_conn,
                 student_result,
                 solution_result,
                 reporter,
                 solution_ast = None,
                 student_ast = None,
                 ast_dispatcher = None):

        for k,v in locals().items():
            if k != 'self': setattr(self, k, v)

        if ast_dispatcher is None: self.ast_dispatcher = Dispatcher.from_dialect(student_conn.dialect.name)

        # Parse solution and student code
        # solution code raises an exception if can't be parsed
        if solution_ast is None: self.solution_ast = self.ast_dispatcher.parse(solution_code)
        if student_ast  is None: self.student_ast  = self.ast_dispatcher.parse(student_code)

    def to_child(self, **kwargs):
        """Basic implementation of returning a child state"""

        good_pars = inspect.signature(self.__init__).parameters
        bad_pars = set(kwargs) - set(good_pars)
        if bad_pars:
            raise KeyError("Invalid init params for State: %s"% ", ".join(bad_pars))

        child = copy(self)
        for k, v in kwargs.items(): setattr(child, k, v)
        child.parent = self
        return child

