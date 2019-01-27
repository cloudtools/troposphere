"""A policy contains information on how code shall be generated from data

The policy determines how the specification data is converted to code. For
example it tells to use the 'print(foo)' syntax for python3 code, and use
'print foo' for python2 code.
"""

from troposphere_gen.codedata import ModuleData, ClassData
from troposphere_gen.specification import Property, Resource

import re

import datetime


def cc_to_sc(name: str) -> str:
    """Convert CamelCase to snake_case"""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class Policy():
    def __init__(self):
        pass

    def get_type(self, prop: Property) -> str:
        type_map = {
            "String": "str",
            "Long": "int",
            "Integer": "int",
            "Double": "float",
            "Boolean": "bool",
            "Timestamp": "str",  # TODO: Add Timestamp class to troposphere
            "Json": "Dict",
            "Map": "Dict"   # Workaround for AWS::ServiceDiscovery::Instance.InstanceAttributes, see types.py TODO: remove
        }

        if prop.primitive_type is not None:
            return type_map[prop.primitive_type.type]

    def module_head_format(self, moduledata: ModuleData):
        """Construct module code

        """
        modulename: str = moduledata.modulename

        # Copyright (c) 2012-2018, Mark Peek <mark@peek.org>
        # All rights reserved.
        #
        # See LICENSE file for full license.

        docstring = (
            f"\"\"\"Module for AWS {modulename} service\n"
            f"Copyright (c) 2012-{datetime.datetime.now().year}, Mark Peek <mark@peek.org>\n"
            f"All rights reserved.\n"
            f"\n"
            f"See LICENSE file for full license.\n"
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
            properties += f"        '{cc_to_sc(name)}': ({self.get_type(prop)}, {prop.required}),\n"

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
