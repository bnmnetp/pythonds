# Parameters to control Makefile operation
PROJECT=pythonds3
SRC_DIR=pythonds
TEST_DIR=tests

# Default
all: package

# Make a package
package:
	python setup.py sdist bdist_wheel

# Remove old package
clean:
	rm -rf dist/ build/ pythonds3.egg-info/

# Upload to PyPi
upload:
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

# Upload to TestPyPi
upload_test:
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
