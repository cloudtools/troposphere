import unittest
from troposphere import Template, Ref
from troposphere import ecs
from troposphere import iam


class TestDict(unittest.TestCase):
    def setUp(self):
        self.d = {
            "Cpu": 1,
            "Environment": [
                {
                    "Name": "REGISTRY_STORAGE",
                    "Value": "s3"
                },
                {
                    "Name": "REGISTRY_STORAGE_S3_REGION",
                    "Value": "eu-west-1"
                }
            ],
            "Essential": True,
            "Image": "registry:2",
            "Memory": 500,
            "Name": "registry",
            "PortMappings": [
                {
                    "ContainerPort": 5000,
                    "HostPort": 5000
                },
                {
                    "ContainerPort": 5001,
                    "HostPort": 5001
                }
            ]
        }

    def test_exclusive(self):
        t = Template()
        cd = ecs.ContainerDefinition.from_dict("mycontainer", self.d)
        td = ecs.TaskDefinition(
                "taskdef",
                ContainerDefinitions=[cd],
                Volumes=[ecs.Volume(Name="myvol")],
                TaskRoleArn=Ref(iam.Role("myecsrole"))
        )
        t.add_resource(td)
        t.to_json()

    def test_invalid_toplevel_property(self):
        self.d["BlahInvalid"] = "Invalid"
        with self.assertRaises(AttributeError):
            ecs.ContainerDefinition.from_dict("mycontainer", self.d)

    def test_invalid_sub_property(self):
        self.d["Environment"][0]["BlahInvalid"] = "Invalid"
        with self.assertRaises(AttributeError):
            ecs.ContainerDefinition.from_dict("mycontainer", self.d)


if __name__ == '__main__':
    unittest.main()
