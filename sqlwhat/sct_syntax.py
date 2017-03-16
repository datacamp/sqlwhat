from sqlwhat.State import State
import copy
from functools import wraps, reduce

def state_dec(f):
    """Decorate check_* functions to return F chain if no state passed"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        state = kwargs.get('state', args[0] if len(args) else None)
        if isinstance(state, State):
            return f(*args, **kwargs)
        else:
            return F._from_func(f, *args, **kwargs)
    
    return wrapper

class Chain:
    def __init__(self, state):
        self._state = state
        self._crnt_sct = None
        self._waiting_on_call = False

    def __getattr__(self, attr):
        if attr not in ATTR_SCTS: raise AttributeError("No SCT named %s"%attr)
        elif self._waiting_on_call: 
            raise AttributeError("Did you forget to call a statement? "
                                 "e.g. Ex().check_list_comp.check_body()")
        else:
            # make a copy to return, 
            # in case someone does: a = chain.a; b = chain.b
            chain = copy.copy(self)
            chain._crnt_sct = ATTR_SCTS[attr]
            chain._waiting_on_call = True
            return chain

    def __call__(self, *args, **kwargs):
        # NOTE: the only change from python what is that state is now 1st pos arg below
        self._state = self._crnt_sct(self._state, *args, **kwargs)
        self._waiting_on_call = False
        return self


class F(Chain):
    def __init__(self, stack = None):
        self._crnt_sct = None
        self._stack = [] if stack is None else stack
        self._waiting_on_call = False

    def __call__(self, *args, **kwargs):
        if not self._crnt_sct:
            state = kwargs.get('state') or args[0]
            return reduce(lambda s, cd: self._call_from_data(*cd, state=s), self._stack, state)
        else:
            call_data = (self._crnt_sct, args, kwargs)
            return self.__class__(self._stack + [call_args])
    
    @staticmethod
    def _call_from_data(f, args, kwargs, state):
        return f(state, *args, **kwargs)

    @classmethod
    def _from_func(cls, f, *args, **kwargs):
        func_chain = cls()
        func_chain._stack.append([f, args, kwargs])
        return func_chain


def Ex(state=None):
    """Returns the current code state as a Chain instance.

    Args:
        state: a State instance, which contains the student/solution code and results.

    This allows SCTs to be run without including their 1st argument, ``state``.

    Note:
        When writing SCTs on DataCamp, no State argument to ``Ex`` is necessary.
        The exercise State is built for you.

    :Example:
    
        ::
            
            # life without Ex
            state = SomeStateProducingFunction()
            test_student_typed(state, text="SELECT id")    # some SCT, w/state as first arg

            # life with Ex
            state = SomeStateProducingFunction()
            Ex(state).test_student_typed(text="SELECT id")      # some SCT, w/o state as arg

            # life writing SCTs on DataCamp.com
            Ex().test_student_typed(text="SELECT id")
            
    """
    return Chain(state or State.root_state)

# Wrap SCT checks -------------------------------------------------------------
from sqlwhat import checks
import builtins

# used in Chain and F, to know what methods are available
ATTR_SCTS = {k: v for k,v in vars(checks).items() if k not in builtins.__dict__ if not k.startswith('__')}
# used in test_exercise, so that scts without Ex() don't run immediately
SCT_CTX = {k: state_dec(v) for k,v in ATTR_SCTS.items()}
SCT_CTX['Ex'] = Ex
SCT_CTX['F'] = F
