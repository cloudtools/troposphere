import json
import os
import re
import unittest

from troposphere.template_generator import TemplateGenerator


def test_template_generator(input_filename, expected_output):
    """
    Ensures that all example outputs can be loaded into the
    template generator and back to JSON with no difference.
    """
    # we first get both outputs as JSON strings
    template = expected_output
    generated = TemplateGenerator(json.loads(template)).to_json()

    # then we make them into a dict for comparison
    template = json.loads(template)
    generated = json.loads(generated)

    assert template == generated


def load_example_tests():
    EXCLUDE_EXAMPLES = ["OpenStack_AutoScaling.py", "OpenStack_Server.py"]
    # Filter out all *.py files from the examples directory
    examples = "examples"
    regex = re.compile(r".py$", re.I)
    example_filesnames = filter(regex.search, os.listdir(examples))

    results = []
    for f in example_filesnames:
        if f in EXCLUDE_EXAMPLES:
            continue
        filename = "tests/examples_output/%s.template" % f[:-3]
        expected_output = open(filename).read()
        results.append((filename, expected_output))

    return results


def pytest_generate_tests(metafunc):
    example_data = load_example_tests()
    metafunc.parametrize("input_filename,expected_output", example_data)


if __name__ == "__main__":
    unittest.main()
