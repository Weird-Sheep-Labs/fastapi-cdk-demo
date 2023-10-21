#!/usr/bin/env python3

import aws_cdk as cdk

from api.infrastructure import FastApiCdkDemoStack

app = cdk.App()
FastApiCdkDemoStack(
    app,
    "FastApiCdkDemoStack",
)

app.synth()
