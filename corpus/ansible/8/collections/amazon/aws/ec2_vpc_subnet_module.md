---
collection: ansible
version: "8"
title: "amazon.aws.ec2_vpc_subnet module – Manage subnets in AWS virtual private clouds"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_vpc_subnet_module.html
fetched_at: 2026-07-28T01:06:46+00:00
---
# amazon.aws.ec2_vpc_subnet module – Manage subnets in AWS virtual private clouds

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **assign_instances_ipv6**  boolean | Whether instances launched into the subnet should default to being automatically assigned an IPv6 address.  If *assign_instances_ipv6=true*, *ipv6_cidr* must also be specified.  **Choices:**   - `false` ← (default) - `true` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **az**  string | The availability zone for the subnet.  Required if *outpost_arn* is set. |
| **cidr**  string / required | The CIDR block for the subnet. E.g. `192.0.2.0/24`. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **ipv6_cidr**  string | The IPv6 CIDR block for the subnet.  The VPC must have a /56 block assigned and this value must be a valid IPv6 /64 that falls in the VPC range.  Required if *assign_instances_ipv6=true*  **Default:** `""` |
| **map_public**  boolean | Whether instances launched into the subnet should default to being assigned public IP address.  **Choices:**   - `false` ← (default) - `true` |
| **outpost_arn**  string | The Amazon Resource Name (ARN) of the Outpost.  If set, allows to create subnet in an Outpost.  If *outpost_arn* is set, *az* must also be specified.  **Default:** `""` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or remove the subnet.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified.  **Default:** `{}` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string / required | -“VPC ID of the VPC in which to create or delete the subnet. |
| **wait**  boolean | Whether to wait for changes to complete.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | Number of seconds to wait for changes to complete  Ignored unless *wait=True*.  **Default:** `300` |

## [Notes](ec2_vpc_subnet_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
| **subnet**  complex | Dictionary of subnet values  **Returned:** *state=present* |
| **assign_ipv6_address_on_creation**  boolean | whether IPv6 address is auto-assigned to new instances  **Returned:** *state=present*  **Sample:** `false` |
| **availability_zone**  string | Availability zone of the Subnet  **Returned:** *state=present*  **Sample:** `"us-east-1a"` |
| **available_ip_address_count**  string | number of available IPv4 addresses  **Returned:** *state=present*  **Sample:** `"251"` |
| **cidr_block**  string | The IPv4 CIDR of the Subnet  **Returned:** *state=present*  **Sample:** `"10.0.0.0/16"` |
| **default_for_az**  boolean | indicates whether this is the default Subnet for this Availability Zone  **Returned:** *state=present*  **Sample:** `false` |
| **id**  string | Subnet resource id  **Returned:** *state=present*  **Sample:** `"subnet-b883b2c4"` |
| **ipv6_association_id**  string | The IPv6 association ID for the currently associated CIDR  **Returned:** *state=present*  **Sample:** `"subnet-cidr-assoc-b85c74d2"` |
| **ipv6_cidr_block**  string | The IPv6 CIDR block actively associated with the Subnet  **Returned:** *state=present*  **Sample:** `"2001:db8:0:102::/64"` |
| **ipv6_cidr_block_association_set**  complex | An array of IPv6 cidr block association set information.  **Returned:** *state=present* |
| **association_id**  string | The association ID  **Returned:** always |
| **ipv6_cidr_block**  string | The IPv6 CIDR block that is associated with the subnet.  **Returned:** always |
| **ipv6_cidr_block_state**  dictionary | A hash/dict that contains a single item. The state of the cidr block association.  **Returned:** always |
| **state**  string | The CIDR block association state.  **Returned:** always |
| **map_public_ip_on_launch**  boolean | whether public IP is auto-assigned to new instances  **Returned:** *state=present*  **Sample:** `false` |
| **state**  string | state of the Subnet  **Returned:** *state=present*  **Sample:** `"available"` |
| **tags**  dictionary | tags attached to the Subnet, includes name  **Returned:** *state=present*  **Sample:** `{"Name": "My Subnet", "env": "staging"}` |
| **vpc_id**  string | the id of the VPC where this Subnet exists  **Returned:** *state=present*  **Sample:** `"vpc-67236184"` |

### Authors

- Robert Estelle (@erydo)
- Brad Davidson (@brandond)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
