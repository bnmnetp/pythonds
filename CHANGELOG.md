# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## 3.1.0 - 2021-12-17

This version adds type annotations and doc strings to many methods.

### Added

- Type annotations
- `pylint` and `mypy` as linters

### Changed

- replaced `pass` with `...`
- replaced `.format()` with "f-strings"

## Deprecated

- Versioning will change to yyyy.mm format soon

### Removed

- `child_left` and `child_right` in the `BinaryTree`

## 3.0.3 - 2020-01-31

This version fixes various bugs and performance issues found during the book review.

### Added

- shebang line to `__init__.py` files
- `flake8` and `codecov` are part of the development requirements now

### Changed

- Implementation of Bubble, Merge, and Heap sorting algorithms
- Start using `venv` instead of `pipenv`

### Deprecated

- Tree methods will be renamed for better alignment with the textbook
- Graph methods will be renamed for better alignment with the textbook
- Incomplete (not implemented) methods will be removed in 3.1.0

### Removed

- N/A

### Fixed

- Heapsort implementation is more efficient

### Security

- N/A

## 3.0.2 - 2019-01-10

This version follows **pylint** recommendations and uses **black** to format code.

### Added

- Shebang line to all source files

### Changed

- Source formatting using **black**

### Deprecated

- N/A

### Removed

- Some code as recommended by **pylint**

### Fixed

- N/A

### Security

- N/A

## 3.0.1 - 2018-07-25

This version adds examples of usage and updates tests.

### Added

- HOWTO explaining the usage of this package.
- HOWTO-DEV with the development guidelines.

### Changed

- Tests for all algorithms and data structures are using pytest.

### Deprecated

- N/A

### Removed

- N/A

### Fixed

- N/A

### Security

- N/A

## 3.0.0 - 2018-06-20

Initial release.

It's a rewrite of the [pythonds](https://pypi.org/project/pythonds/) project with the code restructured and (mostly) PEP8-compliant. The changes are **breaking** and may be inconsistent with the current edition of the [textbook](https://runestone.academy/runestone/static/pythonds/index.html).

The changes between _pythonds_ and _pythonds3_ are as follows:

### Added

- Linked list implementation (unordered and ordered).
- HashTable.
- Sorting algorithms
  - Bubble
  - Selection
  - Insertion
  - Shell sort
  - Mergesort
  - Quicksort
  - Heapsort
- Dijkstra's shortest path algorithm.
- Bellman-Ford shortest path algorithm.
- Prim's spanning tree algorithm.
- Tests for all algorithms and data structures.

### Changed

- Project structure.

### Deprecated

- CamelCase names.

### Removed

- `__main__` functions from all modules.

### Fixed

- Code formatting.
- [Binary heap bug](https://github.com/bnmnetp/pythonds/issues/5).
- [Preorder traversal bug](https://github.com/bnmnetp/pythonds/issues/10).

### Security

- Not all exceptions are handled properly.

[unreleased]: https://github.com/yasinovskyy/pythonds3/compare/v3.1.0...HEAD
