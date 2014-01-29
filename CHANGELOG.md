## 0.4.0 (unreleased)
- Allow to extend resource classes by adding custom attributes [GH-16]
- Add AWS::ElastiCache::SubnetGroup [GH-27]
- Fix examples/VPC\_EC2\_Instance\_With\_Multiple\_Dynamic\_IPAddresses.py [GH-29]
- CacheSecurityGroupNames not required if using VpcSecurityGroupIds [GH-31]
- Add VPNConnectionRoute object and attribute to VPNConnection [GH-33]
- add new CrossZone option to ELB [GH-34]
- Add VPC\_With\_VPN\_Connection example
- Fixup some of the network related validators and pep8 changes
- Add support for Tags and PortRange
- Add more resource name properties per CloudFormation release 2013-12-19
- Add Tier Environment property per CloudFormation release 2013-12-19
- Add VPNGatewayRoutePropagation per CloudFormation release 2013-11-22
- Add Tags properties  per CloudFormation release 2013-09-24
- Add network changes from CloudFormation release 2013-09-17
- Canonicalize integer and bool values for more consistent output [GH-35]
- Add travis-ci for automated testing [GH-38]
- Check output of examples in test\_examples [GH-40]
- Add support for conditions and for Fn::If() [GH-41]
- Tweak ELB ranges to match ec2 console [GH-43]
- Handle bool values better in cfn2py [GH-45]
- Allow strings (as well as Refs) for Subnet VpcId [GH-47]

## 0.3.4 (2013-12-05)
- Adding separators options to print to json function [GH-19]
- Add cfn2py script to convert json templates to Python [GH-22]
- Add EnableDnsSupport and EnableDnsHostnames properties for VPC [GH-23]
- Add VPC support to elasticache [GH-24]
- Fix missing Import Ref [GH-26]
- Add missing AWS::SQS::Queue properties
- Add resource naming (Name Type)
- Allow Ref's in the list objects

## 0.3.3 (2013-10-04)
- Fix Ref() to output the name only [GH-17]
- Add Ref test.
- Fix some IAM issues

## 0.3.2 (2013-09-25)
- Convert VPCDHCPOptionsAssociation to not have \_\_init\_\_
- Fix Output, Parameter and UpdatePolicy to not output a Properties dict
- Raise a ValueError if adding a duplicate object to the template
- Set the correct dictname for UpdatePolicy

## 0.3.1 (2013-09024)
- Make the code more DRY [GH-15]
- Add a optional `name` argument to AWSProperty constructor
- Add ability to push large stack templates to S3
- InstanceType is not required (defaults to m1.small)
- Add AssociatePublicIpAddress property for AutoScaling LaunchConfiguration
- Make Tags an AWSHelperFn to make it easier to assign
- Resource property types should not be in a Properties dictionary
- Clean up "required" error checking and handle property types better

## 0.3.0 (2013-08-07)
- Do not validate AWSHelperFun's [GH-8] [GH-9]
- Add missing return in integer\_range [GH-10]
- integer\_range validator for ELB HealthyCheckInt
- Convert RDS::DBInstance::VPCSecurityGroups to new list type checking
- VPCSecurityGroups for RDS should be a list, not a basestring 

## 0.2.9 (2013-05-07)
- Fixing ELB LoadBalancerPorts not required (error in the AWS docs)

## 0.2.8 (2013-04-24)
- EC2 SecurityGroup Egress & Ingress rules should be objects
- Fix Attributes validator for ELB Policies
- Allow PolicyDocuments to use (if present) awacs Policy objects
- Add test for matching against a tuple of types

## 0.2.6 (2013-03-26)
- Add cfn script to create, tail and show stack resources

## 0.2.5 (2013-03-25)
- UpdatePolicy validation enhancements [GH-5]
- Add VPCSecurityGroups property to AWS::RDS::DBInstance
- DefaultCacheBehavior is a required property for DistributionConfig
- Fix CustomGateway -> CustomerGateway
- Domain does not have any properties
- Fix VPC security group rule bugs
- Added EBSBlockDevice and BlockDeviceMapping classes.
- Add a post-validator to allow individual object to validate themselves
- Add ability to use validate functions on property values
- Add validation of list element types
- Add unit tests

## 0.2.0 (2013-02-26)
- Add support for autoscaling notification configurations [GH-2]
- Add support for AWS::ElastiCache and AWS::RDS
- Move to AWSProperty entirely.
- Add shortcuts for the NotificationTypes strings
- Add Python 3.x compatibility support
- Pass pep8 and pyflakes

## 0.1.2 (2013-02-21)
- First PyPI release
- Add S3 bucket support [GH-1]
