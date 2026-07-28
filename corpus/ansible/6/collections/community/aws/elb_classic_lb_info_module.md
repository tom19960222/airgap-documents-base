---
collection: ansible
version: "6"
title: "community.aws.elb_classic_lb_info module – Gather information about EC2 Elastic Load Balancers in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elb_classic_lb_info_module.html
fetched_at: 2026-07-27T17:04:28+00:00
---
# community.aws.elb_classic_lb_info module – Gather information about EC2 Elastic Load Balancers in AWS

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
> see [Requirements](elb_classic_lb_info_module.md#ansible-collections-community-aws-elb-classic-lb-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elb_classic_lb_info`.

New in community.aws 1.0.0

- [Synopsis](elb_classic_lb_info_module.md#synopsis)
- [Requirements](elb_classic_lb_info_module.md#requirements)
- [Parameters](elb_classic_lb_info_module.md#parameters)
- [Notes](elb_classic_lb_info_module.md#notes)
- [Examples](elb_classic_lb_info_module.md#examples)
- [Return Values](elb_classic_lb_info_module.md#return-values)

## [Synopsis](elb_classic_lb_info_module.md#id1)

- Gather information about EC2 Elastic Load Balancers in AWS

## [Requirements](elb_classic_lb_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elb_classic_lb_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **names**  list / elements=string | List of ELB names to gather information about. Pass this option to gather information about a set of ELBs, otherwise, all ELBs are returned. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](elb_classic_lb_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elb_classic_lb_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.
# Output format tries to match amazon.aws.ec2_elb_lb module input parameters

# Gather information about all ELBs
- community.aws.elb_classic_lb_info:
  register: elb_info

- ansible.builtin.debug:
    msg: "{{ item.dns_name }}"
  loop: "{{ elb_info.elbs }}"

# Gather information about a particular ELB
- community.aws.elb_classic_lb_info:
    names: frontend-prod-elb
  register: elb_info

- ansible.builtin.debug:
    msg: "{{ elb_info.elbs.0.dns_name }}"

# Gather information about a set of ELBs
- community.aws.elb_classic_lb_info:
    names:
    - frontend-prod-elb
    - backend-prod-elb
  register: elb_info

- ansible.builtin.debug:
    msg: "{{ item.dns_name }}"
  loop: "{{ elb_info.elbs }}"
```

## [Return Values](elb_classic_lb_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **elbs**  list / elements=string | a list of load balancers  Returned: always  Sample: `{"elbs": [{"attributes": {"access_log": {"enabled": false}, "connection_draining": {"enabled": true, "timeout": 300}, "connection_settings": {"idle_timeout": 60}, "cross_zone_load_balancing": {"enabled": true}}, "availability_zones": ["us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e"], "backend_server_description": [], "canonical_hosted_zone_name": "test-lb-XXXXXXXXXXXX.us-east-1.elb.amazonaws.com", "canonical_hosted_zone_name_id": "XXXXXXXXXXXXXX", "created_time": "2017-08-23T18:25:03.280000+00:00", "dns_name": "test-lb-XXXXXXXXXXXX.us-east-1.elb.amazonaws.com", "health_check": {"healthy_threshold": 10, "interval": 30, "target": "HTTP:80/index.html", "timeout": 5, "unhealthy_threshold": 2}, "instances": [], "instances_inservice": [], "instances_inservice_count": 0, "instances_outofservice": [], "instances_outofservice_count": 0, "instances_unknownservice": [], "instances_unknownservice_count": 0, "listener_descriptions": [{"listener": {"instance_port": 80, "instance_protocol": "HTTP", "load_balancer_port": 80, "protocol": "HTTP"}, "policy_names": []}], "load_balancer_name": "test-lb", "policies": {"app_cookie_stickiness_policies": [], "lb_cookie_stickiness_policies": [], "other_policies": []}, "scheme": "internet-facing", "security_groups": ["sg-29d13055"], "source_security_group": {"group_name": "default", "owner_alias": "XXXXXXXXXXXX"}, "subnets": ["subnet-XXXXXXXX", "subnet-XXXXXXXX"], "tags": {}, "vpc_id": "vpc-c248fda4"}]}` |

### Authors

- Michael Schultz (@mjschultz)
- Fernando Jose Pando (@nand0p)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
