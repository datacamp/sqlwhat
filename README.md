# sqlwhat

[![Build Status](https://travis-ci.org/datacamp/sqlwhat.svg?branch=master)](https://travis-ci.org/datacamp/sqlwhat)
[![codecov](https://codecov.io/gh/datacamp/sqlwhat/branch/master/graph/badge.svg)](https://codecov.io/gh/datacamp/sqlwhat)
[![PyPI version](https://badge.fury.io/py/sqlwhat.svg)](https://badge.fury.io/py/sqlwhat)

Installing
----------

`pip install sqlwhat`

Reference
---------

* API Docs: https://sqlwhat.readthedocs.io
* AST viewer: https://sqlwhat-viewer.herokuapp.com
* Example DataCamp Course: https://github.com/datacamp/courses-sql-test
* Extensions: https://github.com/datacamp/sqlwhat-ext

Raising issues with how SQL is parsed
-------------------------------------

Please raise an issue on the respsective parser repo:

* [antlr-tsql](https://github.com/datacamp/antlr-tsql)
* [antlr-psql](https://github.com/datacamp/antlr-plsql)

Basic Use
---------

```python
from sqlwhat.State import State    # State holds info needed for tests
from sqlwhat.Reporter import Reporter
from sqlwhat.checks import *       # imports all SCTs
from sqlalchemy import create_engine

code = "SELECT * FROM artists WHERE id < 100"

state = State(
    student_code = code,
    solution_code = code,
    pre_exercise_code = "",
    student_conn = create_engine('sqlite:///'),
    solution_conn = create_engine('sqlite:///'),
    student_result = {'id': [1,2,3], 'name': ['greg', 'jon', 'martha']},
    solution_result = {'id': [1,2,3], 'name': ['toby', 'keith', 'deb']},
    reporter = Reporter()
    )

# test below passes, since code is equal for student and solution
has_equal_ast(state)

# test below raises a TestFail error, since 'name' col of results
# doesn't match between student and solution results
check_result(state)
# shows error data
state.reporter.build_payload()

# can also be done using a chain
from sqlwhat.sct_syntax import Ex
Ex(state).check_result()
```

Setup ANTLR grammar
-------------------

```
docker run -it -v ${PWD}:/output $CONTAINER\_ID /bin/bash
# inside container
cd /output
antlr4 -Dlanguage=Python3 $GRAMMAR_FILE.g4
```

Running unit tests
------------------

In order to install psycopg2 in a virtualenv, I [needed to run](http://stackoverflow.com/a/39244687/1144523)..

```
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install --no-cache psycopg2
```

Building Docs
-------------

Install sqlwhat and run ..

```
cd docs
make html
```
