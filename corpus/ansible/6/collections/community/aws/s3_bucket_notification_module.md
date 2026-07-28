---
collection: ansible
version: "6"
title: "community.aws.s3_bucket_notification module – Creates, updates or deletes S3 Bucket notifications targeting Lambda functions, SNS or SQS."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/s3_bucket_notification_module.html
fetched_at: 2026-07-27T17:05:01+00:00
---
# community.aws.s3_bucket_notification module – Creates, updates or deletes S3 Bucket notifications targeting Lambda functions, SNS or SQS.

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
> see [Requirements](s3_bucket_notification_module.md#ansible-collections-community-aws-s3-bucket-notification-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.s3_bucket_notification`.

New in community.aws 1.0.0

- [Synopsis](s3_bucket_notification_module.md#synopsis)
- [Requirements](s3_bucket_notification_module.md#requirements)
- [Parameters](s3_bucket_notification_module.md#parameters)
- [Notes](s3_bucket_notification_module.md#notes)
- [Examples](s3_bucket_notification_module.md#examples)
- [Return Values](s3_bucket_notification_module.md#return-values)

## [Synopsis](s3_bucket_notification_module.md#id1)

- This module supports the creation, updates and deletions of S3 bucket notification profiles targeting either Lambda functions, SNS topics or SQS queues.
- The target for the notifications must already exist. For lambdas use module [community.aws.lambda](lambda_module.md#ansible-collections-community-aws-lambda-module) to manage the lambda function itself, [community.aws.lambda_alias](lambda_alias_module.md#ansible-collections-community-aws-lambda-alias-module) to manage function aliases and [community.aws.lambda_policy](lambda_policy_module.md#ansible-collections-community-aws-lambda-policy-module) to modify lambda permissions. For SNS or SQS then use [community.aws.sns_topic](sns_topic_module.md#ansible-collections-community-aws-sns-topic-module) or [community.aws.sqs_queue](sqs_queue_module.md#ansible-collections-community-aws-sqs-queue-module).

## [Requirements](s3_bucket_notification_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](s3_bucket_notification_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bucket_name**  string / required | S3 bucket name. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **event_name**  string / required | Unique name for event notification on bucket. |
| **events**  list / elements=string | Events that will be triggering a notification. You can select multiple events to send to the same destination, you can set up different events to send to different destinations, and you can set up a prefix or suffix for an event. However, for each bucket, individual events cannot have multiple configurations with overlapping prefixes or suffixes that could match the same object key.  Required when *state=present*.  Choices:   - `"s3:ObjectCreated:*"` - `"s3:ObjectCreated:Put"` - `"s3:ObjectCreated:Post"` - `"s3:ObjectCreated:Copy"` - `"s3:ObjectCreated:CompleteMultipartUpload"` - `"s3:ObjectRemoved:*"` - `"s3:ObjectRemoved:Delete"` - `"s3:ObjectRemoved:DeleteMarkerCreated"` - `"s3:ObjectRestore:Post"` - `"s3:ObjectRestore:Completed"` - `"s3:ReducedRedundancyLostObject"` |
| **lambda_alias**  string | Name of the Lambda function alias.  Mutually exclusive with *lambda_version*. |
| **lambda_function_arn**  aliases: function_arn  string | The ARN of the lambda function.  Mutually exclusive with *queue_arn* and *topic_arn*. |
| **lambda_version**  integer | Version of the Lambda function.  Mutually exclusive with *lambda_alias*. |
| **prefix**  string | Optional prefix to limit the notifications to objects with keys that start with matching characters. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **queue_arn**  string  added in community.aws 3.2.0 | The ARN of the SQS queue.  Mutually exclusive with *topic_arn* and *lambda_function_arn*. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Describes the desired state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **suffix**  string | Optional suffix to limit the notifications to objects with keys that end with matching characters. |
| **topic_arn**  string  added in community.aws 3.2.0 | The ARN of the SNS topic.  Mutually exclusive with *queue_arn* and *lambda_function_arn*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](s3_bucket_notification_module.md#id4)

> **Note:**
>
> - If using Lambda function as the target then a Lambda policy is also needed, use [community.aws.lambda_policy](lambda_policy_module.md#ansible-collections-community-aws-lambda-policy-module) to do so to allow `lambda:InvokeFunction` for the notification.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](s3_bucket_notification_module.md#id5)

```yaml+jinja
---
# Examples adding notification target configs to a S3 bucket
- name: Setup bucket event notification to a Lambda function
  community.aws.s3_bucket_notification:
    state: present
    event_name: on_file_add_or_remove
    bucket_name: test-bucket
    lambda_function_arn: arn:aws:lambda:us-east-2:526810320200:function:test-lambda
    events: ["s3:ObjectCreated:*", "s3:ObjectRemoved:*"]
    prefix: images/
    suffix: .jpg

- name: Setup bucket event notification to SQS
  community.aws.s3_bucket_notification:
    state: present
    event_name: on_file_add_or_remove
    bucket_name: test-bucket
    queue_arn: arn:aws:sqs:us-east-2:526810320200:test-queue
    events: ["s3:ObjectCreated:*", "s3:ObjectRemoved:*"]
    prefix: images/
    suffix: .jpg

# Example removing an event notification
- name: Remove event notification
  community.aws.s3_bucket_notification:
    state: absent
    event_name: on_file_add_or_remove
    bucket_name: test-bucket
```

## [Return Values](s3_bucket_notification_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **notification_configuration**  complex | dictionary of currently applied notifications  Returned: success |
| **lambda_function_configurations**  list / elements=string | List of current Lambda function notification configurations applied to the bucket.  Returned: success |
| **queue_configurations**  list / elements=string | List of current SQS notification configurations applied to the bucket.  Returned: success |
| **topic_configurations**  list / elements=string | List of current SNS notification configurations applied to the bucket.  Returned: success |

### Authors

- XLAB d.o.o. (@xlab-si)
- Aljaz Kosir (@aljazkosir)
- Miha Plesko (@miha-plesko)
- Mark Woolley (@marknet15)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
