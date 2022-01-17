import unittest

import troposphere.emr as emr
from troposphere import If, Ref, Tags
from troposphere.constants import M4_LARGE

scaling_policy = emr.SimpleScalingPolicyConfiguration(
    AdjustmentType=emr.EXACT_CAPACITY, ScalingAdjustment="1", CoolDown="300"
)

kms_key = "arn:aws:kms:us-east-1:123456789012:key/1234-1234-1234-1234-1234"

security_configuration = {
    "EncryptionConfiguration": {
        "EnableInTransitEncryption": True,
        "InTransitEncryptionConfiguration": {
            "TLSCertificateConfiguration": {
                "CertificateProviderType": "PEM",
                "S3Object": "s3://MyConfigStore/artifacts/MyCerts.zip",
            }
        },
        "EnableAtRestEncryption": True,
        "AtRestEncryptionConfiguration": {
            "S3EncryptionConfiguration": {
                "EncryptionMode": "SSE-KMS",
                "AwsKmsKey": kms_key,
            },
            "LocalDiskEncryptionConfiguration": {
                "EncryptionKeyProviderType": "AwsKms",
                "AwsKmsKey": kms_key,
            },
        },
    }
}


class TestEMR(unittest.TestCase):
    def generate_rules(self, rules_name):
        rules = [
            emr.ScalingRule(
                Name=rules_name,
                Description="%s rules" % rules_name,
                Action=emr.ScalingAction(
                    Market="ON_DEMAND", SimpleScalingPolicyConfiguration=scaling_policy
                ),
                Trigger=emr.ScalingTrigger(
                    CloudWatchAlarmDefinition=emr.CloudWatchAlarmDefinition(
                        ComparisonOperator="GREATER_THAN",
                        EvaluationPeriods="120",
                        MetricName="TestMetric",
                        Namespace="AWS/ElasticMapReduce",
                        Period="300",
                        Statistic="AVERAGE",
                        Threshold="50",
                        Unit="PERCENT",
                        Dimensions=[
                            emr.MetricDimension(
                                "my.custom.master.property", "my.custom.master.value"
                            ),
                        ],
                    )
                ),
            )
        ]
        return rules

    def test_allow_string_cluster(self):
        cluster_security_configuration = emr.SecurityConfiguration(
            "emrsecurityconfiguration",
            Name="EMRSecurityConfiguration",
            SecurityConfiguration=security_configuration,
        )

        spot = "2"
        withSpotPrice = "WithSpotPrice"
        cluster = emr.Cluster(
            "Cluster",
            # AdditionalInfo="Additional Info",
            Applications=[
                emr.Application(Name="Hadoop"),
                emr.Application(Name="Hive"),
                emr.Application(Name="Mahout"),
                emr.Application(Name="Pig"),
                emr.Application(Name="Spark"),
            ],
            BootstrapActions=[
                emr.BootstrapActionConfig(
                    Name="Dummy bootstrap action",
                    ScriptBootstrapAction=emr.ScriptBootstrapActionConfig(
                        Path="file:/usr/share/aws/emr/scripts/install-hue",
                        Args=["dummy", "parameter"],
                    ),
                )
            ],
            Configurations=[
                emr.Configuration(
                    Classification="core-site",
                    ConfigurationProperties={
                        "hadoop.security.groups.cache.secs": "250"
                    },
                )
            ],
            Instances=emr.JobFlowInstancesConfig(
                Ec2KeyName="KeyName",
                Ec2SubnetId="SubnetId",
                MasterInstanceGroup=emr.InstanceGroupConfigProperty(
                    InstanceCount="1",
                    InstanceType=M4_LARGE,
                    AutoScalingPolicy=emr.AutoScalingPolicy(
                        Constraints=emr.ScalingConstraints(
                            MinCapacity="1", MaxCapacity="3"
                        ),
                        Rules=self.generate_rules("MasterAutoScalingPolicy"),
                    ),
                ),
                CoreInstanceGroup=emr.InstanceGroupConfigProperty(
                    Name="Core Instance",
                    BidPrice=If(withSpotPrice, Ref(spot), Ref("AWS::NoValue")),
                    Market=If(withSpotPrice, "SPOT", "ON_DEMAND"),
                    InstanceCount="1",
                    InstanceType=M4_LARGE,
                    AutoScalingPolicy=emr.AutoScalingPolicy(
                        Constraints=emr.ScalingConstraints(
                            MinCapacity="1", MaxCapacity="3"
                        ),
                        Rules=self.generate_rules("CoreAutoScalingPolicy"),
                    ),
                ),
            ),
            JobFlowRole="EMRJobFlowRole",
            LogUri="s3://cluster-logs",
            Name="EMR Cluster",
            ReleaseLabel="emr-5.5.0",
            SecurityConfiguration=Ref(cluster_security_configuration),
            ServiceRole="EMRServiceRole",
            AutoScalingRole="EMR_AutoScaling_DefaultRole",
            VisibleToAllUsers="true",
            Tags=Tags(Name="EMR Sample Cluster"),
        )

        cluster.to_dict()

        autoscale_policy = emr.AutoScalingPolicy(
            Constraints=emr.ScalingConstraints(MinCapacity=0, MaxCapacity=5),
            Rules=[
                emr.ScalingRule(
                    Name="ScaleUpContainerPending",
                    Description="Scale up on over-provisioned " "containers",
                    Action=emr.ScalingAction(
                        SimpleScalingPolicyConfiguration=emr.SimpleScalingPolicyConfiguration(
                            AdjustmentType=emr.CHANGE_IN_CAPACITY,
                            CoolDown=300,
                            ScalingAdjustment=1,
                        )
                    ),
                    Trigger=emr.ScalingTrigger(
                        CloudWatchAlarmDefinition=emr.CloudWatchAlarmDefinition(
                            ComparisonOperator="GREATER_THAN",
                            MetricName="ContainerPendingRatio",
                            Period=300,
                            Threshold=0.75,
                            Dimensions=[
                                emr.MetricDimension(
                                    Key="JobFlowId", Value="${emr.clusterId}"
                                )
                            ],
                        )
                    ),
                ),
                emr.ScalingRule(
                    Name="ScaleUpMemory",
                    Description="Scale up on low memory",
                    Action=emr.ScalingAction(
                        SimpleScalingPolicyConfiguration=emr.SimpleScalingPolicyConfiguration(
                            AdjustmentType="CHANGE_IN_CAPACITY",
                            CoolDown=300,
                            ScalingAdjustment=1,
                        )
                    ),
                    Trigger=emr.ScalingTrigger(
                        CloudWatchAlarmDefinition=emr.CloudWatchAlarmDefinition(
                            ComparisonOperator="LESS_THAN",
                            MetricName="YARNMemoryAvailablePercentage",
                            Period=300,
                            Threshold=15,
                            Dimensions=[
                                emr.MetricDimension(
                                    Key="JobFlowId", Value="${emr.clusterId}"
                                )
                            ],
                        )
                    ),
                ),
                emr.ScalingRule(
                    Name="ScaleDownMemory",
                    Description="Scale down on high memory",
                    Action=emr.ScalingAction(
                        SimpleScalingPolicyConfiguration=emr.SimpleScalingPolicyConfiguration(
                            AdjustmentType=emr.CHANGE_IN_CAPACITY,
                            CoolDown=300,
                            ScalingAdjustment=-1,
                        )
                    ),
                    Trigger=emr.ScalingTrigger(
                        CloudWatchAlarmDefinition=emr.CloudWatchAlarmDefinition(
                            ComparisonOperator="GREATER_THAN",
                            MetricName="YARNMemoryAvailablePercentage",
                            Period=300,
                            Threshold=75,
                            Dimensions=[
                                emr.MetricDimension(
                                    Key="JobFlowId", Value="${emr.clusterId}"
                                )
                            ],
                        )
                    ),
                ),
            ],
        )

        emr.InstanceGroupConfig(
            "TaskInstanceGroup",
            AutoScalingPolicy=autoscale_policy,
            InstanceCount=0,
            InstanceType=M4_LARGE,
            InstanceRole="TASK",
            Market="ON_DEMAND",
            Name="Task Instance",
            JobFlowId=Ref(cluster),
        )

    def test_Configuration(self):
        emr.Configuration(
            Classification="hadoop-env",
            Configurations=[
                emr.Configuration(
                    Classification="export",
                    ConfigurationProperties={
                        "HADOOP_DATANODE_HEAPSIZE": "2048",
                        "HADOOP_NAMENODE_OPTS": "opts",
                    },
                ),
            ],
        ).to_dict()

        with self.assertRaises(TypeError):
            emr.Configuration(
                Classification="hadoop-env",
                Configurations=[
                    "illegalvalue",
                    emr.Configuration(
                        Classification="export",
                        ConfigurationProperties={
                            "HADOOP_DATANODE_HEAPSIZE": "2048",
                            "HADOOP_NAMENODE_OPTS": "opts",
                        },
                    ),
                ],
            ).to_dict()

        with self.assertRaises(TypeError):
            emr.Configuration(
                Classification="hadoop-env",
                Configurations="invalid",
            ).to_dict()

    def simple_helper(self, adjustment, scaling):
        sc = emr.SimpleScalingPolicyConfiguration(
            AdjustmentType=adjustment,
            ScalingAdjustment=scaling,
        )
        sc.validate()

    def test_SimpleScalingPolicyConfiguration(self):
        self.simple_helper(emr.CHANGE_IN_CAPACITY, 1)
        self.simple_helper(emr.CHANGE_IN_CAPACITY, -1)
        self.simple_helper(emr.CHANGE_IN_CAPACITY, "1")
        self.simple_helper(emr.CHANGE_IN_CAPACITY, "-1")

        self.simple_helper(emr.EXACT_CAPACITY, "1")
        self.simple_helper(emr.EXACT_CAPACITY, 1)
        with self.assertRaises(ValueError):
            self.simple_helper(emr.EXACT_CAPACITY, -1)

        self.simple_helper(emr.PERCENT_CHANGE_IN_CAPACITY, "0.1")
        self.simple_helper(emr.PERCENT_CHANGE_IN_CAPACITY, 0.1)
        with self.assertRaises(ValueError):
            self.simple_helper(emr.PERCENT_CHANGE_IN_CAPACITY, "1.1")
        with self.assertRaises(ValueError):
            self.simple_helper(emr.PERCENT_CHANGE_IN_CAPACITY, 1.1)
        with self.assertRaises(ValueError):
            self.simple_helper(emr.PERCENT_CHANGE_IN_CAPACITY, -0.1)
        with self.assertRaises(ValueError):
            self.simple_helper(emr.PERCENT_CHANGE_IN_CAPACITY, -0.1)
