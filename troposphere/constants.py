#
# Regions
#

AP_NORTHEAST_1 = 'ap-northeast-1'
AP_NORTHEAST_2 = 'ap-northeast-2'
AP_SOUTHEAST_1 = 'ap-southeast-1'
AP_SOUTHEAST_2 = 'ap-southeast-2'
EU_WEST_1 = 'eu-west-1'
EU_WEST_2 = 'eu-west-2'
EU_CENTRAL_1 = 'eu-central-1'
SA_EAST_1 = 'sa-east-1'
US_EAST_1 = 'us-east-1'
US_WEST_1 = 'us-west-1'
US_WEST_2 = 'us-west-2'

#
# Availability Zones
#

AP_NORTHEAST_1A = 'ap-northeast-1a'
AP_NORTHEAST_1B = 'ap-northeast-1b'
AP_NORTHEAST_1C = 'ap-northeast-1c'

AP_NORTHEAST_2A = 'ap-northeast-2a'
AP_NORTHEAST_2B = 'ap-northeast-2b'
AP_NORTHEAST_2C = 'ap-northeast-2c'

AP_SOUTHEAST_1A = 'ap-southeast-1a'
AP_SOUTHEAST_1B = 'ap-southeast-1b'

AP_SOUTHEAST_2A = 'ap-southeast-2a'
AP_SOUTHEAST_2B = 'ap-southeast-2b'
AP_SOUTHEAST_2C = 'ap-southeast-2c'

EU_WEST_1A = 'eu-west-1a'
EU_WEST_1B = 'eu-west-1b'
EU_WEST_1C = 'eu-west-1c'

EU_WEST_2A = 'eu-west-2a'
EU_WEST_2B = 'eu-west-2b'

EU_CENTRAL_1A = 'eu-central-1a'
EU_CENTRAL_1B = 'eu-central-1b'

SA_EAST_1A = 'sa-east-1a'
SA_EAST_1B = 'sa-east-1b'
SA_EAST_1C = 'sa-east-1c'

US_EAST_1A = 'us-east-1a'
US_EAST_1B = 'us-east-1b'
US_EAST_1C = 'us-east-1c'
US_EAST_1D = 'us-east-1d'
US_EAST_1E = 'us-east-1e'

US_WEST_1A = 'us-west-1a'
US_WEST_1B = 'us-west-1b'
US_WEST_1C = 'us-west-1c'

US_WEST_2A = 'us-west-2a'
US_WEST_2B = 'us-west-2b'
US_WEST_2C = 'us-west-2c'

#
# Networking
#

QUAD_ZERO = '0.0.0.0/0'
VPC_CIDR_16 = '10.0.0.0/16'

SSH_PORT = 22
MONGODB_PORT = 27017
NTP_PORT = 123
SMTP_PORT_25 = 25
SMTP_PORT_587 = 587
HTTP_PORT = 80
HTTPS_PORT = 443
REDIS_PORT = 6379
MEMCACHED_PORT = 11211
POSTGRESQL_PORT = 5432

TCP_PROTOCOL = 6
UDP_PROTOCOL = 17
ICMP_PROTOCOL = 1
ALL_PROTOCOL = -1

#
# EC2 instance types
#

T2_NANO = 't2.nano'
T2_MICRO = 't2.micro'
T2_SMALL = 't2.small'
T2_MEDIUM = 't2.medium'
T2_LARGE = 't2.large'
T2_XLARGE = 't2.xlarge'
T2_2XLARGE = 't2.2xlarge'

M5_LARGE = 'm5.large'
M5_XLARGE = 'm5.xlarge'
M5_2XLARGE = 'm5.2xlarge'
M5_4XLARGE = 'm5.4xlarge'
M5_12XLARGE = 'm5.12xlarge'
M5_24XLARGE = 'm5.24xlarge'

M4_LARGE = 'm4.large'
M4_XLARGE = 'm4.xlarge'
M4_2XLARGE = 'm4.2xlarge'
M4_4XLARGE = 'm4.4xlarge'
M4_10XLARGE = 'm4.10xlarge'
M4_16XLARGE = 'm4.16xlarge'

M3_MEDIUM = 'm3.medium'
M3_LARGE = 'm3.large'
M3_XLARGE = 'm3.xlarge'
M3_2XLARGE = 'm3.2xlarge'

C3_LARGE = 'c3.large'
C3_XLARGE = 'c3.xlarge'
C3_2XLARGE = 'c3.2xlarge'
C3_4XLARGE = 'c3.4xlarge'
C3_8XLARGE = 'c3.8xlarge'

C4_LARGE = 'c4.large'
C4_XLARGE = 'c4.xlarge'
C4_2XLARGE = 'c4.2xlarge'
C4_4XLARGE = 'c4.4xlarge'
C4_8XLARGE = 'c4.8xlarge'

R3_LARGE = 'r3.large'
R3_XLARGE = 'r3.xlarge'
R3_2XLARGE = 'r3.2xlarge'
R3_4XLARGE = 'r3.4xlarge'
R3_8XLARGE = 'r3.8xlarge'

