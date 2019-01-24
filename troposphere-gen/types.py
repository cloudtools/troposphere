"""Types for Properties used in specification

Documentation: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification-format.html

Type classes take in type string from JSON specifications and outputs the
correct python-type corresponding to the specification-type. Subproperties
are resolved by the parser and the actual generated python class is filled in.
"""

from typing import Union

type_map = {
    "String": str,
    "Long": int,
    "Integer": int,
    "Double": float,
    "Boolean": bool,
    "Timestamp": str,
    "Json": dict
}


class BaseType():
    """Base Type all types inherit from"""

    def __init__(self):
        raise NotImplementedError


class PrimitiveType(BaseType):
    """Primitive type

    Primitive types are String, Long, Integer, Double, Boolean, or Timestamp.
    """

    def __init__(self, type: str):
        super(PrimitiveType, self).__init__()
        if type in type_map:
            self.type = type_map[type]  # type: type
        else:
            raise ValueError("Unknown type: %s" % type)

    def __str__(self) -> str:
        return self.type.__name__


class Subproperty(BaseType):
    """Subproperty type defined in other part of specification"""

    def __init__(self, type: str) -> None:
        super(Subproperty, self).__init__()
        self.type = type  # type: str
        self.print_class = None  # type: type

    def __str__(self) -> str:
        return self.print_class.__name__


class Map(BaseType):
    """Map type

    Map of subproperties or primitives. The keys are always strings.
    """

    def __init__(self, itemtype: Union[Subproperty, PrimitiveType]) -> None:
        super(Map, self).__init__()
        self.itemtype = itemtype  # type: Union[Subproperty, PrimitiveType]

    def __str__(self) -> str:
        return "Dict[str, %s]" % self.itemtype


class List(BaseType):
    """List type

    List of subproperties or primitives.
    """

    def __init__(self, itemtype: Union[Subproperty, PrimitiveType]) -> None:
        super(List, self).__init__()
        self.itemtype = itemtype  # type: Union[Subproperty, PrimitiveType]

    def __str__(self) -> str:
        return "List[%s]" % self.itemtype
