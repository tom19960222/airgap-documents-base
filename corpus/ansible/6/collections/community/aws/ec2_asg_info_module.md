---
collection: ansible
version: "6"
title: "community.aws.ec2_asg_info module – Gather information about ec2 Auto Scaling Groups (ASGs) in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_asg_info_module.html
fetched_at: 2026-07-27T17:03:53+00:00
---
# community.aws.ec2_asg_info module – Gather information about ec2 Auto Scaling Groups (ASGs) in AWS

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
> see [Requirements](ec2_asg_info_module.md#ansible-collections-community-aws-ec2-asg-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_asg_info`.

New in community.aws 1.0.0

- [Synopsis](ec2_asg_info_module.md#synopsis)
- [Requirements](ec2_asg_info_module.md#requirements)
- [Parameters](ec2_asg_info_module.md#parameters)
- [Notes](ec2_asg_info_module.md#notes)
- [Examples](ec2_asg_info_module.md#examples)
- [Return Values](ec2_asg_info_module.md#return-values)

## [Synopsis](ec2_asg_info_module.md#id1)

- Gather information about ec2 Auto Scaling Groups (ASGs) in AWS

## [Requirements](ec2_asg_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_asg_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string | The prefix or name of the auto scaling group(s) you are searching for.  Note: This is a regular expression match with implicit ‘^’ (beginning of string). Append ‘$’ for a complete name match. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **tags**  dictionary | A dictionary/hash of tags in the format { tag1_name: ‘tag1_value’, tag2_name: ‘tag2_value’ } to match against the auto scaling group(s) you are searching for. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_asg_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_asg_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Find all groups
  community.aws.ec2_asg_info:
  register: asgs

- name: Find a group with matching name/prefix
  community.aws.ec2_asg_info:
    name: public-webserver-asg
  register: asgs

- name: Find a group with matching tags
  community.aws.ec2_asg_info:
    tags:
      project: webapp
      env: production
  register: asgs

- name: Find a group with matching name/prefix and tags
  community.aws.ec2_asg_info:
    name: myproject
    tags:
      env: production
  register: asgs

- name: Fail if no groups are found
  community.aws.ec2_asg_info:
    name: public-webserver-asg
  register: asgs
  failed_when: "{{ asgs.results | length == 0 }}"

- name: Fail if more than 1 group is found
  community.aws.ec2_asg_info:
    name: public-webserver-asg
  register: asgs
  failed_when: "{{ asgs.results | length > 1 }}"
```

## [Return Values](ec2_asg_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auto_scaling_group_arn**  string | The Amazon Resource Name of the ASG  Returned: success  Sample: `"arn:aws:autoscaling:us-west-2:1234567890:autoScalingGroup:10787c52-0bcb-427d-82ba-c8e4b008ed2e:autoScalingGroupName/public-webapp-production-1"` |
| **auto_scaling_group_name**  string | Name of autoscaling group  Returned: success  Sample: `"public-webapp-production-1"` |
| **availability_zones**  list / elements=string | List of Availability Zones that are enabled for this ASG.  Returned: success  Sample: `["us-west-2a", "us-west-2b", "us-west-2a"]` |
| **created_time**  string | The date and time this ASG was created, in ISO 8601 format.  Returned: success  Sample: `"2015-11-25T00:05:36.309Z"` |
| **default_cooldown**  integer | The default cooldown time in seconds.  Returned: success  Sample: `300` |
| **desired_capacity**  integer | The number of EC2 instances that should be running in this group.  Returned: success  Sample: `3` |
| **health_check_period**  integer | Length of time in seconds after a new EC2 instance comes into service that Auto Scaling starts checking its health.  Returned: success  Sample: `30` |
| **health_check_type**  string | The service you want the health status from, one of “EC2” or “ELB”.  Returned: success  Sample: `"ELB"` |
| **instances**  list / elements=string | List of EC2 instances and their status as it relates to the ASG.  Returned: success  Sample: `[{"availability_zone": "us-west-2a", "health_status": "Healthy", "instance_id": "i-es22ad25", "launch_configuration_name": "public-webapp-production-1", "lifecycle_state": "InService", "protected_from_scale_in": "false"}]` |
| **launch_config_name**  string | Name of launch configuration associated with the ASG. Same as launch_configuration_name, provided for compatibility with ec2_asg module.  Returned: success  Sample: `"public-webapp-production-1"` |
| **launch_configuration_name**  string | Name of launch configuration associated with the ASG.  Returned: success  Sample: `"public-webapp-production-1"` |
| **lifecycle_hooks**  list / elements=string | List of lifecycle hooks for the ASG.  Returned: success  Sample: `[{"AutoScalingGroupName": "public-webapp-production-1", "DefaultResult": "ABANDON", "GlobalTimeout": 172800, "HeartbeatTimeout": 3600, "LifecycleHookName": "instance-launch", "LifecycleTransition": "autoscaling:EC2_INSTANCE_LAUNCHING"}, {"AutoScalingGroupName": "public-webapp-production-1", "DefaultResult": "ABANDON", "GlobalTimeout": 172800, "HeartbeatTimeout": 3600, "LifecycleHookName": "instance-terminate", "LifecycleTransition": "autoscaling:EC2_INSTANCE_TERMINATING"}]` |
| **load_balancer_names**  list / elements=string | List of load balancers names attached to the ASG.  Returned: success  Sample: `["elb-webapp-prod"]` |
| **max_size**  integer | Maximum size of group  Returned: success  Sample: `3` |
| **min_size**  integer | Minimum size of group  Returned: success  Sample: `1` |
| **new_instances_protected_from_scale_in**  boolean | Whether or not new instances a protected from automatic scaling in.  Returned: success  Sample: `false` |
| **placement_group**  string | Placement group into which instances are launched, if any.  Returned: success  Sample: `"None"` |
| **status**  string | The current state of the group when DeleteAutoScalingGroup is in progress.  Returned: success  Sample: `"None"` |
| **tags**  list / elements=string | List of tags for the ASG, and whether or not each tag propagates to instances at launch.  Returned: success  Sample: `[{"key": "Name", "propagate_at_launch": "true", "resource_id": "public-webapp-production-1", "resource_type": "auto-scaling-group", "value": "public-webapp-production-1"}, {"key": "env", "propagate_at_launch": "true", "resource_id": "public-webapp-production-1", "resource_type": "auto-scaling-group", "value": "production"}]` |
| **target_group_arns**  list / elements=string | List of ARNs of the target groups that the ASG populates  Returned: success  Sample: `["arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:targetgroup/target-group-host-hello/1a2b3c4d5e6f1a2b", "arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:targetgroup/target-group-path-world/abcd1234abcd1234"]` |
| **target_group_names**  list / elements=string | List of names of the target groups that the ASG populates  Returned: success  Sample: `["target-group-host-hello", "target-group-path-world"]` |
| **termination_policies**  string | A list of termination policies for the group.  Returned: success  Sample: `"['Default']"` |

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
