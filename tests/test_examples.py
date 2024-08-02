import io
import os
import re
import sys


def test_example(input_filename, expected_output):
    saved = sys.stdout
    stdout = io.StringIO()
    try:
        sys.stdout = stdout
        with open(input_filename) as f:
            code = compile(f.read(), input_filename, "exec")
            exec(code, {"__name__": "__main__"})
    finally:
        sys.stdout = saved
    # rewind fake stdout so we can read it
    stdout.seek(0)
    actual_output = stdout.read()
    assert str(expected_output) == str(actual_output)


def load_example_tests():
    # Filter out all *.py files from the examples directory
    examples = "examples"
    regex = re.compile(r".py$", re.I)
    example_filenames = filter(regex.search, os.listdir(examples))

    results = []
    for f in example_filenames:
        expected_output = open("tests/examples_output/%s.template" % f[:-3]).read()
        results.append((examples + "/" + f, expected_output))

    return results


def pytest_generate_tests(metafunc):
    example_data = load_example_tests()
    metafunc.parametrize("input_filename,expected_output", example_data)
