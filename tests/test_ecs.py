import unittest

import troposphere.ecs as ecs
from troposphere import Ref, iam


class TestECS(unittest.TestCase):
    def test_allow_placement_strategy_constraint(self):
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
            "Service",
            Cluster="cluster",
            DesiredCount=2,
            PlacementStrategies=[
                ecs.PlacementStrategy(
                    Type="random",
                )
            ],
            PlacementConstraints=[
                ecs.PlacementConstraint(
                    Type="distinctInstance",
                )
            ],
            TaskDefinition=Ref(task_definition),
        )

        ecs_service.to_dict()

    def test_allow_scheduling_strategy(self):
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
            "Service",
            Cluster="cluster",
            DesiredCount=2,
            TaskDefinition=Ref(task_definition),
            SchedulingStrategy=ecs.SCHEDULING_STRATEGY_DAEMON,
        )

        ecs_service.to_dict()

    def test_fargate_launch_type(self):
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
            "Service",
            Cluster="cluster",
            DesiredCount=2,
            PlacementStrategies=[
                ecs.PlacementStrategy(
                    Type="random",
                )
            ],
            LaunchType="FARGATE",
            NetworkConfiguration=ecs.NetworkConfiguration(
                AwsvpcConfiguration=ecs.AwsvpcConfiguration(
                    AssignPublicIp="DISABLED",
                    SecurityGroups=["sg-1234"],
                    Subnets=["subnet-1234"],
                )
            ),
            PlacementConstraints=[
                ecs.PlacementConstraint(
                    Type="distinctInstance",
                )
            ],
            TaskDefinition=Ref(task_definition),
        )

        ecs_service.to_dict()

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
            "Service",
            Cluster="cluster",
            DesiredCount=2,
            TaskDefinition=Ref(task_definition),
        )

        ecs_service.to_dict()

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
            "Service",
            Cluster=Ref(cluster),
            DesiredCount=2,
            TaskDefinition=Ref(task_definition),
        )

        ecs_service.to_dict()

    def test_task_role_arn_is_optional(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
        )

        task_definition.to_dict()

    def test_allow_string_task_role_arn(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
            TaskRoleArn="myiamrole",
        )

        task_definition.to_dict()

    def test_allow_ref_task_role_arn(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
            TaskRoleArn=Ref(iam.Role("myRole")),
        )

        task_definition.to_dict()

    def test_allow_port_mapping_protocol(self):
        container_definition = ecs.ContainerDefinition(
            Image="myimage",
            Memory="300",
            Name="mycontainer",
            PortMappings=[
                ecs.PortMapping(ContainerPort=8125, HostPort=8125, Protocol="udp")
            ],
        )

        container_definition.to_dict()

    def test_port_mapping_does_not_require_protocol(self):
        container_definition = ecs.ContainerDefinition(
            Image="myimage",
            Memory="300",
            Name="mycontainer",
            PortMappings=[
                ecs.PortMapping(
                    ContainerPort=8125,
                    HostPort=8125,
                )
            ],
        )

        container_definition.to_dict()

    def test_allow_container_healthcheck(self):
        health_check_def = ecs.HealthCheck(
            Command=["CMD-SHELL", "curl -f http://localhost/ || exit 1"],
            Interval=5,
            Timeout=30,
            Retries=5,
        )
        container_definition = ecs.ContainerDefinition(
            Image="myimage",
            Memory="300",
            Name="mycontainer",
            HealthCheck=health_check_def,
        )

        container_definition.to_dict()

    def test_docker_volume_configuration(self):
        docker_volume_configuration = ecs.DockerVolumeConfiguration(
            Autoprovision=True,
            Scope="task",
            Labels=dict(label="ok"),
            DriverOpts=dict(option="ok"),
        )
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
                ecs.Volume(
                    Name="my-vol", DockerVolumeConfiguration=docker_volume_configuration
                ),
            ],
        )
        task_definition.to_dict()


class TestECSValidators(unittest.TestCase):
    def test_scope_validator(self):
        valid_values = ["shared", "task"]
        for x in valid_values:
            ecs.scope_validator(x)

        with self.assertRaises(ValueError):
            ecs.scope_validator("bad_scope")

    def test_network_port(self):
        valid_values = [-1, 0, 65535]
        for x in valid_values:
            ecs.validate_network_port(x)

        invalid_values = [-2, 65536]
        for x in invalid_values:
            with self.assertRaises(ValueError):
                ecs.validate_network_port(x)

    def test_scaling_step_size(self):
        valid_values = [1, 100, 10000]
        for x in valid_values:
            ecs.validate_scaling_step_size(x)

        invalid_values = [-1, 0, 10001]
        for x in invalid_values:
            with self.assertRaises(ValueError):
                ecs.validate_scaling_step_size(x)
