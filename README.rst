===========
troposphere
===========

.. image:: https://pypip.in/version/troposphere/badge.svg?text=version&style=flat
    :target: https://pypi.python.org/pypi/troposphere

.. image:: https://travis-ci.org/cloudtools/troposphere.png?branch=master
    :target: https://travis-ci.org/cloudtools/troposphere


About
=====

troposphere - library to create `AWS CloudFormation`_ descriptions

The troposphere library allows for easier creation of the AWS CloudFormation
JSON by writing Python code to describe the AWS resources. Troposphere also
includes some basic support for `OpenStack resources`_ via heat.

To facilitate catching CloudFormation or JSON errors early the library has
property and type checking built into the classes.

Installation Instructions
=========================

troposphere can be installed using the pip distribution system for python by
issuing::

    $ pip install troposphere

Alternatively, you can run use setup.py to install by cloning this repository
and issuing::

    # python setup.py install

Examples
========

A simple example to create an instance would look like this::

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


Alternatively, parameters can be used instead of properties::

    >>> instance = ec2.Instance("myinstance", ImageId="ami-951945d0", InstanceType="t1.micro")
    >>> t.add_resource(instance)
    <troposphere.ec2.Instance object at 0x101bf3550>

And add_resource() returns the object to make it easy to use with Ref()::

    >>> instance = t.add_resource(ec2.Instance("myinstance", ImageId="ami-951945d0", InstanceType="t1.micro"))
    >>> Ref(instance)
    <troposphere.Ref object at 0x101bf3490>

---------------------------------------------------------------------
Examples of the error checking (full tracebacks removed for clarity):
---------------------------------------------------------------------

Incorrect property being set on AWS resource::

    >>> import troposphere.ec2 as ec2
    >>> ec2.Instance("ec2instance", image="i-XXXX")
    Traceback (most recent call last):
    ...
    AttributeError: AWS::EC2::Instance object does not support attribute image

Incorrect type for AWS resource property::

    >>> ec2.Instance("ec2instance", ImageId=1)
    Traceback (most recent call last):
    ...
    TypeError: ImageId is <type 'int'>, expected <type 'basestring'>

Missing required property for the AWS resource::

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

- AWS::AutoScaling
- AWS::CloudFormation
- AWS::CloudFront
- AWS::CloudTrail
- AWS::CloudWatch
- AWS::DynamoDB
- AWS::EC2
- AWS::ElastiCache
- AWS::ElasticBeanstalk
- AWS::ElasticLoadBalancing
- AWS::IAM
- AWS::KINESIS
- AWS::Logs
- AWS::OPSWORKS
- AWS::RDS
- AWS::REDSHIFT
- AWS::Route53
- AWS::S3
- AWS::SDB
- AWS::SNS
- AWS::SQS

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
- Add missing AWS resource types:

  - AWS::CloudFormation::CustomResource

Duplicating a single instance sample would look like this
=========================================================

.. code::

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

We have a google group, cloudtools-dev_, where you can ask questions and
engage with the troposphere community.  Issues & pull requests are always
welcome!


.. _`AWS CloudFormation`: http://aws.amazon.com/cloudformation
.. _`OpenStack resources`: http://docs.openstack.org/developer/heat/template_guide/openstack.html
.. _cloudtools-dev: https://groups.google.com/forum/#!forum/cloudtools-dev
