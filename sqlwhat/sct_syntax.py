# Wrap SCT checks -------------------------------------------------------------

from sqlwhat.State import State
from sqlwhat import checks
from protowhat.sct_syntax import get_checks_dict, create_sct_context

# used in Chain and F, to know what methods are available
sct_dict = get_checks_dict(checks)
SCT_CTX = create_sct_context(State, sct_dict)

# used in test_exercise, so that scts without Ex() don't run immediately
globals().update(SCT_CTX)

# put on module for easy importing
__all__ = list(SCT_CTX.keys())
