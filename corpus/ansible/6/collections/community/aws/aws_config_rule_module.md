---
collection: ansible
version: "6"
title: "community.aws.aws_config_rule module – Manage AWS Config resources"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_config_rule_module.html
fetched_at: 2026-07-27T17:03:20+00:00
---
# community.aws.aws_config_rule module – Manage AWS Config resources

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
> see [Requirements](aws_config_rule_module.md#ansible-collections-community-aws-aws-config-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_config_rule`.

New in community.aws 1.0.0

- [Synopsis](aws_config_rule_module.md#synopsis)
- [Requirements](aws_config_rule_module.md#requirements)
- [Parameters](aws_config_rule_module.md#parameters)
- [Notes](aws_config_rule_module.md#notes)
- [Examples](aws_config_rule_module.md#examples)

## [Synopsis](aws_config_rule_module.md#id1)

- Module manages AWS Config rules

## [Requirements](aws_config_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_config_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | The description that you provide for the AWS Config rule. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **execution_frequency**  string | The maximum frequency with which AWS Config runs evaluations for a rule.  Choices:   - `"One_Hour"` - `"Three_Hours"` - `"Six_Hours"` - `"Twelve_Hours"` - `"TwentyFour_Hours"` |
| **input_parameters**  string | A string, in JSON format, that is passed to the AWS Config rule Lambda function. |
| **name**  string / required | The name of the AWS Config resource. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **scope**  dictionary | Defines which resources can trigger an evaluation for the rule. |
| **compliance_id**  string | The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for *compliance_types*. |
| **compliance_types**  string | The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for *compliance_id*. |
| **tag_key**  string | The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule. |
| **tag_value**  string | The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for *tag_value*, you must also specify a value for *tag_key*. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **source**  dictionary / required | Provides the rule owner (AWS or customer), the rule identifier, and the notifications that cause the function to evaluate your AWS resources. |
| **details**  string | Provides the source and type of the event that causes AWS Config to evaluate your AWS resources.  This parameter expects a list of dictionaries. Each dictionary expects the following key/value pairs.  Key `EventSource` The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.  Key `MessageType` The type of notification that triggers AWS Config to run an evaluation for a rule.  Key `MaximumExecutionFrequency` The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. |
| **identifier**  string | The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for *compliance_types*. |
| **owner**  string | The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for *compliance_id*. |
| **state**  string | Whether the Config rule should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](aws_config_rule_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_config_rule_module.md#id5)

```yaml+jinja
- name: Create Config Rule for AWS Config
  community.aws.aws_config_rule:
    name: test_config_rule
    state: present
    description: 'This AWS Config rule checks for public write access on S3 buckets'
    scope:
        compliance_types:
            - 'AWS::S3::Bucket'
    source:
        owner: AWS
        identifier: 'S3_BUCKET_PUBLIC_WRITE_PROHIBITED'
```

### Authors

- Aaron Smith (@slapula)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
