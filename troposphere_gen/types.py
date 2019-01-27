"""Types for Properties used in specification

Documentation: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification-format.html

Type classes take in type string from JSON specifications and outputs the
correct python-type corresponding to the specification-type. Subproperties
are resolved by the parser and the actual generated python class is filled in.
"""

from typing import Union


class BaseType():
    """Base Type all types inherit from"""
    pass


class PrimitiveType(BaseType):
    """Primitive type

    Primitive types are String, Long, Integer, Double, Boolean, Timestamp, JSON
    """

    def __init__(self, type: str):
        # Map is added here because AWS::ServiceDiscovery::Instance.InstanceAttributes has 'Map' as PrimitiveType
        # Remove it once AWS fixed this TODO: remove
        if type in ["String", "Long", "Integer", "Double", "Boolean", "Timestamp", "Json", "Map"]:
            self.type: str = type
        else:
            raise ValueError("Invalid primitive type: %s" % type)


class Subproperty(BaseType):
    """Subproperty type defined in other part of specification"""

    def __init__(self, type: str) -> None:
        self.type: str = type


class MapType(BaseType):
    """Map type

    Map of subproperties or primitives. The keys are always strings.
    """

    def __init__(self, itemtype: Union[Subproperty, PrimitiveType]) -> None:
        self.itemtype: Union[Subproperty, PrimitiveType] = itemtype


class ListType(BaseType):
    """List type

    List of subproperties or primitives.
    """

    def __init__(self, itemtype: Union[Subproperty, PrimitiveType]) -> None:
        self.itemtype: Union[Subproperty, PrimitiveType] = itemtype
