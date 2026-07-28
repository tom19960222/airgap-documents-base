---
collection: ansible
version: "6"
title: "community.aws.kinesis_stream module – Manage a Kinesis Stream."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/kinesis_stream_module.html
fetched_at: 2026-07-27T17:04:44+00:00
---
# community.aws.kinesis_stream module – Manage a Kinesis Stream.

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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](kinesis_stream_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **encryption_state**  string | Enable or Disable encryption on the Kinesis Stream.  Choices:   - `"enabled"` - `"disabled"` |
| **encryption_type**  string | The type of encryption.  Defaults to `KMS`  Choices:   - `"KMS"` - `"NONE"` |
| **key_id**  string | The GUID or alias for the KMS key. |
| **name**  string / required | The name of the Kinesis Stream you are managing. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **retention_period**  integer | The length of time (in hours) data records are accessible after they are added to the stream.  The default retention period is 24 hours and can not be less than 24 hours.  The maximum retention period is 168 hours.  The retention period can be modified during any point in time. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **shards**  integer | The number of shards you want to have with this stream.  This is required when *state=present* |
| **state**  string | Create or Delete the Kinesis Stream.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary of resource tags of the form: `{ tag1: value1, tag2: value2 }`. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Wait for operation to complete before returning.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How many seconds to wait for an operation to complete before timing out.  Default: `300` |

## [Notes](kinesis_stream_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](kinesis_stream_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic creation example:
- name: Set up Kinesis Stream with 10 shards and wait for the stream to become ACTIVE
  community.aws.kinesis_stream:
    name: test-stream
    shards: 10
    wait: yes
    wait_timeout: 600
  register: test_stream

# Basic creation example with tags:
- name: Set up Kinesis Stream with 10 shards, tag the environment, and wait for the stream to become ACTIVE
  community.aws.kinesis_stream:
    name: test-stream
    shards: 10
    tags:
      Env: development
    wait: yes
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
    wait: yes
    wait_timeout: 600
  register: test_stream

# Basic delete example:
- name: Delete Kinesis Stream test-stream and wait for it to finish deleting.
  community.aws.kinesis_stream:
    name: test-stream
    state: absent
    wait: yes
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
    wait: yes
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
    wait: yes
    wait_timeout: 600
  register: test_stream
```

## [Return Values](kinesis_stream_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **retention_period_hours**  integer | Number of hours messages will be kept for a Kinesis Stream.  Returned: when state == present.  Sample: `24` |
| **stream_arn**  string | The amazon resource identifier  Returned: when state == present.  Sample: `"arn:aws:kinesis:east-side:123456789:stream/test-stream"` |
| **stream_name**  string | The name of the Kinesis Stream.  Returned: when state == present.  Sample: `"test-stream"` |
| **stream_status**  string | The current state of the Kinesis Stream.  Returned: when state == present.  Sample: `"ACTIVE"` |
| **tags**  dictionary | Dictionary containing all the tags associated with the Kinesis stream.  Returned: when state == present.  Sample: `{"Env": "development", "Name": "Splunk"}` |

### Authors

- Allen Sanabria (@linuxdynasty)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
