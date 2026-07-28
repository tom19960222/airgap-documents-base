---
collection: ansible
version: "8"
title: "community.aws.elb_network_lb module – Manage a Network Load Balancer"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/elb_network_lb_module.html
fetched_at: 2026-07-28T01:41:13+00:00
---
# community.aws.elb_network_lb module – Manage a Network Load Balancer

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
> see [Requirements](elb_network_lb_module.md#ansible-collections-community-aws-elb-network-lb-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elb_network_lb`.

New in community.aws 1.0.0

- [Synopsis](elb_network_lb_module.md#synopsis)
- [Requirements](elb_network_lb_module.md#requirements)
- [Parameters](elb_network_lb_module.md#parameters)
- [Notes](elb_network_lb_module.md#notes)
- [Examples](elb_network_lb_module.md#examples)
- [Return Values](elb_network_lb_module.md#return-values)

## [Synopsis](elb_network_lb_module.md#id1)

- Manage an AWS Network Elastic Load Balancer. See <https://aws.amazon.com/blogs/aws/new-network-load-balancer-effortless-scaling-to-millions-of-requests-per-second/> for details.

## [Requirements](elb_network_lb_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](elb_network_lb_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cross_zone_load_balancing**  boolean | Indicates whether cross-zone load balancing is enabled.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **deletion_protection**  boolean | Indicates whether deletion protection for the ELB is enabled.  Defaults to `false`.  **Choices:**   - `false` - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **ip_address_type**  string | Sets the type of IP addresses used by the subnets of the specified Application Load Balancer.  **Choices:**   - `"ipv4"` - `"dualstack"` |
| **listeners**  list / elements=dictionary | A list of dicts containing listeners to attach to the ELB. See examples for detail of the dict required. Note that listener keys are CamelCased. |
| **Certificates**  list / elements=dictionary | The SSL server certificate. |
| **CertificateArn**  string | The Amazon Resource Name (ARN) of the certificate. |
| **DefaultActions**  list / elements=dictionary / required | The default actions for the listener. |
| **TargetGroupArn**  string | The Amazon Resource Name (ARN) of the target group.  Mutually exclusive with *TargetGroupName*. |
| **TargetGroupName**  string | The name of the target group.  Mutually exclusive with *TargetGroupArn*. |
| **Type**  string | The type of action. |
| **Port**  integer / required | The port on which the load balancer is listening. |
| **Protocol**  string / required | The protocol for connections from clients to the load balancer. |
| **SslPolicy**  string | The security policy that defines which ciphers and protocols are supported. |
| **name**  string / required | The name of the load balancer. This name must be unique within your AWS account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_listeners**  boolean | If *purge_listeners=true*, existing listeners will be purged from the ELB to match exactly what is defined by *listeners* parameter.  If the *listeners* parameter is not set then listeners will not be modified.  **Choices:**   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **scheme**  string | Internet-facing or internal load balancer. An ELB scheme can not be modified after creation.  **Choices:**   - `"internet-facing"` ← (default) - `"internal"` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or destroy the load balancer.  The default changed from `'absent'` to `'present'` in release 4.0.0.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet_mappings**  list / elements=dictionary | A list of dicts containing the IDs of the subnets to attach to the load balancer. You can also specify the allocation ID of an Elastic IP to attach to the load balancer or the internal IP address for an internal load balancer. You can specify one Elastic IP address or internal address per subnet.  This parameter is mutually exclusive with *subnets*. |
| **subnets**  list / elements=string | A list of the IDs of the subnets to attach to the load balancer. You can specify only one subnet per Availability Zone. You must specify subnets from at least two Availability Zones.  Required when *state=present*.  This parameter is mutually exclusive with *subnet_mappings*. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Whether or not to wait for the network load balancer to reach the desired state.  **Choices:**   - `false` - `true` |
| **wait_timeout**  integer | The duration in seconds to wait, used in conjunction with *wait*. |

## [Notes](elb_network_lb_module.md#id4)

> **Note:**
>
> - Listeners are matched based on port. If a listener’s port is changed then a new listener will be created.
> - Listener rules are matched based on priority. If a rule’s priority is changed then a new rule will be created.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](elb_network_lb_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create an ELB and attach a listener
  community.aws.elb_network_lb:
    name: myelb
    subnets:
      - subnet-012345678
      - subnet-abcdef000
    listeners:
      - Protocol: TCP # Required. The protocol for connections from clients to the load balancer (TCP, TLS, UDP or TCP_UDP) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        DefaultActions:
          - Type: forward # Required. Only 'forward' is accepted at this time
            TargetGroupName: mytargetgroup # Required. The name of the target group
    state: present

- name: Create an ELB with an attached Elastic IP address
  community.aws.elb_network_lb:
    name: myelb
    subnet_mappings:
      - SubnetId: subnet-012345678
        AllocationId: eipalloc-aabbccdd
    listeners:
      - Protocol: TCP # Required. The protocol for connections from clients to the load balancer (TCP, TLS, UDP or TCP_UDP) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        DefaultActions:
          - Type: forward # Required. Only 'forward' is accepted at this time
            TargetGroupName: mytargetgroup # Required. The name of the target group
    state: present

- name: Create an internal ELB with a specified IP address
  community.aws.elb_network_lb:
    name: myelb
    scheme: internal
    subnet_mappings:
      - SubnetId: subnet-012345678
        PrivateIPv4Address: 192.168.0.1 # Must be an address from within the CIDR of the subnet.
    listeners:
      - Protocol: TCP # Required. The protocol for connections from clients to the load balancer (TCP, TLS, UDP or TCP_UDP) (case-sensitive).
        Port: 80 # Required. The port on which the load balancer is listening.
        DefaultActions:
          - Type: forward # Required. Only 'forward' is accepted at this time
            TargetGroupName: mytargetgroup # Required. The name of the target group
    state: present

- name: Remove an ELB
  community.aws.elb_network_lb:
    name: myelb
    state: absent
```

## [Return Values](elb_network_lb_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **load_balancer**  dictionary  *added in community.aws 5.0.0* | A representation of the Network Load Balancer  **Returned:** when state is present |
| **availability_zones**  list / elements=string | The Availability Zones for the load balancer.  **Returned:** when state is present  **Sample:** `["[{'subnet_id': 'subnet-aabbccddff'", " 'zone_name': 'ap-southeast-2a'", " 'load_balancer_addresses': []}]"]` |
| **canonical_hosted_zone_id**  string | The ID of the Amazon Route 53 hosted zone associated with the load balancer.  **Returned:** when state is present  **Sample:** `"ABCDEF12345678"` |
| **created_time**  string | The date and time the load balancer was created.  **Returned:** when state is present  **Sample:** `"2015-02-12T02:14:02+00:00"` |
| **deletion_protection_enabled**  string | Indicates whether deletion protection is enabled.  **Returned:** when state is present  **Sample:** `"True"` |
| **dns_name**  string | The public DNS name of the load balancer.  **Returned:** when state is present  **Sample:** `"internal-my-elb-123456789.ap-southeast-2.elb.amazonaws.com"` |
| **idle_timeout_timeout_seconds**  string | The idle timeout value, in seconds.  **Returned:** when state is present  **Sample:** `"60"` |
| **ip_address_type**  string | The type of IP addresses used by the subnets for the load balancer.  **Returned:** when state is present  **Sample:** `"ipv4"` |
| **listeners**  complex | Information about the listeners.  **Returned:** when state is present |
| **certificates**  complex | The SSL server certificate.  **Returned:** when state is present |
| **certificate_arn**  string | The Amazon Resource Name (ARN) of the certificate.  **Returned:** when state is present  **Sample:** `""` |
| **default_actions**  string | The default actions for the listener.  **Returned:** when state is present |
| **target_group_arn**  string | The Amazon Resource Name (ARN) of the target group.  **Returned:** when state is present  **Sample:** `""` |
| **type**  string | The type of action.  **Returned:** when state is present  **Sample:** `""` |
| **listener_arn**  string | The Amazon Resource Name (ARN) of the listener.  **Returned:** when state is present  **Sample:** `""` |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer.  **Returned:** when state is present  **Sample:** `""` |
| **port**  integer | The port on which the load balancer is listening.  **Returned:** when state is present  **Sample:** `80` |
| **protocol**  string | The protocol for connections from clients to the load balancer.  **Returned:** when state is present  **Sample:** `"HTTPS"` |
| **ssl_policy**  string | The security policy that defines which ciphers and protocols are supported.  **Returned:** when state is present  **Sample:** `""` |
| **load_balancer_arn**  string | The Amazon Resource Name (ARN) of the load balancer.  **Returned:** when state is present  **Sample:** `"arn:aws:elasticloadbalancing:ap-southeast-2:123456789012:loadbalancer/app/my-elb/001122334455"` |
| **load_balancer_name**  string | The name of the load balancer.  **Returned:** when state is present  **Sample:** `"my-elb"` |
| **load_balancing_cross_zone_enabled**  string | Indicates whether cross-zone load balancing is enabled.  **Returned:** when state is present  **Sample:** `"True"` |
| **scheme**  string | Internet-facing or internal load balancer.  **Returned:** when state is present  **Sample:** `"internal"` |
| **state**  dictionary | The state of the load balancer.  **Returned:** when state is present  **Sample:** `{"code": "active"}` |
| **tags**  dictionary | The tags attached to the load balancer.  **Returned:** when state is present  **Sample:** `{"Tag": "Example"}` |
| **type**  string | The type of load balancer.  **Returned:** when state is present  **Sample:** `"network"` |
| **vpc_id**  string | The ID of the VPC for the load balancer.  **Returned:** when state is present  **Sample:** `"vpc-0011223344"` |

### Authors

- Rob White (@wimnat)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
