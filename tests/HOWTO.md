#pytest
In order to use pytest, you should have a basic knowledge of Python as well as how to use your machine’s command line; the commands here were run on a Linux machine.

##How to get pytest:

	We will be using pip3 so make sure your version of pip is up to date.
	Create a virtual environment, if you don’t have one already, and activate it. Here the virtual environment is called “pythonds3”, but you can name it whatever you like:
		python3 -m virtualenv pythonds3
		source pythonds3/bin/activate
	To install pytest in your virtual environment, use:
		pip3 install pytest
	Reference below for how to use pytest.
	Use deactivate to exit your virtual environment.


##How to use pytest:

In your terminal window, the basic command for running pytest is, simply:
	pytest
Using this command will run all tests in the current directory and all its subdirectories which follow pytest’s naming convention:
	- Test files should be named test_<something>.py or <somthing>_test.py
	- Test methods and functions should be named test_<something>.
	- Test classes should be named Test<Something>.
All the provided tests already follow this naming convention and therefore should run properly.

*Selecting Tests*
If you want to run only certain tests, append the names of subdirectories or test files themselves:
	pytest test_basic_init.py
	pytest test_searching_init.py test_sorting_init.py
	pytest basic/
You can also run a single test within a test file; make sure to include the class name if the test is under a class:
	pytest test_linked_list.py::TestLinkedListMethods::test_node_str

*Options*
You can always view pytest’s default options by using:
	pytest --help
There are more options available than listed here, these are just the most likely to be used for these specific tests.
	-k EXPRESSION		selects only tests with the specified expression as a substring.
					pytest -k "_init" selects all test functions & methods with “_init” in their names
	-x | --exitfirst	exit instantly on first error or failed test
	--maxfail=num		exit after first num failures or errors
	--lf | --last-failed	rerun only the tests that failed last time
	--ff | --failed-first	run all the tests but run the last failures first
	-v | --verbose		increase verbosity (information displayed about the test)
	-q | --quiet		decrease verbosity
	-l | --showlocals	show local variables and their values in traceback (info for failing tests)
	--durations=N		show N slowest setup/test duration (N=0 for all)
	--collect-only		only collect tests, don’t execute them; useful to check other options before running the tests
	--version		display pytest lib version and import information

Reference Material: *Python Testing with pytest: Simple, Rapid, Effective, and Scalable* by Brian Okken
