---
collection: ansible
version: "6"
title: "amazon.aws.ec2_vpc_net module – Configure AWS virtual private clouds"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_vpc_net_module.html
fetched_at: 2026-07-27T16:43:52+00:00
---
# amazon.aws.ec2_vpc_net module – Configure AWS virtual private clouds

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
> see [Requirements](ec2_vpc_net_module.md#ansible-collections-amazon-aws-ec2-vpc-net-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vpc_net`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vpc_net_module.md#synopsis)
- [Requirements](ec2_vpc_net_module.md#requirements)
- [Parameters](ec2_vpc_net_module.md#parameters)
- [Notes](ec2_vpc_net_module.md#notes)
- [Examples](ec2_vpc_net_module.md#examples)
- [Return Values](ec2_vpc_net_module.md#return-values)

## [Synopsis](ec2_vpc_net_module.md#id1)

- Create, modify, and terminate AWS virtual private clouds.

## [Requirements](ec2_vpc_net_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_net_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **cidr_block**  list / elements=string / required | The primary CIDR of the VPC. After 2.5 a list of CIDRs can be provided. The first in the list will be used as the primary CIDR and is used in conjunction with the `name` to ensure idempotence. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **dhcp_opts_id**  string | The id of the DHCP options to use for this VPC. |
| **dns_hostnames**  boolean | Whether to enable AWS hostname support.  Choices:   - `false` - `true` ← (default) |
| **dns_support**  boolean | Whether to enable AWS DNS support.  Choices:   - `false` - `true` ← (default) |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **ipv6_cidr**  boolean | Request an Amazon-provided IPv6 CIDR block with /56 prefix length. You cannot specify the range of IPv6 addresses, or the size of the CIDR block.  Default value is `false` when creating a new VPC.  Choices:   - `false` - `true` |
| **multi_ok**  boolean | By default the module will not create another VPC if there is another VPC with the same name and CIDR block. Specify this as true if you want duplicate VPCs created.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | The name to give your VPC. This is used in combination with `cidr_block` to determine if a VPC already exists. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_cidrs**  boolean | Remove CIDRs that are associated with the VPC and are not specified in `cidr_block`.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | The state of the VPC. Either absent or present.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | The tags you want attached to the VPC. This is independent of the name value, note if you pass a ‘Name’ key it would override the Name of the VPC if it’s different. |
| **tenancy**  string | Whether to be default or dedicated tenancy. This cannot be changed after the VPC has been created.  Choices:   - `"default"` ← (default) - `"dedicated"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_vpc_net_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vpc_net_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: create a VPC with dedicated tenancy and a couple of tags
  amazon.aws.ec2_vpc_net:
    name: Module_dev2
    cidr_block: 10.10.0.0/16
    region: us-east-1
    tags:
      module: ec2_vpc_net
      this: works
    tenancy: dedicated

- name: create a VPC with dedicated tenancy and request an IPv6 CIDR
  amazon.aws.ec2_vpc_net:
    name: Module_dev2
    cidr_block: 10.10.0.0/16
    ipv6_cidr: True
    region: us-east-1
    tenancy: dedicated
```

## [Return Values](ec2_vpc_net_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vpc**  complex | info about the VPC that was created or deleted  Returned: always |
| **cidr_block**  string | The CIDR of the VPC  Returned: always  Sample: `"10.0.0.0/16"` |
| **cidr_block_association_set**  list / elements=string | IPv4 CIDR blocks associated with the VPC  Returned: success  Sample: `{"cidr_block_association_set": [{"association_id": "vpc-cidr-assoc-97aeeefd", "cidr_block": "10.0.0.0/24", "cidr_block_state": {"state": "associated"}}]}` |
| **classic_link_enabled**  boolean | indicates whether ClassicLink is enabled  Returned: always  Sample: `false` |
| **dhcp_options_id**  string | the id of the DHCP options associated with this VPC  Returned: always  Sample: `"dopt-12345678"` |
| **id**  string | VPC resource id  Returned: always  Sample: `"vpc-12345678"` |
| **instance_tenancy**  string | indicates whether VPC uses default or dedicated tenancy  Returned: always  Sample: `"default"` |
| **ipv6_cidr_block_association_set**  list / elements=string | IPv6 CIDR blocks associated with the VPC  Returned: success  Sample: `{"ipv6_cidr_block_association_set": [{"association_id": "vpc-cidr-assoc-97aeeefd", "ipv6_cidr_block": "2001:db8::/56", "ipv6_cidr_block_state": {"state": "associated"}}]}` |
| **is_default**  boolean | indicates whether this is the default VPC  Returned: always  Sample: `false` |
| **owner_id**  string | The AWS account which owns the VPC.  Returned: always  Sample: `"123456789012"` |
| **state**  string | state of the VPC  Returned: always  Sample: `"available"` |
| **tags**  complex | tags attached to the VPC, includes name  Returned: always |
| **Name**  string | name tag for the VPC  Returned: always  Sample: `"pk_vpc4"` |

### Authors

- Jonathan Davila (@defionscode)
- Sloane Hertel (@s-hertel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
