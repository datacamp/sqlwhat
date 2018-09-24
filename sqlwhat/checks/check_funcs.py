def allow_error(state):
    """Allow submission to pass, even if it originally caused a database error.

    Simply use ``Ex().allow_error()`` in your SCT if the intent of the exercise to
    generate an error.
    """
    state.reporter.allow_errors()
    return state

def has_no_error(state, incorrect_msg="Your code generated an error. Fix it and try again!"):
    """Check whether the submission did not generate a runtime error.

    Simply use ``Ex().has_no_error()`` in your SCT whenever you want to check for errors.
    By default, after the entire SCT finished executing, ``sqlwhat`` will check
    for errors before marking the exercise as correct. You can disable this behavior
    by using ``Ex().allow_error()``.

    Args:
        incorrect_msg: If specified, this overrides the automatically generated feedback message
                       in case the student's query did not return a result.
    """

    if state.reporter.get_errors():
        state.do_test(incorrect_msg)

    return state

def has_result(state, incorrect_msg="Your query did not return a result."):
    """Checks if the student's query returned a result.
    
    Args:
        incorrect_msg: If specified, this overrides the automatically generated feedback message
                       in case the student's query did not return a result.
    """

    # first check if there is no error
    has_no_error(state)

    if not state.solution_result:
        raise NameError("You are using has_result() to verify that the student query generated an error, but the solution query did not return a result either!")

    if not state.student_result:
        state.do_test(incorrect_msg)

    return state

def has_nrows(state, incorrect_msg="Your query returned a table with {{n_stu}} row{{'s' if n_stu > 1 else ''}} while it should return a table with {{n_sol}} row{{'s' if n_sol > 1 else ''}}."):
    """Test whether the student and solution query results have equal numbers of rows.
    
    Args:
        incorrect_msg: If specified, this overrides the automatically generated feedback message
                       in case the number of rows in the student and solution query don't match.
    """

    # check that query returned something
    has_result(state)

    # assumes that columns cannot be jagged in size
    n_stu = len(next(iter(state.student_result.values())))
    n_sol = len(next(iter(state.solution_result.values())))

    if n_stu != n_sol:
        _msg = state.build_message(incorrect_msg, fmt_kwargs={'n_stu':n_stu,'n_sol':n_sol})
        state.do_test(_msg)

    return state

def has_ncols(state, incorrect_msg="Your query returned a table with {{n_stu}} column{{'s' if n_stu > 1 else ''}} while it should return a table with {{n_sol}} column{{'s' if n_sol > 1 else ''}}."):
    """Test whether the student and solution query results have equal numbers of columns.

    Args:
        incorrect_msg: If specified, this overrides the automatically generated feedback message
                       in case the number of columns in the student and solution query don't match.

    :Example:

        Consider the following solution and SCT: ::

            # solution
            SELECT artist_id as id, name FROM artists

            # sct
            Ex().has_ncols()

            # passing submission
            SELECT artist_id as id, name FROM artists

            # failing submission (too little columns)
            SELECT artist_id as id FROM artists

            # passing submission (two columns, even though not correct ones)
            SELECT artist_id, label FROM artists

    """

    # check that query returned something
    has_result(state)

    n_stu = len(state.student_result)
    n_sol = len(state.solution_result)

    if n_stu != n_sol:
        _msg = state.build_message(incorrect_msg, fmt_kwargs={'n_stu':n_stu,'n_sol':n_sol})
        state.do_test(_msg)

    return state

