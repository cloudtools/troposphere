# How to Contribute to Troposphere

## tl;dr
1. Fork https://github.com/cloudtools/troposphere
1. Make the code better
1. Make the code pass tests
1. Create a Pull Request

## How to Get Help

See README.md at top of the project for developer mailing list.

## How to Test Your Code

The latest test scripts can be found at https://travis-ci.org/cloudtools/troposphere.
If you look at the details of a job, you can see what automated tests
will be run against any commits to the project.

1. Create a virtualenv (e.g. `virtualenv ~/virtualenv/troposphere`)
1. Activate it: `source ~/virtualenv/troposphere/bin/activate`
1. `pip install --upgrade pip setuptools wheel`
1. `pip install -r docs/requirements.txt`
1. Run tests:
  1. `pep8 .`
  1. `pyflakes .`
  1. `python setup.py test`

Tests are run against Python 2.7, 3.3, 3.4, and 3.5.

## Contributing Example Code

New example code should go into `troposphere/examples`. The expected
CloudFormation Template should be stored in `troposphere/tests/examples_output/`.
When tests are run the output of the code in the examples directory will
be compared with the expected results in the `example_output` directory.
