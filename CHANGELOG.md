# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## 3.0.0 - 2018-06-20

Initial release.

It's a rewrite of the [pythonds](https://pypi.org/project/pythonds/) project with the code restructured and (mostly) PEP8-compliant. The changes are **breaking** and may be inconsistent with the current edition of the [textbook](https://runestone.academy/runestone/static/pythonds/index.html).

The changes between *pythonds* and *pythonds3* are as follows:

### Added
- Linked list implementation (unordered and ordered).
- HashTable.
- Sorting algorithms
  - Bubble
  - Selection
  - Instertion
  - Shellsort
  - Merge sort
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

[Unreleased]: https://github.com/yasinovskyy/pythonds3/compare/v3.0.0...HEAD
