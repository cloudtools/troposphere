# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

import json
import os
from re import compile


if os.getenv("TROPO_REAL_BOOL") in ['1', 'true', 'True']:
    def boolean(x):
        if x in [True, 1, '1', 'true', 'True']:
            return True
        if x in [False, 0, '0', 'false', 'False']:
            return False
        raise ValueError
else:
    def boolean(x):
        if x in [True, 1, '1', 'true', 'True']:
            return "true"
        if x in [False, 0, '0', 'false', 'False']:
            return "false"
        raise ValueError


def integer(x):
    try:
        int(x)
    except (ValueError, TypeError):
        raise ValueError("%r is not a valid integer" % x)
    else:
        return x


def positive_integer(x):
    p = integer(x)
    if int(p) < 0:
        raise ValueError("%r is not a positive integer" % x)
    return x


def integer_range(minimum_val, maximum_val):
    def integer_range_checker(x):
        i = int(x)
        if i < minimum_val or i > maximum_val:
            raise ValueError('Integer must be between %d and %d' % (
                minimum_val, maximum_val))
        return x

    return integer_range_checker


def integer_list_item(allowed_values):
    def integer_list_item_checker(x):
        i = int(x)
        if i in allowed_values:
            return x
        raise ValueError('Integer must be one of following: %s' %
                         ', '.join(str(j) for j in allowed_values))

    return integer_list_item_checker


def double(x):
    try:
        float(x)
    except (ValueError, TypeError):
        raise ValueError("%r is not a valid double" % x)
    else:
        return x


def ignore(x):
    """Method to indicate bypassing property validation"""
    return x


def defer(x):
    """Method to indicate defering property validation"""
    return x


def network_port(x):
    from . import AWSHelperFn

    # Network ports can be Ref items
    if isinstance(x, AWSHelperFn):
        return x

    i = integer(x)
    if int(i) < -1 or int(i) > 65535:
        raise ValueError("network port %r must been between 0 and 65535" % i)
    return x


def tg_healthcheck_port(x):
    if isinstance(x, str) and x == "traffic-port":
        return x
    return network_port(x)


def s3_bucket_name(b):

    # consecutive periods not allowed

    if '..' in b:
        raise ValueError("%s is not a valid s3 bucket name" % b)

    # IP addresses not allowed

    ip_re = compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    if ip_re.match(b):
        raise ValueError("%s is not a valid s3 bucket name" % b)

    s3_bucket_name_re = compile(r'^[a-z\d][a-z\d\.-]{1,61}[a-z\d]$')
    if s3_bucket_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid s3 bucket name" % b)


def elb_name(b):
    elb_name_re = compile(r'^[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,30}[a-zA-Z0-9]{1})?$')  # noqa
    if elb_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid elb name" % b)


def encoding(encoding):
    valid_encodings = ['plain', 'base64']
    if encoding not in valid_encodings:
        raise ValueError('Encoding needs to be one of %r' % valid_encodings)
    return encoding


def status(status):
    valid_statuses = ['Active', 'Inactive']
    if status not in valid_statuses:
        raise ValueError('Status needs to be one of %r' % valid_statuses)
    return status


def s3_transfer_acceleration_status(value):
    valid_status = ['Enabled', 'Suspended']
    if value not in valid_status:
        raise ValueError(
            'AccelerationStatus must be one of: "%s"' % (
                ', '.join(valid_status)
            )
        )
    return value


def iam_names(b):
    iam_name_re = compile(r'^[a-zA-Z0-9_\.\+\=\@\-\,]+$')
    if iam_name_re.match(b):
        return b
    else:
        raise ValueError("%s is not a valid iam name" % b)


def iam_user_name(user_name):
    if not user_name:
        raise ValueError(
            "AWS::IAM::User property 'UserName' may not be empty")

    if len(user_name) > 64:
        raise ValueError(
            "AWS::IAM::User property 'UserName' may not exceed 64 characters")

    iam_user_name_re = compile(r'^[\w+=,.@-]+$')
    if iam_user_name_re.match(user_name):
        return user_name
    else:
        raise ValueError(
            "%s is not a valid value for AWS::IAM::User property 'UserName'",
            user_name)


def iam_path(path):
    if len(path) > 512:
        raise ValueError('IAM path %s may not exceed 512 characters', path)

    iam_path_re = compile(r'^\/.*\/$|^\/$')
    if not iam_path_re.match(path):
        raise ValueError("%s is not a valid iam path name" % path)
    return path


def iam_role_name(role_name):
    if len(role_name) > 64:
        raise ValueError('IAM Role Name may not exceed 64 characters')
    iam_names(role_name)
    return role_name


def iam_group_name(group_name):
    if len(group_name) > 128:
        raise ValueError('IAM Role Name may not exceed 128 characters')
    iam_names(group_name)
    return group_name


