Result Checks
-------------

As you could read in the tutorial, there are two families of SCT functions in sqlwhat:

- result-based checks, that look at the result of the student's query and the solution query
- AST-based checks, that look at the abstract syntax tree representation of the query and allow you to check for elements.

This article gives an overview of all result-based checks, that are typically used as the first argument to ``check_correct()``.

On the lowest level, you can have the SCT fail when the student query generated an error with ``has_no_error()``:

.. code::

    Ex().has_no_error()

Next, you can verify whether the student query actually returned a result with ``has_result()``.
Behind the scenes, this function first uses ``has_no_error()``: if the query resulted in an error, it cannot return a result:

.. code::

    Ex().has_result()

More high-level, you can compare the number of rows of the student's query result and the solution query result with ``has_nrows()``.
This is useful to check whether e.g. a ``WHERE`` or ``LIMIT`` clause was coded up correctly to only return a subset of results:

.. code::

    Ex().has_nrows()

Similarly, but less-used, you can also compare the number of columns the student's query and solution query returned.
This function fails if the number of columns doesn't match. It passes if they do match, even if the column names differ:

.. code::

    Ex().has_ncols()

With ``check_row()``, you can zoom in on a particular record of the student and solution query result,
so you can compare there values later on with ``has_equal_value()`` (see further).
The example below zooms in on the third row (with index 2) of the student query result, returning a state
that only considers the data for the third row. It fails if the student query does not contain 3 rows.

.. code::

    Ex().check_row(2)

Similarly, and more often used than ``check_row()``, you can use ``check_column()`` to zoom in on a particular column
in the student's and solution query result by name. The function fails if the column cannot be found in the student query:

.. code::

    Ex().check_column('title')

Often, the solution selects multiple columns from a table. Writing a ``check_column()`` for every column in there would be tedious.
Therefore, there is a utility function, ``check_all_columns()``, that behind the scenes runs ``check_column()`` for every
column that is found in the solution query result, after which it zooms in on these columns. Suppose you have a solution query
that returns three columns, named ``column1``, ``column2`` and ``column3``. If you want to verify whether these columns are
also included in the student query result, you have different options:

.. code::

    # verbose: use check_column thrice
    Ex().multi(
        check_column('column1'),
        check_column('column2'),
        check_column('column3')
    )

    # short: use check_all_columns()
    Ex().check_all_columns()

As an extra in ``check_all_columns()``, you can also set ``allow_extra`` to ``False``, which causes the function
to fail if the student query contains columns that the solution column `does not` contain. ``allow_extra`` is ``True`` by default.

All of the functions above were about checking whether the number of rows/columns are correct, whether some rows/columns could be found in the query,
but none of them look at the actual contents of the returned table. For this, you can use ``has_equal_value()``. The function simply
looks at the student's query result and solution query result or a subset of them (if ``check_row``, ``check_column`` or ``check_all_columns()`` were used):

.. code::

    # compare entire query result (needs exact match)
    Ex().has_equal_value()

    # compare records on row 3
    Ex().check_row(2).has_equal_value()

    # compare columns title
    Ex().check_column('title').has_equal_value()

    # zoom in on all columsn that are also in the solution and compare them
    Ex().check_all_columns().has_equal_value()

By default, ``has_equal_value()`` will order the records, so that order does not matter. If you want order to matter, you can set ``ordered=True``:

.. code::

    Ex().check_all_columns().has_equal_value(ordered = True)

Finally, there is a utility function called ``lowercase()`` that takes the state it is passed, and converts all column names in both
the student and solution query result to their lowercase versions. This increases the chance for 'matches' when using ``check_column()`` and ``check_all_columns()``.

Suppose the student did

.. code-block:: sql

    SELECT Title FROM artists

while the solution expected

.. code-block:: sql

    SELECT title FROM artists

Depending on the SCT you write, it will pass or fail:

.. code::

    # SCT that will fail
    Ex().check_column('title').has_equal_value()

    # SCT that will pass (because Title is converted to title)
    Ex().check_column('Title').has_equal_value()

For advanced examples on how result-based checks are typically used in combination with ``check_correct()``, check out the glossary!
