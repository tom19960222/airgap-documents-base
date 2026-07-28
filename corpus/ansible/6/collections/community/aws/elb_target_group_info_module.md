---
collection: ansible
version: "6"
title: "community.aws.elb_target_group_info module – Gather information about ELB target groups in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elb_target_group_info_module.html
fetched_at: 2026-07-27T17:04:32+00:00
---
# community.aws.elb_target_group_info module – Gather information about ELB target groups in AWS

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
> see [Requirements](elb_target_group_info_module.md#ansible-collections-community-aws-elb-target-group-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elb_target_group_info`.

New in community.aws 1.0.0

- [Synopsis](elb_target_group_info_module.md#synopsis)
- [Requirements](elb_target_group_info_module.md#requirements)
- [Parameters](elb_target_group_info_module.md#parameters)
- [Notes](elb_target_group_info_module.md#notes)
- [Examples](elb_target_group_info_module.md#examples)
- [Return Values](elb_target_group_info_module.md#return-values)

## [Synopsis](elb_target_group_info_module.md#id1)

- Gather information about ELB target groups in AWS

## [Requirements](elb_target_group_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elb_target_group_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **collect_targets_health**  boolean | When set to “yes”, output contains targets health description  Choices:   - `false` ← (default) - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer. |
| **names**  list / elements=string | The names of the target groups. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **target_group_arns**  list / elements=string | The Amazon Resource Names (ARN) of the target groups. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](elb_target_group_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elb_target_group_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather information about all target groups
  community.aws.elb_target_group_info:

- name: Gather information about the target group attached to a particular ELB
  community.aws.elb_target_group_info:
    load_balancer_arn: "arn:aws:elasticloadbalancing:ap-southeast-2:001122334455:loadbalancer/app/my-elb/aabbccddeeff"

- name: Gather information about a target groups named 'tg1' and 'tg2'
  community.aws.elb_target_group_info:
    names:
      - tg1
      - tg2
```

## [Return Values](elb_target_group_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **target_groups**  complex | a list of target groups  Returned: always |
| **deregistration_delay_timeout_seconds**  integer | The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused.  Returned: always  Sample: `300` |
| **health_check_interval_seconds**  integer | The approximate amount of time, in seconds, between health checks of an individual target.  Returned: always  Sample: `30` |
| **health_check_path**  string | The destination for the health check request.  Returned: always  Sample: `"/index.html"` |
| **health_check_port**  string | The port to use to connect with the target.  Returned: always  Sample: `"traffic-port"` |
| **health_check_protocol**  string | The protocol to use to connect with the target.  Returned: always  Sample: `"HTTP"` |
| **health_check_timeout_seconds**  integer | The amount of time, in seconds, during which no response means a failed health check.  Returned: always  Sample: `5` |
| **healthy_threshold_count**  integer | The number of consecutive health checks successes required before considering an unhealthy target healthy.  Returned: always  Sample: `5` |
| **load_balancer_arns**  list / elements=string | The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.  Returned: always  Sample: `[]` |
| **matcher**  dictionary | The HTTP codes to use when checking for a successful response from a target.  Returned: always  Sample: `{"http_code": "200"}` |
| **port**  integer | The port on which the targets are listening.  Returned: always  Sample: `80` |
| **protocol**  string | The protocol to use for routing traffic to the targets.  Returned: always  Sample: `"HTTP"` |
| **stickiness_enabled**  boolean | Indicates whether sticky sessions are enabled.  Returned: always  Sample: `true` |
| **stickiness_lb_cookie_duration_seconds**  integer | Indicates whether sticky sessions are enabled.  Returned: always  Sample: `86400` |
| **stickiness_type**  string | The type of sticky sessions.  Returned: always  Sample: `"lb_cookie"` |
| **tags**  dictionary | The tags attached to the target group.  Returned: always  Sample: `{"Tag": "Example"}` |
| **target_group_arn**  string | The Amazon Resource Name (ARN) of the target group.  Returned: always  Sample: `"arn:aws:elasticloadbalancing:ap-southeast-2:01234567890:targetgroup/mytargetgroup/aabbccddee0044332211"` |
| **target_group_name**  string | The name of the target group.  Returned: always  Sample: `"mytargetgroup"` |
| **targets_health_description**  complex | Targets health description.  Returned: when collect_targets_health is enabled |
| **health_check_port**  string | The port to check target health.  Returned: always  Sample: `"80"` |
| **target**  complex | The target metadata.  Returned: always |
| **id**  string | The ID of the target.  Returned: always  Sample: `"i-0123456789"` |
| **port**  integer | The port to use to connect with the target.  Returned: always  Sample: `80` |
| **target_health**  complex | The target health status.  Returned: always |
| **state**  string | The state of the target health.  Returned: always  Sample: `"healthy"` |
| **unhealthy_threshold_count**  integer | The number of consecutive health check failures required before considering the target unhealthy.  Returned: always  Sample: `2` |
| **vpc_id**  string | The ID of the VPC for the targets.  Returned: always  Sample: `"vpc-0123456"` |

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
