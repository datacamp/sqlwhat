sqlwhat
-------

``sqlwhat`` enables you to write Submission Correctness Tests (SCTs) for interactive SQL exercises on DataCamp.

- If you are new to teaching on DataCamp, check out https://authoring.datacamp.com.
- If you want to learn what SCTs are and how they work, visit `this article <https://authoring.datacamp.com/courses/exercises/technical-details/sct.html>`_ specifically.

If you are new to writing SCTs for SQL exercises, start with the ``protowhat`` docs (`link <https://protowhat.readthedocs.io>`_)
that explain the concept of state, SCT chaining, and how this relates to abstract syntax trees, in addition to providing documentation
on all SCT functions that are shared with the ``shellwhat`` package (used for writing SCTs for Shell exercises).

After consulting the resources above, you can continue with this site that features:

- Articles that list best practices commonly used SCT patterns.
- Reference documentation for all SCT functions that are specific to SQL exercises.

Because SQL scripts aren't as free form as, say, Python scripts,
you will find yourself using the AST-related SCT functions very often when checking SQL exercises.
The `AST viewer <https://ast-viewer.datacamp.com>`_ is a great tool to
understand how different SQL statements are parsed and will be very helpful in writing up your own SCTs.

.. toctree::
   :maxdepth: 1
   :caption: Articles

   articles/glossary.rst

.. toctree::
   :maxdepth: 2
   :caption: Reference

   reference