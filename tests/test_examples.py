import io
import os
import re
import sys
import unittest


class TestExamples(unittest.TestCase):
    maxDiff = None

    # those are set by create_test_class
    filename = None
    expected_output = None

    def test_example(self):
        saved = sys.stdout
        stdout = io.StringIO()
        try:
            sys.stdout = stdout
            with open(self.filename) as f:
                code = compile(f.read(), self.filename, "exec")
                exec(code, {"__name__": "__main__"})
        finally:
            sys.stdout = saved
        # rewind fake stdout so we can read it
        stdout.seek(0)
        actual_output = stdout.read()
        self.assertEqual(str(self.expected_output), str(actual_output))


def create_test_class(testname, **kwargs):
    klass = type(testname, (TestExamples,), kwargs)
    return klass


def load_tests(loader, tests, pattern):
    # Filter out all *.py files from the examples directory
    examples = "examples"
    regex = re.compile(r".py$", re.I)
    example_filesnames = filter(regex.search, os.listdir(examples))

    suite = unittest.TestSuite()

    for f in example_filesnames:
        testname = "test_" + f[:-3]
        expected_output = open("tests/examples_output/%s.template" % f[:-3]).read()
        test_class = create_test_class(
            testname, filename=examples + "/" + f, expected_output=expected_output
        )
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    return suite


if __name__ == "__main__":
    unittest.main()
