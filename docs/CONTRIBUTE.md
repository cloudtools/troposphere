# How to Contribute to Troposphere

## tl;dr
1. Fork https://github.com/cloudtools/troposphere
1. Make the code better
1. Make the code pass tests
1. Create a Pull Request

## How to Get Help

See README.md at top of the project for developer mailing list.

## How to Test Your Code

1. Create a virtualenv (e.g. `virtualenv troposphere-env`)
1. Install modules
  1. `pip install pep8`
  1. `pip install pyflakes`
  1. `pip install awacs`
1. Run `python -m unittest discover tests`
