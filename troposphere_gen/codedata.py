from typing import Dict, Union

import re

from troposphere_gen.specification import Property, Resource


def module_name_from_namespace(namespace: str) -> str:
    """Parse module name from AWS namespace

    Examples:
    AWS::EC2::InternetGateway -> EC2
    AWS::EC2::LaunchTemplate.PrivateIpAdd -> EC2
    """
    match = re.match(r"(?:AWS|Alexa)::(.*)::.*", namespace)
    return match.group(1)


def class_name_from_property_name(propertyname: str) -> str:
    """Parse AWS namespaced property names to class names

    Example:
    AWS::WAF::SizeConstraintSet.FieldToMatch -> FieldToMatch
    """
    match = re.match(r"(?:AWS|Alexa)::.*::.*\.(.*)", propertyname)
    return match.group(1)


def class_name_from_resource_name(resourcename: str) -> str:
    """Parse AWS namespaced resource name to class name

    Example:
    AWS::WAF::SizeConstraintSet -> SizeConstraintSet
    """
    match = re.match(r"(?:AWS|Alexa)::.*::(.*)", resourcename)
    return match.group(1)


class ModuleData():
    """Convert multiple Specifications belonging to AWS Resource to module"""

    def __init__(self, name: str):
        self.modulename: str = name

        self.properties: Dict[str, ClassData] = {}
        self.resources: Dict[str, ClassData] = {}

    def add_property(self, name: str, property: Property) -> None:
        # Some properties are redefined for different Resources, but produce the exact same code.
        for existingname in self.properties:
            if class_name_from_property_name(existingname) == class_name_from_property_name(name):
                return
        self.properties[name] = ClassData(name, property)

    def add_resource(self, name: str, resource: Resource) -> None:
        # Some properties are redefined for different Resources, but produce the exact same code.
        for existingname in self.resources:
            if class_name_from_resource_name(existingname) == class_name_from_resource_name(name):
                return
        self.resources[name] = ClassData(name, resource)

    def resolve_name_conflicts(self):
        for prop in self.properties.values():
            for resource in self.resources.values():
                if prop.classname == resource.classname:
                    prop.classname += "Property"

class ClassData():
    """Convert Property or Resource to required classdata"""

    def __init__(self, name: str, data: Union[Property, Resource]) -> None:
        if type(data) is Property and data.common:
            self.classname: str = name
        elif type(data) is Property:
            self.classname: str = class_name_from_property_name(name)
        elif type(data) is Resource:
            self.classname: str = class_name_from_resource_name(name)
        self.data: Property = data

        self.subproperties: Dict[str, Property] = {}
        self.get_subproperties()

    def get_subproperties(self) -> None:
        """Gets all subproperties of property"""
        for name, prop in self.data.properties.items():
            self.subproperties[name] = prop
