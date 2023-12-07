4.5.3 (2023*12*06)
-------------------------------
* Upgrade readthedocs config to v2
* Add tests and lint runs for maintenance action
* Install correct version of pyright for maintenance action
* Rename due to conflict: S3::StorageLensGroup.StorageLensFilter
* Add required Name to GuardDuty.IPSet tests
* Updates from spec version 149.0.0 (#2207)
* Add AWS::ARCZonalShift
* Add AWS::S3Express
* Add new supported resources to docs
* Prefer ECS::Service.LoadBalancer (Fixes #2206)

4.5.2 (2023*11*11)
-------------------------------
* Updates from spec version 146.0.0 (#2201)
* Updates from spec version 148.0.0 (#2202)
* Remove EMRserverless "Configurations" due to recursive reference to ConfigurationObject
* Move __hash__ to BaseAWSObject to support objects in dictionaries (Fixes #2204)
* Add missing patch related to EMRserverless Configurations removal
* Remove Tags from EventBridge.Rule (Fixes #2203)

4.5.1 (2023*10*26)
-------------------------------
* Fix __eq__ protocol (#2197)
* Fix formatting
* Object equality fixes (#2200)
* Add new OpenSearch instance names to constants.py (Fixes: #2198) (#2199)

4.5.0 (2023*10*24)
-------------------------------
* Updates from spec version 136.0.0 (#2175)
* Add AWS::BackupGateway
* Add AWS::CleanRooms
* Add AWS::Comprehend
* Add AWS::InternetMonitor
* Add AWS::IVSChat
* Add AWS::Omics
* Add AWS::OSIS
* Add AWS::Proton
* Add AWS::Shield
* Add AWS::SimSpaceWeaver
* Add AWS::SystemsManagerSAP
* Add AWS::VerifiedPermissions
* Add AWS::VpcLattice
* Add new AWS services to resource doc
* Updates from spec version 137.0.0 (#2177)
* Updates from spec version 138.0.0 (#2178)
* Updates from spec version 139.0.0 (#2179)
* Fix incorrect backward compatibility for ReplicationConfiguration
* Update isort version to fix pip-shims error
* RDS: allow AllocatedStorage to be a Ref (Fixes #2176)
* Updates from spec version 140.0.0 (#2181)
* Updates from spec version 141.0.0 (#2183)
* Updates from spec version 142.0.0 (#2185)
* Fixup Events patch due to removal of AWS::Events::Rule.Tag
* Updates from spec version 142.1.0 (#2187)
* Add support for object comparison (#2182)
* Reduce error output when encountering a jsonpatch error
* Collect all the service items before modifying the service
* Fixup Events patch due to removal of AWS::Events::EventBus.TagEntry
* Updates from spec version 143.0.0 (#2192)
* Updates from spec version 144.0.0 (#2193)
* Drop support for Python 3.7 (#2190)
* Run tests against Python 3.12 and add trove classifier (#2189)
* Fix Parameters.validate incorrect validate for CommaDelimitedList (#2191)
* Updates from spec version 145.0.0 (#2195)
* Fix lint error from a previous commit to gen.py
* RDS: Allow defining ManageMasterUserPassword property instead of the MasterUserPassword property.
* Adding support for default values in FindInMap
* Add AWS::EntityResolution
* Add AWS::HealthImaging
* Add AWS::MediaPackageV2
* Add AWS::PCAConnectorAD
* Add AWS::WorkSpacesWeb
* Add new AWS services to resource doc and fix some trailing parens
* Fix EC2::TransitGatewayMulticastDomain.Options conflict

4.4.1 (2023*08*16)
-------------------------------
* Remove EOL Python 3.7 from the tests action
* Add new DeletionPolicy attribute option, RetainExceptOnCreate (#2174)
* Fix RDS Validations (#2171)

4.4.0 (2023*08*13)
-------------------------------
* Add validator for AWS::RDS::DBCluster.ServerlessV2ScalingConfiguration (#2135)
* Updates from spec version 116.0.0 (#2133)
* Updates from spec version 117.0.0 (#2136)
* update engine types validator for AWS::RDS::DBInstance (#2137)
* Remove storage size validation for gp3 RDS StorageType (#2142)
* Updates from spec version 118.1.0 (#2140)
* Fix black formatting from #2142
* Fix Macie jsonpatch for spec 119.0.0 changes
* Updates from spec version 119.0.0 (#2143)
* Automate fixing and generation of standalone types
* Updates from spec version 119.1.0
* Updates from spec version 120.0.0
* Update S3 patch to remove Encryption changes
* Omit Connect::EvaluationForm for now due to recursion issues
* Updates from spec version 121.0.0
* Updates from spec version 122.0.0
* Updates from spec version 124.0.0
* Updates from spec version 125.0.0
* Updates from spec version 126.0.0
* Updates from spec version 127.0.0
* Remove SageMaker CreatedBy and LastModifiedBy patches
* Updates from spec version 129.0.0
* Updates from spec version 130.0.0
* Updates from spec version 131.0.0
* Updates from spec version 132.0.0
* Updates from spec version 133.0.0
* Updates from spec version 134.0.0
* Fix regex compile error in ec2.py (#2156)
* Batch validators add support for SPOT_PRICE_CAPACITY_OPTIMIZED (#2167)
* Update rds validator logic (#2164)
* Add more Serverless Application Model event sources
* Add all valid origin_request_policy config behaviors to validators (#2163)
* Updated the gen.py script example
* Added Tags into EventBridge Rule
* Addded RuntimeManagementConfig attribute to serverless Function.
* Fix black formatting
* Updates from spec version 135.0.0 (#2170)
* Support "elastic" throughput mode for EFS
* AWS::EC2::PlacementGroup validators
* Run regen to fixup recent changes
* Add ApiFunctionAuth serverless class for Api Function events (#2145)
* Fix up previous serverless ApiEvent Auth change
* TypeError() return the expected Class as last exception argument (#2147)
* Fix TypeError formatting to reflect the true error (Fixes #2157)
* Fix black formatting
* Update requirements for building docs
* Upgrade black from 22.3.0 to 23.7.0

4.3.2 (2023*03*10)
-------------------------------
* Include the troposphere/type_defs package in the build

4.3.1 (2023*03*10)
-------------------------------
* Updates from spec version 109.0.0 (#2120)
* Updates from spec version 112.0.0 (#2121)
* Add many missing EC2, RDS and Elasticache instance type constants. (#2124)
* Run spec checks in their own GitHub Actions job (#2127)
* Fix valid values used by validators (#2125)
* Mark constants as final (#2126)
* Updates from spec version 113.0.0 (#2129)
* Fix black formatting
* Fix generating constants based on recent use of typing.Final
* Add gp3 as valid RDS StorageType (Fixes #2123)
* Change Lambda ZipFile limit from 4096 to 4MB (Fixes #2119)
* Allow gp3, st1, sc1 for EMR volume type (Fixes #2113)
* Updates from spec version 114.0.0 (#2130)
* Fixup for a new 114.0.0 spec - remove AppIntegrations patch
* Updates from spec version 115.0.0 (#2131)

4.3.0 (2023*01*28)
-------------------------------
* Patch GameLift::Fleet to add type for AnywhereConfiguration
* Updates from spec version 100.0.0 (#2103)
* Add support for Flink 1.15 runtime environment (#2106)
* Remove unneeded patches due to spec updates
* Updates from spec version 101.0.0 (#2109)
* Allow version override for spec download
* Fix lint issues
* Updates from spec version 102.0.0
* Updates from spec version 103.0.0
* Updates from spec version 104.0.0
* Updates from spec version 105.0.0
* Updates from spec version 106.0.0
* Updates from spec version 107.0.0
* Updates from spec version 108.0.0
* Updates from spec version 109.0.0
* Add AWS::DocDBElastic
* Add AWS::Grafana
* Add AWS::KendraRanking
* Add AWS::Oam
* Add AWS::OpenSearchServerless
* Add AWS::Pipes
* Add AWS::Scheduler
* Add new AWS services to resource doc
* Modify `SourceDBInstanceIdentifier` validator to allow `BackupRetentionPeriod` (#2116)
* Fix tests related to GH-2116
* Add support for TagMap tags
* Enable AWS::Scheduler
* Support for FSx/Lustre PERSISTENT_2 DeploymentType (#2110)
* Be more lenient about types for Export (#2114)

4.2.0 (2022*11*28)
-------------------------------
* me-central-1 (UAE) (#2078)
* Updates from spec version 91.0.0 (#2077)
* Fix EC2 and MSK issues from the 91.0.0 spec
* Add T3, T4G, M4, M5, M6G, R4, R5 and R6G constants for Elasticache nodes. (#2079)
* Add spec patches for GreengrassV2 and Rekognition
* Redo SageMaker Clarify* patches now that it is implemented more fully
* Sort available property keys for error message
* Updates from spec version 93.0.0 (#2082)
* Allow setting hosted elasticsearch volume_types to gp3 (#2083)
* Updates from spec version 94.0.0 (#2085)
* Added AWS::Serverless::StateMachine (#2076)
* Fix import issue with previous serverless.py change
* Add a simple test for the new AWS::LanguageExtensions transform (#2074)
* Add support for FunctionUrlConfig in Serverless Function (#2072)
* Allow RDS storage for sqlserver to have a minimum of 20GB (#2087)
* Run tests against Python 3.11 and add trove classifier (#2089)
* Updates from spec version 95.0.0 (#2090)
* Updates from spec version 96.0.0 (#2091)
* Use the latest github actions (#2092)
* Updates from spec version 97.0.0 (#2093)
* Lakeformation: remove ResourceProperty naming conflict (#2088)
* Fix jsonpatch for SageMaker::ModelPackage (spec file removed Tag)
* Updates from spec version 98.0.0 (#2097)
* Updates from spec version 99.0.0 (#2098)
* Add redshiftserverless.py module (#2101)
* Add AWS::Organizations support (#2102)
* Add comment to include validator in Organizations regen
* Fix regen script to be more specific on service names to exclude
* Sort missing service names
* Add AWS::ConnectCampaigns
* Add AWS::ControlTower
* Add AWS::EMRServerless
* Add AWS::IdentityStore
* Add AWS::IoTFleetWise
* Add AWS::M2
* Add AWS::ResourceExplorer2
* Add AWS::RolesAnywhere
* AWS::SupportApp
* Update resources_aws.md with newly added services
* Switched ApiGatewayV2 Stage resource props to show tag as a dict instead of validator, and also updated LogLevels to match CloudFormation/Boto3 definition of LogLevels
* Fix CodeDeploy LoadBalancerInfo validator to include TargetGroupPairInfoList (fixes #2096)

4.1.0 (2022*08*08)
-------------------------------
* Updates from spec version 72.0.0 (#2046)
* Make spec download and isort fixups less verbose
* Fix issues with recent changes to SageMaker spec files (72.1.0)
* Updates from spec version 72.1.0 (#2048)
* Updates from spec version 73.1.0 (#2049)
* Updates from spec version 75.0.0 (#2051)
* Updates from spec version 76.0.0 (#2052)
* Updates from spec version 76.0.0 (#2056)
* Update SSM Patch Baseline OS validator (#2057)
* Add spec patch for AppFlow
* Updates from spec version 78.0.0 (#2059)
* Remove unused Clarify* properties from SageMaker to pass lint
* Add "allExcept" as a valid CloudFront::Cachepolicy QueryStringBehavior (Fixes #2060)
* Remove uneeded `from __future__ import print_function` (#2058)
* Allow json/yaml strings for SSM Document.Content property (#2055)
* Fix broken regen due to LakeFormation changes
* Fix DataSync::LocationFSxONTAP.Protocol type duplication
* Fix spec issue with Transfer::Server ProtocolDetails
* Updates from spec version 81.1.0 (#2062)
* Allow CodeArtifact resources to accept policytypes (Fixes #2065)
* Pin pyright to version 1.1.261
* Add support for list types and validator functions in GlobalsHelperFn type check (#2064)
* Add gp3 as an allowed volume type for ImageBuilder
* Provide better error message for missing property in generator
* Fix issue in spec 82.0.0 with DynamoDB KeySchema Type
* Updates from spec version 82.0.0 (#2067)
* Add example of SNS alert for failed batch job events (#2069)
* Fix backup of spec files
* Revert "Fix issue in spec 82.0.0 with DynamoDB KeySchema Type"
* Fix first run of "make spec" where a spec file isn't initally there
* Updates from spec version 83.0.0 (#2068)

4.0.2 (2022*05*11)
-------------------------------
* Add ephemeral storage
* #2038 Add support for additional Flink runtime environments (#2037)
* Fix isort in serverless.py
* Updates from spec version 66.0.0 (#2039)
* Updates from spec version 66.1.0 (#2040)
* Updates from spec version 68.0.0 (#2041)
* tests action: ensure spec generation and formatting fixups are clean
* Add AWS::IoTTwinMaker and AWS::MediaTailor
* Add package-lock engines dependency info
* Install development dependencies when testing
* Add flake8 to requirements-dev.txt
* Updates from spec version 68.1.0 (#2043)
* Updates from spec version 69.0.0 (#2044)
* Fail on error for commands used to regen
* When generating files, handle a primitive type in the item_type
* Further updates from spec version 69.0.0

4.0.1 (2022*04*04)
-------------------------------
Breaking Changes
^^^^^^^^^^^^^^^^
* The json template indent was reduced from 4 to 1 for space savings.
  Old spacing can be restored using to_json(indent=4).

Changes
^^^^^^^
* Updates from spec version 63.0.0
* reduce JSON CloudFormation template size (#2028)
* Updates from spec version 65.0.0
* Update black and isort versions
* Output resource_type string in a more black compatible format
* Let type hints show that lists are also valid
* Fix WAFv2 AndStatement and OrStatement validation (Fixes #2026)
* Add click to requirements-dev.txt to force version
* Black formatting

4.0.0 (2022*03*28)
-------------------------------
Breaking Changes
^^^^^^^^^^^^^^^^
* See breaking changes in 4.0.0-beta.0 and 4.0.0-beta.1

Changes
^^^^^^^
* Fix AccessControlAllowMethods.Items validator (Fixes #2023)
* Fix duplicate resource names due to FSx::Volume
* Updates from spec version 62.0.0
* Update serverless.py
* EMR: Add missing JobFlowInstancesConfig properties

4.0.0-beta.1 (2022*03*20)
-------------------------------
Breaking Changes
^^^^^^^^^^^^^^^^
* AWS::DataBrew
  - Renamed Job.S3TableOutputOptions S3Location => JobS3Location
* AWS::ImageBuilder
  - Renamed ContainerRecipe ComponentConfiguration => ContainerComponentConfiguration
* AWS::SageMaker
  - Renamed ModelBiasEndpointInput EndpointInput => ModelBiasEndpointInput
  - Renamed ModelExplainabilityJobInput EndpointInput => ModelExplainabilityEndpointInput
  - Renamed ModelQualityJobDefinition EndpointInput => ModelBiasEndpointInput

* AWS::WAFv2
  - Renamed AndStatementOne, AndStatementTwo => AndStatement
  - Renamed NotStatementOne, NotStatementTwo => NotStatement
  - Renamed OrStatementOne, OrStatementTwo => OrStatement
  - Renamed RateBasedStatementOne, RateBasedStatementTwo => RateBasedStatement
  - Renamed StatementOne, StatementTwo, StatementThree => Statement

Changes
^^^^^^^
* Updates from spec version 58.0.0
* automating maintenance with Github actions
* removing double requirement from requirements-dev.txt
* Run maintenance action once a day at 5am
* Fix typo in ECS validator name
* Allow the use of AWSHelperFn in one_of validator
* Update maintenance workflow to include spec version
* Updates from spec version 59.0.0
* Remove maintenance run on push to main and change cron time
* Add type annotations for base classes & some validators (#2013)
* Reimplement WAFv2 Statement validation
* Fix typing issues in openstack
* Only run the maintenance workflow once a day
* Improve error message for AWSProperty types where resource_type is not defined
* Add AWS::KinesisVideo and AWS::Personalize
* Updates from spec version 60.0.0
* Updates from spec version 61.0.0
* Add AWS::BillingConductor
* DataBrew: Fix duplicate but different S3Location
* ImageBuilder: Fix duplicate but different ComponentConfiguration
* SageMaker: Fix duplicate but different ComponentConfiguration

4.0.0-beta.0 (2022*02*19)
-------------------------
This release has refactored the code to allow for auto-generation of the troposphere classes from the AWS
Resource Specification. Backward compatibility changes were applied to minimize changes to existing scripts.

Breaking Changes
^^^^^^^^^^^^^^^^
* AWS::EC2
  - Ipv6Addresses AWSHelperFn class is now an AWSProperty InstanceIpv6Address
  - Added Ipv6Addresses function that returns a InstanceIpv6Address for backward compatibility
  - SpotFleet::LaunchSpecifications IamInstanceProfile change: IamInstanceProfile => IamInstanceProfileSpecification
  - SpotFleet::LaunchSpecifications NetworkInterfaces change: NetworkInterfaces => InstanceNetworkInterfaceSpecification
  - SpotFleet::LaunchSpecifications Placement change: Placement => SpotPlacement
  - SpotFleet::LaunchSpecifications TagSpecifications change: SpotFleetTagSpecification => TagSpecifications
* AWS::ElasticLoadBalancingV2::ListenerRule Action was renamed ListenerRuleAction due to conflict with Listener Action AuthenticateOidcConfig
* AWS::OpsWorksCM resources have been moved out of opsworks.py into opsworkscm.py, please adjust imports.
* AWS::Route53Resolver resources have been moved out of route53.py into route53resolver.py, please adjust imports.
* Removed deprecated Elasticsearch ElasticsearchDomain alias, use Domain instead
* Removed deprecated IAM PolicyProperty alias, use Policy instead.
  Note: a future major version will rename the Policy resource and property again..
* json_checker now uses TypeError (rather than ValueError) for non-str or non-dict types

Changes
^^^^^^^
* Add missing entry for the 3.2.2 release
* Auto-generate MWAA
* Auto-generate ElasticBeanstalk
* Auto-generate Elasticsearch
* Auto-generate ElastiCache
* Auto-generate SNS
* Auto-generate SecurityHub
* Auto-generate Synthetics
* Auto-generate Neptune
* Auto-generate KMS
* Auto-generate GlobalAccelerator
* Better handle selective imports of primitive types in code generator
* Auto-generate EFS
* Auto-generate SecretsManager
* Auto-generate DAX
* Auto-generate DMS
* Auto-generate DataPipeline
* Auto-generate Detective
* Auto-generate DirectoryService
* Auto-generate DLM
* Auto-generate DocDB
* Add backward compatibility to allow resource renames to work correctly
* Fix SNS Subscription resource type
* Auto-generate IAM
* Add missing EFS patch
* Auto-generate Macie
* Auto-generate ResourceGroups
* Auto-generate GuardDuty
* Auto-generate Panorama
* Auto-generate WAFRegional
* Auto-generate StepFunctions
* Remove unneeded properties that should not be emitted
* Auto-generate Cassandra
* Auto-generate Athena
* Auto-generate FMS
* Remove py.typed until type information is fully implemented (#2003)
* Change for gen to emit all meaningful properties, Tags cleanup, and other changes
* Auto-generate NetworkManager
* Auto-generate ApiGateway
* Auto-generate Config
* Auto-generate EKS
* Update AppSync per 2022-01-13 changes
* Add AWS::Forecast
* Updates from 53.0.0 spec
* Auto-generate KinesisFirehose
* Tweaks for the regen script
* Add PropsDictType into policies.py
* Auto-generate ApiGatewayV2
* Auto-generate AppConfig
* Add PrivateDnsPropertiesMutable to ServiceDiscovery
* Auto-generate AppMesh
* Auto-generate CloudTrail
* Fixup some incorrect Tags types
* Auto-generate EventSchemas
* Auto-generate CustomerProfiles
* Auto-generate Chatbot
* Auto-generate FraudDetector
* Auto-generate WAF
* Auto-generate IoT
* Auto-generate IoT1Click
* Auto-generate EMR
* Auto-generate RDS
* Auto-generate Cognito
* Remove workaround for Lex TextLogDestination
* Auto-generate CloudWatch
* Auto-generate Redshift
* Auto-generate CodePipeline
* Auto-generate ServiceCatalog
* Auto-generate OpsWorks
* Auto-generate OpsWorksCM
* Auto-generate Route53
* Auto-generate Route53Resolver
* Auto-generate Pinpoint
* Auto-generate PinpointEmail
* Auto-generate AutoScalingPlans
* Updates from spec version 53.1.0
* Auto-generate Logs
* Auto-generate GroundStation
* Auto-generate Glue
* Auto-generate Batch
* Auto-generate Budgets
* Auto-generate CodeCommit
* Auto-generate CodeBuild
* Auto-generate MediaConnect
* Auto-generate MediaLive
* Auto-generate MediaStore
* Auto-generate Kendra
* Auto-generate ImageBuilder
* Auto-generate IoTWireless
* Updates from spec version 54.0.0
* Auto-generate CloudFormation
* Auto-generate MediaPackage
* Auto-generate KinesisAnalyticsV2
* Auto-generate IoTAnalytics
* Anchor some substitutions in regen
* Auto-generate ElasticLoadBalancing
* Auto-generate ElasticLoadBalancingV2
* Auto-generate DynamoDB
* Updates from spec version 55.0.0
* Auto-generate AutoScaling
* Updates from spec version 56.0.0
* Add AWS::KafkaConnect
* Run black and isort on kafkaconnect.py
* Updates from spec version 57.0.0
* Add AWS::IoTThingsGraph and AWS::RefactorSpaces
* Allow function exports in gen.py
* Auto-generate EC2
* Save copy of resource spec via "make spec"

3.2.2 (2022*01*07)
------------------
* Auto-generate CloudFront
* Auto-generate Backup
* Auto-generate AmazonMQ
* Auto-generate SSM
* Auto-generate IVS
* Auto-generate IoTEvents
* Auto-generate ManagedBlockchain
* Auto-generate MediaConvert
* Auto-generate MSK
* Auto-generate NimbleStudio
* Auto-generate OpenSearchService
* Auto-generate RAM
* Auto-generate Route53RecoveryControl
* Auto-generate S3ObjectLambda
* Auto-generate S3Outposts
* Auto-generate ServiceDiscovery
* Auto-generate SSMContacts
* Auto-generate SSMIncidents
* Auto-generate Transfer
* Auto-generate Events
* Auto-generate FIS
* Auto-generate DataSync
* Various changes to the code generator
* Fix copy/paste issue resulting in incorrect ECS validator assignment (Fixes #2000)
* Automatically correct Resource/Property dups in the code generator
* Auto-generate XRay
* Add missing CloudFront jsonpatch
* Auto-generate Greengrass
* Auto-generate GreengrassV2
* Add code regen and remove the resource spec version from the code
* Upgrade auto-generated files to spec version 52.0.0
* Auto-generate AppStream
* Auto-generate Inspector
* Add AWS::InspectorV2
* Add missing jsonpatch files
* Add the TableClass property to DynamoDB Resource

3.2.1 (2022*01*03)
------------------
* Restore AWS::ECS::TaskDefinition AuthorizationConfig (Fixes #1997)
* Fix backward compat issue with ECS HostVolumeProperties => Host
* Fix backward compat issue with CodeDeploy RevisionLocation => Revision

3.2.0 (2022*01*01)
------------------
Major Changes
^^^^^^^^^^^^^
* Python 3.6 support removed due to Python EOL
* Moving to auto-generation of troposphere classes

  To make troposphere easier to maintain and keep up-to-date, the core
  troposphere classes will be migrated to be auto-generated from
  the CloudFormation Resource Specification. Changes have been made to
  maintain backward compatibility in troposphere 3.x releases. Please
  open a github issue if an auto-generated class is not compatible.

  Note: a future troposphere 4.x release will likely align more with the AWS
  naming of Resources and Properties which would break backward compatibility.

Changes
^^^^^^^
* Add Architectures to AWS::Serverless::Function (#1971)
* Update EKS per 2021-11-10 changes
* Update IoTWireless per 2021-11-11 changes
* Update Batch per 2021-11-11 changes
* Added CopyTagsToSnapshot to DBCluster (#1973)
* Run tests against Python 3.10 and add trove classifier (#1974)
* Update Location per 2021-11-12 changes
* Update AppStream per 2021-11-18 changes
* Update MSK per 2021-11-18 changes
* Update FSx per 2021-11-18 changes
* Update FinSpace per 2021-11-18 changes
* Update CloudFormation per 2021-11-18 changes
* Added ecs.TaskDefinition.RuntimePlatform (#1976)
* AWS::ElastiCache::ReplicationGroup.DataTieringEnabled (#1977)
* AWS::Logs::LogGroup.Tags (#1978)
* CHANGELOG.rst Formatting Fixes (#1983)
* Fixed NetworkFirewall::LoggingConfiguration (#1984)
* Update NetworkFirewall jsonpatch for LoggingConfiguration
* Update CloudFront (adding ResponseHeadersPolicyId fields) per 2021-11-04 changes (#1982)
* Update cfn2py - change add_description to set_description (#1975)
* Added CompatibleArchitectures to Serverless::LayerVersion (#1972)
* Add UpdateConfig to EKS::Nodegroup (#1980)
* Added RedshiftRetryOptions and enabled support for RetryOptions in Re… (#1981)
* Update Kinesis per 2021-12-09 (#1988)
* Update AppFlow 18.6.0->51.0.0 (#1985)
* Move validators into a module to support future changes
* pre-commit checks for black+isort (#1989)
* Fix black formatting/isort
* First pass cleanup for the code generator script
* Auto-generate NetworkFirewall
* Update Timestream per 2021-12-03 changes
* Add AWS::RUM per 2021-12-03 changes
* Auto-generate FSx
* Add AWS::Evidently per 2021-12-03 changes
* Remove (now unused) yaml import from the gen.py
* ap-southeast-3 (Jakarta), ap-northeast-3 (Osaka), and new zone in Beijing (#1991)
* More updates for code generation and update some resources
* Update Connect per 2021-12-03 changes
* Add AWS::ResilienceHub
* Update SageMaker per 2021-12-03 changes and fix SageMaker::Device
* Rearrange S3 classes to make comparison to auto-generated code easier
* Auto-generate S3 and update per 2021-12-03 changes
* Auto-generate AppSync and update per 2021-12-06 changes
* Auto-generate Kinesis
* Auto-generate AccessAnalyzer
* Auto-generate ACMPCA
* Makefile tweaks: add fix target and combine spec2 with spec
* Add a few more items into .gitignore
* Fix some lint errors
* Remove support for Python 3.6 due to EOL
* Re-gen Evidently to add documentation links
* Use anonymous hyperlink targers to prevent warnings in the docs
* Auto-generate LakeFormation
* Auto-generate Lightsail
* Auto-generate CodeDeploy
* Regenerate doc links
* First pass update to CONTRIBUTING documentation
* Auto-generate ECR
* Install myst_parser for markdown docs
* Adding missing troposphere.validators package (#1995)
* Clean up stub generation
* Auto-generate WAFv2 (#1996)
* Remove redundent classes from KinesisFirehose
* Fix examples where variables were aliasing classes
* Introduce PropsDictType and other changes to be more mypy friendly
* Add AWS::Lex
* Regen AccessAnalyzer
* Regen ACMPCA
* Auto-generate Amplify
* Auto-generate KinesisAnalytics
* Auto-generate AppFlow
* Auto-generate ApplicationAutoScaling
* Auto-generate ApplicationInsights
* Auto-generate AppRunner
* Auto-generate APS
* Auto-generate ASK
* Auto-generate AuditManager
* Auto-generate QLDB
* Auto-generate QuickSight
* Auto-generate RUM
* Auto-generate Wisdom
* Auto-generate WorkSpaces
* Auto-generate FinSpace
* Auto-generate GameLift
* Auto-generate HealthLake
* Auto-generate EMRContainers
* Auto-generate DevOpsGuru
* Auto-generate MemoryDB
* Auto-generate Signer
* Add back Endpoint to MemoryDB for backward compatibility
* Regen AppSync, ResilienceHub, and S3
* Regen Kinesis, LakeFormation, and Lightsail
* Auto-generate LookoutEquipment, LookoutMetrics, and LookoutVision
* Auto-generate ECS
* Auto-generate Location
* Auto-generate LicenseManager
* Regen IoTSiteWise
* Auto-generate IoTCoreDeviceAdvisor and IoTFleetHub
* Don't emit a Tags import for Json style tags
* Auto-generate CodeGuruProfiler and CodeGuruReviewer
* Auto-generate CodeStar, CodeStarConnections, and CodeStarNotifications
* Auto-generate CodeArtifact
* Auto-generate AppIntegrations
* Auto-generate Rekognition
* Auto-generate Route53RecoveryReadiness
* Auto-generate ServiceCatalogAppRegistry
* Auto-generate Timestream
* Auto-generate SSO
* Auto-generate RoboMaker
* Auto-generate SDB
* Auto-generate SES
* Auto-generate SQS
* Updates to gen.py
* Auto-generate Lambda
* Regen CodeDeploy, Connect, DataBrew, ECR, and Evidently
* Regen FSx, NetworkFirewall, SageMaker, and WAFv2
* Auto-generate CE
* Auto-generate CertificateManager
* Auto-generate Cloud9
* Auto-generate CUR

3.1.1 (2021*11*06)
------------------
* Added "CompatibleArchitectures" to LayerVersion (#1963)
* Update AWS::Events::Rule EcsParameters (#1966)
* AWS::Cassandra::Table.DefaultTimeToLive and AWS::Cassandra::Table.TimeToLiveEnabled (#1967)
* AWS::ElasticLoadBalancingV2::TargetGroup.TargetType (#1968)
* Add multi-region param to KMS (#1969)
* Fix black formatting
* Add AWS::Rekognition per 2021-10-21 changes
* Add AWS::Panorama per 2021-10-21 changes
* Update SageMaker per 2021-10-21 changes
* Update FMS per 2021-10-21 changes
* Update MediaConnect per 2021-10-27 changes
* Update Route53Resolver per 2021-10-28 changes
* Update Lightsail per 2021-10-28 changes
* Update EC2 per 2021-10-28 changes
* Update api docs
* Add explicit readthedocs config and requirements.txt
* Add sphinx requirement versions
* Added Cloudfront Response Header changes per Nov 4 updates. (#1970)
* Fix black formatting
* Update IoT per 2021-11-04 changes
* Update DataSync per 2021-11-04 changes
* Update Pinpoint per 2021-11-04 changes
* Update Redshift per 2021-11-04 changes
* Update NetworkFirewall per 2021-11-04 changes
* Update EC2 per 2021-11-04 changes

3.1.0 (2021*10*16)
------------------
* Add KinesisFirehose::DeliveryStream.HttpEndpointDestinationConfiguration
* Update S3 per 2021-09-02 changes
* Update IoT per 2021-09-02 changes
* Update KinesisFirehose per 2021-09-02 changes
* Update EventSchemas per 2021-09-02 changes
* Update DataSync per 2021-09-02 changes
* Update ACMPCA per 2021-09-02 changes
* Update Transfer per 2021-09-02 changes
* Update firehose.py parameter type validation (#1953)
* AWS Backup: Add EnableContinuousBackup boolean to BackupRuleResourceType (#1958)
* fix: creating specific AWS::MediaPackage::OriginEndpoint  AWSProperty sets, as they are different from AWS::MediaPackage::PackagingConfiguration's AWSProperty sets
* making user role optional for emr studio
* Add missing properties to EMR::Studio
* Fix black formatting
* allow helper functions for codebuild project type
* Update Cloudtrail per 2021-09-10 changes
* Add AWS::APS per 2021-09-16 changes
* Add AWS::HealthLake per 2021-09-17 changes
* Updaate ACMPCA per 2021-09-17 changes
* Add AWS::MemoryDB per 2021-09-23 changes
* Update AppSync per 2021-09-23 changes
* Update Lambda per 2021-09-30 changes
* Update KinesisFirehose per 2021-09-30 changes
* Updat ECR per 2021-09-30 changes
* Update IoT per 2021-10-07 changes
* Add AWS::Lightsail per 2021-10-07 changes
* Update Backup per 2021-10-07 changes
* Add AWS::OpenSearchService per 2021-10-16 changes
* Import ABC from collections.abc for Python 3.10 compatibility.
* Add validation and tests to AWS::OpenSearchService::Domain.EngineVersion (#1960)
* Fix isort and black formatting issues
* Update Backup with missing resources from 2021-10-07 changes
* Update CodeBuild per 2021-10-13 changes
* Move resource type lists from README to individual files
* Fix missing underscore in README links
* Add AWS::Wisdom per 2021-10-14 changes
* Support Globals section for serverless

3.0.3 (2021*08*28)
------------------
* Enable MSK IAM Role based authentication
* Add AWS::Signer
* Allow LaunchTemplateSpecification in LaunchTemplateOverrides
* Add AWS::Route53RecoveryControl and AWS::Route53RecoveryReadiness per 2021-07-29 changes
* Update S3Outposts per 2021-07-29 changes
* Update DataBrew per 2021-07-29 changes
* Update FSx per 2021-08-05 changes
* Update ApiGatewayV2 per 2021-08-12 changes
* Update AppSync per 2021-08-05 changes
* Add Athena::PreparedStatement per 2021-08-05 changes
* Update ApiGateway per 2021-08-12 changes
* Add TimeZone property to AWS::AutoScaling::ScheduledAction
* Fix black formatting in autoscaling.py
* Update WAFv2 per 2021-08-12 changes
* Update Elasticsearch per 2021-08-17 changes
* Update SageMaker per 2021-08-19 changes
* Update Redshift per 2021-08-19 changes
* Update AutoScaling per 2021-08-19 changes
* Update CodeBuild per 2021-08-19 changes
* Add AWS::Logs::ResourcePolicy (#1936)
* Add AWS::Serverless::HttpApi (#1941)
* Update to main branch for tests workflow
* Switch build status badge from travis-ci to github
* Fix duplicate AWS::Logs::ResourcePolicy
* Remove duplicate TargetTrackingScalingPolicyConfiguration from dynamodb.py

3.0.2 (2021*07*24)
------------------
* Add JWT to apigatewayv2 valid_authorizer_types (#1929)
* [batch] Update ContainerProperties properties (#1930)
* Remove p3s directory
* Update ImageBuilder per 2021-07-01 changes
* Update ServiceDiscovery per 2021-07-08 changes
* Update CodeDeploy per 2021-07-08 changes
* Add KmsKeyId Attribute to LogGroup (#1931)
* Added missing AWS::Neptune::DBCluster properties (#1932)
* Added Sign and Verify key usage (#1935)
* Fix CanarySettings PercentTraffic definition
* Fix NetworkFirewall properties
* Fixup formatting in NetworkFirewall
* Use jsonpatch to fixup spec files before generating code
* Update DataBrew per 2021-07-09 changes
* Update Logs per 2021-07-15 changes
* Update EC2 per 2021-07-21 changes
* Update Cassandra per 2021-07-21 changes
* Add AWS::LookoutEquipment per 2021-07-22 changes
* Update QLDB per 2021-07-22 changes
* Update CloudWatch per 2021-07-22 changes

3.0.1 (2021*07*06)
------------------
* Fix CHANGELOG with correct 3.0.0 release date
* Fix EKS::Nodegroup.Taints to use the correct key for taints (#1925)
* Include cfn_flip in setup.cfg (#1927)
* Catch install dependencies with "make release-test

3.0.0 (2021*07*05)
------------------
This release now only supports Python 3.6+
Special thanks to @michael-k for the Python 3 work and tooling improvements.

Breaking Changes
^^^^^^^^^^^^^^^^
* Python 3.6+ (Python 2.x and earlier Python 3.x support is now deprecated due to Python EOL)
* Remove previously deprecated Template methods.
  To update to currently supported methods, substitute:
  ::

      add_description() => set_description()
      add_metadata() => set_metadata()
      add_transform() => set_transform()
      add_version() => set_version()

* Remove deprecated troposphere.UpdatePolicy()
* Remove TROPO_REAL_BOOL. Booleans are output instead of string booleans for better interoperability with tools like cfn-lint.
* Remove deprecated troposphere.dynamodb2. Use troposphere.dynamodb instead.
* Remove StageName deprecation warning in apigateway StageDescription
* Rename ElasticBeanstalk OptionSettings property to OpionSetting per AWS spec files

Changes
^^^^^^^
* Run '2to3 -n -w --no-diffs .'
* Require Python >= 3.6
* [utils,examples] Revert changes to print functions made by 2to3
* Remove unnecessary conversions of iterables to lists
* Cleanup scripts
* Restore TypeError's message
* Cleanup ImportErrors and NameErrors
* [tests] Make necessary adjustments
* [examples] Fix indentation
* Make BaseAWSObject.propnames pickleable
* Remove '# -*- coding: utf-8 -*-'
* Stop inheriting from object explicitly
* Modernize super() calls
* AWS::MWAA Adding for managed airflow (#1858)
* Add constants for EC2 instance types: T4g. (#1885)
* Add AppIntegrations per 2021-03-25 changes
* Add LookoutMetrics per 2021-03-25 changes
* Add CustomerProfiles per 2021-03-25 changes
* Fix Python3 deprecation: import from collections.abc
* Run black and isort over main directories (examples scripts tests troposphere)
* Switch to using setup.cfg and add test checks for black/isort
* Remove previously deprecated Template methods
* Remove deprecated troposphere.UpdatePolicy()
* Remove troposphere.dynamodb2. Use troposphere.dynamodb instead.
* Remove StageName deprecation warning in apigateway StageDescription
* Start adding CHANGELOG entries for pending 3.0.0 release
* Quick fix for travis needing cfn_flip imported
* Set the pending release as 3.0.0
* Remove Python 2.7 artifacts from Makefile
* Fix intermittent failure due to an incorrect resource_name in ECR
* Remove TROPO_REAL_BOOL and output real boolean values
* Fix template generator boolean interoperability (Fixes #1044)
* Update fis.py (#1887)
* lambda memory can be configured in 1 MB increments now (#1886)
* Make generation script more black format compliant
* Fix black format in tests/test_awslambda.py
* Fix properties in LookoutMetrics VpcConfiguration
* Update ServiceDiscovery per 2021-03-18 changes and re-gen file
* Adding support for using KinesisStreamSpecification with DynamoDB
* Run black over last change to correct formatting (#1889)
* Update Batch per 2021-03-31 changes
* Update imports in some recent changes with isort
* Update Logs per 2021-04-01 changes
* Update CloudWatch per 2021-04-01 changes
* Update Route53Resolver per 2021-04-01 changes
* Update GameLift per 2021-04-01 changes
* Update ElasticBeanstalk per 2021-04-01 update
* Update Cloud9 per 2021-04-01 changes
* Update Budgets per 2021-04-01 changes
* Update ApiGateway per 2021-04-01 changes
* Update Config per 2021-04-01 changes
* Update DataBrew per 2021-04-01 changes
* Update ElastiCache per 2021-04-08 changes
* Update IVS per 2021-04-15 changes
* Update EC2 per 2021-04-15 changes
* Update MWAA per 2021-04-15 changes
* Update CloudFormation per 2021-04-15 changes
* Update AutoScaling per 2021-04-23 changes
* Update ElastiCache per 2021-04-23 changes
* Update IoTWireless per 2021-04-26 changes
* Add NimbleStudio per 2021-04-26 updates
* Add IoTFleetHub per 2021-04-29 updat4es
* Update SES per 2021-04-29 changes
* Update Detective per 2021-04-29 changes
* rearrange make file, add some new targets, remove linting from test
* add github action to replace travis
* remove .travis.yml as a GitHub Action was added as a replacement
* implement suggestion to use `python -m pip ...`
* rename workflow to tests
* Create Export instances for Output.Export in cfn2py (#1895)
* ec2 volume throughput (#1896)
* Transit-Gateway MulticastSupport (#1897)
* Add helpers.userdata.from_file_sub() (#1898)
* AWS::WAFv2::WebACL.CustomResponseBodies and AWS::WAFv2::RuleGroup.CustomResponseBodies (#1899)
* Fixup black formatting
* Add M6G, C6G, R6G and R6GD constants for Elasticsearch data and master nodes. (#1900)
* Add fargate ephemeral storage property (#1906)
* AWS::ApiGatewayV2::Integration.IntegrationSubtype (#1907)
* AWS::RDS::DBCluster: add missing GlobalClusterIdentifier parameter (#1908)
* Add constants for RDS instance types: R6G (#1905)
* [batch] Update AWS::Batch required properties (#1913)
* Add compression property to Serverless::Api (#1914)
* Limit flake8 to core troposphere directories
* Add AWS::FinSpace per 2021-05-06 changes
* Update CloudFront::Function per 2021-05-06 changes
* Add AWS::XRay per 2021-05-06 changes
* Add AWS::FraudDetector per 2021-05-06 changes
* Update IoT per 2021-05-06 changes
* Update GameLift per 2021-05-06 changes
* Update CloudFront per 2021-05-06 changes
* Update ACMPCA per 2021-05-06 changes
* Update S3 per 2021-05-13 changes
* Update ECR per 2021-05-13 changes
* Add AWS::SSMIncidents per 2021-05-14 changes
* Update DynamoDB per 2021-05-14 changes
* Add AWS::SSMContacts per 2021-05-14 changes
* Update CloudFormation per 2021-05-14 changes
* Add AWS::IoTCoreDeviceAdvisor per 2021-05-20 changes
* Add AWS::AppRunner per 2021-05-20 changes
* Update EC2 per 2021-05-20 changes
* Add AWS::CUR per 2021-05-27 changes
* Update FSx per 2021-05-27 changes
* Update MediaPackage per 2021-05-27 changes
* Add ConnectivityType property for NatGateway
* AWS::ECR::Repository.ImageScanningConfiguration
* Allow all policy types in s3.AccessPoint.Policy, not just dicts
* Add new sns event parameters
* Fix black formatting for serverless.py
* Update ACMPCA per 20201-05-27 update
* Add AWS::Location per 2021-06-07 changes
* Update SSM per 2021-06-10 changes
* Update SQS per 2021-06-10 changes
* Update KinesisAnalyticsV2 per 2021-06-10 changes
* Update RAM per 2021-06-10 changes
* Update KMS per 2021-06-17 changes
* Update MWAA per 2021-06-21 changes
* Add AWS::Connect per 2021-06-24 changes
* Update CloudFormation per 2021-06-24 changes
* Update DAX per 2021-06-24 changes
* Update Transfer per 2021-06-24 changes
* Update ApplicationAutoScaling per 2021-07-01 changes
* Update AppMesh per 2021-06-17 changes
* Fix TestSplit negtive test (Fixes #1919)
* Add EngineVersion to Athena::WorkGroup (Fixes #1915)
* Add ResourceTags to ImageBuilder::InfrastructureConfiguration (Fixes #1909)
* S3 ReplicationConfigurationRules Prefix is no longer required (Fixes #1910)
* Update ApiGateway per 2021-04-15 changes (Fixes #1893)
* Rename ElasticBeanstalk OptionSettings property to OpionSetting per AWS spec files
* Add ProtocolVersion to ElasticLoadBalancingV2::TargetGroup (Fixes #1888)
* Update example for ElasticBeanstalk OptionSettings property rename
* Switched VALID_CONNECTION_PROVIDERTYPE to list and added GitHub and GitHubEnterprise
* Add AWS::EKS::Nodegroup.Taints
* Add support for Container based Serverless::Functions and added missing props
* Update requirements-dev.txt for dependencies
* Update black formatting
* Update setup.cfg awacs dependency
* Update RELEASE.rst with new release commands

2.7.0 (2021*03*20)
------------------
* Fix typo in ECS DeploymentCircuitBreaker RollBack => Rollback (Fixes #1877)
* added sort flag to yaml method arguments (#1090)
* Fix line length issue from previous commit (#1090)
* docs: use Template.set_metadata instead of add_metadata (#1864)
* change PropertyMap in kinesisanalyticsv2 PropertyGroup to dict (#1863)
* Fix tests by removing import of json_checker in kinesisanalyticsv2 (#1863)
* Adding optional Elasticsearch::Domain options for custom endpoints (#1866)
* Add support for AppConfig::HostedConfigurationVersion (#1870)
* Add constants for RDS instance types: M5d, M6g. (#1875)
* Support Throughput for gp3 ebs volumes (#1873)
* Add GreengrassV2 per 2020-12-18 changes
* Add AuditManager per 2020-12-18 changes
* Update SageMaker per 2020-12-18, 2021-01-21, 2021-02-11, and 2021-02-25 changes
* Add LicenseManager per 2020-12-18 changes
* Update ECR per 2020-12-18 and 2021-02-04 changes
* Update EC2 per 2020-12-18, 2021-02-12, 2021-02-25, and 2021-03-11 changes
* Add DevOpsGuru per 2020-12-18 changes
* Update CloudFormation per 2020-12-18 changes
* Update S3 with some missing properties
* Update FSx per 2020-12-18 changes
* Update ElastiCache per 2020-12-18 changes
* Add DataSync per 2021-01-07 changes
* Update Route53 and Route53Resolver per 2021-01-07 changes
* Update Config per 2021-01-07 changes
* Add MediaConnect per 2021-01-07 changes
* Update ApiGatewayV2 per 2021-01-07 changes
* Add IoTWireless per 2021-01-07 changes
* Update SSO per 2021-01-07 changes
* Add ServiceCatalogAppRegistry per 2021-01-14 changes
* Add QuickSight per 2021-01-14 changes
* Add EMRContainers per 2021-01-14 changes
* Update ACMPCA per 2021-01-21 changes
* Add LookoutVision per 2021-01-28 changes
* Update ImageBuilder per 2021-02-04 changes and reorder classes a bit
* Update ElastiCache per 2021-02-04 changes
* Update Casandra per 2021-02-04 changes
* Update IoTAnalytics per 2021-02-05 changes
* Update ServiceCatalog per 2021-02-11 changes
* Update CloudFormation per 2021-02-11 changes
* Update DMS per 2021-02-11 changes
* Update IoTAnalytics per 2021-02-18 changes
* Update FSx per 2021-02-18 changes
* Update Kendra per 2021-02-18 changes
* Update AppMesh per 2021-02-21 changes
* Update DynamoDB per 2021-02-22 changes
* Update Pinpoint per 2021-02-24 changes
* Update IAM per 2021-02-25 changes
* Update EKS per 2021-02-25 changes
* Update IoTSiteWise per 2021-03-01 changes
* Add S3Outposts per 2021-03-04 changes
* Update IoT per 2021-03-04 changes
* Update Events per 2021-03-04 changes
* Update SecretsManager per 2021-03-04 changes
* Update StepFunctions per 2021-03-10 changes
* Update RDS per 2021-03-11 changes
* Update ECS per 2021-03-11 changes
* Update CE per 2021-03-11 changes
* Update EFS per 2021-03-11 changes
* Update required fields for Batch::ComputeResources (Fixes #1880)
* Fix autoscaling.Tags to use boolean instead of str (#1874)
* Add OutpostArn to EC2::Subnet (Fixes #1849)
* Update Transfer per 2020-10-22 changes (Fixes #1817)
* Add MediaPackage per 2020-10-22 changes (Fixes #1815)
* Update README with functioning example of missing required property (Fixes #1763)
* Update EMR per 2020-10-22 and 2021-02-25 changes (Fixes #1816)
* Add DataBrew (Fixes #1862)
* Update version in docs (#1882)
* Fix some corner cases in the autogenerator
* Update CertificateManager per 2021-03-11 changes
* Update Detective per 2021-03-15 changes
* Update ECS per 2021-03-16 changes
* Add S3ObjectLambda per 2021-03-18 changes
* Add FIS per 2021-03-18 changes

2.6.4 (2021*03*08)
------------------
* Remove extraneous import
* Fix required value for ecs.EFSVolumeConfiguation AuthorizationConfig (Fixes #1806)
* Added Period attribute to CloudWath::Alarm MetricDataQuery (#1805)
* Fix issues with ecs.EFSVolumeConfiguration usage (#1808)
* Updating region and availability zone constants (#1810)
* fixing typo in updated region and availability zone constants
* Add mising constants for Elasticsearch data and master node instance sizes. (#1809)
* AWS::Elasticsearch::Domain.DomainEndpointOptions (#1811)
* increased CloudFormation template limits (#1814)
* Fix tests with new template limits (Related to #1814)
* Add CapacityReservationSpecification to EC2::LaunchTemplateData (Fixes #1813)
* Update Appstream per 2020-10-22 changes
* Update SecretsManager::ResourcePolicy per 2020-10-22 changes
* Add Tags to resources in Batch per 2020-10-22 changes
* Update SNS::Topic per 2020-10-22 changes
* Update Events per 2020-10-22 changes
* Update KinesisFirehose::DeliveryStream per 2020-10-22 changes
* Update AppSync::ApiKey per 2020-10-22 changes
* Update Elasticsearch per 2020-10-22 changes
* AWS::CloudFront::Distribution.LambdaFunctionAssociation.IncludeBody (#1819)
* AWS::SSM::PatchBaseline.OperatingSystem AllowedValues expansion (#1823)
* AWS::ImageBuilder::ImageRecipe.EbsInstanceBlockDeviceSpecification.VolumeType AllowedValues expansion (io2) (#1824)
* AWS::CodeBuild::Project.Environment.Type AllowedValues expansion (WINDOWS_SERVER_2019_CONTAINER) (#1825)
* AWS::Glue::Connection.ConnectionInput.ConnectionType AllowedValues expansion (NETWORK) (#1826)
* Update AWS::Cognito::UserPoolClient (#1818)
* Update firehose.py (#1830)
* Update AWS::CodeArtifact::Repository (#1829)
* AWS::EC2::VPCEndpoint.VpcEndpointType AllowedValues expansion (GatewayLoadBalancer) (#1833)
* AWS::KinesisAnalyticsV2::Application.RuntimeEnvironment AllowedValues expansion (FLINK-1_11)
* AWS::Kinesis::Stream.ShardCount required (#1841)
* flake8 fixes (#1845)
* Add ReplicaModifications of s3 (#1850)
* Update serverless apievent (#1836)
* Add AllocationStrategy to EMR instance fleet configuration (#1837)
* Add CopyActions prop to BackupRuleResourceType (#1838)
* Fix formatting in recent EMR PR
* AWS::AutoScaling::LaunchConfiguration.MetadataOptions (#1840)
* AWS::AutoScaling::AutoScalingGroup.CapacityRebalance (#1842)
* AWS Lambda Has Increased Memory Limits (#1844)
* AWS::Lambda::Function support for container image deployment package (#1846)
* Fix tests from previous merge
* AWS::CloudFront::Distribution.CacheBehavior.TrustedKeyGroups (#1847)
* AWS::CloudFront::Distribution.Origin.OriginShield (#1848)
* docs: fix simple typo, shoud -> should (#1851)
* AWS::Glue::Connection.ConnectionInput.ConnectionType AllowedValues expansion (#1852)
* Adding DeploymentCircuitBreaker property for ECS Service (#1853)
* ec2: add ClientVpnEndpoint.ClientConnectOptions & SelfServicePortal (#1854)
* s3: add property BucketKeyEnabled (#1857)
* Add g4ad, c6gn, d3, and d3en instance types to constants (#1859)
* Add IoTSiteWise
* Add IVS
* Update copyright year
* Add RDS::GlobalCluster per 2020-11-05 update
* Add IoT::DomainConfiguration per 2020-11-05 update
* Add Events::Archive per 2020-11-05 update
* Updates to AWS::Lambda EventSourceMapping
* Updates for EC2::Route
* Updates to Batch::JobDefinition per 2020-11-05 updates
* Update CodeArtifact per 2020-11-05 changes
* Update AppMesh per 2020-11-12 changes
* Update EC2::VPCEndpointService per 2020-11-12 changes
* Add S3::StorageLens per 2020-11-19 changes
* Add NetworkFirewall per 2020-11-19 changes
* Update Glue per 2020-11-19 changes
* Update CloudFront per 2020-11-19 changes
* Update KMS per 2020-11-19 changes
* Update Events per 2020-11-19 changes
* Update EC2 per 2020-11-19 changes
* Update Amplify per 2020-11-19 changes
* Update Lambda per 2020-11-23 changes
* Update GameList per 2020-11-24 changes
* Update EKS per 2020-12-17 changes
* Update SSO per 2020-12-18 changes
* Add IoT::TopicRuleDestination per 2020-12-18 changes
* Move "make release-test" to use python-3.9

2.6.3 (2020*10*11)
------------------
* SageMaker: Mark tags props as optional, per AWS documentation.
* Add c5a, c6g, and r6g to instance types in constants
* Make flake8 happy again
* AWS::ServiceCatalog::LaunchRoleConstraint.RoleArn not required (#1765)
* AWS::DocDB::DBCluster.DeletionProtection (#1748)
* AWS::KinesisFirehose::DeliveryStream BufferingHints and CompressionFormat not required in S3DestinationConfigurations (#1766)
* AWS::KinesisFirehose::DeliveryStream.ElasticsearchDestinationConfiguration.TypeName not required (#1767)
* AWS::StepFunctions::StateMachine DefinitionString and S3Location.Version not required (#1768)
* Add AWS::EC2::SecurityGroup.Ingress.SourcePrefixListId to SecurityGroupRule (#1762)
* AWS::Elasticsearch::Domain.AdvancedSecurityOptions (#1775)
* AWS::Glue::Connection.ConnectionInput.ConnectionType AllowedValues expansion (#1777)
* Add additional properties to KinesisEvent
* Change OnFailure and OnSuccess as not required per CloudFormation reference
* Add AWS::Serverless::Api's Domain
* Support for OpenApiVersion in serverless.Api
* add efs backupPolicy
* Fix some flake8 errors
* Add ECS Fargate EFS mounting capability
* Add new instance types to constants
* Added SSM Parameter examples (#1770)
* Update SecretsManager per 2020-07-23 update and alphabetize cleanups
* Update SageMaker::EndpointConfig per 2020-07-23 update
* Update CodeStarConnections::Connection per 2020-07-23 update
* Update CloudFront::Distribution per 2020-07-23 update
* Add ECR ImageScanningConfiguration and ImageTagMutability (Fixes #1544)
* AWS::EKS::Nodegroup.LaunchTemplate (#1780)
* AWS::SecretsManager::RotationSchedule.RotationLambdaARN not required (#1783)
* Fix capitalization in AwsVpcConfiguration (#1788)
* AWS::StepFunctions::StateMachine.TracingConfiguration (#1795)
* AppMesh Gateway support (#1758)
* fixing tags data type (#1785)
* Added Types to EndpointConfiguration (#1793)
* update TargetGroup.TargetType to support Ref values (#1794)
* Run tests against Python 3.9 (#1790)
* Cloudfront cache and origin policy (#1796)
* Fix typo AWSOject => AWSObject
* Remove list for Tags attribute
* Remove trailing blank line from serverless.py
* Update CodeGuruProfiler per 2020-07-30
* Add Mtu to GroundStation::DataflowEndpoint per 2020-07-30 changes
* Update EC2::FlowLog per 2020-07-30 changes
* Add AutoImportPolicy to FSx::LustreConfiguration per 2020-08-06
* Add BuildBatchConfig to CodeBuild::Project per 2020-08-06 changes
* Revert "Fix capitalization in AwsVpcConfiguration (#1788)" (#1798)
* Add EC2::CarrierGateway per 2020-08-13 changes
* Add new ApplicationInsights::Application per 2020-08-13 changes
* Tweaks to the gen.py script
* Add SageMaker::MonitoringSchedule from 2020-08-13 changes
* Add SecurityPolicy to Transfer::Server from 2020-08-13 changes
* Add Topics to Lambda::EventSourceMapping from 2020-08-13 changes
* Add DriveCacheType to FSx LustreConfiguration from 2020-08-13 changes
* Add EnvironmentFiles to ECS::TaskDefinition from 2020-08-13 changes
* Update Route53Resolver per 2020-08-27 changes
* Update GameLift resources per 2020-08-27
* Update ServiceCatalog per 2020-08-27 changes
* Update CodeCommit per 2020-08-31 changes
* Add EKS::FargateProfile per 2020-09-03 changes
* Add AWS::CodeGuruReviewer per 2020-09-03 changes
* Add CloudFront::RealtimeLogConfig per 2020-09-03 changes
* Add AWS::Kendra per 2020-09-10 changes
* Add AWS::SSO per 2020-09-10 changes
* Add IoT::Authorizer per 2020-09-10 changes
* Add DeleteReports to CodeBuild::ReportGroup per 2020-09-10 changes
* AWS::Synthetics::Canary.RuntimeVersion AllowedValues expansion (#1801)
* Update ApiGatewayV2::Authorizer per 2020-09-10 changes
* Add CloudFormation::StackSet per 2020-09-17 changes
* Add AWS::AppFlow per 2020-09-17 changes
* Add DisableExecuteApiEndpoint to ApiGatewayV2::Api per 2020-09-17 changes
* Add MutualTlsAuthentication to ApiGateway::DomainName per 2020-09-17 changes
* Add MutualTlsAuthentication to ApiGatewayV2::DomainName per 2020-09-17 changes
* AWS::MSK::Cluster.ClientAuthentication.Sasl (#1802)
* Add WorkSpaces::ConnectionAlias per 2020-10-01 changes
* Fix formatting in MSK
* Update AWS::Batch per 2020-10-01 changes
* Add CapacityProviderStrategy to ECS::Service per 2020-10-01 changes
* Remove duplicate elasticache NodeGroupConfiguration property (Fixes #1803)
* Add AWS::Timestream per 2020-10-08 changes
* Add AWS::CodeArtifact per 2020-10-08 changes
* Update Backup per 2020-10-08 changes
* Update AmazonMQ per 2020-10-08 changes
* Update EKS per 2020-10-08 changes
* AWS::AutoScaling::AutoScalingGroup.NewInstancesProtectedFromScaleIn (#1804)
* Improve grammar on install steps (#1800)
* Update DLM to support cross region copy (Fixes #1799)
* Update WAFv2 per 2020-0723 changes (Fixes #1797)
* Update ECR::Repository.ImageScanningConfiguration to output the correct json (Fixes #1791)

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
* Adds 'ErrorOutputPrefix' to *S3DestinationConfiguration* (#1439)
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
