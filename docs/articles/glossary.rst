Glossary
--------

This article lists some example solutions. For each of these solutions, an SCT
is included, as well as some example student submissions that would pass and fail. In all of these, a submission that
is identical to the solution will evidently pass.

.. note:: 

    These SCT examples are not golden bullets that are perfect for your situation.
    Depending on the exercise, you may want to focus on certain parts of a statement, or be 
    more accepting for different alternative answers.

Basic query check (strict)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

    # solution
    SELECT title FROM films

    # sct
    Ex().check_node('SelectStmt').multi(check_field('from_clause').has_equal_ast(),
                                        check_field('target_list').has_equal_ast())
    Ex().check_result()

    # passing submissions
    SELECT title FROM films

    # failing submissions
    SELECT id, title FROM films 
    SELECT * FROM films 
    SELECT id FROM films


Basic query check (robust)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that ``check_result()`` currently allows students to specify more columns than the solution strictly requires.

.. code-block:: none

    # solution
    SELECT title FROM films

    # sct
    Ex().test_correct(check_result(),
                      check_node('SelectStmt').multi(check_field('from_clause').has_equal_ast(),
                                                     check_field('target_list').has_equal_ast()))

    # passing submissions
    SELECT title FROM films
    SELECT id, title FROM films 
    SELECT * FROM films 

    # failing submissions
    SELECT id FROM films


TODO ADD MORE