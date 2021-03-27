import unittest

from troposphere.appsync import PipelineConfig, Resolver


class TestAppsyncResolver(unittest.TestCase):
    def test_resolver_kind_bad_value(self):
        with self.assertRaisesRegex(ValueError, "Kind must be one of"):
            Resolver(
                "MutationField",
                DataSourceName="SomeDatasource",
                FieldName="Field",
                TypeName="Mutation",
                ApiId="some_api_id",
                Kind="SOME_KIND",
                PipelineConfig=PipelineConfig(Functions=["FunctionId1", "FunctionId"]),
                RequestMappingTemplateS3Location=("s3://bucket/key.req.vtl"),
                ResponseMappingTemplateS3Location=("s3://bucket/key.res.vtl"),
            )

    def test_resolver(self):
        Resolver(
            "MutationField",
            DataSourceName="SomeDatasource",
            FieldName="Field",
            TypeName="Mutation",
            ApiId="some_api_id",
            Kind="PIPELINE",
            PipelineConfig=PipelineConfig(Functions=["FunctionId1", "FunctionId"]),
            RequestMappingTemplateS3Location=("s3://bucket/key.req.vtl"),
            ResponseMappingTemplateS3Location=("s3://bucket/key.res.vtl"),
        )

        Resolver(
            "MutationField",
            DataSourceName="SomeDatasource",
            FieldName="Field",
            TypeName="Mutation",
            ApiId="some_api_id",
            Kind="UNIT",
            RequestMappingTemplateS3Location=("s3://bucket/key.req.vtl"),
            ResponseMappingTemplateS3Location=("s3://bucket/key.res.vtl"),
        )
