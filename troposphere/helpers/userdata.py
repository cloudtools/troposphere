#!/usr/bin/python

from troposphere import Base64, Join


def from_file(filepath, whitespace=False):
    """Imports userdata from a file.

    This function ignore blank lines within the file.
    Special characters are automatically escaped.

    Args:
        filepath (string): The absolute path to the file
        containing the userdata to be imported.

    Returns:
        Base64 object: The Base64 object being passed a Join object
        with strings.
        If file not found, an empty string list is used.

    """

    data = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                data.append(line)
    except IOError:
        raise IOError('Error opening or reading file: ' + filepath)

    return Base64(Join(',', data))
