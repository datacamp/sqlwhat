from copy import copy
import inspect

from sqlwhat.selectors import Dispatcher
from protowhat.State import State as BaseState

class State(BaseState):

    def get_dispatcher(self):
        # MCE doesn't always have connection - fallback on postgresql
        dialect = self.student_conn.dialect.name if self.student_conn else 'postgresql'
        return Dispatcher.from_dialect(dialect)
