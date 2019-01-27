"""A policy contains information on how code shall be generated from data

The policy determines how the specification data is converted to code. For
example it tells to use the 'print(foo)' syntax for python3 code, and use
'print foo' for python2 code.
"""

from troposphere_gen.codedata import ModuleData, ClassData
from troposphere_gen.specification import Property, Resource, Specification
from troposphere_gen.types import ListType, MapType

import re

import datetime


def cc_to_sc(name: str) -> str:
    """Convert CamelCase to snake_case"""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class Policy():
    def get_type(self, prop: Property, deconflict: bool = False) -> str:
        pass

    def module_head_format(self, moduledata: ModuleData, specification: Specification):
        pass

    def class_format(self, classdata: ClassData) -> str:
        pass

    def between_class(self) -> str:
        pass

    def after_import(self) -> str:
        pass


class Policy_3_7(Policy):
    def get_type(self, prop: Property, deconflict: bool = False) -> str:
        type_map = {
            "String": "str",
            "Long": "int",
            "Integer": "int",
            "Double": "float",
            "Boolean": "bool",
            "Timestamp": "str",  # TODO: Add Timestamp class to troposphere
            "Json": "Dict",
            "Map": "Dict"
        # Workaround for AWS::ServiceDiscovery::Instance.InstanceAttributes, see types.py TODO: remove
        }

        deconflicter: str = ""
        if deconflict:
            deconflicter = "Property"

        if prop.primitive_type is not None:
            return type_map[prop.primitive_type.type]
        else:
            if type(prop.type) == ListType:
                if prop.type.itemtype.type in type_map:
                    return f"List[{type_map[prop.type.itemtype.type]}{deconflicter}]"
                else:
                    return f"List[{prop.type.itemtype.type}{deconflicter}]"
            elif type(prop.type) == MapType:
                if prop.type.itemtype.type in type_map:
                    return f"Dict[str, {type_map[prop.type.itemtype.type]}{deconflicter}]"
                else:
                    return f"Dict[str, {prop.type.itemtype.type}]{deconflicter}"
            else:
                return f"{prop.type.type}{deconflicter}"

    def module_head_format(self, moduledata: ModuleData, specification: Specification):
        """Construct module code

        """
        modulename: str = moduledata.modulename

        # Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
        # All rights reserved.
        #
        # See LICENSE file for full license.

        versionstring = str(specification.resource_specification_version)
        if specification.resource_specification_version.version[2] == 0:
            # StrictVersion doesn't print patch if it's 0
            versionstring += ".0"

        docstring = (
            f"\"\"\"Module for AWS {modulename} service\n"
            f"Copyright (c) 2012-{datetime.datetime.now().year}, Mark Peek <mark@peek.org>\n"
            f"All rights reserved.\n"
            f"\n"
            f"See LICENSE file for full license.\n"
            f"\n"
            f"AUOTGENERATED CODE, DO NOT EDIT!\n"
            f"Generated from Specification Version {versionstring}\n"
            f"\"\"\"\n"
        )

        imports = "\nfrom troposphere import AWSProperty, AWSObject\n"
        imports += "from typing import Dict, List\n"
        if modulename is not "common":
            imports += "from troposphere.common import Tag\n"

        modulecode = docstring + imports

        return modulecode

    def class_format(self, classdata: ClassData) -> str:
        """Construct class code

        """

        if type(classdata.data) is Property:
            parentclass: str = "AWSProperty"
        elif type(classdata.data) is Resource:
            parentclass: str = "AWSObject"

        properties: str = ""
        for name, prop in classdata.subproperties.items():
            conflicted = name in classdata.conflictedproperties
            properties += f"        '{cc_to_sc(name)}': ({self.get_type(prop, conflicted)}, {prop.required}),\n"

        classcode = (
            f"class {classdata.classname}({parentclass}):\n"
            f"    props = {{\n"
            f"{properties}"
            f"    }}\n"
        )

        return classcode

    def between_class(self) -> str:
        return "\n\n"

    def after_import(self) -> str:
        return "\n\n"
