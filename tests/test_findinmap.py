import unittest

from troposphere import BaseAWSObject, FindInMap

expected_find_in_map = {"Fn::FindInMap": ["m", "t", "s"]}

expected_find_in_map_with_default = {
    "Fn::FindInMap": ["m", "t", "s", {"DefaultValue": "d"}]
}

map_object = BaseAWSObject(title="m")


class TestFindInMap(unittest.TestCase):
    def test_find_in_map(self):
        find_in_map = FindInMap(mapname="m", toplevelkey="t", secondlevelkey="s")
        self.assertEqual(find_in_map.to_dict(), expected_find_in_map)

    def test_find_in_map_with_object(self):
        find_in_map = FindInMap(mapname=map_object, toplevelkey="t", secondlevelkey="s")
        self.assertEqual(find_in_map.to_dict(), expected_find_in_map)

    def test_find_in_map_with_default(self):
        find_in_map = FindInMap(
            mapname="m", toplevelkey="t", secondlevelkey="s", defaultvalue="d"
        )
        self.assertEqual(find_in_map.to_dict(), expected_find_in_map_with_default)

    def test_find_in_map_with_object_and_default(self):
        find_in_map = FindInMap(
            mapname=map_object, toplevelkey="t", secondlevelkey="s", defaultvalue="d"
        )
        self.assertEqual(find_in_map.to_dict(), expected_find_in_map_with_default)


if __name__ == "__main__":
    unittest.main()
