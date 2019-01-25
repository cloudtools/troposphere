"""AWS Specification Resource Class

These classes parse an AWS CF specification as documented here:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification-format.html
"""

from typing import Dict, Union
from troposphere_gen.types import PrimitiveType, Subproperty, MapType, ListType


class Attribute():
    """Parsed attribute"""

    def __init__(self, name: str, attributedict: Dict) -> None:
        self.name: str = name
        self.item_type: Subproperty = None
        self.primitive_item_type: PrimitiveType = None
        self.primitive_type: PrimitiveType = None
        self.type: Union[Subproperty, ListType, MapType] = None

        self.parse(attributedict)

    def parse(self, attributedict: Dict) -> None:
        """Parse JSON attribute definition"""
        # Determine type
        if "PrimitiveType" in attributedict:
            self.primitive_type = PrimitiveType(attributedict["PrimitiveType"])
        elif "Type" in attributedict:
            if attributedict["Type"] == "List":
                if "PrimitiveItemType" in attributedict:
                    self.type = ListType(PrimitiveType(attributedict["PrimitiveItemType"]))
                elif "ItemType" in attributedict:
                    self.type = ListType(Subproperty(attributedict["ItemType"]))
            elif attributedict["Type"] == "Map":
                if "PrimitiveItemType" in attributedict:
                    self.type = MapType(PrimitiveType(attributedict["PrimitiveItemType"]))
                elif "ItemType" in attributedict:
                    self.type = MapType(Subproperty(attributedict["ItemType"]))
            else:
                self.type = Subproperty(attributedict["Type"])


class Property(Attribute):
    """Parsed property"""

    def __init__(self, name: str, propertydict: Dict) -> None:
        super(Property, self).__init__(name, propertydict)
        self.documentation: str = None
        self.duplicate_allowed: bool = None
        self.required: bool = None
        self._update_type: str = None

        self.parse(propertydict)

    def parse(self, propertydict: Dict) -> None:
        """Parse JSON property definition"""
        super(Property, self).parse(propertydict)

        # Required fields for every property
        self.documentation = propertydict["Documentation"]
        self.update_type = propertydict["UpdateType"]
        self.required = propertydict["Required"]

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
