---
collection: ansible
version: "6"
title: "community.aws.ec2_vpc_peer module – create, delete, accept, and reject VPC peering connections between two VPCs."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/ec2_vpc_peer_module.html
fetched_at: 2026-07-27T17:04:10+00:00
---
# community.aws.ec2_vpc_peer module – create, delete, accept, and reject VPC peering connections between two VPCs.

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
> see [Requirements](ec2_vpc_peer_module.md#ansible-collections-community-aws-ec2-vpc-peer-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_vpc_peer`.

New in community.aws 1.0.0

- [Synopsis](ec2_vpc_peer_module.md#synopsis)
- [Requirements](ec2_vpc_peer_module.md#requirements)
- [Parameters](ec2_vpc_peer_module.md#parameters)
- [Notes](ec2_vpc_peer_module.md#notes)
- [Examples](ec2_vpc_peer_module.md#examples)
- [Return Values](ec2_vpc_peer_module.md#return-values)

## [Synopsis](ec2_vpc_peer_module.md#id1)

- Read the AWS documentation for VPC Peering Connections <https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpc-peering.html>.

## [Requirements](ec2_vpc_peer_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_peer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **peer_owner_id**  string | The AWS account number for cross account peering. |
| **peer_region**  string | Region of the accepting VPC. |
| **peer_vpc_id**  string | VPC id of the accepting VPC. |
| **peering_id**  string | Peering connection id. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in community.aws 2.0.0 | Remove tags not listed in *tags*.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create, delete, accept, reject a peering connection.  Choices:   - `"present"` ← (default) - `"absent"` - `"accept"` - `"reject"` |
| **tags**  dictionary | Dictionary of tags to look for and apply when creating a Peering Connection. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_id**  string | VPC id of the requesting VPC. |
| **wait**  boolean | Wait for peering state changes to complete.  Choices:   - `false` ← (default) - `true` |

## [Notes](ec2_vpc_peer_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vpc_peer_module.md#id5)

```yaml+jinja
# Complete example to create and accept a local peering connection.
- name: Create local account VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    vpc_id: vpc-12345678
    peer_vpc_id: vpc-87654321
    state: present
    tags:
      Name: Peering connection for VPC 21 to VPC 22
      CostCode: CC1234
      Project: phoenix
  register: vpc_peer

- name: Accept local VPC peering request
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    peering_id: "{{ vpc_peer.peering_id }}"
    state: accept
  register: action_peer

# Complete example to delete a local peering connection.
- name: Create local account VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    vpc_id: vpc-12345678
    peer_vpc_id: vpc-87654321
    state: present
    tags:
      Name: Peering connection for VPC 21 to VPC 22
      CostCode: CC1234
      Project: phoenix
  register: vpc_peer

- name: delete a local VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    peering_id: "{{ vpc_peer.peering_id }}"
    state: absent
  register: vpc_peer

  # Complete example to create and accept a cross account peering connection.
- name: Create cross account VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    vpc_id: vpc-12345678
    peer_vpc_id: vpc-12345678
    peer_owner_id: 123456789102
    state: present
    tags:
      Name: Peering connection for VPC 21 to VPC 22
      CostCode: CC1234
      Project: phoenix
  register: vpc_peer

- name: Accept peering connection from remote account
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    peering_id: "{{ vpc_peer.peering_id }}"
    profile: bot03_profile_for_cross_account
    state: accept
  register: vpc_peer

# Complete example to create and accept an intra-region peering connection.
- name: Create intra-region VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: us-east-1
    vpc_id: vpc-12345678
    peer_vpc_id: vpc-87654321
    peer_region: us-west-2
    state: present
    tags:
      Name: Peering connection for us-east-1 VPC to us-west-2 VPC
      CostCode: CC1234
      Project: phoenix
  register: vpc_peer

- name: Accept peering connection from peer region
  community.aws.ec2_vpc_peer:
    region: us-west-2
    peering_id: "{{ vpc_peer.peering_id }}"
    state: accept
  register: vpc_peer

# Complete example to create and reject a local peering connection.
- name: Create local account VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    vpc_id: vpc-12345678
    peer_vpc_id: vpc-87654321
    state: present
    tags:
      Name: Peering connection for VPC 21 to VPC 22
      CostCode: CC1234
      Project: phoenix
  register: vpc_peer

- name: Reject a local VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    peering_id: "{{ vpc_peer.peering_id }}"
    state: reject

# Complete example to create and accept a cross account peering connection.
- name: Create cross account VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    vpc_id: vpc-12345678
    peer_vpc_id: vpc-12345678
    peer_owner_id: 123456789102
    state: present
    tags:
      Name: Peering connection for VPC 21 to VPC 22
      CostCode: CC1234
      Project: phoenix
  register: vpc_peer

- name: Accept a cross account VPC peering connection request
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    peering_id: "{{ vpc_peer.peering_id }}"
    profile: bot03_profile_for_cross_account
    state: accept
    tags:
      Name: Peering connection for VPC 21 to VPC 22
      CostCode: CC1234
      Project: phoenix

# Complete example to create and reject a cross account peering connection.
- name: Create cross account VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    vpc_id: vpc-12345678
    peer_vpc_id: vpc-12345678
    peer_owner_id: 123456789102
    state: present
    tags:
      Name: Peering connection for VPC 21 to VPC 22
      CostCode: CC1234
      Project: phoenix
  register: vpc_peer

- name: Reject a cross account VPC peering Connection
  community.aws.ec2_vpc_peer:
    region: ap-southeast-2
    peering_id: "{{ vpc_peer.peering_id }}"
    profile: bot03_profile_for_cross_account
    state: reject
```

## [Return Values](ec2_vpc_peer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **peering_id**  string | The id of the VPC peering connection created/deleted.  Returned: always  Sample: `"pcx-034223d7c0aec3cde"` |
| **vpc_peering_connection**  complex | The details of the VPC peering connection as returned by Boto3 (snake cased).  Returned: success |
| **accepter_vpc_info**  complex | Information about the VPC which accepted the connection.  Returned: success |
| **cidr_block**  string | The primary CIDR for the VPC.  Returned: when connection is in the accepted state.  Sample: `"10.10.10.0/23"` |
| **cidr_block_set**  complex | A list of all CIDRs for the VPC.  Returned: when connection is in the accepted state. |
| **cidr_block**  string | A CIDR block used by the VPC.  Returned: success  Sample: `"10.10.10.0/23"` |
| **owner_id**  string | The AWS account that owns the VPC.  Returned: success  Sample: `"012345678901"` |
| **peering_options**  dictionary | Additional peering configuration.  Returned: when connection is in the accepted state. |
| **allow_dns_resolution_from_remote_vpc**  boolean | Indicates whether a VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.  Returned: success |
| **allow_egress_from_local_classic_link_to_remote_vpc**  boolean | Indicates whether a local ClassicLink connection can communicate with the peer VPC over the VPC peering connection.  Returned: success |
| **allow_egress_from_local_vpc_to_remote_classic_link**  boolean | Indicates whether a local VPC can communicate with a ClassicLink connection in the peer VPC over the VPC peering connection.  Returned: success |
| **region**  string | The AWS region that the VPC is in.  Returned: success  Sample: `"us-east-1"` |
| **vpc_id**  string | The ID of the VPC  Returned: success  Sample: `"vpc-0123456789abcdef0"` |
| **requester_vpc_info**  complex | Information about the VPC which requested the connection.  Returned: success |
| **cidr_block**  string | The primary CIDR for the VPC.  Returned: when connection is not in the deleted state.  Sample: `"10.10.10.0/23"` |
| **cidr_block_set**  complex | A list of all CIDRs for the VPC.  Returned: when connection is not in the deleted state. |
| **cidr_block**  string | A CIDR block used by the VPC  Returned: success  Sample: `"10.10.10.0/23"` |
| **owner_id**  string | The AWS account that owns the VPC.  Returned: success  Sample: `"012345678901"` |
| **peering_options**  dictionary | Additional peering configuration.  Returned: when connection is not in the deleted state. |
| **allow_dns_resolution_from_remote_vpc**  boolean | Indicates whether a VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.  Returned: success |
| **allow_egress_from_local_classic_link_to_remote_vpc**  boolean | Indicates whether a local ClassicLink connection can communicate with the peer VPC over the VPC peering connection.  Returned: success |
| **allow_egress_from_local_vpc_to_remote_classic_link**  boolean | Indicates whether a local VPC can communicate with a ClassicLink connection in the peer VPC over the VPC peering connection.  Returned: success |
| **region**  string | The AWS region that the VPC is in.  Returned: success  Sample: `"us-east-1"` |
| **vpc_id**  string | The ID of the VPC  Returned: success  Sample: `"vpc-0123456789abcdef0"` |
| **status**  complex | Details of the current status of the connection.  Returned: success |
| **code**  string | A short code describing the status of the connection.  Returned: success  Sample: `"active"` |
| **message**  string | Additional information about the status of the connection.  Returned: success  Sample: `"Pending Acceptance by 012345678901"` |
| **tags**  dictionary | Tags applied to the connection.  Returned: success |
| **vpc_peering_connection_id**  string | The ID of the VPC peering connection.  Returned: success  Sample: `"pcx-0123456789abcdef0"` |

### Authors

- Mike Mochan (@mmochan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
