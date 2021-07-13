import json
import os
import re
import unittest

from troposphere.template_generator import TemplateGenerator


class TestTemplateGenerator(unittest.TestCase):
    maxDiff = None

    # those are set by create_test_class
    filename = None
    expected_output = None

    def test_template_generator(self):
        """
        Ensures that all example outputs can be loaded into the
        template generator and back to JSON with no difference.
        """
        # we first get both outputs as JSON strings
        template = self.expected_output
        generated = TemplateGenerator(json.loads(template)).to_json()

        # then we make them into a dict for comparison
        template = json.loads(template)
        generated = json.loads(generated)

        self.assertDictEqual(template, generated)


def create_test_class(testname, **kwargs):
    klass = type(testname, (TestTemplateGenerator,), kwargs)
    return klass


def load_tests(loader, tests, pattern):
    EXCLUDE_EXAMPLES = ["OpenStack_AutoScaling.py", "OpenStack_Server.py"]
    # Filter out all *.py files from the examples directory
    examples = "examples"
    regex = re.compile(r".py$", re.I)
    example_filesnames = filter(regex.search, os.listdir(examples))

    suite = unittest.TestSuite()

    for f in example_filesnames:
        if f in EXCLUDE_EXAMPLES:
            continue
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