def check_row(state, index,
              missing_msg=None,
              expand_msg=None):
    """Zoom in on a particular row in the query result, by index.

    After zooming in on a row, which is represented as a single-row query result,
    you can use ``has_equal_value()`` to verify whether all columns in the zoomed in solution
    query result have a match in the student query result.

    Args:
        index: index of the row to zoom in on (zero-based indexed).
        missing_msg: if specified, this overrides the automatically generated feedback
                     message in case the row is missing in the student query result.
        expand_msg: if specified, this overrides the automatically generated feedback 
                    message that is prepended to feedback messages that are thrown
                    further in the SCT chain.

    :Example:

        Suppose we are testing the following SELECT statements

        * solution: ``SELECT artist_id as id, name FROM artists LIMIT 5``
        * student : ``SELECT artist_id, name       FROM artists LIMIT 2``

        We can write the following SCTs: ::

            # fails, since row 3 at index 2 is not in the student result
            Ex().check_row(2)

            # passes, since row 2 at index 1 is in the student result
            Ex().check_row(0)

    """

    if missing_msg is None: missing_msg = "The system wants to verify row {{index + 1}} of your query result, but couldn't find it. Have another look."
    if expand_msg is None: expand_msg = "Have another look at row {{index + 1}} in your query result. "
    msg_kwargs = { 'index': index }

    # check that query returned something
    has_result(state)

    stu_res = state.student_result
    sol_res = state.solution_result

    n_sol = len(next(iter(sol_res.values())))
    n_stu = len(next(iter(stu_res.values())))
    
    if index >= n_sol:
        raise BaseException("There are only {} rows in the solution query result, and you're trying to fetch the row at index {}".format(n_sol, index))
    
    if index >= n_stu:
        _msg = state.build_message(missing_msg, fmt_kwargs = msg_kwargs)
        state.do_test(_msg)

    return state.to_child(
        append_message = { 'msg': expand_msg, 'kwargs': msg_kwargs },
        student_result = { k: [v[index]] for k,v in stu_res.items() },
        solution_result = { k: [v[index]] for k,v in sol_res.items() }
    )

def check_column(state, name,
              missing_msg=None,
              expand_msg=None):
    """Zoom in on a particular column in the query result, by name.

    After zooming in on a column, which is represented as a single-column query result,
    you can use ``has_equal_value()`` to verify whether the column in the solution query result
    matches the column in student query result.

    Args:
        name: name of the column to zoom in on.
        missing_msg: if specified, this overrides the automatically generated feedback
                     message in case the column is missing in the student query result.
        expand_msg: if specified, this overrides the automatically generated feedback 
                    message that is prepended to feedback messages that are thrown
                    further in the SCT chain.

    :Example:

        Suppose we are testing the following SELECT statements

        * solution: ``SELECT artist_id as id, name FROM artists``
        * student : ``SELECT artist_id, name       FROM artists``

        We can write the following SCTs: ::

            # fails, since no column named id in student result
            Ex().check_column('id')

            # passes, since a column named name is in student_result
            Ex().check_column('name')

    """

    if missing_msg is None: missing_msg = "We expected to find a column named `{{name}}` in the result of your query, but couldn't."
    if expand_msg is None: expand_msg = "Have another look at your query result. "
    msg_kwargs = { 'name': name }

    # check that query returned something
    has_result(state)

    stu_res = state.student_result
    sol_res = state.solution_result

    if name not in sol_res:
        raise BaseException("name %s not in solution column names"%name)

    if name not in stu_res:
        _msg = state.build_message(missing_msg, fmt_kwargs = msg_kwargs)
        state.do_test(_msg)

    return state.to_child(
        append_message = { 'msg': expand_msg, 'kwargs': msg_kwargs },
        student_result = { name: stu_res[name] },
        solution_result = { name: sol_res[name] }
    )

def check_all_columns(state, allow_extra=True, too_many_cols_msg=None, expand_msg=None):
    """Zoom in on the columns that are specified by the solution
    
    Behind the scenes, this is using ``check_column()`` for every column that is in the solution query result.
    Afterwards, it's selecting only these columns from the student query result and stores them in a child
    state that is returned, so you can use ``has_equal_value()`` on it.

    This function does not allow you to customize the messages for ``check_column()``. If you want to manually
    set those, simply use ``check_column()`` explicitly.

    Args:
        allow_extra: True by default, this determines whether students are allowed to have included
                     other columns in their query result.
        too_many_cols_msg: If specified, this overrides the automatically generated feedback message in
                           case ``allow_extra`` is False and the student's query returned extra columns when
                           comparing the so the solution query result.
        expand_msg: if specified, this overrides the automatically generated feedback 
                    message that is prepended to feedback messages that are thrown
                    further in the SCT chain.

    :Example:

        Consider the following solution and SCT: ::

            # solution
            SELECT artist_id as id, name FROM artists

            # sct
            Ex().check_all_columns()

            # passing submission
            SELECT artist_id as id, name FROM artists

            # failing submission (wrong names)
            SELECT artist_id, name FROM artists

            # passing submission (allow_extra is True by default)
            SELECT artist_id as id, name, label FROM artists
    """

    if too_many_cols_msg is None: too_many_cols_msg = "Your query result contains the column {{col}} but shouldn't."
    if expand_msg is None: expand_msg = "Have another look at your query result. "
 
    child_stu_result = {}
    child_sol_result = {}

    for col in state.solution_result:
        child = check_column(state, col)
        child_stu_result.update(**child.student_result)
        child_sol_result.update(**child.solution_result)

    cols_not_in_sol = list(set(state.student_result.keys()) - set(child_stu_result.keys()))
    if not allow_extra and len(cols_not_in_sol) > 0:
        _msg = state.build_message("Your query result contains the column `{{col}}` but shouldn't.", fmt_kwargs = { 'col': cols_not_in_sol[0] })
        state.do_test(_msg)

    return state.to_child(
        append_message = { 'msg': expand_msg, 'kwargs': {} },
        student_result = child_stu_result,
        solution_result = child_sol_result
    )

