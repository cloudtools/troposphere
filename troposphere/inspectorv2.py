# Copyright (c) 2012-2025, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType
from .validators import double, integer


class CisTargets(AWSProperty):
    """
    `CisTargets <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-cistargets.html>`__
    """

    props: PropsDictType = {
        "AccountIds": ([str], True),
        "TargetResourceTags": (dict, True),
    }


class Time(AWSProperty):
    """
    `Time <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-time.html>`__
    """

    props: PropsDictType = {
        "TimeOfDay": (str, True),
        "TimeZone": (str, True),
    }


class DailySchedule(AWSProperty):
    """
    `DailySchedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-dailyschedule.html>`__
    """

    props: PropsDictType = {
        "StartTime": (Time, True),
    }


class MonthlySchedule(AWSProperty):
    """
    `MonthlySchedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.html>`__
    """

    props: PropsDictType = {
        "Day": (str, True),
        "StartTime": (Time, True),
    }


class WeeklySchedule(AWSProperty):
    """
    `WeeklySchedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.html>`__
    """

    props: PropsDictType = {
        "Days": ([str], True),
        "StartTime": (Time, True),
    }


class Schedule(AWSProperty):
    """
    `Schedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html>`__
    """

    props: PropsDictType = {
        "Daily": (DailySchedule, False),
        "Monthly": (MonthlySchedule, False),
        "OneTime": (dict, False),
        "Weekly": (WeeklySchedule, False),
    }


class CisScanConfiguration(AWSObject):
    """
    `CisScanConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html>`__
    """

    resource_type = "AWS::InspectorV2::CisScanConfiguration"

    props: PropsDictType = {
        "ScanName": (str, True),
        "Schedule": (Schedule, True),
        "SecurityLevel": (str, True),
        "Tags": (dict, False),
        "Targets": (CisTargets, True),
    }


class DateFilter(AWSProperty):
    """
    `DateFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html>`__
    """

    props: PropsDictType = {
        "EndInclusive": (integer, False),
        "StartInclusive": (integer, False),
    }


class MapFilter(AWSProperty):
    """
    `MapFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html>`__
    """

    props: PropsDictType = {
        "Comparison": (str, True),
        "Key": (str, False),
        "Value": (str, False),
    }


class NumberFilter(AWSProperty):
    """
    `NumberFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html>`__
    """

    props: PropsDictType = {
        "LowerInclusive": (double, False),
        "UpperInclusive": (double, False),
    }


class StringFilter(AWSProperty):
    """
    `StringFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html>`__
    """

    props: PropsDictType = {
        "Comparison": (str, True),
        "Value": (str, True),
    }


class PackageFilter(AWSProperty):
    """
    `PackageFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html>`__
    """

    props: PropsDictType = {
        "Architecture": (StringFilter, False),
        "Epoch": (NumberFilter, False),
        "FilePath": (StringFilter, False),
        "Name": (StringFilter, False),
        "Release": (StringFilter, False),
        "SourceLambdaLayerArn": (StringFilter, False),
        "SourceLayerHash": (StringFilter, False),
        "Version": (StringFilter, False),
    }


class PortRangeFilter(AWSProperty):
    """
    `PortRangeFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html>`__
    """

    props: PropsDictType = {
        "BeginInclusive": (integer, False),
        "EndInclusive": (integer, False),
    }


class FilterCriteria(AWSProperty):
    """
    `FilterCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html>`__
    """

    props: PropsDictType = {
        "AwsAccountId": ([StringFilter], False),
        "CodeVulnerabilityDetectorName": ([StringFilter], False),
        "CodeVulnerabilityDetectorTags": ([StringFilter], False),
        "CodeVulnerabilityFilePath": ([StringFilter], False),
        "ComponentId": ([StringFilter], False),
        "ComponentType": ([StringFilter], False),
        "Ec2InstanceImageId": ([StringFilter], False),
        "Ec2InstanceSubnetId": ([StringFilter], False),
        "Ec2InstanceVpcId": ([StringFilter], False),
        "EcrImageArchitecture": ([StringFilter], False),
        "EcrImageHash": ([StringFilter], False),
        "EcrImagePushedAt": ([DateFilter], False),
        "EcrImageRegistry": ([StringFilter], False),
        "EcrImageRepositoryName": ([StringFilter], False),
        "EcrImageTags": ([StringFilter], False),
        "EpssScore": ([NumberFilter], False),
        "ExploitAvailable": ([StringFilter], False),
        "FindingArn": ([StringFilter], False),
        "FindingStatus": ([StringFilter], False),
        "FindingType": ([StringFilter], False),
        "FirstObservedAt": ([DateFilter], False),
        "FixAvailable": ([StringFilter], False),
        "InspectorScore": ([NumberFilter], False),
        "LambdaFunctionExecutionRoleArn": ([StringFilter], False),
        "LambdaFunctionLastModifiedAt": ([DateFilter], False),
        "LambdaFunctionLayers": ([StringFilter], False),
        "LambdaFunctionName": ([StringFilter], False),
        "LambdaFunctionRuntime": ([StringFilter], False),
        "LastObservedAt": ([DateFilter], False),
        "NetworkProtocol": ([StringFilter], False),
        "PortRange": ([PortRangeFilter], False),
        "RelatedVulnerabilities": ([StringFilter], False),
        "ResourceId": ([StringFilter], False),
        "ResourceTags": ([MapFilter], False),
        "ResourceType": ([StringFilter], False),
        "Severity": ([StringFilter], False),
        "Title": ([StringFilter], False),
        "UpdatedAt": ([DateFilter], False),
        "VendorSeverity": ([StringFilter], False),
        "VulnerabilityId": ([StringFilter], False),
        "VulnerabilitySource": ([StringFilter], False),
        "VulnerablePackages": ([PackageFilter], False),
    }


class Filter(AWSObject):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html>`__
    """

    resource_type = "AWS::InspectorV2::Filter"

    props: PropsDictType = {
        "Description": (str, False),
        "FilterAction": (str, True),
        "FilterCriteria": (FilterCriteria, True),
        "Name": (str, True),
        "Tags": (dict, False),
    }
