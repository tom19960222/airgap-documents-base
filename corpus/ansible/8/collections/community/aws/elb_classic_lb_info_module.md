---
collection: ansible
version: "8"
title: "community.aws.elb_classic_lb_info module – Gather information about EC2 Elastic Load Balancers in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/elb_classic_lb_info_module.html
fetched_at: 2026-07-28T01:41:11+00:00
---
# community.aws.elb_classic_lb_info module – Gather information about EC2 Elastic Load Balancers in AWS

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](elb_classic_lb_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **names**  list / elements=string | List of ELB names to gather information about. Pass this option to gather information about a set of ELBs, otherwise, all ELBs are returned.  **Default:** `[]` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](elb_classic_lb_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
| **elbs**  list / elements=string | a list of load balancers  **Returned:** always  **Sample:** `{"elbs": [{"attributes": {"access_log": {"enabled": false}, "connection_draining": {"enabled": true, "timeout": 300}, "connection_settings": {"idle_timeout": 60}, "cross_zone_load_balancing": {"enabled": true}}, "availability_zones": ["us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e"], "backend_server_description": [], "canonical_hosted_zone_name": "test-lb-XXXXXXXXXXXX.us-east-1.elb.amazonaws.com", "canonical_hosted_zone_name_id": "XXXXXXXXXXXXXX", "created_time": "2017-08-23T18:25:03.280000+00:00", "dns_name": "test-lb-XXXXXXXXXXXX.us-east-1.elb.amazonaws.com", "health_check": {"healthy_threshold": 10, "interval": 30, "target": "HTTP:80/index.html", "timeout": 5, "unhealthy_threshold": 2}, "instances": [], "instances_inservice": [], "instances_inservice_count": 0, "instances_outofservice": [], "instances_outofservice_count": 0, "instances_unknownservice": [], "instances_unknownservice_count": 0, "listener_descriptions": [{"listener": {"instance_port": 80, "instance_protocol": "HTTP", "load_balancer_port": 80, "protocol": "HTTP"}, "policy_names": []}], "load_balancer_name": "test-lb", "policies": {"app_cookie_stickiness_policies": [], "lb_cookie_stickiness_policies": [], "other_policies": []}, "scheme": "internet-facing", "security_groups": ["sg-29d13055"], "source_security_group": {"group_name": "default", "owner_alias": "XXXXXXXXXXXX"}, "subnets": ["subnet-XXXXXXXX", "subnet-XXXXXXXX"], "tags": {}, "vpc_id": "vpc-c248fda4"}]}` |

### Authors

- Michael Schultz (@mjschultz)
- Fernando Jose Pando (@nand0p)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
