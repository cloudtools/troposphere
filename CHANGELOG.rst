2.6.2 (2020*07*12)
------------------
* Add Description property to EC2::TransitGateway (#1674)
* Adding AWS::ImageBuilder::Image object, per May 7, 2020 update
* Adding missing AWS::ApiGatewayV2::VpcLink object
* Adding new AWS::SSM::Association property, per May 7, 2020 update
* Update template_generator.py
* Handle list type properties with a function validator (#1673)
* Change RegularExpressionList
* Remove Regex object in favour of basestring
* Bug Fixes: wafv2 names not required
* Update instance types in constants
* Add AWS::CodeStarConnections::Connection props, per May 14, 2020 update
* Adding misc AWS::DMS properties, per May 14, 2020 update
* Adding misc AWS::MediaStore::Container properties, per May 14, 2020 update
* updating AWS::ServiceCatalog::CloudFormationProduct properties, per May 14, 2020 update
* Changing AWS::Synthetics::Canary props, per May 14, 2020 update
* Adding misc AWS::GlobalAccelerator objects, per May 14, 2020 update
* Adding new AWS::Macie resources, per May 14, 2020 update
* Add sample Aurora Serverless RDS template
* Fixing misc AWS::ImageBuilder properties
* Updating AWS::StepFunctions::StateMachine props, per May 21, 2020 update
* Update AWS::SSM::Parameter properties, per May 21, 2020 update
* Update AWS::CodeBuild::ReportGroup properties, per May 21, 2020 update
* Fix bools in example output
* Adding hibernation options to LaunchTemplateData
* ExcludedRules are listed directly, not wrapped
* fix syntax
* add OnSuccess
* Update AWS::EFS::AccessPoint per 2020-05-28 changes
* Update AWS::CodeGuruProfiler::ProfilingGroup per 2020-06-03 changes
* Update AWS::EC2::ClientVpnEndpoint per 2020-05-28 changes
* Add DBProxy and DBProxyTargetGroup to AWS::RDS per 2020-06-04 changes
*  Add support for ARM and GPU containers for CodeBuild (#1699)
* Fix S3Encryptions in Glue EncryptionConfiguration (#1725)
* Convert stepfunctions.DefinitionSubstitutions to dict (#1726)
* Add GroundStation link (#1727)
* Update AWS::ElasticLoadBalancingV2::LoadBalancer per 2020-06-11 changes
* Update AWS::ElastiCache::ReplicationGroup per 2020-06-11 changes
* Update AWS::CloudFront::Distribution per 2020-06-11 changes
* Update AWS::CertificateManager::Certificate per 2020-06-11 changes
* Update AWS::EC2::Volume per 2020-06-11 changes
* Add AWS::IoT::ProvisioningTemplate per 2020-06-04 changes (Fixes #1723)
* Added Serverless::Application and Serverless ApplicationLocation (#1549)
* Fix required setting for SageMaker::Model PrimaryContainer (Fixes #1729)
* Added capacity providers
* Update AWS::EFS::FileSystem per 2020-06-16 changes
* Update AWS::Lambda::Function per 2020-06-16 changes
* Update AWS::FMS::Policy per 2020-06-18 changes
* Fix tests and alphabetize properties in ECS
* Update AWS::ServiceDiscovery per 2020-06-22 changes
* This isn't required
* Update AWS::AppMesh per 2020-06-25 changes
* Support attribute Mode for SageMaker Model ContainerDefinition
* Add SourcePrefixListId to the ec2.SecurityGroupIngress validator (Fixes #1739)
* Add ApplicationCloudWatchLoggingOption for KinesisAnalyticsV2 (Fixes #1738)
* Add required TargetGroupName to DBProxyTargetGroup
* Add VpcConfiguration to AWS::KinesisFirehose::DeliveryStream (Fixes #1717)
* Update AWS::Events::Rule per 2020-07-06 changes
* Add AWS::QLDB::Stream per 2020-07-08 update
* Add AWS::CodeGuruProfiler::ProfilingGroup.ComputePlatform per 2020-07-09 update
* Add AWS::CodeBuild::Project Source: BuildStatusConfig per 2020-0709 update
* Add AWS::Athena::DataCatalog per 2020-07-09 update
* Add AWS::EC2::PrefixList per 2020-07-09 update
* Add AWS::ElasticLoadBalancingV2::Listener.AlpnPolicy per 2020-07-09 update
* Update AWS::Synthetics per 2020-07-09 update
* Add AWS::Amplify::App.EnableBranchAutoDeletion per 2020-07-09 update
* Update AWS::FSx::FileSystem.LustreConfiguration per 2020-07-09 update
* Update AWS::Amplify::Domain per 2020-07-09 update

2.6.1 (2020*05*04)
------------------
* Fix README for PyPI upload
* Remove extra PublicAccessBlockConfiguration in s3 (Fixes #1541)
* Added support for ForwardConfig in Listener (#1555)
* Fix up a couple of items for ELBv2 from #1555
* Fixing a missimplementation of rules, caused by a bug in the document… (#1599)
* fix: include valid postgres capacity configurations (#1602)
* adding misc AppMesh properties, per Feb 27 2020 update
* adding misc FSX properties, per Feb 27 2020 update
* Adding new AWS::CloudWatch::CompositeAlarm object, per March 2 2020 update
* Adding new AWS::GroundStation resources, per Feb 27 2020 update
* Add README link for GroundStation (#1606)
* Fixup WAFv2 TextTransformations property and required (#1607)
* Adding cloudfront OriginGroups properties, per March 5 2020 update
* AWS::EC2::SecurityGroupIngress.SourcePrefixListId (#1622)
* adding AWS::Athena::WorkGroup, per March 5 2020 update
* Adding EncryptionConfig props to AWS::EKS::Cluster, per March 5 2020 update (#1610)
* adding AWS::CodeStarConnections::Connection, per Marche 5 2020 update
* Adding AWS::Chatbot::SlackChannelConfiguration, per March 5 2020 update
* Fixup recent CodeStarConnections and Chatbot additions
* Fixes to acmpca (#1660)
* adding misc Greengrass props, per March 09 2020 update
* adding misc AWS::MSK::Cluster properties, per March 12 2020 update
* Adding MeshOwner prop to misc AppMesh objects, per March 12 2020 update
* Adding new AWS::Cassandra resources, per March 16 2020 update
* Fixup link and comments for AWS::Cassandra (related to #1616)
* Fix several problems in wafv2
* Add IotAnalyticsAction and StepFunctionsAction to IoT TopicRule Actions
* Add missing IoTAnalytics properties, add Datastore object, add test IoTAnalytics example
* Attributes for AddAttributes is a dict
* add secrets manager type to codebuild environment variable types
* Usageplan throttle (#2)
* update example to include method as required
* Adding AWS::ResourceGroups::Group resource, per March 19, 2020 update
* Adding AWS::CodeGuruProfiler::ProfilingGroup resource, per March 19, 2020 update
* Fixup links in README.rst
* adding AWS::EC2::ClientVpnEndpoint properties, per March 19, 2020 update
* Adding AWS::DMS::Endpoint props, per March 23, 2020 update
* Adding AWS::AutoScaling::AutoScalingGroup props, per March 26, 2020 update
* Adding misc AWS::ApiGatewayV2::Integration properties, per March 26, 2020 update
* Adding AWS::ServiceCatalog::LaunchRoleConstraint props, per April 2, 2020 update
* Adding AWS::CloudWatch::InsightRule props, per April 2, 2020 update
* Fix new test changes to use TROPO_REAL_BOOL
* Change ApiGateway::RestApi FailOnWarnings from basestring to boolean (Fixes #1655)
* Update SAM Schedule event source spec
* AWS::SecurityHub::Hub Tags uses the wrong format
* Adding AWS::NetworkManager resource, per March 19, 2020 update
* Adding AWS::Detective resources, per March 26, 2020 update
* Adding misc AWS::IoT props, per March 26, 2020 update
* Adding AWS::EC2::Volume props, per March 26, 2020 update
* Adding AWS::FSx::FileSystem properties, per April 2, 2020 update
* Adding misc AWS::Glue properties, per April 16, 2020 update
* Adding new AWS::Synthetics::Canary resource, per April 23, 2020 update
* Adding AWS::ImageBuilder resources, per April 23, 2020 update
* Adding new AWS::CE::CostCategory resource, per April 23, 2020 update
* Fix typo: pros => props
* Update EventSchemas per 2020-04-30 changes
* Update Synthetics per 2020-04-30 changes
* Update Transfer per 2020-04-30 changes

2.6.0 (2020*02*22)
------------------
* Add ProvisionedConcurrencyConfig for AWS::Serverless::Function (#1535)
* Add update policy that allows for in place upgrade of ES cluster (#1537)
* Add ReportGroup and SourceCredential to CodeBuild
* Add Count property to EC2::Instance ElasticInferenceAccelerator
* Add EC2::GatewayRouteTableAssociation
* Update FSx per 2019-12-19 changes
* Add MaxAllocatedStorage to RDS::DBInstance
* Add Name property to SSM::Document
* Add OpenMonitoring property to MSK::Cluster
* Break out NoDevice property validation (Fixes #1551) (#1553)
* Fixed check_required validator error message (#1550)
* Add test for check_required (#1550)
* Add CloudWatch Alarm TreatMissingData validator (#1536)
* Add WAFv2 resources, per Nov 25 2019 update (#1545)
* linking AWS::WAFv2 and OpenStack resource types in README (#1559)
* Strategy in AWS::EC2::PlacementGroup is not required (#1560)
* Combine JSON + YAML example (#1561)
* Add CACertificateIdentifier to DBInstance (#1557)
* fixing AWS::Serverless documentation link (#1562)
* adding new AWS::WAFv2::WebACLAssociation resource, per Jan 16 2020 update (#1567)
* adding SyncSource & SyncType props to AWS::SSM::ResourceDataSync, per Jan 16 2020 update (#1566)
* adding AWS::EC2::Instance HibernationOptions property, per Jan 16 2020 update (#1563)
* Add QueuedTimeoutInMinutes to CodeBuild Project (#1540)
* Add WeightedCapacity to AutoScaling::AutoScalingGroup LaunchTemplateOverrides (#1565)
* Use correct curl option for compressed downloads
* Update properties in AWS::Serverless::Api's Auth (#1568)
* Add new pinpoint properties, per Jan 23 2020 update (#1569)
* Add new AWS::RDS::DBCluster VALID_DB_ENGINE_MODES (#1573)
* ServiceDiscovery DnsConfig NamespaceId is not required (#1575)
* Add missing SecretTargetAttachment TargetTypes (#1578)
* Ignore If expression during validation on AutoScalingRollingUpdate min instances (#1577)
* adding Tags to Server, per Feb 6 2020 update
* AWS::KinesisAnalyticsV2::Application.RuntimeEnvironment VALID_RUNTIME_ENVIRONMENTS
* adding misc EC2 properties, per Feb 6 2020 update
* adding new Config resources, per 2020 Feb 13 update
* adding new Transfer properties, per 2020 Feb 13 update
* adding new ACMPCA resources, per Jan 23 2020 update (#1570)
* adding new AppConfig resource, per Jan 23 2020 update (#1571)
* Nodegroup tags type (#1576)
* adding XrayEnabled prop to GraphQLApi, per Feb 6 2020 update (#1579)
* adding AccountRecoverySetting prop to UserPool, per Feb 6 2020 update (#1580)
* adding Tags to Server, per Feb 6 2020 update (#1581)
* Merge pull request #1582 from axelpavageau/feature/20200206-ec2
* Merge pull request #1584 from cloudtools/PatMyron-patch-5
* Alphebetize some properties
* Merge pull request #1585 from axelpavageau/feature/20200213-transfer
* Merge pull request #1586 from axelpavageau/feature/20200213-config
* Adding new EC2 resources, per 2020 Feb 13 update (#1587)
* Adding new FMS resources, per 2020 Feb 13 update (#1588)
* adding misc Lakeformation properties, per Jan 16 2020 update (#1589)
* Adding new AWS::Neptune::DBCluster properties, per Feb 18 2020 update (#1594)
* fixing property according to the documentation's example (#1595)
* adding UsernameConfiguration prop to UserPool, per Feb 20 2020 update (#1596)
* Adding new ProjectFileSystemLocation property to CodeBuild::Project, per Feb 20 2020 update (#1597)

2.5.3 (2019*12*08)
------------------
* Switch to using the gzip version of the Resource Specification
* Amend RefreshTokenValidity to match Cognito changes. (#1498)
* Update placement object (#1501)
* Add hyperlinks to AWS resource types (#1499)
* Added missing CrawlerName field to Glue Action and Condition objects (#1500)
* Fix multiple mappings being overwritten (#1041)
* Cognito is missing UserPoolResourceServer (#1509)
* Add EnabledMfas to cognito UserPool Object. (#1507)
* Cognito EnabledMfa needs to be a list of strings (#1511)
* Make Python 3.8 support official (#1513)
* Added missing rds scaling configuration capacity (#1514)
* Add AllocationStrategy parameter for AWS::Batch::ComputeEnvironment ComputeResources (#1515)
* Add SelfManagedActiveDirectoryConfiguration property to fsx (#1516)
* Add logging capability to EKS Cloudwatch (#1512)
* Fix some flake8 breakage due to recent commits
* Output the resource specification version after downloading
* Add EventBus class in events script (#1518)
* Add new EC2 resources per 2019-10-03 update
* Add new cognito resources per 2019-10-03 update
* Add PlannedBudgetLimits to Budgets::Budget BudgetData
* Add AWS::Pinpoint
* Adding missing property for guardduty FindingPublishing (#1517)
* Support for API Gateway SecurityPolicy (#1521)
* Add AWS::GameLift
* Update AppStream per 2019-11-07 update
* Add AWS::CodeStarNotifications and AWS::MediaConvert
* Update AppMesh per 2019-11-04 update
* Add DynamoDBTargets and CatalogTargets to Glue::Crawler
* Update ApiGateway resources per 2019-11-31 changes
* Add Tags to CodePipeline CustomActionType and Pipeline
* Updates to Amplify per 2019-10-31 changes
* Update Events per 2019-11-31 changes
* Add InferenceAccelerator to ECS::TaskDefinitiion per 2019-10-31 change
* Add LogPublishingOptions to Elasticsearch::Domain
* Add Tags to SNS::Topic per 2019-11-31 changes
* Add WAF Action Type validator (#1524)
* Adding AWS::EKS::Nodegroup resource, per Nov 18 2019 update (#1529)
* Adding CpuOptions support for LaunchTemplateData (#1531)
* Update AppSync per 2019-11-21 changes
* Update SNS per 2019-11-21 changes
* Update OpsWorksCM per 2019-11-21 changes
* Update IAM per 2019-11-21 changes
* Update Glue per 2019-11-21 changes
* Update Elasticsearch per 2019-11-21 changes
* Update EC2 per 2019-11-21 changes
* Update Cognito per 2019-11-21 changes
* Update ApiGateway per 2019-11-21 changes
* Update RDS per 2019-11-21 changes
* Update ECS per 2019-11-21 changes
* Update CloudWatch per 2019-11-21 changes
* Update ECS per 2019-11-25 changes
* Update per 2019-11 changes
* Update CodePipeline per 2019-11-25 changes
* Add ProvisionedConcurrencyConfiguration for Lambda alias and version (#1533)
* Add AWS::EventSchemas
* Add AWS::AccessAnalyzer
* Add S3::AccessPoint per 2019-12-03 update
* Update StepFunctions per 2019-12-03 update
* Update ApiGatewayV2 per 2019-12-04 changes

2.5.2 (2019*09*29)
------------------
* Use double validator instead of a raw float for Double types (#1485)
* Add PythonVersion to Glue JobCommand (#1486)
* ImageId in EC2 LaunchTemplateData is no longer required (#1487)
* Add KmsKeyID prop to AWS::ElastiCache::ReplicationGroup, per 2019 Aug 30 update (#1488)
* Add threshold metric to CloudWatch::Alarm (#1489)
* Fix naming of parameters in FindInMap helper. (#1491)
* Add missing EnableNonSecurity property to SSM Rule (#1493)
* Add EnableCloudwatchLogsExports to Neptune::DBCluster
* Update AppMesh::Route properties per 2019-08-29 update
* Add Config::OrganizationConfigRule resource
* Add ZoneAwarenessConfig to Elasticsearch ElasticsearchClusterConfig
* Add AWS::QLDB
* Update RDS resources per 2019-08-29 update
* Travis CI: Add flake8 which is a superset of pycodestyle and pyflakes (#1470)
* Run flake8 via "make test" (#1470)
* Add SourceVersion to CodeBuild::Project (#1495)
* Add new Properties to SSM::Parameter (#1496)
* iam: Add Description field to Role (#1497)
* Add MaximumBatchingWindowInSeconds to Lambda::EventSourceMapping
* Update Events::Rule EcsParameters per 2019-08-29 changes
* Update ECS::TaskDefinition per 2019-08-29 changes
* Update EC2::Instance per 2019-08-29 changes
* Update DynamoDB::Table per 2019-08-29 changes
* Update ApplicationAutoScaling::ScalableTarget per 2019-08-29 changes
* Update DocDB::DBCluster per 2019-09-26 changes
* Update Glue per 2019-09-26 changes

2.5.1 (2019*08*25)
------------------
* Fix missing required field in CodeContent object (#1472)
* updated crawler tag attribute to match aws cloudformation doc (#1482)
* Change Tags to dict in Glue resources (#1482)
* Update gen script to understand "Json" Tags to be a dict
* Fixed a typo in the ClientBroker's value (#1480)
* Fix test output in MskCluster.template from issue #1480
* Update MaintenanceWindow Properties (#1476)
* Modified AdditionalAuthenticationProviders field in GraphQlApi to be a list (#1479)
* Add new properties to Glue::Job (#1484)
* Update missing properties in cognito (#1475)
* Add AWS::LakeFormation
* Update dms properties
* Add SageMaker::Workteam
* Add SplitTunnel to EC2::ClientVpnEndpoint
* Add Tags properties to some Greengrass resources
* Add ExcludeVerboseContent to AppSync LogConfig property type
* Add AWS::ManagedBlockchain
* Add Glue::MLTransform resource
* Add AWS::CodeStar
* Add LinuxParameters to Batch::ContainerProperties

2.5.0 (2019*07*28)
------------------
* Return real booleans in the output (#1409)

  Note: it was noted in #1136 that cfn-lint prefers real booleans. Since this
  may break existing scripts/updates, it was implemented via #1409 via an
  environment variable: TROPO_REAL_BOOL=true

  At some point troposphere likely will make this a warning and default to
  real booleans. Thanks for @michel-k and @ikben for implementing it.

* Add AWS::SecurityHub
* EC2: Update SpotOptions properties
* Merge branch 'master' into feature/rules
* Add Template.add_rule() function to be consistent with the Template API
* Write doc for add_rule()
* Adapt test case to the add_rule() interface
* Add duplicate name check in add_rule
* Add Tags to ECR Repository definition (#1444)
* Merge pull request #1412 from vrtdev/feature/rules
* EBSBlockDevice supports KmsKeyId (#1451)
* Add Medialive resources (#1447)
* Fix RecoveryPointTags/BackupVaultTags type for AWS Backup resources (#1448)
* Add Code property to Codecommit (#1454)
* Add support for LicenseSpecification for LaunchTemplateData (#1458)
* Add AWS::MediaLive to README
* Tweak to allow "make test" work with the real boolean change (#1409)
* Prefer awacs.aws.PolicyDocument over awacs.aws.Policy (#1338)
* Add EFS FileSystem LifecyclePolicies (#1456)
* Fix Transfer::User SshPublicKeys type (#1459)
* Fix TemporaryPasswordValidityDays type (#1460)
* Add Cloudwatch AnomalyDetector resource (#1461)
* Update ASK to the latest AWS documentation (#1467)
* Adding AllowMajorVersionUpgrade to DMS Replication Instance (#1464)
* Change ElastiCache ReplicaAvailabilityZones from string to string list (#1468)
* Add AmazonMQ::Broker EncryptionOptions property
* Update AWS::Amplify resources
* Add AWS::IoTEvents
* Add Tags to AWS::CodeCommit::Repository
* Add EmailSendingAccount to Cognito::UserPool EmailConfiguration

2.4.9 (2019*06*26)
------------------
* add tag to role (#1441)
* Fix regression in EC2::VPNConnection - add list back to Tags (#1442)

2.4.8 (2019*06*23)
------------------
* [iot1click] resource_type should be a string, not tuple (#1402)
* Fix Parameters on AWS::Batch::JobDefinition (#1404)
* Add new wafregional resources (#1406)
* Add AppMesh::VirtualRouter (#1410)
* Add InterfaceType to EC2 LaunchTemplate (#1405)
* Adding AWS::Transfer resources, per 2019 May 23 update (#1407)
* Adding AWS::PinpointEmail, per 2019 May 23 update (#1408)
* Add missing LOCAL caching option (#1413)
* Allow for AWSHelperFn objects in Tags (#1403)
* Fix bug where FilterGroups were required, when technically they are not (#1424)
* Adding AWS::Backup resources from May 23, 2019 update (#1419)
* adding missing X-ray activation property for AWS::ApiGateway::Stage (#1420)
* Change add_description to set_description in all examples (#1425)
* Add support for httpHeaderConfig (#1426)
* Add Config attributes to ELBV2 Condition (#1426)
* Update ECS resources from June 13, 2019 update (#1430)
* Add ClientVPN resources (#1431)
* Change HeartbeatTimeout type to integer (#1415) (#1432)
* Add transit gateway ID to Route (#1433)
* Add Sagemaker::CodeRepository (#1422)
* Adding SageMaker NotebookInstance properties (#1421)
* Update ElasticLoadBalancingV2 ListenerRule (#1427)
* Update DLM rule interval values (#1333) (#1437)
* Add resources for Amazon MSK, from June 13, 2019 update (#1436)
* Add HostRecovery property to EC2::Host
* Add SecondarySourceVersions to CodeBuild::Project
* Add ObjectLock* properties to S3::Bucket
* Add Ec2SubnetIds property to EMR JobFlowInstancesConfig
* Add AWS::Amplify
* Adds 'ErrorOutputPrefix' to *S3DestinationConfiguration (#1439)
* Add ServiceCatalog::StackSetConstraint and update CFProvisionedProduct
* Add IdleDisconnectTimeoutInSeconds to AppStream::Fleet
* Add Config::RemediationConfiguration resource
* Add AppMesh AwsCloudMapServiceDiscovery and reformat for autogen
* DLM: add Parameters and PolicyType properties to PolicyDetails
* IoTAnalytics: add ContentDeliveryRules and VersioningConfiguration to Dataset
* KinesisFirehose: updates to ExtendedS3DestinationConfiguration

2.4.7 (2019*05*18)
------------------
* Add authenticate-cognito and authenticate-oidc to elb v2 Action's "type" validator (#1352)
* Update the instance types in constants. (#1353)
* Add missing Termination Policies (#1354)
* Add Tags to various AppStream objects, per 2019 March 19 update (#1355)
* Add new AWS::AppMesh resources, per 2019 March 28 update (#1356)
* Add ServiceCatalog::ResourceUpdateConstraint
* Add ResourceRequirements property to Batch::JobDefinition
* Add an improved troposphere code generator for use with AWS spec files
* Add a Makefile helper to download the spec file
* Fix a pep8 issue introduced with pycodestyle 2.5.0
* Add constants for missing rds instance types (#1365)
* EngineAttributes should take list (#1363)
* Added support for lambda in TargetGroup with additional validation (#1376)
* Fix the scripts for Python3 (#1364)
* Add #! header and print_function import
* Add scripts directory to tests
* Fix pycodestyle issues with scripts
* Add HealthCheckEnabled to ElasticLoadBalancingV2::TargetGroup
* Fixed: Codebuild Webhook Filters are to be a list of list of WebhookFilter (#1372)
* Use enumeration in codebuild FilterGroup validate and add some tests
* Add AWS::EC2::CapacityReservation resource (#1379)
* Add AWS::Greengrass (#1384)
* Add Events::EventBusPolicy (#1386)
* Add Python 3.7 to travis testing (#1302)
* Added ECS ProxyConfiguration, DependsOn,  StartTimeout and StopTimeout parameters (#1382)
* Username property in DMS::Endpoint class should not be required (#1387)
* Fix MethodSettings on AWS::Serverless::Api (#1391)
* Adds TmpFs prop to LinuxParameters (#1392)
* Add SharedMemorySize property to ECS LinuxParameters (#1392)
* Make DefinitionString and DefinitionBody mutually exclusive, but allow no definition (#1390)
* Add T3a, M/R5ad, and I3en instances to constants (#1393)
* Fixed issue #1394 wrong appmesh Listener property and #1396 dependson should be a type list and #1397 proxy props should be list (#1395)
* Add ApiGatewayV2 ApiMapping and DomainName resources
* Added missing container name propery (#1398)
* Update region/az information (#1399)
* Add missing Role property for serverless DeploymentPreference (#1400)
* Add DisableTemplateValidation to ServiceCatalog ProvisioningArtifactProperties
* Add AWS::MediaStore
* Add multiple changes to AWS::Glue
* Add AppSync GraphQLApi changes
* Add TemporaryPasswordValidityDays to Cognito PasswordPolicy

2.4.6 (2019*03*20)
------------------
* Discourage usage of Python 3.4 (#1326)
* Remove validation for ElastiCache::ReplicationGroup some properties (#1063)
* Add auth configs for ElasticLoadBalancingV2::ListenerRule actions
* Add new RDS DBCluster and DBInstance properties (#1329)
* Add new Elasticsearch Domain property (#1330)
* Add new ApiGateway Apikey property (#1331)
* Add new Codebuild ProjectCache property (#1332)
* Add new AWS::RAM and AWS::RoboMaker resources
* Add psuedo-parameter Ref for AWS::Partition (#1334)
* Add SageMaker::NotebookInstance VolumeSizeInGB property
* Add missing properties in SSM::PatchBaseline (#1339)
* Add Tags to StepFunctions objects, per 2019 March 07 update (#1340)
* Update valid values for emr.StepConfig ActionOnFailure (#1350)
* Add RootAccess prop to AWS::SageMaker::NotebookInstance, per 2019 March 14 update (#1342)
* Add prop to AWS::OpsWorksCM::Server per 2019 March 14 update (#1343)
* Add new AWS::CodeBuild::Project props, per 2019 March 14 update (#1344)
* Fix EC2 SpotFleet LoadBalancersConfig TargetGroupConfig (#1346)
* Add URLSuffix Ref (#1347)
* CodeBuild::Project Name is not required (#1348)

2.4.5 (2019*02*19)
------------------

* Add "pip install" step for source dist file before a release (#1318)
* Exclude OpenStack modules within the template generator (#1319)
* Add AWS::CodeBuild::Project subproperties, per Feb 2019 14 update (#1321)
* Add AWS::FSx::FileSystem resource, per Feb 2019 15 update (#1322)
* Add KinesisAnalyticsV2 resources, per 2019 Feb 15 update (#1323)
* Remove awacs as a hard dependency; ensure awacs>=0.8 otherwise (#1325)
* Add FSx and KinesisAnalyticsV2 modules to the documentation

2.4.4 (2019*02*13)
------------------

* Include requirements.txt in release tarball

2.4.3 (2019*02*13)
------------------

* Fix Glue StorageDescriptor NumberOfBuckets spelling (#1310)
* ServiceDiscovery::Service DNSConfig is no longer required
* Sphinx docs (#1311)
* Add autogeneration of troposphere index files
* Fix  ApiGateway AccessLogSetting prop spelling (#1316)
* Docs update (#1314)
* Add AWS::ApiGatewayV2 Resources (#1312)
* Updates for new resources being added

2.4.2 (2019*02*02)
------------------

* Add AWS::DocDB
* Add UpdateReplacePolicy attribute
* Use a dict instead of the Tags object for the Tags property on the dax resource (#1045) (#1046)
* Add better method names for Troposphere objects. (#1169)
* Update integer_list_item to always cast value to an int for comparison (#1192)
* Remove name parameter from json_checker (#1260)
* Remove duplicate VpcConfig/DomainJoinInfo classes from AppStream (#1285)
* Add 'Kind' property to AWS::AppSync::Resolver (#1287)
* Add missing region information. (#1288)
* Fix tag sorting on py3 (#1289)
* Updated autoscalingplans to match cloudformation doco (#1291)
* ResourceGroupArn is no longer mandatory for AWS::Inspector::AssessmentTarget (#1292)
* Fix creating RotationSchedule for SecretsManager (#1293)
* Add missing serverless properties (Fixes #1294)
* Make DataSourceName non*mandatory in appsync resolvers (#1296)
* Add new properties to AWS::CodeBuild::Project, per 2019 Jan 24 update (#1297)
* Add new AWS::OpsWorksCM::Server resource, per 2019 Jan 24 update (#1298)
* Add AWS::Serverless::LayerVersion (#1305)
* Fix for AWS Lambda reserved environment variables (#1306)
* Add SqsParameters support to Rule Target (#1307)
* Add DestinationPrefixListId to EC2 SecurityGroupRule (#1309)
* Fix for pyflakes 2.1.0

2.4.1 (2019*01*09)
------------------

* Add a S3OriginConfig object to distinguish between Distribution and StreamingDistribution properties (#1273)
* Add SSM Example for patch baselines and filter groups (#1274)
* Add better validation for AWS::CloudWatch::Alarm properties (#1276)
* Allow empty To/From port ranges for SG's for certain IP protocols (#1277)
* Add additional properties to AWS::Serverless::Api (#1278)
* Fixes DynamoDB validator error (#1280)

2.4.0 (2019*01*06)
------------------

* Setup tox (#1187)
* Set line length for Python files in EditorConfig (#1188)
* Fix EC2 SpotFleet properties #1195 (#1198)
* Add MultiValueAnswer property for AWS::Route53::RecordSet (#1199)
* adding RDS properties, per Nov 9 2018 update https://docs.aws.amazon.… (#1201)
* Add Secrets Managers resources, per Nov 9 2018 update (#1202)
* Add DLM support, per Nov 12 2018 update (#1203)
* Adds support for Permissions Boundaries on AWS::IAM::Role and AWS::IAM::User (#1205)
* Add support for multi*region action in CodePipeline (#1207)
* Added support for Aurora BacktrackWindow. (#1210)
* Add AWS::AppStream resources
* Add Tags and WorkspaceProperties to WorkSpaces::Workspace
* Add support for AWS::AutoScalingPlans::ScalingPlan (#1197)
* adding KmsMasterKeyId to Topics, per Nov 19 2018 update
* adding PublicAccessBlockConfiguration to s3 buckets, per Nov 19 2018 update
* Validate Lambda environment variable names (#1186)
* Fix DockerVolumeConfiguration Labels and DriverOpts definition (#1194)
* Setup to_dict for Tags AWSHelper (#1189)
* Delete CodeDeploy EC2TagSetList class as it is just a property of EC2TagSet (#1212)
* Fix bugs and add missing properties in sagemaker (#1214)
* adding DeletionProtection property to RDS, per Nov 19 2018 update (#1215)
* adding PublicAccessBlockConfiguration to s3 buckets, per Nov 19 2018 update (#1216)
* Merge pull request #1217 from axelpavageau/feature/sns*20181119*update
* Add volume encryption, per Nov 19 2018 update (#1218)
* Add PublicIpv4Pool property to EIPs, per Nov 19 2018 update (#1219)
* Add new Lambda resources and props, per Nov 29 2018 update (#1242)
* Add MixedInstancesPolicy property to autoscaling groups, per Nov 19 2018 update. (#1220)
* Add tags to API Gateway resources, per Nov 19 2018 update (#1221)
* Add various EMR properties, per Nov 19 2018 update (#1222)
* Add new kinesis resource, per Nov 20 2018 update (#1224)
* Make Lambda::LayerVersion CompatibleRuntimes a list of strings
* Add new route53 resources, per Nov 20 2018 update (#1223)
* Add new EC2Fleet resource, per Nov 20 2018 update (#1225)
* Add new appsync FunctionConfiguration resource & properties, per Nov 20 2018 update (#1226)
* Update AWS::CloudWatch::Alarm, per Nov 20 2018 update (#1227)
* CloudWatch MetricDataQuery Id is required
* Add DatapointsToAlarm to AWS::CloudWatch::Alarm (#1244)
* Alphabetize DatapointsToAlarm in CloudWatch
* Update Autoscalingplans properties, per Nov 20 2018 update (#1228)
* Add Iot1click resources (#1229)
* Add new Transit Gateway resources, per Nov 26 2018 release (#1232)
* Fix online merge issue
* Fixes EC2 SpotFleet LoadBalancersConfig structure (#1233)
* Sets InstanceType in EC2 LaunchTemplateData to not required. (#1234)
* Add new HttpNamespace resource & various servicediscovery props, per Nov 28 2018 update (#1237)
* Add new ec2 properties, per Nov 28 2018 update (#1238)
* EC2 Instance LicenseConfigurationArn is required
* Add on*demand billing for DynamoDB tables (#1243)
* Correct RoleArn case for OrganizationAggregationSource (#1247)
* Add various codebuild properties, per Dec 6 2018 update (#1249)
* Add support for DeploymentPreference to AWS::Serverless::Function (#1251)
* Update typo on EnableCloudwatchLogsExports (#1253)
* Add new AmazonMQ resource, per Dec 13 2018 update (#1254)
* Add Alexa Skill resource, per Nov 20 2018 update (#1230)
* Add new IoTAnalytics resources, per Dec 13 2018 update (#1255)
* Extend Action to support Redirect and FixedResponse for AWS::ElasticLoadBalancingV2::ListenerRule (#1140)
* Add support for extensible resource definitions in template generator (#1154)
* Updates CloudFront with missing parameters and validators (#1235)
* Added support for AWS Batch PlacementGroup & LaunchTemplate (#1262)
* Add DeleteAutomatedBackups to RDS DBInstance (#1263)
* Add missing KMS key properties (#1265)
* Fix pep errors due to online merge
* Fix EC2Fleet class definition to match functional correctness of CloudFormation (#1266)
* Add Tags property to AWS::AmazonMQ::Broker, per 2019 Jan 3 update (#1267)
* Add Containers property to AWS::SageMaker::Model per 2019 Jan 3 update (#1268)
* Add AWS::Route53Resolver::ResolverRuleAssociation resource, per 2019 Jan 3 update (#1269)
* Fix nested 'Name' sections in Output import (#1270)
* README.rst: Use SVG build status badge (#1271)
* Add test for nested Name in TemplateGenerator fixed via #1270

2.3.4 (2018*11*04)
------------------

* Add CloudFormation::Macro
* Instance ImageId is no longer required, specifically if using Launch Templates; updated tests (#1137)
* Fix amazonmq missing properties (#1143)
* Update AmazonMQ::Broker properties to use [basestring] instead of list
* Update the OnPremisesInstanceTagFilters parameter for AWS::CodeDeploy::DeploymentGroup (#1145)
* Update constants.py (#1147)
* Fix AutoScalingRollingUpdate validation failure (#1148)
* Adding UseOnlineResharding policy per 09/20/2018 update (#1149)
* Add SchedulingStrategy as a prop to ecs.Service (#1150)
* Added ConnectionId and ConnectionType to API GW method integration (#1153)
* Use dict as aws expects for ApiGateway::RestApi Parameters (#1156)
* Add support for AWS*interface metadata (#1171)
* Add new properties to ServiceRegistry (#1172)
* [#1167] Add support for DockerVolumeConfiguration in AWS::ECS::TaskDefinition (#1168)
* Add missing Codebuild source types (#1160)
* [#1155] Aurora serverless support (#1166)
* Missing RepositoryCredentials attribute for ContainerDefinition object (#1165)
* Update for new S3 destination option in flow logs (#1158)
* updates rds vpc example and closes #985 (#1157)
* Update apigateway as of 09/20/18 (#1173)
* Add missing APIGateway properties
* Update codebuild as of 09/20/18 (#1175)
* Update ec2 as of 09/20/18 (#1177)
* Additional codebuild source types (#1178)
* Use basestring to allow percentage definition in MaintenanceWindowTask (#1151)
* Fix issues with CanaraySettings properties (#1181)
* 9/20/2018 update * NodeGroupId for Elasticache (#1182)
* Update codedeploy as of 09/20/18 (#1176)
* Add LambdaPermission in Example CloudWatchEventsSample.py (#1141)
* improve double validation and fix some property datatypes (#1179)
* Fix #1174 TemplateGenerator fail to parse template Fn::Sub with variable (#1180)

2.3.3 (2018*09*05)
------------------

* Revert schedule expression validation (#1114)

2.3.2 (2018*09*04)
------------------

* Auto add Parameter and Output to template when specified (#1018)
* Changed policy to AmazonDynamoDBFullAccess for delete and put (#1106)
* Fix CPUCredits casing and implement LaunchTemplateCreditSpecification class (#1100)
* Add UsernameAttributes to Cognito (#1104)
* Add SQS Event to serverless.py (#1103)
* Add support for Windows containers in CodeBuild (#1097)
* Generate class stubs necessary for autocompletion (#1079)
* Add AWS::IAM::ServiceLinkedRole (#1110)
* Made S3 Prefix in Firehose optional (#1102)
* Prefix is still required in ExtendedS3DestinationConfiguration
* SimpleTable has more attributes (#1108)
* Alphabetize properties in servlerless::SimpleTable
* AccountAggregationSources must be a list (#1111)
* Schedule expression validation (#1114)
* Add EndpointIdnetifier property to AWS::DMS::Endpoint object (#1117)
* Add get_or_add parameter method (#1118)
* Added HealthCheckCustomConfig to ServiceDiscovery Service (#1120)
* Tags support for SQS queues (#1121)
* VPCPeeringConnection PeerRegion (#1123)
* Add FilterPolicy as a property of SubscriptionResource (#1125)
* Add missing properties to SNS::Subscription
* Add ThroughputMode and ProvisionedThroughputInMibps to EFS (#1124) (#1126)
* Add AWS::EC2::VPCEndpointServicePermissions (#1130)
* AMAZON_LINUX_2 is now supported by SSM (#1133)
* [codebuild] Source * use value comparison instead of identity (#1134)
* InvitationId in GuardDuty::Master is now optional
* Fix missing boolean import in sns
* Add CodePipeline::Webhook resource
* Add ReportBuildStatus to CodeBuild Source property
* Add HttpConfig to AppSync::DataSource
* Add FieldLevelEncryptionId to CacheBehavior properties
* Add Timeout to Batch::JobDefinition
* Add EncryptionDisabled and OverrideArtifactName to CodeBuild Artifacts
* Add SSESpecification to DAX::Cluster
* Add KerberosAttributes to EMR::Cluster
* Add ValidationMethod to CertificateManager::Certificate
* Add Classifiers and Configuration to Glue resources
* Add SecondaryArtifacts and SecondarySources to CodeBuild::Project
* Add Logs to AmazonMQ::Broker

2.3.1 (2018*07*01)
------------------

* Add support for AWS::Neptune
* Add support for AWS::EKS
* Add support for AWS::AmazonMQ
* Add support for AWS::SageMaker
* Fix use of to_yaml long_form parameter (#1055)
* Adding CENTOS to validators.operating_system (#1058)
* Update constants with additional EC2 instances (#1059)
* Fix casing of CreditSpecification CpuCredits (#1068)
* Add 'Name' property for AWS::Serverless::Api (#1070)
* Add equality methods to Template (#1072)
* AWS PrivateLink support (#1084)
* Add return value to template.add_condition() (#1087)
* Add tests for to_yaml parameters
* Use endpoint_type for vpc_endpoint_type param instead of type
* Add resource EC2::VPCEndpointConnectionNotification
* Add resource SSM::ResourceDataSync

2.3.0 (2018*05*26)
------------------

* Allow Refs to be hashable using their data (#1053)
* Add AWS::Budgets
* Add new AWS::ServiceCatalog resources
* Add Policy to ApiGateway::RestApi
* Add ServiceLinkedRoleARN to AutoScaling::AutoScalingGroup
* Add LaunchConfigurationName to AutoScaling::LaunchConfiguration
* Add Edition to DirectoryService::MicrosoftAD
* Add PointInTimeRecoverySpecification to DynamoDB::Table
* Add ServiceRegistries to ECS::Service
* Add HealthCheck to ECS::TaskDefinition ContainerDefinition
* Add EncryptionAtRestOptions to Elasticsearch::Domain
* Add MaxSessionDuration ti IAM::Role
* Add SplunkDestinationConfiguration to KinesisFirehose::DeliveryStream
* StartingPosition is no longer required in Lambda::EventSourceMapping
* Add DefaultValue to Logs::MetricFilter MetricTransformation
* Add OutputLocation to SSM::Association
* Add AutoScaling and EC2  LaunchTemplate support (#1038)
* Add LaunchTemplate to EC2::Instance
* Adding ECS Container Healthchecks tests (#1024)
* Rename ActionTypeID to ActionTypeId in CodePipeline

2.2.2 (2018*05*23)
------------------

* Allow up to 50:1 ratio for iops and allocated storage
* Correct Spot Fleet TagSpecifications (#1010)
* Change GetCidr to Cidr (Fixes #1013)
* Add missing OpsWorks::Instance properties (Fixes #1014)
* Adding SUSE to list of operating systems for SSM (#1015)
* Updates for latest pycodestyle warnings
* Add AWS::AppSync
* Add AWS::ServiceCatalog
* Special case Tags support in gen.py
* Add constants for EC2 C5 instance types (#1025)
* Update guardduty.py (#1037)
* Add OpenIdConnectConfig to AppSync::GraphQLApi
* Update AWS Config features (updates #1022)
* Updated appsync apikey expires to be an int. (#1040)
* Fix AutoScalingRole in EMR: Fixes #984 (#1036)
* Rename SES Template to EmailTemplate (#1047)
* Add GuardDuty::Filter
* Remove python 3.3 support since it's EOL (#1049)
* Corrected the description of NatGateway (#1005)
* Update deprecated modules (#1007)
* Updared CodeBuild Source Options (#1017)
* Allow Ref's to test equality against their data (#1048)
* Update to cfn*flip 1.0.2 (#1003)
* Eliminate infinite loop when pickle loads BaseAWSObject and objects derived from it. (#1016)
* Allow multiple NoValue properties in mutually_exclusive (#1050)

2.2.1 (2018*03*10)
------------------

* type is not required for EnvironmentVariable (#975)
* Properly handle list objects used with DependsOn (Fixes #982)
* Explicitly convert allocated_storage to integer before using it in comparisons (#983)
* Allow CreationPolicy override of props on WaitCondition (#988)
* "JobDefinitionName" property in JobDefinition class is not required (#995)
* ApiGateway::DomainName CertificateArn fix (#996)
* Tags support for SSM documents #999 (#1000)
* Add SSESpecification to DynamoDB::Table (#981)
* Add GitCloneDepth and InsecureSsl to CodeBuild Source
* Add Trippers property to CodeBuild::Project
* Add aurora*mysql to list of valid RDS engines
* Batch ContainerProperties is required
* Add Regions to Route53 HealthCheckConfiguration
* Add ClusterIdentifier to Redshift::Cluster
* Add DBClusterIdentifier to RDS::DBCluster
* Add TagSpecification to EC2::SpotFleet LaunchSpecifcations
* Add DisableScaleIn to ApplicationAutoScaling
* Add ApiKeySourceType and MinimumCompressionSize to ApiGateway::RestApi
* Add AutoScalingGroupName to AutoScaling::AutoScalingGroup
* Add AWS::ApiGateway::VpcLink
* Add AWS::GuardDuty::Master and AWS::GuardDuty::Member
* Add AWS::SES
* Add GetCidr function for Fn::GetCidr

2.2.0 (2018*01*29)
------------------

* Add AWS::Inspector
* Add AWS::ServiceDiscovery
* Add InputProcessingConfiguration to KinesisAnalytics::Application
* EndpointConfiguration in ApiGateway::DomainName is not required
* Allow setting Subnets and SubnetMappings properties on ELBv2 LoadBalancers (#934)
* increase lambda memory limit to support up to 3008 MB (#936)
* Stop validation if CodeBuild Source Type is a Ref (#940)
* Added support for AutoPublishAlias to AWS::Serverless::Function as specified https://github.com/awslabs/serverless*application*model/blob/master/versions/2016*10*31.md (#941)
* Add resource_type value and unit tests for guardduty AWSObject's (#945)
* Added elasticsearch instance types for m4, c4 and r4 generations (#948)
* Correct type in API Gateway GatewayResponse type (#950)
* Fixes the lifecyclepolicy problem reported at Issue #953 (#954)
* Add constants for EC2 M5 instance types (#955)
* Adding support for Block Device Mapping V2 (#960)
* Add support for Policy Document in SAM template. (#961)
* Stab at documenting Troposphere basics (#963)
* Adding HealthCheckGracePeriodSeconds into ECS Service (#966)
* Add AllowedPattern to Parameter (#968)
* Add long form parameter to to_yaml (#972)
* Use S3.Filter for the serverless S3Event Filter property
* Remove erroneous print in tests/test_serverless.py
* Add FunctionForPackaging class to serverless
* Add AssociationName to AWS::SSM::Association
* Update S3::Bucket with 20180123 property changes
* Add DBSubnetGroupName to AWS::RDS::DBSubnetGroup
* Add ReservedConcurrentExecutions to AWS:Lambda:Function
* Add StreamEncryption to AWS::Kinesis::Stream
* Add LambdaOutput to KinesisAnalytics ApplicationOutput property
* Update required fields in IoT TopicRule DynamoDBAction
* Add validator for InstanceTenancy in EC2::VPC
* Add CreditSpecification and ElasticGpuSpecifications to EC2::Instance

2.1.2 (2017*12*03)
------------------

* In SpotFleet::SpotFleetRequestConfigData SpotPrice is optional
* Add RoutingConfig to AWS::Lambda::Alias
* Update AWS::CodeDeploy
* Add CodeDeployLambdaAliasUpdate to UpdatePolicy
* Add AWS::GuardDuty
* Add AWS::Cloud9
* Add initial python resource spec generator
* Update AWS::CodeBuild::Project to 20171201 changes
* Change AWS::Batch::ComputeResources.Tags type to dict (#867)
* Update README for YAML template (#925)
* Typo fix in examples/ElastiCacheRedis.py (#926)
* Adds Fargate support to ECS types (#929)
* Fix SSM NotificationConfig validator type (#930)
* Fix SQS::Queue validation in the case of no QueueName specified (#931)

2.1.1 (2017*11*26)
------------------

* Add support for VPCOptions in ElasticSearch (#862)
* Add Description property for security group ingress and egress (#910)
* Add QueryLoggingConfig to Route53::HostedZone
* Add SourceRegion to RDS::DBInstance
* Add RootVolumeSize and caleDownBehavior to EMR::Cluster
* Add new properties to ElastiCache::ReplicationGroup
* Add LinuxParameters to ECS::TaskDefinition ContainerDefinitions
* Add LifecyclePolicy to ECR::Repository
* Add ScheduledActions to ApplicationAutoScaling::ScalableTarget
* Add new properties into ApiGateway

2.1.0 (2017*11*19)
------------------

* Output yaml (to_yaml) using cfn_flip (Fixes #567)
* Allow AWSHelperFn for CodeCommit Trigger Event(s) (#869)
* Adding the AWS::Glue resources (#872)
* Use a list for Serverless::Function Tags (#873)
* Support ProcessingConfiguration for Elasticsearch and Redshift (#876)
* Fixes incorrect class definition. (#877)
* Add TargetGroupInfo to DeploymentGroup #884 (#895)
* Reverting #810 as AWS has changed the casing again (#896)
* Add EMR Cluster MasterInstanceFleet and CoreInstanceFleet properties (#897)
* Add EMR Cluster CustomAmiId (#888) (#898)
* Add SecurityGroupRule Description property (#885) (#899)
* Add support for tags in AWS::KMS::Key. (#900)
* Adding OriginReadTimeout aka OriginResponseTimeout to cloudfront origin settings (#901)
* Added property for OriginKeepaliveTimeout
* Add CloudFrontOriginAccessIdentity type (#903)
* Added support for VpnTunnelOptionsSpecifications (#904)
* Allow ref on Parameter (#905)
* Adds Tags to Cloudfront Distribution (#906)
* CloudFront: add IPV6Enabled property for DistributionConfig (#908)
* Add OptionVersion to RDS:OptionConfigurations
* Add Tags to OpsWorks Layer and Stack
* Add LifecycleHookSpecification in AutoScalingGroup
* Add AmazonSideAsn to EC2::VPNGateway
* Add StateMachineName to StepFunctions::StateMachine
* Change KMS::Key to accept a standard Tags
* Add LambdaFunctionAssociations to CloudFront CacheBehaviors
* Add ResourceName to elasticbeanstalk OptionSettings
* Add AnalyticsConfigurations and InventoryConfigurations to S3::Bucket
* Add RequestValidatorId and OperationName to ApiGateway::Method
* Add deprecation warning for StageName in ApiGateway StageDescription
* Add AWS::CloudFront::StreamingDistribution

2.0.2 (2017*10*23)
------------------

* Set EC2 BlockDeviceMapping NoDevice property to type dict (#866)

2.0.1 (2017*10*21)
------------------

* Allow s3.Bucket AccessControl to be an AWSHelperFn
* Add AWS::ElasticLoadBalancingV2::ListenerCertificate
* Add serverless FunctionName and change how Tags are implemented
* Make AdjustmentType an optional property of ScalingPolicy as it is not used/supported for target (#849)
* Add maintenance window for SSM (#851)
* Add Tags, Tracing, KmsKeyArn, DLQ to serverless(SAM) (#853)
* Add new AWS::SSM resources (#854)
* EC2 NoDevice should be type boolean not dict (#858)
* Fixes RecordColumns cardinality for InputSchema and ReferenceSchema (#859)
* Make AWS::Batch::JobQueue::JobQueueName optional (#860)
* Fixes ApplicationOutput/Output cardinality (#863)

2.0.0 (2017*10*07)
------------------

* Note: the s3.Bucket change (#844) *may* cause a breaking change for non*named arguments.
* Add DefinitionBody to serverless API (#822)
* Adding kinesis stream source to firehose (#823)
* Add `Event::Rule::Target::EcsParameters` (#824)
* Add S3 Transfer Acceleration to AWS::S3::Bucket (#833)
* Add AvailabilityZone property to TargetDescription (#834)
* Add Tags to NATGateway (#835)
* Add ResourceLifecycleConfig to ElasticBeanstalk (#836)
* Add AWS::Athena::NamedQuery (#837)
* Added platformArn to Environment and ConfigurationTemplate (#839)
* Events target (fixes #830) (#840)
* Refactor s3.Bucket to remove custom __init__() and add tests (#844)
* Be more explicit on the use of the Tags object for Tags (#845)

1.9.6 (2017*09*24)
------------------

* Added missing EU_WEST_2 constants. (#776)
* Override object validation (#780)
* Update PyPI Information (#785)
* Adding IPv6 changes to AWS::EC2::Subnet (#786)
* NetworkACL Protocl Constants (#787)
* Add support for EFS encryption (#789)
* Add AWS::ApiGateway::GatewayResponse (#790)
* Add support for aurora*postgresql as a valid DB engine (#791)
* adding sqs server side encryption (#793)
* Support new code deploy options (#794)
* Add AWS Batch Support (#796)
* VPC expansion support (#797)
* Add NLB Functionality (#806)
* Fix typos in examples/DynamoDB_Table.py (#807)
* Revert "Accept Join type as parameter default value as it returns a string (#752)" (#808)
* Change Cognito UserPool SchemaAttribute required value to boolean (#809)
* Updating case of 'AssignIPv6AddressOnCreation' (#810)
* Fix spelling error  to  in RedshiftVPC example (#811)
* EFS example: SecurityGroupRule can't be referred to as a Ref (#813)
* Update README.rst with current supported resources (#814)
* Add CloudTrail EventSelectors (#815)
* Add DAX support (#818)
* Add KinesisAnalytics support (#819)
* Add new ApiGateway resources (#820)
* Add autoscaling example for http requests that closes #630 (#821)
* Add new S3 Lifecycle Rule properties
* Add IoT DynamoDBv2Action and update DynamoDBAction properties
* Add EventSourceToken to Lambda::Permission
* Add new pseudo parameters
* Add DocumentationVersion to AWS::ApiGateway::Stage
* Add S3 Bucket MetricsConfiguration and fix TagFilter spelling
* Add TargetType to ELBv2::TargetGroup
* Add TargetTrackingConfiguration to AutoScaling::ScalingPolicy
* Add ReplaceUnhealthyInstances and Type to SpotFleetRequestConfigData
* Add ExtendedS3DestinationConfiguration to firehose DeliveryStream
* Add AWS::EC2::NetworkInterfacePermission

1.9.5 (2017*07*26)
------------------

* Add support for latest Cloudwatch alarms properties (#694)
* Raise ValueError for Outputs and Mappings * Fix Issue #732 (#733)
* Add AWS::EMR::SecurityConfiguration support (#738)
* Create CODE_OF_CONDUCT.md (#740)
* Added UsagePlans to API Gateway example (#741)
* EMR AutoScaling Complex Validation and Introduction of an ignore validator type (#743)
* Add PrivilegedMode option to CodeBuild Environments (#744)
* EFS DependsOn Ref to object fix (#746)
* README * add syntax highlighting (#747)
* Make handling of DependsOn more pythonic (#748)
* Accept Join type as parameter default value as it returns a string (#752)
* AWS SAM support (#754)
* Fixed UsagePlan example to proper Ref (#755)
* Fix cognito StringAttributeConstraints property names (Fixes #756)
* Add 'SourceAuth' property to CodeBuild Source (#758)
* Make it easier to get at hidden attributes (Fixes #760)
* Size/IOPS should be positive_integers (#761)
* Check that FIFO Queues end with .fifo (#757)
* Add AWS::CloudWatch::Dashboard (Fixes #763)
* Ulimit's HardLimit and SoftLimit validator change (#764)
* Adding EgressOnlyInternetGateway to EC2::Route (#765)
* Allow passing in a dict into DashboardBody (#767)
* Handle SQS QueueName using an AWSHelperFn (Fixes #773)
* LifecycleHook NotificationTargetARN and RoleARN are now optional
* Remove RoleArn from Events::Rule and add to Target property
* Add TracingConfig property to AWS::Lambda::Function
* Add Tags to some RedShift resources
* Add AWS::ApiGateway::DomainName
* Add AWS::EC2::EgressOnlyInternetGateway
* Add AWS::EMR::InstanceFleetConfig
* Add BinaryMediaTypes to ApiGateway::RestApi
* Add TargetTrackingScalingPolicyConfiguration
* Add TrailName to CloudTrail::Trail
* Add AlarmConfiguration and TriggerConfigurations
* Add Tags and TimeToLiveSpecification to DynamoDB::Table
* Add RetentionPeriodHours to Kinesis::Stream
* Add ReplicationSourceIdentifier to RDS::DBCluster
* Add LoggingProperties to Redshift::Cluster
* Add AWS Database Migration Service (DMS) support
* Add test target to Makefile
* Make it easier to download the latest CF resource spec
* Added and reverted out of this release:
    * Fix pycodestyle issue in tests/test_yaml.py
    * Output yaml (to_yaml) using cfn_flip (Fixes #567)
    * Special case If during parameter checking (Fixes #772)
    * Raise TypeError when a scaler AWSHelperFn is used in a list context (#751)

1.9.4 (2017*06*04)
------------------

* Fix typo in S3_Bucket.py example (#696)
* Added .Ref & .GetAtt helper methods (#697)
* Add Pseudo Parameter Ref objects (#698)
* Fix NamespaceType typo in codebuild::Artifacts() (fixes #701)
* Add IpAddressType property to elbv2. (#703)
* Add new AWS::Lambda::Function Tags support (#705)
* Added ECS PlacementConstraints, PlacementStrategy, and ServiceName (#706)
* Add missing CidrIpv6 property to securityrule. (#710)
* Add missing properties to various objects in ec2.py (#711)
* logs.LogGroup#RetentionInDays is strictly defined list (#712)
* Add ManagedPolicyName to AWS::IAM::ManagedPolicy (Fixes #714)
* Add better validations for Parameter Default types (Fixes #717)
* Add AWS::Cognito (fixes #720)
* Add required attribute, JobFlowId, to EMR::InstanceGroupConfig (#722)
* Add WAFRegional support (#723)
* fix for ElastiCacheRedis.py example to use awacs (#725)
* Add EMR autoscaling (#729)
* Add SshUsername to AWS::OpsWorks::UserProfile
* Add PlacementConstraints to AWS::ECS::TaskDefinition
* Add MaximumExecutionFrequency to Config SourceDetails

1.9.3 (2017*04*13)
------------------

* Fix pycodestyle by using an explicit exception type
* Add more details to pycodestyle errors for travis runs
* Fix validator function exception test
* Remove limit check on conditions * Fixes #657
* Allow valid value for TargetGroup HealthCheckPort (#659)
* Added step functions and basic tests (#661)
* Adding example for CloudTrail (from http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws*resource*cloudtrail*trail.html) (#667)
* Fix ApiGateway.py sample (#666)
* Update comment on type checking
* Added missing props to ec2.NetworkInterfaces (#669) (#670)
* Add WAF Common Attacks Sample (#675)
* Updated constants with new instance types (#674)
* SSM Targets * fix spelling mistake (Value => Values) (#673)
* Do json validation on ApiGateway::Model Schema (Fix #679) (#681)
* SQS: Add FifoQueue and ContentBasedDeduplication (#687)
* VPCPeeringConnection: add PeerOwnerId & PeerRoleArn (#688)
* IAM: Add InstanceProfileName to InstanceProfile (#689)
* Add ApiGateway UsagePlanKey resource
* Add DeadLetterConfig property to Lambda::Function
* Add new subproperties to route53 and redshift (#690)
* Route53: ChildHealthChecks is a list of strings (#690)
* Fix typo in S3_Bucket_With_Versioning_And_Lifecycle_Rules.py (#693)
* Allow a dict to be passed in to initalize Tags (#692)
* Add SSM::Parameter
* Update autoscaling example to remove rebinding (#695)

1.9.2 (2017*01*29)
------------------

* Extra template validation (#635)
* Update ECS to Jan 17, 2017 release (#642)
* Add Timezone property to DBInstance (#643)
* Test Python 3.6 (#644)
* Adding RDS engine support for oracle*se2 (#646)
* Correct required in ecs.Service (#645)
* Add Separator property to IoT Firehose Action
* Add Fn::Split function (#647)
* Added to_dict() method to troposphere.Template (#651)
* Allow use of AWSHelperFn for IOPS (#652)
* Allow HelperFN w/ autoscaling policies (#654)

1.9.1 (2017*01*03)
------------------

* Improve readability of AssumeRolePolicyDocument attribute (#591)
* Add Environment to Lambda Function (#616)
* Adding DataSources to OpsWorks App and RdsDbInstances to OpsWorks Stack (#621)
* Added SNS::Subscription resource (SubscriptionResource) (#622)
* Added CodeBuild Project resource and a CodeBuild example (#624)
* Add back support for Python 2.6 (#626)
* Fixed missing add_resource in example Cloudwatch rule (#629)
* Create new property Environment for aws lambda Function (#631)
* Add KmsKeyArn to Lambda Function
* Add CopyTagsToSnapshot to RDS::DBInstance
* Fix pycodestyle issues with examples/Lambda.py
* Add AWS::SSM::Association
* Add AWS::EC2::SubnetCidrBlock and AWS::EC2::VPCCidrBlock
* Add mutually_exclusive validator
* Add DocumentType to AWS::SSM::Document
* Add OpsWorks Resources: UserProfile and Volume
* Update opsworks per 2016*11*22 changes
* Allow both dict and string for opswork CustomJson
* Add IPv6 support from 2016*12*01 update

1.9.0 (2016*11*15)
------------------

* Note: the dynamodb change below may cause backwards compatibility issues.
  There have been deprecation warnings for a while.
* Replace dynamodb module with dynamodb2 (#564)
* Add CodeCommit as a supported AWS resource type
* Add update of github Releases page to RELEASE doc
* Update elasticache for 2016*10*12 changes (#592)
* Support for S3 Lifecycle Rule property NoncurrentVersionTransitions (#596)
* Include resource title in required attr exception (#597)
* Added Placement class for the Placement property in LaunchSpecifications. (#598)
* Add EFS example (#601)
* Add support to old mysql db engine (#602)
* Fix typo in Example Allowed Values (#603)
* Remove `title` validation. Fixes #428 (#605)
* Add support for conditions in cfn2py script (#606)
* Added MongoDB default port to constants (#608)
* Add HttpVersion prop to DistributionConfig (CloudFront HTTP/2 Support) (#609)
* Added missing QueryStringCacheKeys property to CloudFront ForwardedValues (#612)
* Add a validator for ELB names (#615)

1.8.2 (2016*10*08)
------------------

* Add SpotPrice to SpotFleet LaunchSpecifications
* Add new properties to ECS (Clustername to Cluster and Family to TaskDefinition)
* Add Alias object to KMS (fixes #568)
* Added cross*stack references (#569)
* Handle lambda => awslambda mapping in cfn2py (#573)
* Add support for Tags to Certificate Manager Certificates (#574)
* Adding enhanced monitoring to rds.DBInstance (#575)
* Add support for LogGroupName in Logs::LogGroup (#576)
* Update Export param (#579)
* Add support for `Fn::Sub` (#582)
* RDS DBInstance Engine required even when DBSnapshotIdentifier is set (#583)
* Resource updates for 2016*10*06 changes (Fixes #584)
* Add AWS::ApiGateway::UsagePlan (fixes #585)
* Add AWS::CodeCommit::Repository (fixes #586)
* Provide better type checking for values in from_dict (#587)
* Allow HelperFn in UpdatePolicy for ASG (#588)
* Fixed from_dict case where you have a list of non BaseAWSObjects (#589)

1.8.1 (2016*09*12)
------------------

* Add TargetGroupArn and fix ContainerPort (#549)
* Update ApiGateway resources (#550)
* Add support for AutoScalingCreationPolicy (#552)
* Change param type for resource: RestAPI (#553)
* Add support for IAM Roles in ECS Task Definitions (#556)
* Allow Tags on AWS::CloudFormation::Stack (#557)
* Added support for protocol in container definition PortMapping property. (#558)
* Add Tags prop to Kinesis::Stream (#565)
* Add a sample ECS Cluster template (#559)
* Add support for ElasticsearchVersion in Elasticsearch Domain (#560)
* WAF SizeContraint needs to be an AWSProperty (Fixes #561)
* Add Tags prop to Kinesis::Stream (#565)

1.8.0 (2016*08*15)
------------------

* Support "UserName" property for AWS::IAM::User #529
* Remove double S from S3ObjectVersion (fixes #530) (#531)
* Fix TemplateGenerator import logic. (#533)
* Add Name attributes for IAM groups and roles (#535)
* Automatically check if zip_file exceeds 4096 chars #537
* Add AWS Certificate Manager (#538)
* Add Application Auto Scaling (#539)
* CloudFront updates (Aug 9, 2016) (#540)
* Add PerformanceMode to FileSystem resource (#541)
* Add AWS Internet of Things (#542)
* Extend Template constructor. (#543)
* Add application loadbalancer objects and properties (#544)
* Improve check_zip_file to calculate a minimum length (#548)

1.7.0 (2016*07*07)
------------------

* Convert fake AWSHelperFns into AWSProperties (#478)
* cfn script: allow update (#484)
* Validate the template against AWS before stack creation (#485)
* Fix capitalization in README (#487)
* Remove duplicate waf FieldToMatch class (fixes #489)
* Tune validation logic and test cases for S3 bucket names (#486)
* waf XssMatchTuple should be an AWSProperty (Fixes #498)
* Allow setting a different region for S3 upload (#491)
* fix attribute for ApiKey (Enable -> Enabled) (#492)
* Invoke join correctly (#493)
* EMR: fix EBS configuration (#497)
* EMR: Action on Failure Fix (CONTINUE_AND_WAIT*>CANCEL_AND_WAIT) (#501)
* Rewritten the helper to be more flexible (#502)
* Added support for Kinesis Firehose (#505)
* Add support for VPC Flow Logs (#507)
* Syntax highlighting for readme python sample (#508)
* Added Name property to Kinesis streams (#510)
* Availability zones and EC2 instance type (#512)
* Add `AutoScalingReplacingUpdate` to `UpdatePolicy` (#513)
* Removed validation for DBSubnetGroupName when creating a read replica with SourceDBInstanceIdentifier (#515)
* EMR configurations values: also allow AWS helper functions (#516)
* Fix AssociationParameters Value type to list of strings (#518)
* Add DependsOn to Deployment and remove Enabled from StageKey (#519)
* Update fields in apigateway StageDescription (#521)
* Fix rename pep8*>pycodestyle and bump to fixed pyflakes (#522)
* Allows MultiAZ=false with AvailabilityZone in rds (#524)
* Do not require Status as a param in iam.AccessKey (#525)
* Fix badges in README

1.6.0 (2016*05*04)
------------------

* Remove unnecessary AWSHelperFn from props
* ReplicationConfigurationRules Destination is now an object (#380)
* Add WAF SizeConstraintSet and XssMatchSet
* Logs SubscriptionFilter (#413)
* Elasticsearch support (#415)
* Fixed ConfigSnapshotDeliveryProperties type (#420)
* Adding support for EMR resources (#421)
* Fix `ecs.TaskDefinition.Volumes` that was incorrectly flagged as required (#422)
* AWS::ECR test example (#423)
* Add cloudfront hostedzoneid for route53 (#427)
* Typo in variable name (431)
* ScalingAdjustment is an integer (#432)
* Add Compress to CloudFront (#433)
* Added missing S3OriginConfig parameter(#437)
* Allow both GetAtt and a basestring (#440)
* Add VpcConfig to AWS::Lambda::Function (#442)
* Add Version Resource to awslambda (#443)
* Add Alias Resource to awslambda (#444)
* Ignore If expression during validation of ASG (#446)
* Add test and tweak fix for ASG MaxSize If fix (#446)
* Provide Valid Lambda Function Memory Values for use in Parameters (#449)
* Add FunctionName to Lambda::Function (#452)
* Add support for EBS volume configuration in EMR resources (#453)
* Add elasticsearch instance type constants (#454)
* DomainName isn't a required parameter (#457)
* Create Documentation To Help Contributors (#458)
* Move Groups to property, add policy template version (#460)
* Fix Elasticsarch Domain object naming and add backward compatibility (#461)
* EC2 update FromPort, ToPort and Egress as optional (#463)
* ApiGateway Resources (#466)
* Added CloudWatch Events support (#467)
* Import JSON Templates (#468)
* Fix config Source object to take a list of SourceDetails (#469)
* Update Contribute Document to Use Requirements.txt (#470)
* Update to Apr 25, 2016 release (#471)
* Implement LifecycleRule Transitions property (#472)
* Better AWSHelperFn support in template generator (#473)
* Fix Bucket AccessControl to allow Ref (#475)
* Fix baseclass for AWS::Logs::Destination (#481)
* Add test for AWS::Logs::Destination (#482)

1.5.0 (2016*03*01)
------------------

* Add MariaDB to list of RDS engines [GH*368]
* Add ap*northeast [GH*373]
* Add T2 Nano [GH*374]
* capability support for cfn [GH*375]
* Update to resource list in documentation [GH*383]
* More info from validator function errors [GH*385]
* Add testing for python 3.5 [GH*388]
* Extended title validation [GH*389]
* EC2 NAT Gateway [GH*394]
* Add AWS::ECR::Repository [GH*395]
* Add KmsKeyId and StorageEncrypted to DBCluster [GH*396]
* Add awacs soft dependency [GH*397]
* New dynamodb2 module to replace dynamodb for consistent interface [GH*398]
* Add IsMultiRegionTrail support [GH*399]
* Add IncludeGlobalResourceTypes to RecordingGroup [GH*400]
* Capitalize examples [GH*404]
* use location constants for bucket creation in cfn [GH*409]

1.4.0 (2016*01*01)
------------------

* Add RDS Aurora support [GH*335]
* Change DeploymentGroup Ec2TagFilters to list [GH*337]
* Correct EC2 SpotFleet LaunchSpecifications [GH*338]
* RDS::DBCluster change AvailabilityZone to AvailabilityZones [GH*341]
* ECS LoadBalancerName property is a string [GH*342]
* CodeDeploy S3Location Version property is not a default requirement [GH*345]
* Add AutoEnableIO to AWS::EC2::Volume
* Only discard Properties in JSONrepr [GH*354]
* CodeDeploy added ApplicationName [GH*357]
* CodeDeploy DeploymentGroupName property missing [GH*358]
* Add in cloudfront properties for max, default [GH*360]
* Allow RDS iops to be 0 [GH*361]
* Add CodePipline support [GH*362]
* Implemented CloudFormation changes from Dec 3 and Dec 28 [GH*366]
* Add AWS::Config, AWS::KMS, AWS::SSM

1.3.0 (2015*10*21)
------------------

* Add new resources from 2015*10*01 CloudFormation release:
    * AWS::CodeDeploy
    * AWS::DirectoryService::SimpleAD
    * AWS::EC2::PlacementGroup and AWS::EC2::SpotFleet
    * AWS::Lambda::EventSourceMapping and AWS::Lambda::Permission
    * AWS::Logs::SubscriptionFilter
    * AWS::RDS::DBCluster and AWS::RDS::DBClusterParameter
    * AWS::WorkSpaces::Workspace
* Add updates to these resources from 2015*10*01 CloudFormation release:
    * AWS::ElastiCache::ReplicationGroup
    * AWS::OpsWorks::Stack
    * AWS::OpsWorks::App
    * AWS::S3::Bucket
* Add ElastiCache (Redis) Example [ GH*329]
* RDS: Added postgresql*license [GH*324]
* tail: only add unseen events [GH*327]
* Make Ref() work with datapipeline.ObjectField.RefValue [GH*328]
* Fix DeploymentGroup resource_type (AWS::CodeDeploy::DeploymentGroup) [GH*333]
* Add concatenation operator function __add__ for Tags [GH*334]

1.2.2 (2015*09*15)
------------------

* Give more info about type errors [GH*312]
* Move `tail` within the troposphere library. This lets external libraries
  leverage this function [GH*315]
* Improve opsworks validation [GH*319]
* Fix RDS validation with conditional parameters [GH*320]

1.2.1 (2015*09*07)
------------------

* Bugfix for RDS Ref/GetAtt issue [GH*310]

1.2.0 (2015*09*04)
------------------

* Add support for EFS
* Elasticache: only validate az choices if azs is a list [GH*292]
* Add from_dict function to BaseAWSObject [GH*294]
* IAM: Path is optional for Role and InstanceProfile [GH*295]
* Validate parameter options based on Type [GH*296]
* RDS: Add more specific validators to DBInstance [GH*297]
* Add constants for the parameter types [GH*300]
* Add lambda ZipFile property [GH*301]
* Adds VPCEndpoint resource type [GH*304]
* Supports tags in ElasticBeanstalk environments [GH*308]
* Move cloudformation attribute setting to __setattr__ [GH*309]

1.1.2 (2015*07*23)
------------------

* Clarify the license is a [BSD 2*Clause license](http://opensource.org/licenses/BSD*2*Clause)
* Add FindInMap type check for AutoScalingGroup validation of group sizes [GH*285]
* Implement the template Metadata section [GH*286]

1.1.1 (2015*07*12)
------------------

* Rename lambda*>awslambda [GH*268]
* Add t2 large instance type [GH*269]
* IAM: status required and managedpolicyarns [GH*272]
* Fix wrong prop name in rds.OptionGroup OptionGroupConfigurations*>OptionConfigurations [GH*274]
* Add CloudFormation CustomResource [GH*278]
* Add rds snapshot on delete example [GH*280]
* Unable to pass Cluster name as String [GH*281]
* Fix unable to set StringValue on ObjectField in DataPipeline [GH*283]

1.1.0 (2015*06*15)
------------------

* added AWS::CloudFormation::Stack NotificationARNs property [GH*243]
* Add additional import for PrivateIpAddressSpecification [GH*247]
* Add true s3 bucket name validator [GH*249]
* Replace strict `int` comparison by flexible `troposphere.validators.integer` [GH*251]
* Add validation for AZMode property on CacheCluster objects [GH*252]
* Fixing Opsworks Naming (ThresholdWaitTime -> ThresholdsWaitTime) [GH*253]
* Adding AutoScalingType to OpsWorks Instance [GH*255]
* Allow extending classes + tests [GH*257]
* Release June 11, 2015 [GH*259]
* Add M4 instances and Memcached port [GH*260]
* Add property for Subnet: MapPublicIpOnLaunch [GH*261]
* Minor improvements and fixes [GH*262]
* Update LoginProfile. Note: this is a breaking change and requires adding a
  ```Password=``` keyword parameter into LoginProfile. [GH*264]
* Add 2 additional properties (elasticache:CacheCluster:SnapshotName and opsworks:Layer:LifecycleEventConfiguration) [GH*265]

1.0.0 (2015*05*11)
------------------

* Fix two elasticache properties [GH*196]
* Add interim MinimumProtocolVersion to CloudFront ViewerCertificate [GH*218]
* Missing OriginPath in cloudfront.py [GH*220]
* Fix DBInstance constraints in order to allow the creation of RDS read*only replicas  [GH*221]
* Add properties CharacterSetName, KmsKeyId, and StorageEncrypted to AWS::RDS::DBInstance [GH*224]
* Add Route53 HostedZoneVPCs, HostedZoneTags, HealthCheckTags
* Add new properties from 2015*04*16 CloudFormation release [GH*225, GH*240]
* Allow default region for GetAZs() [GH*232]
* Make AvailabilityZones parameter optional in AutoScalingGroup
* EventSubscription resource + EC2 types [GH*227]
* Python 3.4 support [GH*228]
* examples fix: users is list [GH*237]
* SNS Topic fields are not required [GH*230]
* Make AvailabilityZones parameter optional in AutoScalingGroup [GH*236]

0.7.2 (2015*03*23)
------------------

* Support AWS helper functions in lists during validation [GH*179]
* Update README [GH*183]
* Fixing RedshiftClusterInVpc example; incorrect SG setup [GH*186]
* Add optional NonKeyAttributes to DynamoDB Projection class [GH*188]
* Change AutoScaling ScheduledAction StartTime, EndTime, and Recurrence to optional [GH*189]
* CloudFront forwarded values required on cache behavior [GH*191]
* DynamoDB attribute definitions required [GH*192]
* Add some ec2 required fields [GH*193]
* Fix ElasticBeanstalk resources [GH*213]
* Fix iam Policy Resource/Property bug [GH*214]

0.7.1 (2015*01*11)
------------------

* Fix UpdatePolicy validation [GH*173]
* Add AWS::CloudFormation::Init ConfigSets support [GH*176]
* Change CloudWatch Alarm's Threshold prop to be basestring [GH*178]

0.7.0 (2015*01*02)
------------------

* Added new Google Group for discussion:
  https://groups.google.com/forum/#!forum/cloudtools*dev
* Fixing ValueError message to refer the correct package [GH*135]
* Change cfn to add *R* with no argument lists all the Stacks [GH*138]
* Add eu*central*1 region (Frankfurt) [GH*139]
* ConfigurationTemplate is an Object [GH*140]
* Release: AWS CloudFormation on 2014*11*06 [GH*141]
* Remove duplicate security_group from port [GH*143]
* UpdatePolicy and CreationPolicy [GH*144]
* Fixes duplicate key error reporting [GH*145]
* Fix warning in CloudFront example description [GH*148]
* Cfn script create bucket in the specified region [GH*149]
* Remove Unnecessary EOL whitespace [GH*150]
  Note: this changes the default JSON separators.
* More metadata options [GH*153]
* Metadata auth [GH*155]
* Fixed CreationPolicy [GH*157] [GH*160]
* Addded AWS template VPC_Single_Instance_In_Subnet example [GH*162]
* Add 2014*12*24 CloudFormation release changes [GH*167] [GH*168] [GH*169]
* Add GSI & LSI Functionality [GH*161] [GH*172]
* Fixed landscape.io issues [GH*170]

0.6.2 (2014*10*09)
------------------

* Update to 2014*09*29 AWS release [GH*132]
* Add ElastiCache & Port # Constants [GH*132]
* Add ELB Tag Support [GH*133]
* Fix DBSecurityGroupIngress required properties [GH*134]

0.6.1 (2014*09*28)
------------------

* Update InitConfig per AWS docs [GH*120]
* S3 improvement + essential constants [GH*125]
* Allow FindInMap() for ec2.NetworkInterfaceProperty.GroupSet [GH*128]

0.6.0 (2014*08*26)
------------------

* Use subnet group for param, not vpc securitygroup [GH*65]
* Add support for Equals function and Condition [GH*66]
* Added ELB access logs and CrossZone test [GH*67]
* Added support for more condition functions [GH*69]
* Tweaked a few integer validation messages [GH*71]
* Fix resource.name backward compatibility regression
* Fix pep8 errors due to new pep8 1.5.x changes [GH*72]
* Allow Ref() in VPNGatewayRoutePropagation RouteTableIds list [GH*73]
* Add OpsWorks Support [GH*74]
* Add AutoScalingGroup TerminationPolicies [GH*77, GH*87]
* Add new property MetricsCollection [GH*79]
* Patching Users class to use basestring or Ref type for Groups [GH*80]
* Added support for Kinesis [GH*81]
* Allow autoscaling group to support 'min instances in service' and 'max size' values that are Refs [GH*82]
* Added support for Redshift [GH*84]
* Add DestinationSecurityGroupId in ec2.SecurityGroupRule [GH*85]
* Add CloudFront CacheBehavior [GH*86]
* Tweak UpdatePolicy properties [GH*88]
* Tweaks to rds.DNInstance [GH*89]
* Tweaks to EC2 DeviceIndex property values [GH*90]
* Fix AutoScalingGroup MinSize MaxSize [ GH*92]
* Add Encrypted option to AWS::EC2::Volume [GH*96]
* Add missing config to s3.Bucket [GH*97]
* Add CloudFront DistributionConfig, CacheBehavior and DefaultCacheBehavior [GH*98]
* Add EC2 Instance InstanceInitiatedShutdownBehavior [GH*99]
* Updating the block device options for AutoScalingGroups [GH*100]
* Added support for AWS::CloudFormation::Init in AutoScalingGroup [GH*101]
* Added VPCPeering class [GH*102]
* Opworks CustomJson property expects a JSON object not a string [GH*103]
* Add support for VersioningConfiguration on S3 buckets [GH*104]
* Added Logs resource type [GH*105]
* Add PlacementGroup param to AutoScalingGroup [GH*111]
* Add VpcPeeringConnectionId parameter to EC2 Route [GH*113]
* Make RDS DBInstance MasterUsername and MasterPassword optional [GH*116]
* Add CloudTrail, tweaks to CloudWatch Alarm, and support route53 AliasTarger EvaluateTargetHealth [GH*117]
* Add LogDeliveryWrite canned ACL for S3 bucket [GH*118]

0.5.0 (2014*03*21)
------------------

* Add OpenStack native types [GH*61]
* Make `integer()` validator work with any integer*like object [GH*57]
* Add support to ELB ConnectionDrainingPolicy [GH*62]
* Add more OpenStack resource types and validation [GH*63]

0.4.0 (2014*02*19)
------------------

* Allow to extend resource classes by adding custom attributes [GH*16]
* Add AWS::ElastiCache::SubnetGroup [GH*27]
* Fix examples/VPC\_EC2\_Instance\_With\_Multiple\_Dynamic\_IPAddresses.py [GH*29]
* CacheSecurityGroupNames not required if using VpcSecurityGroupIds [GH*31]
* Add VPNConnectionRoute object and attribute to VPNConnection [GH*33]
* add new CrossZone option to ELB [GH*34]
* Add VPC\_With\_VPN\_Connection example
* Fixup some of the network related validators and pep8 changes
* Add support for Tags and PortRange
* Add more resource name properties per CloudFormation release 2013*12*19
* Add Tier Environment property per CloudFormation release 2013*12*19
* Add VPNGatewayRoutePropagation per CloudFormation release 2013*11*22
* Add Tags properties  per CloudFormation release 2013*09*24
* Add network changes from CloudFormation release 2013*09*17
* Canonicalize integer and bool values for more consistent output [GH*35]
* Add travis*ci for automated testing [GH*38]
* Check output of examples in test\_examples [GH*40]
* Add support for conditions and for Fn::If() [GH*41]
* Tweak ELB ranges to match ec2 console [GH*43]
* Handle bool values better in cfn2py [GH*45]
* Allow strings (as well as Refs) for Subnet VpcId [GH*47]
* Add InstanceID to AutoScalingGroup and LaunchConfiguration
* ec2.DHCPOptions NTPservers -> NtpServers [GH*54]
* Add SQS dead letter queue from CloudFormation release 2014*01*29
* Add AutoScaling ScheduledAction from release 2014*01*27
* Add Tags for SecurityGroups [GH*55]
* RecordSets in Route53 not formatted correctly [GH*51]
* Allow Ref() in NetworkInterfaceProperty GroupSet list [GH*56]

0.3.4 (2013*12*05)
------------------

* Adding separators options to print to json function [GH*19]
* Add cfn2py script to convert json templates to Python [GH*22]
* Add EnableDnsSupport and EnableDnsHostnames properties for VPC [GH*23]
* Add VPC support to elasticache [GH*24]
* Fix missing Import Ref [GH*26]
* Add missing AWS::SQS::Queue properties
* Add resource naming (Name Type)
* Allow Ref's in the list objects

0.3.3 (2013*10*04)
------------------

* Fix Ref() to output the name only [GH*17]
* Add Ref test.
* Fix some IAM issues

0.3.2 (2013*09*25)
------------------

* Convert VPCDHCPOptionsAssociation to not have \_\_init\_\_
* Fix Output, Parameter and UpdatePolicy to not output a Properties dict
* Raise a ValueError if adding a duplicate object to the template
* Set the correct dictname for UpdatePolicy

0.3.1 (2013*09024)
------------------

* Make the code more DRY [GH*15]
* Add a optional `name` argument to AWSProperty constructor
* Add ability to push large stack templates to S3
* InstanceType is not required (defaults to m1.small)
* Add AssociatePublicIpAddress property for AutoScaling LaunchConfiguration
* Make Tags an AWSHelperFn to make it easier to assign
* Resource property types should not be in a Properties dictionary
* Clean up "required" error checking and handle property types better

0.3.0 (2013*08*07)
------------------

* Do not validate AWSHelperFun's [GH*8] [GH*9]
* Add missing return in integer\_range [GH*10]
* integer\_range validator for ELB HealthyCheckInt
* Convert RDS::DBInstance::VPCSecurityGroups to new list type checking
* VPCSecurityGroups for RDS should be a list, not a basestring 

0.2.9 (2013*05*07)
------------------

* Fixing ELB LoadBalancerPorts not required (error in the AWS docs)

0.2.8 (2013*04*24)
------------------

* EC2 SecurityGroup Egress & Ingress rules should be objects
* Fix Attributes validator for ELB Policies
* Allow PolicyDocuments to use (if present) awacs Policy objects
* Add test for matching against a tuple of types

0.2.6 (2013*03*26)
------------------

* Add cfn script to create, tail and show stack resources

0.2.5 (2013*03*25)
------------------

* UpdatePolicy validation enhancements [GH*5]
* Add VPCSecurityGroups property to AWS::RDS::DBInstance
* DefaultCacheBehavior is a required property for DistributionConfig
* Fix CustomGateway -> CustomerGateway
* Domain does not have any properties
* Fix VPC security group rule bugs
* Added EBSBlockDevice and BlockDeviceMapping classes.
* Add a post*validator to allow individual object to validate themselves
* Add ability to use validate functions on property values
* Add validation of list element types
* Add unit tests

0.2.0 (2013*02*26)
------------------

* Add support for autoscaling notification configurations [GH*2]
* Add support for AWS::ElastiCache and AWS::RDS
* Move to AWSProperty entirely.
* Add shortcuts for the NotificationTypes strings
* Add Python 3.x compatibility support
* Pass pep8 and pyflakes

0.1.2 (2013*02*21)
------------------

* First PyPI release
* Add S3 bucket support [GH*1]
