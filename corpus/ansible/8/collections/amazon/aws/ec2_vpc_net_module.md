---
collection: ansible
version: "8"
title: "amazon.aws.ec2_vpc_net module – Configure AWS Virtual Private Clouds"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_vpc_net_module.html
fetched_at: 2026-07-28T01:06:43+00:00
---
# amazon.aws.ec2_vpc_net module – Configure AWS Virtual Private Clouds

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

- Create, modify, and terminate AWS Virtual Private Clouds (VPCs).

## [Requirements](ec2_vpc_net_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_net_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cidr_block**  list / elements=string | The primary CIDR of the VPC.  The first in the list will be used as the primary CIDR and is used in conjunction with *name* to ensure idempotence.  Required when *vpc_id* is not set. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **dhcp_opts_id**  string | The id of the DHCP options to use for this VPC. |
| **dns_hostnames**  boolean | Whether to enable AWS hostname support.  Default value is `true` when creating a new VPC.  **Choices:**   - `false` - `true` |
| **dns_support**  boolean | Whether to enable AWS DNS support.  Default value is `true` when creating a new VPC.  **Choices:**   - `false` - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **ipv6_cidr**  boolean | Request an Amazon-provided IPv6 CIDR block with /56 prefix length. You cannot specify the range of IPv6 addresses, or the size of the CIDR block.  Default value is `false` when creating a new VPC.  **Choices:**   - `false` - `true` |
| **multi_ok**  boolean | By default the module will not create another VPC if there is another VPC with the same name and CIDR block. Specify *multi_ok=true* if you want duplicate VPCs created.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The name to give your VPC. This is used in combination with *cidr_block* to determine if a VPC already exists.  The value of *name* overrides any value set for `Name` in the *tags* parameter.  At least one of *name* and *vpc_id* must be specified.  *name* must be specified when creating a new VPC. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_cidrs**  boolean | Remove CIDRs that are associated with the VPC and are not specified in *cidr_block*.  **Choices:**   - `false` ← (default) - `true` |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | The state of the VPC. Either absent or present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **tenancy**  string | Whether to be default or dedicated tenancy.  This cannot be changed after the VPC has been created.  **Choices:**   - `"default"` ← (default) - `"dedicated"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string  *added in amazon.aws 4.0.0* | The ID of the VPC.  At least one of *name* and *vpc_id* must be specified.  At least one of *name* and *cidr_block* must be specified. |

## [Notes](ec2_vpc_net_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
| **vpc**  complex | info about the VPC that was created or deleted  **Returned:** always |
| **cidr_block**  string | The CIDR of the VPC  **Returned:** always  **Sample:** `"10.0.0.0/16"` |
| **cidr_block_association_set**  list / elements=string | IPv4 CIDR blocks associated with the VPC  **Returned:** success  **Sample:** `{"cidr_block_association_set": [{"association_id": "vpc-cidr-assoc-97aeeefd", "cidr_block": "10.0.0.0/24", "cidr_block_state": {"state": "associated"}}]}` |
| **dhcp_options_id**  string | the id of the DHCP options associated with this VPC  **Returned:** always  **Sample:** `"dopt-12345678"` |
| **id**  string | VPC resource id  **Returned:** always  **Sample:** `"vpc-12345678"` |
| **instance_tenancy**  string | indicates whether VPC uses default or dedicated tenancy  **Returned:** always  **Sample:** `"default"` |
| **ipv6_cidr_block_association_set**  list / elements=string | IPv6 CIDR blocks associated with the VPC  **Returned:** success  **Sample:** `{"ipv6_cidr_block_association_set": [{"association_id": "vpc-cidr-assoc-97aeeefd", "ipv6_cidr_block": "2001:db8::/56", "ipv6_cidr_block_state": {"state": "associated"}}]}` |
| **is_default**  boolean | indicates whether this is the default VPC  **Returned:** always  **Sample:** `false` |
| **name**  string  *added in amazon.aws 4.0.0* | The Name tag of the VPC.  **Returned:** When the Name tag has been set on the VPC  **Sample:** `"MyVPC"` |
| **owner_id**  string | The AWS account which owns the VPC.  **Returned:** always  **Sample:** `"123456789012"` |
| **state**  string | state of the VPC  **Returned:** always  **Sample:** `"available"` |
| **tags**  complex | tags attached to the VPC, includes name  **Returned:** always |
| **Name**  string | name tag for the VPC  **Returned:** always  **Sample:** `"pk_vpc4"` |

### Authors

- Jonathan Davila (@defionscode)
- Sloane Hertel (@s-hertel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
