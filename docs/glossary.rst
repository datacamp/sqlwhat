Glossary
--------

This article lists some example solutions. For each of these solutions, an SCT
is included, as well as some example student submissions that would pass and fail. In all of these, a submission that
is identical to the solution will evidently pass.

.. note:: 

    These SCT examples are not golden bullets that are perfect for your situation.
    Depending on the exercise, you may want to focus on certain parts of a statement, or be 
    more accepting for different alternative answers.

All of these examples come from the `Intro to SQL for Data Science <https://https://www.datacamp.com/courses/intro-to-sql-for-data-science>`_
and `Joining data in PostgreSQL <https://www.datacamp.com/courses/joining-data-in-postgresql>`_ courses. You can have a look at their
respective GitHub sources `here <https://github.com/datacamp/courses-intro-to-sql>`_ (public) and
`here <https://github.com/datacamp/courses-joining-data-in-postgresql>`_ (viewable by DataCamp employees only), respectively.


Selecting a column
~~~~~~~~~~~~~~~~~~

.. code-block:: sql

    -- solution query
    SELECT title FROM films;

.. code::

    # sct
    Ex().check_correct(
        check_col('title').is_equal(),
        check_node('SelectStmt').multi(
            check_field('target_list', 0).has_equal_ast(),
            check_field('from_clause').has_equal_ast()
        )   
    )

.. code-block:: sql

    -- submissions that pass
    SELECT title FROM films
    SELECT id, title FROM films
    SELECT id, title FROM films ORDER by id

    -- submissions that fail
    SELECT id FROM films
    SELECT id FROM films LIMIT 5

Star argument
~~~~~~~~~~~~~

.. code-block:: sql

    -- solution query
    SELECT * FROM films;

.. code::

    # sct
    Ex().check_correct(
        check_solution_cols().is_equal(),
        check_node('SelectStmt').multi(
            check_node('Star', missing_msg="Are you using `SELECT *` to select _all_ columns?"),
            check_field('from_clause').has_equal_ast()
        )
    )

.. code-block:: sql

    -- submissions that pass
    SELECT * FROM films
    SELECT id, title, <all_other_cols>, year FROM films
    SELECT * FROM films ORDER by year

    -- submissions that fail
    SELECT id FROM films
    SELECT id, title FROM films
    SELECT * FROM films LIMIT 5

``COUNT(*)``
~~~~~~~~~~~~

.. code-block:: sql

    -- solution query
    SELECT COUNT(*) FROM films;

.. code::

    # sct
    Ex().check_correct(
        check_col('count').is_equal(),
        check_node('SelectStmt').multi(
            check_node('Call').multi(
                check_field('name').has_equal_ast(msg="Are you calling the `COUNT()` function?"),
                check_field('args').has_equal_ast(msg='Are you using `COUNT(*)`?')
            ),
            check_field('from_clause').has_equal_ast()
        )
    )

.. code-block:: sql

    -- submissions that pass
    SELECT COUNT(*) FROM films
    SELECT COUNT(id) FROM films

    -- submissions that fail
    SELECT * FROM films
    SELECT COUNT(*) FROM films WHERE id < 100

``WHERE`` clause
~~~~~~~~~~~~~~~~

.. code-block:: sql

    -- solution query
    SELECT name, birthdate
    FROM people
    WHERE birthdate = '1974-11-11';

.. code::

    # First check if the WHERE clause was correct
    Ex().check_correct(
        has_nrows(),
        check_node('SelectStmt').multi(
            check_field('from_clause').has_equal_ast(),
            check_field('where_clause').has_equal_ast()
        )
    )

    # Next check if right columns were included
    Ex().check_correct(
        check_solution_cols().is_equal(),
        check_node('SelectStmt').check_field('target_list').check_or(
            has_equal_ast(),
            has_equal_ast(sql = "birthdate, name")
        )
    )

``ORDER BY``
~~~~~~~~~~~~

.. code-block:: sql

    SELECT name
    FROM people
    ORDER BY name;

.. code::

    # Check whether the right column was included
    Ex().check_col('name')

    Ex().check_correct(
        # Check whether the name column is correct (taking into account order)
        check_col('name').is_equal(ordered=True),
        check_node('SelectStmt').multi(
            check_field('from_clause').has_equal_ast(),
            check_field('order_by_clause').has_equal_ast()
        )
    )

Joins
~~~~~

.. code-block:: sql

    SELECT *
    FROM cities
    INNER JOIN countries
    ON cities.country_code = countries.code;

.. code::

    # First check if the joining went well (through checking the number of rows)
    Ex().check_correct(
        has_nrows(),
        check_node('SelectStmt').check_field('from_clause').multi(
            check_field('join_type').has_equal_ast(),
            check_field('left').has_equal_ast(),
            check_field('right').has_equal_ast(),
            check_field('cond').check_or(
                has_equal_ast(),
                # the other way around should also work
                has_equal_ast(sql = 'countries.code = cities.country_code')
            )
        )
    )

    # Check if all columns are included and correct
    Ex().check_correct(
        check_solution_cols().is_equal(),
        check_node('SelectStmt').check_node('Star')
    )

