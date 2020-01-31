**This guide is intended for the project developers. See docs/HOWTO.md for the usage examples.**

# General information

## Introduction

This educational project is a supplement to the textbook and is not intended to be a comprehensive collection of algorithms and data structures. Some implementation details are intentionally left out and should be used as practice exercises.

This project is developed on Linux but most commands used in this document are platform-independent.

## Contributing to the project

This project can be used to demonstrate new features of Python (type hints, f-strings, data classes etc.) Any improvement of this kind is welcome.

## Getting started

1. Clone the repository

    You'll need to fork the repository and submit a pull request if you'd like to merge your changes to the upstream. You can also clone my repository directly.

    `git clone git@github.com:yasinovskyy/pythonds3.git`

    or

    `git clone https://github.com/yasinovskyy/pythonds3.git`

1. Setup the virtual environment

    There are no external dependencies in the code, but the package uses *pytest* for testing, *flake8* for linting, and *black* for formatting.

    `make init`

    or 

    `python3 -m venv .venv`

    `source .venv/bin/activate`

    `python3 -m pip install -r requirements-dev.txt`

# Testing

This project uses *pytest* framework. In order to use pytest, you must have a basic knowledge of Python and command line interface.  
  
## Getting pytest

pytest is installed when you activate the virtual environment and install dependencies. You can also install it using `pip`.

`python3 -m pip install -U pytest`

## Using pytest
  
The basic command for running pytest is `pytest`.

Using this command will run all tests in the current directory and all its subdirectories which follow pytest’s naming convention:

* Test files should be named test_*.py or *_test.py

* Test methods and functions should be named test_*

* Test classes should be named Test*

All the provided tests already follow this naming convention and therefore should run properly.  
  
## Selective testing

It is possible to run certain tests by providing the names of subdirectories or test files as arguments:

`pytest test_basic_init.py`

or

`pytest test_searching_init.py test_sorting_init.py`

or

`pytest basic/`  

You can also run a single test within a test file; make sure to include the class name if the test is under a class:

`pytest test_linked_list.py::TestLinkedListMethods::test_node_str`  
  
## pytest options

You can always view pytest’s default options by using `pytest --help`.

There are more options available than listed here, these are just the most likely to be used for these specific tests.

* select only tests with the specified expression as a substring

    `-k EXPRESSION`

* select all test functions & methods with “_init” in their names

    `pytest -k "_init"` 

* exit instantly on first error or failed test

    `-x | --exitfirst`

* exit after first num failures or errors

    `--maxfail=num`

* rerun only the tests that failed last time  

    `--lf | --last-failed`

* run all the tests but run the last failures first

    `--ff | --failed-first`

* increase verbosity (information displayed about the test)

    `-v | --verbose`

* decrease verbosity

    `-q | --quiet`

* show local variables and their values in traceback (info for failing tests)

    `-l | --showlocals`

* show N slowest setup/test duration (N=0 for all)

    `--durations=N`

* collect tests but don’t execute them; useful to check other options before running the tests

    `--collect-only`

* display pytest lib version and import information

    `--version`

Reference Material: *Python Testing with pytest: Simple, Rapid, Effective, and Scalable* by Brian Okken

## Packaging

Following the [guidelines](https://packaging.python.org/tutorials/packaging-projects/).

* Remove old and temporary directories (e.g `__pycache__`).

    `make clean`

* Update the version number in the **setup** file.

* Generate a package

    `make package`

    or

    `python3 setup.py sdist bdist_wheel`
    
* Upload the package to PyPi

    `make upload`

    or

    `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`
