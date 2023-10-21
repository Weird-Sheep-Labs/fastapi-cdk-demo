import aws_cdk as core
import aws_cdk.assertions as assertions

from api.infrastructure import FastApiCdkDemoStack


# example tests. To run these tests, uncomment this file along with the example
# resource in dummy/dummy_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FastApiCdkDemoStack(app, "dummy")
    _ = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
