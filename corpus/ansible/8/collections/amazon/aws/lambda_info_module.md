---
collection: ansible
version: "8"
title: "amazon.aws.lambda_info module – Gathers AWS Lambda function details"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/lambda_info_module.html
fetched_at: 2026-07-28T01:06:59+00:00
---
# amazon.aws.lambda_info module – Gathers AWS Lambda function details

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](lambda_info_module.md#ansible-collections-amazon-aws-lambda-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.lambda_info`.

New in amazon.aws 5.0.0

- [Synopsis](lambda_info_module.md#synopsis)
- [Requirements](lambda_info_module.md#requirements)
- [Parameters](lambda_info_module.md#parameters)
- [Notes](lambda_info_module.md#notes)
- [Examples](lambda_info_module.md#examples)
- [Return Values](lambda_info_module.md#return-values)

## [Synopsis](lambda_info_module.md#id1)

- Gathers various details related to Lambda functions, including aliases, versions and event source mappings.
- Use module [amazon.aws.lambda](lambda_module.md#ansible-collections-amazon-aws-lambda-module) to manage the lambda function itself, [amazon.aws.lambda_alias](lambda_alias_module.md#ansible-collections-amazon-aws-lambda-alias-module) to manage function aliases, [amazon.aws.lambda_event](lambda_event_module.md#ansible-collections-amazon-aws-lambda-event-module) to manage lambda event source mappings, and [amazon.aws.lambda_policy](lambda_policy_module.md#ansible-collections-amazon-aws-lambda-policy-module) to manage policy statements.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](lambda_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](lambda_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **event_source_arn**  string | When *query=mappings*, this is the Amazon Resource Name (ARN) of the Amazon Kinesis or DynamoDB stream. |
| **function_name**  aliases: function, name  string | The name of the lambda function for which information is requested. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **query**  string | Specifies the resource type for which to gather information.  Defaults to `all` when *function_name* is specified.  Defaults to `config` when *function_name* is NOT specified.  **Choices:**   - `"aliases"` - `"all"` - `"config"` - `"mappings"` - `"policy"` - `"versions"` - `"tags"` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](lambda_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](lambda_info_module.md#id5)

```yaml+jinja
---
# Simple example of listing all info for a function
- name: List all for a specific function
  amazon.aws.lambda_info:
    query: all
    function_name: myFunction
  register: my_function_details

# List all versions of a function
- name: List function versions
  amazon.aws.lambda_info:
    query: versions
    function_name: myFunction
  register: my_function_versions

# List all info for all functions
- name: List all functions
  amazon.aws.lambda_info:
    query: all
  register: output

- name: show Lambda information
  ansible.builtin.debug:
    msg: "{{ output['function'] }}"
```

## [Return Values](lambda_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **function**  dictionary | lambda function list.  `function` has been deprecated in will be removed in the next major release after 2025-01-01.  **Returned:** success |
| **function.TheName**  dictionary | lambda function information, including event, mapping, and version information.  `function` has been deprecated in will be removed in the next major release after 2025-01-01.  **Returned:** success |
| **functions**  list / elements=dictionary  *added in community.aws 4.1.0* | List of information for each lambda function matching the query.  **Returned:** always |
| **aliases**  list / elements=string | The aliases associated with the function.  **Returned:** when `query` is *aliases* or *all* |
| **architectures**  list / elements=string | The architectures supported by the function.  **Returned:** successful run where botocore >= 1.21.51  **Sample:** `["arm64"]` |
| **code_sha256**  string | The SHA256 hash of the function’s deployment package.  **Returned:** success  **Sample:** `"zOAGfF5JLFuzZoSNirUtOrQp+S341IOA3BcoXXoaIaU="` |
| **code_size**  integer | The size of the function’s deployment package in bytes.  **Returned:** success  **Sample:** `123` |
| **dead_letter_config**  dictionary | The function’s dead letter queue.  **Returned:** when the function has a dead letter queue configured  **Sample:** `{"target_arn": "arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"}` |
| **target_arn**  string | The ARN of an SQS queue or SNS topic.  **Returned:** when the function has a dead letter queue configured  **Sample:** `"arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"` |
| **description**  string | The function’s description.  **Returned:** success  **Sample:** `"My function"` |
| **environment**  dictionary | The function’s environment variables.  **Returned:** when environment variables exist |
| **error**  dictionary | Error message for environment variables that could not be applied.  **Returned:** when there is an error applying environment variables |
| **error_code**  string | The error code.  **Returned:** when there is an error applying environment variables |
| **message**  string | The error message.  **Returned:** when there is an error applying environment variables |
| **variables**  dictionary | Environment variable key-value pairs.  **Returned:** when environment variables exist  **Sample:** `{"key": "value"}` |
| **function_arn**  string | The function’s Amazon Resource Name (ARN).  **Returned:** on success  **Sample:** `"arn:aws:lambda:us-east-1:123456789012:function:myFunction:1"` |
| **function_name**  string | The function’s name.  **Returned:** on success  **Sample:** `"myFunction"` |
| **handler**  string | The function Lambda calls to begin executing your function.  **Returned:** on success  **Sample:** `"index.handler"` |
| **last_modified**  string | The date and time that the function was last updated, in ISO-8601 format (YYYY-MM-DDThh:mm:ssTZD).  **Returned:** on success  **Sample:** `"2017-08-01T00:00:00.000+0000"` |
| **mappings**  list / elements=dictionary | List of configuration information for each event source mapping.  **Returned:** when `query` is *all* or *mappings* |
| **batch_size**  integer | The largest number of records that AWS Lambda will retrieve from the event source at the time of invoking the function.  **Returned:** on success |
| **event_source_arn**  string | The ARN of the Amazon Kinesis or DyanmoDB stream that is the source of events.  **Returned:** on success |
| **function_arn**  string | The Lambda function to invoke when AWS Lambda detects an event on the poll-based source.  **Returned:** on success |
| **last_modified**  string | The UTC time string indicating the last time the event mapping was updated.  **Returned:** on success |
| **last_processing_result**  string | The result of the last AWS Lambda invocation of your Lambda function.  **Returned:** on success |
| **state**  string | The state of the event source mapping.  **Returned:** on success |
| **state_transition_reason**  string | The reason the event source mapping is in its current state.  **Returned:** on success |
| **uuid**  string | The AWS Lambda assigned opaque identifier for the mapping.  **Returned:** on success |
| **memory_size**  integer | The memory allocated to the function.  **Returned:** on success  **Sample:** `128` |
| **policy**  dictionary | The policy associated with the function.  **Returned:** when `query` is *all* or *policy* |
| **revision_id**  string | The latest updated revision of the function or alias.  **Returned:** on success  **Sample:** `"a2x9886d-d48a-4a0c-ab64-82abc005x80c"` |
| **role**  string | The function’s execution role.  **Returned:** on success  **Sample:** `"arn:aws:iam::123456789012:role/lambda_basic_execution"` |
| **runtime**  string | The funtime environment for the Lambda function.  **Returned:** on success  **Sample:** `"nodejs6.10"` |
| **timeout**  integer | The amount of time that Lambda allows a function to run before terminating it.  **Returned:** on success  **Sample:** `3` |
| **tracing_config**  dictionary | The function’s AWS X-Ray tracing configuration.  **Returned:** on success  **Sample:** `{"mode": "Active"}` |
| **mode**  string | The tracing mode.  **Returned:** on success  **Sample:** `"Active"` |
| **version**  string | The version of the Lambda function.  **Returned:** on success  **Sample:** `"1"` |
| **versions**  list / elements=dictionary | List of Lambda function versions.  **Returned:** when `query` is *all* or *versions* |
| **vpc_config**  dictionary | The function’s networking configuration.  **Returned:** on success  **Sample:** `{"security_group_ids": [], "subnet_ids": [], "vpc_id": "123"}` |

### Authors

- Pierre Jodouin (@pjodouin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
