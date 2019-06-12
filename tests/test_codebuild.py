import unittest

from troposphere import codebuild


class TestCodeBuild(unittest.TestCase):
    def test_linux_environment(self):
        environment = codebuild.Environment(
            ComputeType='BUILD_GENERAL1_SMALL',
            Image='aws/codebuild/ubuntu-base:14.04',
            Type='LINUX_CONTAINER'
        )
        environment.to_dict()

    def test_windows_environment(self):
        environment = codebuild.Environment(
            ComputeType='BUILD_GENERAL1_LARGE',
            Image='aws/codebuild/windows-base:1.0',
            Type='WINDOWS_CONTAINER'
        )
        environment.to_dict()

    def test_source_codepipeline(self):
        source = codebuild.Source(
            Type='CODEPIPELINE'
        )
        source.to_dict()


class TestCodeBuildFilters(unittest.TestCase):
    def test_filter(self):
        wh = codebuild.WebhookFilter
        codebuild.ProjectTriggers(FilterGroups=[
            [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
            [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
        ]).validate()

    def test_filter_no_filtergroup(self):
        codebuild.ProjectTriggers(Webhook=True).validate()
        # Technically this is valid, not sure why you would want this though?
        codebuild.ProjectTriggers().validate()

    def test_filter_not_list(self):
        match = "<type 'int'>, expected <type 'list'>"
        with self.assertRaisesRegexp(TypeError, match):
            codebuild.ProjectTriggers(FilterGroups=42).validate()

    def test_filter_element_not_a_list(self):
        wh = codebuild.WebhookFilter
        match = "is <type 'str'>, expected <type 'list'>"
        with self.assertRaisesRegexp(TypeError, match):
            codebuild.ProjectTriggers(FilterGroups=[
                [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
                "not a list",
                [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
            ]).validate()

    def test_filter_fail(self):
        wh = codebuild.WebhookFilter
        match = "<type 'NoneType'>"
        with self.assertRaisesRegexp(TypeError, match):
            codebuild.ProjectTriggers(FilterGroups=[
                [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
                [wh(Type="EVENT", Pattern="PULL_REQUEST_CREATED")],
                [None],
            ]).validate()
