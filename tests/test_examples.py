import os
import re
import sys
import unittest

from functools import partial


class TestExamples(unittest.TestCase):
    pass


def test_file(filename):
    # Ignore the output
    saved = sys.stdout
    sys.stdout = open('/dev/null', 'w')
    try:
        execfile(filename)
    finally:
        sys.stdout = saved


def add_tests():
    # Filter out all *.py files from the examples directory
    examples = 'examples'
    regex = re.compile(r'.py$', re.I)
    example_filesnames = filter(regex.search, os.listdir(examples))

    # Add new test functions to the TestExamples class
    for f in example_filesnames:
        testname = 'test_' + f[:-3]
        testfunc = partial(test_file, examples + '/' + f)
        # Get rid of partial() __doc__
        testfunc.__doc__ = None
        setattr(TestExamples, testname, testfunc)

add_tests()

if __name__ == '__main__':
    unittest.main()
