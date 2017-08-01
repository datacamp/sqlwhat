from protowhat.Test import Feedback, TestFail as TF, Test as _Test
from protowhat.Reporter import Reporter
from sqlwhat.State import State
from sqlwhat.selectors import Dispatcher
from antlr_tsql import ast
import pytest

def test_feedback_init_fail_strict():
    with pytest.raises(AttributeError):
        Feedback("MESSAGE", {}, strict=True)

@pytest.mark.parametrize('sql_cmd,start,pos', [
    # pos is 4-tuple (line_start, column_start, line_end, column_end)
    ("SELECT x FROM y", 'tsql_file', [1, 0, 1, 14]),
    ("SELECT x FROM yy", 'tsql_file', [1, 0, 1, 15]),
    (" SELECT x FROM y", 'tsql_file', [1, 1, 1, 15]),
    ("\nSELECT x FROM y", 'tsql_file', [2, 0, 2, 14]),
    ("\nSELECT x FROM y\nSELECT a FROM b", 'tsql_file', [2, 0, 3, 14])
    ])
def test_feedback_init(sql_cmd, start, pos):
    tree = ast.parse(sql_cmd, start)
    fb = Feedback("MESSAGE", tree, strict=True)
    pos_names = ['line_start', 'column_start', 'line_end', 'column_end']
    for ii, k in enumerate(pos_names):
        assert fb.line_info[k] == pos[ii]

def test_reporter_line_info_1_based_cols():
    rep = Reporter()
    rep.failed_test = True
    rep.feedback = Feedback("MESSAGE", ast.parse("\nSELECT x FROM y"))
    payload = rep.build_payload()
    pos = [2, 1, 2, 15]
    pos_names = ['line_start', 'column_start', 'line_end', 'column_end']
    for ii, k in enumerate(pos_names):
        assert payload[k] == pos[ii]

def test_state_line_info():
    state = State("\nSELECT x FROM y", "SELECT x FROM y", "", 
                  None, None,
                  {}, {},
                  Reporter(),
                  ast_dispatcher = Dispatcher.from_dialect('mssql'))
    
    with pytest.raises(TF):
        state.do_test(_Test("failure message"))

    payload = state.reporter.build_payload()

    pos = [2, 1, 2, 15]
    pos_names = ['line_start', 'column_start', 'line_end', 'column_end']
    for ii, k in enumerate(pos_names):
        assert payload[k] == pos[ii]
