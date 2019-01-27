"""AWS Specification Resource Class

These classes parse an AWS CF specification as documented here:
https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-resource-specification-format.html
"""

from typing import Dict, Union
from troposphere_gen.types import PrimitiveType, Subproperty, MapType, ListType
from distutils.version import StrictVersion


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
        self.documentation: str = None
        self.duplicate_allowed: bool = None
        self.required: bool = None
        self._update_type: str = None
        self.properties: Dict[str, Property] = {}

        # If name isn't namespaced, property is common (example: Tag)
        self.common: bool = "::" not in name

        super(Property, self).__init__(name, propertydict)

    def parse(self, propertydict: Dict) -> None:
        """Parse JSON property definition"""
        if "Documentation" in propertydict:
            # Not all properties have documentation, for example
            # AWS::EC2::LaunchTemplate.CapacityReservationPreference
            self.documentation = propertydict["Documentation"]

        # If property contains subproperties, only parse those
        if "Properties" in propertydict:
            for name, subpropertydict in propertydict["Properties"].items():
                self.properties[name] = Property(name, subpropertydict)
            return

        if "UpdateType" in propertydict:
            self.update_type = propertydict["UpdateType"]
        if "Required" in propertydict:
            self.required = propertydict["Required"]

        super(Property, self).parse(propertydict)

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


class Resource():
    """Parsed resource"""

    def __init__(self, name: str, resourcedict: Dict) -> None:
        self.name: str = name
        self.documentation: str = None
        self.attributes: Dict[str, Attribute] = {}
        self.properties: Dict[str, Property] = {}

        self.parse(resourcedict)

    def parse(self, resourcedict: Dict) -> None:
        """Parse JSON resource definition"""
        self.documentation = resourcedict["Documentation"]

        for name, attributedict in resourcedict["Attributes"].items():
            self.attributes[name] = Attribute(name, attributedict)

        for name, propertydict in resourcedict["Properties"].items():
            self.properties[name] = Property(name, propertydict)


class Specification():
    def __init__(self, specificationdict: Dict) -> None:
        self.resource_specification_version: StrictVersion = None
        self.property_types: Dict[str, Property] = {}
        self.resource_types: Dict[str, Resource] = {}

        self.parse(specificationdict)

    def parse(self, specificationsdict: Dict) -> None:
        self.resource_specification_version = StrictVersion(specificationsdict["ResourceSpecificationVersion"])

        if "PropertyTypes" in specificationsdict:
            for name, attributedict in specificationsdict["PropertyTypes"].items():
                self.property_types[name] = Property(name, attributedict)

        if "ResourceType" in specificationsdict:
            for name, propertydict in specificationsdict["ResourceType"].items():
                self.resource_types[name] = Resource(name, propertydict)
