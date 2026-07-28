---
collection: ansible
version: "6"
title: "amazon.aws.aws_resource_actions callback – summarizes all “resource:actions” completed"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/aws_resource_actions_callback.html
fetched_at: 2026-07-27T16:43:55+00:00
---
# amazon.aws.aws_resource_actions callback – summarizes all “resource:actions” completed

> **Note:**
>
> This callback plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](aws_resource_actions_callback.md#ansible-collections-amazon-aws-aws-resource-actions-callback-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.aws_resource_actions`.

- [Callback plugin](aws_resource_actions_callback.md#callback-plugin)
- [Synopsis](aws_resource_actions_callback.md#synopsis)
- [Requirements](aws_resource_actions_callback.md#requirements)
- [Examples](aws_resource_actions_callback.md#examples)

## [Callback plugin](aws_resource_actions_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](aws_resource_actions_callback.md#id2)

- Ansible callback plugin for collecting the AWS actions completed by all boto3 modules using AnsibleAWSModule in a playbook. Botocore endpoint logs need to be enabled for those modules, which can be done easily by setting debug_botocore_endpoint_logs to True for group/aws using module_defaults.

## [Requirements](aws_resource_actions_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration - see examples section below for details.

## [Examples](aws_resource_actions_callback.md#id4)

```yaml+jinja
example: >
  To enable, add this to your ansible.cfg file in the defaults block
    [defaults]
    callback_whitelist = aws_resource_actions
sample output: >
#
# AWS ACTIONS: ['s3:PutBucketAcl', 's3:HeadObject', 's3:DeleteObject', 's3:PutObjectAcl', 's3:CreateMultipartUpload',
#               's3:DeleteBucket', 's3:GetObject', 's3:DeleteObjects', 's3:CreateBucket', 's3:CompleteMultipartUpload',
#               's3:ListObjectsV2', 's3:HeadBucket', 's3:UploadPart', 's3:PutObject']
#
sample output: >
#
# AWS ACTIONS: ['ec2:DescribeVpcAttribute', 'ec2:DescribeVpcClassicLink', 'ec2:ModifyVpcAttribute', 'ec2:CreateTags',
#               'sts:GetCallerIdentity', 'ec2:DescribeSecurityGroups', 'ec2:DescribeTags', 'ec2:DescribeVpcs', 'ec2:CreateVpc']
#
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