G2_2XLARGE = 'g2.2xlarge'
G2_8XLARGE = 'g2.8xlarge'

I2_XLARGE = 'i2.xlarge'
I2_2XLARGE = 'i2.2xlarge'
I2_4XLARGE = 'i2.4xlarge'
I2_8XLARGE = 'i2.8xlarge'

D2_XLARGE = 'd2.xlarge'
D2_2XLARGE = 'd2.2xlarge'
D2_4XLARGE = 'd2.4xlarge'
D2_8XLARGE = 'd2.8xlarge'

HS1_8XLARGE = 'hs1.8xlarge'

M1_SMALL = 'm1.small'
M1_MEDIUM = 'm1.medium'
M1_LARGE = 'm1.large'
M1_XLARGE = 'm1.xlarge'

C1_MEDIUM = 'c1.medium'
C1_XLARGE = 'c1.xlarge'
CC2_8XLARGE = 'cc2.8xlarge'

CG1_4XLARGE = 'cg1.4xlarge'

M2_XLARGE = 'm2.xlarge'
M2_2XLARGE = 'm2.2xlarge'
M2_4XLARGE = 'm2.4xlarge'
CR1_8XLARGE = 'cr1.8xlarge'

HI1_4XLARGE = 'hi1.4xlarge'

T1_MICRO = 't1.micro'

X1_32XLARGE = 'x1.32xlarge'
X1_16XLARGE = 'x1.16xlarge'

R4_LARGE = 'r4.large'
R4_XLARGE = 'r4.xlarge'
R4_2XLARGE = 'r4.2xlarge'
R4_4XLARGE = 'r4.4xlarge'
R4_8XLARGE = 'r4.8xlarge'
R4_16XLARGE = 'r4.16xlarge'

P2_XLARGE = 'p2.xlarge'
P2_8XLARGE = 'p2.8xlarge'
P2_16XLARGE = 'p2.16xlarge'

F1_2XLARGE = 'f1.2xlarge'
F1_16XLARGE = 'f1.16xlarge'

I3_LARGE = 'i3.large'
I3_XLARGE = 'i3.xlarge'
I3_2XLARGE = 'i3.2xlarge'
I3_4XLARGE = 'i3.4xlarge'
I3_8XLARGE = 'i3.8xlarge'
I3_16XLARGE = 'i3.16xlarge'

#
# RDS DB instance classes
#

DB_M3_MEDIUM = 'db.m3.medium'
DB_M3_LARGE = 'db.m3.large'
DB_M3_XLARGE = 'db.m3.xlarge'
DB_M3_2XLARGE = 'db.m3.2xlarge'

DB_R3_LARGE = 'db.r3.large'
DB_R3_XLARGE = 'db.r3.xlarge'
DB_R3_2XLARGE = 'db.r3.2xlarge'
DB_R3_4XLARGE = 'db.r3.4xlarge'
DB_R3_8XLARGE = 'db.r3.8xlarge'

DB_T2_MICRO = 'db.t2.micro'
DB_T2_SMALL = 'db.t2.small'
DB_T2_MEDIUM = 'db.t2.medium'

DB_M1_SMALL = 'db.m1.small'
DB_M1_MEDIUM = 'db.m1.medium'
DB_M1_LARGE = 'db.m1.large'
DB_M1_XLARGE = 'db.m1.xlarge'

DB_M2_XLARGE = 'db.m2.xlarge'
DB_M2_2XLARGE = 'db.m2.2xlarge'
DB_M2_4XLARGE = 'db.m2.4xlarge'
DB_CR1_8XLARGE = 'db.cr1.8xlarge'

DB_T1_MICRO = 'db.t1.micro'

#
# ElastiCache node types
#

CACHE_T2_MICRO = 'cache.t2.micro'
CACHE_T2_SMALL = 'cache.t2.small'
CACHE_T2_MEDIUM = 'cache.t2.medium'

CACHE_M3_MEDIUM = 'cache.m3.medium'
CACHE_M3_LARGE = 'cache.m3.large'
CACHE_M3_XLARGE = 'cache.m3.xlarge'
CACHE_M3_2XLARGE = 'cache.m3.2xlarge'

CACHE_R3_LARGE = 'cache.r3.large'
CACHE_R3_XLARGE = 'cache.r3.xlarge'
CACHE_R3_2XLARGE = 'cache.r3.2xlarge'
CACHE_R3_4XLARGE = 'cache.r3.4xlarge'
CACHE_R3_8XLARGE = 'cache.r3.8xlarge'

CACHE_M1_SMALL = 'cache.m1.small'
CACHE_M1_MEDIUM = 'cache.m1.medium'
CACHE_M1_LARGE = 'cache.m1.large'
CACHE_M1_XLARGE = 'cache.m1.xlarge'

CACHE_M2_XLARGE = 'cache.m2.xlarge'
CACHE_M2_2XLARGE = 'cache.m2.2xlarge'
CACHE_M2_4XLARGE = 'cache.m2.4xlarge'

CACHE_C1_XLARGE = 'cache.c1.xlarge'

CACHE_T1_MICRO = 'cache.t1.micro'

#
# Elasticsearch instance types
#

