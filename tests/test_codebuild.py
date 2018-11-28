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
