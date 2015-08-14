import unittest
from troposphere import Template
from troposphere import ecs


class TestDict(unittest.TestCase):
    def test_exclusive(self):
        d = {
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

        t = Template()
        cd = ecs.ContainerDefinition.from_dict("mycontainer", d)
        td = ecs.TaskDefinition(
                "taskdef",
                ContainerDefinitions=[cd],
                Volumes=[ecs.Volume(Name="myvol")],
        )
        t.add_resource(td)
        t.to_json()

if __name__ == '__main__':
    unittest.main()
