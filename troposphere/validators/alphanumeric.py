"""Alphanumeric validator"""

from troposphere.validators.exceptions import TroposphereValidationError
import re

alphanumeric_expr = re.compile("[^a-zA-Z0-9]")

def alphanumeric(input: str, *args, **kwargs):
    match = alphanumeric_expr.search(input)
    # If any non-alphanumeric characters are found, throw an exception
    if match:
        raise TroposphereValidationError(
            "Only alphanumeric characters (a-z A-Z 0-9) are allowed."
        )
