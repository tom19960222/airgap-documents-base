---
collection: ansible
version: "8"
title: "community.aws.directconnect_virtual_interface module – Manage Direct Connect virtual interfaces"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/directconnect_virtual_interface_module.html
fetched_at: 2026-07-28T01:40:34+00:00
---
# community.aws.directconnect_virtual_interface module – Manage Direct Connect virtual interfaces

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
> see [Requirements](directconnect_virtual_interface_module.md#ansible-collections-community-aws-directconnect-virtual-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.directconnect_virtual_interface`.

New in community.aws 1.0.0

- [Synopsis](directconnect_virtual_interface_module.md#synopsis)
- [Requirements](directconnect_virtual_interface_module.md#requirements)
- [Parameters](directconnect_virtual_interface_module.md#parameters)
- [Notes](directconnect_virtual_interface_module.md#notes)
- [Examples](directconnect_virtual_interface_module.md#examples)
- [Return Values](directconnect_virtual_interface_module.md#return-values)

## [Synopsis](directconnect_virtual_interface_module.md#id1)

- Create, delete, or modify a Direct Connect public or private virtual interface.
- Prior to release 5.0.0 this module was called `community.aws.aws_direct_connect_virtual_interface`. The usage did not change.

Aliases: aws_direct_connect_virtual_interface

## [Requirements](directconnect_virtual_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](directconnect_virtual_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **address_type**  string | The type of IP address for the BGP peer. |
| **amazon_address**  string | The amazon address CIDR with which to create the virtual interface. |
| **authentication_key**  string | The authentication key for BGP configuration. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **bgp_asn**  integer | The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.  **Default:** `65000` |
| **cidr**  list / elements=string | A list of route filter prefix CIDRs with which to create the public virtual interface. |
| **customer_address**  string | The customer address CIDR with which to create the virtual interface. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **direct_connect_gateway_id**  string | The direct connect gateway ID for creating a private virtual interface.  To create a private virtual interface *virtual_gateway_id* or *direct_connect_gateway_id* is required. These options are mutually exclusive. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **id_to_associate**  aliases: link_aggregation_group_id, connection_id  string / required | The ID of the link aggregation group or connection to associate with the virtual interface. |
| **name**  string | The name of the virtual interface. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **public**  boolean | The type of virtual interface.  **Choices:**   - `false` - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | The desired state of the Direct Connect virtual interface.  **Choices:**   - `"present"` - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **virtual_gateway_id**  string | The virtual gateway ID required for creating a private virtual interface.  To create a private virtual interface *virtual_gateway_id* or *direct_connect_gateway_id* is required. These options are mutually exclusive. |
| **virtual_interface_id**  string | The virtual interface ID. |
| **vlan**  integer | The VLAN ID.  **Default:** `100` |

## [Notes](directconnect_virtual_interface_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](directconnect_virtual_interface_module.md#id5)

```yaml+jinja
---
- name: create an association between a LAG and connection
  community.aws.directconnect_virtual_interface:
    state: present
    name: "{{ name }}"
    link_aggregation_group_id: LAG-XXXXXXXX
    connection_id: dxcon-XXXXXXXX

- name: remove an association between a connection and virtual interface
  community.aws.directconnect_virtual_interface:
    state: absent
    connection_id: dxcon-XXXXXXXX
    virtual_interface_id: dxv-XXXXXXXX
```

## [Return Values](directconnect_virtual_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address_family**  string | The address family for the BGP peer.  **Returned:** always  **Sample:** `"ipv4"` |
| **amazon_address**  string | IP address assigned to the Amazon interface.  **Returned:** always  **Sample:** `"169.254.255.1/30"` |
| **asn**  integer | The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.  **Returned:** always  **Sample:** `65000` |
| **auth_key**  string | The authentication key for BGP configuration.  **Returned:** always  **Sample:** `"0xZ59Y1JZ2oDOSh6YriIlyRE"` |
| **bgp_peers**  complex | A list of the BGP peers configured on this virtual interface.  **Returned:** always |
| **address_family**  string | The address family for the BGP peer.  **Returned:** always  **Sample:** `"ipv4"` |
| **amazon_address**  string | IP address assigned to the Amazon interface.  **Returned:** always  **Sample:** `"169.254.255.1/30"` |
| **asn**  integer | The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.  **Returned:** always  **Sample:** `65000` |
| **auth_key**  string | The authentication key for BGP configuration.  **Returned:** always  **Sample:** `"0xZ59Y1JZ2oDOSh6YriIlyRE"` |
| **bgp_peer_state**  string | The state of the BGP peer (verifying, pending, available)  **Returned:** always  **Sample:** `"available"` |
| **bgp_status**  string | The up/down state of the BGP peer.  **Returned:** always  **Sample:** `"up"` |
| **customer_address**  string | IP address assigned to the customer interface.  **Returned:** always  **Sample:** `"169.254.255.2/30"` |
| **changed**  boolean | Indicated if the virtual interface has been created/modified/deleted  **Returned:** always  **Sample:** `false` |
| **connection_id**  string | The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).  **Returned:** always  **Sample:** `"dxcon-fgb175av"` |
| **customer_address**  string | IP address assigned to the customer interface.  **Returned:** always  **Sample:** `"169.254.255.2/30"` |
| **customer_router_config**  string | Information for generating the customer router configuration.  **Returned:** always |
| **direct_connect_gateway_id**  string | The ID of the Direct Connect gateway. This only applies to private virtual interfaces.  **Returned:** when *public=False*  **Sample:** `"f7593767-eded-44e8-926d-a2234175835d"` |
| **location**  string | Where the connection is located.  **Returned:** always  **Sample:** `"EqDC2"` |
| **owner_account**  string | The AWS account that will own the new virtual interface.  **Returned:** always  **Sample:** `"123456789012"` |
| **route_filter_prefixes**  complex | A list of routes to be advertised to the AWS network in this region (public virtual interface).  **Returned:** always |
| **cidr**  string | A routes to be advertised to the AWS network in this region.  **Returned:** always  **Sample:** `"54.227.92.216/30"` |
| **virtual_gateway_id**  string | The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.  **Returned:** when *public=False*  **Sample:** `"vgw-f3ce259a"` |
| **virtual_interface_id**  string | The ID of the virtual interface.  **Returned:** always  **Sample:** `"dxvif-fh0w7cex"` |
| **virtual_interface_name**  string | The name of the virtual interface assigned by the customer.  **Returned:** always  **Sample:** `"test_virtual_interface"` |
| **virtual_interface_state**  string | State of the virtual interface (confirming, verifying, pending, available, down, rejected).  **Returned:** always  **Sample:** `"available"` |
| **virtual_interface_type**  string | The type of virtual interface (private, public).  **Returned:** always  **Sample:** `"private"` |
| **vlan**  integer | The VLAN ID.  **Returned:** always  **Sample:** `100` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
