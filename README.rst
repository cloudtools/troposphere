===========
troposphere
===========

.. image:: https://img.shields.io/pypi/v/troposphere.svg
    :target: https://pypi.python.org/pypi/troposphere
    :alt: PyPI Version

.. image:: https://travis-ci.org/cloudtools/troposphere.svg?branch=master
    :target: https://travis-ci.org/cloudtools/troposphere
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
    >>> t.add_resource(ec2.Instance("ec2instance", InstanceType="m3.medium"))
    <troposphere.ec2.Instance object at 0x109ee2e50>
    >>> print(t.to_json())
    Traceback (most recent call last):
    ...
    ValueError: Resource ImageId required in type AWS::EC2::Instance

Currently supported AWS resource types
======================================

- `AWS::AccessAnalyzer`_
- `AWS::ACMPCA`_
- `AWS::AmazonMQ`_
- `AWS::Amplify`_
- `AWS::ApiGateway`_
- `AWS::ApiGatewayV2`_
- `AWS::AppConfig`_
- `AWS::AppFlow`_
- `AWS::AppMesh`_
- `AWS::AppStream`_
- `AWS::AppSync`_
- `AWS::ApplicationAutoScaling`_
- `AWS::ApplicationInsights`_
- `AWS::Athena`_
- `AWS::AutoScaling`_
- `AWS::AutoScalingPlans`_
- `AWS::Batch`_
- `AWS::Budgets`_
- `AWS::Cassandra`_
- `AWS::CE`_
- `AWS::CertificateManager`_
- `AWS::Chatbot`_
- `AWS::Cloud9`_
- `AWS::CloudFormation`_
- `AWS::CloudFront`_
- `AWS::CloudTrail`_
- `AWS::CloudWatch`_
- `AWS::CodeArtifact`_
- `AWS::CodeBuild`_
- `AWS::CodeCommit`_
- `AWS::CodeDeploy`_
- `AWS::CodeGuruProfiler`_
- `AWS::CodeGuruReviewer`_
- `AWS::CodePipeline`_
- `AWS::CodeStar`_
- `AWS::CodeStarConnections`_
- `AWS::CodeStarNotifications`_
- `AWS::Cognito`_
- `AWS::Config`_
- `AWS::DAX`_
- `AWS::Detective`_
- `AWS::DLM`_
- `AWS::DMS`_
- `AWS::DataPipeline`_
- `AWS::DirectoryService`_
- `AWS::DocDB`_
- `AWS::DynamoDB`_
- `AWS::EC2`_
- `AWS::ECR`_
- `AWS::ECS`_
- `AWS::EFS`_
- `AWS::EKS`_
- `AWS::EMR`_
- `AWS::ElastiCache`_
- `AWS::ElasticBeanstalk`_
- `AWS::ElasticLoadBalancing`_
- `AWS::ElasticLoadBalancingV2`_
- `AWS::Elasticsearch`_
- `AWS::Events`_
- `AWS::EventSchemas`_
- `AWS::FMS`_
- `AWS::FSx`_
- `AWS::GameLift`_
- `AWS::GlobalAccelerator`_
- `AWS::Glue`_
- `AWS::Greengrass`_
- `AWS::GroundStation`_
- `AWS::GuardDuty`_
- `AWS::IAM`_
- `AWS::ImageBuilder`_
- `AWS::Inspector`_
- `AWS::IoT`_
- `AWS::IoT1Click`_
- `AWS::IoTAnalytics`_
- `AWS::IoTEvents`_
- `AWS::KMS`_
- `AWS::Kendra`_
- `AWS::Kinesis`_
- `AWS::KinesisAnalytics`_
- `AWS::KinesisAnalyticsV2`_
- `AWS::KinesisFirehose`_
- `AWS::LakeFormation`_
- `AWS::Lambda`_
- `AWS::Logs`_
- `AWS::Macie`_
- `AWS::ManagedBlockchain`_
- `AWS::MediaConvert`_
- `AWS::MediaLive`_
- `AWS::MediaStore`_
- `AWS::MSK`_
- `AWS::Neptune`_
- `AWS::NetworkManager`_
- `AWS::OpsWorks`_
- `AWS::OpsWorksCM`_
- `AWS::Pinpoint`_
- `AWS::PinpointEmail`_
- `AWS::QLDB`_
- `AWS::RAM`_
- `AWS::RDS`_
- `AWS::Redshift`_
- `AWS::ResourceGroups`_
- `AWS::RoboMaker`_
- `AWS::Route53`_
- `AWS::Route53Resolver`_
- `AWS::S3`_
- `AWS::SDB`_
- `AWS::SES`_
- `AWS::SNS`_
- `AWS::SQS`_
- `AWS::SSM`_
- `AWS::SSO`_
- `AWS::SageMaker`_
- `AWS::SecretsManager`_
- `AWS::SecurityHub`_
- `AWS::Serverless`_
- `AWS::ServiceCatalog`_
- `AWS::ServiceDiscovery`_
- `AWS::StepFunctions`_
- `AWS::Synthetics`_
- `AWS::Timestream`_
- `AWS::Transfer`_
- `AWS::WAF`_
- `AWS::WAFRegional`_
- `AWS::WAFv2`_
- `AWS::WorkSpaces`_

