"""Alphanumeric validator"""

from troposphere.validators.exceptions import TroposphereValidationError
import re

from typing import Union, List


def regex(value: str, *args, must_match: Union[List[str], str] = None, **kwargs):
    """Regex validator

    This validator uses regex patterns to check if the input string is valid.

    Arguments:
        must_match: Either a single regex pattern or a list of regex patterns, which must all match.

    Raises:
        TroposphereValidationError: If the rules passed via kwargs are violated, this exception is raised.
    """

    if must_match is not None and type(must_match) is not list:
        must_match = [must_match]
    if must_match is not None:
        for pattern in must_match:
            match = re.search(pattern, value)
            if not match:
                raise TroposphereValidationError(f"Input value '{value}' does not match pattern '{must_match}'")
