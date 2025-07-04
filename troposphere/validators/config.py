# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from ..type_defs.compat import Final

ONE_HOUR: Final[str] = "One_Hour"
THREE_HOURS: Final[str] = "Three_Hours"
SIX_HOURS: Final[str] = "Six_Hours"
TWELVE_HOURS: Final[str] = "Twelve_Hours"
TWENTYFOUR_HOURS: Final[str] = "TwentyFour_Hours"


def validate_source_details(self):
    """
    Class: SourceDetails
    """

    valid_freqs = [
        ONE_HOUR,
        THREE_HOURS,
        SIX_HOURS,
        TWELVE_HOURS,
        TWENTYFOUR_HOURS,
    ]
    freq = self.properties.get("MaximumExecutionFrequency")
    if freq and freq not in valid_freqs:
        raise ValueError(
            "MaximumExecutionFrequency (given: %s) must be one of: %s"
            % (freq, ", ".join(valid_freqs))
        )
