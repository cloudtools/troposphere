import collections
import importlib
import pkgutil
import unittest

from troposphere import AWSObject


class TestIntTypeShouldNotBeUsed(unittest.TestCase):
    def test_there_should_not_be_any_awsobject_with_int_in_props(self):
        """
        Anything that requires an integer should use `validators.integer`
        rather than `int`, because `int` does not work with types
        that behave like an integer (i.e. `long` in Python 2).
        """
        aws_objects = self.get_aws_objects()
        for obj in aws_objects:
            self.assertNoIntType(obj)

    def get_aws_objects(self):
        result = []
        modules = self._import_all_modules()
        for module in modules:
            for name in dir(module):
                obj = getattr(module, name)
                if (
                    isinstance(obj, type)
                    and obj != AWSObject
                    and issubclass(obj, AWSObject)
                ):
                    result.append(obj)
        return result

    def assertNoIntType(self, obj):
        for prop_name, (types, required) in obj.props.items():
            error_msg = (
                "{}.props['{}'] should have `validators.integer` "
                "rather than `int`".format(obj.__name__, prop_name)
            )
            if isinstance(types, collections.abc.Iterable):
                assert int not in types, error_msg
            else:
                assert types != int, error_msg

    def _get_all_troposphere_modules(self, dirname):
        return [
            pkg_name
            for importer, pkg_name, is_pkg in pkgutil.walk_packages([dirname])
            if not is_pkg and pkg_name.startswith("troposphere")
        ]

    def _import_all_modules(self):
        module_names = self._get_all_troposphere_modules(".")
        return [importlib.import_module(m) for m in module_names]
