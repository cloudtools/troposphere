===========
troposphere
===========

.. image:: https://img.shields.io/pypi/v/troposphere.svg
    :target: https://pypi.python.org/pypi/troposphere

.. image:: https://travis-ci.org/cloudtools/troposphere.png?branch=master
    :target: https://travis-ci.org/cloudtools/troposphere

.. image:: https://img.shields.io/pypi/l/troposphere.svg
    :target: https://opensource.org/licenses/BSD-2-Clause


About
=====

troposphere - library to create `AWS CloudFormation`_ descriptions

The troposphere library allows for easier creation of the `AWS CloudFormation
JSON`_ by writing Python code to describe the AWS resources. troposphere also
includes some basic support for `OpenStack resources`_ via Heat.

To facilitate catching CloudFormation or JSON errors early the library has
property and type checking built into the classes.

Installation
============

troposphere can be installed using the pip distribution system for Python by
issuing:

.. code:: sh

    $ pip install troposphere

To install troposphere with `awacs <https://github.com/cloudtools/awacs>`_
(recommended soft dependency):

.. code:: sh

    $ pip install troposphere[policy]

Alternatively, you can run use setup.py to install by cloning this repository
and issuing:

.. code:: sh

    $ python setup.py install  # you may need sudo depending on your python installation

Examples
========

A simple example to create an instance would look like this:

.. code:: python

    >>> from troposphere import Ref, Template
    >>> import troposphere.ec2 as ec2
    >>> t = Template()
    >>> instance = ec2.Instance("myinstance")
    >>> instance.ImageId = "ami-951945d0"
    >>> instance.InstanceType = "t1.micro"
    >>> t.add_resource(instance)
    <troposphere.ec2.Instance object at 0x101bf3390>
    >>> print(t.to_json())
    {
        "Resources": {
            "myinstance": {
                "Properties": {
                    "ImageId": "ami-951945d0",
                    "InstanceType": "t1.micro"
                },
                "Type": "AWS::EC2::Instance"
            }
        }
    }


A simple example to create an instance (YAML) would look like this:

.. code:: python

    >>> from troposphere import Ref, Template
    >>> import troposphere.ec2 as ec2
    >>> t = Template()
    >>> instance = ec2.Instance("myinstance")
    >>> instance.ImageId = "ami-951945d0"
    >>> instance.InstanceType = "t1.micro"
    >>> t.add_resource(instance)
    <troposphere.ec2.Instance object at 0x101bf3390>
    >>> print(t.to_yaml())

    Resources:
        myinstance:
            Properties:
                ImageId: ami-951945d0
                InstanceType: t1.micro
            Type: AWS::EC2::Instance

Alternatively, parameters can be used instead of properties:

.. code:: python

    >>> instance = ec2.Instance("myinstance", ImageId="ami-951945d0", InstanceType="t1.micro")
    >>> t.add_resource(instance)
    <troposphere.ec2.Instance object at 0x101bf3550>

And ``add_resource()`` returns the object to make it easy to use with ``Ref()``:

.. code:: python

    >>> instance = t.add_resource(ec2.Instance("myinstance", ImageId="ami-951945d0", InstanceType="t1.micro"))
    >>> Ref(instance)
    <troposphere.Ref object at 0x101bf3490>

---------------------------------------------------------------------
Examples of the error checking (full tracebacks removed for clarity):
---------------------------------------------------------------------

Incorrect property being set on AWS resource:

.. code:: python

    >>> import troposphere.ec2 as ec2
    >>> ec2.Instance("ec2instance", image="i-XXXX")
    Traceback (most recent call last):
    ...
    AttributeError: AWS::EC2::Instance object does not support attribute image

Incorrect type for AWS resource property:

.. code:: python

    >>> ec2.Instance("ec2instance", ImageId=1)
    Traceback (most recent call last):
    ...
    TypeError: ImageId is <type 'int'>, expected <type 'basestring'>

Missing required property for the AWS resource:

.. code:: python

    >>> from troposphere import Template
    >>> import troposphere.ec2 as ec2
    >>> t = Template()
    >>> t.add_resource(ec2.Instance("ec2instance", InstanceType="m3.medium"))
    <troposphere.ec2.Instance object at 0x109ee2e50>
    >>> print(t.to_json())
    Traceback (most recent call last):
    ...
    ValueError: Resource ImageId required in type AWS::EC2::Instance

Currently supported AWS resource types
======================================

