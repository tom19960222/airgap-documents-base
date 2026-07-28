---
collection: ansible
version: "8"
title: "community.aws.autoscaling_lifecycle_hook module – Create, delete or update AWS ASG Lifecycle Hooks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/autoscaling_lifecycle_hook_module.html
fetched_at: 2026-07-28T01:40:12+00:00
---
# community.aws.autoscaling_lifecycle_hook module – Create, delete or update AWS ASG Lifecycle Hooks

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
> see [Requirements](autoscaling_lifecycle_hook_module.md#ansible-collections-community-aws-autoscaling-lifecycle-hook-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.autoscaling_lifecycle_hook`.

New in community.aws 1.0.0

- [Synopsis](autoscaling_lifecycle_hook_module.md#synopsis)
- [Requirements](autoscaling_lifecycle_hook_module.md#requirements)
- [Parameters](autoscaling_lifecycle_hook_module.md#parameters)
- [Notes](autoscaling_lifecycle_hook_module.md#notes)
- [Examples](autoscaling_lifecycle_hook_module.md#examples)
- [Return Values](autoscaling_lifecycle_hook_module.md#return-values)

## [Synopsis](autoscaling_lifecycle_hook_module.md#id1)

- Will create a new hook when *state=present* and no given Hook is found.
- Will update an existing hook when *state=present* and a Hook is found, but current and provided parameters differ.
- Will delete the hook when *state=absent* and a Hook is found.
- Prior to release 5.0.0 this module was called `community.aws.ec2_asg_lifecycle_hook`. The usage did not change.

Aliases: ec2_asg_lifecycle_hook

## [Requirements](autoscaling_lifecycle_hook_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](autoscaling_lifecycle_hook_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **autoscaling_group_name**  string / required | The name of the Auto Scaling group to which you want to assign the lifecycle hook. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **default_result**  string | Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs.  **Choices:**   - `"ABANDON"` ← (default) - `"CONTINUE"` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **heartbeat_timeout**  integer | The amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the default action. You can prevent the lifecycle hook from timing out by calling RecordLifecycleActionHeartbeat.  By default Amazon AWS will use `3600` (1 hour). |
| **lifecycle_hook_name**  string / required | The name of the lifecycle hook. |
| **notification_meta_data**  string | Contains additional information that you want to include any time Auto Scaling sends a message to the notification target. |
| **notification_target_arn**  string | The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook.  This target can be either an SQS queue or an SNS topic.  If you specify an empty string, this overrides the current ARN. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **role_arn**  string | The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or delete Lifecycle Hook.  When *state=present* updates existing hook or creates a new hook if not found.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **transition**  string | The instance state to which you want to attach the lifecycle hook.  Required when *state=present*.  **Choices:**   - `"autoscaling:EC2_INSTANCE_TERMINATING"` - `"autoscaling:EC2_INSTANCE_LAUNCHING"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](autoscaling_lifecycle_hook_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](autoscaling_lifecycle_hook_module.md#id5)

```yaml+jinja
- name: Create / Update lifecycle hook
  community.aws.autoscaling_lifecycle_hook:
    region: eu-central-1
    state: present
    autoscaling_group_name: example
    lifecycle_hook_name: example
    transition: autoscaling:EC2_INSTANCE_LAUNCHING
    heartbeat_timeout: 7000
    default_result: ABANDON

- name: Delete lifecycle hook
  community.aws.autoscaling_lifecycle_hook:
    region: eu-central-1
    state: absent
    autoscaling_group_name: example
    lifecycle_hook_name: example
```

## [Return Values](autoscaling_lifecycle_hook_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auto_scaling_group_name**  string | The unique name of the auto scaling group.  **Returned:** success  **Sample:** `"myasg"` |
| **default_result**  string | Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs.  **Returned:** success  **Sample:** `"CONTINUE"` |
| **global_timeout**  integer | The maximum time, in seconds, that an instance can remain in a `Pending:Wait` or `Terminating:Wait` state.  **Returned:** success  **Sample:** `172800` |
| **heartbeat_timeout**  integer | The maximum time, in seconds, that can elapse before the lifecycle hook times out.  **Returned:** success  **Sample:** `3600` |
| **lifecycle_hook_name**  string | The name of the lifecycle hook.  **Returned:** success  **Sample:** `"mylifecyclehook"` |
| **lifecycle_transition**  string | The instance state to which lifecycle hook should be attached.  **Returned:** success  **Sample:** `"autoscaling:EC2_INSTANCE_LAUNCHING"` |

### Authors

- Igor ‘Tsigankov’ Eyrich (@tsiganenok)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
