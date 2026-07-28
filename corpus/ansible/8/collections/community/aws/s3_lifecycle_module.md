---
collection: ansible
version: "8"
title: "community.aws.s3_lifecycle module – Manage S3 bucket lifecycle rules in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/s3_lifecycle_module.html
fetched_at: 2026-07-28T01:41:49+00:00
---
# community.aws.s3_lifecycle module – Manage S3 bucket lifecycle rules in AWS

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](s3_lifecycle_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **abort_incomplete_multipart_upload_days**  integer  *added in community.aws 2.2.0* | Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before permanently removing all parts of the upload. |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **expiration_date**  string | Indicates the lifetime of the objects that are subject to the rule by the date they will expire.  The value must be ISO-8601 format, the time must be midnight and a GMT timezone must be specified.  This cannot be specified with *expire_object_delete_marker* |
| **expiration_days**  integer | Indicates the lifetime, in days, of the objects that are subject to the rule.  The value must be a non-zero positive integer.  This cannot be specified with *expire_object_delete_marker* |
| **expire_object_delete_marker**  boolean  *added in community.aws 2.2.0* | Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions.  If set to `true`, the delete marker will be expired; if set to `false` the policy takes no action.  This cannot be specified with *expiration_days* or *expiration_date*.  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the S3 bucket. |
| **noncurrent_version_expiration_days**  integer | The number of days after which non-current versions should be deleted.  Must be set if *noncurrent_version_keep_newer* is set. |
| **noncurrent_version_keep_newer**  integer  *added in community.aws 5.3.0* | The minimum number of non-current versions to retain.  Requires `botocore >= 1.23.12`  Requres *noncurrent_version_expiration_days*. |
| **noncurrent_version_storage_class**  string | The storage class to which non-current versions are transitioned.  **Choices:**   - `"glacier"` ← (default) - `"onezone_ia"` - `"standard_ia"` - `"intelligent_tiering"` - `"deep_archive"` |
| **noncurrent_version_transition_days**  integer | The number of days after which non-current versions will be transitioned to the storage class specified in *noncurrent_version_storage_class*. |
| **noncurrent_version_transitions**  list / elements=dictionary | A list of transition behaviors to be applied to noncurrent versions for the rule.  Each storage class may be used only once. Each transition behavior contains these elements *transition_days* *storage_class* |
| **prefix**  string | Prefix identifying one or more objects to which the rule applies.  If no prefix is specified, the rule will apply to the whole bucket. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_transitions**  boolean | Whether to replace all the current transition(s) with the new transition(s).  When `false`, the provided transition(s) will be added, replacing transitions with the same storage_class. When true, existing transitions will be removed and replaced with the new transition(s)  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **rule_id**  string | Unique identifier for the rule.  The value cannot be longer than 255 characters.  A unique value for the rule will be generated if no value is provided. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or remove the lifecycle rule.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **status**  string | If `enabled`, the rule is currently being applied.  If `disabled`, the rule is not currently being applied.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |
| **storage_class**  string | The storage class to transition to.  **Choices:**   - `"glacier"` ← (default) - `"onezone_ia"` - `"standard_ia"` - `"intelligent_tiering"` - `"deep_archive"` |
| **transition_date**  string | Indicates the lifetime of the objects that are subject to the rule by the date they will transition to a different storage class.  The value must be ISO-8601 format, the time must be midnight and a GMT timezone must be specified.  If (transition_days) is not specified, this parameter is required. |
| **transition_days**  integer | Indicates when, in days, an object transitions to a different storage class.  If *transition_date* is not specified, this parameter is required. |
| **transitions**  list / elements=dictionary | A list of transition behaviors to be applied to the rule.  Each storage class may be used only once. Each transition behavior may contain these elements *transition_days* *transition_date* *storage_class* |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean  *added in community.aws 1.5.0* | Wait for the configuration to complete before returning.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](s3_lifecycle_module.md#id4)

> **Note:**
>
> - If specifying expiration time as days then transition time must also be specified in days.
> - If specifying expiration time as a date then transition time must also be specified as a date.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
