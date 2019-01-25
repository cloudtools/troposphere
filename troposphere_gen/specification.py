"""AWS Specification Resource Class

These classes parse an AWS CF specification as documented here:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification-format.html
"""

from typing import Dict, List, Union
from .types import PrimitiveType, Subproperty, MapType, ListType


class Property():
    """Parsed property"""

    def __init__(self, name: str, propertydict: Dict) -> None:
        self.name: str = name
        self.documentation: str = None
        self.duplicate_allowed: bool = None
        self.item_type: Subproperty = None
        self.primitive_item_type: PrimitiveType = None
        self.primitive_type: PrimitiveType = None
        self.required: bool = None
        self.type: Union[Subproperty, ListType, MapType] = None
        self._update_type: str = None

        self.parse(propertydict)

    def parse(self, propertydict: Dict) -> None:
        """Parse JSON property definition"""
        # Required fields for every property
        self.documentation = propertydict["Documentation"]
        self.update_type = propertydict["UpdateType"]
        self.required = propertydict["Required"]

        # Determine type
        if "PrimitiveType" in propertydict:
            self.primitive_type = PrimitiveType(propertydict["PrimitiveType"])
        elif "Type" in propertydict:
            if propertydict["Type"] == "List":
                if "PrimitiveItemType" in propertydict:
                    self.type = ListType(PrimitiveType(propertydict["PrimitiveItemType"]))
                elif "ItemType" in propertydict:
                    self.type = ListType(Subproperty(propertydict["ItemType"]))
            elif propertydict["Type"] == "Map":
                if "PrimitiveItemType" in propertydict:
                    self.type = MapType(PrimitiveType(propertydict["PrimitiveItemType"]))
                elif "ItemType" in propertydict:
                    self.type = MapType(Subproperty(propertydict["ItemType"]))
            else:
                self.type = Subproperty(propertydict["Type"])

        if "DuplicatesAllowed" in propertydict:
            self.duplicate_allowed = propertydict["DuplicatesAllowed"]

    @property
    def update_type(self) -> str:
        return self._update_type

    @update_type.setter
    def update_type(self, update_type: str) -> None:
        if update_type in ["Immutable", "Mutable", "Conditional"]:
            self._update_type = update_type
        else:
            raise ValueError("Invalid update type: %s" % update_type)
