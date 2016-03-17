# Converted from Elasticsearch Domain example located at:
# http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html#d0e51519

from troposphere import Template
from troposphere.elasticsearch import ElasticsearchDomain, EBSOptions
from troposphere.elasticsearch import ElasticsearchClusterConfig
from troposphere.elasticsearch import SnapshotOptions


templ = Template()

templ.add_description('Elasticsearch Domain example')

es_domain = templ.add_resource(ElasticsearchDomain(
    'ElasticsearchDomain',
    DomainName="ExampleElasticsearchDomain",
    ElasticsearchClusterConfig=ElasticsearchClusterConfig(
        DedicatedMasterEnabled=True,
        InstanceCount=2,
        ZoneAwarenessEnabled=True,
        InstanceType="m3.medium.elasticsearch",
        DedicatedMasterType="m3.medium.elasticsearch",
        DedicatedMasterCount=3
    ),
    EBSOptions=EBSOptions(EBSEnabled=True,
                          Iops=0,
                          VolumeSize=20,
                          VolumeType="gp2"),
    SnapshotOptions=SnapshotOptions(AutomatedSnapshotStartHour=0),
    AccessPolicies={'Version': '2012-10-17',
                    'Statement': [{
                        'Effect': 'Allow',
                        'Principal': {
                            'AWS': '*'
                        },
                        'Action': 'es:*',
                        'Resource': '*'
                    }]},
    AdvancedOptions={"rest.action.multi.allow_explicit_index": "true"}
))

print(templ.to_json())
