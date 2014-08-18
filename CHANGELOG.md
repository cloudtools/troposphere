## Pending
- Use subnet group for param, not vpc securitygroup [GH-65]
- Add support for Equals function and Condition [GH-66]
- Added ELB access logs and CrossZone test [GH-67]
- Added support for more condition functions [GH-69]
- Tweaked a few integer validation messages [GH-71]
- Fix resource.name backward compatibility regression
- Fix pep8 errors due to new pep8 1.5.x changes [GH-72]
- Allow Ref() in VPNGatewayRoutePropagation RouteTableIds list [GH-73]
- Add OpsWorks Support [GH-74]
- Add AutoScalingGroup TerminationPolicies [GH-77, GH-87]
- Add new property MetricsCollection [GH-79]
- Patching Users class to use basestring or Ref type for Groups [GH-80]
- Added support for Kinesis [GH-81]
- Allow autoscaling group to support 'min instances in service' and 'max size' values that are Refs [GH-82]
- Added support for Redshift [GH-84]
- Add DestinationSecurityGroupId in ec2.SecurityGroupRule [GH-85]
- Add CloudFront CacheBehavior [GH-86]
- Tweak UpdatePolicy properties [GH-88]
- Tweaks to rds.DNInstance [GH-89]
- Tweaks to EC2 DeviceIndex property values [GH-90]
- Fix AutoScalingGroup MinSize MaxSize [ GH-92]
- Add Encrypted option to AWS::EC2::Volume [GH-96]
- Add missing config to s3.Bucket [GH-97]
- Add CloudFront DistributionConfig, CacheBehavior and DefaultCacheBehavior [GH-98]
- Add EC2 Instance InstanceInitiatedShutdownBehavior [GH-99]
- Updating the block device options for AutoScalingGroups [GH-100]
- Added support for AWS::CloudFormation::Init in AutoScalingGroup [GH-101]
- Added VPCPeering class [GH-102]
- Opworks CustomJson property expects a JSON object not a string [GH-103]
- Add support for VersioningConfiguration on S3 buckets [GH-104]
- Added Logs resource type [GH-105]
- Add PlacementGroup param to AutoScalingGroup [GH-111]
- Add VpcPeeringConnectionId parameter to EC2 Route [GH-113]

## 0.5.0 (2014-03-21)
- Add OpenStack native types [GH-61]
- Make `integer()` validator work with any integer-like object [GH-57]
- Add support to ELB ConnectionDrainingPolicy [GH-62]
- Add more OpenStack resource types and validation [GH-63]

## 0.4.0 (2014-02-19)
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
- Add InstanceID to AutoScalingGroup and LaunchConfiguration
- ec2.DHCPOptions NTPservers -> NtpServers [GH-54]
- Add SQS dead letter queue from CloudFormation release 2014-01-29
- Add AutoScaling ScheduledAction from release 2014-01-27
- Add Tags for SecurityGroups [GH-55]
- RecordSets in Route53 not formatted correctly [GH-51]
- Allow Ref() in NetworkInterfaceProperty GroupSet list [GH-56]

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
