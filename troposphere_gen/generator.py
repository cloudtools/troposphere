"""Generator that takes data parsed from specification and generates code

The code generator takes data parsed from specification, and converts it into
modules with classes. The code style is dictated by the policy used.
"""

from troposphere_gen.specification import Specification
from troposphere_gen.codedata import ModuleData
from troposphere_gen.codedata import module_name_from_namespace

from typing import Dict

# Some services are named after reserved keywords or require other exceptions
modname_exceptions = {
    "Lambda": "AwsLambda"
}


class Generator():
    def __init__(self, specification: Specification):
        self.specification: Specification = specification

        self.modules: Dict[str, ModuleData] = {}

        self.gen_property_classdata()
        self.gen_resource_classdata()

    def gen_property_classdata(self):
        """Generates class data for each property and adds it to module"""
        for name, property in self.specification.property_types.items():
            moddata = self.get_module(name)

            moddata.add_property(name, property)

    def gen_resource_classdata(self):
        """Generates class data for each property and adds it to module"""
        for name, resource in self.specification.resource_types.items():
            moddata = self.get_module(name)

            moddata.add_resource(name, resource)

    def get_module(self, name: str) -> ModuleData:
        """Find or create module from namespaced name"""
        if not "::" in name:
            # Some properties aren't namespaced, for example 'Tag'
            modname = "common"
        else:
            modname = module_name_from_namespace(name)

        if modname in modname_exceptions:
            modname = modname_exceptions[modname]

        if modname not in self.modules:
            self.modules[modname] = ModuleData(modname)

        return self.modules[modname]
