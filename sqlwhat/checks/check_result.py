from sqlwhat.Test import TestFail, Test

def allow_error(state):
    """Allow submission to pass, even if it originally caused a database error."""

    state.reporter.errors_allowed = True

    return state

def test_error(state, msg="Your command returned the following error: {}"):
    """Test whether submission caused a database error."""

    error = state.reporter.get_error()

    if error is not None:
        state.do_test(Test(msg.format(error)))

    return state

def check_result(state, msg="Incorrect result."):
    """High level function which wraps other SCTs for checking results."""

    stu_res = state.student_result
    sol_res = state.solution_result

    # empty test
    test_has_columns(state)
    # row test
    test_nrows(state)
    # column tests
    child = sort_rows(state)
    for k in sol_res:
        test_column_name(child, k)
        test_column(child, k)

    return state

def test_has_columns(state, msg="Your result did not output any columns."):
    """Test if the student's query result contains any columns"""

    if not state.student_result:
        state.do_test(Test(msg))

    return state

def test_nrows(state, msg="Result has {} row(s) but expected {}."):
    """Test whether the student and solution query results have equal numbers of rows.""" 

    stu_res = state.student_result
    sol_res = state.solution_result
    
    # assumes that columns cannot be jagged in size
    n_stu = len(next(iter(state.student_result.values())))
    n_sol = len(next(iter(state.solution_result.values())))

    if n_stu != n_sol:
        _msg = msg.format(n_stu, n_sol)
        state.do_test(Test(_msg))

    return state

def test_ncols(state, msg="Result has {} column(s) but expected {}."):
    """Test whether the student and solution query results have equal numbers of columns."""

    stu_res = state.student_result
    sol_res = state.solution_result
    
    n_stu = len(state.student_result)
    n_sol = len(state.solution_result)

    if n_stu != n_sol:
        _msg = msg.format(n_stu, n_sol)
        state.do_test(Test(_msg))

    return state

def test_name_miscased(state, name, 
                       msg="Check the name of column `{}`. It looks similar to column name `{}` in the result, but is not an exact match."):
    stu_res = state.student_result
    sol_res = state.solution_result

    if name not in sol_res:
        raise BaseException("name %s not in solution column names"%name)

    stu_lower = {k.lower() : k for k in stu_res.keys()}

    if name.lower() in stu_lower and name not in stu_res:
        _msg = msg.format(stu_lower[name.lower()], name)
        state.do_test(Test(_msg))

    return state

def test_column_name(state, name, 
                     msg="Make sure your results contain a column named `{}`. Case does not matter."):
    stu_res = state.student_result
    sol_res = state.solution_result

    if name not in sol_res:
        raise BaseException("name %s not in solution column names"%name)

    stu_lower = {k.lower() : k for k in stu_res.keys()}

    if name.lower() not in stu_lower:
        _msg = msg.format(name)
        state.do_test(Test(_msg))

    return state

def test_column(state, name, msg="Column `{}` in the solution does not have a column with the same name and values in your results.", 
                match = ('exact', 'alias', 'any')[0],
                digits = None):
    """Test whether a specific column from solution is contained in the student query results.
    
    Args:
        name: name used in the solution code for target column.
        msg : feedback message if column not contained in student query result.
        match: condition for whether student column could be possible match to solution.
               Should either be 'exact' if names must be identical, or 'any' if
               all student columns should be tested against solution.
        digits: if specified, number of decimals to use when comparing column values.

    :Example:
        Suppose we are testing the following SELECT statements

        * solution: ``SELECT artist_id as id, name FROM artists``
        * student : ``SELECT artist_id             FROM artists``

        Then, the resulting columns can be tested in the following ways.. ::

            # fails, since no column named id in student result
            Ex().test_column(name = 'id', match = 'exact')
            # passes, since id in solution matches artist_id in student result
            Ex().test_column(name = 'id', match = 'any')  
            # fails, since this column in solution doesn't match any in the student result
            Ex().test_column(name = 'name', match = 'any')


    """

    stu_res = state.student_result or {}
    sol_res = state.solution_result
    
    round_seq = lambda seq, digits: [round(x, digits) for x in seq]

    src_col = sol_res[name] if digits is None else round_seq(sol_res[name], digits)

    # get submission columns to test against
    if match == 'any':
        dst_cols = list(stu_res.values())
    elif match == 'alias':
        raise NotImplementedError()
    elif match == "exact":
        stu_res_lower = {k.lower() : v for k, v in stu_res.items()}
        dst_cols = [stu_res_lower.get(name.lower())]
    else:
        raise BaseException("match must be one of 'any', 'alias', 'exact'")

    # test that relevant submission columns contain the solution column
    for col in dst_cols:
        if digits is not None: 
            try: col = round_seq(col, digits)
            except TypeError: continue

        if src_col == col:
            return state

    # fail test if no match
    _msg = msg.format(name)
    state.do_test(Test(_msg))

    # return state just in case, but should never happen
    return state

def sort_rows(state, keys=None):
    stu_res = state.student_result or {}
    sol_res = state.solution_result

    # ensure all columns in solution are in submission result
    for k in sol_res:
        test_column_name(state, k)

    # map lower case key names to keys
    stu_keys = {k.lower(): k for k in stu_res}
    sol_keys = {k.lower(): k for k in sol_res}

    sort_cols = sorted(sol_keys)
    stu_cols = sort_cols + list(set(stu_keys) - set(sol_keys))

    # convert results to a tuple of rows
    sorted_sol = zip(*[state.solution_result[sol_keys[k]] for k in sort_cols])
    sorted_stu = zip(*[state.student_result[stu_keys[k]] for k in stu_cols])

    # sort
    tiny_none = TinyNone()
    for ii, k in enumerate(sort_cols):
        sorted_sol = sorted(sorted_sol, key = lambda row: row[ii] or tiny_none)

        sorted_stu = sorted(sorted_stu, key = lambda row: row[ii] or tiny_none)

    # convert sorted results back to dictionaries
    out_sol_res = dict(zip([sol_keys[k] for k in sort_cols], zip(*sorted_sol)))
    out_stu_res = dict(zip([stu_keys[k] for k in stu_cols] , zip(*sorted_stu)))

    return state.to_child(
                student_result = out_stu_res,
                solution_result = out_sol_res)

class TinyNone:
    def __lt__(self, x): return True

    def __gt__(self, x): return False
