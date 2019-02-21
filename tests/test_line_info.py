from protowhat.Test import Feedback, TestFail as TF
from protowhat.Reporter import Reporter
from protowhat.selectors import Dispatcher
from sqlwhat.State import State, PARSER_MODULES
from antlr_tsql import ast
import pytest

pos_names = ["line_start", "column_start", "line_end", "column_end"]


@pytest.mark.parametrize(
    "sql_cmd,start,pos",
    [
        # pos is 4-tuple (line_start, column_start, line_end, column_end)
        ("SELECT x FROM y", "tsql_file", [1, 1, 1, 15]),
        ("SELECT x FROM yy", "tsql_file", [1, 1, 1, 16]),
        (" SELECT x FROM y", "tsql_file", [1, 2, 1, 16]),
        ("\nSELECT x FROM y", "tsql_file", [2, 1, 2, 15]),
        ("\nSELECT x FROM y\nSELECT a FROM b", "tsql_file", [2, 1, 3, 15]),
    ],
)
def test_line_info(sql_cmd, start, pos):
    state = State(
        sql_cmd,
        "",
        "",
        None,
        None,
        {},
        {},
        Reporter(),
        ast_dispatcher=Dispatcher.from_module(PARSER_MODULES["mssql"]),
    )
    try:
        state.do_test("failure message")
    except TF as tf:
        for ii, k in enumerate(pos_names):
            assert tf.payload[k] == pos[ii]
