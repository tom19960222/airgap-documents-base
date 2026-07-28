---
collection: ansible
version: "8"
title: "amazon.aws.autoscaling_group_info module – Gather information about EC2 Auto Scaling Groups (ASGs) in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/autoscaling_group_info_module.html
fetched_at: 2026-07-28T01:06:05+00:00
---
# amazon.aws.autoscaling_group_info module – Gather information about EC2 Auto Scaling Groups (ASGs) in AWS

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](autoscaling_group_info_module.md#ansible-collections-amazon-aws-autoscaling-group-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.autoscaling_group_info`.

New in amazon.aws 5.0.0

- [Synopsis](autoscaling_group_info_module.md#synopsis)
- [Requirements](autoscaling_group_info_module.md#requirements)
- [Parameters](autoscaling_group_info_module.md#parameters)
- [Notes](autoscaling_group_info_module.md#notes)
- [Examples](autoscaling_group_info_module.md#examples)
- [Return Values](autoscaling_group_info_module.md#return-values)

## [Synopsis](autoscaling_group_info_module.md#id1)

- Gather information about EC2 Auto Scaling Groups (ASGs) in AWS.
- Prior to release 5.0.0 this module was called `community.aws.ec2_asg_info`. The usage did not change.
- This module was originally added to `community.aws` in release 1.0.0.

Aliases: ec2_asg_info

## [Requirements](autoscaling_group_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](autoscaling_group_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string | The prefix or name of the auto scaling group(s) you are searching for.  Note: This is a regular expression match with implicit ‘^’ (beginning of string). Append ‘$’ for a complete name match. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **tags**  dictionary | A dictionary/hash of tags in the format { tag1_name: ‘tag1_value’, tag2_name: ‘tag2_value’ } to match against the auto scaling group(s) you are searching for. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](autoscaling_group_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](autoscaling_group_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Find all groups
  amazon.aws.autoscaling_group_info:
  register: asgs

- name: Find a group with matching name/prefix
  amazon.aws.autoscaling_group_info:
    name: public-webserver-asg
  register: asgs

- name: Find a group with matching tags
  amazon.aws.autoscaling_group_info:
    tags:
      project: webapp
      env: production
  register: asgs

- name: Find a group with matching name/prefix and tags
  amazon.aws.autoscaling_group_info:
    name: myproject
    tags:
      env: production
  register: asgs

- name: Fail if no groups are found
  amazon.aws.autoscaling_group_info:
    name: public-webserver-asg
  register: asgs
  failed_when: "{{ asgs.results | length == 0 }}"

- name: Fail if more than 1 group is found
  amazon.aws.autoscaling_group_info:
    name: public-webserver-asg
  register: asgs
  failed_when: "{{ asgs.results | length > 1 }}"
```

## [Return Values](autoscaling_group_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **auto_scaling_group_arn**  string | The Amazon Resource Name of the ASG  **Returned:** success  **Sample:** `"arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:10787c52-0bcb-427d-82ba-c8e4b008ed2e:autoScalingGroupName/public-webapp-production-1"` |
| **auto_scaling_group_name**  string | Name of autoscaling group  **Returned:** success  **Sample:** `"public-webapp-production-1"` |
| **availability_zones**  list / elements=string | List of Availability Zones that are enabled for this ASG.  **Returned:** success  **Sample:** `["us-west-2a", "us-west-2b", "us-west-2a"]` |
| **created_time**  string | The date and time this ASG was created, in ISO 8601 format.  **Returned:** success  **Sample:** `"2015-11-25T00:05:36.309Z"` |
| **default_cooldown**  integer | The default cooldown time in seconds.  **Returned:** success  **Sample:** `300` |
| **desired_capacity**  integer | The number of EC2 instances that should be running in this group.  **Returned:** success  **Sample:** `3` |
| **health_check_period**  integer | Length of time in seconds after a new EC2 instance comes into service that Auto Scaling starts checking its health.  **Returned:** success  **Sample:** `30` |
| **health_check_type**  string | The service you want the health status from, one of “EC2” or “ELB”.  **Returned:** success  **Sample:** `"ELB"` |
| **instances**  list / elements=string | List of EC2 instances and their status as it relates to the ASG.  **Returned:** success  **Sample:** `[{"availability_zone": "us-west-2a", "health_status": "Healthy", "instance_id": "i-es22ad25", "launch_configuration_name": "public-webapp-production-1", "lifecycle_state": "InService", "protected_from_scale_in": "false"}]` |
| **launch_config_name**  string | Name of launch configuration associated with the ASG. Same as launch_configuration_name, provided for compatibility with [amazon.aws.autoscaling_group](autoscaling_group_module.md#ansible-collections-amazon-aws-autoscaling-group-module) module.  **Returned:** success  **Sample:** `"public-webapp-production-1"` |
| **launch_configuration_name**  string | Name of launch configuration associated with the ASG.  **Returned:** success  **Sample:** `"public-webapp-production-1"` |
| **lifecycle_hooks**  list / elements=string | List of lifecycle hooks for the ASG.  **Returned:** success  **Sample:** `[{"AutoScalingGroupName": "public-webapp-production-1", "DefaultResult": "ABANDON", "GlobalTimeout": 172800, "HeartbeatTimeout": 3600, "LifecycleHookName": "instance-launch", "LifecycleTransition": "autoscaling:EC2_INSTANCE_LAUNCHING"}, {"AutoScalingGroupName": "public-webapp-production-1", "DefaultResult": "ABANDON", "GlobalTimeout": 172800, "HeartbeatTimeout": 3600, "LifecycleHookName": "instance-terminate", "LifecycleTransition": "autoscaling:EC2_INSTANCE_TERMINATING"}]` |
| **load_balancer_names**  list / elements=string | List of load balancers names attached to the ASG.  **Returned:** success  **Sample:** `["elb-webapp-prod"]` |
| **max_size**  integer | Maximum size of group  **Returned:** success  **Sample:** `3` |
| **min_size**  integer | Minimum size of group  **Returned:** success  **Sample:** `1` |
| **new_instances_protected_from_scale_in**  boolean | Whether or not new instances a protected from automatic scaling in.  **Returned:** success  **Sample:** `false` |
| **placement_group**  string | Placement group into which instances are launched, if any.  **Returned:** success  **Sample:** `"None"` |
| **status**  string | The current state of the group when DeleteAutoScalingGroup is in progress.  **Returned:** success  **Sample:** `"None"` |
| **tags**  list / elements=string | List of tags for the ASG, and whether or not each tag propagates to instances at launch.  **Returned:** success  **Sample:** `[{"key": "Name", "propagate_at_launch": "true", "resource_id": "public-webapp-production-1", "resource_type": "auto-scaling-group", "value": "public-webapp-production-1"}, {"key": "env", "propagate_at_launch": "true", "resource_id": "public-webapp-production-1", "resource_type": "auto-scaling-group", "value": "production"}]` |
| **target_group_arns**  list / elements=string | List of ARNs of the target groups that the ASG populates  **Returned:** success  **Sample:** `["arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:targetgroup/target-group-host-hello/1a2b3c4d5e6f1a2b", "arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:targetgroup/target-group-path-world/abcd1234abcd1234"]` |
| **target_group_names**  list / elements=string | List of names of the target groups that the ASG populates  **Returned:** success  **Sample:** `["target-group-host-hello", "target-group-path-world"]` |
| **termination_policies**  string | A list of termination policies for the group.  **Returned:** success  **Sample:** `"['Default']"` |

### Authors

- Rob White (@wimnat)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
