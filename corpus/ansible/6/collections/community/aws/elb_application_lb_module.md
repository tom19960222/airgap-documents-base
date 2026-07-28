---
collection: ansible
version: "6"
title: "community.aws.elb_application_lb module – Manage an Application Load Balancer"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elb_application_lb_module.html
fetched_at: 2026-07-27T17:04:27+00:00
---
# community.aws.elb_application_lb module – Manage an Application Load Balancer

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
> see [Requirements](elb_application_lb_module.md#ansible-collections-community-aws-elb-application-lb-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elb_application_lb`.

New in community.aws 1.0.0

- [Synopsis](elb_application_lb_module.md#synopsis)
- [Requirements](elb_application_lb_module.md#requirements)
- [Parameters](elb_application_lb_module.md#parameters)
- [Notes](elb_application_lb_module.md#notes)
- [Examples](elb_application_lb_module.md#examples)
- [Return Values](elb_application_lb_module.md#return-values)

## [Synopsis](elb_application_lb_module.md#id1)

- Manage an AWS Application Elastic Load Balancer. See <https://aws.amazon.com/blogs/aws/new-aws-application-load-balancer/> for details.

## [Requirements](elb_application_lb_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elb_application_lb_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_logs_enabled**  boolean | Whether or not to enable access logs.  When set, *access_logs_s3_bucket* must also be set.  Choices:   - `false` - `true` |
| **access_logs_s3_bucket**  string | The name of the S3 bucket for the access logs.  The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permission to write to the bucket.  Required if access logs in Amazon S3 are enabled.  When set, *access_logs_enabled* must also be set. |
| **access_logs_s3_prefix**  string | The prefix for the log location in the S3 bucket.  If you don’t specify a prefix, the access logs are stored in the root of the bucket.  Cannot begin or end with a slash. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **deletion_protection**  boolean | Indicates whether deletion protection for the ALB is enabled.  Defaults to `False`.  Choices:   - `false` - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **http2**  boolean | Indicates whether to enable HTTP2 routing.  Defaults to `True`.  Choices:   - `false` - `true` |
| **http_desync_mitigation_mode**  string  added in community.aws 3.2.0 | Determines how the load balancer handles requests that might pose a security risk to an application.  Defaults to `'defensive'`  Choices:   - `"monitor"` - `"defensive"` - `"strictest"` |
| **http_drop_invalid_header_fields**  boolean  added in community.aws 3.2.0 | Indicates whether HTTP headers with invalid header fields are removed by the load balancer `True` or routed to targets `False`.  Defaults to `False`.  Choices:   - `false` - `true` |
| **http_x_amzn_tls_version_and_cipher_suite**  boolean  added in community.aws 3.2.0 | Indicates whether the two headers are added to the client request before sending it to the target.  Defaults to `False`.  Choices:   - `false` - `true` |
| **http_xff_client_port**  boolean  added in community.aws 3.2.0 | Indicates whether the X-Forwarded-For header should preserve the source port that the client used to connect to the load balancer.  Defaults to `False`.  Choices:   - `false` - `true` |
| **idle_timeout**  integer | The number of seconds to wait before an idle connection is closed. |
| **ip_address_type**  string | Sets the type of IP addresses used by the subnets of the specified Application Load Balancer.  Choices:   - `"ipv4"` - `"dualstack"` |
| **listeners**  list / elements=dictionary | A list of dicts containing listeners to attach to the ALB. See examples for detail of the dict required. Note that listener keys are CamelCased. |
| **Certificates**  list / elements=dictionary | The SSL server certificate. |
| **CertificateArn**  string | The Amazon Resource Name (ARN) of the certificate. |
| **DefaultActions**  list / elements=dictionary / required | The default actions for the listener. |
| **TargetGroupArn**  string | The Amazon Resource Name (ARN) of the target group.  Mutually exclusive with *TargetGroupName*. |
| **TargetGroupName**  string | The name of the target group.  Mutually exclusive with *TargetGroupArn*. |
| **Type**  string | The type of action. |
| **Port**  integer / required | The port on which the load balancer is listening. |
| **Protocol**  string / required | The protocol for connections from clients to the load balancer. |
| **Rules**  list / elements=dictionary | A list of ALB Listener Rules.  For the complete documentation of possible Conditions and Actions please see the boto3 documentation:  <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elbv2.html#ElasticLoadBalancingv2.Client.create_rule> |
| **Actions**  list / elements=dictionary | Actions to apply if all of the rule’s conditions are met. |
| **Conditions**  list / elements=dictionary | Conditions which must be met for the actions to be applied. |
| **Priority**  integer | The rule priority. |
| **SslPolicy**  string | The security policy that defines which ciphers and protocols are supported. |
| **name**  string / required | The name of the load balancer. This name must be unique within your AWS account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_listeners**  boolean | If `yes`, existing listeners will be purged from the ALB to match exactly what is defined by *listeners* parameter.  If the *listeners* parameter is not set then listeners will not be modified.  Choices:   - `false` - `true` ← (default) |
| **purge_rules**  boolean | When set to `no`, keep the existing load balancer rules in place. Will modify and add, but will not delete.  Choices:   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If yes, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **scheme**  string | Internet-facing or internal load balancer. An ALB scheme can not be modified after creation.  Choices:   - `"internet-facing"` ← (default) - `"internal"` |
| **security_groups**  list / elements=string | A list of the names or IDs of the security groups to assign to the load balancer.  Required if *state=present*.  If `[]`, the VPC’s default security group will be used. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or destroy the load balancer.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string | A list of the IDs of the subnets to attach to the load balancer. You can specify only one subnet per Availability Zone. You must specify subnets from at least two Availability Zones.  Required if *state=present*. |
| **tags**  dictionary | A dictionary of one or more tags to assign to the load balancer. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **waf_fail_open**  boolean  added in community.aws 3.2.0 | Indicates whether to allow a AWS WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF.  Defaults to `False`.  Choices:   - `false` - `true` |
| **wait**  boolean | Wait for the load balancer to have a state of ‘active’ before completing. A status check is performed every 15 seconds until a successful state is reached. An error is returned after 40 failed checks.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | The time in seconds to use in conjunction with *wait*. |

## [Notes](elb_application_lb_module.md#id4)

> **Note:**
>
> - Listeners are matched based on port. If a listener’s port is changed then a new listener will be created.
> - Listener rules are matched based on priority. If a rule’s priority is changed then a new rule will be created.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elb_application_lb_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an ALB and attach a listener
- community.aws.elb_application_lb:
    name: myalb
    security_groups:
      - sg-12345678
      - my-sec-group
    subnets:
      - subnet-012345678
      - subnet-abcdef000
    listeners:
      - Protocol: HTTP # Required. The protocol for connections from clients to the load balancer (HTTP or HTTPS) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        # The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
        SslPolicy: ELBSecurityPolicy-2015-05
        Certificates: # The ARN of the certificate (only one certficate ARN should be provided)
          - CertificateArn: arn:aws:iam::12345678987:server-certificate/test.domain.com
        DefaultActions:
          - Type: forward # Required.
            TargetGroupName: # Required. The name of the target group
    state: present

# Create an ALB and attach a listener with logging enabled
- community.aws.elb_application_lb:
    access_logs_enabled: yes
    access_logs_s3_bucket: mybucket
    access_logs_s3_prefix: "logs"
    name: myalb
    security_groups:
      - sg-12345678
      - my-sec-group
    subnets:
      - subnet-012345678
      - subnet-abcdef000
    listeners:
      - Protocol: HTTP # Required. The protocol for connections from clients to the load balancer (HTTP or HTTPS) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        # The security policy that defines which ciphers and protocols are supported. The default is the current predefined security policy.
        SslPolicy: ELBSecurityPolicy-2015-05
        Certificates: # The ARN of the certificate (only one certficate ARN should be provided)
          - CertificateArn: arn:aws:iam::12345678987:server-certificate/test.domain.com
        DefaultActions:
          - Type: forward # Required.
            TargetGroupName: # Required. The name of the target group
    state: present

# Create an ALB with listeners and rules
- community.aws.elb_application_lb:
    name: test-alb
    subnets:
      - subnet-12345678
      - subnet-87654321
    security_groups:
      - sg-12345678
    scheme: internal
    listeners:
      - Protocol: HTTPS
        Port: 443
        DefaultActions:
          - Type: forward
            TargetGroupName: test-target-group
        Certificates:
          - CertificateArn: arn:aws:iam::12345678987:server-certificate/test.domain.com
        SslPolicy: ELBSecurityPolicy-2015-05
        Rules:
          - Conditions:
              - Field: path-pattern
                Values:
                  - '/test'
            Priority: '1'
            Actions:
              - TargetGroupName: test-target-group
                Type: forward
          - Conditions:
              - Field: path-pattern
                Values:
                  - "/redirect-path/*"
            Priority: '2'
            Actions:
              - Type: redirect
                RedirectConfig:
                  Host: "#{host}"
                  Path: "/example/redir" # or /#{path}
                  Port: "#{port}"
                  Protocol: "#{protocol}"
                  Query: "#{query}"
                  StatusCode: "HTTP_302" # or HTTP_301
          - Conditions:
              - Field: path-pattern
                Values:
                  - "/fixed-response-path/"
            Priority: '3'
            Actions:
              - Type: fixed-response
                FixedResponseConfig:
                  ContentType: "text/plain"
                  MessageBody: "This is the page you're looking for"
                  StatusCode: "200"
          - Conditions:
              - Field: host-header
                Values:
                  - "hostname.domain.com"
                  - "alternate.domain.com"
            Priority: '4'
            Actions:
              - TargetGroupName: test-target-group
                Type: forward
    state: present

# Remove an ALB
- community.aws.elb_application_lb:
    name: myalb
    state: absent
```

## [Return Values](elb_application_lb_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **access_logs_s3_bucket**  string | The name of the S3 bucket for the access logs.  Returned: when state is present  Sample: `"mys3bucket"` |
| **access_logs_s3_enabled**  boolean | Indicates whether access logs stored in Amazon S3 are enabled.  Returned: when state is present  Sample: `true` |
| **access_logs_s3_prefix**  string | The prefix for the location in the S3 bucket.  Returned: when state is present  Sample: `"my/logs"` |
| **availability_zones**  list / elements=string | The Availability Zones for the load balancer.  Returned: when state is present  Sample: `[{"load_balancer_addresses": [], "subnet_id": "subnet-aabbccddff", "zone_name": "ap-southeast-2a"}]` |
| **canonical_hosted_zone_id**  string | The ID of the Amazon Route 53 hosted zone associated with the load balancer.  Returned: when state is present  Sample: `"ABCDEF12345678"` |
| **changed**  boolean | Whether an ALB was created/updated/deleted  Returned: always  Sample: `true` |
| **created_time**  string | The date and time the load balancer was created.  Returned: when state is present  Sample: `"2015-02-12T02:14:02+00:00"` |
| **deletion_protection_enabled**  boolean | Indicates whether deletion protection is enabled.  Returned: when state is present  Sample: `true` |
| **dns_name**  string | The public DNS name of the load balancer.  Returned: when state is present  Sample: `"internal-my-elb-123456789.ap-southeast-2.elb.amazonaws.com"` |
| **idle_timeout_timeout_seconds**  integer | The idle timeout value, in seconds.  Returned: when state is present  Sample: `60` |
| **ip_address_type**  string | The type of IP addresses used by the subnets for the load balancer.  Returned: when state is present  Sample: `"ipv4"` |
| **listeners**  complex | Information about the listeners.  Returned: when state is present |
| **certificates**  complex | The SSL server certificate.  Returned: when state is present |
| **certificate_arn**  string | The Amazon Resource Name (ARN) of the certificate.  Returned: when state is present  Sample: `""` |
| **default_actions**  string | The default actions for the listener.  Returned: when state is present |
| **target_group_arn**  string | The Amazon Resource Name (ARN) of the target group.  Returned: when state is present  Sample: `""` |
| **type**  string | The type of action.  Returned: when state is present  Sample: `""` |
| **listener_arn**  string | The Amazon Resource Name (ARN) of the listener.  Returned: when state is present  Sample: `""` |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer.  Returned: when state is present  Sample: `""` |
| **port**  integer | The port on which the load balancer is listening.  Returned: when state is present  Sample: `80` |
| **protocol**  string | The protocol for connections from clients to the load balancer.  Returned: when state is present  Sample: `"HTTPS"` |
| **ssl_policy**  string | The security policy that defines which ciphers and protocols are supported.  Returned: when state is present  Sample: `""` |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer.  Returned: when state is present  Sample: `"arn:aws:elasticloadbalancing:ap-southeast-2:0123456789:loadbalancer/app/my-alb/001122334455"` |
| **load_balancer_name**  string | The name of the load balancer.  Returned: when state is present  Sample: `"my-alb"` |
| **routing_http2_enabled**  boolean | Indicates whether HTTP/2 is enabled.  Returned: when state is present  Sample: `true` |
| **routing_http_desync_mitigation_mode**  string | Determines how the load balancer handles requests that might pose a security risk to an application.  Returned: when state is present  Sample: `"defensive"` |
| **routing_http_drop_invalid_header_fields_enabled**  boolean | Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true) or routed to targets (false).  Returned: when state is present  Sample: `false` |
| **routing_http_x_amzn_tls_version_and_cipher_suite_enabled**  boolean | Indicates whether the two headers are added to the client request before sending it to the target.  Returned: when state is present  Sample: `false` |
| **routing_http_xff_client_port_enabled**  boolean | Indicates whether the X-Forwarded-For header should preserve the source port that the client used to connect to the load balancer.  Returned: when state is present  Sample: `false` |
| **scheme**  string | Internet-facing or internal load balancer.  Returned: when state is present  Sample: `"internal"` |
| **security_groups**  list / elements=string | The IDs of the security groups for the load balancer.  Returned: when state is present  Sample: `["sg-0011223344"]` |
| **state**  dictionary | The state of the load balancer.  Returned: when state is present  Sample: `{"code": "active"}` |
| **tags**  dictionary | The tags attached to the load balancer.  Returned: when state is present  Sample: `{"Tag": "Example"}` |
| **type**  string | The type of load balancer.  Returned: when state is present  Sample: `"application"` |
| **vpc_id**  string | The ID of the VPC for the load balancer.  Returned: when state is present  Sample: `"vpc-0011223344"` |
| **waf_fail_open_enabled**  boolean | Indicates whether to allow a AWS WAF-enabled load balancer to route requests to targets if it is unable to forward the request to AWS WAF.  Returned: when state is present  Sample: `false` |

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
