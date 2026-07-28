---
collection: ansible
version: "6"
title: "community.aws.ec2_asg_scheduled_action module – Create, modify and delete ASG scheduled scaling actions."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_asg_scheduled_action_module.html
fetched_at: 2026-07-27T17:03:56+00:00
---
# community.aws.ec2_asg_scheduled_action module – Create, modify and delete ASG scheduled scaling actions.

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
> see [Requirements](ec2_asg_scheduled_action_module.md#ansible-collections-community-aws-ec2-asg-scheduled-action-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_asg_scheduled_action`.

New in community.aws 2.2.0

- [Synopsis](ec2_asg_scheduled_action_module.md#synopsis)
- [Requirements](ec2_asg_scheduled_action_module.md#requirements)
- [Parameters](ec2_asg_scheduled_action_module.md#parameters)
- [Notes](ec2_asg_scheduled_action_module.md#notes)
- [Examples](ec2_asg_scheduled_action_module.md#examples)
- [Return Values](ec2_asg_scheduled_action_module.md#return-values)

## [Synopsis](ec2_asg_scheduled_action_module.md#id1)

- The module will create a new scheduled action when *state=present* and no given action is found.
- The module will update a new scheduled action when *state=present* and the given action is found.
- The module will delete a new scheduled action when *state=absent* and the given action is found.

## [Requirements](ec2_asg_scheduled_action_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_asg_scheduled_action_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autoscaling_group_name**  string / required | The name of the autoscaling group to add a scheduled action to. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **desired_capacity**  integer | ASG desired capacity. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **end_time**  string | End time for the action. |
| **max_size**  integer | ASG max capacity. |
| **min_size**  integer | ASG min capacity. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **recurrence**  string | Cron style schedule to repeat the action on.  Required when *state=present*. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **scheduled_action_name**  string / required | The name of the scheduled action. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **start_time**  string | Start time for the action. |
| **state**  string | Create / update or delete scheduled action.  Choices:   - `"present"` ← (default) - `"absent"` |
| **time_zone**  string | Time zone to run against. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_asg_scheduled_action_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_asg_scheduled_action_module.md#id5)

```yaml+jinja
# Create a scheduled action for a autoscaling group.
- name: Create a minimal scheduled action for autoscaling group
  community.aws.ec2_asg_scheduled_action:
    region: eu-west-1
    autoscaling_group_name: test_asg
    scheduled_action_name: test_scheduled_action
    start_time: 2021 October 25 08:00 UTC
    recurrence: 40 22 * * 1-5
    desired_capacity: 10
    state: present
  register: scheduled_action

- name: Create a scheduled action for autoscaling group
  community.aws.ec2_asg_scheduled_action:
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
  community.aws.ec2_asg_scheduled_action:
    region: eu-west-1
    autoscaling_group_name: test_asg
    scheduled_action_name: test_scheduled_action
    state: absent
```

## [Return Values](ec2_asg_scheduled_action_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **desired_capacity**  integer | ASG desired capacity.  Returned: when *state=present*  Sample: `1` |
| **end_time**  string | End time for the action.  Returned: when *state=present*  Sample: `"2021 October 25 08:00 UTC"` |
| **max_size**  integer | ASG max capacity.  Returned: when *state=present*  Sample: `2` |
| **min_size**  integer | ASG min capacity.  Returned: when *state=present*  Sample: `1` |
| **recurrence**  string | Cron style schedule to repeat the action on.  Returned: when *state=present*  Sample: `"40 22 * * 1-5"` |
| **scheduled_action_name**  string | The name of the scheduled action.  Returned: when *state=present*  Sample: `"test_scheduled_action"` |
| **start_time**  string | Start time for the action.  Returned: when *state=present*  Sample: `"2021 October 25 08:00 UTC"` |
| **time_zone**  string | The ID of the Amazon Machine Image used by the launch configuration.  Returned: when *state=present*  Sample: `"Europe/London"` |

### Authors

- Mark Woolley(@marknet15)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
