---
collection: ansible
version: "6"
title: "community.aws.lambda_event module – Creates, updates or deletes AWS Lambda function event mappings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/lambda_event_module.html
fetched_at: 2026-07-27T17:04:46+00:00
---
# community.aws.lambda_event module – Creates, updates or deletes AWS Lambda function event mappings

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
> see [Requirements](lambda_event_module.md#ansible-collections-community-aws-lambda-event-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.lambda_event`.

New in community.aws 1.0.0

- [Synopsis](lambda_event_module.md#synopsis)
- [Requirements](lambda_event_module.md#requirements)
- [Parameters](lambda_event_module.md#parameters)
- [Notes](lambda_event_module.md#notes)
- [Examples](lambda_event_module.md#examples)
- [Return Values](lambda_event_module.md#return-values)

## [Synopsis](lambda_event_module.md#id1)

- This module allows the management of AWS Lambda function event source mappings such as DynamoDB and Kinesis stream events via the Ansible framework. These event source mappings are relevant only in the AWS Lambda pull model, where AWS Lambda invokes the function. It is idempotent and supports “Check” mode. Use module [community.aws.lambda](lambda_module.md#ansible-collections-community-aws-lambda-module) to manage the lambda function itself and [community.aws.lambda_alias](lambda_alias_module.md#ansible-collections-community-aws-lambda-alias-module) to manage function aliases.

## [Requirements](lambda_event_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](lambda_event_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alias**  string | Name of the function alias.  Mutually exclusive with *version*. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **event_source**  string | Source of the event that triggers the lambda function.  For DynamoDB and Kinesis events, select `stream`  For SQS queues, select `sqs`  Choices:   - `"stream"` ← (default) - `"sqs"` |
| **lambda_function_arn**  aliases: function_name, function_arn  string / required | The name or ARN of the lambda function. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **source_params**  dictionary / required | Sub-parameters required for event source. |
| **batch_size**  integer | The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.  Default: `100` |
| **enabled**  boolean | Indicates whether AWS Lambda should begin polling or readin from the event source.  Choices:   - `false` - `true` ← (default) |
| **source_arn**  string / required | The Amazon Resource Name (ARN) of the SQS queue, Kinesis stream or DynamoDB stream that is the event source. |
| **starting_position**  string | The position in the stream where AWS Lambda should start reading.  Required when *event_source=stream*.  Choices:   - `"TRIM_HORIZON"` - `"LATEST"` |
| **state**  string | Describes the desired state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **version**  integer | Version of the Lambda function.  Mutually exclusive with *alias*. |

## [Notes](lambda_event_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](lambda_event_module.md#id5)

```yaml+jinja
# Example that creates a lambda event notification for a DynamoDB stream
- name: DynamoDB stream event mapping
  community.aws.lambda_event:
    state: present
    event_source: stream
    function_name: "{{ function_name }}"
    alias: Dev
    source_params:
    source_arn: arn:aws:dynamodb:us-east-1:123456789012:table/tableName/stream/2016-03-19T19:51:37.457
    enabled: True
    batch_size: 100
    starting_position: TRIM_HORIZON
  register: event

- name: Show source event
  ansible.builtin.debug:
    var: event.lambda_stream_events
```

## [Return Values](lambda_event_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **lambda_stream_events**  list / elements=string | list of dictionaries returned by the API describing stream event mappings  Returned: success |

### Authors

- Pierre Jodouin (@pjodouin), Ryan Brown (@ryansb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
