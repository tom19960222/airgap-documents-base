---
collection: ansible
version: "6"
title: "community.aws.s3_metrics_configuration module – Manage s3 bucket metrics configuration in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/s3_metrics_configuration_module.html
fetched_at: 2026-07-27T17:05:03+00:00
---
# community.aws.s3_metrics_configuration module – Manage s3 bucket metrics configuration in AWS

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
> see [Requirements](s3_metrics_configuration_module.md#ansible-collections-community-aws-s3-metrics-configuration-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.s3_metrics_configuration`.

New in community.aws 1.3.0

- [Synopsis](s3_metrics_configuration_module.md#synopsis)
- [Requirements](s3_metrics_configuration_module.md#requirements)
- [Parameters](s3_metrics_configuration_module.md#parameters)
- [Notes](s3_metrics_configuration_module.md#notes)
- [Examples](s3_metrics_configuration_module.md#examples)

## [Synopsis](s3_metrics_configuration_module.md#id1)

- Manage s3 bucket metrics configuration in AWS which allows to get the CloudWatch request metrics for the objects in a bucket

## [Requirements](s3_metrics_configuration_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](s3_metrics_configuration_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bucket_name**  string / required | Name of the s3 bucket |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filter_prefix**  string | A prefix used when evaluating a metrics filter |
| **filter_tags**  aliases: filter_tag  dictionary | A dictionary of one or more tags used when evaluating a metrics filter |
| **id**  string / required | The ID used to identify the metrics configuration |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or delete metrics configuration  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](s3_metrics_configuration_module.md#id4)

> **Note:**
>
> - This modules manages single metrics configuration, the s3 bucket might have up to 1,000 metrics configurations
> - To request metrics for the entire bucket, create a metrics configuration without a filter
> - Metrics configurations are necessary only to enable request metric, bucket-level daily storage metrics are always turned on
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](s3_metrics_configuration_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create a metrics configuration that enables metrics for an entire bucket
  community.aws.s3_metrics_configuration:
    bucket_name: my-bucket
    id: EntireBucket
    state: present

- name: Put a metrics configuration that enables metrics for objects starting with a prefix
  community.aws.s3_metrics_configuration:
    bucket_name: my-bucket
    id: Assets
    filter_prefix: assets
    state: present

- name: Put a metrics configuration that enables metrics for objects with specific tag
  community.aws.s3_metrics_configuration:
    bucket_name: my-bucket
    id: Assets
    filter_tag:
      kind: asset
    state: present

- name: Put a metrics configuration that enables metrics for objects that start with a particular prefix and have specific tags applied
  community.aws.s3_metrics_configuration:
    bucket_name: my-bucket
    id: ImportantBlueDocuments
    filter_prefix: documents
    filter_tags:
      priority: high
      class: blue
    state: present

- name: Delete metrics configuration
  community.aws.s3_metrics_configuration:
    bucket_name: my-bucket
    id: EntireBucket
    state: absent
```

### Authors

- Dmytro Vorotyntsev (@vorotech)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
