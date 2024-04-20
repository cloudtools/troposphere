# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class FilterExpression(AWSProperty):
    """
    `FilterExpression <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-filterexpression.html>`__
    """

    props: PropsDictType = {
        "Expression": (str, True),
        "Type": (str, True),
    }


class RelationalFilterConfiguration(AWSProperty):
    """
    `RelationalFilterConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-relationalfilterconfiguration.html>`__
    """

    props: PropsDictType = {
        "DatabaseName": (str, True),
        "FilterExpressions": ([FilterExpression], False),
        "SchemaName": (str, False),
    }


class GlueRunConfigurationInput(AWSProperty):
    """
    `GlueRunConfigurationInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-gluerunconfigurationinput.html>`__
    """

    props: PropsDictType = {
        "AutoImportDataQualityResult": (boolean, False),
        "DataAccessRole": (str, False),
        "RelationalFilterConfigurations": ([RelationalFilterConfiguration], True),
    }


class RedshiftCredentialConfiguration(AWSProperty):
    """
    `RedshiftCredentialConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftcredentialconfiguration.html>`__
    """

    props: PropsDictType = {
        "SecretManagerArn": (str, True),
    }


class RedshiftClusterStorage(AWSProperty):
    """
    `RedshiftClusterStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftclusterstorage.html>`__
    """

    props: PropsDictType = {
        "ClusterName": (str, True),
    }


class RedshiftServerlessStorage(AWSProperty):
    """
    `RedshiftServerlessStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftserverlessstorage.html>`__
    """

    props: PropsDictType = {
        "WorkgroupName": (str, True),
    }


class RedshiftStorage(AWSProperty):
    """
    `RedshiftStorage <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftstorage.html>`__
    """

    props: PropsDictType = {
        "RedshiftClusterSource": (RedshiftClusterStorage, False),
        "RedshiftServerlessSource": (RedshiftServerlessStorage, False),
    }


class RedshiftRunConfigurationInput(AWSProperty):
    """
    `RedshiftRunConfigurationInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-redshiftrunconfigurationinput.html>`__
    """

    props: PropsDictType = {
        "DataAccessRole": (str, False),
        "RedshiftCredentialConfiguration": (RedshiftCredentialConfiguration, True),
        "RedshiftStorage": (RedshiftStorage, True),
        "RelationalFilterConfigurations": ([RelationalFilterConfiguration], True),
    }


class DataSourceConfigurationInput(AWSProperty):
    """
    `DataSourceConfigurationInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-datasourceconfigurationinput.html>`__
    """

    props: PropsDictType = {
        "GlueRunConfiguration": (GlueRunConfigurationInput, False),
        "RedshiftRunConfiguration": (RedshiftRunConfigurationInput, False),
    }


class FormInput(AWSProperty):
    """
    `FormInput <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-forminput.html>`__
    """

    props: PropsDictType = {
        "Content": (str, False),
        "FormName": (str, True),
        "TypeIdentifier": (str, False),
        "TypeRevision": (str, False),
    }


class RecommendationConfiguration(AWSProperty):
    """
    `RecommendationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-recommendationconfiguration.html>`__
    """

    props: PropsDictType = {
        "EnableBusinessNameGeneration": (boolean, False),
    }


class ScheduleConfiguration(AWSProperty):
    """
    `ScheduleConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-datasource-scheduleconfiguration.html>`__
    """

    props: PropsDictType = {
        "Schedule": (str, False),
        "Timezone": (str, False),
    }


class DataSource(AWSObject):
    """
    `DataSource <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-datasource.html>`__
    """

    resource_type = "AWS::DataZone::DataSource"

    props: PropsDictType = {
        "AssetFormsInput": ([FormInput], False),
        "Configuration": (DataSourceConfigurationInput, False),
        "Description": (str, False),
        "DomainIdentifier": (str, True),
        "EnableSetting": (str, False),
        "EnvironmentIdentifier": (str, True),
        "Name": (str, True),
        "ProjectIdentifier": (str, True),
        "PublishOnImport": (boolean, False),
        "Recommendation": (RecommendationConfiguration, False),
        "Schedule": (ScheduleConfiguration, False),
        "Type": (str, True),
    }


