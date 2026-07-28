---
collection: ansible
version: "8"
title: "community.aws.api_gateway module – Manage AWS API Gateway APIs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/api_gateway_module.html
fetched_at: 2026-07-28T01:40:05+00:00
---
# community.aws.api_gateway module – Manage AWS API Gateway APIs

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](api_gateway_module.md#ansible-collections-community-aws-api-gateway-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.api_gateway`.

New in community.aws 1.0.0

- [Synopsis](api_gateway_module.md#synopsis)
- [Requirements](api_gateway_module.md#requirements)
- [Parameters](api_gateway_module.md#parameters)
- [Notes](api_gateway_module.md#notes)
- [Examples](api_gateway_module.md#examples)
- [Return Values](api_gateway_module.md#return-values)

## [Synopsis](api_gateway_module.md#id1)

- Allows for the management of API Gateway APIs.
- Normally you should give the api_id since there is no other stable guaranteed unique identifier for the API. If you do not give api_id then a new API will be created each time this is run.
- swagger_file and swagger_text are passed directly on to AWS transparently whilst swagger_dict is an ansible dict which is converted to JSON before the API definitions are uploaded.
- Prior to release 5.0.0 this module was called `community.aws.aws_api_gateway`. The usage did not change.

Aliases: aws_api_gateway

## [Requirements](api_gateway_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](api_gateway_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **api_id**  string | The ID of the API you want to manage. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cache_enabled**  boolean | Enable API GW caching of backend responses.  **Choices:**   - `false` ← (default) - `true` |
| **cache_size**  string | Size in GB of the API GW cache, becomes effective when cache_enabled is true.  **Choices:**   - `"0.5"` ← (default) - `"1.6"` - `"6.1"` - `"13.5"` - `"28.4"` - `"58.2"` - `"118"` - `"237"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **deploy_desc**  string | Description of the deployment.  Recorded and visible in the AWS console.  **Default:** `"Automatic deployment by Ansible."` |
| **endpoint_type**  string | Type of endpoint configuration.  Use `EDGE` for an edge optimized API endpoint, `REGIONAL` for just a regional deploy or `PRIVATE` for a private API.  This flag will only be used when creating a new API Gateway setup, not for updates.  **Choices:**   - `"EDGE"` ← (default) - `"REGIONAL"` - `"PRIVATE"` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **lookup**  string  *added in community.aws 6.2.0* | Look up API gateway by either *tags* (and *name* if supplied) or by *api_id*.  If *lookup=tag* and *tags* is not specified then no lookup for an existing API gateway is performed and a new API gateway will be created.  When using *lookup=tag*, multiple matches being found will result in a failure and no changes will be made.  To change the tags of a API gateway use *lookup=id*.  **Choices:**   - `"tag"` ← (default) - `"id"` |
| **name**  string  *added in community.aws 6.2.0* | The name of the RestApi. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **stage**  string | The name of the stage the API should be deployed to. |
| **stage_canary_settings**  dictionary | Canary settings for the deployment of the stage.  Dict with following settings:  `percentTraffic`: The percent (0-100) of traffic diverted to a canary deployment.  `deploymentId`: The ID of the canary deployment.  `stageVariableOverrides`: Stage variables overridden for a canary release deployment.  `useStageCache`: A Boolean flag to indicate whether the canary deployment uses the stage cache or not.  See docs <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigateway.html#APIGateway.Client.create_stage>  **Default:** `{}` |
| **stage_variables**  dictionary | ENV variables for the stage. Define a dict of key values pairs for variables.  **Default:** `{}` |
| **state**  string | Create or delete API Gateway.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **swagger_dict**  json | Swagger definitions API ansible dictionary which will be converted to JSON and uploaded. |
| **swagger_file**  aliases: src, api_file  path | JSON or YAML file containing swagger definitions for API. Exactly one of *swagger_file*, *swagger_text* or *swagger_dict* must be present. |
| **swagger_text**  string | Swagger definitions for API in JSON or YAML as a string direct from playbook. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **tracing_enabled**  boolean | Specifies whether active tracing with X-ray is enabled for the API GW stage.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](api_gateway_module.md#id4)

> **Note:**
>
> - Tags are used to uniquely identify API gateway when the *api_id* is not supplied. version_added=6.2.0
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](api_gateway_module.md#id5)

```yaml+jinja
- name: Setup AWS API Gateway setup on AWS and deploy API definition
  community.aws.api_gateway:
    swagger_file: my_api.yml
    stage: production
    cache_enabled: true
    cache_size: '1.6'
    tracing_enabled: true
    endpoint_type: EDGE
    state: present

- name: Update API definition to deploy new version
  community.aws.api_gateway:
    api_id: 'abc123321cba'
    swagger_file: my_api.yml
    deploy_desc: Make auth fix available.
    cache_enabled: true
    cache_size: '1.6'
    endpoint_type: EDGE
    state: present

- name: Update API definitions and settings and deploy as canary
  community.aws.api_gateway:
    api_id: 'abc123321cba'
    swagger_file: my_api.yml
    cache_enabled: true
    cache_size: '6.1'
    canary_settings: { percentTraffic: 50.0, deploymentId: '123', useStageCache: True }
    state: present

- name: Delete API gateway
  amazon.aws.api_gateway:
    name: ansible-rest-api
    tags:
      automation: ansible
    lookup: tags
    state: absent
```

## [Return Values](api_gateway_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_id**  string | API id of the API endpoint created  **Returned:** success  **Sample:** `"0ln4zq7p86"` |
| **configure_response**  dictionary | AWS response from the API configure call  **Returned:** success  **Sample:** `{"api_key_source": "HEADER", "created_at": "2020-01-01T11:37:59+00:00", "id": "0ln4zq7p86"}` |
| **deploy_response**  dictionary | AWS response from the API deploy call  **Returned:** success  **Sample:** `{"created_date": "2020-01-01T11:36:59+00:00", "description": "Automatic deployment by Ansible.", "id": "rptv4b"}` |
| **resource_actions**  list / elements=string | Actions performed against AWS API  **Returned:** always  **Sample:** `["apigateway:CreateRestApi", "apigateway:CreateDeployment", "apigateway:PutRestApi"]` |

### Authors

- Michael De La Rue (@mikedlr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
