---
collection: ansible
version: "6"
title: "community.aws.s3_lifecycle module – Manage S3 bucket lifecycle rules in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/s3_lifecycle_module.html
fetched_at: 2026-07-27T17:05:02+00:00
---
# community.aws.s3_lifecycle module – Manage S3 bucket lifecycle rules in AWS

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
> see [Requirements](s3_lifecycle_module.md#ansible-collections-community-aws-s3-lifecycle-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.s3_lifecycle`.

New in community.aws 1.0.0

- [Synopsis](s3_lifecycle_module.md#synopsis)
- [Requirements](s3_lifecycle_module.md#requirements)
- [Parameters](s3_lifecycle_module.md#parameters)
- [Notes](s3_lifecycle_module.md#notes)
- [Examples](s3_lifecycle_module.md#examples)

## [Synopsis](s3_lifecycle_module.md#id1)

- Manage S3 bucket lifecycle rules in AWS.

## [Requirements](s3_lifecycle_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](s3_lifecycle_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **abort_incomplete_multipart_upload_days**  integer  added in community.aws 2.2.0 | Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **expiration_date**  string | Indicates the lifetime of the objects that are subject to the rule by the date they will expire.  The value must be ISO-8601 format, the time must be midnight and a GMT timezone must be specified.  This cannot be specified with *expire_object_delete_marker* |
| **expiration_days**  integer | Indicates the lifetime, in days, of the objects that are subject to the rule.  The value must be a non-zero positive integer.  This cannot be specified with *expire_object_delete_marker* |
| **expire_object_delete_marker**  boolean  added in community.aws 2.2.0 | Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions.  If set to `true`, the delete marker will be expired; if set to `false` the policy takes no action.  This cannot be specified with *expiration_days* or *expiration_date*.  Choices:   - `false` - `true` |
| **name**  string / required | Name of the S3 bucket. |
| **noncurrent_version_expiration_days**  integer | The number of days after which non-current versions should be deleted. |
| **noncurrent_version_storage_class**  string | The storage class to which non-current versions are transitioned.  Choices:   - `"glacier"` ← (default) - `"onezone_ia"` - `"standard_ia"` - `"intelligent_tiering"` - `"deep_archive"` |
| **noncurrent_version_transition_days**  integer | The number of days after which non-current versions will be transitioned to the storage class specified in *noncurrent_version_storage_class*. |
| **noncurrent_version_transitions**  list / elements=dictionary | A list of transition behaviors to be applied to noncurrent versions for the rule.  Each storage class may be used only once. Each transition behavior contains these elements *transition_days* *storage_class* |
| **prefix**  string | Prefix identifying one or more objects to which the rule applies.  If no prefix is specified, the rule will apply to the whole bucket. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_transitions**  boolean | Whether to replace all the current transition(s) with the new transition(s).  When `false`, the provided transition(s) will be added, replacing transitions with the same storage_class. When true, existing transitions will be removed and replaced with the new transition(s)  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **requester_pays**  boolean | The *requester_pays* option does nothing and will be removed after 2022-06-01  Choices:   - `false` - `true` |
| **rule_id**  string | Unique identifier for the rule.  The value cannot be longer than 255 characters.  A unique value for the rule will be generated if no value is provided. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or remove the lifecycle rule.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | If `enabled`, the rule is currently being applied.  If `disabled`, the rule is not currently being applied.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **storage_class**  string | The storage class to transition to.  Choices:   - `"glacier"` ← (default) - `"onezone_ia"` - `"standard_ia"` - `"intelligent_tiering"` - `"deep_archive"` |
| **transition_date**  string | Indicates the lifetime of the objects that are subject to the rule by the date they will transition to a different storage class.  The value must be ISO-8601 format, the time must be midnight and a GMT timezone must be specified.  If (transition_days) is not specified, this parameter is required. |
| **transition_days**  integer | Indicates when, in days, an object transitions to a different storage class.  If *transition_date* is not specified, this parameter is required. |
| **transitions**  list / elements=dictionary | A list of transition behaviors to be applied to the rule.  Each storage class may be used only once. Each transition behavior may contain these elements *transition_days* *transition_date* *storage_class* |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean  added in community.aws 1.5.0 | Wait for the configuration to complete before returning.  Choices:   - `false` ← (default) - `true` |

## [Notes](s3_lifecycle_module.md#id4)

> **Note:**
>
> - If specifying expiration time as days then transition time must also be specified in days.
> - If specifying expiration time as a date then transition time must also be specified as a date.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](s3_lifecycle_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Configure a lifecycle rule on a bucket to expire (delete) items with a prefix of /logs/ after 30 days
  community.aws.s3_lifecycle:
    name: mybucket
    expiration_days: 30
    prefix: logs/
    status: enabled
    state: present

- name: Configure a lifecycle rule to transition all items with a prefix of /logs/ to glacier after 7 days and then delete after 90 days
  community.aws.s3_lifecycle:
    name: mybucket
    transition_days: 7
    expiration_days: 90
    prefix: logs/
    status: enabled
    state: present

# Note that midnight GMT must be specified.
# Be sure to quote your date strings
- name: Configure a lifecycle rule to transition all items with a prefix of /logs/ to glacier on 31 Dec 2020 and then delete on 31 Dec 2030.
  community.aws.s3_lifecycle:
    name: mybucket
    transition_date: "2020-12-30T00:00:00.000Z"
    expiration_date: "2030-12-30T00:00:00.000Z"
    prefix: logs/
    status: enabled
    state: present

- name: Disable the rule created above
  community.aws.s3_lifecycle:
    name: mybucket
    prefix: logs/
    status: disabled
    state: present

- name: Delete the lifecycle rule created above
  community.aws.s3_lifecycle:
    name: mybucket
    prefix: logs/
    state: absent

- name: Configure a lifecycle rule to transition all backup files older than 31 days in /backups/ to standard infrequent access class.
  community.aws.s3_lifecycle:
    name: mybucket
    prefix: backups/
    storage_class: standard_ia
    transition_days: 31
    state: present
    status: enabled

- name: Configure a lifecycle rule to transition files to infrequent access after 30 days and glacier after 90
  community.aws.s3_lifecycle:
    name: mybucket
    prefix: logs/
    state: present
    status: enabled
    transitions:
      - transition_days: 30
        storage_class: standard_ia
      - transition_days: 90
        storage_class: glacier
```

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