Currently supported OpenStack resource types
============================================

- `OS::Neutron::Firewall`_
- `OS::Neutron::FirewallPolicy`_
- `OS::Neutron::FirewallRule`_
- `OS::Neutron::FloatingIP`_
- `OS::Neutron::FloatingIPAssociation`_
- OS::Neutron::HealthMonitor
- OS::Neutron::Pool
- OS::Neutron::LoadBalancer
- `OS::Neutron::Net`_
- OS::Neutron::PoolMember
- `OS::Neutron::Port`_
- `OS::Neutron::SecurityGroup`_
- OS::Nova::FloatingIP
- OS::Nova::FloatingIPAssociation
- `OS::Nova::KeyPair`_
- `OS::Nova::Server`_

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

.. _`AWS::AccessAnalyzer`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AccessAnalyzer.html
.. _`AWS::ACMPCA`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ACMPCA.html
.. _`AWS::AmazonMQ`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AmazonMQ.html
.. _`AWS::Amplify`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Amplify.html
.. _`AWS::ApiGateway`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApiGateway.html
.. _`AWS::ApiGatewayV2`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApiGatewayV2.html
.. _`AWS::AppConfig`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppConfig.html
.. _`AWS::AppFlow`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppFlow.html
.. _`AWS::AppMesh`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppMesh.html
.. _`AWS::AppStream`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppStream.html
.. _`AWS::AppSync`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppSync.html
.. _`AWS::ApplicationAutoScaling`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationAutoScaling.html
.. _`AWS::ApplicationInsights`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApplicationInsights.html
.. _`AWS::Athena`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Athena.html
.. _`AWS::AutoScaling`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AutoScaling.html
.. _`AWS::AutoScalingPlans`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AutoScalingPlans.html
.. _`AWS::Batch`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Batch.html
.. _`AWS::Budgets`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Budgets.html
.. _`AWS::Cassandra`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cassandra.html
.. _`AWS::CE`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CE.html
.. _`AWS::CertificateManager`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CertificateManager.html
.. _`AWS::Chatbot`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Chatbot.html
.. _`AWS::Cloud9`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cloud9.html
.. _`AWS::CloudFormation`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CloudFormation.html
.. _`AWS::CloudFront`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CloudFront.html
.. _`AWS::CloudTrail`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CloudTrail.html
.. _`AWS::CloudWatch`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CloudWatch.html
.. _`AWS::CodeArtifact`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeArtifact.html
.. _`AWS::CodeBuild`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeBuild.html
.. _`AWS::CodeCommit`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeCommit.html
.. _`AWS::CodeDeploy`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeDeploy.html
.. _`AWS::CodeGuruProfiler`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeGuruProfiler.html
.. _`AWS::CodeGuruReviewer`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeGuruReviewer.html
.. _`AWS::CodePipeline`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodePipeline.html
.. _`AWS::CodeStarConnections`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeStarConnections.html
.. _`AWS::CodeStarNotifications`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeStarNotifications.html
.. _`AWS::CodeStar`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeStar.html
.. _`AWS::Cognito`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cognito.html
.. _`AWS::Config`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Config.html
.. _`AWS::DAX`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DAX.html
.. _`AWS::Detective`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Detective.html
.. _`AWS::DLM`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DLM.html
.. _`AWS::DMS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DMS.html
.. _`AWS::DataPipeline`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DataPipeline.html
.. _`AWS::DirectoryService`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectoryService.html
.. _`AWS::DocDB`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DocDB.html
.. _`AWS::DynamoDB`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DynamoDB.html
.. _`AWS::EC2`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EC2.html
.. _`AWS::ECR`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ECR.html
.. _`AWS::ECS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ECS.html
.. _`AWS::EFS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EFS.html
.. _`AWS::EKS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EKS.html
.. _`AWS::EMR`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMR.html
.. _`AWS::ElastiCache`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElastiCache.html
.. _`AWS::ElasticBeanstalk`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElasticBeanstalk.html
.. _`AWS::ElasticLoadBalancing`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElasticLoadBalancing.html
.. _`AWS::ElasticLoadBalancingV2`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ElasticLoadBalancingV2.html
.. _`AWS::Elasticsearch`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Elasticsearch.html
.. _`AWS::Events`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Events.html
.. _`AWS::EventSchemas`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EventSchemas.html
.. _`AWS::FMS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FMS.html
.. _`AWS::FSx`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FSx.html
.. _`AWS::GameLift`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GameLift.html
.. _`AWS::GlobalAccelerator`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GlobalAccelerator.html
.. _`AWS::Glue`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Glue.html
.. _`AWS::Greengrass`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Greengrass.html
.. _`AWS::GroundStation`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GroundStation.html
.. _`AWS::GuardDuty`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GuardDuty.html
.. _`AWS::IAM`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IAM.html
.. _`AWS::ImageBuilder`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ImageBuilder.html
.. _`AWS::Inspector`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Inspector.html
.. _`AWS::IoT`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoT.html
.. _`AWS::IoT1Click`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoT1Click.html
.. _`AWS::IoTAnalytics`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTAnalytics.html
.. _`AWS::IoTEvents`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTEvents.html
.. _`AWS::KMS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KMS.html
.. _`AWS::Kendra`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Kendra.html
.. _`AWS::Kinesis`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Kinesis.html
.. _`AWS::KinesisAnalytics`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalytics.html
.. _`AWS::KinesisAnalyticsV2`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisAnalyticsV2.html
.. _`AWS::KinesisFirehose`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisFirehose.html
.. _`AWS::LakeFormation`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LakeFormation.html
.. _`AWS::Lambda`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lambda.html
.. _`AWS::Logs`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Logs.html
.. _`AWS::Macie`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Macie.html
.. _`AWS::ManagedBlockchain`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ManagedBlockchain.html
.. _`AWS::MediaConvert`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaConvert.html
.. _`AWS::MediaLive`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaLive.html
.. _`AWS::MediaStore`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaStore.html
.. _`AWS::MSK`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MSK.html
.. _`AWS::Neptune`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Neptune.html
.. _`AWS::NetworkManager`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkManager.html
.. _`AWS::OpsWorks`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpsWorks.html
.. _`AWS::OpsWorksCM`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OpsWorksCM.html
.. _`AWS::Pinpoint`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Pinpoint.html
.. _`AWS::PinpointEmail`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PinpointEmail.html
.. _`AWS::QLDB`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_QLDB.html
.. _`AWS::RAM`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RAM.html
.. _`AWS::RDS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RDS.html
.. _`AWS::Redshift`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Redshift.html
.. _`AWS::ResourceGroups`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ResourceGroups.html
.. _`AWS::RoboMaker`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RoboMaker.html
.. _`AWS::Route53`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53.html
.. _`AWS::Route53Resolver`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Route53Resolver.html
.. _`AWS::S3`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3.html
.. _`AWS::SDB`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SDB.html
.. _`AWS::SES`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SES.html
.. _`AWS::SNS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SNS.html
.. _`AWS::SQS`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SQS.html
.. _`AWS::SSM`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSM.html
.. _`AWS::SSO`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSO.html
.. _`AWS::SageMaker`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SageMaker.html
.. _`AWS::SecretsManager`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecretsManager.html
.. _`AWS::SecurityHub`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.html
.. _`AWS::Serverless`: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-resources-and-properties.html
.. _`AWS::ServiceCatalog`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ServiceCatalog.html
.. _`AWS::ServiceDiscovery`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ServiceDiscovery.html
.. _`AWS::StepFunctions`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_StepFunctions.html
.. _`AWS::Synthetics`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Synthetics.html
.. _`AWS::Timestream`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Timestream.html
.. _`AWS::Transfer`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Transfer.html
.. _`AWS::WAF`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WAF.html
.. _`AWS::WAFRegional`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WAFRegional.html
.. _`AWS::WAFv2`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WAFv2.html
.. _`AWS::WorkSpaces`: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpaces.html

.. _`OS::Neutron::Firewall`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Neutron::Firewall
.. _`OS::Neutron::FirewallPolicy`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Neutron::FirewallPolicy
.. _`OS::Neutron::FirewallRule`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Neutron::FirewallRule
.. _`OS::Neutron::FloatingIP`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Neutron::FloatingIP
.. _`OS::Neutron::FloatingIPAssociation`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Neutron::FloatingIPAssociation
.. _`OS::Neutron::Net`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Neutron::Net
.. _`OS::Neutron::Port`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Neutron::Port
.. _`OS::Neutron::SecurityGroup`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Neutron::SecurityGroup
.. _`OS::Nova::KeyPair`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Nova::KeyPair
.. _`OS::Nova::Server`: https://docs.openstack.org/heat/latest/template_guide/openstack.html#OS::Nova::Server
