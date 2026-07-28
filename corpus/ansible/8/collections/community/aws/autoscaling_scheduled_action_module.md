---
collection: ansible
version: "8"
title: "community.aws.autoscaling_scheduled_action module – Create, modify and delete ASG scheduled scaling actions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/autoscaling_scheduled_action_module.html
fetched_at: 2026-07-28T01:40:14+00:00
---
# community.aws.autoscaling_scheduled_action module – Create, modify and delete ASG scheduled scaling actions

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
> see [Requirements](autoscaling_scheduled_action_module.md#ansible-collections-community-aws-autoscaling-scheduled-action-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.autoscaling_scheduled_action`.

New in community.aws 2.2.0

- [Synopsis](autoscaling_scheduled_action_module.md#synopsis)
- [Requirements](autoscaling_scheduled_action_module.md#requirements)
- [Parameters](autoscaling_scheduled_action_module.md#parameters)
- [Notes](autoscaling_scheduled_action_module.md#notes)
- [Examples](autoscaling_scheduled_action_module.md#examples)
- [Return Values](autoscaling_scheduled_action_module.md#return-values)

## [Synopsis](autoscaling_scheduled_action_module.md#id1)

- The module will create a new scheduled action when *state=present* and no given action is found.
- The module will update a new scheduled action when *state=present* and the given action is found.
- The module will delete a new scheduled action when *state=absent* and the given action is found.
- Prior to release 5.0.0 this module was called `community.aws.ec2_asg_scheduled_action`. The usage did not change.

Aliases: ec2_asg_scheduled_action

## [Requirements](autoscaling_scheduled_action_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](autoscaling_scheduled_action_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **autoscaling_group_name**  string / required | The name of the autoscaling group to add a scheduled action to. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **desired_capacity**  integer | ASG desired capacity. |
| **end_time**  string | End time for the action. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **max_size**  integer | ASG max capacity. |
| **min_size**  integer | ASG min capacity. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **recurrence**  string | Cron style schedule to repeat the action on.  Required when *state=present*. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **scheduled_action_name**  string / required | The name of the scheduled action. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **start_time**  string | Start time for the action. |
| **state**  string | Create / update or delete scheduled action.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **time_zone**  string | Time zone to run against. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](autoscaling_scheduled_action_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](autoscaling_scheduled_action_module.md#id5)

```yaml+jinja
# Create a scheduled action for a autoscaling group.
- name: Create a minimal scheduled action for autoscaling group
  community.aws.autoscaling_scheduled_action:
    region: eu-west-1
    autoscaling_group_name: test_asg
    scheduled_action_name: test_scheduled_action
    start_time: 2021 October 25 08:00 UTC
    recurrence: 40 22 * * 1-5
    desired_capacity: 10
    state: present
  register: scheduled_action

- name: Create a scheduled action for autoscaling group
  community.aws.autoscaling_scheduled_action:
    region: eu-west-1
    autoscaling_group_name: test_asg
    scheduled_action_name: test_scheduled_action
    start_time: 2021 October 25 08:00 UTC
    end_time: 2021 October 25 08:00 UTC
    time_zone: Europe/London
    recurrence: 40 22 * * 1-5
    min_size: 10
    max_size: 15
    desired_capacity: 10
    state: present
  register: scheduled_action

- name: Delete scheduled action
  community.aws.autoscaling_scheduled_action:
    region: eu-west-1
    autoscaling_group_name: test_asg
    scheduled_action_name: test_scheduled_action
    state: absent
```

## [Return Values](autoscaling_scheduled_action_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **desired_capacity**  integer | ASG desired capacity.  **Returned:** when *state=present*  **Sample:** `1` |
| **end_time**  string | End time for the action.  **Returned:** when *state=present*  **Sample:** `"2021 October 25 08:00 UTC"` |
| **max_size**  integer | ASG max capacity.  **Returned:** when *state=present*  **Sample:** `2` |
| **min_size**  integer | ASG min capacity.  **Returned:** when *state=present*  **Sample:** `1` |
| **recurrence**  string | Cron style schedule to repeat the action on.  **Returned:** when *state=present*  **Sample:** `"40 22 * * 1-5"` |
| **scheduled_action_name**  string | The name of the scheduled action.  **Returned:** when *state=present*  **Sample:** `"test_scheduled_action"` |
| **start_time**  string | Start time for the action.  **Returned:** when *state=present*  **Sample:** `"2021 October 25 08:00 UTC"` |
| **time_zone**  string | The ID of the Amazon Machine Image used by the launch configuration.  **Returned:** when *state=present*  **Sample:** `"Europe/London"` |

### Authors

- Mark Woolley(@marknet15)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
