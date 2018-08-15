# Changelog

All notable changes to the sqlwhat project will be documented in this file.

## 3.0.0

**Contains breaking changes!**

- All functions that start with `test_` have been deprecated.
- `check_error()` renamed to `has_error()`
- New functions `has_nrows()`, `has_ncols()`, `check_row`, `check_column`, `check_all_columns`, `has_equal_value`
- piece-wise messaging (uses new functionality in protowhat)
- Complete rewrite of documentation, explaining both the result-based checks and AST-based checks
- Improve coverage to 99% by adding tests on both functionality (pass/fail) and messaging.
- Improve package structure and test structure in general

