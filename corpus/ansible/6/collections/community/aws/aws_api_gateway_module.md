---
collection: ansible
version: "6"
title: "community.aws.aws_api_gateway module – Manage AWS API Gateway APIs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_api_gateway_module.html
fetched_at: 2026-07-27T17:03:11+00:00
---
# community.aws.aws_api_gateway module – Manage AWS API Gateway APIs

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/community/aws) (version 3.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](aws_api_gateway_module.md#ansible-collections-community-aws-aws-api-gateway-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_api_gateway`.

New in community.aws 1.0.0

- [Synopsis](aws_api_gateway_module.md#synopsis)
- [Requirements](aws_api_gateway_module.md#requirements)
- [Parameters](aws_api_gateway_module.md#parameters)
- [Notes](aws_api_gateway_module.md#notes)
- [Examples](aws_api_gateway_module.md#examples)
- [Return Values](aws_api_gateway_module.md#return-values)

## [Synopsis](aws_api_gateway_module.md#id1)

- Allows for the management of API Gateway APIs.
- Normally you should give the api_id since there is no other stable guaranteed unique identifier for the API. If you do not give api_id then a new API will be created each time this is run.
- swagger_file and swagger_text are passed directly on to AWS transparently whilst swagger_dict is an ansible dict which is converted to JSON before the API definitions are uploaded.

## [Requirements](aws_api_gateway_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_api_gateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_id**  string | The ID of the API you want to manage. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cache_enabled**  boolean | Enable API GW caching of backend responses.  Choices:   - `false` ← (default) - `true` |
| **cache_size**  string | Size in GB of the API GW cache, becomes effective when cache_enabled is true.  Choices:   - `"0.5"` ← (default) - `"1.6"` - `"6.1"` - `"13.5"` - `"28.4"` - `"58.2"` - `"118"` - `"237"` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **deploy_desc**  string | Description of the deployment.  Recorded and visible in the AWS console.  Default: `"Automatic deployment by Ansible."` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **endpoint_type**  string | Type of endpoint configuration.  Use `EDGE` for an edge optimized API endpoint, `REGIONAL` for just a regional deploy or `PRIVATE` for a private API.  This flag will only be used when creating a new API Gateway setup, not for updates.  Choices:   - `"EDGE"` ← (default) - `"REGIONAL"` - `"PRIVATE"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **stage**  string | The name of the stage the API should be deployed to. |
| **stage_canary_settings**  dictionary | Canary settings for the deployment of the stage.  Dict with following settings:  `percentTraffic`: The percent (0-100) of traffic diverted to a canary deployment.  `deploymentId`: The ID of the canary deployment.  `stageVariableOverrides`: Stage variables overridden for a canary release deployment.  `useStageCache`: A Boolean flag to indicate whether the canary deployment uses the stage cache or not.  See docs <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_stage> |
| **stage_variables**  dictionary | ENV variables for the stage. Define a dict of key values pairs for variables. |
| **state**  string | Create or delete API Gateway.  Choices:   - `"present"` ← (default) - `"absent"` |
| **swagger_dict**  json | Swagger definitions API ansible dictionary which will be converted to JSON and uploaded. |
| **swagger_file**  aliases: src, api_file  path | JSON or YAML file containing swagger definitions for API. Exactly one of *swagger_file*, *swagger_text* or *swagger_dict* must be present. |
| **swagger_text**  string | Swagger definitions for API in JSON or YAML as a string direct from playbook. |
| **tracing_enabled**  boolean | Specifies whether active tracing with X-ray is enabled for the API GW stage.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_api_gateway_module.md#id4)

> **Note:**
>
> - A future version of this module will probably use tags or another ID so that an API can be created only once.
> - As an early work around an intermediate version will probably do the same using a tag embedded in the API name.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_api_gateway_module.md#id5)

```yaml+jinja
- name: Setup AWS API Gateway setup on AWS and deploy API definition
  community.aws.aws_api_gateway:
    swagger_file: my_api.yml
    stage: production
    cache_enabled: true
    cache_size: '1.6'
    tracing_enabled: true
    endpoint_type: EDGE
    state: present

- name: Update API definition to deploy new version
  community.aws.aws_api_gateway:
    api_id: 'abc123321cba'
    swagger_file: my_api.yml
    deploy_desc: Make auth fix available.
    cache_enabled: true
    cache_size: '1.6'
    endpoint_type: EDGE
    state: present

- name: Update API definitions and settings and deploy as canary
  community.aws.aws_api_gateway:
    api_id: 'abc123321cba'
    swagger_file: my_api.yml
    cache_enabled: true
    cache_size: '6.1'
    canary_settings: { percentTraffic: 50.0, deploymentId: '123', useStageCache: True }
    state: present
```

## [Return Values](aws_api_gateway_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_id**  string | API id of the API endpoint created  Returned: success  Sample: `"0ln4zq7p86"` |
| **configure_response**  dictionary | AWS response from the API configure call  Returned: success  Sample: `{"api_key_source": "HEADER", "created_at": "2020-01-01T11:37:59+00:00", "id": "0ln4zq7p86"}` |
| **deploy_response**  dictionary | AWS response from the API deploy call  Returned: success  Sample: `{"created_date": "2020-01-01T11:36:59+00:00", "description": "Automatic deployment by Ansible.", "id": "rptv4b"}` |
| **resource_actions**  list / elements=string | Actions performed against AWS API  Returned: always  Sample: `["apigateway:CreateRestApi", "apigateway:CreateDeployment", "apigateway:PutRestApi"]` |

### Authors

- Michael De La Rue (@mikedlr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
