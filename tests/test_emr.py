from troposphere import If, Ref, Tags
from troposphere.constants import M4_LARGE

import unittest
import troposphere.emr as emr


scaling_policy = emr.SimpleScalingPolicyConfiguration(
                    AdjustmentType="EXACT_CAPACITY",
                    ScalingAdjustment="1",
                    CoolDown="300"
                )


class TestEMR(unittest.TestCase):

    def generate_rules(self, rules_name):
        rules = [
            emr.Rules(
                Name=rules_name,
                Description="%s rules" % rules_name,
                Action=emr.RulesActionConfig(
                    Market="ON_DEMAND",
                    SimpleScalingPolicyConfiguration=scaling_policy
                ),
                Trigger=emr.Trigger(
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
                            emr.KeyValue(
                                'my.custom.master.property',
                                'my.custom.master.value'
                            )
                        ]
                    )
                )
            )
        ]
        return rules

    def test_allow_string_cluster(self):
        spot = "2"
        withSpotPrice = "WithSpotPrice"
        cluster = emr.Cluster(
            'Cluster',
            # AdditionalInfo="Additional Info",
            Applications=[
                emr.Application(Name="Hadoop"),
                emr.Application(Name="Hive"),
                emr.Application(Name="Mahout"),
                emr.Application(Name="Pig"),
                emr.Application(Name="Spark")
            ],
            BootstrapActions=[
                emr.BootstrapActionConfig(
                    Name='Dummy bootstrap action',
                    ScriptBootstrapAction=emr.ScriptBootstrapActionConfig(
                        Path='file:/usr/share/aws/emr/scripts/install-hue',
                        Args=["dummy", "parameter"]
                    )
                )
            ],
            Configurations=[
                emr.Configuration(
                    Classification="core-site",
                    ConfigurationProperties={
                        'hadoop.security.groups.cache.secs': '250'
                    }
                )
            ],
            Instances=emr.JobFlowInstancesConfig(
                Ec2KeyName="KeyName",
                Ec2SubnetId="SubnetId",
                MasterInstanceGroup=emr.InstanceGroupConfigProperty(
                    InstanceCount="1",
                    InstanceType=M4_LARGE,
                    AutoScalingPolicy=emr.AutoScalingPolicy(
                      Constraints=emr.Constraints(
                        MinCapacity="1",
                        MaxCapacity="3"
                      ),
                      Rules=self.generate_rules("MasterAutoScalingPolicy")
                    ),
                ),
                CoreInstanceGroup=emr.InstanceGroupConfigProperty(
                    Name="Core Instance",
                    BidPrice=If(withSpotPrice, Ref(spot), Ref("AWS::NoValue")),
                    Market=If(withSpotPrice, "SPOT", "ON_DEMAND"),
                    InstanceType=M4_LARGE,
                    AutoScalingPolicy=emr.AutoScalingPolicy(
                        Constraints=emr.Constraints(
                            MinCapacity="1",
                            MaxCapacity="3"
                        ),
                        Rules=self.generate_rules("CoreAutoScalingPolicy"),
                    )
                ),
            ),
            JobFlowRole="EMRJobFlowRole",
            LogUri="s3://cluster-logs",
            Name="EMR Cluster",
            ReleaseLabel="emr-5.5.0",
            ServiceRole="EMRServiceRole",
            AutoScalingRole="EMR_AutoScaling_DefaultRole",
            VisibleToAllUsers="true",
            Tags=Tags(
                Name="EMR Sample Cluster"
            )
        )

        cluster.to_dict()
