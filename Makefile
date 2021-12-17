# Parameters to control Makefile operation
PROJECT=pythonds3
SRC_DIR=pythonds3
DOC_DIR=docs
TEST_DIR=tests

# Default
all: package

# Initialize the environment
init:
	python3 -m pip install -r requirements-dev.txt

# Make a package
package:
	python3 setup.py sdist bdist_wheel

# Remove old package
clean:
	rm -rf dist/ build/ pythonds3.egg-info/
	find . -name "__pycache__" -type d -prune -exec rm -rf "{}" \;

# Upload to PyPi
upload:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

# Upload to TestPyPi
upload_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Autodiscover and run tests
test:
	python3 -m pytest $(TEST_DIR)

# Don't display instructions while cleaning
.SILENT: clean init test
