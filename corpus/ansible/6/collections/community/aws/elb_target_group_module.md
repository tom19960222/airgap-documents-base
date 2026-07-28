---
collection: ansible
version: "6"
title: "community.aws.elb_target_group module – Manage a target group for an Application or Network load balancer"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elb_target_group_module.html
fetched_at: 2026-07-27T17:04:31+00:00
---
# community.aws.elb_target_group module – Manage a target group for an Application or Network load balancer

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
> see [Requirements](elb_target_group_module.md#ansible-collections-community-aws-elb-target-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elb_target_group`.

New in community.aws 1.0.0

- [Synopsis](elb_target_group_module.md#synopsis)
- [Requirements](elb_target_group_module.md#requirements)
- [Parameters](elb_target_group_module.md#parameters)
- [Notes](elb_target_group_module.md#notes)
- [Examples](elb_target_group_module.md#examples)
- [Return Values](elb_target_group_module.md#return-values)

## [Synopsis](elb_target_group_module.md#id1)

- Manage an AWS Elastic Load Balancer target group. See <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html> or <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html> for details.

## [Requirements](elb_target_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elb_target_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **deregistration_connection_termination**  boolean  added in community.aws 3.1.0 | Indicates whether the load balancer terminates connections at the end of the deregistration timeout.  Using this option is only supported when attaching to a Network Load Balancer (NLB).  Choices:   - `false` ← (default) - `true` |
| **deregistration_delay_timeout**  integer | The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused. The range is 0-3600 seconds. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **health_check_interval**  integer | The approximate amount of time, in seconds, between health checks of an individual target. |
| **health_check_path**  string | The ping path that is the destination on the targets for health checks. The path must be defined in order to set a health check.  Requires the *health_check_protocol* parameter to be set. |
| **health_check_port**  string | The port the load balancer uses when performing health checks on targets. Can be set to ‘traffic-port’ to match target port.  When not defined will default to the port on which each target receives traffic from the load balancer. |
| **health_check_protocol**  string | The protocol the load balancer uses when performing health checks on targets.  Choices:   - `"http"` - `"https"` - `"tcp"` - `"tls"` - `"udp"` - `"tcp_udp"` - `"HTTP"` - `"HTTPS"` - `"TCP"` - `"TLS"` - `"UDP"` - `"TCP_UDP"` |
| **health_check_timeout**  integer | The amount of time, in seconds, during which no response from a target means a failed health check. |
| **healthy_threshold_count**  integer | The number of consecutive health checks successes required before considering an unhealthy target healthy. |
| **load_balancing_algorithm_type**  string  added in community.aws 3.2.0 | The type of load balancing algorithm to use.  Changing the load balancing algorithm is only supported when used with Application Load Balancers (ALB).  If not set AWS will default to `round_robin`.  Choices:   - `"round_robin"` - `"least_outstanding_requests"` |
| **modify_targets**  boolean | Whether or not to alter existing targets in the group to match what is passed with the module  Choices:   - `false` - `true` ← (default) |
| **name**  string / required | The name of the target group. |
| **port**  integer | The port on which the targets receive traffic. This port is used unless you specify a port override when registering the target.  Required when *state* is `present` and *target_type* is `instance`, `ip`, or `alb`. |
| **preserve_client_ip_enabled**  boolean  added in community.aws 2.1.0 | Indicates whether client IP preservation is enabled.  The default is disabled if the target group type is `ip` address and the target group protocol is `tcp` or `tls`. Otherwise, the default is enabled. Client IP preservation cannot be disabled for `udp` and `tcp_udp` target groups.  *preserve_client_ip_enabled* is supported only by Network Load Balancers.  Choices:   - `false` - `true` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **protocol**  string | The protocol to use for routing traffic to the targets.  Required when *state* is `present` and *target_type* is `instance`, `ip`, or `alb`.  Choices:   - `"http"` - `"https"` - `"tcp"` - `"tls"` - `"udp"` - `"tcp_udp"` - `"HTTP"` - `"HTTPS"` - `"TCP"` - `"TLS"` - `"UDP"` - `"TCP_UDP"` |
| **proxy_protocol_v2_enabled**  boolean  added in community.aws 2.1.0 | Indicates whether Proxy Protocol version 2 is enabled.  The value is `true` or `false`.  *proxy_protocol_v2_enabled* is supported only by Network Load Balancers.  Choices:   - `false` - `true` |
| **purge_tags**  boolean | If yes, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter. If the tag parameter is not set then tags will not be modified.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Create or destroy the target group.  Choices:   - `"present"` - `"absent"` |
| **stickiness_app_cookie_duration**  integer  added in community.aws 1.5.0 | The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the application-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). |
| **stickiness_app_cookie_name**  string  added in community.aws 1.5.0 | The name of the application cookie. Required if *stickiness_type=app_cookie*. |
| **stickiness_enabled**  boolean | Indicates whether sticky sessions are enabled.  Choices:   - `false` - `true` |
| **stickiness_lb_cookie_duration**  integer | The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). |
| **stickiness_type**  string | The type of sticky sessions.  Valid values are `lb_cookie`, `app_cookie` or `source_ip`.  If not set AWS will default to `lb_cookie` for Application Load Balancers or `source_ip` for Network Load Balancers. |
| **successful_response_codes**  string | The HTTP codes to use when checking for a successful response from a target.  Accepts multiple values (for example, “200,202”) or a range of values (for example, “200-299”).  Requires the *health_check_protocol* parameter to be set. |
| **tags**  dictionary | A dictionary of one or more tags to assign to the target group. |
| **target_type**  string | The type of target that you must specify when registering targets with this target group. The possible values are `instance` (targets are specified by instance ID), `ip` (targets are specified by IP address), `lambda` (target is specified by ARN), or `alb` (target is specified by ARN). Note that you can’t specify targets for a target group using more than one type. Target types lambda and alb only accept one target. When more than one target is specified, only the first one is used. All additional targets are ignored. If the target type is ip, specify IP addresses from the subnets of the virtual private cloud (VPC) for the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can’t specify publicly routable IP addresses.  The default behavior is `instance`.  Choices:   - `"instance"` - `"ip"` - `"lambda"` - `"alb"` |
| **targets**  list / elements=dictionary | A list of targets to assign to the target group. This parameter defaults to an empty list. Unless you set the ‘modify_targets’ parameter then all existing targets will be removed from the group. The list should be an Id and a Port parameter. See the Examples for detail. |
| **unhealthy_threshold_count**  integer | The number of consecutive health check failures required before considering a target unhealthy. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_id**  string | The identifier of the virtual private cloud (VPC).  Required when *state* is `present` and *target_type* is `instance`, `ip`, or `alb`. |
| **wait**  boolean | Whether or not to wait for the target group.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | The time to wait for the target group.  Default: `200` |

## [Notes](elb_target_group_module.md#id4)

> **Note:**
>
> - Once a target group has been created, only its health check can then be modified using subsequent calls
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elb_target_group_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create a target group with a default health check
  community.aws.elb_target_group:
    name: mytargetgroup
    protocol: http
    port: 80
    vpc_id: vpc-01234567
    state: present

- name: Modify the target group with a custom health check
  community.aws.elb_target_group:
    name: mytargetgroup
    protocol: http
    port: 80
    vpc_id: vpc-01234567
    health_check_protocol: http
    health_check_path: /health_check
    health_check_port: 80
    successful_response_codes: 200
    health_check_interval: 15
    health_check_timeout: 3
    healthy_threshold_count: 4
    unhealthy_threshold_count: 3
    state: present

- name: Delete a target group
  community.aws.elb_target_group:
    name: mytargetgroup
    state: absent

- name: Create a target group with instance targets
  community.aws.elb_target_group:
    name: mytargetgroup
    protocol: http
    port: 81
    vpc_id: vpc-01234567
    health_check_protocol: http
    health_check_path: /
    successful_response_codes: "200,250-260"
    targets:
      - Id: i-01234567
        Port: 80
      - Id: i-98765432
        Port: 80
    state: present
    wait_timeout: 200
    wait: True

- name: Create a target group with IP address targets
  community.aws.elb_target_group:
    name: mytargetgroup
    protocol: http
    port: 81
    vpc_id: vpc-01234567
    health_check_protocol: http
    health_check_path: /
    successful_response_codes: "200,250-260"
    target_type: ip
    targets:
      - Id: 10.0.0.10
        Port: 80
        AvailabilityZone: all
      - Id: 10.0.0.20
        Port: 80
    state: present
    wait_timeout: 200
    wait: True

# Using lambda as targets require that the target group
# itself is allow to invoke the lambda function.
# therefore you need first to create an empty target group
# to receive its arn, second, allow the target group
# to invoke the lambda function and third, add the target
# to the target group
- name: first, create empty target group
  community.aws.elb_target_group:
    name: my-lambda-targetgroup
    target_type: lambda
    state: present
    modify_targets: False
  register: out

- name: second, allow invoke of the lambda
  community.aws.lambda_policy:
    state: "{{ state | default('present') }}"
    function_name: my-lambda-function
    statement_id: someID
    action: lambda:InvokeFunction
    principal: elasticloadbalancing.amazonaws.com
    source_arn: "{{ out.target_group_arn }}"

- name: third, add target
  community.aws.elb_target_group:
    name: my-lambda-targetgroup
    target_type: lambda
    state: present
    targets:
        - Id: arn:aws:lambda:eu-central-1:123456789012:function:my-lambda-function
```

## [Return Values](elb_target_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **deregistration_connection_termination**  boolean | Indicates whether the load balancer terminates connections at the end of the deregistration timeout.  Returned: when state present  Sample: `true` |
| **deregistration_delay_timeout_seconds**  integer | The amount time for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused.  Returned: when state present  Sample: `300` |
| **health_check_interval_seconds**  integer | The approximate amount of time, in seconds, between health checks of an individual target.  Returned: when state present  Sample: `30` |
| **health_check_path**  string | The destination for the health check request.  Returned: when state present  Sample: `"/index.html"` |
| **health_check_port**  string | The port to use to connect with the target.  Returned: when state present  Sample: `"traffic-port"` |
| **health_check_protocol**  string | The protocol to use to connect with the target.  Returned: when state present  Sample: `"HTTP"` |
| **health_check_timeout_seconds**  integer | The amount of time, in seconds, during which no response means a failed health check.  Returned: when state present  Sample: `5` |
| **healthy_threshold_count**  integer | The number of consecutive health checks successes required before considering an unhealthy target healthy.  Returned: when state present  Sample: `5` |
| **load_balancer_arns**  list / elements=string | The Amazon Resource Names (ARN) of the load balancers that route traffic to this target group.  Returned: when state present  Sample: `[]` |
| **load_balancing_algorithm_type**  string  added in community.aws 3.2.0 | The type load balancing algorithm used.  Returned: when state present  Sample: `"least_outstanding_requests"` |
| **matcher**  dictionary | The HTTP codes to use when checking for a successful response from a target.  Returned: when state present  Sample: `{"http_code": "200"}` |
| **port**  integer | The port on which the targets are listening.  Returned: when state present  Sample: `80` |
| **protocol**  string | The protocol to use for routing traffic to the targets.  Returned: when state present  Sample: `"HTTP"` |
| **stickiness_enabled**  boolean | Indicates whether sticky sessions are enabled.  Returned: when state present  Sample: `true` |
| **stickiness_lb_cookie_duration_seconds**  integer | The time period, in seconds, during which requests from a client should be routed to the same target.  Returned: when state present  Sample: `86400` |
| **stickiness_type**  string | The type of sticky sessions.  Returned: when state present  Sample: `"lb_cookie"` |
| **tags**  dictionary | The tags attached to the target group.  Returned: when state present  Sample: `{"Tag": "Example"}` |
| **target_group_arn**  string | The Amazon Resource Name (ARN) of the target group.  Returned: when state present  Sample: `"arn:aws:elasticloadbalancing:ap-southeast-2:01234567890:targetgroup/mytargetgroup/aabbccddee0044332211"` |
| **target_group_name**  string | The name of the target group.  Returned: when state present  Sample: `"mytargetgroup"` |
| **unhealthy_threshold_count**  integer | The number of consecutive health check failures required before considering the target unhealthy.  Returned: when state present  Sample: `2` |
| **vpc_id**  string | The ID of the VPC for the targets.  Returned: when state present  Sample: `"vpc-0123456"` |

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
