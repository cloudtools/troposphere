# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


ONE_HOUR = "One_Hour"
THREE_HOURS = "Three_Hours"
SIX_HOURS = "Six_Hours"
TWELVE_HOURS = "Twelve_Hours"
TWENTYFOUR_HOURS = "TwentyFour_Hours"


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
