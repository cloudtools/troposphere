"""A policy contains information on how code shall be generated from data

The policy determines how the specification data is converted to code. For
example it tells to use the 'print(foo)' syntax for python3 code, and use
'print foo' for python2 code.
"""

from troposphere_gen.codedata import ModuleData, ClassData
from troposphere_gen.specification import Property, Resource, Specification
from troposphere_gen.types import ListType, MapType, PrimitiveType, Subproperty
from troposphere_gen.validatordata import ValidatorData

import re

import datetime

from typing import Union


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

    def get_type(self, prop: Property, deconflict: bool = False) -> str:
        deconflicter: str = ""
        if deconflict:
            deconflicter = "Property"

        if prop.primitive_type is not None:
            return Policy_3_7.type_map[prop.primitive_type.type]
        else:
            if type(prop.type) == ListType:
                if prop.type.itemtype.type in Policy_3_7.type_map:
                    return f"List[{Policy_3_7.type_map[prop.type.itemtype.type]}{deconflicter}]"
                else:
                    return f"List[{prop.type.itemtype.type}{deconflicter}]"
            elif type(prop.type) == MapType:
                if prop.type.itemtype.type in Policy_3_7.type_map:
                    return f"Dict[str, {Policy_3_7.type_map[prop.type.itemtype.type]}{deconflicter}]"
                else:
                    return f"Dict[str, {prop.type.itemtype.type}]{deconflicter}"
            else:
                return f"{prop.type.type}{deconflicter}"

    def get_itemtype(self, listmap: Union[ListType, MapType], deconflict: bool = False) -> str:
        deconflicter: str = ""
        if deconflict:
            deconflicter = "Property"

        itemtype: Union[Subproperty, PrimitiveType] = listmap.itemtype
        if type(itemtype) is Subproperty:
            return itemtype.type + deconflicter
        elif type(itemtype) is PrimitiveType:
            return Policy_3_7.type_map[itemtype.type]

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

        imports = "\nfrom troposphere.aws_objects import AWSProperty, AWSObject\n"
        imports += "from typing import Dict, List\n"
        imports += "from troposphere import validators\n"
        if modulename is not "common":
            imports += "from troposphere.common import Tag\n"

        modulecode = docstring + imports

        return modulecode

    def class_format(self, classdata: ClassData) -> str:
        """Construct class code

        """

        # Determine type of class
        if type(classdata.data) is Property:
            parentclass: str = "AWSProperty"
        elif type(classdata.data) is Resource:
            parentclass: str = "AWSObject"

        # Determine list of properties relevant for Property/Resource
        prop_dict: str = ""
        for name, prop in classdata.subproperties.items():
            conflicted = name in classdata.conflictedproperties
            prop_dict += f"        '{cc_to_sc(name)}': {self.get_type(prop, conflicted)},\n"

        # Generate init signature
        init_code = "    def __init__(self,\n"
        for name, prop in classdata.subproperties.items():
            conflicted = name in classdata.conflictedproperties
            init_code += f"                 {cc_to_sc(name)}: {self.get_type(prop, conflicted)} = None,\n"
        init_code += "                 ):\n"

        # Generate field declarations
        for name, prop in classdata.subproperties.items():
            conflicted = name in classdata.conflictedproperties
            init_code += f"        self._{cc_to_sc(name)}: {self.get_type(prop, conflicted)} = None\n"
            init_code += f"        self.{cc_to_sc(name)} = {cc_to_sc(name)}\n"

        property_funcs = ""
        for name, prop in classdata.subproperties.items():
            conflicted = name in classdata.conflictedproperties

            property_funcs += self.between_functions()
            property_funcs += self.property_getter(prop, conflicted)
            property_funcs += self.between_functions()
            property_funcs += self.property_setter(prop, classdata, conflicted)

        classcode = (
            f"class {classdata.classname}({parentclass}):\n"
            f"    props = {{\n"
            f"{prop_dict}"
            f"    }}\n"
            f"\n"
            f"{init_code}"
            f"{property_funcs}"
        )

        return classcode

    def property_getter(self, propertydata: Property, conflicted: bool) -> str:
        return (
            f"    @property\n"
            f"    def {cc_to_sc(propertydata.name)}(self) -> {self.get_type(propertydata, conflicted)}:\n"
            f"        return self._{cc_to_sc(propertydata.name)}\n"
        )

    def property_setter(self, propertydata: Property, classdata: ClassData, conflicted: bool) -> str:
        # Generate type-checker
        if type(propertydata.type) == ListType:
            type_check = (
                f"        if not isinstance(value, list):\n"
                f"            raise ValueError(\"{cc_to_sc(propertydata.name)} must be of type 'list' (is: '%s')\" % type(value))\n"
                f"        for listitem in value:\n"
                f"            if not isinstance(listitem, {self.get_itemtype(propertydata.type)}):\n"
                f"                raise ValueError(\"{cc_to_sc(propertydata.name)} list-items must be of type '{self.get_itemtype(propertydata.type)}' (is: '%s')\" % type(listitem))\n"
            )
            if classdata.validatordata is not None and propertydata.name in classdata.validatordata.validators:
                type_check += f"            validators.{classdata.validatordata.validators[propertydata.name].function}(value, self"
                for k, v in classdata.validatordata.validators[propertydata.name].kwargs.items():
                    type_check += f", {k}=\"{v}\""
                type_check += f")\n"
        elif type(propertydata.type) == MapType:
            type_check = (
                f"        if not isinstance(value, dict):\n"
                f"            raise ValueError(\"'{cc_to_sc(propertydata.name)}' must be of type 'dict' (is: '%s')\" % type(value))\n"
                f"        for k, v in value.items():\n"
                f"            if not isinstance(k, str):\n"
                f"                raise ValueError(\"{cc_to_sc(propertydata.name)} map-keys must be of type 'str' (is: '%s')\" % type(k))\n"
                f"            if not isinstance(v, {self.get_itemtype(propertydata.type)}):\n"
                f"                raise ValueError(\"{cc_to_sc(propertydata.name)} map-values must be of type '{self.get_itemtype(propertydata.type)}' (is: '%s')\" % type(v))\n"
            )
            if classdata.validatordata is not None and propertydata.name in classdata.validatordata.validators:
                type_check += f"            validators.{classdata.validatordata.validators[propertydata.name].map_key_function}(k, self"
                for k, v in classdata.validatordata.validators[propertydata.name].map_key_kwargs.items():
                    type_check += f", {k}=\"{v}\""
                type_check += f")\n"
                type_check += f"            validators.{classdata.validatordata.validators[propertydata.name].map_value_function}(v, self"
                for k, v in classdata.validatordata.validators[propertydata.name].map_value_kwargs.items():
                    type_check += f", {k}=\"{v}\""
                type_check += f")\n"
        else:  # Subproperty or primitive type
            type_check = (
                f"        if not isinstance(value, {self.get_type(propertydata, conflicted)}):\n"
                f"            raise ValueError(\"{cc_to_sc(propertydata.name)} must be of type '{self.get_type(propertydata, conflicted)}' (is: '%s')\" % type(value))\n"
            )
            if classdata.validatordata is not None and propertydata.name in classdata.validatordata.validators:
                type_check += f"        validators.{classdata.validatordata.validators[propertydata.name].function}(value, self"
                for k, v in classdata.validatordata.validators[propertydata.name].kwargs.items():
                    type_check += f", {k}=\"{v}\""
                type_check += f")\n"

        return (
            f"    @{cc_to_sc(propertydata.name)}.setter\n"
            f"    def {cc_to_sc(propertydata.name)}(self, value: {self.get_type(propertydata, conflicted)}) -> None:\n"
            f"        if value is None:\n"
            f"            self._{cc_to_sc(propertydata.name)} = None\n"
            f"            return\n"
            f"{type_check}"
            f"        self._{cc_to_sc(propertydata.name)} = value\n"
        )

    def between_class(self) -> str:
        return "\n\n"

    def between_functions(self) -> str:
        return "    \n"

    def after_import(self) -> str:
        return "\n\n"


class Policy_2_7(Policy):
    def get_type(self, prop: Property, deconflict: bool = False) -> str:
        type_map = {
            "String": "basestring",
            "Long": "int",
            "Integer": "int",
            "Double": "float",
            "Boolean": "boolean",
            "Timestamp": "basestring",  # TODO: Add Timestamp class to troposphere
            "Json": "dict",
            "Map": "dict"
            # Workaround for AWS::ServiceDiscovery::Instance.InstanceAttributes, see types.py TODO: remove
        }

        deconflicter: str = ""
        if deconflict:
            deconflicter = "Property"

        if prop.primitive_type is not None:
            return type_map[prop.primitive_type.type]
        else:
            if type(prop.type) == ListType:
                return "list"
            elif type(prop.type) == MapType:
                return "dict"
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