- AWS::ApiGateway
- AWS::ApplicationAutoScaling
- AWS::AppSync
- AWS::Athena
- AWS::AutoScaling
- AWS::Batch
- AWS::CertificateManager
- AWS::Cloud9
- AWS::CloudFormation
- AWS::CloudFront
- AWS::CloudTrail
- AWS::CloudWatch
- AWS::CodeBuild
- AWS::CodeCommit
- AWS::CodeDeploy
- AWS::CodePipeline
- AWS::Cognito
- AWS::Config
- AWS::DAX
- AWS::DMS
- AWS::DataPipeline
- AWS::DirectoryService
- AWS::DynamoDB
- AWS::EC2
- AWS::ECR
- AWS::ECS
- AWS::EFS
- AWS::EMR
- AWS::ElastiCache
- AWS::ElasticBeanstalk
- AWS::ElasticLoadBalancing
- AWS::ElasticLoadBalancingV2
- AWS::Elasticsearch
- AWS::Events
- AWS::GuardDuty
- AWS::Glue
- AWS::IAM
- AWS::Inspector
- AWS::IoT
- AWS::KMS
- AWS::Kinesis
- AWS::KinesisAnalytics
- AWS::KinesisFirehose
- AWS::Lambda
- AWS::Logs
- AWS::OpsWorks
- AWS::RDS
- AWS::Redshift
- AWS::Route53
- AWS::S3
- AWS::SDB
- AWS::SES
- AWS::SNS
- AWS::SQS
- AWS::SSM
- AWS::Serverless
- AWS::ServiceCatalog
- AWS::ServiceDiscovery
- AWS::StepFunctions
- AWS::WAF
- AWS::WAFRegional
- AWS::WorkSpaces

Currently supported OpenStack resource types
============================================

- OS::Neutron::Firewall
- OS::Neutron::FirewallPolicy
- OS::Neutron::FirewallRule
- OS::Neutron::FloatingIP
- OS::Neutron::FloatingIPAssociation
- OS::Neutron::HealthMonitor
- OS::Neutron::Pool
- OS::Neutron::LoadBalancer
- OS::Neutron::Net
- OS::Neutron::PoolMember
- OS::Neutron::Port
- OS::Neutron::SecurityGroup
- OS::Nova::FloatingIP
- OS::Nova::FloatingIPAssociation
- OS::Nova::KeyPair
- OS::Nova::Server

Todo:

- Add additional validity checks

Duplicating a single instance sample would look like this
=========================================================

.. code:: python

    # Converted from EC2InstanceSample.template located at:
    # http://aws.amazon.com/cloudformation/aws-cloudformation-templates/

    from troposphere import Base64, FindInMap, GetAtt
    from troposphere import Parameter, Output, Ref, Template
    import troposphere.ec2 as ec2


    template = Template()

    keyname_param = template.add_parameter(Parameter(
        "KeyName",
        Description="Name of an existing EC2 KeyPair to enable SSH "
                    "access to the instance",
        Type="String",
    ))

    template.add_mapping('RegionMap', {
        "us-east-1":      {"AMI": "ami-7f418316"},
        "us-west-1":      {"AMI": "ami-951945d0"},
        "us-west-2":      {"AMI": "ami-16fd7026"},
        "eu-west-1":      {"AMI": "ami-24506250"},
        "sa-east-1":      {"AMI": "ami-3e3be423"},
        "ap-southeast-1": {"AMI": "ami-74dda626"},
        "ap-northeast-1": {"AMI": "ami-dcfa4edd"}
    })

    ec2_instance = template.add_resource(ec2.Instance(
        "Ec2Instance",
        ImageId=FindInMap("RegionMap", Ref("AWS::Region"), "AMI"),
        InstanceType="t1.micro",
        KeyName=Ref(keyname_param),
        SecurityGroups=["default"],
        UserData=Base64("80")
    ))

    template.add_output([
        Output(
            "InstanceId",
            Description="InstanceId of the newly created EC2 instance",
            Value=Ref(ec2_instance),
        ),
        Output(
            "AZ",
            Description="Availability Zone of the newly created EC2 instance",
            Value=GetAtt(ec2_instance, "AvailabilityZone"),
        ),
        Output(
            "PublicIP",
            Description="Public IP address of the newly created EC2 instance",
            Value=GetAtt(ec2_instance, "PublicIp"),
        ),
        Output(
            "PrivateIP",
            Description="Private IP address of the newly created EC2 instance",
            Value=GetAtt(ec2_instance, "PrivateIp"),
        ),
        Output(
            "PublicDNS",
            Description="Public DNSName of the newly created EC2 instance",
            Value=GetAtt(ec2_instance, "PublicDnsName"),
        ),
        Output(
            "PrivateDNS",
            Description="Private DNSName of the newly created EC2 instance",
            Value=GetAtt(ec2_instance, "PrivateDnsName"),
        ),
    ])

    print(template.to_json())

Community
=========

We have a Google Group, cloudtools-dev_, where you can ask questions and
engage with the troposphere community. Issues and pull requests are always
welcome!

Licensing
=========

troposphere is licensed under the `BSD 2-Clause license`_.
See `LICENSE`_ for the troposphere full license text.


.. _`AWS CloudFormation`: http://aws.amazon.com/cloudformation
.. _`AWS CloudFormation JSON`: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
.. _`OpenStack resources`: http://docs.openstack.org/developer/heat/template_guide/openstack.html
.. _cloudtools-dev: https://groups.google.com/forum/#!forum/cloudtools-dev
.. _`LICENSE`: https://github.com/cloudtools/troposphere/blob/master/LICENSE
.. _`BSD 2-Clause license`: http://opensource.org/licenses/BSD-2-Clause
