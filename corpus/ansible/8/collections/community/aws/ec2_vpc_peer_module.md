---
collection: ansible
version: "8"
title: "community.aws.ec2_vpc_peer module – create, delete, accept, and reject VPC peering connections between two VPCs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ec2_vpc_peer_module.html
fetched_at: 2026-07-28T01:40:49+00:00
---
# community.aws.ec2_vpc_peer module – create, delete, accept, and reject VPC peering connections between two VPCs.

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
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_peer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **peer_owner_id**  string | The AWS account number for cross account peering. |
| **peer_region**  string | Region of the accepting VPC. |
| **peer_vpc_id**  string | VPC id of the accepting VPC. |
| **peering_id**  string | Peering connection id. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create, delete, accept, reject a peering connection.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"accept"` - `"reject"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string | VPC id of the requesting VPC. |
| **wait**  boolean | Wait for peering state changes to complete.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ec2_vpc_peer_module.md#id4)

> **Note:**
>
> - Support for *purge_tags* was added in release 2.0.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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
    peer_owner_id: 123456789012
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
    peer_owner_id: 123456789012
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
    peer_owner_id: 123456789012
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
| **peering_id**  string | The id of the VPC peering connection created/deleted.  **Returned:** always  **Sample:** `"pcx-034223d7c0aec3cde"` |
| **vpc_peering_connection**  complex | The details of the VPC peering connection as returned by Boto3 (snake cased).  **Returned:** success |
| **accepter_vpc_info**  complex | Information about the VPC which accepted the connection.  **Returned:** success |
| **cidr_block**  string | The primary CIDR for the VPC.  **Returned:** when connection is in the accepted state.  **Sample:** `"10.10.10.0/23"` |
| **cidr_block_set**  complex | A list of all CIDRs for the VPC.  **Returned:** when connection is in the accepted state. |
| **cidr_block**  string | A CIDR block used by the VPC.  **Returned:** success  **Sample:** `"10.10.10.0/23"` |
| **owner_id**  string | The AWS account that owns the VPC.  **Returned:** success  **Sample:** `"123456789012"` |
| **peering_options**  dictionary | Additional peering configuration.  **Returned:** when connection is in the accepted state. |
| **allow_dns_resolution_from_remote_vpc**  boolean | Indicates whether a VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.  **Returned:** success |
| **allow_egress_from_local_classic_link_to_remote_vpc**  boolean | Indicates whether a local ClassicLink connection can communicate with the peer VPC over the VPC peering connection.  **Returned:** success |
| **allow_egress_from_local_vpc_to_remote_classic_link**  boolean | Indicates whether a local VPC can communicate with a ClassicLink connection in the peer VPC over the VPC peering connection.  **Returned:** success |
| **region**  string | The AWS region that the VPC is in.  **Returned:** success  **Sample:** `"us-east-1"` |
| **vpc_id**  string | The ID of the VPC  **Returned:** success  **Sample:** `"vpc-0123456789abcdef0"` |
| **requester_vpc_info**  complex | Information about the VPC which requested the connection.  **Returned:** success |
| **cidr_block**  string | The primary CIDR for the VPC.  **Returned:** when connection is not in the deleted state.  **Sample:** `"10.10.10.0/23"` |
| **cidr_block_set**  complex | A list of all CIDRs for the VPC.  **Returned:** when connection is not in the deleted state. |
| **cidr_block**  string | A CIDR block used by the VPC  **Returned:** success  **Sample:** `"10.10.10.0/23"` |
| **owner_id**  string | The AWS account that owns the VPC.  **Returned:** success  **Sample:** `"123456789012"` |
| **peering_options**  dictionary | Additional peering configuration.  **Returned:** when connection is not in the deleted state. |
| **allow_dns_resolution_from_remote_vpc**  boolean | Indicates whether a VPC can resolve public DNS hostnames to private IP addresses when queried from instances in a peer VPC.  **Returned:** success |
| **allow_egress_from_local_classic_link_to_remote_vpc**  boolean | Indicates whether a local ClassicLink connection can communicate with the peer VPC over the VPC peering connection.  **Returned:** success |
| **allow_egress_from_local_vpc_to_remote_classic_link**  boolean | Indicates whether a local VPC can communicate with a ClassicLink connection in the peer VPC over the VPC peering connection.  **Returned:** success |
| **region**  string | The AWS region that the VPC is in.  **Returned:** success  **Sample:** `"us-east-1"` |
| **vpc_id**  string | The ID of the VPC  **Returned:** success  **Sample:** `"vpc-0123456789abcdef0"` |
| **status**  complex | Details of the current status of the connection.  **Returned:** success |
| **code**  string | A short code describing the status of the connection.  **Returned:** success  **Sample:** `"active"` |
| **message**  string | Additional information about the status of the connection.  **Returned:** success  **Sample:** `"Pending Acceptance by 123456789012"` |
| **tags**  dictionary | Tags applied to the connection.  **Returned:** success |
| **vpc_peering_connection_id**  string | The ID of the VPC peering connection.  **Returned:** success  **Sample:** `"pcx-0123456789abcdef0"` |

### Authors

- Mike Mochan (@mmochan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
