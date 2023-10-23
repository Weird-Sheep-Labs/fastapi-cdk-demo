from aws_cdk import BundlingOptions, Stack
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class FastApiCdkDemoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        song_table = dynamodb.Table(
            self,
            "SongTable",
            partition_key=dynamodb.Attribute(
                name="Artist", type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="Title", type=dynamodb.AttributeType.STRING
            ),
        )

        api_function = _lambda.Function(
            self,
            "ApiFunction",
            code=_lambda.Code.from_asset(
                "api/v1",
                bundling=BundlingOptions(
                    image=_lambda.Runtime.PYTHON_3_11.bundling_image,
                    command=[
                        "bash",
                        "-c",
                        (
                            "pip install --no-cache -r requirements.txt -t"
                            "/asset-output && cp -au . /asset-output"
                        ),
                    ],
                ),
            ),
            handler="main.handler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            environment={"DYNAMODB_SONG_TABLE_NAME": song_table.table_name},
        )

        apigw.LambdaRestApi(
            self,
            "ApiGatewayEndpoint",
            handler=api_function,  # type: ignore
        )

        song_table.grant_read_write_data(api_function)
