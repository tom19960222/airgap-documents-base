---
collection: ansible
version: "8"
title: "amazon.aws.lambda_event module – Creates, updates or deletes AWS Lambda function event mappings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/lambda_event_module.html
fetched_at: 2026-07-28T01:06:57+00:00
---
# amazon.aws.lambda_event module – Creates, updates or deletes AWS Lambda function event mappings

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
> see [Requirements](lambda_event_module.md#ansible-collections-amazon-aws-lambda-event-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.lambda_event`.

New in amazon.aws 5.0.0

- [Synopsis](lambda_event_module.md#synopsis)
- [Requirements](lambda_event_module.md#requirements)
- [Parameters](lambda_event_module.md#parameters)
- [Notes](lambda_event_module.md#notes)
- [Examples](lambda_event_module.md#examples)
- [Return Values](lambda_event_module.md#return-values)

## [Synopsis](lambda_event_module.md#id1)

- This module allows the management of AWS Lambda function event source mappings such as DynamoDB and Kinesis stream events via the Ansible framework. These event source mappings are relevant only in the AWS Lambda pull model, where AWS Lambda invokes the function. It is idempotent and supports “Check” mode. Use module [amazon.aws.lambda](lambda_module.md#ansible-collections-amazon-aws-lambda-module) to manage the lambda function itself and [amazon.aws.lambda_alias](lambda_alias_module.md#ansible-collections-amazon-aws-lambda-alias-module) to manage function aliases.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](lambda_event_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](lambda_event_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **alias**  string | Name of the function alias.  Mutually exclusive with *version*. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **event_source**  string | Source of the event that triggers the lambda function.  For DynamoDB and Kinesis events, select `stream`  For SQS queues, select `sqs`  **Choices:**   - `"stream"` ← (default) - `"sqs"` |
| **lambda_function_arn**  aliases: function_name, function_arn  string / required | The name or ARN of the lambda function. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **source_params**  dictionary / required | Sub-parameters required for event source. |
| **batch_size**  integer | The largest number of records that AWS Lambda will retrieve from your event source at the time of invoking your function.  **Default:** `100` |
| **enabled**  boolean | Indicates whether AWS Lambda should begin polling or readin from the event source.  **Choices:**   - `false` - `true` ← (default) |
| **function_response_types**  list / elements=string  *added in amazon.aws 5.5.0* | (Streams and Amazon SQS) A list of current response type enums applied to the event source mapping.  **Choices:**   - `"ReportBatchItemFailures"` |
| **source_arn**  string / required | The Amazon Resource Name (ARN) of the SQS queue, Kinesis stream or DynamoDB stream that is the event source. |
| **starting_position**  string | The position in the stream where AWS Lambda should start reading.  Required when *event_source=stream*.  **Choices:**   - `"TRIM_HORIZON"` - `"LATEST"` |
| **state**  string | Describes the desired state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **version**  integer | Version of the Lambda function.  Mutually exclusive with *alias*.  **Default:** `0` |

## [Notes](lambda_event_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](lambda_event_module.md#id5)

```yaml+jinja
# Example that creates a lambda event notification for a DynamoDB stream
- name: DynamoDB stream event mapping
  amazon.aws.lambda_event:
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

# Example that creates a lambda event notification for a DynamoDB stream
- name: DynamoDB stream event mapping
  amazon.aws.lambda_event:
    state: present
    event_source: stream
    function_name: "{{ function_name }}"
    source_params:
      source_arn: arn:aws:dynamodb:us-east-1:123456789012:table/tableName/stream/2016-03-19T19:51:37.457
      enabled: True
      batch_size: 100
      starting_position: LATEST
      function_response_types:
        - ReportBatchItemFailures
  register: event

- name: Show source event
  ansible.builtin.debug:
    var: event.lambda_stream_events
```

## [Return Values](lambda_event_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **lambda_stream_events**  list / elements=string | list of dictionaries returned by the API describing stream event mappings  **Returned:** success |

### Authors

- Pierre Jodouin (@pjodouin)
- Ryan Brown (@ryansb)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