def one_of(class_name, properties, property, conditionals):
    if properties.get(property) not in conditionals:
        raise ValueError(
            # Ensure we handle None as a valid value
            '%s.%s must be one of: "%s"' % (
                class_name, property, ', '.join(
                    condition for condition in conditionals if condition
                )
            )
        )


def mutually_exclusive(class_name, properties, conditionals):
    from . import NoValue

    found_list = []
    for c in conditionals:
        if c in properties and not properties[c] == NoValue:
            found_list.append(c)
    seen = set(found_list)
    specified_count = len(seen)
    if specified_count > 1:
        raise ValueError(('%s: only one of the following'
                          ' can be specified: %s') % (
            class_name, ', '.join(conditionals)))
    return specified_count


def exactly_one(class_name, properties, conditionals):
    specified_count = mutually_exclusive(class_name, properties, conditionals)
    if specified_count != 1:
        raise ValueError(('%s: one of the following'
                          ' must be specified: %s') % (
            class_name, ', '.join(conditionals)))
    return specified_count


def check_required(class_name, properties, conditionals):
    for c in conditionals:
        if c not in properties:
            raise ValueError("Resource %s required in %s" % (c, class_name))


def json_checker(prop):
    from . import AWSHelperFn

    if isinstance(prop, basestring):
        # Verify it is a valid json string
        json.loads(prop)
        return prop
    elif isinstance(prop, dict):
        # Convert the dict to a basestring
        return json.dumps(prop)
    elif isinstance(prop, AWSHelperFn):
        return prop
    else:
        raise ValueError("json object must be a str or dict")


def notification_type(notification):
    valid_notifications = ['Command', 'Invocation']
    if notification not in valid_notifications:
        raise ValueError(
            'NotificationType must be one of: "%s"' % (
                ', '.join(valid_notifications)
            )
        )
    return notification


def notification_event(events):
    valid_events = ['All', 'InProgress', 'Success', 'TimedOut', 'Cancelled',
                    'Failed']
    for event in events:
        if event not in valid_events:
            raise ValueError(
                'NotificationEvents must be at least one of: "%s"' % (
                    ', '.join(valid_events)
                )
            )
    return events


def task_type(task):
    valid_tasks = ['RUN_COMMAND', 'AUTOMATION', 'LAMBDA', 'STEP_FUNCTION']
    if task not in valid_tasks:
        raise ValueError(
            'TaskType must be one of: "%s"' % (
                ', '.join(valid_tasks)
            )
        )
    return task


def compliance_level(level):
    valid_levels = ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFORMATIONAL',
                    'UNSPECIFIED']
    if level not in valid_levels:
        raise ValueError(
            'ApprovedPatchesComplianceLevel must be one of: "%s"' % (
                ', '.join(valid_levels)
            )
        )
    return level


def operating_system(os):
    valid_os = ['WINDOWS', 'AMAZON_LINUX', 'AMAZON_LINUX_2', 'UBUNTU',
                'REDHAT_ENTERPRISE_LINUX', 'SUSE', 'CENTOS']
    if os not in valid_os:
        raise ValueError(
            'OperatingSystem must be one of: "%s"' % (
                ', '.join(valid_os)
            )
        )
    return os


def vpn_pre_shared_key(key):
    pre_shared_key_match_re = compile(
        r'^(?!0)([A-Za-z0-9]|\_|\.){8,64}$'
    )
    if not pre_shared_key_match_re.match(key):
        raise ValueError(
            '%s is not a valid key.'
            ' Allowed characters are alphanumeric characters and ._. Must'
            ' be between 8 and 64 characters in length and cannot'
            ' start with zero (0).' % key
        )
    return(key)


def vpn_tunnel_inside_cidr(cidr):
    reserved_cidrs = [
        '169.254.0.0/30',
        '169.254.1.0/30',
        '169.254.2.0/30',
        '169.254.3.0/30',
        '169.254.4.0/30',
        '169.254.5.0/30',
        '169.254.169.252/30'
    ]
    cidr_match_re = compile(
        r"^169\.254\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)"
        r"\.(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\/30$"
    )
    if cidr in reserved_cidrs:
        raise ValueError(
            'The following CIDR blocks are reserved and cannot be used: "%s"' %
            (', '.join(reserved_cidrs))
        )
    elif not cidr_match_re.match(cidr):
        raise ValueError(
            '%s is not a valid CIDR.'
            ' A size /30 CIDR block from the 169.254.0.0/16 must be specified.'
            % cidr)
    return(cidr)


def vpc_endpoint_type(endpoint_type):
    valid_types = ['Interface', 'Gateway']
    if endpoint_type not in valid_types:
        raise ValueError(
            'VpcEndpointType must be one of: "%s"' % (
                ', '.join(valid_types)
            )
        )
    return(endpoint_type)


