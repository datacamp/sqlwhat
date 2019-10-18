# Changelog

All notable changes to the sqlwhat project will be documented in this file.

## 3.8.1

- Update antlr-plsql

## 3.8.0

- Reuse protowhat functionality
- Remove backend dependency in tests
- Update dependencies

## 3.7.0

- Add Oracle support

## 3.6.0

- Expose `_debug` function
- Update protowhat
- Update ANTLR dependencies

## 3.5.0

- Update parsing layer (antlr-x and protowhat)
- `check_edge` default argument value change (see protowhat v1.5.0 release notes)

## 3.4.0

- Update ANTLR dependencies

## 3.3.0

- Add optional `force_diagnose` parameter to `test_exercise` to force passing the `diagnose` tests in `check_correct`.

## 3.2.1

- Update ANTLR dependencies

## 3.2.0

### Improved

- `has_error()` renamed to `has_no_error()` for more intuitive reasoning.

## 3.1.0

### Added

- Function `check_query()` to execute arbitrary queries against the database to verify whether database state updates happened correctly.

### Improved

- CI now runs all tests, including the ones that need the (private) `sqlbackend`.

## 3.0.0

**Contains breaking changes!**

- All functions that start with `test_` have been deprecated.
- `check_error()` renamed to `has_error()`
- New functions `has_nrows()`, `has_ncols()`, `check_row`, `check_column`, `check_all_columns`, `has_equal_value`
- piece-wise messaging (uses new functionality in protowhat)
- Complete rewrite of documentation, explaining both the result-based checks and AST-based checks
- Improve coverage to 99% by adding tests on both functionality (pass/fail) and messaging.
- Improve package structure and test structure in general
