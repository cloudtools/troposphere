#!/usr/bin/python

from troposphere import Base64, Join


def from_file(filepath, delimiter='', blanklines=False):
    """
    Imports userdata from a file.
    Also supports passing Troposphere Ref function

    :type filepath: string
    :param filepath
    The absolute path to the file.

    :type delimiter: string
    :param: delimiter
    Delimiter to use with the troposphere.Join().

    :type blanklines: boolean
    :param blanklines
    If blank lines shoud be ignored

    rtype: troposphere.Base64
    :return The base64 representation of the file.
    """

    ref_pattern = re.compile('(?P<prefix>.*)Ref\(\'(?P<reference>[a-zA-Z0-9\:]+)\'\)(?P<suffix>.*[^\\*])')
    data = []

    try:
        with open(filepath, 'r') as f:
            for line in f:
                if blanklines and line.strip('\n\r ') == '':
                    continue

                ref_ex = ref_pattern.match(line)

                if ref_ex:
                    data.append(ref_ex.group('prefix'))
                    data.append(Ref(ref_ex.group('reference')))

                    if ref_ex.group('suffix'):
                        data.append(ref_ex.group('suffix'))
                        continue

                else:
                    data.append(line)
    except IOError:
        raise IOError('Error opening or reading file: {}'.format(filepath))

    return Base64(Join(delimiter, data))
