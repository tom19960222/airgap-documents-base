---
collection: ansible
version: "8"
title: "community.aws.kinesis_stream module – Manage a Kinesis Stream."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/kinesis_stream_module.html
fetched_at: 2026-07-28T01:41:28+00:00
---
# community.aws.kinesis_stream module – Manage a Kinesis Stream.

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
> see [Requirements](kinesis_stream_module.md#ansible-collections-community-aws-kinesis-stream-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.kinesis_stream`.

New in community.aws 1.0.0

- [Synopsis](kinesis_stream_module.md#synopsis)
- [Requirements](kinesis_stream_module.md#requirements)
- [Parameters](kinesis_stream_module.md#parameters)
- [Notes](kinesis_stream_module.md#notes)
- [Examples](kinesis_stream_module.md#examples)
- [Return Values](kinesis_stream_module.md#return-values)

## [Synopsis](kinesis_stream_module.md#id1)

- Create or Delete a Kinesis Stream.
- Update the retention period of a Kinesis Stream.
- Update Tags on a Kinesis Stream.
- Enable/disable server side encryption on a Kinesis Stream.

## [Requirements](kinesis_stream_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](kinesis_stream_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **encryption_state**  string | Enable or Disable encryption on the Kinesis Stream.  **Choices:**   - `"enabled"` - `"disabled"` |
| **encryption_type**  string | The type of encryption.  Defaults to `KMS`  **Choices:**   - `"KMS"` - `"NONE"` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **key_id**  string | The GUID or alias for the KMS key. |
| **name**  string / required | The name of the Kinesis Stream you are managing. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **retention_period**  integer | The length of time (in hours) data records are accessible after they are added to the stream.  The default retention period is 24 hours and can not be less than 24 hours.  The maximum retention period is 168 hours.  The retention period can be modified during any point in time. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **shards**  integer | The number of shards you want to have with this stream.  This is required when *state=present* |
| **state**  string | Create or Delete the Kinesis Stream.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary of resource tags of the form: `{ tag1: value1, tag2: value2 }`. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for operation to complete before returning.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How many seconds to wait for an operation to complete before timing out.  **Default:** `300` |

## [Notes](kinesis_stream_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](kinesis_stream_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic creation example:
- name: Set up Kinesis Stream with 10 shards and wait for the stream to become ACTIVE
  community.aws.kinesis_stream:
    name: test-stream
    shards: 10
    wait: true
    wait_timeout: 600
  register: test_stream

# Basic creation example with tags:
- name: Set up Kinesis Stream with 10 shards, tag the environment, and wait for the stream to become ACTIVE
  community.aws.kinesis_stream:
    name: test-stream
    shards: 10
    tags:
      Env: development
    wait: true
    wait_timeout: 600
  register: test_stream

# Basic creation example with tags and increase the retention period from the default 24 hours to 48 hours:
- name: Set up Kinesis Stream with 10 shards, tag the environment, increase the retention period and wait for the stream to become ACTIVE
  community.aws.kinesis_stream:
    name: test-stream
    retention_period: 48
    shards: 10
    tags:
      Env: development
    wait: true
    wait_timeout: 600
  register: test_stream

# Basic delete example:
- name: Delete Kinesis Stream test-stream and wait for it to finish deleting.
  community.aws.kinesis_stream:
    name: test-stream
    state: absent
    wait: true
    wait_timeout: 600
  register: test_stream

# Basic enable encryption example:
- name: Encrypt Kinesis Stream test-stream.
  community.aws.kinesis_stream:
    name: test-stream
    state: present
    shards: 1
    encryption_state: enabled
    encryption_type: KMS
    key_id: alias/aws/kinesis
    wait: true
    wait_timeout: 600
  register: test_stream

# Basic disable encryption example:
- name: Encrypt Kinesis Stream test-stream.
  community.aws.kinesis_stream:
    name: test-stream
    state: present
    shards: 1
    encryption_state: disabled
    encryption_type: KMS
    key_id: alias/aws/kinesis
    wait: true
    wait_timeout: 600
  register: test_stream
```

## [Return Values](kinesis_stream_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **retention_period_hours**  integer | Number of hours messages will be kept for a Kinesis Stream.  **Returned:** when state == present.  **Sample:** `24` |
| **stream_arn**  string | The amazon resource identifier  **Returned:** when state == present.  **Sample:** `"arn:aws:kinesis:east-side:123456789:stream/test-stream"` |
| **stream_name**  string | The name of the Kinesis Stream.  **Returned:** when state == present.  **Sample:** `"test-stream"` |
| **stream_status**  string | The current state of the Kinesis Stream.  **Returned:** when state == present.  **Sample:** `"ACTIVE"` |
| **tags**  dictionary | Dictionary containing all the tags associated with the Kinesis stream.  **Returned:** when state == present.  **Sample:** `{"Env": "development", "Name": "Splunk"}` |

### Authors

- Allen Sanabria (@linuxdynasty)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
