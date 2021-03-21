from troposphere import Base64, Join, Output, GetAtt, Tags
from troposphere import Parameter, Ref, Template
from troposphere import cloudformation
import troposphere.ec2 as ec2

t = Template()

t.set_description("Configures an EC2 instance using cfn-init configsets")

key_name = t.add_parameter(Parameter(
    'KeyName',
    Type='AWS::EC2::KeyPair::KeyName',
    Description='Name of an existing EC2 KeyPair to enable SSH access'
))

ami_id = t.add_parameter(Parameter(
    'AmiId',
    Type='String',
    Default='ami-98aa1cf0'
))

security_group = t.add_resource(ec2.SecurityGroup(
    'SecurityGroup',
    GroupDescription='Allows SSH access from anywhere',
    SecurityGroupIngress=[
        ec2.SecurityGroupRule(
            IpProtocol='tcp',
            FromPort=22,
            ToPort=22,
            CidrIp='0.0.0.0/0'
        )
    ],
    Tags=Tags(
        Name='ops.cfninit-sg'
    )
))

ec2_instance = t.add_resource(ec2.Instance(
    'Ec2Instance',
    ImageId=Ref(ami_id),
    InstanceType='t1.micro',
    KeyName=Ref(key_name),
    SecurityGroups=[Ref(security_group)],
    IamInstanceProfile='PullCredentials',
    UserData=Base64(Join('', [
        '#!/bin/bash\n',
        'sudo apt-get update\n',
        'sudo apt-get -y install python-setuptools\n',
        'sudo apt-get -y install python-pip\n',
        'sudo pip install https://s3.amazonaws.com/cloudformation-examples/',
        'aws-cfn-bootstrap-latest.tar.gz\n',
        'cfn-init -s \'', Ref('AWS::StackName'),
        '\' -r Ec2Instance -c ascending'
    ])),
    Metadata=cloudformation.Metadata(
        cloudformation.Init(
            cloudformation.InitConfigSets(
                ascending=['config1', 'config2'],
                descending=['config2', 'config1']
            ),
            config1=cloudformation.InitConfig(
                commands={
                    'test': {
                        'command': 'echo "$CFNTEST" > text.txt',
                        'env': {
                            'CFNTEST': 'I come from config1.'
                        },
                        'cwd': '~'
                    }
                }
            ),
            config2=cloudformation.InitConfig(
                commands={
                    'test': {
                        'command': 'echo "$CFNTEST" > text.txt',
                        'env': {
                            'CFNTEST': 'I come from config2.'
                        },
                        'cwd': '~'
                    }
                }
            )
        )
    ),
    Tags=Tags(
        Name='ops.cfninit',
        env='ops'
    )
))

t.add_output(Output(
    'PublicIp',
    Description='Public IP of the newly created EC2 instance',
    Value=GetAtt(ec2_instance, 'PublicIp')
))

print(t.to_json())
