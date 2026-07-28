---
collection: ansible
version: "6"
title: "amazon.aws.ec2_eni_info module – Gather information about ec2 ENI interfaces in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_eni_info_module.html
fetched_at: 2026-07-27T16:43:42+00:00
---
# amazon.aws.ec2_eni_info module – Gather information about ec2 ENI interfaces in AWS

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
> see [Requirements](ec2_eni_info_module.md#ansible-collections-amazon-aws-ec2-eni-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_eni_info`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_eni_info_module.md#synopsis)
- [Requirements](ec2_eni_info_module.md#requirements)
- [Parameters](ec2_eni_info_module.md#parameters)
- [Notes](ec2_eni_info_module.md#notes)
- [Examples](ec2_eni_info_module.md#examples)
- [Return Values](ec2_eni_info_module.md#return-values)

## [Synopsis](ec2_eni_info_module.md#id1)

- Gather information about ec2 ENI interfaces in AWS.

## [Requirements](ec2_eni_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_eni_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **eni_id**  string  added in amazon.aws 1.3.0 | The ID of the ENI.  This option is mutually exclusive of *filters*. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html> for possible filters.  This option is mutually exclusive of *eni_id*. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_eni_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_eni_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather information about all ENIs
- amazon.aws.ec2_eni_info:

# Gather information about a particular ENI
- amazon.aws.ec2_eni_info:
    filters:
      network-interface-id: eni-xxxxxxx
```

## [Return Values](ec2_eni_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **network_interfaces**  complex | List of matching elastic network interfaces  Returned: always |
| **association**  dictionary | Info of associated elastic IP (EIP)  Returned: When an ENI is associated with an EIP  Sample: `{"allocation_id": "eipalloc-5sdf123", "association_id": "eipassoc-8sdf123", "ip_owner_id": "4415120123456", "public_dns_name": "ec2-52-1-0-63.compute-1.amazonaws.com", "public_ip": "52.1.0.63"}` |
| **attachment**  dictionary | Info about attached ec2 instance  Returned: When an ENI is attached to an ec2 instance  Sample: `{"attach_time": "2017-08-05T15:25:47+00:00", "attachment_id": "eni-attach-149d21234", "delete_on_termination": false, "device_index": 1, "instance_id": "i-15b8d3cadbafa1234", "instance_owner_id": "4415120123456", "status": "attached"}` |
| **availability_zone**  string | Availability zone of ENI  Returned: always  Sample: `"us-east-1b"` |
| **description**  string | Description text for ENI  Returned: always  Sample: `"My favourite network interface"` |
| **groups**  list / elements=string | List of attached security groups  Returned: always  Sample: `[{"group_id": "sg-26d0f1234", "group_name": "my_ec2_security_group"}]` |
| **id**  string | The id of the ENI (alias for network_interface_id)  Returned: always  Sample: `"eni-392fsdf"` |
| **interface_type**  string | Type of the network interface  Returned: always  Sample: `"interface"` |
| **ipv6_addresses**  list / elements=string | List of IPv6 addresses for this interface  Returned: always  Sample: `[]` |
| **mac_address**  string | MAC address of the network interface  Returned: always  Sample: `"0a:f8:10:2f:ab:a1"` |
| **name**  string  added in amazon.aws 1.3.0 | The Name tag of the ENI, often displayed in the AWS UIs as Name  Returned: When a Name tag has been set |
| **network_interface_id**  string | The id of the ENI  Returned: always  Sample: `"eni-392fsdf"` |
| **owner_id**  string | AWS account id of the owner of the ENI  Returned: always  Sample: `"4415120123456"` |
| **private_dns_name**  string | Private DNS name for the ENI  Returned: always  Sample: `"ip-172-16-1-180.ec2.internal"` |
| **private_ip_address**  string | Private IP address for the ENI  Returned: always  Sample: `"172.16.1.180"` |
| **private_ip_addresses**  list / elements=string | List of private IP addresses attached to the ENI  Returned: always  Sample: `[]` |
| **requester_id**  string | The ID of the entity that launched the ENI  Returned: always  Sample: `"AIDAIONYVJQNIAZFT3ABC"` |
| **requester_managed**  boolean | Indicates whether the network interface is being managed by an AWS service.  Returned: always  Sample: `false` |
| **source_dest_check**  boolean | Indicates whether the network interface performs source/destination checking.  Returned: always  Sample: `false` |
| **status**  string | Indicates if the network interface is attached to an instance or not  Returned: always  Sample: `"in-use"` |
| **subnet_id**  string | Subnet ID the ENI is in  Returned: always  Sample: `"subnet-7bbf01234"` |
| **tag_set**  dictionary | Dictionary of tags added to the ENI  Returned: always  Sample: `{}` |
| **tags**  dictionary  added in amazon.aws 1.3.0 | Dictionary of tags added to the ENI  Returned: always  Sample: `{}` |
| **vpc_id**  string | ID of the VPC the network interface it part of  Returned: always  Sample: `"vpc-b3f1f123"` |

### Authors

- Rob White (@wimnat)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
