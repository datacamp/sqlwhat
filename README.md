> :warning: **This repo has outdated tokens in its travisci config** 
> To make new releases for this project it needs to be moved to circleci

# sqlwhat

[![Build Status](https://travis-ci.org/datacamp/sqlwhat.svg?branch=master)](https://travis-ci.org/datacamp/sqlwhat)
[![codecov](https://codecov.io/gh/datacamp/sqlwhat/branch/master/graph/badge.svg)](https://codecov.io/gh/datacamp/sqlwhat)
[![PyPI version](https://badge.fury.io/py/sqlwhat.svg)](https://badge.fury.io/py/sqlwhat)

`sqlwhat` enables you to write Submission Correctness Tests (SCTs) for interactive SQL exercises on DataCamp.

- If you are new to teaching on DataCamp, check out https://authoring.datacamp.com.
- If you want to learn what SCTs are and how they work, visit [this article](https://authoring.datacamp.com/courses/exercises/technical-details/sct.html) specifically.
- For more information about writing SCTs for SQL exercises, consult https://sqlwhat.readthedocs.io.

## Installing

```
pip install sqlwhat     # install from pypi
make install            # install from source
```

## Reference

* API Docs: https://sqlwhat.readthedocs.io
* AST viewer: https://ast-viewer.datacamp.com
* Extensions: https://github.com/datacamp/sqlwhat-ext

## Raising issues with how SQL is parsed

Please raise an issue on the respsective parser repo:

* [antlr-tsql](https://github.com/datacamp/antlr-tsql)
* [antlr-psql](https://github.com/datacamp/antlr-plsql)

## Basic Use

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

## Running unit tests

```bash
pytest -m "not backend"
```

If you also want to run the backend tests, you need to set a `GITHUB_TOKEN` environment variable with access to the (private) `sqlbackend` repository.
After this, you can:

```bash
make install
pytest
```

### Rules of testing

1. Running queries is the backend's job
2. If a test doesn't run queries, it doesn't need the backend
3. Very few tests should run queries

## Building Docs

Install sqlwhat and run ..

```
cd docs
make html
```
