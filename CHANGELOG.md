## 2.1.2 (2017-12-03)
- In SpotFleet::SpotFleetRequestConfigData SpotPrice is optional
- Add RoutingConfig to AWS::Lambda::Alias
- Update AWS::CodeDeploy
- Add CodeDeployLambdaAliasUpdate to UpdatePolicy
- Add AWS::GuardDuty
- Add AWS::Cloud9
- Add initial python resource spec generator
- Update AWS::CodeBuild::Project to 20171201 changes
- Change AWS::Batch::ComputeResources.Tags type to dict (#867)
- Update README for YAML template (#925)
- Typo fix in examples/ElastiCacheRedis.py (#926)
- Adds Fargate support to ECS types (#929)
- Fix SSM NotificationConfig validator type (#930)
- Fix SQS::Queue validation in the case of no QueueName specified (#931)

## 2.1.1 (2017-11-26)
- Add support for VPCOptions in ElasticSearch (#862)
- Add Description property for security group ingress and egress (#910)
- Add QueryLoggingConfig to Route53::HostedZone
- Add SourceRegion to RDS::DBInstance
- Add RootVolumeSize and caleDownBehavior to EMR::Cluster
- Add new properties to ElastiCache::ReplicationGroup
- Add LinuxParameters to ECS::TaskDefinition ContainerDefinitions
- Add LifecyclePolicy to ECR::Repository
- Add ScheduledActions to ApplicationAutoScaling::ScalableTarget
- Add new properties into ApiGateway

## 2.1.0 (2017-11-19)
- Output yaml (to_yaml) using cfn_flip (Fixes #567)
- Allow AWSHelperFn for CodeCommit Trigger Event(s) (#869)
- Adding the AWS::Glue resources (#872)
- Use a list for Serverless::Function Tags (#873)
- Support ProcessingConfiguration for Elasticsearch and Redshift (#876)
- Fixes incorrect class definition. (#877)
- Add TargetGroupInfo to DeploymentGroup #884 (#895)
- Reverting #810 as AWS has changed the casing again (#896)
- Add EMR Cluster MasterInstanceFleet and CoreInstanceFleet properties (#897)
- Add EMR Cluster CustomAmiId (#888) (#898)
- Add SecurityGroupRule Description property (#885) (#899)
- Add support for tags in AWS::KMS::Key. (#900)
- Adding OriginReadTimeout aka OriginResponseTimeout to cloudfront origin settings (#901)
- Added property for OriginKeepaliveTimeout
- Add CloudFrontOriginAccessIdentity type (#903)
- Added support for VpnTunnelOptionsSpecifications (#904)
- Allow ref on Parameter (#905)
- Adds Tags to Cloudfront Distribution (#906)
- CloudFront: add IPV6Enabled property for DistributionConfig (#908)
- Add OptionVersion to RDS:OptionConfigurations
- Add Tags to OpsWorks Layer and Stack
- Add LifecycleHookSpecification in AutoScalingGroup
- Add AmazonSideAsn to EC2::VPNGateway
- Add StateMachineName to StepFunctions::StateMachine
- Change KMS::Key to accept a standard Tags
- Add LambdaFunctionAssociations to CloudFront CacheBehaviors
- Add ResourceName to elasticbeanstalk OptionSettings
- Add AnalyticsConfigurations and InventoryConfigurations to S3::Bucket
- Add RequestValidatorId and OperationName to ApiGateway::Method
- Add deprecation warning for StageName in ApiGateway StageDescription
- Add AWS::CloudFront::StreamingDistribution

## 2.0.2 (2017-10-23)
- Set EC2 BlockDeviceMapping NoDevice property to type dict (#866)

## 2.0.1 (2017-10-21)
- Allow s3.Bucket AccessControl to be an AWSHelperFn
- Add AWS::ElasticLoadBalancingV2::ListenerCertificate
- Add serverless FunctionName and change how Tags are implemented
- Make AdjustmentType an optional property of ScalingPolicy as it is not used/supported for target (#849)
- Add maintenance window for SSM (#851)
- Add Tags, Tracing, KmsKeyArn, DLQ to serverless(SAM) (#853)
- Add new AWS::SSM resources (#854)
- EC2 NoDevice should be type boolean not dict (#858)
- Fixes RecordColumns cardinality for InputSchema and ReferenceSchema (#859)
- Make AWS::Batch::JobQueue::JobQueueName optional (#860)
- Fixes ApplicationOutput/Output cardinality (#863)

## 2.0.0 (2017-10-07)
- Note: the s3.Bucket change (#844) *may* cause a breaking change for non-named arguments.
- Add DefinitionBody to serverless API (#822)
- Adding kinesis stream source to firehose (#823)
- Add `Event::Rule::Target::EcsParameters` (#824)
- Add S3 Transfer Acceleration to AWS::S3::Bucket (#833)
- Add AvailabilityZone property to TargetDescription (#834)
- Add Tags to NATGateway (#835)
- Add ResourceLifecycleConfig to ElasticBeanstalk (#836)
- Add AWS::Athena::NamedQuery (#837)
- Added platformArn to Environment and ConfigurationTemplate (#839)
- Events target (fixes #830) (#840)
- Refactor s3.Bucket to remove custom __init__() and add tests (#844)
- Be more explicit on the use of the Tags object for Tags (#845)

## 1.9.6 (2017-09-24)
- Added missing EU_WEST_2 constants. (#776)
- Override object validation (#780)
- Update PyPI Information (#785)
- Adding IPv6 changes to AWS::EC2::Subnet (#786)
- NetworkACL Protocl Constants (#787)
- Add support for EFS encryption (#789)
- Add AWS::ApiGateway::GatewayResponse (#790)
- Add support for aurora-postgresql as a valid DB engine (#791)
- adding sqs server side encryption (#793)
- Support new code deploy options (#794)
- Add AWS Batch Support (#796)
- VPC expansion support (#797)
- Add NLB Functionality (#806)
- Fix typos in examples/DynamoDB_Table.py (#807)
- Revert "Accept Join type as parameter default value as it returns a string (#752)" (#808)
- Change Cognito UserPool SchemaAttribute required value to boolean (#809)
- Updating case of 'AssignIPv6AddressOnCreation' (#810)
- Fix spelling error  to  in RedshiftVPC example (#811)
- EFS example: SecurityGroupRule can't be referred to as a Ref (#813)
- Update README.rst with current supported resources (#814)
- Add CloudTrail EventSelectors (#815)
- Add DAX support (#818)
- Add KinesisAnalytics support (#819)
- Add new ApiGateway resources (#820)
- Add autoscaling example for http requests that closes #630 (#821)
- Add new S3 Lifecycle Rule properties
- Add IoT DynamoDBv2Action and update DynamoDBAction properties
- Add EventSourceToken to Lambda::Permission
- Add new pseudo parameters
- Add DocumentationVersion to AWS::ApiGateway::Stage
- Add S3 Bucket MetricsConfiguration and fix TagFilter spelling
- Add TargetType to ELBv2::TargetGroup
- Add TargetTrackingConfiguration to AutoScaling::ScalingPolicy
- Add ReplaceUnhealthyInstances and Type to SpotFleetRequestConfigData
- Add ExtendedS3DestinationConfiguration to firehose DeliveryStream
- Add AWS::EC2::NetworkInterfacePermission

## 1.9.5 (2017-07-26)
- Add support for latest Cloudwatch alarms properties (#694)
- Raise ValueError for Outputs and Mappings - Fix Issue #732 (#733)
- Add AWS::EMR::SecurityConfiguration support (#738)
- Create CODE_OF_CONDUCT.md (#740)
- Added UsagePlans to API Gateway example (#741)
- EMR AutoScaling Complex Validation and Introduction of an ignore validator type (#743)
- Add PrivilegedMode option to CodeBuild Environments (#744)
- EFS DependsOn Ref to object fix (#746)
- README - add syntax highlighting (#747)
- Make handling of DependsOn more pythonic (#748)
- Accept Join type as parameter default value as it returns a string (#752)
- AWS SAM support (#754)
- Fixed UsagePlan example to proper Ref (#755)
- Fix cognito StringAttributeConstraints property names (Fixes #756)
- Add 'SourceAuth' property to CodeBuild Source (#758)
- Make it easier to get at hidden attributes (Fixes #760)
- Size/IOPS should be positive_integers (#761)
- Check that FIFO Queues end with .fifo (#757)
- Add AWS::CloudWatch::Dashboard (Fixes #763)
- Ulimit's HardLimit and SoftLimit validator change (#764)
- Adding EgressOnlyInternetGateway to EC2::Route (#765)
- Allow passing in a dict into DashboardBody (#767)
- Handle SQS QueueName using an AWSHelperFn (Fixes #773)
- LifecycleHook NotificationTargetARN and RoleARN are now optional
- Remove RoleArn from Events::Rule and add to Target property
- Add TracingConfig property to AWS::Lambda::Function
- Add Tags to some RedShift resources
- Add AWS::ApiGateway::DomainName
- Add AWS::EC2::EgressOnlyInternetGateway
- Add AWS::EMR::InstanceFleetConfig
- Add BinaryMediaTypes to ApiGateway::RestApi
- Add TargetTrackingScalingPolicyConfiguration
- Add TrailName to CloudTrail::Trail
- Add AlarmConfiguration and TriggerConfigurations
- Add Tags and TimeToLiveSpecification to DynamoDB::Table
- Add RetentionPeriodHours to Kinesis::Stream
- Add ReplicationSourceIdentifier to RDS::DBCluster
- Add LoggingProperties to Redshift::Cluster
- Add AWS Database Migration Service (DMS) support
- Add test target to Makefile
- Make it easier to download the latest CF resource spec
- Added and reverted out of this release:
  - Fix pycodestyle issue in tests/test_yaml.py
  - Output yaml (to_yaml) using cfn_flip (Fixes #567)
  - Special case If during parameter checking (Fixes #772)
  - Raise TypeError when a scaler AWSHelperFn is used in a list context (#751)

## 1.9.4 (2017-06-04)
- Fix typo in S3_Bucket.py example (#696)
- Added .Ref & .GetAtt helper methods (#697)
- Add Pseudo Parameter Ref objects (#698)
- Fix NamespaceType typo in codebuild::Artifacts() (fixes #701)
- Add IpAddressType property to elbv2. (#703)
- Add new AWS::Lambda::Function Tags support (#705)
- Added ECS PlacementConstraints, PlacementStrategy, and ServiceName (#706)
- Add missing CidrIpv6 property to securityrule. (#710)
- Add missing properties to various objects in ec2.py (#711)
- logs.LogGroup#RetentionInDays is strictly defined list (#712)
- Add ManagedPolicyName to AWS::IAM::ManagedPolicy (Fixes #714)
- Add better validations for Parameter Default types (Fixes #717)
- Add AWS::Cognito (fixes #720)
- Add required attribute, JobFlowId, to EMR::InstanceGroupConfig (#722)
- Add WAFRegional support (#723)
- fix for ElastiCacheRedis.py example to use awacs (#725)
- Add EMR autoscaling (#729)
- Add SshUsername to AWS::OpsWorks::UserProfile
- Add PlacementConstraints to AWS::ECS::TaskDefinition
- Add MaximumExecutionFrequency to Config SourceDetails

## 1.9.3 (2017-04-13)
- Fix pycodestyle by using an explicit exception type
- Add more details to pycodestyle errors for travis runs
- Fix validator function exception test
- Remove limit check on conditions - Fixes #657
- Allow valid value for TargetGroup HealthCheckPort (#659)
- Added step functions and basic tests (#661)
- Adding example for CloudTrail (from http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html) (#667)
- Fix ApiGateway.py sample (#666)
- Update comment on type checking
- Added missing props to ec2.NetworkInterfaces (#669) (#670)
- Add WAF Common Attacks Sample (#675)
- Updated constants with new instance types (#674)
- SSM Targets - fix spelling mistake (Value => Values) (#673)
- Do json validation on ApiGateway::Model Schema (Fix #679) (#681)
- SQS: Add FifoQueue and ContentBasedDeduplication (#687)
- VPCPeeringConnection: add PeerOwnerId & PeerRoleArn (#688)
- IAM: Add InstanceProfileName to InstanceProfile (#689)
- Add ApiGateway UsagePlanKey resource
- Add DeadLetterConfig property to Lambda::Function
- Add new subproperties to route53 and redshift (#690)
- Route53: ChildHealthChecks is a list of strings (#690)
- Fix typo in S3_Bucket_With_Versioning_And_Lifecycle_Rules.py (#693)
- Allow a dict to be passed in to initalize Tags (#692)
- Add SSM::Parameter
- Update autoscaling example to remove rebinding (#695)

## 1.9.2 (2017-01-29)
- Extra template validation (#635)
- Update ECS to Jan 17, 2017 release (#642)
- Add Timezone property to DBInstance (#643)
- Test Python 3.6 (#644)
- Adding RDS engine support for oracle-se2 (#646)
- Correct required in ecs.Service (#645)
- Add Separator property to IoT Firehose Action
- Add Fn::Split function (#647)
- Added to_dict() method to troposphere.Template (#651)
- Allow use of AWSHelperFn for IOPS (#652)
- Allow HelperFN w/ autoscaling policies (#654)

## 1.9.1 (2017-01-03)
- Improve readability of AssumeRolePolicyDocument attribute (#591)
- Add Environment to Lambda Function (#616)
- Adding DataSources to OpsWorks App and RdsDbInstances to OpsWorks Stack (#621)
- Added SNS::Subscription resource (SubscriptionResource) (#622)
- Added CodeBuild Project resource and a CodeBuild example (#624)
- Add back support for Python 2.6 (#626)
- Fixed missing add_resource in example Cloudwatch rule (#629)
- Create new property Environment for aws lambda Function (#631)
- Add KmsKeyArn to Lambda Function
- Add CopyTagsToSnapshot to RDS::DBInstance
- Fix pycodestyle issues with examples/Lambda.py
- Add AWS::SSM::Association
- Add AWS::EC2::SubnetCidrBlock and AWS::EC2::VPCCidrBlock
- Add mutually_exclusive validator
- Add DocumentType to AWS::SSM::Document
- Add OpsWorks Resources: UserProfile and Volume
- Update opsworks per 2016-11-22 changes
- Allow both dict and string for opswork CustomJson
- Add IPv6 support from 2016-12-01 update

## 1.9.0 (2016-11-15)
- Note: the dynamodb change below may cause backwards compatibility issues.
  There have been deprecation warnings for a while.
- Replace dynamodb module with dynamodb2 (#564)
- Add CodeCommit as a supported AWS resource type
- Add update of github Releases page to RELEASE doc
- Update elasticache for 2016-10-12 changes (#592)
- Support for S3 Lifecycle Rule property NoncurrentVersionTransitions (#596)
- Include resource title in required attr exception (#597)
- Added Placement class for the Placement property in LaunchSpecifications. (#598)
- Add EFS example (#601)
- Add support to old mysql db engine (#602)
- Fix typo in Example Allowed Values (#603)
- Remove `title` validation. Fixes #428 (#605)
- Add support for conditions in cfn2py script (#606)
- Added MongoDB default port to constants (#608)
- Add HttpVersion prop to DistributionConfig (CloudFront HTTP/2 Support) (#609)
- Added missing QueryStringCacheKeys property to CloudFront ForwardedValues (#612)
- Add a validator for ELB names (#615)

## 1.8.2 (2016-10-08)
- Add SpotPrice to SpotFleet LaunchSpecifications
- Add new properties to ECS (Clustername to Cluster and Family to TaskDefinition)
- Add Alias object to KMS (fixes #568)
- Added cross-stack references (#569)
- Handle lambda => awslambda mapping in cfn2py (#573)
- Add support for Tags to Certificate Manager Certificates (#574)
- Adding enhanced monitoring to rds.DBInstance (#575)
- Add support for LogGroupName in Logs::LogGroup (#576)
- Update Export param (#579)
- Add support for `Fn::Sub` (#582)
- RDS DBInstance Engine required even when DBSnapshotIdentifier is set (#583)
- Resource updates for 2016-10-06 changes (Fixes #584)
- Add AWS::ApiGateway::UsagePlan (fixes #585)
- Add AWS::CodeCommit::Repository (fixes #586)
- Provide better type checking for values in from_dict (#587)
- Allow HelperFn in UpdatePolicy for ASG (#588)
- Fixed from_dict case where you have a list of non BaseAWSObjects (#589)

## 1.8.1 (2016-09-12)
- Add TargetGroupArn and fix ContainerPort (#549)
- Update ApiGateway resources (#550)
- Add support for AutoScalingCreationPolicy (#552)
- Change param type for resource: RestAPI (#553)
- Add support for IAM Roles in ECS Task Definitions (#556)
- Allow Tags on AWS::CloudFormation::Stack (#557)
- Added support for protocol in container definition PortMapping property. (#558)
- Add Tags prop to Kinesis::Stream (#565)
- Add a sample ECS Cluster template (#559)
- Add support for ElasticsearchVersion in Elasticsearch Domain (#560)
- WAF SizeContraint needs to be an AWSProperty (Fixes #561)
- Add Tags prop to Kinesis::Stream (#565)

## 1.8.0 (2016-08-15)
- Support "UserName" property for AWS::IAM::User #529
- Remove double S from S3ObjectVersion (fixes #530) (#531)
- Fix TemplateGenerator import logic. (#533)
- Add Name attributes for IAM groups and roles (#535)
- Automatically check if zip_file exceeds 4096 chars #537
- Add AWS Certificate Manager (#538)
- Add Application Auto Scaling (#539)
- CloudFront updates (Aug 9, 2016) (#540)
- Add PerformanceMode to FileSystem resource (#541)
- Add AWS Internet of Things (#542)
- Extend Template constructor. (#543)
- Add application loadbalancer objects and properties (#544)
- Improve check_zip_file to calculate a minimum length (#548)

## 1.7.0 (2016-07-07)
- Convert fake AWSHelperFns into AWSProperties (#478)
- cfn script: allow update (#484)
- Validate the template against AWS before stack creation (#485)
- Fix capitalization in README (#487)
- Remove duplicate waf FieldToMatch class (fixes #489)
- Tune validation logic and test cases for S3 bucket names (#486)
- waf XssMatchTuple should be an AWSProperty (Fixes #498)
- Allow setting a different region for S3 upload (#491)
- fix attribute for ApiKey (Enable -> Enabled) (#492)
- Invoke join correctly (#493)
- EMR: fix EBS configuration (#497)
- EMR: Action on Failure Fix (CONTINUE_AND_WAIT->CANCEL_AND_WAIT) (#501)
- Rewritten the helper to be more flexible (#502)
- Added support for Kinesis Firehose (#505)
- Add support for VPC Flow Logs (#507)
- Syntax highlighting for readme python sample (#508)
- Added Name property to Kinesis streams (#510)
- Availability zones and EC2 instance type (#512)
- Add `AutoScalingReplacingUpdate` to `UpdatePolicy` (#513)
- Removed validation for DBSubnetGroupName when creating a read replica with SourceDBInstanceIdentifier (#515)
- EMR configurations values: also allow AWS helper functions (#516)
- Fix AssociationParameters Value type to list of strings (#518)
- Add DependsOn to Deployment and remove Enabled from StageKey (#519)
- Update fields in apigateway StageDescription (#521)
- Fix rename pep8->pycodestyle and bump to fixed pyflakes (#522)
- Allows MultiAZ=false with AvailabilityZone in rds (#524)
- Do not require Status as a param in iam.AccessKey (#525)
- Fix badges in README

## 1.6.0 (2016-05-04)
- Remove unnecessary AWSHelperFn from props
- ReplicationConfigurationRules Destination is now an object (#380)
- Add WAF SizeConstraintSet and XssMatchSet
- Logs SubscriptionFilter (#413)
- Elasticsearch support (#415)
- Fixed ConfigSnapshotDeliveryProperties type (#420)
- Adding support for EMR resources (#421)
- Fix `ecs.TaskDefinition.Volumes` that was incorrectly flagged as required (#422)
- AWS::ECR test example (#423)
- Add cloudfront hostedzoneid for route53 (#427)
- Typo in variable name (431)
- ScalingAdjustment is an integer (#432)
- Add Compress to CloudFront (#433)
- Added missing S3OriginConfig parameter(#437)
- Allow both GetAtt and a basestring (#440)
- Add VpcConfig to AWS::Lambda::Function (#442)
- Add Version Resource to awslambda (#443)
- Add Alias Resource to awslambda (#444)
- Ignore If expression during validation of ASG (#446)
- Add test and tweak fix for ASG MaxSize If fix (#446)
- Provide Valid Lambda Function Memory Values for use in Parameters (#449)
- Add FunctionName to Lambda::Function (#452)
- Add support for EBS volume configuration in EMR resources (#453)
- Add elasticsearch instance type constants (#454)
- DomainName isn't a required parameter (#457)
- Create Documentation To Help Contributors (#458)
- Move Groups to property, add policy template version (#460)
- Fix Elasticsarch Domain object naming and add backward compatibility (#461)
- EC2 update FromPort, ToPort and Egress as optional (#463)
- ApiGateway Resources (#466)
- Added CloudWatch Events support (#467)
- Import JSON Templates (#468)
- Fix config Source object to take a list of SourceDetails (#469)
- Update Contribute Document to Use Requirements.txt (#470)
- Update to Apr 25, 2016 release (#471)
- Implement LifecycleRule Transitions property (#472)
- Better AWSHelperFn support in template generator (#473)
- Fix Bucket AccessControl to allow Ref (#475)
- Fix baseclass for AWS::Logs::Destination (#481)
- Add test for AWS::Logs::Destination (#482)

## 1.5.0 (2016-03-01)
- Add MariaDB to list of RDS engines [GH-368]
- Add ap-northeast [GH-373]
- Add T2 Nano [GH-374]
- capability support for cfn [GH-375]
- Update to resource list in documentation [GH-383]
- More info from validator function errors [GH-385]
- Add testing for python 3.5 [GH-388]
- Extended title validation [GH-389]
- EC2 NAT Gateway [GH-394]
- Add AWS::ECR::Repository [GH-395]
- Add KmsKeyId and StorageEncrypted to DBCluster [GH-396]
- Add awacs soft dependency [GH-397]
- New dynamodb2 module to replace dynamodb for consistent interface [GH-398]
- Add IsMultiRegionTrail support [GH-399]
- Add IncludeGlobalResourceTypes to RecordingGroup [GH-400]
- Capitalize examples [GH-404]
- use location constants for bucket creation in cfn [GH-409]

## 1.4.0 (2016-01-01)
- Add RDS Aurora support [GH-335]
- Change DeploymentGroup Ec2TagFilters to list [GH-337]
- Correct EC2 SpotFleet LaunchSpecifications [GH-338]
- RDS::DBCluster change AvailabilityZone to AvailabilityZones [GH-341]
- ECS LoadBalancerName property is a string [GH-342]
- CodeDeploy S3Location Version property is not a default requirement [GH-345]
- Add AutoEnableIO to AWS::EC2::Volume
- Only discard Properties in JSONrepr [GH-354]
- CodeDeploy added ApplicationName [GH-357]
- CodeDeploy DeploymentGroupName property missing [GH-358]
- Add in cloudfront properties for max, default [GH-360]
- Allow RDS iops to be 0 [GH-361]
- Add CodePipline support [GH-362]
- Implemented CloudFormation changes from Dec 3 and Dec 28 [GH-366]
- Add AWS::Config, AWS::KMS, AWS::SSM

## 1.3.0 (2015-10-21)
- Add new resources from 2015-10-01 CloudFormation release:
  - AWS::CodeDeploy
  - AWS::DirectoryService::SimpleAD
  - AWS::EC2::PlacementGroup and AWS::EC2::SpotFleet
  - AWS::Lambda::EventSourceMapping and AWS::Lambda::Permission
  - AWS::Logs::SubscriptionFilter
  - AWS::RDS::DBCluster and AWS::RDS::DBClusterParameter
  - AWS::WorkSpaces::Workspace
- Add updates to these resources from 2015-10-01 CloudFormation release:
  - AWS::ElastiCache::ReplicationGroup
  - AWS::OpsWorks::Stack
  - AWS::OpsWorks::App
  - AWS::S3::Bucket
- Add ElastiCache (Redis) Example [ GH-329]
- RDS: Added postgresql-license [GH-324]
- tail: only add unseen events [GH-327]
- Make Ref() work with datapipeline.ObjectField.RefValue [GH-328]
- Fix DeploymentGroup resource_type (AWS::CodeDeploy::DeploymentGroup) [GH-333]
- Add concatenation operator function __add__ for Tags [GH-334]

## 1.2.2 (2015-09-15)
- Give more info about type errors [GH-312]
- Move `tail` within the troposphere library. This lets external libraries
  leverage this function [GH-315]
- Improve opsworks validation [GH-319]
- Fix RDS validation with conditional parameters [GH-320]

## 1.2.1 (2015-09-07)
- Bugfix for RDS Ref/GetAtt issue [GH-310]

## 1.2.0 (2015-09-04)
- Add support for EFS
- Elasticache: only validate az choices if azs is a list [GH-292]
- Add from_dict function to BaseAWSObject [GH-294]
- IAM: Path is optional for Role and InstanceProfile [GH-295]
- Validate parameter options based on Type [GH-296]
- RDS: Add more specific validators to DBInstance [GH-297]
- Add constants for the parameter types [GH-300]
- Add lambda ZipFile property [GH-301]
- Adds VPCEndpoint resource type [GH-304]
- Supports tags in ElasticBeanstalk environments [GH-308]
- Move cloudformation attribute setting to __setattr__ [GH-309]

## 1.1.2 (2015-07-23)
- Clarify the license is a [BSD 2-Clause license](http://opensource.org/licenses/BSD-2-Clause)
- Add FindInMap type check for AutoScalingGroup validation of group sizes [GH-285]
- Implement the template Metadata section [GH-286]

## 1.1.1 (2015-07-12)
- Rename lambda->awslambda [GH-268]
- Add t2 large instance type [GH-269]
- IAM: status required and managedpolicyarns [GH-272]
- Fix wrong prop name in rds.OptionGroup OptionGroupConfigurations->OptionConfigurations [GH-274]
- Add CloudFormation CustomResource [GH-278]
- Add rds snapshot on delete example [GH-280]
- Unable to pass Cluster name as String [GH-281]
- Fix unable to set StringValue on ObjectField in DataPipeline [GH-283]

## 1.1.0 (2015-06-15)
- added AWS::CloudFormation::Stack NotificationARNs property [GH-243]
- Add additional import for PrivateIpAddressSpecification [GH-247]
- Add true s3 bucket name validator [GH-249]
- Replace strict `int` comparison by flexible `troposphere.validators.integer` [GH-251]
- Add validation for AZMode property on CacheCluster objects [GH-252]
- Fixing Opsworks Naming (ThresholdWaitTime -> ThresholdsWaitTime) [GH-253]
- Adding AutoScalingType to OpsWorks Instance [GH-255]
- Allow extending classes + tests [GH-257]
- Release June 11, 2015 [GH-259]
- Add M4 instances and Memcached port [GH-260]
- Add property for Subnet: MapPublicIpOnLaunch [GH-261]
- Minor improvements and fixes [GH-262]
- Update LoginProfile. Note: this is a breaking change and requires adding a
  ```Password=``` keyword parameter into LoginProfile. [GH-264]
- Add 2 additional properties (elasticache:CacheCluster:SnapshotName and opsworks:Layer:LifecycleEventConfiguration) [GH-265]

## 1.0.0 (2015-05-11)
- Fix two elasticache properties [GH-196]
- Add interim MinimumProtocolVersion to CloudFront ViewerCertificate [GH-218]
- Missing OriginPath in cloudfront.py [GH-220]
- Fix DBInstance constraints in order to allow the creation of RDS read-only replicas  [GH-221]
- Add properties CharacterSetName, KmsKeyId, and StorageEncrypted to AWS::RDS::DBInstance [GH-224]
- Add Route53 HostedZoneVPCs, HostedZoneTags, HealthCheckTags
- Add new properties from 2015-04-16 CloudFormation release [GH-225, GH-240]
- Allow default region for GetAZs() [GH-232]
- Make AvailabilityZones parameter optional in AutoScalingGroup
- EventSubscription resource + EC2 types [GH-227]
- Python 3.4 support [GH-228]
- examples fix: users is list [GH-237]
- SNS Topic fields are not required [GH-230]
- Make AvailabilityZones parameter optional in AutoScalingGroup [GH-236]

## 0.7.2 (2015-03-23)
- Support AWS helper functions in lists during validation [GH-179]
- Update README [GH-183]
- Fixing RedshiftClusterInVpc example; incorrect SG setup [GH-186]
- Add optional NonKeyAttributes to DynamoDB Projection class [GH-188]
- Change AutoScaling ScheduledAction StartTime, EndTime, and Recurrence to optional [GH-189]
- CloudFront forwarded values required on cache behavior [GH-191]
- DynamoDB attribute definitions required [GH-192]
- Add some ec2 required fields [GH-193]
- Fix ElasticBeanstalk resources [GH-213]
- Fix iam Policy Resource/Property bug [GH-214]

## 0.7.1 (2015-01-11)
- Fix UpdatePolicy validation [GH-173]
- Add AWS::CloudFormation::Init ConfigSets support [GH-176]
- Change CloudWatch Alarm's Threshold prop to be basestring [GH-178]

## 0.7.0 (2015-01-02)
- Added new Google Group for discussion:
  https://groups.google.com/forum/#!forum/cloudtools-dev
- Fixing ValueError message to refer the correct package [GH-135]
- Change cfn to add -R with no argument lists all the Stacks [GH-138]
- Add eu-central-1 region (Frankfurt) [GH-139]
- ConfigurationTemplate is an Object [GH-140]
- Release: AWS CloudFormation on 2014-11-06 [GH-141]
- Remove duplicate security_group from port [GH-143]
- UpdatePolicy and CreationPolicy [GH-144]
- Fixes duplicate key error reporting [GH-145]
- Fix warning in CloudFront example description [GH-148]
- Cfn script create bucket in the specified region [GH-149]
- Remove Unnecessary EOL whitespace [GH-150]
  Note: this changes the default JSON separators.
- More metadata options [GH-153]
- Metadata auth [GH-155]
- Fixed CreationPolicy [GH-157] [GH-160]
- Addded AWS template VPC_Single_Instance_In_Subnet example [GH-162]
- Add 2014-12-24 CloudFormation release changes [GH-167] [GH-168] [GH-169]
- Add GSI & LSI Functionality [GH-161] [GH-172]
- Fixed landscape.io issues [GH-170]

## 0.6.2 (2014-10-09)
- Update to 2014-09-29 AWS release [GH-132]
- Add ElastiCache & Port # Constants [GH-132]
- Add ELB Tag Support [GH-133]
- Fix DBSecurityGroupIngress required properties [GH-134]

## 0.6.1 (2014-09-28)
- Update InitConfig per AWS docs [GH-120]
- S3 improvement + essential constants [GH-125]
- Allow FindInMap() for ec2.NetworkInterfaceProperty.GroupSet [GH-128]

## 0.6.0 (2014-08-26)
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
- Make RDS DBInstance MasterUsername and MasterPassword optional [GH-116]
- Add CloudTrail, tweaks to CloudWatch Alarm, and support route53 AliasTarger EvaluateTargetHealth [GH-117]
- Add LogDeliveryWrite canned ACL for S3 bucket [GH-118]

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
