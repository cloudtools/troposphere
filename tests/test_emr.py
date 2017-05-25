from troposphere import Parameter, Ref, Template, Tags, If, Equals, Not, Join
from troposphere.constants import KEY_PAIR_NAME, SUBNET_ID, M4_LARGE, NUMBER

import unittest
import troposphere.emr as emr


class TestEMR(unittest.TestCase):

    def test_allow_string_cluster(self):
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
                    InstanceType=M4_LARGE
                ),
                CoreInstanceGroup=emr.InstanceGroupConfigProperty(
                    InstanceCount="1",
                    InstanceType=M4_LARGE
                ),
            ),
            JobFlowRole="EMRJobFlowRole",
            LogUri="s3://cluster-logs",
            Name="EMR Cluster",
            ReleaseLabel="emr-5.5.0",
            ServiceRole="EMRServiceRole",
            VisibleToAllUsers="true",
            Tags=Tags(
                Name="EMR Sample Cluster"
            )
        )

        cluster.to_dict()
