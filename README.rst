===========
troposphere
===========

.. image:: https://img.shields.io/pypi/v/troposphere.svg
    :target: https://pypi.python.org/pypi/troposphere
    :alt: PyPI Version

.. image:: https://github.com/cloudtools/troposphere/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/cloudtools/troposphere/actions?query=branch%3Amain
    :alt: Build Status

.. image:: https://img.shields.io/pypi/l/troposphere.svg
    :target: https://opensource.org/licenses/BSD-2-Clause
    :alt: license: New BSD license

.. image:: https://readthedocs.org/projects/troposphere/badge/?version=latest
    :target: https://troposphere.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

About
=====

troposphere - library to create `AWS CloudFormation`_ descriptions

The troposphere library allows for easier creation of the `AWS CloudFormation
JSON`_ by writing Python code to describe the AWS resources. troposphere also
includes some basic support for `OpenStack resources`_ via Heat.

To facilitate catching CloudFormation or JSON errors early the library has
property and type checking built into the classes.

About this fork
===============
This is a fork kept in order to guarantee that Troposphere is always available in our organization. For instructions on how to work with this fork internally see `here`: https://github.com/nentgroup/troposphere/blob/master/VIAPLAY_CONTRIBUTING.md

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

Alternatively, you can use `setup.py` to install by cloning this repository
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
    >>> t.add_resource(ec2.Subnet("ec2subnet", VpcId="vpcid"))
    <troposphere.ec2.Subnet object at 0x100830ed0>
    >>> print(t.to_json())
    Traceback (most recent call last):
    ...
    ValueError: Resource CidrBlock required in type AWS::EC2::Subnet (title: ec2subnet)

Currently supported resource types
======================================

- `AWS Resource Types`_
- `OpenStack Resource Types`_

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
.. _`AWS Resource Types`: https://github.com/cloudtools/troposphere/blob/master/resources_aws.md
.. _`OpenStack Resource Types`: https://github.com/cloudtools/troposphere/blob/master/resources_openstack.md