def scalable_dimension_type(scalable_dimension):
    valid_values = ['autoscaling:autoScalingGroup:DesiredCapacity',
                    'ecs:service:DesiredCount',
                    'ec2:spot-fleet-request:TargetCapacity',
                    'rds:cluster:ReadReplicaCount',
                    'dynamodb:table:ReadCapacityUnits',
                    'dynamodb:table:WriteCapacityUnits',
                    'dynamodb:index:ReadCapacityUnits',
                    'dynamodb:index:WriteCapacityUnits'
                    ]
    if scalable_dimension not in valid_values:
        raise ValueError(
            'ScalableDimension must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(scalable_dimension)


def service_namespace_type(service_namespace):
    valid_values = ['autoscaling', 'ecs', 'ec2', 'rds', 'dynamodb']
    if service_namespace not in valid_values:
        raise ValueError(
            'ServiceNamespace must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(service_namespace)


def statistic_type(statistic):
    valid_values = ['Average', 'Minimum', 'Maximum',
                    'SampleCount', 'Sum'
                    ]
    if statistic not in valid_values:
        raise ValueError(
            'Statistic must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(statistic)


def key_usage_type(key):
    valid_values = ['ENCRYPT_DECRYPT']
    if key not in valid_values:
        raise ValueError(
            'KeyUsage must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(key)


def cloudfront_event_type(event_type):
    valid_values = ['viewer-request', 'viewer-response',
                    'origin-request', 'origin-response']
    if event_type not in valid_values:
        raise ValueError(
            'EventType must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(event_type)


def cloudfront_viewer_protocol_policy(viewer_protocol_policy):
    valid_values = ['allow-all', 'redirect-to-https', 'https-only']
    if viewer_protocol_policy not in valid_values:
        raise ValueError(
            'ViewerProtocolPolicy must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(viewer_protocol_policy)


def cloudfront_restriction_type(restriction_type):
    valid_values = ['none', 'blacklist', 'whitelist']
    if restriction_type not in valid_values:
        raise ValueError(
            'RestrictionType must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(restriction_type)


def cloudfront_forward_type(forward):
    valid_values = ['none', 'all', 'whitelist']
    if forward not in valid_values:
        raise ValueError(
            'Forward must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(forward)


def cloudfront_cache_cookie_behavior(cookie_behavior):
    valid_values = ['none', 'whitelist', 'allExcept', 'all']
    if cookie_behavior not in valid_values:
        raise ValueError(
            'CookieBehavior must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(cookie_behavior)


def cloudfront_cache_header_behavior(header_behavior):
    valid_values = ['none', 'whitelist']
    if header_behavior not in valid_values:
        raise ValueError(
            'HeaderBehavior must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(header_behavior)


def cloudfront_cache_query_string_behavior(query_string_behavior):
    valid_values = ['none', 'whitelist', 'all']
    if query_string_behavior not in valid_values:
        raise ValueError(
            'QueryStringBehavior must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(query_string_behavior)


def cloudfront_origin_request_cookie_behavior(cookie_behavior):
    valid_values = ['none', 'whitelist', 'all']
    if cookie_behavior not in valid_values:
        raise ValueError(
            'CookieBehavior must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(cookie_behavior)


def cloudfront_origin_request_header_behavior(header_behavior):
    valid_values = [
        'none', 'whitelist', 'allViewer', 'allViewerAndWhitelistCloudFront']
    if header_behavior not in valid_values:
        raise ValueError(
            'HeaderBehavior must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(header_behavior)


def cloudfront_origin_request_query_string_behavior(query_string_behavior):
    valid_values = ['none', 'whitelist', 'all']
    if query_string_behavior not in valid_values:
        raise ValueError(
            'QueryStringBehavior must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(query_string_behavior)


def priceclass_type(price_class):
    valid_values = ['PriceClass_100', 'PriceClass_200',
                    'PriceClass_All']
    if price_class not in valid_values:
        raise ValueError(
            'PriceClass must be one of: "%s"' % (
                ', '.join(valid_values)
            )
        )
    return(price_class)


def ecs_proxy_type(proxy_type):
    valid_types = ['APPMESH']
    if proxy_type not in valid_types:
        raise ValueError(
            'Type must be one of: "%s"' % (
                ', '.join(valid_types)
            )
        )
    return(proxy_type)


def backup_vault_name(name):
    vault_name_re = compile(r'^[a-zA-Z0-9\-\_\.]{1,50}$')  # noqa
    if vault_name_re.match(name):
        return name
    else:
        raise ValueError("%s is not a valid backup vault name" % name)


def waf_action_type(action):
    valid_actions = ['ALLOW', 'BLOCK', 'COUNT']
    if action not in valid_actions:
        raise ValueError(
            'Type must be one of: "%s"' % (
                ', '.join(valid_actions)
            )
        )
    return action


def resourcequery_type(type):
    valid_types = ['TAG_FILTERS_1_0', 'CLOUDFORMATION_STACK_1_0']
    if type not in valid_types:
        raise ValueError(
            'Type must be one of: "%s"' % (
                ', '.join(valid_types)
            )
        )
    return type


def storage_type(storage_type):
    valid_storage_types = ['SSD', 'HDD']
    if storage_type not in valid_storage_types:
        raise ValueError(
            'StorageType must be one of: "%s"' % (
                ', '.join(valid_storage_types)
            )
        )
    return storage_type


def canary_runtime_version(runtime_version):
    valid_runtime_versions = [
        'syn-nodejs-2.0', 'syn-nodejs-2.0-beta', 'syn-1.0']
    if runtime_version not in valid_runtime_versions:
        raise ValueError(
            'RuntimeVersion must be one of: "%s"' % (
                ', '.join(valid_runtime_versions)
            )
        )
    return(runtime_version)


def component_platforms(component_platform):
    valid_component_platforms = ['Linux', 'Windows']
    if component_platform not in valid_component_platforms:
        raise ValueError(
            'Platform must be one of: "%s"' % (
                ', '.join(valid_component_platforms)
            )
        )
    return component_platform


def imagepipeline_status(status):
    valid_status = ['DISABLED', 'ENABLED']
    if status not in valid_status:
        raise ValueError(
            'Status must be one of: "%s"' % (
                ', '.join(valid_status)
            )
        )
    return status


def schedule_pipelineexecutionstartcondition(startcondition):
    valid_startcondition = [
        'EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE',
        'EXPRESSION_MATCH_ONLY']
    if startcondition not in valid_startcondition:
        raise ValueError(
            'PipelineExecutionStartCondition must be one of: "%s"' % (
                ', '.join(valid_startcondition)
            )
        )
    return startcondition


def ebsinstanceblockdevicespecification_volume_type(type):
    valid_types = ['gp2', 'io1', 'sc1', 'st1', 'standard']
    if type not in valid_types:
        raise ValueError(
            'VolumeType must be one of: "%s"' % (
                ', '.join(valid_types)
            )
        )
    return type


def containerlevelmetrics_status(status):
    valid_status = ['DISABLED', 'ENABLED']
    if status not in valid_status:
        raise ValueError(
            'ContainerLevelMetrics must be one of: "%s"' % (
                ', '.join(valid_status)
            )
        )
    return status


def accelerator_ipaddresstype(type):
    valid_types = ['IPV4']
    if type not in valid_types:
        raise ValueError(
            'IpAddressType must be one of: "%s"' % (
                ', '.join(valid_types)
            )
        )
    return type


def listener_clientaffinity(affinity):
    valid_affinities = ['NONE', 'SOURCE_IP']
    if affinity not in valid_affinities:
        raise ValueError(
            'ClientAffinity must be one of: "%s"' % (
                ', '.join(valid_affinities)
            )
        )
    return affinity


def listener_protocol(protocol):
    valid_protocols = ['TCP', 'UDP']
    if protocol not in valid_protocols:
        raise ValueError(
            'Protocol must be one of: "%s"' % (
                ', '.join(valid_protocols)
            )
        )
    return protocol


def endpointgroup_healthcheckprotocol(protocol):
    valid_protocols = ['HTTP', 'HTTPS', 'TCP']
    if protocol not in valid_protocols:
        raise ValueError(
            'HealthCheckProtocol must be one of: "%s"' % (
                ', '.join(valid_protocols)
            )
        )
    return protocol


def session_findingpublishingfrequency(frequency):
    valid_frequencies = ['FIFTEEN_MINUTES',
                         'ONE_HOUR', 'SIX_HOURS']
    if frequency not in valid_frequencies:
        raise ValueError(
            'FindingPublishingFrequency must be one of: "%s"' % (
                ', '.join(valid_frequencies)
            )
        )
    return frequency


def session_status(status):
    valid_status = ['ENABLED', 'DISABLED']
    if status not in valid_status:
        raise ValueError(
            'Status must be one of: "%s"' % (
                ', '.join(valid_status)
            )
        )
    return status


def findingsfilter_action(action):
    valid_actions = ['ARCHIVE', 'NOOP']
    if action not in valid_actions:
        raise ValueError(
            'Action must be one of: "%s"' % (
                ', '.join(valid_actions)
            )
        )
    return action


def ecs_efs_encryption_status(status):
    valid_status = ['ENABLED', 'DISABLED']
    if status not in valid_status:
        raise ValueError(
            'ECS EFS Encryption in transit can only be one of' % (
                ', '.join(valid_status))
        )
