import os
import re
import sys
import unittest
from StringIO import StringIO

from functools import partial


class TestExamples(unittest.TestCase):
    pass


def _test_file(filename, expected_output):
    # capture the output
    saved = sys.stdout
    stdout = StringIO()
    try:
        sys.stdout = stdout
        with open(filename) as f:
            code = compile(f.read(), filename, 'exec')
            exec(code, {'__name__': '__main__'})
    finally:
        sys.stdout = saved
    # rewind fake stdout so we can read it
    stdout.seek(0)
    actual_output = stdout.read()
    assert expected_output == actual_output


def add_tests():
    # Filter out all *.py files from the examples directory
    examples = 'examples'
    regex = re.compile(r'.py$', re.I)
    example_filesnames = filter(regex.search, os.listdir(examples))

    # Add new test functions to the TestExamples class
    for f in example_filesnames:
        testname = 'test_' + f[:-3]
        expected_output = open('tests/examples_output/%s.template' %
                               f[:-3]).read()
        testfunc = partial(_test_file, examples + '/' + f, expected_output)
        # Get rid of partial() __doc__
        testfunc.__doc__ = None
        setattr(TestExamples, testname, testfunc)

add_tests()

if __name__ == '__main__':
    unittest.main()
