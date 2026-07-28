---
collection: ansible
version: "8"
title: "community.aws.s3_bucket_notification module – Creates, updates or deletes S3 Bucket notifications targeting Lambda functions, SNS or SQS."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/s3_bucket_notification_module.html
fetched_at: 2026-07-28T01:41:47+00:00
---
# community.aws.s3_bucket_notification module – Creates, updates or deletes S3 Bucket notifications targeting Lambda functions, SNS or SQS.

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](s3_bucket_notification_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **bucket_name**  string / required | S3 bucket name. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **event_name**  string / required | Unique name for event notification on bucket. |
| **events**  list / elements=string | Events that will be triggering a notification. You can select multiple events to send to the same destination, you can set up different events to send to different destinations, and you can set up a prefix or suffix for an event. However, for each bucket, individual events cannot have multiple configurations with overlapping prefixes or suffixes that could match the same object key.  Required when *state=present*.  **Choices:**   - `"s3:ObjectCreated:*"` - `"s3:ObjectCreated:Put"` - `"s3:ObjectCreated:Post"` - `"s3:ObjectCreated:Copy"` - `"s3:ObjectCreated:CompleteMultipartUpload"` - `"s3:ObjectRemoved:*"` - `"s3:ObjectRemoved:Delete"` - `"s3:ObjectRemoved:DeleteMarkerCreated"` - `"s3:ObjectRestore:Post"` - `"s3:ObjectRestore:Completed"` - `"s3:ReducedRedundancyLostObject"`   **Default:** `[]` |
| **lambda_alias**  string | Name of the Lambda function alias.  Mutually exclusive with *lambda_version*. |
| **lambda_function_arn**  aliases: function_arn  string | The ARN of the lambda function.  Mutually exclusive with *queue_arn* and *topic_arn*. |
| **lambda_version**  integer | Version of the Lambda function.  Mutually exclusive with *lambda_alias*.  **Default:** `0` |
| **prefix**  string | Optional prefix to limit the notifications to objects with keys that start with matching characters.  **Default:** `""` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **queue_arn**  string  *added in community.aws 3.2.0* | The ARN of the SQS queue.  Mutually exclusive with *topic_arn* and *lambda_function_arn*. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Describes the desired state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **suffix**  string | Optional suffix to limit the notifications to objects with keys that end with matching characters.  **Default:** `""` |
| **topic_arn**  string  *added in community.aws 3.2.0* | The ARN of the SNS topic.  Mutually exclusive with *queue_arn* and *lambda_function_arn*. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](s3_bucket_notification_module.md#id4)

> **Note:**
>
> - If using Lambda function as the target then a Lambda policy is also needed, use [community.aws.lambda_policy](lambda_policy_module.md#ansible-collections-community-aws-lambda-policy-module) to do so to allow `lambda:InvokeFunction` for the notification.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](s3_bucket_notification_module.md#id5)

```yaml+jinja
---
# Examples adding notification target configs to a S3 bucket
- name: Setup bucket event notification to a Lambda function
  community.aws.s3_bucket_notification:
    state: present
    event_name: on_file_add_or_remove
    bucket_name: test-bucket
    lambda_function_arn: arn:aws:lambda:us-east-2:123456789012:function:test-lambda
    events: ["s3:ObjectCreated:*", "s3:ObjectRemoved:*"]
    prefix: images/
    suffix: .jpg

- name: Setup bucket event notification to SQS
  community.aws.s3_bucket_notification:
    state: present
    event_name: on_file_add_or_remove
    bucket_name: test-bucket
    queue_arn: arn:aws:sqs:us-east-2:123456789012:test-queue
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
| **notification_configuration**  complex | dictionary of currently applied notifications  **Returned:** success |
| **lambda_function_configurations**  list / elements=string | List of current Lambda function notification configurations applied to the bucket.  **Returned:** success |
| **queue_configurations**  list / elements=string | List of current SQS notification configurations applied to the bucket.  **Returned:** success |
| **topic_configurations**  list / elements=string | List of current SNS notification configurations applied to the bucket.  **Returned:** success |

### Authors

- XLAB d.o.o. (@xlab-si)
- Aljaz Kosir (@aljazkosir)
- Miha Plesko (@miha-plesko)
- Mark Woolley (@marknet15)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
