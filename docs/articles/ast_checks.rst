AST Checks
----------

.. warning::

    If a student submission cannot be parsed properly because of a syntax error,
    all AST-based checks will `not` run! It is therefore vital that you include your
    AST-based checks in the second argument of ``check_correct()`` so they can serve
    as 'diagnosing' SCTs rather than as 'correctness verifying' SCTs.

``check_field()``

``check_node()``

``has_equal_ast()``

``has_code()``

