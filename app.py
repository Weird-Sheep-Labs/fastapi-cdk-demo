#!/usr/bin/env python3
import os

import aws_cdk as cdk

from api.infrastructure import FastApiCdkDemoStack

app = cdk.App()
FastApiCdkDemoStack(
    app,
    "FastApiCdkDemoStack",
    env=cdk.Environment(
        account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
        region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]),
    ),
)

app.synth()
