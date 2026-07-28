---
collection: ansible
version: "6"
title: "community.aws.ec2_asg_lifecycle_hook module – Create, delete or update AWS ASG Lifecycle Hooks."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_asg_lifecycle_hook_module.html
fetched_at: 2026-07-27T17:03:55+00:00
---
# community.aws.ec2_asg_lifecycle_hook module – Create, delete or update AWS ASG Lifecycle Hooks.

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
> see [Requirements](ec2_asg_lifecycle_hook_module.md#ansible-collections-community-aws-ec2-asg-lifecycle-hook-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_asg_lifecycle_hook`.

New in community.aws 1.0.0

- [Synopsis](ec2_asg_lifecycle_hook_module.md#synopsis)
- [Requirements](ec2_asg_lifecycle_hook_module.md#requirements)
- [Parameters](ec2_asg_lifecycle_hook_module.md#parameters)
- [Notes](ec2_asg_lifecycle_hook_module.md#notes)
- [Examples](ec2_asg_lifecycle_hook_module.md#examples)

## [Synopsis](ec2_asg_lifecycle_hook_module.md#id1)

- Will create a new hook when *state=present* and no given Hook is found.
- Will update an existing hook when *state=present* and a Hook is found, but current and provided parameters differ.
- Will delete the hook when *state=absent* and a Hook is found.

## [Requirements](ec2_asg_lifecycle_hook_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_asg_lifecycle_hook_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autoscaling_group_name**  string / required | The name of the Auto Scaling group to which you want to assign the lifecycle hook. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **default_result**  string | Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs.  Choices:   - `"ABANDON"` ← (default) - `"CONTINUE"` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **heartbeat_timeout**  integer | The amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling RecordLifecycleActionHeartbeat.  By default Amazon AWS will use 3600 (1 hour) |
| **lifecycle_hook_name**  string / required | The name of the lifecycle hook. |
| **notification_meta_data**  string | Contains additional information that you want to include any time Auto Scaling sends a message to the notification target. |
| **notification_target_arn**  string | The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook.  This target can be either an SQS queue or an SNS topic.  If you specify an empty string, this overrides the current ARN. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **role_arn**  string | The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or delete Lifecycle Hook.  When *state=present* updates existing hook or creates a new hook if not found.  Choices:   - `"present"` ← (default) - `"absent"` |
| **transition**  string | The instance state to which you want to attach the lifecycle hook.  Required when *state=present*.  Choices:   - `"autoscaling:EC2_INSTANCE_TERMINATING"` - `"autoscaling:EC2_INSTANCE_LAUNCHING"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_asg_lifecycle_hook_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_asg_lifecycle_hook_module.md#id5)

```yaml+jinja
- name: Create / Update lifecycle hook
  community.aws.ec2_asg_lifecycle_hook:
    region: eu-central-1
    state: present
    autoscaling_group_name: example
    lifecycle_hook_name: example
    transition: autoscaling:EC2_INSTANCE_LAUNCHING
    heartbeat_timeout: 7000
    default_result: ABANDON

- name: Delete lifecycle hook
  community.aws.ec2_asg_lifecycle_hook:
    region: eu-central-1
    state: absent
    autoscaling_group_name: example
    lifecycle_hook_name: example
```

### Authors

- Igor ‘Tsigankov’ Eyrich (@tsiganenok)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
