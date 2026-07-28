---
collection: ansible
version: "8"
title: "amazon.aws.elb_application_lb_info module – Gather information about Application Load Balancers in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/elb_application_lb_info_module.html
fetched_at: 2026-07-28T01:06:48+00:00
---
# amazon.aws.elb_application_lb_info module – Gather information about Application Load Balancers in AWS

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
> see [Requirements](elb_application_lb_info_module.md#ansible-collections-amazon-aws-elb-application-lb-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.elb_application_lb_info`.

New in amazon.aws 5.0.0

- [Synopsis](elb_application_lb_info_module.md#synopsis)
- [Requirements](elb_application_lb_info_module.md#requirements)
- [Parameters](elb_application_lb_info_module.md#parameters)
- [Notes](elb_application_lb_info_module.md#notes)
- [Examples](elb_application_lb_info_module.md#examples)
- [Return Values](elb_application_lb_info_module.md#return-values)

## [Synopsis](elb_application_lb_info_module.md#id1)

- Gather information about Application Load Balancers in AWS
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](elb_application_lb_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](elb_application_lb_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **load_balancer_arns**  list / elements=string | The Amazon Resource Names (ARN) of the load balancers. You can specify up to 20 load balancers in a single call. |
| **names**  list / elements=string | The names of the load balancers. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](elb_application_lb_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](elb_application_lb_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather information about all ALBs
  amazon.aws.elb_application_lb_info:

- name: Gather information about a particular ALB given its ARN
  amazon.aws.elb_application_lb_info:
    load_balancer_arns:
      - "arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:loadbalancer/app/my-alb/aabbccddeeff"

- name: Gather information about ALBs named 'alb1' and 'alb2'
  amazon.aws.elb_application_lb_info:
    names:
      - alb1
      - alb2

- name: Gather information about specific ALB
  amazon.aws.elb_application_lb_info:
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
| **load_balancers**  complex | a list of load balancers  **Returned:** always |
| **access_logs_s3_bucket**  string | The name of the S3 bucket for the access logs.  **Returned:** success  **Sample:** `"mys3bucket"` |
| **access_logs_s3_enabled**  boolean | Indicates whether access logs stored in Amazon S3 are enabled.  **Returned:** success  **Sample:** `true` |
| **access_logs_s3_prefix**  string | The prefix for the location in the S3 bucket.  **Returned:** success  **Sample:** `"my/logs"` |
| **availability_zones**  list / elements=string | The Availability Zones for the load balancer.  **Returned:** success  **Sample:** `[{"load_balancer_addresses": [], "subnet_id": "subnet-aabbccddff", "zone_name": "ap-southeast-2a"}]` |
| **canonical_hosted_zone_id**  string | The ID of the Amazon Route 53 hosted zone associated with the load balancer.  **Returned:** success  **Sample:** `"ABCDEF12345678"` |
| **created_time**  string | The date and time the load balancer was created.  **Returned:** success  **Sample:** `"2015-02-12T02:14:02+00:00"` |
| **deletion_protection_enabled**  boolean | Indicates whether deletion protection is enabled.  **Returned:** success  **Sample:** `true` |
| **dns_name**  string | The public DNS name of the load balancer.  **Returned:** success  **Sample:** `"internal-my-alb-123456789.ap-southeast-2.elb.amazonaws.com"` |
| **idle_timeout_timeout_seconds**  integer | The idle timeout value, in seconds.  **Returned:** success  **Sample:** `60` |
| **ip_address_type**  string | The type of IP addresses used by the subnets for the load balancer.  **Returned:** success  **Sample:** `"ipv4"` |
| **listeners**  complex | Information about the listeners.  **Returned:** success |
| **certificates**  complex | The SSL server certificate.  **Returned:** success |
| **certificate_arn**  string | The Amazon Resource Name (ARN) of the certificate.  **Returned:** success  **Sample:** `""` |
| **default_actions**  string | The default actions for the listener.  **Returned:** success |
| **target_group_arn**  string | The Amazon Resource Name (ARN) of the target group.  **Returned:** success  **Sample:** `""` |
| **type**  string | The type of action.  **Returned:** success  **Sample:** `""` |
| **listener_arn**  string | The Amazon Resource Name (ARN) of the listener.  **Returned:** success  **Sample:** `""` |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer.  **Returned:** success  **Sample:** `""` |
| **port**  integer | The port on which the load balancer is listening.  **Returned:** success  **Sample:** `80` |
| **protocol**  string | The protocol for connections from clients to the load balancer.  **Returned:** success  **Sample:** `"HTTPS"` |
| **ssl_policy**  string | The security policy that defines which ciphers and protocols are supported.  **Returned:** success  **Sample:** `""` |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer.  **Returned:** success  **Sample:** `"arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:loadbalancer/app/my-alb/001122334455"` |
| **load_balancer_name**  string | The name of the load balancer.  **Returned:** success  **Sample:** `"my-alb"` |
| **routing_http2_enabled**  boolean | Indicates whether HTTP/2 is enabled.  **Returned:** success  **Sample:** `true` |
| **routing_http_desync_mitigation_mode**  string | Determines how the load balancer handles requests that might pose a security risk to an application.  **Returned:** success  **Sample:** `"defensive"` |
| **routing_http_drop_invalid_header_fields_enabled**  boolean | Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true) or routed to targets (false).  **Returned:** success  **Sample:** `false` |
| **routing_http_x_amzn_tls_version_and_cipher_suite_enabled**  boolean | Indicates whether the two headers are added to the client request before sending it to the target.  **Returned:** success  **Sample:** `false` |
| **routing_http_xff_client_port_enabled**  boolean | Indicates whether the X-Forwarded-For header should preserve the source port that the client used to connect to the load balancer.  **Returned:** success  **Sample:** `false` |
| **scheme**  string | Internet-facing or internal load balancer.  **Returned:** success  **Sample:** `"internal"` |
| **security_groups**  list / elements=string | The IDs of the security groups for the load balancer.  **Returned:** success  **Sample:** `["sg-0011223344"]` |
| **state**  dictionary | The state of the load balancer.  **Returned:** success  **Sample:** `{"code": "active"}` |
| **tags**  dictionary | The tags attached to the load balancer.  **Returned:** success  **Sample:** `{"Tag": "Example"}` |
| **type**  string | The type of load balancer.  **Returned:** success  **Sample:** `"application"` |
| **vpc_id**  string | The ID of the VPC for the load balancer.  **Returned:** success  **Sample:** `"vpc-0011223344"` |
| **waf_fail_open_enabled**  boolean | Indicates whether to allow a AWS WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF.  **Returned:** success  **Sample:** `false` |

### Authors

- Rob White (@wimnat)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
