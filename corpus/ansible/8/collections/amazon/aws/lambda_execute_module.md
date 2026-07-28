---
collection: ansible
version: "8"
title: "amazon.aws.lambda_execute module – Execute an AWS Lambda function"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/lambda_execute_module.html
fetched_at: 2026-07-28T01:06:58+00:00
---
# amazon.aws.lambda_execute module – Execute an AWS Lambda function

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
> see [Requirements](lambda_execute_module.md#ansible-collections-amazon-aws-lambda-execute-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.lambda_execute`.

New in amazon.aws 5.0.0

- [Synopsis](lambda_execute_module.md#synopsis)
- [Requirements](lambda_execute_module.md#requirements)
- [Parameters](lambda_execute_module.md#parameters)
- [Notes](lambda_execute_module.md#notes)
- [Examples](lambda_execute_module.md#examples)
- [Return Values](lambda_execute_module.md#return-values)

## [Synopsis](lambda_execute_module.md#id1)

- This module executes AWS Lambda functions, allowing synchronous and asynchronous invocation.
- Prior to release 5.0.0 this module was called `community.aws.execute_lambda`. The usage did not change.
- This module was originally added to `community.aws` in release 1.0.0.

Aliases: execute_lambda

## [Requirements](lambda_execute_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](lambda_execute_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **dry_run**  boolean | Do not \*actually\* invoke the function. A `DryRun` call will check that the caller has permissions to call the function, especially for checking cross-account permissions.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **function_arn**  string | The name of the function to be invoked |
| **name**  string | The name of the function to be invoked. This can only be used for invocations within the calling account. To invoke a function in another account, use *function_arn* to specify the full ARN. |
| **payload**  dictionary | A dictionary in any form to be provided as input to the Lambda function.  **Default:** `{}` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **tail_log**  boolean | If *tail_log=true*, the result of the task will include the last 4 KB of the CloudWatch log for the function execution. Log tailing only works if you use synchronous invocation *wait=true*. This is usually used for development or testing Lambdas.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version_qualifier**  string | Which version/alias of the function to run. This defaults to the `LATEST` revision, but can be set to any existing version or alias. See <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html> for details. |
| **wait**  boolean | Whether to wait for the function results or not. If *wait=no* the task will not return any results. To wait for the Lambda function to complete, set *wait=true* and the result will be available in the *output* key.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](lambda_execute_module.md#id4)

> **Note:**
>
> - Async invocation will always return an empty `output` key.
> - Synchronous invocation may result in a function timeout, resulting in an empty `output` key.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](lambda_execute_module.md#id5)

```yaml+jinja
- amazon.aws.lambda_execute:
    name: test-function
    # the payload is automatically serialized and sent to the function
    payload:
      foo: bar
      value: 8
  register: response

# Test that you have sufficient permissions to execute a Lambda function in
# another account
- amazon.aws.lambda_execute:
    function_arn: arn:aws:lambda:us-east-1:123456789012:function/some-function
    dry_run: true

- amazon.aws.lambda_execute:
    name: test-function
    payload:
      foo: bar
      value: 8
    wait: true
    tail_log: true
  register: response
  # the response will have a `logs` key that will contain a log (up to 4KB) of the function execution in Lambda

# Pass the Lambda event payload as a json file.
- amazon.aws.lambda_execute:
    name: test-function
    payload: "{{ lookup('file','lambda_event.json') }}"
  register: response

- amazon.aws.lambda_execute:
    name: test-function
    version_qualifier: PRODUCTION
```

## [Return Values](lambda_execute_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | Resulting data structure from a successful task execution.  **Returned:** success |
| **logs**  string | The last 4KB of the function logs. Only provided if *tail_log* is `true`  **Returned:** if *tail_log* == true |
| **output**  dictionary | Function output if wait=true and the function returns a value  **Returned:** success  **Sample:** `{"output": "something"}` |
| **status**  integer | `StatusCode` of API call exit (200 for synchronous invokes, 202 for async)  **Returned:** always  **Sample:** `200` |

### Authors

- Ryan Scott Brown (@ryansb)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
