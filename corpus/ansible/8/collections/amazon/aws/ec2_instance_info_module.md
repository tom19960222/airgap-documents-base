---
collection: ansible
version: "8"
title: "amazon.aws.ec2_instance_info module – Gather information about ec2 instances in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_instance_info_module.html
fetched_at: 2026-07-28T01:06:26+00:00
---
# amazon.aws.ec2_instance_info module – Gather information about ec2 instances in AWS

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
> see [Requirements](ec2_instance_info_module.md#ansible-collections-amazon-aws-ec2-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_instance_info`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_instance_info_module.md#synopsis)
- [Requirements](ec2_instance_info_module.md#requirements)
- [Parameters](ec2_instance_info_module.md#parameters)
- [Notes](ec2_instance_info_module.md#notes)
- [Examples](ec2_instance_info_module.md#examples)
- [Return Values](ec2_instance_info_module.md#return-values)

## [Synopsis](ec2_instance_info_module.md#id1)

- Gather information about ec2 instances in AWS

## [Requirements](ec2_instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html> for possible filters. Filter names and values are case sensitive.  **Default:** `{}` |
| **instance_ids**  list / elements=string | If you specify one or more instance IDs, only instances that have the specified IDs are returned.  **Default:** `[]` |
| **minimum_uptime**  aliases: uptime  integer | Minimum running uptime in minutes of instances. For example if *uptime* is `60` return all instances that have run more than 60 minutes. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_instance_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_instance_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather information about all instances
  amazon.aws.ec2_instance_info:

- name: Gather information about all instances in AZ ap-southeast-2a
  amazon.aws.ec2_instance_info:
    filters:
      availability-zone: ap-southeast-2a

- name: Gather information about a particular instance using ID
  amazon.aws.ec2_instance_info:
    instance_ids:
      - i-12345678

- name: Gather information about any instance with a tag key Name and value Example
  amazon.aws.ec2_instance_info:
    filters:
      "tag:Name": Example

- name: Gather information about any instance in states "shutting-down", "stopping", "stopped"
  amazon.aws.ec2_instance_info:
    filters:
      instance-state-name: [ "shutting-down", "stopping", "stopped" ]

- name: Gather information about any instance with Name beginning with RHEL and an uptime of at least 60 minutes
  amazon.aws.ec2_instance_info:
    region: "{{ ec2_region }}"
    uptime: 60
    filters:
      "tag:Name": "RHEL-*"
      instance-state-name: [ "running"]
  register: ec2_node_info
```

## [Return Values](ec2_instance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instances**  complex | A list of ec2 instances.  **Returned:** always |
| **ami_launch_index**  integer | The AMI launch index, which can be used to find this instance in the launch group.  **Returned:** always  **Sample:** `0` |
| **architecture**  string | The architecture of the image.  **Returned:** always  **Sample:** `"x86_64"` |
| **block_device_mappings**  complex | Any block device mapping entries for the instance.  **Returned:** always |
| **device_name**  string | The device name exposed to the instance (for example, /dev/sdh or xvdh).  **Returned:** always  **Sample:** `"/dev/sdh"` |
| **ebs**  complex | Parameters used to automatically set up EBS volumes when the instance is launched.  **Returned:** always |
| **attach_time**  string | The time stamp when the attachment initiated.  **Returned:** always  **Sample:** `"2017-03-23T22:51:24+00:00"` |
| **delete_on_termination**  boolean | Indicates whether the volume is deleted on instance termination.  **Returned:** always  **Sample:** `true` |
| **status**  string | The attachment state.  **Returned:** always  **Sample:** `"attached"` |
| **volume_id**  string | The ID of the EBS volume.  **Returned:** always  **Sample:** `"vol-12345678"` |
| **client_token**  string | The idempotency token you provided when you launched the instance, if applicable.  **Returned:** always  **Sample:** `"mytoken"` |
| **cpu_options**  complex | The CPU options set for the instance.  **Returned:** always |
| **core_count**  integer | The number of CPU cores for the instance.  **Returned:** always  **Sample:** `1` |
| **threads_per_core**  integer | The number of threads per CPU core. On supported instance, a value of 1 means Intel Hyper-Threading Technology is disabled.  **Returned:** always  **Sample:** `1` |
| **ebs_optimized**  boolean | Indicates whether the instance is optimized for EBS I/O.  **Returned:** always  **Sample:** `false` |
| **hypervisor**  string | The hypervisor type of the instance.  **Returned:** always  **Sample:** `"xen"` |
| **iam_instance_profile**  complex | The IAM instance profile associated with the instance, if applicable.  **Returned:** always |
| **arn**  string | The Amazon Resource Name (ARN) of the instance profile.  **Returned:** always  **Sample:** `"arn:aws:iam::123456789012:instance-profile/myprofile"` |
| **id**  string | The ID of the instance profile.  **Returned:** always  **Sample:** `"JFJ397FDG400FG9FD1N"` |
| **image_id**  string | The ID of the AMI used to launch the instance.  **Returned:** always  **Sample:** `"ami-0011223344"` |
| **instance_id**  string | The ID of the instance.  **Returned:** always  **Sample:** `"i-012345678"` |
| **instance_type**  string | The instance type size of the running instance.  **Returned:** always  **Sample:** `"t2.micro"` |
| **key_name**  string | The name of the key pair, if this instance was launched with an associated key pair.  **Returned:** always  **Sample:** `"my-key"` |
| **launch_time**  string | The time the instance was launched.  **Returned:** always  **Sample:** `"2017-03-23T22:51:24+00:00"` |
| **monitoring**  complex | The monitoring for the instance.  **Returned:** always |
| **state**  string | Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.  **Returned:** always  **Sample:** `"disabled"` |
| **network_interfaces**  complex | One or more network interfaces for the instance.  **Returned:** always |
| **association**  complex | The association information for an Elastic IPv4 associated with the network interface.  **Returned:** always |
| **ip_owner_id**  string | The ID of the owner of the Elastic IP address.  **Returned:** always  **Sample:** `"amazon"` |
| **public_dns_name**  string | The public DNS name.  **Returned:** always  **Sample:** `""` |
| **public_ip**  string | The public IP address or Elastic IP address bound to the network interface.  **Returned:** always  **Sample:** `"1.2.3.4"` |
| **attachment**  complex | The network interface attachment.  **Returned:** always |
| **attach_time**  string | The time stamp when the attachment initiated.  **Returned:** always  **Sample:** `"2017-03-23T22:51:24+00:00"` |
| **attachment_id**  string | The ID of the network interface attachment.  **Returned:** always  **Sample:** `"eni-attach-3aff3f"` |
| **delete_on_termination**  boolean | Indicates whether the network interface is deleted when the instance is terminated.  **Returned:** always  **Sample:** `true` |
| **device_index**  integer | The index of the device on the instance for the network interface attachment.  **Returned:** always  **Sample:** `0` |
| **status**  string | The attachment state.  **Returned:** always  **Sample:** `"attached"` |
| **description**  string | The description.  **Returned:** always  **Sample:** `"My interface"` |
| **groups**  list / elements=dictionary | One or more security groups.  **Returned:** always |
| **group_id**  string | The ID of the security group.  **Returned:** always  **Sample:** `"sg-abcdef12"` |
| **group_name**  string | The name of the security group.  **Returned:** always  **Sample:** `"mygroup"` |
| **ipv6_addresses**  list / elements=dictionary | One or more IPv6 addresses associated with the network interface.  **Returned:** always |
| **ipv6_address**  string | The IPv6 address.  **Returned:** always  **Sample:** `"2001:0db8:85a3:0000:0000:8a2e:0370:7334"` |
| **mac_address**  string | The MAC address.  **Returned:** always  **Sample:** `"00:11:22:33:44:55"` |
| **network_interface_id**  string | The ID of the network interface.  **Returned:** always  **Sample:** `"eni-01234567"` |
| **owner_id**  string | The AWS account ID of the owner of the network interface.  **Returned:** always  **Sample:** `"01234567890"` |
| **private_ip_address**  string | The IPv4 address of the network interface within the subnet.  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **private_ip_addresses**  list / elements=dictionary | The private IPv4 addresses associated with the network interface.  **Returned:** always |
| **association**  complex | The association information for an Elastic IP address (IPv4) associated with the network interface.  **Returned:** always |
| **ip_owner_id**  string | The ID of the owner of the Elastic IP address.  **Returned:** always  **Sample:** `"amazon"` |
| **public_dns_name**  string | The public DNS name.  **Returned:** always  **Sample:** `""` |
| **public_ip**  string | The public IP address or Elastic IP address bound to the network interface.  **Returned:** always  **Sample:** `"1.2.3.4"` |
| **primary**  boolean | Indicates whether this IPv4 address is the primary private IP address of the network interface.  **Returned:** always  **Sample:** `true` |
| **private_ip_address**  string | The private IPv4 address of the network interface.  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **source_dest_check**  boolean | Indicates whether source/destination checking is enabled.  **Returned:** always  **Sample:** `true` |
| **status**  string | The status of the network interface.  **Returned:** always  **Sample:** `"in-use"` |
| **subnet_id**  string | The ID of the subnet for the network interface.  **Returned:** always  **Sample:** `"subnet-0123456"` |
| **vpc_id**  string | The ID of the VPC for the network interface.  **Returned:** always  **Sample:** `"vpc-0123456"` |
| **placement**  complex | The location where the instance launched, if applicable.  **Returned:** always |
| **availability_zone**  string | The Availability Zone of the instance.  **Returned:** always  **Sample:** `"ap-southeast-2a"` |
| **group_name**  string | The name of the placement group the instance is in (for cluster compute instances).  **Returned:** always  **Sample:** `""` |
| **tenancy**  string | The tenancy of the instance (if the instance is running in a VPC).  **Returned:** always  **Sample:** `"default"` |
| **private_dns_name**  string | The private DNS name.  **Returned:** always  **Sample:** `"ip-10-0-0-1.ap-southeast-2.compute.internal"` |
| **private_ip_address**  string | The IPv4 address of the network interface within the subnet.  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **product_codes**  list / elements=dictionary | One or more product codes.  **Returned:** always |
| **product_code_id**  string | The product code.  **Returned:** always  **Sample:** `"aw0evgkw8ef3n2498gndfgasdfsd5cce"` |
| **product_code_type**  string | The type of product code.  **Returned:** always  **Sample:** `"marketplace"` |
| **public_dns_name**  string | The public DNS name assigned to the instance.  **Returned:** always |
| **public_ip_address**  string | The public IPv4 address assigned to the instance.  **Returned:** always  **Sample:** `"52.0.0.1"` |
| **root_device_name**  string | The device name of the root device.  **Returned:** always  **Sample:** `"/dev/sda1"` |
| **root_device_type**  string | The type of root device used by the AMI.  **Returned:** always  **Sample:** `"ebs"` |
| **security_groups**  list / elements=dictionary | One or more security groups for the instance.  **Returned:** always |
| **group_id**  string | The ID of the security group.  **Returned:** always  **Sample:** `"sg-0123456"` |
| **group_name**  string | The name of the security group.  **Returned:** always  **Sample:** `"my-security-group"` |
| **source_dest_check**  boolean | Indicates whether source/destination checking is enabled.  **Returned:** always  **Sample:** `true` |
| **state**  complex | The current state of the instance.  **Returned:** always |
| **code**  integer | The low byte represents the state.  **Returned:** always  **Sample:** `16` |
| **name**  string | The name of the state.  **Returned:** always  **Sample:** `"running"` |
| **state_transition_reason**  string | The reason for the most recent state transition.  **Returned:** always |
| **subnet_id**  string | The ID of the subnet in which the instance is running.  **Returned:** always  **Sample:** `"subnet-00abcdef"` |
| **tags**  dictionary | Any tags assigned to the instance.  **Returned:** always |
| **virtualization_type**  string | The type of virtualization of the AMI.  **Returned:** always  **Sample:** `"hvm"` |
| **vpc_id**  dictionary | The ID of the VPC the instance is in.  **Returned:** always  **Sample:** `"vpc-0011223344"` |

### Authors

- Michael Schuett (@michaeljs1990)
- Rob White (@wimnat)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
