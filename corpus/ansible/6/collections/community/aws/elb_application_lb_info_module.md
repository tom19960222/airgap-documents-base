---
collection: ansible
version: "6"
title: "community.aws.elb_application_lb_info module – Gather information about Application Load Balancers in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elb_application_lb_info_module.html
fetched_at: 2026-07-27T17:04:28+00:00
---
# community.aws.elb_application_lb_info module – Gather information about Application Load Balancers in AWS

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
> see [Requirements](elb_application_lb_info_module.md#ansible-collections-community-aws-elb-application-lb-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elb_application_lb_info`.

New in community.aws 1.0.0

- [Synopsis](elb_application_lb_info_module.md#synopsis)
- [Requirements](elb_application_lb_info_module.md#requirements)
- [Parameters](elb_application_lb_info_module.md#parameters)
- [Notes](elb_application_lb_info_module.md#notes)
- [Examples](elb_application_lb_info_module.md#examples)
- [Return Values](elb_application_lb_info_module.md#return-values)

## [Synopsis](elb_application_lb_info_module.md#id1)

- Gather information about Application Load Balancers in AWS

## [Requirements](elb_application_lb_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elb_application_lb_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **load_balancer_arns**  list / elements=string | The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call. |
| **names**  list / elements=string | The names of the load balancers. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](elb_application_lb_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elb_application_lb_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather information about all ALBs
  community.aws.elb_application_lb_info:

- name: Gather information about a particular ALB given its ARN
  community.aws.elb_application_lb_info:
    load_balancer_arns:
      - "arn:aws:elasticloadbalancing:ap-southeast-2:001122334455:loadbalancer/app/my-alb/aabbccddeeff"

- name: Gather information about ALBs named 'alb1' and 'alb2'
  community.aws.elb_application_lb_info:
    names:
      - alb1
      - alb2

- name: Gather information about specific ALB
  community.aws.elb_application_lb_info:
    names: "alb-name"
    region: "aws-region"
  register: alb_info
- ansible.builtin.debug:
    var: alb_info
```

## [Return Values](elb_application_lb_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **load_balancers**  complex | a list of load balancers  Returned: always |
| **access_logs_s3_bucket**  string | The name of the S3 bucket for the access logs.  Returned: success  Sample: `"mys3bucket"` |
| **access_logs_s3_enabled**  boolean | Indicates whether access logs stored in Amazon S3 are enabled.  Returned: success  Sample: `true` |
| **access_logs_s3_prefix**  string | The prefix for the location in the S3 bucket.  Returned: success  Sample: `"my/logs"` |
| **availability_zones**  list / elements=string | The Availability Zones for the load balancer.  Returned: success  Sample: `[{"load_balancer_addresses": [], "subnet_id": "subnet-aabbccddff", "zone_name": "ap-southeast-2a"}]` |
| **canonical_hosted_zone_id**  string | The ID of the Amazon Route 53 hosted zone associated with the load balancer.  Returned: success  Sample: `"ABCDEF12345678"` |
| **created_time**  string | The date and time the load balancer was created.  Returned: success  Sample: `"2015-02-12T02:14:02+00:00"` |
| **deletion_protection_enabled**  boolean | Indicates whether deletion protection is enabled.  Returned: success  Sample: `true` |
| **dns_name**  string | The public DNS name of the load balancer.  Returned: success  Sample: `"internal-my-alb-123456789.ap-southeast-2.elb.amazonaws.com"` |
| **idle_timeout_timeout_seconds**  integer | The idle timeout value, in seconds.  Returned: success  Sample: `60` |
| **ip_address_type**  string | The type of IP addresses used by the subnets for the load balancer.  Returned: success  Sample: `"ipv4"` |
| **listeners**  complex | Information about the listeners.  Returned: success |
| **certificates**  complex | The SSL server certificate.  Returned: success |
| **certificate_arn**  string | The Amazon Resource Name (ARN) of the certificate.  Returned: success  Sample: `""` |
| **default_actions**  string | The default actions for the listener.  Returned: success |
| **target_group_arn**  string | The Amazon Resource Name (ARN) of the target group.  Returned: success  Sample: `""` |
| **type**  string | The type of action.  Returned: success  Sample: `""` |
| **listener_arn**  string | The Amazon Resource Name (ARN) of the listener.  Returned: success  Sample: `""` |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer.  Returned: success  Sample: `""` |
| **port**  integer | The port on which the load balancer is listening.  Returned: success  Sample: `80` |
| **protocol**  string | The protocol for connections from clients to the load balancer.  Returned: success  Sample: `"HTTPS"` |
| **ssl_policy**  string | The security policy that defines which ciphers and protocols are supported.  Returned: success  Sample: `""` |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer.  Returned: success  Sample: `"arn:aws:elasticloadbalancing:ap-southeast-2:0123456789:loadbalancer/app/my-alb/001122334455"` |
| **load_balancer_name**  string | The name of the load balancer.  Returned: success  Sample: `"my-alb"` |
| **routing_http2_enabled**  boolean | Indicates whether HTTP/2 is enabled.  Returned: success  Sample: `true` |
| **routing_http_desync_mitigation_mode**  string | Determines how the load balancer handles requests that might pose a security risk to an application.  Returned: success  Sample: `"defensive"` |
| **routing_http_drop_invalid_header_fields_enabled**  boolean | Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true) or routed to targets (false).  Returned: success  Sample: `false` |
| **routing_http_x_amzn_tls_version_and_cipher_suite_enabled**  boolean | Indicates whether the two headers are added to the client request before sending it to the target.  Returned: success  Sample: `false` |
| **routing_http_xff_client_port_enabled**  boolean | Indicates whether the X-Forwarded-For header should preserve the source port that the client used to connect to the load balancer.  Returned: success  Sample: `false` |
| **scheme**  string | Internet-facing or internal load balancer.  Returned: success  Sample: `"internal"` |
| **security_groups**  list / elements=string | The IDs of the security groups for the load balancer.  Returned: success  Sample: `["sg-0011223344"]` |
| **state**  dictionary | The state of the load balancer.  Returned: success  Sample: `{"code": "active"}` |
| **tags**  dictionary | The tags attached to the load balancer.  Returned: success  Sample: `{"Tag": "Example"}` |
| **type**  string | The type of load balancer.  Returned: success  Sample: `"application"` |
| **vpc_id**  string | The ID of the VPC for the load balancer.  Returned: success  Sample: `"vpc-0011223344"` |
| **waf_fail_open_enabled**  boolean | Indicates whether to allow a AWS WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF.  Returned: success  Sample: `false` |

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
