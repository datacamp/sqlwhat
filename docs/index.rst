sqlwhat
-------

For an introduction to SCTs and how they use sqlwhat, visit the `README <https://github.com/datacamp/sqlwhat>`_.

This documentation features:

- A glossary with typical use-cases and corresponding SCT constructs.
- Reference documentation of all actively maintained sqlwhat functions.
- Some articles that gradually expose of sqlwhat's functionality and best practices.

If you are new to writing SCTs for SQL exercises, start with the tutorial.
The glossary is good to get a quick overview of how all functions play together after you have a basic understanding.
The reference docs become useful when you grasp all concepts and want to look up details on how to call certain functions and specify custom feedback messages.

If you find yourself writing SCTs for more advanced SQL queries, you'll probably venture into SCT functions that verify the AST representation of SQL queries.
When you do, make sure to keep the `AST viewer <https://ast-viewer.datacamp.com>`_ open; it is a great tool to
understand how different SQL statements are parsed and how to write your SCTs.

.. toctree::
   :maxdepth: 1
   :caption: Glossary

   glossary

.. toctree::
   :maxdepth: 2
   :caption: Reference

   reference

.. toctree::
   :maxdepth: 1
   :caption: Articles

   articles/tutorial.rst
   articles/result_checks.rst
   articles/ast_checks.rst

For details, questions and suggestions, `contact us <mailto:content-engineering@datacamp.com>`_.
