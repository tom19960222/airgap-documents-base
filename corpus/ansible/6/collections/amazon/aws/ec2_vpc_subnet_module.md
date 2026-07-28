---
collection: ansible
version: "6"
title: "amazon.aws.ec2_vpc_subnet module – Manage subnets in AWS virtual private clouds"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_vpc_subnet_module.html
fetched_at: 2026-07-27T16:43:53+00:00
---
# amazon.aws.ec2_vpc_subnet module – Manage subnets in AWS virtual private clouds

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
> see [Requirements](ec2_vpc_subnet_module.md#ansible-collections-amazon-aws-ec2-vpc-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vpc_subnet`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vpc_subnet_module.md#synopsis)
- [Requirements](ec2_vpc_subnet_module.md#requirements)
- [Parameters](ec2_vpc_subnet_module.md#parameters)
- [Notes](ec2_vpc_subnet_module.md#notes)
- [Examples](ec2_vpc_subnet_module.md#examples)
- [Return Values](ec2_vpc_subnet_module.md#return-values)

## [Synopsis](ec2_vpc_subnet_module.md#id1)

- Manage subnets in AWS virtual private clouds.

## [Requirements](ec2_vpc_subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **assign_instances_ipv6**  boolean | Specify `yes` to indicate that instances launched into the subnet should be automatically assigned an IPv6 address.  Choices:   - `false` ← (default) - `true` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **az**  string | The availability zone for the subnet. |
| **cidr**  string / required | The CIDR block for the subnet. E.g. 192.0.2.0/24. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **ipv6_cidr**  string | The IPv6 CIDR block for the subnet. The VPC must have a /56 block assigned and this value must be a valid IPv6 /64 that falls in the VPC range.  Required if *assign_instances_ipv6=true* |
| **map_public**  boolean | Specify `yes` to indicate that instances launched into the subnet should be assigned public IP address by default.  Choices:   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | Whether or not to remove tags that do not appear in the *tags* list.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or remove the subnet.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dict of tags to apply to the subnet. Any tags currently applied to the subnet and not present here will be removed. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_id**  string / required | VPC ID of the VPC in which to create or delete the subnet. |
| **wait**  boolean | When *wait=true* and *state=present*, module will wait for subnet to be in available state before continuing.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | Number of seconds to wait for subnet to become available *wait=True*.  Default: `300` |

## [Notes](ec2_vpc_subnet_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vpc_subnet_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Create subnet for database servers
  amazon.aws.ec2_vpc_subnet:
    state: present
    vpc_id: vpc-123456
    cidr: 10.0.1.16/28
    tags:
      Name: Database Subnet
  register: database_subnet

- name: Remove subnet for database servers
  amazon.aws.ec2_vpc_subnet:
    state: absent
    vpc_id: vpc-123456
    cidr: 10.0.1.16/28

- name: Create subnet with IPv6 block assigned
  amazon.aws.ec2_vpc_subnet:
    state: present
    vpc_id: vpc-123456
    cidr: 10.1.100.0/24
    ipv6_cidr: 2001:db8:0:102::/64

- name: Remove IPv6 block assigned to subnet
  amazon.aws.ec2_vpc_subnet:
    state: present
    vpc_id: vpc-123456
    cidr: 10.1.100.0/24
    ipv6_cidr: ''
```

## [Return Values](ec2_vpc_subnet_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **subnet**  complex | Dictionary of subnet values  Returned: *state=present* |
| **assign_ipv6_address_on_creation**  boolean | whether IPv6 address is auto-assigned to new instances  Returned: *state=present*  Sample: `false` |
| **availability_zone**  string | Availability zone of the Subnet  Returned: *state=present*  Sample: `"us-east-1a"` |
| **available_ip_address_count**  string | number of available IPv4 addresses  Returned: *state=present*  Sample: `"251"` |
| **cidr_block**  string | The IPv4 CIDR of the Subnet  Returned: *state=present*  Sample: `"10.0.0.0/16"` |
| **default_for_az**  boolean | indicates whether this is the default Subnet for this Availability Zone  Returned: *state=present*  Sample: `false` |
| **id**  string | Subnet resource id  Returned: *state=present*  Sample: `"subnet-b883b2c4"` |
| **ipv6_association_id**  string | The IPv6 association ID for the currently associated CIDR  Returned: *state=present*  Sample: `"subnet-cidr-assoc-b85c74d2"` |
| **ipv6_cidr_block**  string | The IPv6 CIDR block actively associated with the Subnet  Returned: *state=present*  Sample: `"2001:db8:0:102::/64"` |
| **ipv6_cidr_block_association_set**  complex | An array of IPv6 cidr block association set information.  Returned: *state=present* |
| **association_id**  string | The association ID  Returned: always |
| **ipv6_cidr_block**  string | The IPv6 CIDR block that is associated with the subnet.  Returned: always |
| **ipv6_cidr_block_state**  dictionary | A hash/dict that contains a single item. The state of the cidr block association.  Returned: always |
| **state**  string | The CIDR block association state.  Returned: always |
| **map_public_ip_on_launch**  boolean | whether public IP is auto-assigned to new instances  Returned: *state=present*  Sample: `false` |
| **state**  string | state of the Subnet  Returned: *state=present*  Sample: `"available"` |
| **tags**  dictionary | tags attached to the Subnet, includes name  Returned: *state=present*  Sample: `{"Name": "My Subnet", "env": "staging"}` |
| **vpc_id**  string | the id of the VPC where this Subnet exists  Returned: *state=present*  Sample: `"vpc-67236184"` |

### Authors

- Robert Estelle (@erydo)
- Brad Davidson (@brandond)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
