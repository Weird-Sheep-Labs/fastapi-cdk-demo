from unittest import TestCase

import aws_cdk as core
import aws_cdk.assertions as assertions

from api.infrastructure import FastApiCdkDemoStack


class FastApiCdkDemoStackTestCase(TestCase):
    def setUp(self) -> None:
        app = core.App()
        stack = FastApiCdkDemoStack(app, "TestStack")
        self.template = assertions.Template.from_stack(stack)
        return super().setUp()

    def test_song_table_created(self):
        self.template.has_resource(type="AWS::DynamoDB::Table", props={})

    def test_api_function_created(self):
        self.template.has_resource(type="AWS::Lambda::Function", props={})

    def test_api_gateway_created(self):
        self.template.has_resource(type="AWS::ApiGateway::RestApi", props={})
