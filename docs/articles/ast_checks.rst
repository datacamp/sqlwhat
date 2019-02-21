AST Checks
----------

As you could read in the tutorial, there are two families of SCT functions in sqlwhat:

- result-based checks, that look at the result of the student's query and the solution query
- AST-based checks, that look at the abstract syntax tree representation of the query and allow you to check for elements.

This article gives an overview of all AST-based checks, that are typically used as the second argument to ``check_correct()``.

.. warning::

    If a student submission cannot be parsed properly because of a syntax error,
    all AST-based checks will `not` run! It is therefore vital that you include your
    AST-based checks in the second argument of ``check_correct()`` so they can serve
    as 'diagnosing' SCTs rather than as 'correctness verifying' SCTs.

Navigating the tree
===================

The tutorial gave a gentle introduction into how the AST of a SQL query can be 'walked' as it were, using ``check_edge()`` and
``check_node()``. In addition to the state they start from, these functions take a couple of different arguments:

- ``name``: the name of the node or field you want to zoom in on,
- ``index``: an optional argument to specify which occurrence of the node or field to zoom in on,
- ``missing_msg``: if specified, this overrides the automatically generated feedback message in case the node or field could not be found.

How to figure out which ``name`` to use? Navigate to the `AST viewer <https://ast-viewer.datacamp.com>`_ and in Editor mode,
paste the SQL query of the solution. This will produce a parse tree in the first box, and an Astract Syntax Tree in the second box.

For a full example of how this 'walk down the tree' works, read Example 2 of the tutorial.

As another example, suppose you want to check whether the ``ON`` part of an ``INNER JOIN`` is correct according to the following solution:

.. code-block:: sql

    SELECT *
    FROM cities
    INNER JOIN countries
    ON cities.country_code = countries.code;

The AST representation of this SQL query looks as follows:

  .. image:: ast_checks_ast.png
     :align: center

To zoom in on the sub-tree that corresponds to the ``ON`` part, we have to:

- take the ``SelectStmt`` node (with ``check_node('SelectStmt')``)
- walk down the ``from_clause`` edge (with ``check_edge('from_clause')``)
- walk down the ``cond`` edge (with ``check_edge('cond')``)

.. code::

    Ex(). \
        check_node('SelectStmt'). \
        check_edge('from_clause'). \
        check_edge('cond')

This SCT will focus on the following part of the solution query:

.. code-block:: sql

    cities.country_code = countries.code

Suppose that the student made a mistake (using ``code`` twice), and submitted the following query:

.. code-block:: sql

    SELECT *
    FROM cities
    INNER JOIN countries
    ON cities.code = countries.code;

The SCT will focus on the following part of the student query:

.. code-block:: sql

    cities.code = countries.code

Checking the tree
=================

Once you've used a combination of ``check_node()`` and ``check_edge()`` to zoom in on a part of interest
you can use ``has_equal_ast()`` to verify whether the elements correspond.

Continuing from the ``INNER JOIN`` example, we can verify whether the snippets of SQL code that have been zoomed in have a matching AST representation:

.. code::

    Ex(). \
        check_node('SelectStmt'). \
        check_edge('from_clause'). \
        check_edge('cond'). \
        has_equal_ast()

You can supplement this with a ``check_or()`` call and a manually specified ``sql`` snippet if you want to allow for multiple ways of specifying the condition:

.. code::

    Ex(). \
        check_node('SelectStmt'). \
        check_edge('from_clause'). \
        check_edge('cond'). \
        check_or(
            has_equal_ast(),
            has_equal_ast(sql = "countries.code = cities.code")
        )

Now, using either ``ON cities.code = countries.code`` or ``countries.code = cities.code`` will be accepted.

For a more complete and robust example of an ``INNER JOIN`` query, visit the glossary.

In addition to ``has_equal_ast()``, you can also use ``has_code()`` to
look at the actual code of a part of the SQL query and verify it with a regular expression,
but you will rarely find yourself using it.

