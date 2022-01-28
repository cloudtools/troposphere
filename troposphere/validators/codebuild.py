# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from .. import AWSHelperFn


def validate_environmentvariable_or_list(x):
    """
    Property: Environment.EnvironmentVariables
    """

    from ..codebuild import EnvironmentVariable

    if isinstance(x, AWSHelperFn):
        return x

    if not isinstance(x, list):
        raise ValueError(f"Value {x} of type {type(x)} must be a list")

    for elem in x:
        if not isinstance(elem, (dict, EnvironmentVariable)):
            raise ValueError(
                f"Value {elem} of type {type(elem)} must be either dict or EnvironmentVariable"
            )

    return x


def validate_image_pull_credentials(image_pull_credentials):
    """
    Validate ImagePullCredentialsType for Project
    Property: Environment.ImagePullCredentialsType
    """

    VALID_IMAGE_PULL_CREDENTIALS = ("CODEBUILD", "SERVICE_ROLE")

    if image_pull_credentials not in VALID_IMAGE_PULL_CREDENTIALS:
        raise ValueError(
            "Project ImagePullCredentialsType must be one of: %s"
            % ", ".join(VALID_IMAGE_PULL_CREDENTIALS)
        )
    return image_pull_credentials


def validate_credentials_provider(credential_provider):
    """
    Validate CredentialProvider for Project's RegistryCredential
    Property: RegistryCredential.CredentialProvider
    """

    VALID_CREDENTIAL_PROVIDERS = "SECRETS_MANAGER"

    if credential_provider not in VALID_CREDENTIAL_PROVIDERS:
        raise ValueError(
            "RegistryCredential CredentialProvider must be one of: %s"
            % ", ".join(VALID_CREDENTIAL_PROVIDERS)
        )
    return credential_provider


def validate_webhookfilter_type(webhookfilter_type):
    """
    Validate WebHookFilter type property for a Project
    Property: WebhookFilter.Type
    """

    VALID_WEBHOOKFILTER_TYPES = (
        "EVENT",
        "ACTOR_ACCOUNT_ID",
        "HEAD_REF",
        "BASE_REF",
        "FILE_PATH",
    )

    if webhookfilter_type not in VALID_WEBHOOKFILTER_TYPES:
        raise ValueError(
            "Project Webhookfilter Type must be one of: %s"
            % ", ".join(VALID_WEBHOOKFILTER_TYPES)
        )
    return webhookfilter_type


def validate_projectfilesystemlocation_type(projectfilesystemlocation_type):
    """
    Validate ProjectFileSystemLocation type property
    Property: ProjectFileSystemLocation.Type
    """

    VALID_PROJECTFILESYSTEMLOCATION_TYPE = "EFS"

    if projectfilesystemlocation_type not in VALID_PROJECTFILESYSTEMLOCATION_TYPE:
        raise ValueError(
            "ProjectFileSystemLocation Type must be one of: %s"
            % ", ".join(VALID_PROJECTFILESYSTEMLOCATION_TYPE)
        )
    return projectfilesystemlocation_type


def validate_source_auth(self):
    """
    Class: SourceAuth
    """

    valid_types = ["OAUTH"]
    auth_types = self.properties.get("Type")
    if auth_types not in valid_types:
        raise ValueError("SourceAuth Type: must be one of %s" % ",".join(valid_types))


def validate_artifacts(self):
    """
    Class: Artifacts
    """
    valid_types = [
        "CODEPIPELINE",
        "NO_ARTIFACTS",
        "S3",
    ]
    artifact_type = self.properties.get("Type")
    if artifact_type not in valid_types:
        raise ValueError("Artifacts Type: must be one of %s" % ",".join(valid_types))

    if artifact_type == "S3":
        for required_property in ["Name", "Location"]:
            if not self.properties.get(required_property):
                raise ValueError(
                    "Artifacts Type S3: requires %s to be set" % required_property
                )


def validate_environment_variable(self):
    """
    Class: EnvironmentVariable
    """
    if "Type" in self.properties:
        valid_types = ["PARAMETER_STORE", "PLAINTEXT", "SECRETS_MANAGER"]
        env_type = self.properties.get("Type")
        if env_type not in valid_types:
            raise ValueError(
                "EnvironmentVariable Type: must be one of %s" % ",".join(valid_types)
            )


def validate_environment(self):
    """
    Class: Environment
    """
    valid_types = [
        "ARM_CONTAINER",
        "LINUX_CONTAINER",
        "LINUX_GPU_CONTAINER",
        "WINDOWS_CONTAINER",
        "WINDOWS_SERVER_2019_CONTAINER",
    ]
    env_type = self.properties.get("Type")

    if isinstance(env_type, AWSHelperFn):
        return

    if env_type not in valid_types:
        raise ValueError("Environment Type: must be one of %s" % ",".join(valid_types))


def validate_project_cache(self):
    """
    Class: ProjectCache
    """
    valid_types = [
        "NO_CACHE",
        "LOCAL",
        "S3",
    ]
    cache_type = self.properties.get("Type")
    if cache_type not in valid_types:
        raise ValueError("ProjectCache Type: must be one of %s" % ",".join(valid_types))


def validate_source(self):
    """
    Class: Source
    """
    valid_types = [
        "BITBUCKET",
        "CODECOMMIT",
        "CODEPIPELINE",
        "GITHUB",
        "GITHUB_ENTERPRISE",
        "NO_SOURCE",
        "S3",
    ]

    location_agnostic_types = [
        "CODEPIPELINE",
        "NO_SOURCE",
    ]

    source_type = self.properties.get("Type")

    # Don't do additional checks if source_type can't
    # be determined (for example, being a Ref).
    if isinstance(source_type, AWSHelperFn):
        return

    if source_type not in valid_types:
        raise ValueError("Source Type: must be one of %s" % ",".join(valid_types))

    location = self.properties.get("Location")

    if source_type not in location_agnostic_types and not location:
        raise ValueError(
            "Source Location: must be defined when type is %s" % source_type
        )

    auth = self.properties.get("Auth")
    if auth is not None and source_type != "GITHUB":
        raise ValueError(
            "SourceAuth: must only be defined when using " "'GITHUB' Source Type."
        )


def validate_project_triggers(self):
    """
    FilterGroups, if set, needs to be a list of a list of WebhookFilters
    Class: ProjectTriggers
    """

    from ..codebuild import WebhookFilter

    filter_groups = self.properties.get("FilterGroups")
    if filter_groups is not None:
        if not isinstance(filter_groups, list):
            self._raise_type("FilterGroups", filter_groups, list)

        for counti, elem in enumerate(filter_groups):
            if not isinstance(elem, list):
                self._raise_type(
                    "FilterGroups[{}]".format(counti), filter_groups[counti], list
                )
            for countj, hook in enumerate(filter_groups[counti]):
                if not isinstance(hook, WebhookFilter):
                    self._raise_type(
                        "FilterGroups[{}][{}]".format(counti, countj),
                        hook,
                        WebhookFilter,
                    )


def validate_status(status):
    """
    Validate status
    :param status: The Status of CloudWatchLogs or S3Logs
    :return: The provided value if valid
    Property: CloudWatchLogs.Status
    Property: S3Logs.Status
    """
    valid_statuses = ["ENABLED", "DISABLED"]

    if status not in valid_statuses:
        raise ValueError("Status: must be one of %s" % ",".join(valid_statuses))
    return status
