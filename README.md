<p><a target="_blank" href="https://app.eraser.io/workspace/xZ6vqLhNXQs5If6dCugr" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

![](https://weirdsheeplabs.com/android-chrome-192x192.png "")

# fastapi-cdk-demo
### Demo FastAPI application deployed with CDK
by Weird Sheep Labs

## Overview 📖
The purpose of this repo is to serve as a simple example of how one can deploy a serverless [﻿FastAPI](https://fastapi.tiangolo.com/) application to AWS using [﻿CDK](https://docs.aws.amazon.com/cdk/api/v1/). The basic architecture of the application is shown below:

![Figure 1](/.eraser/xZ6vqLhNXQs5If6dCugr___lEZ5gYkDWAXyFfElOvugFytWGsf2___---figure---9SK-VY94FjDpZQ6zRb6hO---figure---1itafUElg2LjZQXeqxmSqw.png "Figure 1")

### API 🌐
There is nothing special or complex about the API itself, users can interact with a `Song` model via three endpoints that are exposed:

- Create
- List
- Delete (all)
DynamoDB is used for persistence. The `boto3` DynamoDB API is extrememly verbose, so [﻿Dyntastic](https://github.com/nayaverdier/dyntastic) is used to handle DB operations and define the data model due to its support for Pydantic/FastAPI.

### IaC 🧱
All infrastructure code is written in Python 3.11 and defined in one stack, `FastApiCdkDemoStack`.

Lambda application dependencies are bundled using the `BundlingOptions` CDK interface along the lines of the example in the [﻿documentation](https://docs.aws.amazon.com/cdk/api/v1/docs/aws-lambda-readme.html#bundling-asset-code).

## Setup ⚙️
Dependency management is handled by [﻿Poetry](http://python-poetry.org/). To install the project, simply run:

```
poetry install
```
The `docker-compose.yml` file defines a Docker container that runs dynamodb-local so that the application can be run locally. To spin up the container, first define the following environment variables:

```
DYNAMODB_HOST=http://localhost:8000
DYNAMODB_SONG_TABLE_NAME=Song
```
and then run:

```
docker-compose up
```
This will run DynamoDB locally on port 8000 (you can change this in the `docker-compose.yml` file). Then start the FastAPI dev server, making sure to specify a different port to the one in use by DynamoDB:

```
cd api/v1
uvicorn main:app --reload --port 8001
```
## Deployment 🚀
Configuring the AWS deployment environment requires specifying the following environment variables:

```
CDK_DEPLOY_ACCOUNT=<aws_account_number>
CDK_DEPLOY_REGION=<aws_region>
```
Otherwise, the default account/region will be used. Then, deploy with:

```
cdk deploy
```



<!--- Eraser file: https://app.eraser.io/workspace/xZ6vqLhNXQs5If6dCugr --->