ELASTICSEARCH_T2_MICRO = 't2.micro.elasticsearch'
ELASTICSEARCH_T2_SMALL = 't2.small.elasticsearch'
ELASTICSEARCH_T2_MEDIUM = 't2.medium.elasticsearch'

ELASTICSEARCH_M3_MEDIUM = 'm3.medium.elasticsearch'
ELASTICSEARCH_M3_LARGE = 'm3.large.elasticsearch'
ELASTICSEARCH_M3_XLARGE = 'm3.xlarge.elasticsearch'
ELASTICSEARCH_M3_2XLARGE = 'm3.2xlarge.elasticsearch'

ELASTICSEARCH_M4_LARGE = 'm4.large.elasticsearch'
ELASTICSEARCH_M4_XLARGE = 'm4.xlarge.elasticsearch'
ELASTICSEARCH_M4_2XLARGE = 'm4.2xlarge.elasticsearch'
ELASTICSEARCH_M4_4XLARGE = 'm4.4xlarge.elasticsearch'
ELASTICSEARCH_M4_10XLARGE = 'm4.10xlarge.elasticsearch'

ELASTICSEARCH_C4_LARGE = 'c4.large.elasticsearch'
ELASTICSEARCH_C4_XLARGE = 'c4.xlarge.elasticsearch'
ELASTICSEARCH_C4_2XLARGE = 'c4.2xlarge.elasticsearch'
ELASTICSEARCH_C4_4XLARGE = 'c4.4xlarge.elasticsearch'
ELASTICSEARCH_C4_8XLARGE = 'c4.8xlarge.elasticsearch'

ELASTICSEARCH_R3_LARGE = 'r3.large.elasticsearch'
ELASTICSEARCH_R3_XLARGE = 'r3.xlarge.elasticsearch'
ELASTICSEARCH_R3_2XLARGE = 'r3.2xlarge.elasticsearch'
ELASTICSEARCH_R3_4XLARGE = 'r3.4xlarge.elasticsearch'
ELASTICSEARCH_R3_8XLARGE = 'r3.8xlarge.elasticsearch'

ELASTICSEARCH_R4_LARGE = 'r4.large.elasticsearch'
ELASTICSEARCH_R4_XLARGE = 'r4.xlarge.elasticsearch'
ELASTICSEARCH_R4_2XLARGE = 'r4.2xlarge.elasticsearch'
ELASTICSEARCH_R4_4XLARGE = 'r4.4xlarge.elasticsearch'
ELASTICSEARCH_R4_8XLARGE = 'r4.8xlarge.elasticsearch'
ELASTICSEARCH_R4_16XLARGE = 'r4.16xlarge.elasticsearch'

ELASTICSEARCH_I2_XLARGE = 'i2.xlarge.elasticsearch'
ELASTICSEARCH_I2_2XLARGE = 'i2.2xlarge.elasticsearch'

#
# Parameter types
#

STRING = 'String'
NUMBER = 'Number'
LIST_OF_NUMBERS = 'List<Number>'
COMMA_DELIMITED_LIST = 'CommaDelimitedList'

AVAILABILITY_ZONE_NAME = 'AWS::EC2::AvailabilityZone::Name'
IMAGE_ID = 'AWS::EC2::Image::Id'
INSTANCE_ID = 'AWS::EC2::Instance::Id'
KEY_PAIR_NAME = 'AWS::EC2::KeyPair::KeyName'
SECURITY_GROUP_NAME = 'AWS::EC2::SecurityGroup::GroupName'
SECURITY_GROUP_ID = 'AWS::EC2::SecurityGroup::Id'
SUBNET_ID = 'AWS::EC2::Subnet::Id'
VOLUME_ID = 'AWS::EC2::Volume::Id'
VPC_ID = 'AWS::EC2::VPC::Id'
HOSTED_ZONE_ID = 'AWS::Route53::HostedZone::Id'

LIST_OF_AVAILABILITY_ZONE_NAMES = 'List<AWS::EC2::AvailabilityZone::Name>'
LIST_OF_IMAGE_ID = 'List<AWS::EC2::Image::Id>'
LIST_OF_INSTANCE_IDS = 'List<AWS::EC2::Instance::Id>'
LIST_OF_SECURITY_GROUP_NAMES = 'List<AWS::EC2::SecurityGroup::GroupName>'
LIST_OF_SECURITY_GROUP_IDS = 'List<AWS::EC2::SecurityGroup::Id>'
LIST_OF_SUBNET_IDS = 'List<AWS::EC2::Subnet::Id>'
LIST_OF_VOLUME_IDS = 'List<AWS::EC2::Volume::Id>'
LIST_OF_VPC_IDS = 'List<AWS::EC2::VPC::Id>'
LIST_OF_HOSTED_ZONE_IDS = 'List<AWS::Route53::HostedZone::Id>'

#
# Logs
#
LOGS_ALLOWED_RETENTION_DAYS = [1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180,
                               365, 400, 545, 731, 1827, 3653]

#
# Route53
#

CLOUDFRONT_HOSTEDZONEID = 'Z2FDTNDATAQYW2'
