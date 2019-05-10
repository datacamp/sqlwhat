from protowhat.Feedback import Feedback


def has_no_error(
    state, incorrect_msg="Your code generated an error. Fix it and try again!"
):
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
        state.report(incorrect_msg)

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
        raise NameError(
            "You are using has_result() to verify that the student query generated an error, but the solution query did not return a result either!"
        )

    if not state.student_result:
        state.report(incorrect_msg)

    return state


def has_nrows(
    state,
    incorrect_msg="Your query returned a table with {{n_stu}} row{{'s' if n_stu > 1 else ''}} while it should return a table with {{n_sol}} row{{'s' if n_sol > 1 else ''}}.",
):
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
        _msg = state.build_message(
            incorrect_msg, fmt_kwargs={"n_stu": n_stu, "n_sol": n_sol}
        )
        state.report(_msg)

    return state


def has_ncols(
    state,
    incorrect_msg="Your query returned a table with {{n_stu}} column{{'s' if n_stu > 1 else ''}} while it should return a table with {{n_sol}} column{{'s' if n_sol > 1 else ''}}.",
):
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
        _msg = state.build_message(
            incorrect_msg, fmt_kwargs={"n_stu": n_stu, "n_sol": n_sol}
        )
        state.report(_msg)

    return state


def has_equal_value(state, ordered=False, ndigits=None, incorrect_msg=None):
    """Verify if a student and solution query result match up.

    This function must always be used after 'zooming' in on certain columns or records (check_column, check_row or check_result).
    ``has_equal_value`` then goes over all columns that are still left in the solution query result, and compares each column with the
    corresponding column in the student query result.

    Args:
        ordered: if set to False, the default, all rows are sorted (according
                 to the first column and the following columns as tie breakers).
                 if set to True, the order of rows in student and solution query have to match.
        ndigits: if specified, number of decimals to use when comparing column values.
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

    if not state.parent_state:
        raise ValueError(
            "You can only use has_equal_value() on the state resulting from check_column, check_row or check_result."
        )

    if incorrect_msg is None:
        incorrect_msg = "Column `{{col}}` seems to be incorrect.{{' Make sure you arranged the rows correctly.' if ordered else ''}}"

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
            _msg = state.build_message(
                incorrect_msg, fmt_kwargs={"col": sol_col_name, "ordered": ordered}
            )
            state.report(_msg)

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
        sorted_sol = sorted(sorted_sol, key=lambda row: row[ii] or tiny_none)
        sorted_stu = sorted(sorted_stu, key=lambda row: row[ii] or tiny_none)

    # convert sorted results back to dictionaries
    out_sol_res = dict(zip([k for k in sort_cols], zip(*sorted_sol)))
    out_stu_res = dict(zip([k for k in stu_cols], zip(*sorted_stu)))

    return out_stu_res, out_sol_res


class TinyNone:
    def __lt__(self, x):
        return True

    def __gt__(self, x):
        return False


round_seq = lambda seq, digits: [round(x, digits) if x is not None else x for x in seq]
