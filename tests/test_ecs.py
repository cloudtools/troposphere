import unittest
from troposphere import Ref
import troposphere.ecs as ecs


class TestECS(unittest.TestCase):

    def test_allow_string_cluster(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
            Volumes=[
                ecs.Volume(Name="my-vol"),
            ],
        )
        ecs_service = ecs.Service(
            'Service',
            Cluster='cluster',
            DesiredCount=2,
            TaskDefinition=Ref(task_definition),
        )

        ecs_service.JSONrepr()

    def test_allow_ref_cluster(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
            Volumes=[
                ecs.Volume(Name="my-vol"),
            ],
        )
        cluster = ecs.Cluster("mycluster")
        ecs_service = ecs.Service(
            'Service',
            Cluster=Ref(cluster),
            DesiredCount=2,
            TaskDefinition=Ref(task_definition),
        )

        ecs_service.JSONrepr()

    def test_all_container_definition_options(self):
        container_def = ecs.ContainerDefinition(
            Command=['option1', 'option2'],
            Cpu="100",
            DisableNetworking=False,
            DnsSearchDomains=["domain1", "domain2"],
            DnsServers=["server1", "server2"],
            DockerSecurityOptions=["option1", "option2"],
            EntryPoint=["run", "this"],
            Environment=[ecs.Environment(Name="Env", Value="var")],
            ExtraHosts=[ecs.ExtraHost(Hostname="Foo", IpAddress="127.0.0.1")],
            Essential=True,
            Hostname="myHost",
            Image="myimage",
            Links=["name:name"],
            Memory="300",
            MountPoints=[ecs.MountPoint(
                ContainerPath="/path", SourceVolume="Volume", ReadOnly=True)
            ],
            Name="mycontainer",
            PortMappings=[ecs.PortMapping(
                ContainerPort=2000, HostPort=3000, Protocol="udp")
            ],
            Privileged=True,
            ReadonlyRootFilesystem=True,
            User="user",
            ULimits=[ecs.ULimit(Name="core", SoftLimit=1, HardLimit=2)],
            VolumesFrom=[
                ecs.VolumesFrom(SourceContainer="Container", ReadOnly=True)
            ],
            Workingdirectory="/path/"
        )

        container_def.JSONrepr()
