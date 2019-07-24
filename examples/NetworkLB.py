# Converted from ELBSample.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

from troposphere import Base64, FindInMap, GetAtt, Join, Output
from troposphere import Parameter, Ref, Template
import troposphere.ec2 as ec2
import troposphere.elasticloadbalancingv2 as elb


def AddAMI(template):
    template.add_mapping("RegionMap", {
        "us-east-1": {"AMI": "ami-6411e20d"},
        "us-west-1": {"AMI": "ami-c9c7978c"},
        "us-west-2": {"AMI": "ami-fcff72cc"},
        "eu-west-1": {"AMI": "ami-37c2f643"},
        "ap-southeast-1": {"AMI": "ami-66f28c34"},
        "ap-northeast-1": {"AMI": "ami-9c03a89d"},
        "sa-east-1": {"AMI": "ami-a039e6bd"}
    })


def main():
    template = Template()
    template.add_version("2010-09-09")

    template.set_description(
        "AWS CloudFormation Sample Template: NLB with 1 EC2 instance")

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

    subnetA = template.add_parameter(Parameter(
        "subnetA",
        Type="String",
        Default="subnet-096fd06d"
    ))

    subnetB = template.add_parameter(Parameter(
        "subnetB",
        Type="String",
        Default="subnet-1313ef4b"
    ))

    VpcId = template.add_parameter(Parameter(
        "VpcId",
        Type="String",
        Default="vpc-82c514e6"
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

    eipA = template.add_resource(ec2.EIP('eipA', Domain='vpc',))

    eipB = template.add_resource(ec2.EIP('eipB', Domain='vpc',))

    # Add the web server instance
    WebInstance = template.add_resource(ec2.Instance(
        "WebInstance",
        SecurityGroups=[Ref(instance_sg)],
        KeyName=Ref(keyname_param),
        InstanceType=Ref("InstanceType"),
        ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
        UserData=Base64(Ref(webport_param)),
    ))

    # Add the network LB
    NetworkLB = template.add_resource(elb.LoadBalancer(
        "NetworkLB",
        Name="NetworkLB",
        Scheme="internet-facing",
        SubnetMappings=[
            elb.SubnetMapping(
                AllocationId=GetAtt(eipA, 'AllocationId'),
                SubnetId=Ref(subnetA)
            ),
            elb.SubnetMapping(
                AllocationId=GetAtt(eipB, 'AllocationId'),
                SubnetId=Ref(subnetB)
            )
        ],
        Type='network'
    ))

    TargetGroupWeb = template.add_resource(elb.TargetGroup(
        "TargetGroupWeb",
        HealthCheckIntervalSeconds="30",
        HealthCheckProtocol="HTTP",
        HealthCheckTimeoutSeconds="10",
        HealthyThresholdCount="4",
        Matcher=elb.Matcher(
            HttpCode="200"),
        Name="WebTarget",
        Port=Ref(webport_param),
        Protocol="HTTP",
        Targets=[elb.TargetDescription(
            Id=Ref(WebInstance),
            Port=Ref(webport_param))],
        UnhealthyThresholdCount="3",
        VpcId=Ref(VpcId)

    ))

    template.add_resource(elb.Listener(
        "Listener",
        Port="80",
        Protocol="HTTP",
        LoadBalancerArn=Ref(NetworkLB),
        DefaultActions=[elb.Action(
            Type="forward",
            TargetGroupArn=Ref(TargetGroupWeb)
        )]
    ))

    template.add_output(Output(
        "URL",
        Description="URL of the sample website",
        Value=Join("", ["http://", GetAtt(NetworkLB, "DNSName")])
    ))

    print(template.to_json())


if __name__ == '__main__':
    main()
