---
collection: ansible
version: "8"
title: "community.aws.sqs_queue module – Creates or deletes AWS SQS queues"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/sqs_queue_module.html
fetched_at: 2026-07-28T01:41:58+00:00
---
# community.aws.sqs_queue module – Creates or deletes AWS SQS queues

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
> see [Requirements](sqs_queue_module.md#ansible-collections-community-aws-sqs-queue-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.sqs_queue`.

New in community.aws 1.0.0

- [Synopsis](sqs_queue_module.md#synopsis)
- [Requirements](sqs_queue_module.md#requirements)
- [Parameters](sqs_queue_module.md#parameters)
- [Notes](sqs_queue_module.md#notes)
- [Examples](sqs_queue_module.md#examples)
- [Return Values](sqs_queue_module.md#return-values)

## [Synopsis](sqs_queue_module.md#id1)

- Create or delete AWS SQS queues.
- Update attributes on existing queues.

## [Requirements](sqs_queue_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](sqs_queue_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **content_based_deduplication**  boolean | Enables content-based deduplication. Used for FIFOs only.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **deduplication_scope**  string  *added in community.aws 5.3.0* | Deduplication scope for FIFO queues.  `messageGroup` is required for high throughput FIFO.  Defaults to `queue` on creation.  **Choices:**   - `"queue"` - `"messageGroup"` |
| **delay_seconds**  aliases: delivery_delay  integer | The delivery delay in seconds. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **fifo_throughput_limit**  string  *added in community.aws 5.3.0* | Throughput limit for FIFO queues.  `perMessageGroupId` is required for high throughput FIFO.  Defaults to `perQueue` on creation.  **Choices:**   - `"perQueue"` - `"perMessageGroupId"` |
| **kms_data_key_reuse_period_seconds**  aliases: kms_data_key_reuse_period  integer | The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. |
| **kms_master_key_id**  string | The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK.  Specifying a valid *kms_master_key_id* will enable encryption automatically. |
| **maximum_message_size**  integer | The maximum message size in bytes. |
| **message_retention_period**  integer | The message retention period in seconds. |
| **name**  string / required | Name of the queue. |
| **policy**  dictionary | Policy to attach to the queue.  Policy body can be YAML or JSON.  This is required for certain use cases for example with S3 bucket notifications. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **queue_type**  string | Standard or FIFO queue.  *queue_type* can only be set at queue creation and will otherwise be ignored.  **Choices:**   - `"standard"` ← (default) - `"fifo"` |
| **receive_message_wait_time_seconds**  aliases: receive_message_wait_time  integer | The receive message wait time in seconds. |
| **redrive_policy**  dictionary | JSON dict with the redrive_policy (see example). |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or delete the queue.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **visibility_timeout**  aliases: default_visibility_timeout  integer | The default visibility timeout in seconds. |

## [Notes](sqs_queue_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](sqs_queue_module.md#id5)

```yaml+jinja
- name: Create SQS queue with redrive policy
  community.aws.sqs_queue:
    name: my-queue
    region: ap-southeast-2
    default_visibility_timeout: 120
    message_retention_period: 86400
    maximum_message_size: 1024
    delivery_delay: 30
    receive_message_wait_time: 20
    policy: "{{ json_dict }}"
    redrive_policy:
      maxReceiveCount: 5
      deadLetterTargetArn: arn:aws:sqs:eu-west-1:123456789012:my-dead-queue

- name: Drop redrive policy
  community.aws.sqs_queue:
    name: my-queue
    region: ap-southeast-2
    redrive_policy: {}

- name: Create FIFO queue
  community.aws.sqs_queue:
    name: fifo-queue
    region: ap-southeast-2
    queue_type: fifo
    content_based_deduplication: true

- name: Tag queue
  community.aws.sqs_queue:
    name: fifo-queue
    region: ap-southeast-2
    tags:
      example: SomeValue

- name: Configure Encryption, automatically uses a new data key every hour
  community.aws.sqs_queue:
    name: fifo-queue
    region: ap-southeast-2
    kms_master_key_id: alias/MyQueueKey
    kms_data_key_reuse_period_seconds: 3600

- name: Example queue allowing s3 bucket notifications
  sqs_queue:
    name: "S3Notifications"
    default_visibility_timeout: 120
    message_retention_period: 86400
    maximum_message_size: 1024
    delivery_delay: 30
    receive_message_wait_time: 20
    policy:
      Version: 2012-10-17
      Id: s3-queue-policy
      Statement:
        - Sid: allowNotifications
          Effect: Allow
          Principal:
            Service: s3.amazonaws.com
          Action:
            - SQS:SendMessage
          Resource: "arn:aws:sqs:*:*:S3Notifications"
          Condition:
            ArnLike:
              aws:SourceArn: "arn:aws:s3:*:*:SomeBucket"

- name: Delete SQS queue
  community.aws.sqs_queue:
    name: my-queue
    region: ap-southeast-2
    state: absent
```

## [Return Values](sqs_queue_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content_based_deduplication**  boolean | Enables content-based deduplication. Used for FIFOs only.  **Returned:** always  **Sample:** `true` |
| **deduplication_scope**  string | The deduplication setting.  **Returned:** always  **Sample:** `"messageGroup"` |
| **delay_seconds**  integer | The delivery delay in seconds.  **Returned:** always  **Sample:** `0` |
| **fifo_throughput_limit**  string | Which throughput limit strategy is applied.  **Returned:** always  **Sample:** `"perQueue"` |
| **kms_data_key_reuse_period_seconds**  integer | The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again.  **Returned:** always  **Sample:** `300` |
| **kms_master_key_id**  string | The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK.  **Returned:** if value exists  **Sample:** `"alias/MyAlias"` |
| **maximum_message_size**  integer | The maximum message size in bytes.  **Returned:** always  **Sample:** `262144` |
| **message_retention_period**  integer | The message retention period in seconds.  **Returned:** always  **Sample:** `345600` |
| **name**  string | Name of the SQS Queue  **Returned:** always  **Sample:** `"queuename-987d2de0"` |
| **queue_arn**  string | The queue’s Amazon resource name (ARN).  **Returned:** on success  **Sample:** `"arn:aws:sqs:us-east-1:123456789012:queuename-987d2de0"` |
| **queue_url**  string | URL to access the queue  **Returned:** on success  **Sample:** `"https://queue.amazonaws.com/123456789012/MyQueue"` |
| **receive_message_wait_time_seconds**  integer | The receive message wait time in seconds.  **Returned:** always  **Sample:** `0` |
| **region**  string | Region that the queue was created within  **Returned:** always  **Sample:** `"us-east-1"` |
| **tags**  dictionary | List of queue tags  **Returned:** always  **Sample:** `{"Env": "prod"}` |
| **visibility_timeout**  integer | The default visibility timeout in seconds.  **Returned:** always  **Sample:** `30` |

### Authors

- Alan Loi (@loia)
- Fernando Jose Pando (@nand0p)
- Nadir Lloret (@nadirollo)
- Dennis Podkovyrin (@sbj-ss)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
