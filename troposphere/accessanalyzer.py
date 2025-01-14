# Copyright (c) 2012-2024, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer


class AnalysisRuleCriteria(AWSProperty):
    """
    `AnalysisRuleCriteria <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analysisrulecriteria.html>`__
    """

    props: PropsDictType = {
        "AccountIds": ([str], False),
        "ResourceTags": (dict, False),
    }


class AnalysisRule(AWSProperty):
    """
    `AnalysisRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analysisrule.html>`__
    """

    props: PropsDictType = {
        "Exclusions": ([AnalysisRuleCriteria], False),
    }


class UnusedAccessConfiguration(AWSProperty):
    """
    `UnusedAccessConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-unusedaccessconfiguration.html>`__
    """

    props: PropsDictType = {
        "AnalysisRule": (AnalysisRule, False),
        "UnusedAccessAge": (integer, False),
    }


class AnalyzerConfiguration(AWSProperty):
    """
    `AnalyzerConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-analyzerconfiguration.html>`__
    """

    props: PropsDictType = {
        "UnusedAccessConfiguration": (UnusedAccessConfiguration, False),
    }


class Filter(AWSProperty):
    """
    `Filter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-filter.html>`__
    """

    props: PropsDictType = {
        "Contains": ([str], False),
        "Eq": ([str], False),
        "Exists": (boolean, False),
        "Neq": ([str], False),
        "Property": (str, True),
    }


class ArchiveRule(AWSProperty):
    """
    `ArchiveRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-accessanalyzer-analyzer-archiverule.html>`__
    """

    props: PropsDictType = {
        "Filter": ([Filter], True),
        "RuleName": (str, True),
    }


class Analyzer(AWSObject):
    """
    `Analyzer <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-accessanalyzer-analyzer.html>`__
    """

    resource_type = "AWS::AccessAnalyzer::Analyzer"

    props: PropsDictType = {
        "AnalyzerConfiguration": (AnalyzerConfiguration, False),
        "AnalyzerName": (str, False),
        "ArchiveRules": ([ArchiveRule], False),
        "Tags": (Tags, False),
        "Type": (str, True),
    }
