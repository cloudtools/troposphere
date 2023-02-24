import unittest

from troposphere import codebuild


class TestCodeBuild(unittest.TestCase):
    def test_linux_environment(self):
        environment = codebuild.Environment(
            ComputeType="BUILD_GENERAL1_SMALL",
            Image="aws/codebuild/ubuntu-base:14.04",
            Type="LINUX_CONTAINER",
        )
        environment.to_dict()

    def test_windows_environment(self):
        environment = codebuild.Environment(
            ComputeType="BUILD_GENERAL1_LARGE",
            Image="aws/codebuild/windows-base:1.0",
            Type="WINDOWS_CONTAINER",
        )
        environment.to_dict()

    def test_arm_environment(self):
        environment = codebuild.Environment(
            ComputeType="BUILD_GENERAL1_LARGE",
            Image="aws/codebuild/amazonlinux2-aarch64-standard:1.0",
            Type="ARM_CONTAINER",
        )
        environment.to_dict()

    def test_linux_gpu_environment(self):
        environment = codebuild.Environment(
            ComputeType="BUILD_GENERAL1_LARGE",
            Image="aws/codebuild/standard:4.0",
            Type="LINUX_GPU_CONTAINER",
        )
        environment.to_dict()

    def test_source_codepipeline(self):
        source = codebuild.Source(Type="CODEPIPELINE")
        source.to_dict()


class TestCodeBuildFilters(unittest.TestCase):
    def test_filter(self):
        wh = codebuild.WebhookFilter
        codebuild.ProjectTriggers(
            FilterGroups=[
                [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
                [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
            ]
        ).validate()

    def test_filter_no_filtergroup(self):
        codebuild.ProjectTriggers(Webhook=True).validate()
        # Technically this is valid, not sure why you would want this though?
        codebuild.ProjectTriggers().validate()

    def test_filter_not_list(self):
        match = "<class 'int'>, expected <class 'list'>"
        with self.assertRaisesRegex(TypeError, match):
            codebuild.ProjectTriggers(FilterGroups=42).validate()

    def test_filter_element_not_a_list(self):
        wh = codebuild.WebhookFilter
        match = "is <class 'str'>, expected <class 'list'>"
        with self.assertRaisesRegex(TypeError, match):
            codebuild.ProjectTriggers(
                FilterGroups=[
                    [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
                    "not a list",
                    [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
                ]
            ).validate()

    def test_filter_fail(self):
        wh = codebuild.WebhookFilter
        match = "<class 'NoneType'>"
        with self.assertRaisesRegex(TypeError, match):
            codebuild.ProjectTriggers(
                FilterGroups=[
                    [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
                    [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
                    [None],
                ]
            ).validate()


class TestCodeBuildRegistryCredential(unittest.TestCase):
    def test_registrycredential_provider_bad_value(self):
        with self.assertRaisesRegex(ValueError, "CredentialProvider must be one of"):
            codebuild.RegistryCredential(
                Credential="Foo",
                CredentialProvider="SECRETS",
            )

    def test_registrycredential(self):
        codebuild.RegistryCredential(
            Credential="Foo",
            CredentialProvider="SECRETS_MANAGER",
        )


class TestCodeBuildProjectFileSystemLocation(unittest.TestCase):
    def test_projectfilesystemlocation_type_bad_value(self):
        with self.assertRaisesRegex(ValueError, "Type must be one of"):
            codebuild.ProjectFileSystemLocation(
                Identifier="foo",
                Location="bar",
                MountPoint="baz",
                Type="EF",
            )

    def test_projectfilesystemlocation(self):
        codebuild.ProjectFileSystemLocation(
            Identifier="foo",
            Location="bar",
            MountPoint="baz",
            Type="EFS",
        )
