# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from . import AWSObject
from . import AWSProperty
from troposphere import Tags
from .validators import boolean
from .validators import double


class AnalysisError(AWSProperty):
    props = {
        'Message': (str, False),
        'Type': (str, False),
    }


class DataSetReference(AWSProperty):
    props = {
        'DataSetArn': (str, True),
        'DataSetPlaceholder': (str, True),
    }


class AnalysisSourceTemplate(AWSProperty):
    props = {
        'Arn': (str, True),
        'DataSetReferences': ([DataSetReference], True),
    }


class AnalysisSourceEntity(AWSProperty):
    props = {
        'SourceTemplate': (AnalysisSourceTemplate, False),
    }


class DateTimeParameter(AWSProperty):
    props = {
        'Name': (str, True),
        'Values': ([str], True),
    }


class DecimalParameter(AWSProperty):
    props = {
        'Name': (str, True),
        'Values': ([double], True),
    }


class IntegerParameter(AWSProperty):
    props = {
        'Name': (str, True),
        'Values': ([double], True),
    }


class StringParameter(AWSProperty):
    props = {
        'Name': (str, True),
        'Values': ([str], True),
    }


class Parameters(AWSProperty):
    props = {
        'DateTimeParameters': ([DateTimeParameter], False),
        'DecimalParameters': ([DecimalParameter], False),
        'IntegerParameters': ([IntegerParameter], False),
        'StringParameters': ([StringParameter], False),
    }


class ResourcePermission(AWSProperty):
    props = {
        'Actions': ([str], True),
        'Principal': (str, True),
    }


class Analysis(AWSObject):
    resource_type = "AWS::QuickSight::Analysis"

    props = {
        'AnalysisId': (str, True),
        'AwsAccountId': (str, True),
        'Errors': ([AnalysisError], False),
        'Name': (str, False),
        'Parameters': (Parameters, False),
        'Permissions': ([ResourcePermission], False),
        'SourceEntity': (AnalysisSourceEntity, False),
        'Tags': (Tags, False),
        'ThemeArn': (str, False),
    }


class AdHocFilteringOption(AWSProperty):
    props = {
        'AvailabilityStatus': (str, False),
    }


class ExportToCSVOption(AWSProperty):
    props = {
        'AvailabilityStatus': (str, False),
    }


class SheetControlsOption(AWSProperty):
    props = {
        'VisibilityState': (str, False),
    }


class DashboardPublishOptions(AWSProperty):
    props = {
        'AdHocFilteringOption': (AdHocFilteringOption, False),
        'ExportToCSVOption': (ExportToCSVOption, False),
        'SheetControlsOption': (SheetControlsOption, False),
    }


class DashboardSourceTemplate(AWSProperty):
    props = {
        'Arn': (str, True),
        'DataSetReferences': ([DataSetReference], True),
    }


class DashboardSourceEntity(AWSProperty):
    props = {
        'SourceTemplate': (DashboardSourceTemplate, False),
    }


class Dashboard(AWSObject):
    resource_type = "AWS::QuickSight::Dashboard"

    props = {
        'AwsAccountId': (str, True),
        'DashboardId': (str, True),
        'DashboardPublishOptions': (DashboardPublishOptions, False),
        'Name': (str, False),
        'Parameters': (Parameters, False),
        'Permissions': ([ResourcePermission], False),
        'SourceEntity': (DashboardSourceEntity, False),
        'Tags': (Tags, False),
        'ThemeArn': (str, False),
        'VersionDescription': (str, False),
    }


class TemplateSourceAnalysis(AWSProperty):
    props = {
        'Arn': (str, True),
        'DataSetReferences': ([DataSetReference], True),
    }


class TemplateSourceTemplate(AWSProperty):
    props = {
        'Arn': (str, True),
    }


class TemplateSourceEntity(AWSProperty):
    props = {
        'SourceAnalysis': (TemplateSourceAnalysis, False),
        'SourceTemplate': (TemplateSourceTemplate, False),
    }


class Template(AWSObject):
    resource_type = "AWS::QuickSight::Template"

    props = {
        'AwsAccountId': (str, True),
        'Name': (str, False),
        'Permissions': ([ResourcePermission], False),
        'SourceEntity': (TemplateSourceEntity, False),
        'Tags': (Tags, False),
        'TemplateId': (str, True),
        'VersionDescription': (str, False),
    }


class DataColorPalette(AWSProperty):
    props = {
        'Colors': ([str], False),
        'EmptyFillColor': (str, False),
        'MinMaxGradient': ([str], False),
    }


class GutterStyle(AWSProperty):
    props = {
        'Show': (boolean, False),
    }


class MarginStyle(AWSProperty):
    props = {
        'Show': (boolean, False),
    }


class TileLayoutStyle(AWSProperty):
    props = {
        'Gutter': (GutterStyle, False),
        'Margin': (MarginStyle, False),
    }


class BorderStyle(AWSProperty):
    props = {
        'Show': (boolean, False),
    }


class TileStyle(AWSProperty):
    props = {
        'Border': (BorderStyle, False),
    }


class SheetStyle(AWSProperty):
    props = {
        'Tile': (TileStyle, False),
        'TileLayout': (TileLayoutStyle, False),
    }


class Font(AWSProperty):
    props = {
        'FontFamily': (str, False),
    }


class Typography(AWSProperty):
    props = {
        'FontFamilies': ([Font], False),
    }


class UIColorPalette(AWSProperty):
    props = {
        'Accent': (str, False),
        'AccentForeground': (str, False),
        'Danger': (str, False),
        'DangerForeground': (str, False),
        'Dimension': (str, False),
        'DimensionForeground': (str, False),
        'Measure': (str, False),
        'MeasureForeground': (str, False),
        'PrimaryBackground': (str, False),
        'PrimaryForeground': (str, False),
        'SecondaryBackground': (str, False),
        'SecondaryForeground': (str, False),
        'Success': (str, False),
        'SuccessForeground': (str, False),
        'Warning': (str, False),
        'WarningForeground': (str, False),
    }


class ThemeConfiguration(AWSProperty):
    props = {
        'DataColorPalette': (DataColorPalette, False),
        'Sheet': (SheetStyle, False),
        'Typography': (Typography, False),
        'UIColorPalette': (UIColorPalette, False),
    }


class Theme(AWSObject):
    resource_type = "AWS::QuickSight::Theme"

    props = {
        'AwsAccountId': (str, True),
        'BaseThemeId': (str, False),
        'Configuration': (ThemeConfiguration, False),
        'Name': (str, False),
        'Permissions': ([ResourcePermission], False),
        'Tags': (Tags, False),
        'ThemeId': (str, True),
        'VersionDescription': (str, False),
    }
