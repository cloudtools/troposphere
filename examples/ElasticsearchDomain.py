# Converted from Elasticsearch Domain example located at:
# http://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticsearch-domain.html#d0e51519

from troposphere import Template, constants
from troposphere.elasticsearch import (
    Domain,
    EBSOptions,
    ElasticsearchClusterConfig,
    SnapshotOptions,
    VPCOptions,
)

templ = Template()

templ.set_description("Elasticsearch Domain example")

es_domain = templ.add_resource(
    Domain(
        "ElasticsearchDomain",
        DomainName="ExampleElasticsearchDomain",
        ElasticsearchClusterConfig=ElasticsearchClusterConfig(
            DedicatedMasterEnabled=True,
            InstanceCount=2,
            ZoneAwarenessEnabled=True,
            InstanceType=constants.ELASTICSEARCH_M3_MEDIUM,
            DedicatedMasterType=constants.ELASTICSEARCH_M3_MEDIUM,
            DedicatedMasterCount=3,
        ),
        EBSOptions=EBSOptions(EBSEnabled=True, Iops=0, VolumeSize=20, VolumeType="gp2"),
        SnapshotOptions=SnapshotOptions(AutomatedSnapshotStartHour=0),
        AccessPolicies={
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"},
                    "Action": "es:*",
                    "Resource": "*",
                }
            ],
        },
        AdvancedOptions={"rest.action.multi.allow_explicit_index": True},
        VPCOptions=VPCOptions(
            SubnetIds=["subnet-4f2bb123"], SecurityGroupIds=["sg-04cf048c"]
        ),
    )
)

print(templ.to_json())