class SingleSignOn(AWSProperty):
    """
    `SingleSignOn <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-domain-singlesignon.html>`__
    """

    props: PropsDictType = {
        "Type": (str, False),
        "UserAssignment": (str, False),
    }


class Domain(AWSObject):
    """
    `Domain <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-domain.html>`__
    """

    resource_type = "AWS::DataZone::Domain"

    props: PropsDictType = {
        "Description": (str, False),
        "DomainExecutionRole": (str, True),
        "KmsKeyIdentifier": (str, False),
        "Name": (str, True),
        "SingleSignOn": (SingleSignOn, False),
        "Tags": (Tags, False),
    }


class EnvironmentParameter(AWSProperty):
    """
    `EnvironmentParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentprofile-environmentparameter.html>`__
    """

    props: PropsDictType = {
        "Name": (str, False),
        "Value": (str, False),
    }


class Environment(AWSObject):
    """
    `Environment <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environment.html>`__
    """

    resource_type = "AWS::DataZone::Environment"

    props: PropsDictType = {
        "Description": (str, False),
        "DomainIdentifier": (str, True),
        "EnvironmentProfileIdentifier": (str, True),
        "GlossaryTerms": ([str], False),
        "Name": (str, True),
        "ProjectIdentifier": (str, True),
        "UserParameters": ([EnvironmentParameter], False),
    }


class RegionalParameter(AWSProperty):
    """
    `RegionalParameter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-environmentblueprintconfiguration-regionalparameter.html>`__
    """

    props: PropsDictType = {
        "Parameters": (dict, False),
        "Region": (str, False),
    }


class EnvironmentBlueprintConfiguration(AWSObject):
    """
    `EnvironmentBlueprintConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentblueprintconfiguration.html>`__
    """

    resource_type = "AWS::DataZone::EnvironmentBlueprintConfiguration"

    props: PropsDictType = {
        "DomainIdentifier": (str, True),
        "EnabledRegions": ([str], True),
        "EnvironmentBlueprintIdentifier": (str, True),
        "ManageAccessRoleArn": (str, False),
        "ProvisioningRoleArn": (str, False),
        "RegionalParameters": ([RegionalParameter], False),
    }


class EnvironmentProfile(AWSObject):
    """
    `EnvironmentProfile <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-environmentprofile.html>`__
    """

    resource_type = "AWS::DataZone::EnvironmentProfile"

    props: PropsDictType = {
        "AwsAccountId": (str, True),
        "AwsAccountRegion": (str, True),
        "Description": (str, False),
        "DomainIdentifier": (str, True),
        "EnvironmentBlueprintIdentifier": (str, True),
        "Name": (str, True),
        "ProjectIdentifier": (str, True),
        "UserParameters": ([EnvironmentParameter], False),
    }


class Project(AWSObject):
    """
    `Project <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-project.html>`__
    """

    resource_type = "AWS::DataZone::Project"

    props: PropsDictType = {
        "Description": (str, False),
        "DomainIdentifier": (str, True),
        "GlossaryTerms": ([str], False),
        "Name": (str, True),
    }


class SubscriptionTargetForm(AWSProperty):
    """
    `SubscriptionTargetForm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-datazone-subscriptiontarget-subscriptiontargetform.html>`__
    """

    props: PropsDictType = {
        "Content": (str, True),
        "FormName": (str, True),
    }


class SubscriptionTarget(AWSObject):
    """
    `SubscriptionTarget <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datazone-subscriptiontarget.html>`__
    """

    resource_type = "AWS::DataZone::SubscriptionTarget"

    props: PropsDictType = {
        "ApplicableAssetTypes": ([str], True),
        "AuthorizedPrincipals": ([str], True),
        "DomainIdentifier": (str, True),
        "EnvironmentIdentifier": (str, True),
        "ManageAccessRole": (str, True),
        "Name": (str, True),
        "Provider": (str, False),
        "SubscriptionTargetConfig": ([SubscriptionTargetForm], True),
        "Type": (str, True),
    }
