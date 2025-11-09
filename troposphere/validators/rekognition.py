# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from .. import AWSProperty, PropsDictType
from . import double


class Point(AWSProperty):
    """
    Export:
    """

    props: PropsDictType = {
        "X": (double, True),
        "Y": (double, True),
    }


def validate_PolygonRegionsOfInterest(polygons):
    """
    Property: StreamProcessor.PolygonRegionsOfInterest
    """

    if not isinstance(polygons, list):
        raise TypeError("PolygonRegionsOfInterest must be a list")

    all_lists = all(isinstance(item, list) for item in polygons)
    if not all_lists:
        raise TypeError("PolygonRegionsOfInterest must be a list of lists")

    all_points = all(
        isinstance(point, Point) for sublist in polygons for point in sublist
    )
    if not all_points:
        raise TypeError("PolygonRegionsOfInterest must be a list of lists of ponts")
