---
collection: ansible
version: "8"
title: "community.aws.elb_target_group_info module – Gather information about ELB target groups in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/elb_target_group_info_module.html
fetched_at: 2026-07-28T01:41:15+00:00
---
# community.aws.elb_target_group_info module – Gather information about ELB target groups in AWS

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](elb_target_group_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **collect_targets_health**  boolean | When set to `True`, output contains targets health description  **Choices:**   - `false` ← (default) - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer. |
| **names**  list / elements=string | The names of the target groups. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **target_group_arns**  list / elements=string | The Amazon Resource Names (ARN) of the target groups. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](elb_target_group_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](elb_target_group_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather information about all target groups
  community.aws.elb_target_group_info:

- name: Gather information about the target group attached to a particular ELB
  community.aws.elb_target_group_info:
    load_balancer_arn: "arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:loadbalancer/app/my-elb/aabbccddeeff"

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
| **target_groups**  complex | a list of target groups  **Returned:** always |
| **deregistration_delay_timeout_seconds**  integer | The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused.  **Returned:** always  **Sample:** `300` |
| **health_check_interval_seconds**  integer | The approximate amount of time, in seconds, between health checks of an individual target.  **Returned:** always  **Sample:** `30` |
| **health_check_path**  string | The destination for the health check request.  **Returned:** always  **Sample:** `"/index.html"` |
| **health_check_port**  string | The port to use to connect with the target.  **Returned:** always  **Sample:** `"traffic-port"` |
| **health_check_protocol**  string | The protocol to use to connect with the target.  **Returned:** always  **Sample:** `"HTTP"` |
| **health_check_timeout_seconds**  integer | The amount of time, in seconds, during which no response means a failed health check.  **Returned:** always  **Sample:** `5` |
| **healthy_threshold_count**  integer | The number of consecutive health checks successes required before considering an unhealthy target healthy.  **Returned:** always  **Sample:** `5` |
| **load_balancer_arns**  list / elements=string | The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.  **Returned:** always  **Sample:** `[]` |
| **matcher**  dictionary | The HTTP codes to use when checking for a successful response from a target.  **Returned:** always  **Sample:** `{"http_code": "200"}` |
| **port**  integer | The port on which the targets are listening.  **Returned:** always  **Sample:** `80` |
| **protocol**  string | The protocol to use for routing traffic to the targets.  **Returned:** always  **Sample:** `"HTTP"` |
| **stickiness_enabled**  boolean | Indicates whether sticky sessions are enabled.  **Returned:** always  **Sample:** `true` |
| **stickiness_lb_cookie_duration_seconds**  integer | Indicates whether sticky sessions are enabled.  **Returned:** always  **Sample:** `86400` |
| **stickiness_type**  string | The type of sticky sessions.  **Returned:** always  **Sample:** `"lb_cookie"` |
| **tags**  dictionary | The tags attached to the target group.  **Returned:** always  **Sample:** `{"Tag": "Example"}` |
| **target_group_arn**  string | The Amazon Resource Name (ARN) of the target group.  **Returned:** always  **Sample:** `"arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:targetgroup/mytargetgroup/aabbccddee0044332211"` |
| **target_group_name**  string | The name of the target group.  **Returned:** always  **Sample:** `"mytargetgroup"` |
| **targets_health_description**  complex | Targets health description.  **Returned:** when collect_targets_health is enabled |
| **health_check_port**  string | The port to check target health.  **Returned:** always  **Sample:** `"80"` |
| **target**  complex | The target metadata.  **Returned:** always |
| **id**  string | The ID of the target.  **Returned:** always  **Sample:** `"i-0123456789"` |
| **port**  integer | The port to use to connect with the target.  **Returned:** always  **Sample:** `80` |
| **target_health**  complex | The target health status.  **Returned:** always |
| **state**  string | The state of the target health.  **Returned:** always  **Sample:** `"healthy"` |
| **unhealthy_threshold_count**  integer | The number of consecutive health check failures required before considering the target unhealthy.  **Returned:** always  **Sample:** `2` |
| **vpc_id**  string | The ID of the VPC for the targets.  **Returned:** always  **Sample:** `"vpc-0123456"` |

### Authors

- Rob White (@wimnat)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