round_seq = lambda seq, digits: [round(x, digits) if x is not None else x for x in seq]

def has_equal_value(state, ordered=False, ndigits=None, incorrect_msg=None):
    """Verify if a student and solution query result match up.

    This function must always be used after 'zooming' in on certain columns or records (check_column, check_row or check_result).
    ``has_equal_value`` then goes over all columns that are still left in the solution query result, and compares each column with the
    corresponding column in the student query result.

    Args:
        ordered: if set to False, the default, all rows are sorted (according
                 to the first column and the following columns as tie breakers).
                 if set to True, the order of rows in student and solution query have to match.
        digits: if specified, number of decimals to use when comparing column values.
        incorrect_msg: if specified, this overrides the automatically generated feedback
                       message in case a column in the student query result does not match
                       a column in the solution query result.

    :Example:

        Suppose we are testing the following SELECT statements

        * solution: ``SELECT artist_id as id, name FROM artists ORDER BY name``
        * student : ``SELECT artist_id, name       FROM artists``

        We can write the following SCTs: ::

            # passes, as order is not important by default
            Ex().check_column('name').has_equal_value()

            # fails, as order is deemed important
            Ex().check_column('name').has_equal_value(ordered=True)

            # check_column fails, as id is not in the student query result
            Ex().check_column('id').has_equal_value()

            # check_all_columns fails, as id not in the student query result
            Ex().check_all_columns().has_equal_value()
    """

    if not hasattr(state, 'parent'):
        raise ValueError("You can only use has_equal_value() on the state resulting from check_column, check_row or check_result.")
    
    if incorrect_msg is None: incorrect_msg="Column `{{col}}` seems to be incorrect.{{' Make sure you arranged the rows correctly.' if ordered else ''}}"

    # First of all, check if number of rows correspond
    has_nrows(state)

    if not ordered:
        stu_res, sol_res = sort_rows(state)
    else:
        stu_res = state.student_result
        sol_res = state.solution_result

    for sol_col_name, sol_col_vals in sol_res.items():
        stu_col_vals = stu_res[sol_col_name]
        if ndigits is not None:
            try:
                sol_col_vals = round_seq(sol_col_vals, ndigits)
                stu_col_vals = round_seq(stu_col_vals, ndigits)
            except:
                pass
        
        if sol_col_vals != stu_col_vals:
            _msg = state.build_message(incorrect_msg, fmt_kwargs = { 'col': sol_col_name, 'ordered': ordered })
            state.do_test(_msg)

    return state

def sort_rows(state):
    stu_res = state.student_result
    sol_res = state.solution_result

    sort_cols = sorted(sol_res.keys())
    stu_cols = sort_cols + list(set(stu_res.keys()) - set(sol_res.keys()))

    # convert results to a tuple of rows
    sorted_sol = zip(*[state.solution_result[k] for k in sort_cols])
    sorted_stu = zip(*[state.student_result[k] for k in stu_cols])

    # sort
    tiny_none = TinyNone()
    for ii, k in enumerate(sort_cols):
        sorted_sol = sorted(sorted_sol, key = lambda row: row[ii] or tiny_none)
        sorted_stu = sorted(sorted_stu, key = lambda row: row[ii] or tiny_none)

    # convert sorted results back to dictionaries
    out_sol_res = dict(zip([k for k in sort_cols], zip(*sorted_sol)))
    out_stu_res = dict(zip([k for k in stu_cols] , zip(*sorted_stu)))

    return out_stu_res, out_sol_res

class TinyNone:
    def __lt__(self, x): return True
    def __gt__(self, x): return False

