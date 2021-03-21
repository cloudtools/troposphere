from troposphere import FindInMap, Ref, Template, Parameter, Tags
from troposphere.iam import InstanceProfile, Role
from troposphere.efs import FileSystem, MountTarget
from troposphere.ec2 import SecurityGroup, SecurityGroupRule, Instance
from awacs.aws import Allow, Statement, PolicyDocument, Action


template = Template()
template.add_version('2010-09-09')

template.add_mapping('RegionMap', {
    "us-east-1": {"AMI": "ami-7f418316"},
    "us-west-1": {"AMI": "ami-951945d0"},
    "us-west-2": {"AMI": "ami-16fd7026"},
    "eu-west-1": {"AMI": "ami-24506250"},
    "sa-east-1": {"AMI": "ami-3e3be423"},
    "ap-southeast-1": {"AMI": "ami-74dda626"},
    "ap-northeast-1": {"AMI": "ami-dcfa4edd"}
})

keyname_param = template.add_parameter(Parameter(
    "KeyName",
    Description="Name of an existing EC2 KeyPair to enable SSH "
                "access to the instance",
    Type="String",
))

vpcid_param = template.add_parameter(Parameter(
    "VpcId",
    Description="VPC ID where the MountTarget and instance should be created",
    Type="String",
))

subnetid_param = template.add_parameter(Parameter(
    "SubnetId",
    Description="Subnet ID where the MountTarget and instance "
                "should be created",
    Type="String",
))

# security group for the host
efs_host_security_group = SecurityGroup(
    "EFSHostSecurityGroup",
    GroupDescription="EC2 Instance Security Group"
)
template.add_resource(efs_host_security_group)

# create security group for NFS over TCP for EC2 instances. Only allow the
# instance(s) from the efs_host_security_group to access the mount target
# given by this security group.
efs_security_group_rule = SecurityGroupRule(
    IpProtocol='tcp',
    FromPort='2049',
    ToPort='2049',
    SourceSecurityGroupId=Ref(efs_host_security_group)
)

# Security group that's applied to the Mount Targets.
efs_security_group = SecurityGroup(
    "SecurityGroup",
    SecurityGroupIngress=[efs_security_group_rule],
    VpcId=Ref(vpcid_param),
    GroupDescription="Allow NFS over TCP"
)
template.add_resource(efs_security_group)

# Create FileSystem. This is the actual filesystem, which has one or more
# mount targets. Give it some tags so we can identify it later.
tags = Tags(Name='MyEFSFileSystem')
efs_file_system = FileSystem(
    "MyEFSFileSystem",
    FileSystemTags=tags
)
template.add_resource(efs_file_system)

# create MountTarget. You really want a mount target in each subnet where
# it's required, but for the purpose of this example we'll
# put it in just one.
efs_mount_target = MountTarget(
    "MyEFSMountTarget",
    FileSystemId=Ref(efs_file_system),
    SecurityGroups=[Ref(efs_security_group)],
    SubnetId=Ref(subnetid_param)
)
template.add_resource(efs_mount_target)

# Create the policy that allows the instance to describe file systems and tags,
# so it can lookup the file system using AWS tags. An alternative would be to
# pass in the FileSystem name as UserData.
efs_host_role = Role(
    "EFSHostRole",
    AssumeRolePolicyDocument=PolicyDocument(
        Statement=[
            Statement(
                Effect=Allow,
                Action=[
                    Action('elasticfilesystem', 'DescribeFileSystems'),
                    Action('elasticfilesystem', 'DescribeTags')
                ],
                Resource=["*"]
            )
        ]
    )
)
template.add_resource(efs_host_role)

efs_host_instance_profile = InstanceProfile(
    "EFSInstanceProfile",
    Roles=[Ref(efs_host_role)]
)
template.add_resource(efs_host_instance_profile)

# And finally the EC2 instance.
ec2_instance = Instance(
    "Ec2Instance",
    ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
    InstanceType="t1.micro",
    KeyName=Ref(keyname_param),
    SecurityGroups=[Ref(efs_host_security_group)],
    IamInstanceProfile=Ref(efs_host_instance_profile),
    DependsOn=efs_mount_target
)
template.add_resource(ec2_instance)

# the instance can then mount the filesystem with something like
# (depending on your operating system):
#   mount <az>.<filesystem-name>.efs.<region>.amazonaws.com: /path
# for example:
#   mount us-west-1a.fs-abcd1234.efs.us-west-1.amazonaws.com: /path

print(template.to_json())
