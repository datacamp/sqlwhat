from copy import copy
import inspect

from protowhat.selectors import Dispatcher
from protowhat.State import State as BaseState
from protowhat.State import DummyParser
from functools import wraps

PARSER_MODULES = {
    'postgresql': 'antlr_plsql.ast',
    'sqlite': 'antlr_plsql.ast', # uses postgres parser for now
    'mssql': 'antlr_tsql.ast'
}

def lower_case(f):
    """Decorator specifically for turning mssql AST into lowercase"""
    # if it has already been wrapped, we return original
    if hasattr(f, 'lower_cased'): return f

    @wraps(f)
    def wrapper(*args, **kwargs):
        f.lower_cased = True
        return f(*args, **kwargs).lower()
    return wrapper

class State(BaseState):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_dispatcher(self):
        if not self.student_conn:
            return DummyParser()

        dialect = self.student_conn.dialect.name
        ast_dispatcher = Dispatcher.from_module(PARSER_MODULES[dialect])
        
        # TODO: the code below monkney patches the mssql ast to use only lowercase
        #       representations. This is because msft server has a setting to be
        #       case sensitive. However, this is often not the case, and probably
        #       detremental to DataCamp courses. Need to move to more sane configuration.
        if dialect == 'mssql':
            AstNode = ast_dispatcher.ast.AstNode
            AstNode.__repr__ = lower_case(AstNode.__repr__)

        return ast_dispatcher