def lowercase(state):
    """Convert all column names to their lower case versions to improve robustness
    
    :Example:

        Suppose we are testing the following SELECT statements

        * solution: ``SELECT artist_id as id FROM artists``
        * student : ``SELECT artist_id as ID FROM artists``

        We can write the following SCTs: ::

            # fails, as id and ID have different case
            Ex().check_column('id').has_equal_value()

            # passes, as lowercase() is being used
            Ex().lowercase().check_column('id').has_equal_value()

    """
    return state.to_child(
        student_result = { k.lower():v for k,v in state.student_result.items() },
        solution_result = { k.lower():v for k,v in state.solution_result.items() } 
    )

def check_result(state):
    """High level function which wraps other SCTs for checking results.
    
    ``check_result()``

    * uses ``lowercase()``, then
    * runs ``check_all_columns()`` on the state produced by ``lowercase()``, then
    * runs ``has_equal_value`` on the state produced by ``check_all_columns()``.
    """

    state1 = lowercase(state)
    state2 = check_all_columns(state1)
    has_equal_value(state2)
    return state2

def check_query(state, query, error_msg=None, expand_msg=None):
    """Run arbitrary queries against to the DB connection to verify the database state.

    For queries that do not return any output (INSERTs, UPDATEs, ...),
    you cannot use functions like ``check_col()`` and ``is_equal()`` to verify the query result.

    ``check_query()`` will rerun the solution query in the transaction prepared by sqlbackend,
    and immediately afterwards run the query specified in ``query``.

    Next, it will also run this query after rerunning the student query in a transaction.

    Finally, it produces a child state with these results, that you can then chain off of
    with functions like ``check_column()`` and ``has_equal_value()``.

    Args:
        query: A SQL query as a string that is executed after the student query is re-executed.
        error_msg: if specified, this overrides the automatically generated feedback
                   message in case the query generated an error.
        expand_msg: if specified, this overrides the automatically generated feedback 
                    message that is prepended to feedback messages that are thrown
                    further in the SCT chain.

    :Example:

        Suppose we are checking whether an INSERT happened correctly: ::

            INSERT INTO company VALUES (2, 'filip', 28, 'sql-lane', 42)

        We can write the following SCT: ::

            Ex().check_query('SELECT COUNT(*) AS c FROM company').has_equal_value()

    """

    if error_msg is None: error_msg = "Running `{{query}}` after your submission generated an error."
    if expand_msg is None: expand_msg = "The autograder verified the result of running `{{query}}` against the database. "

    msg_kwargs = { 'query': query }

    # before redoing the query, 
    # make sure that it didn't generate any errors
    has_no_error(state)

    _msg = state.build_message(error_msg, fmt_kwargs = msg_kwargs)

    # sqlbackend makes sure all queries are run in transactions.
    # Rerun the solution code first, after which we run the provided query
    with dbconn(state.solution_conn) as conn:
        _ = runQuery(conn, state.solution_code)
        sol_res = runQuery(conn, query)

    if sol_res is None:
        raise ValueError("Solution failed: " + _msg)

    # sqlbackend makes sure all queries are run in transactions.
    # Rerun the student code first, after wich we run the provided query
    with dbconn(state.student_conn) as conn:
        _ = runQuery(conn, state.student_code)
        stu_res = runQuery(conn, query)

    if stu_res is None:
        state.do_test(_msg)

    return state.to_child(
        append_message = { 'msg': expand_msg, 'kwargs': msg_kwargs },
        student_result = stu_res,
        solution_result = sol_res
    )

# The functions below are almost exact copies of what is in sqlbackend,
# But already use a conn object inside a transaction (this is how sqlbackend calls test_exercise)

from collections import OrderedDict
from contextlib import contextmanager

@contextmanager
def dbconn(conn):
    sub_conn = conn.connect()
    trans = sub_conn.begin()
    yield sub_conn
    try:
        trans.rollback()
        sub_conn.close()
    except:
        # we tried
        pass

def runQuery(conn, code):
    try:
        if not code: return OrderedDict()
        cursor = conn.connection.cursor()
        cursor.execute(str(code))
        try:
            records = [list(record) for record in cursor.fetchall()]
            columns = [i[0] for i in cursor.description]
            result = OrderedDict(zip(columns, list(zip(*records))))
        except Exception:
            result = None
        cursor.close()
        return result
    except Exception:
        return None
