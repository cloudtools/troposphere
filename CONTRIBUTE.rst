Contributing
============

tl;dr
-----

1. Fork https://github.com/cloudtools/troposphere
#. Make the code better
#. Make the code pass tests
#. Create a Pull Request

How to Get Help
---------------

We have a Google Group, cloudtools-dev_, where you can ask questions and
engage with the troposphere community. Issues and pull requests are always
welcome!

How to Test Your Code
---------------------

The latest test scripts can be found at Travis-CI_.
If you look at the details of a job, you can see what automated tests
will be run against any commits to the project.

1. Create a virtualenv (e.g. `virtualenv ~/virtualenv/troposphere`)
#. Activate it: `source ~/virtualenv/troposphere/bin/activate`
#. `pip install --upgrade pip setuptools wheel`
#. `pip install -r requirements-dev.txt`
#. Run tests
    1. `pycodestyle .`
    #. `pyflakes .`
    #. `python setup.py test`
#. Alternatively, make can be used to run the tests, i.e. `make test`.

Tests are run against Python 2.7, 3.5, and 3.6.

Contributing Example Code
-------------------------

New example code should go into `troposphere/examples`. The expected
CloudFormation Template should be stored in `troposphere/tests/examples_output/`.
When tests are run the output of the code in the examples directory will
be compared with the expected results in the `example_output` directory.

.. _cloudtools-dev: https://groups.google.com/forum/#!forum/cloudtools-dev
.. _Travis-CI: https://travis-ci.org/cloudtools/troposphere
