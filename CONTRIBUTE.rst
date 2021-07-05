Contributing
============

tl;dr
-----

1. Fork https://github.com/cloudtools/troposphere
#. Make the code better
#. Make the code pass tests
#. Create a Pull Request

How to Setup Your Development Environment
-----------------------------------------

This project uses `poetry <https://python-poetry.org/>`_ for dependency
management and creating virtual environments.

Currently, we require use the use of a pre-release version (``>=1.2.0a1``)
to support including scripts with troposphere.

#. Install poetry ``curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python - --preview``
#. Run ``make setup``.

How to Get Help
---------------

We have a Google Group, cloudtools-dev_, where you can ask questions and
engage with the troposphere community. Issues and pull requests are always
welcome!

How to Test Your Code
---------------------

#. Setup your development environment as outlined above.
#. Run ``make like`` to lint your code.
#. Run ``make test`` to test your code.

Tests are run against Python 3.6, 3.7, 3.8, and 3.9.

Contributing Example Code
-------------------------

New example code should go into `troposphere/examples`. The expected
CloudFormation Template should be stored in `troposphere/tests/examples_output/`.
When tests are run the output of the code in the examples directory will
be compared with the expected results in the `example_output` directory.

.. _cloudtools-dev: https://groups.google.com/forum/#!forum/cloudtools-dev
