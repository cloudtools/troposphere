# Converted from ELBSample.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Base64, FindInMap, GetAtt, GetAZs, Join, Output
from troposphere import Parameter, Ref, Template
import troposphere.ec2 as ec2
import troposphere.elasticloadbalancing as elb


def AddAMI(template):
    template.add_mapping("RegionMap", {
        "us-west-1": {"AMI": "ami-3bcc9e7e"},
    })


def main():
    template = Template()
    AddAMI(template)

    # Add the Parameters
    keyname_param = template.add_parameter(Parameter(
        "KeyName",
        Type="String",
        Default="mark",
        Description="Name of an existing EC2 KeyPair to "
                    "enable SSH access to the instance",
    ))

    template.add_parameter(Parameter(
        "InstanceType",
        Type="String",
        Description="WebServer EC2 instance type",
        Default="m1.small",
        AllowedValues=[
            "t1.micro", "m1.small", "m1.medium", "m1.large", "m1.xlarge",
            "m2.xlarge", "m2.2xlarge", "m2.4xlarge", "c1.medium", "c1.xlarge",
            "cc1.4xlarge", "cc2.8xlarge", "cg1.4xlarge"
        ],
        ConstraintDescription="must be a valid EC2 instance type.",
    ))

    webport_param = template.add_parameter(Parameter(
        "WebServerPort",
        Type="String",
        Default="8888",
        Description="TCP/IP port of the web server",
    ))

    # Define the instance security group
    instance_sg = template.add_resource(
        ec2.SecurityGroup(
            "InstanceSecurityGroup",
            GroupDescription="Enable SSH and HTTP access on the inbound port",
            SecurityGroupIngress=[
                ec2.SecurityGroupRule(
                    IpProtocol="tcp",
                    FromPort="22",
                    ToPort="22",
                    CidrIp="0.0.0.0/0",
                ),
                ec2.SecurityGroupRule(
                    IpProtocol="tcp",
                    FromPort=Ref(webport_param),
                    ToPort=Ref(webport_param),
                    CidrIp="0.0.0.0/0",
                ),
            ]
        )
    )

    # Add the web server instances
    web_instances = []
    for name in ("Ec2Instance1", "Ec2Instance2"):
        instance = template.add_resource(ec2.Instance(
            name,
            SecurityGroups=[Ref(instance_sg)],
            KeyName=Ref(keyname_param),
            InstanceType=Ref("InstanceType"),
            ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
            UserData=Base64(Ref(webport_param)),
        ))
        web_instances.append(instance)

    elasticLB = template.add_resource(elb.LoadBalancer(
        'ElasticLoadBalancer',
        AvailabilityZones=GetAZs(""),
        Instances=[Ref(r) for r in web_instances],
        Listeners=[
            elb.Listener(
                LoadBalancerPort="80",
                InstancePort=Ref(webport_param),
                Protocol="HTTP",
            ),
        ],
        HealthCheck=elb.HealthCheck(
            Target=Join("", ["HTTP:", Ref(webport_param), "/"]),
            HealthyThreshold="3",
            UnhealthyThreshold="5",
            Interval="30",
            Timeout="5",
        )
    ))

    template.add_output(Output(
        "URL",
        Description="URL of the sample website",
        Value=Join("", ["http://", GetAtt(elasticLB, "DNSName")])
    ))

    print(template.to_json())


if __name__ == '__main__':
    main()
