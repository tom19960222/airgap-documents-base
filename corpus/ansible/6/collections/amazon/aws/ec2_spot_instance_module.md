---
collection: ansible
version: "6"
title: "amazon.aws.ec2_spot_instance module – request, stop, reboot or cancel spot instance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_spot_instance_module.html
fetched_at: 2026-07-27T16:43:46+00:00
---
# amazon.aws.ec2_spot_instance module – request, stop, reboot or cancel spot instance

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
> see [Requirements](ec2_spot_instance_module.md#ansible-collections-amazon-aws-ec2-spot-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_spot_instance`.

New in amazon.aws 2.0.0

- [Synopsis](ec2_spot_instance_module.md#synopsis)
- [Requirements](ec2_spot_instance_module.md#requirements)
- [Parameters](ec2_spot_instance_module.md#parameters)
- [Notes](ec2_spot_instance_module.md#notes)
- [Examples](ec2_spot_instance_module.md#examples)
- [Return Values](ec2_spot_instance_module.md#return-values)

## [Synopsis](ec2_spot_instance_module.md#id1)

- Creates or cancels spot instance requests.

## [Requirements](ec2_spot_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_spot_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **client_token**  string | The idempotency token you provided when you launched the instance, if applicable. |
| **count**  integer | Number of instances to launch.  Default: `1` |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **interruption**  string | The behavior when a Spot Instance is interrupted.  Choices:   - `"hibernate"` - `"stop"` - `"terminate"` ← (default) |
| **launch_group**  string | Launch group for spot requests, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-spot-instances-work.html#spot-launch-group>. |
| **launch_specification**  dictionary | The launch specification. |
| **block_device_mappings**  list / elements=dictionary | A list of hash/dictionaries of volumes to add to the new instance. |
| **device_name**  string | The device name (for example, /dev/sdh or xvdh ). |
| **ebs**  dictionary | Parameters used to automatically set up EBS volumes when the instance is launched, see <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.request_spot_instances> |
| **no_device**  string | To omit the device from the block device mapping, specify an empty string. |
| **virtual_name**  string | The virtual device name |
| **ebs_optimized**  boolean | Whether instance is using optimized EBS volumes, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSOptimized.html>.  Choices:   - `false` ← (default) - `true` |
| **iam_instance_profile**  dictionary | The IAM instance profile. |
| **arn**  string | The Amazon Resource Name (ARN) of the instance profile.  Only one of *arn* or *name* may be specified. |
| **name**  string | The name of the instance profile.  Only one of *arn* or *name* may be specified. |
| **image_id**  string | The ID of the AMI. |
| **instance_type**  string | Instance type to use for the instance, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html>.  Required when creating a new instance. |
| **kernel_id**  string | The ID of the kernel. |
| **key_name**  string | Key to use on the instance.  The SSH key must already exist in AWS in order to use this argument.  Keys can be created / deleted using the [amazon.aws.ec2_key](ec2_key_module.md#ansible-collections-amazon-aws-ec2-key-module) module. |
| **monitoring**  dictionary | Indicates whether basic or detailed monitoring is enabled for the instance. |
| **enabled**  boolean | Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.  Choices:   - `false` ← (default) - `true` |
| **network_interfaces**  list / elements=dictionary | One or more network interfaces. If you specify a network interface, you must specify subnet IDs and security group IDs using the network interface. |
| **associate_carrier_ip_address**  boolean | Indicates whether to assign a carrier IP address to the network interface.  Choices:   - `false` - `true` |
| **associate_public_ip_address**  boolean | Indicates whether to assign a public IPv4 address to an instance you launch in a VPC.  Choices:   - `false` - `true` |
| **delete_on_termination**  boolean | If set to true , the interface is deleted when the instance is terminated. You can specify true only if creating a new network interface when launching an instance.  Choices:   - `false` - `true` |
| **description**  string | The description of the network interface. Applies only if creating a network interface when launching an instance. |
| **device_index**  integer | The position of the network interface in the attachment order. A primary network interface has a device index of 0.  If you specify a network interface when launching an instance, you must specify the device index. |
| **groups**  list / elements=string | The IDs of the security groups for the network interface. Applies only if creating a network interface when launching an instance. |
| **interface_type**  string | The type of network interface.  Choices:   - `"interface"` - `"efa"` |
| **ipv4_prefix_count**  integer | The number of IPv4 delegated prefixes to be automatically assigned to the network interface |
| **ipv4_prefixes**  list / elements=dictionary | One or more IPv4 delegated prefixes to be assigned to the network interface. |
| **ipv6_address_count**  integer | A number of IPv6 addresses to assign to the network interface |
| **ipv6_addresses**  list / elements=dictionary | One or more IPv6 addresses to assign to the network interface. |
| **ipv6address**  string | The IPv6 address. |
| **ipv6_prefix_count**  integer | The number of IPv6 delegated prefixes to be automatically assigned to the network interface |
| **ipv6_prefixes**  list / elements=dictionary | One or more IPv6 delegated prefixes to be assigned to the network interface |
| **network_card_index**  integer | The index of the network card. |
| **network_interface_id**  string | The ID of the network interface. |
| **private_ip_address**  string | The private IPv4 address of the network interface |
| **private_ip_addresses**  list / elements=dictionary | One or more private IPv4 addresses to assign to the network interface |
| **secondary_private_ip_address_count**  integer | The number of secondary private IPv4 addresses. |
| **subnet_id**  string | The ID of the subnet associated with the network interface |
| **placement**  dictionary | The placement information for the instance. |
| **availability_zone**  string | The Availability Zone. |
| **group_name**  string | The name of the placement group. |
| **tenancy**  string | the tenancy of the host  Choices:   - `"default"` ← (default) - `"dedicated"` - `"host"` |
| **ramdisk_id**  string | The ID of the RAM disk. |
| **security_group_ids**  list / elements=string | Security group id (or list of ids) to use with the instance. |
| **security_groups**  list / elements=string | Security group name (or list of group names) to use with the instance.  Only supported with EC2 Classic. To launch in a VPC, use `group_id` |
| **subnet_id**  string | The ID of the subnet in which to launch the instance. |
| **user_data**  string | The base64-encoded user data for the instance. User data is limited to 16 KB. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **spot_instance_request_ids**  list / elements=string | List of strings with IDs of spot requests to be cancelled  Default: `[]` |
| **spot_price**  string | Maximum spot price to bid. If not set, a regular on-demand instance is requested.  A spot request is made with this maximum bid. When it is filled, the instance is started. |
| **spot_type**  string | The type of spot request.  After being interrupted a `persistent` spot instance will be started once there is capacity to fill the request again.  Choices:   - `"one-time"` ← (default) - `"persistent"` |
| **state**  string | Whether the spot request should be created or removed.  When *state=present*, *launch_specification* is required.  When *state=absent*, *spot_instance_request_ids* is required.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tags**  dictionary | A dictionary of key-value pairs for tagging the Spot Instance request on creation. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **zone_group**  string | Name for logical grouping of spot requests.  All spot instances in the request are launched in the same availability zone. |

## [Notes](ec2_spot_instance_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_spot_instance_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Simple Spot Request Creation
  amazon.aws.ec2_spot_instance:
    launch_specification:
      image_id: ami-123456789
      key_name: my-keypair
      instance_type: t2.medium

- name: Spot Request Creation with more options
  amazon.aws.ec2_spot_instance:
    launch_specification:
      image_id: ami-123456789
      key_name: my-keypair
      instance_type: t2.medium
      subnet_id: subnet-12345678
      block_device_mappings:
        - device_name: /dev/sdb
          ebs:
            delete_on_termination: True
            volume_type: gp3
            volume_size: 5
        - device_name: /dev/sdc
          ebs:
            delete_on_termination: True
            volume_type: io2
            volume_size: 30
      network_interfaces:
        - associate_public_ip_address: False
          delete_on_termination: True
          device_index: 0
      placement:
        availability_zone: us-west-2a
      monitoring:
        enabled: False
    spot_price: 0.002
    tags:
      Environment: Testing

- name: Spot Request Termination
  amazon.aws.ec2_spot_instance:
    spot_instance_request_ids: ['sir-12345678', 'sir-abcdefgh']
    state: absent
```

## [Return Values](ec2_spot_instance_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cancelled_spot_request**  string | The spot instance request details that has been cancelled  Returned: always  Sample: `"Spot requests with IDs: sir-1234abcd have been cancelled"` |
| **spot_request**  dictionary | The spot instance request details after creation  Returned: when success  Sample: `{"create_time": "2021-08-23T22:59:12+00:00", "instance_interruption_behavior": "terminate", "launch_specification": {"block_device_mappings": [{"device_name": "/dev/sdb", "ebs": {"delete_on_termination": true, "volume_size": 5, "volume_type": "gp3"}}], "ebs_optimized": false, "iam_instance_profile": {"arn": "arn:aws:iam::EXAMPLE:instance-profile/myinstanceprofile"}, "image_id": "ami-083ac7c7ecf9bb9b0", "instance_type": "t2.small", "key_name": "mykey", "monitoring": {"enabled": false}, "network_interfaces": [{"associate_public_ip_address": false, "delete_on_termination": true, "device_index": 0}], "placement": {"availability_zone": "us-west-2a", "tenancy": "default"}, "security_groups": [{"group_name": "default"}]}, "product_description": "Linux/UNIX", "spot_instance_request_id": "sir-1234abcd", "spot_price": "0.00600", "state": "open", "status": {"code": "pending-evaluation", "message": "Your Spot request has been submitted for review, and is pending evaluation.", "update_time": "2021-08-23T22:59:12+00:00"}, "type": "one-time"}` |

### Authors

- Sri Rachana Achyuthuni (@srirachanaachyuthuni)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
