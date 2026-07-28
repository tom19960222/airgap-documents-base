---
collection: ansible
version: "6"
title: "community.aws.sqs_queue module – Creates or deletes AWS SQS queues"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/sqs_queue_module.html
fetched_at: 2026-07-27T17:05:08+00:00
---
# community.aws.sqs_queue module – Creates or deletes AWS SQS queues

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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](sqs_queue_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **content_based_deduplication**  boolean | Enables content-based deduplication. Used for FIFOs only.  Defaults to `false`.  Choices:   - `false` - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delay_seconds**  aliases: delivery_delay  integer | The delivery delay in seconds. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **kms_data_key_reuse_period_seconds**  aliases: kms_data_key_reuse_period  integer | The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. |
| **kms_master_key_id**  string | The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK.  Specifying a valid *kms_master_key_id* will enable encryption automatically. |
| **maximum_message_size**  integer | The maximum message size in bytes. |
| **message_retention_period**  integer | The message retention period in seconds. |
| **name**  string / required | Name of the queue. |
| **policy**  dictionary | Policy to attach to the queue.  Policy body can be YAML or JSON.  This is required for certain use cases for example with S3 bucket notifications. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | Remove tags not listed in *tags*.  Choices:   - `false` ← (default) - `true` |
| **queue_type**  string | Standard or FIFO queue.  *queue_type* can only be set at queue creation and will otherwise be ignored.  Choices:   - `"standard"` ← (default) - `"fifo"` |
| **receive_message_wait_time_seconds**  aliases: receive_message_wait_time  integer | The receive message wait time in seconds. |
| **redrive_policy**  dictionary | JSON dict with the redrive_policy (see example). |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or delete the queue.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | Tag dict to apply to the queue.  To remove all tags set *tags={}* and *purge_tags=true*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **visibility_timeout**  aliases: default_visibility_timeout  integer | The default visibility timeout in seconds. |

## [Notes](sqs_queue_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
    content_based_deduplication: yes

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
| **content_based_deduplication**  boolean | Enables content-based deduplication. Used for FIFOs only.  Returned: always  Sample: `true` |
| **delay_seconds**  integer | The delivery delay in seconds.  Returned: always  Sample: `0` |
| **kms_data_key_reuse_period_seconds**  integer | The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again.  Returned: always  Sample: `300` |
| **kms_master_key_id**  string | The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK.  Returned: if value exists  Sample: `"alias/MyAlias"` |
| **maximum_message_size**  integer | The maximum message size in bytes.  Returned: always  Sample: `262144` |
| **message_retention_period**  integer | The message retention period in seconds.  Returned: always  Sample: `345600` |
| **name**  string | Name of the SQS Queue  Returned: always  Sample: `"queuename-987d2de0"` |
| **queue_arn**  string | The queue’s Amazon resource name (ARN).  Returned: on success  Sample: `"arn:aws:sqs:us-east-1:199999999999:queuename-987d2de0"` |
| **queue_url**  string | URL to access the queue  Returned: on success  Sample: `"https://queue.amazonaws.com/123456789012/MyQueue"` |
| **receive_message_wait_time_seconds**  integer | The receive message wait time in seconds.  Returned: always  Sample: `0` |
| **region**  string | Region that the queue was created within  Returned: always  Sample: `"us-east-1"` |
| **tags**  dictionary | List of queue tags  Returned: always  Sample: `{"Env": "prod"}` |
| **visibility_timeout**  integer | The default visibility timeout in seconds.  Returned: always  Sample: `30` |

### Authors

- Alan Loi (@loia)
- Fernando Jose Pando (@nand0p)
- Nadir Lloret (@nadirollo)
- Dennis Podkovyrin (@sbj-ss)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
