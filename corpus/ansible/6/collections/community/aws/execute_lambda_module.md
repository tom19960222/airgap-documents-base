---
collection: ansible
version: "6"
title: "community.aws.execute_lambda module – Execute an AWS Lambda function"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/execute_lambda_module.html
fetched_at: 2026-07-27T17:04:33+00:00
---
# community.aws.execute_lambda module – Execute an AWS Lambda function

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
> see [Requirements](execute_lambda_module.md#ansible-collections-community-aws-execute-lambda-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.execute_lambda`.

New in community.aws 1.0.0

- [Synopsis](execute_lambda_module.md#synopsis)
- [Requirements](execute_lambda_module.md#requirements)
- [Parameters](execute_lambda_module.md#parameters)
- [Notes](execute_lambda_module.md#notes)
- [Examples](execute_lambda_module.md#examples)
- [Return Values](execute_lambda_module.md#return-values)

## [Synopsis](execute_lambda_module.md#id1)

- This module executes AWS Lambda functions, allowing synchronous and asynchronous invocation.

## [Requirements](execute_lambda_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](execute_lambda_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **dry_run**  boolean | Do not \*actually\* invoke the function. A `DryRun` call will check that the caller has permissions to call the function, especially for checking cross-account permissions.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **function_arn**  string | The name of the function to be invoked |
| **name**  string | The name of the function to be invoked. This can only be used for invocations within the calling account. To invoke a function in another account, use *function_arn* to specify the full ARN. |
| **payload**  dictionary | A dictionary in any form to be provided as input to the Lambda function.  Default: `{}` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **tail_log**  boolean | If *tail_log=yes*, the result of the task will include the last 4 KB of the CloudWatch log for the function execution. Log tailing only works if you use synchronous invocation *wait=yes*. This is usually used for development or testing Lambdas.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **version_qualifier**  string | Which version/alias of the function to run. This defaults to the `LATEST` revision, but can be set to any existing version or alias. See <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html> for details. |
| **wait**  boolean | Whether to wait for the function results or not. If *wait=no* the task will not return any results. To wait for the Lambda function to complete, set *wait=yes* and the result will be available in the *output* key.  Choices:   - `false` - `true` ← (default) |

## [Notes](execute_lambda_module.md#id4)

> **Note:**
>
> - Async invocation will always return an empty `output` key.
> - Synchronous invocation may result in a function timeout, resulting in an empty `output` key.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](execute_lambda_module.md#id5)

```yaml+jinja
- community.aws.execute_lambda:
    name: test-function
    # the payload is automatically serialized and sent to the function
    payload:
      foo: bar
      value: 8
  register: response

# Test that you have sufficient permissions to execute a Lambda function in
# another account
- community.aws.execute_lambda:
    function_arn: arn:aws:lambda:us-east-1:123456789012:function/some-function
    dry_run: true

- community.aws.execute_lambda:
    name: test-function
    payload:
      foo: bar
      value: 8
    wait: true
    tail_log: true
  register: response
  # the response will have a `logs` key that will contain a log (up to 4KB) of the function execution in Lambda

# Pass the Lambda event payload as a json file.
- community.aws.execute_lambda:
    name: test-function
    payload: "{{ lookup('file','lambda_event.json') }}"
  register: response

- community.aws.execute_lambda:
    name: test-function
    version_qualifier: PRODUCTION
```

## [Return Values](execute_lambda_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | Resulting data structure from a successful task execution.  Returned: success |
| **logs**  string | The last 4KB of the function logs. Only provided if *tail_log* is `true`  Returned: if *tail_log* == true |
| **output**  dictionary | Function output if wait=true and the function returns a value  Returned: success  Sample: `{"output": "something"}` |
| **status**  integer | `StatusCode` of API call exit (200 for synchronous invokes, 202 for async)  Returned: always  Sample: `200` |

### Authors

- Ryan Scott Brown (@ryansb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
