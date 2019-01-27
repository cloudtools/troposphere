from typing import Dict, Union, List

import re

from troposphere_gen.specification import Property, Resource
from troposphere_gen.types import ListType, MapType

from collections import OrderedDict

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

        self.conflictednames: List[str] = []    # List of conflicted properties

        self.properties: OrderedDict[str, ClassData] = OrderedDict()
        self.resources: OrderedDict[str, ClassData] = OrderedDict()

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
        # Detect if any property has the same name as resource
        # If yes, append 'Property' to the class name
        for cd in self.properties.values():
            for resource in self.resources.values():
                if cd.classname == resource.classname:
                    self.conflictednames.append(cd.classname)
                    cd.classname += "Property"

        # Now we have to replace all occurences of this Property with the
        # adjusted name
        for cd in self.properties.values():
            for name, subprop in cd.subproperties.items():
                if type(subprop.type) is ListType or type(subprop.type) is MapType:
                    if subprop.type.itemtype.type in self.conflictednames:
                        cd.conflictedproperties.append(name)

    def resolve_dependencies(self):
        """Make sure classes are defined before they are referenced by other classes"""
        for i in range(100):    # Make 100 attemps to fix dependencies
            # Check if property references subproperty of following properties
            # * Iterate over all properties
            # * Check if any of the properties coming AFTER current property is
            #   referenced by checkprop
            # * If yes, move checkprop to end of properties
            # * Do 100 attempts at bubble-sort-ish resolving before failing
            done = True     # Done if clean runthrough with no deps is achieved
            propertiescopy = self.properties.copy()
            for checkidx, checkitem in enumerate(propertiescopy.items()):
                checkname, checkprop = checkitem
                for idx, prop in enumerate(propertiescopy.values()):
                    if idx <= checkidx:  # Gone past check prop
                        continue
                    for subidx, subprop in enumerate(checkprop.subproperties.values()):
                        if subprop.type is not None:
                            if type(subprop.type) is ListType or type(subprop.type) is MapType:
                                if subprop.type.itemtype.type == prop.classname:
                                    self.properties.move_to_end(checkname, last=True)
                                    done = False
                            elif subprop.type.type == prop.classname:
                                self.properties.move_to_end(checkname, last=True)
                                done = False
                    if done is False:
                        # Something was moved, continue with next item
                        break
            if done:
                break
        else:   # Only triggered if for-loop finishes without break!
            raise Exception(f"Couldn't resolve possible dependency cycle in {self.modulename}")

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

        self.conflictedproperties: List[str] = []

        self.subproperties: Dict[str, Property] = {}
        self.get_subproperties()

    def get_subproperties(self) -> None:
        """Gets all subproperties of property"""
        for name, prop in self.data.properties.items():
            self.subproperties[name] = prop
