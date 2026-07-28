---
collection: ansible
version: "6"
title: "amazon.aws.ec2_instance_info module – Gather information about ec2 instances in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_instance_info_module.html
fetched_at: 2026-07-27T16:43:44+00:00
---
# amazon.aws.ec2_instance_info module – Gather information about ec2 instances in AWS

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html> for possible filters. Filter names and values are case sensitive.  Default: `{}` |
| **instance_ids**  list / elements=string | If you specify one or more instance IDs, only instances that have the specified IDs are returned. |
| **minimum_uptime**  aliases: uptime  integer | Minimum running uptime in minutes of instances. For example if *uptime* is `60` return all instances that have run more than 60 minutes. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_instance_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
| **instances**  complex | a list of ec2 instances  Returned: always |
| **ami_launch_index**  integer | The AMI launch index, which can be used to find this instance in the launch group.  Returned: always  Sample: `0` |
| **architecture**  string | The architecture of the image  Returned: always  Sample: `"x86_64"` |
| **block_device_mappings**  complex | Any block device mapping entries for the instance.  Returned: always |
| **device_name**  string | The device name exposed to the instance (for example, /dev/sdh or xvdh).  Returned: always  Sample: `"/dev/sdh"` |
| **ebs**  complex | Parameters used to automatically set up EBS volumes when the instance is launched.  Returned: always |
| **attach_time**  string | The time stamp when the attachment initiated.  Returned: always  Sample: `"2017-03-23T22:51:24+00:00"` |
| **delete_on_termination**  boolean | Indicates whether the volume is deleted on instance termination.  Returned: always  Sample: `true` |
| **status**  string | The attachment state.  Returned: always  Sample: `"attached"` |
| **volume_id**  string | The ID of the EBS volume  Returned: always  Sample: `"vol-12345678"` |
| **client_token**  string | The idempotency token you provided when you launched the instance, if applicable.  Returned: always  Sample: `"mytoken"` |
| **cpu_options**  complex | The CPU options set for the instance.  Returned: always |
| **core_count**  integer | The number of CPU cores for the instance.  Returned: always  Sample: `1` |
| **threads_per_core**  integer | The number of threads per CPU core. On supported instance, a value of 1 means Intel Hyper-Threading Technology is disabled.  Returned: always  Sample: `1` |
| **ebs_optimized**  boolean | Indicates whether the instance is optimized for EBS I/O.  Returned: always  Sample: `false` |
| **hypervisor**  string | The hypervisor type of the instance.  Returned: always  Sample: `"xen"` |
| **iam_instance_profile**  complex | The IAM instance profile associated with the instance, if applicable.  Returned: always |
| **arn**  string | The Amazon Resource Name (ARN) of the instance profile.  Returned: always  Sample: `"arn:aws:iam::000012345678:instance-profile/myprofile"` |
| **id**  string | The ID of the instance profile  Returned: always  Sample: `"JFJ397FDG400FG9FD1N"` |
| **image_id**  string | The ID of the AMI used to launch the instance.  Returned: always  Sample: `"ami-0011223344"` |
| **instance_id**  string | The ID of the instance.  Returned: always  Sample: `"i-012345678"` |
| **instance_type**  string | The instance type size of the running instance.  Returned: always  Sample: `"t2.micro"` |
| **key_name**  string | The name of the key pair, if this instance was launched with an associated key pair.  Returned: always  Sample: `"my-key"` |
| **launch_time**  string | The time the instance was launched.  Returned: always  Sample: `"2017-03-23T22:51:24+00:00"` |
| **monitoring**  complex | The monitoring for the instance.  Returned: always |
| **state**  string | Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.  Returned: always  Sample: `"disabled"` |
| **network_interfaces**  complex | One or more network interfaces for the instance.  Returned: always |
| **association**  complex | The association information for an Elastic IPv4 associated with the network interface.  Returned: always |
| **ip_owner_id**  string | The ID of the owner of the Elastic IP address.  Returned: always  Sample: `"amazon"` |
| **public_dns_name**  string | The public DNS name.  Returned: always  Sample: `""` |
| **public_ip**  string | The public IP address or Elastic IP address bound to the network interface.  Returned: always  Sample: `"1.2.3.4"` |
| **attachment**  complex | The network interface attachment.  Returned: always |
| **attach_time**  string | The time stamp when the attachment initiated.  Returned: always  Sample: `"2017-03-23T22:51:24+00:00"` |
| **attachment_id**  string | The ID of the network interface attachment.  Returned: always  Sample: `"eni-attach-3aff3f"` |
| **delete_on_termination**  boolean | Indicates whether the network interface is deleted when the instance is terminated.  Returned: always  Sample: `true` |
| **device_index**  integer | The index of the device on the instance for the network interface attachment.  Returned: always  Sample: `0` |
| **status**  string | The attachment state.  Returned: always  Sample: `"attached"` |
| **description**  string | The description.  Returned: always  Sample: `"My interface"` |
| **groups**  list / elements=dictionary | One or more security groups.  Returned: always |
| **group_id**  string | The ID of the security group.  Returned: always  Sample: `"sg-abcdef12"` |
| **group_name**  string | The name of the security group.  Returned: always  Sample: `"mygroup"` |
| **ipv6_addresses**  list / elements=dictionary | One or more IPv6 addresses associated with the network interface.  Returned: always |
| **ipv6_address**  string | The IPv6 address.  Returned: always  Sample: `"2001:0db8:85a3:0000:0000:8a2e:0370:7334"` |
| **mac_address**  string | The MAC address.  Returned: always  Sample: `"00:11:22:33:44:55"` |
| **network_interface_id**  string | The ID of the network interface.  Returned: always  Sample: `"eni-01234567"` |
| **owner_id**  string | The AWS account ID of the owner of the network interface.  Returned: always  Sample: `"01234567890"` |
| **private_ip_address**  string | The IPv4 address of the network interface within the subnet.  Returned: always  Sample: `"10.0.0.1"` |
| **private_ip_addresses**  list / elements=dictionary | The private IPv4 addresses associated with the network interface.  Returned: always |
| **association**  complex | The association information for an Elastic IP address (IPv4) associated with the network interface.  Returned: always |
| **ip_owner_id**  string | The ID of the owner of the Elastic IP address.  Returned: always  Sample: `"amazon"` |
| **public_dns_name**  string | The public DNS name.  Returned: always  Sample: `""` |
| **public_ip**  string | The public IP address or Elastic IP address bound to the network interface.  Returned: always  Sample: `"1.2.3.4"` |
| **primary**  boolean | Indicates whether this IPv4 address is the primary private IP address of the network interface.  Returned: always  Sample: `true` |
| **private_ip_address**  string | The private IPv4 address of the network interface.  Returned: always  Sample: `"10.0.0.1"` |
| **source_dest_check**  boolean | Indicates whether source/destination checking is enabled.  Returned: always  Sample: `true` |
| **status**  string | The status of the network interface.  Returned: always  Sample: `"in-use"` |
| **subnet_id**  string | The ID of the subnet for the network interface.  Returned: always  Sample: `"subnet-0123456"` |
| **vpc_id**  string | The ID of the VPC for the network interface.  Returned: always  Sample: `"vpc-0123456"` |
| **placement**  complex | The location where the instance launched, if applicable.  Returned: always |
| **availability_zone**  string | The Availability Zone of the instance.  Returned: always  Sample: `"ap-southeast-2a"` |
| **group_name**  string | The name of the placement group the instance is in (for cluster compute instances).  Returned: always  Sample: `""` |
| **tenancy**  string | The tenancy of the instance (if the instance is running in a VPC).  Returned: always  Sample: `"default"` |
| **private_dns_name**  string | The private DNS name.  Returned: always  Sample: `"ip-10-0-0-1.ap-southeast-2.compute.internal"` |
| **private_ip_address**  string | The IPv4 address of the network interface within the subnet.  Returned: always  Sample: `"10.0.0.1"` |
| **product_codes**  list / elements=dictionary | One or more product codes.  Returned: always |
| **product_code_id**  string | The product code.  Returned: always  Sample: `"aw0evgkw8ef3n2498gndfgasdfsd5cce"` |
| **product_code_type**  string | The type of product code.  Returned: always  Sample: `"marketplace"` |
| **public_dns_name**  string | The public DNS name assigned to the instance.  Returned: always |
| **public_ip_address**  string | The public IPv4 address assigned to the instance  Returned: always  Sample: `"52.0.0.1"` |
| **root_device_name**  string | The device name of the root device  Returned: always  Sample: `"/dev/sda1"` |
| **root_device_type**  string | The type of root device used by the AMI.  Returned: always  Sample: `"ebs"` |
| **security_groups**  list / elements=dictionary | One or more security groups for the instance.  Returned: always |
| **group_id**  string | The ID of the security group.  Returned: always  Sample: `"sg-0123456"` |
| **group_name**  string | The name of the security group.  Returned: always  Sample: `"my-security-group"` |
| **source_dest_check**  boolean | Indicates whether source/destination checking is enabled.  Returned: always  Sample: `true` |
| **state**  complex | The current state of the instance.  Returned: always |
| **code**  integer | The low byte represents the state.  Returned: always  Sample: `16` |
| **name**  string | The name of the state.  Returned: always  Sample: `"running"` |
| **state_transition_reason**  string | The reason for the most recent state transition.  Returned: always |
| **subnet_id**  string | The ID of the subnet in which the instance is running.  Returned: always  Sample: `"subnet-00abcdef"` |
| **tags**  dictionary | Any tags assigned to the instance.  Returned: always |
| **virtualization_type**  string | The type of virtualization of the AMI.  Returned: always  Sample: `"hvm"` |
| **vpc_id**  dictionary | The ID of the VPC the instance is in.  Returned: always  Sample: `"vpc-0011223344"` |

### Authors

- Michael Schuett (@michaeljs1990)
- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
