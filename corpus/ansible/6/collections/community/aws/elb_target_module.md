---
collection: ansible
version: "6"
title: "community.aws.elb_target module – Manage a target in a target group"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elb_target_module.html
fetched_at: 2026-07-27T17:04:30+00:00
---
# community.aws.elb_target module – Manage a target in a target group

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
> see [Requirements](elb_target_module.md#ansible-collections-community-aws-elb-target-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elb_target`.

New in community.aws 1.0.0

- [Synopsis](elb_target_module.md#synopsis)
- [Requirements](elb_target_module.md#requirements)
- [Parameters](elb_target_module.md#parameters)
- [Notes](elb_target_module.md#notes)
- [Examples](elb_target_module.md#examples)

## [Synopsis](elb_target_module.md#id1)

- Used to register or deregister a target in a target group.

## [Requirements](elb_target_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elb_target_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **deregister_unused**  boolean | The default behaviour for targets that are unused is to leave them registered.  If instead you would like to remove them set *deregister_unused=true*.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Register or deregister the target.  Choices:   - `"present"` - `"absent"` |
| **target_az**  string | An Availability Zone or `all`. This determines whether the target receives traffic from the load balancer nodes in the specified Availability Zone or from all enabled Availability Zones for the load balancer. This parameter is not supported if the target type of the target group is instance. |
| **target_group_arn**  string | The Amazon Resource Name (ARN) of the target group.  Mutually exclusive of *target_group_name*. |
| **target_group_name**  string | The name of the target group.  Mutually exclusive of *target_group_arn*. |
| **target_id**  string / required | The ID of the target. |
| **target_port**  integer | The port on which the target is listening. You can specify a port override. If a target is already registered, you can register it again using a different port.  The default port for a target is the port for the target group. |
| **target_status**  string | Blocks and waits for the target status to equal given value. For more detail on target status see <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html#target-health-states>  Choices:   - `"initial"` - `"healthy"` - `"unhealthy"` - `"unused"` - `"draining"` - `"unavailable"` |
| **target_status_timeout**  integer | Maximum time in seconds to wait for *target_status* change.  Default: `60` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](elb_target_module.md#id4)

> **Note:**
>
> - If you specified a port override when you registered a target, you must specify both the target ID and the port when you deregister it.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elb_target_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Register an IP address target to a target group
  community.aws.elb_target:
    target_group_name: myiptargetgroup
    target_id: i-1234567
    state: present

- name: Register an instance target to a target group
  community.aws.elb_target:
    target_group_name: mytargetgroup
    target_id: i-1234567
    state: present

- name: Deregister a target from a target group
  community.aws.elb_target:
    target_group_name: mytargetgroup
    target_id: i-1234567
    state: absent

# Modify a target to use a different port
- name: Register a target to a target group
  community.aws.elb_target:
    target_group_name: mytargetgroup
    target_id: i-1234567
    target_port: 8080
    state: present
```

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
