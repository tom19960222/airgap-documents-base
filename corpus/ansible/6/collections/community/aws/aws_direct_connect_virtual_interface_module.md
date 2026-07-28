---
collection: ansible
version: "6"
title: "community.aws.aws_direct_connect_virtual_interface module – Manage Direct Connect virtual interfaces"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/aws_direct_connect_virtual_interface_module.html
fetched_at: 2026-07-27T17:03:24+00:00
---
# community.aws.aws_direct_connect_virtual_interface module – Manage Direct Connect virtual interfaces

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
> see [Requirements](aws_direct_connect_virtual_interface_module.md#ansible-collections-community-aws-aws-direct-connect-virtual-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.aws_direct_connect_virtual_interface`.

New in community.aws 1.0.0

- [Synopsis](aws_direct_connect_virtual_interface_module.md#synopsis)
- [Requirements](aws_direct_connect_virtual_interface_module.md#requirements)
- [Parameters](aws_direct_connect_virtual_interface_module.md#parameters)
- [Notes](aws_direct_connect_virtual_interface_module.md#notes)
- [Examples](aws_direct_connect_virtual_interface_module.md#examples)
- [Return Values](aws_direct_connect_virtual_interface_module.md#return-values)

## [Synopsis](aws_direct_connect_virtual_interface_module.md#id1)

- Create, delete, or modify a Direct Connect public or private virtual interface.

## [Requirements](aws_direct_connect_virtual_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](aws_direct_connect_virtual_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address_type**  string | The type of IP address for the BGP peer. |
| **amazon_address**  string | The amazon address CIDR with which to create the virtual interface. |
| **authentication_key**  string | The authentication key for BGP configuration. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **bgp_asn**  integer | The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.  Default: `65000` |
| **cidr**  list / elements=string | A list of route filter prefix CIDRs with which to create the public virtual interface. |
| **customer_address**  string | The customer address CIDR with which to create the virtual interface. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **direct_connect_gateway_id**  string | The direct connect gateway ID for creating a private virtual interface.  To create a private virtual interface *virtual_gateway_id* or *direct_connect_gateway_id* is required. These options are mutually exclusive. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **id_to_associate**  aliases: link_aggregation_group_id, connection_id  string / required | The ID of the link aggregation group or connection to associate with the virtual interface. |
| **name**  string | The name of the virtual interface. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **public**  boolean | The type of virtual interface.  Choices:   - `false` - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | The desired state of the Direct Connect virtual interface.  Choices:   - `"present"` - `"absent"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **virtual_gateway_id**  string | The virtual gateway ID required for creating a private virtual interface.  To create a private virtual interface *virtual_gateway_id* or *direct_connect_gateway_id* is required. These options are mutually exclusive. |
| **virtual_interface_id**  string | The virtual interface ID. |
| **vlan**  integer | The VLAN ID.  Default: `100` |

## [Notes](aws_direct_connect_virtual_interface_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](aws_direct_connect_virtual_interface_module.md#id5)

```yaml+jinja
---
- name: create an association between a LAG and connection
  community.aws.aws_direct_connect_virtual_interface:
    state: present
    name: "{{ name }}"
    link_aggregation_group_id: LAG-XXXXXXXX
    connection_id: dxcon-XXXXXXXX

- name: remove an association between a connection and virtual interface
  community.aws.aws_direct_connect_virtual_interface:
    state: absent
    connection_id: dxcon-XXXXXXXX
    virtual_interface_id: dxv-XXXXXXXX
```

## [Return Values](aws_direct_connect_virtual_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **address_family**  string | The address family for the BGP peer.  Returned: always  Sample: `"ipv4"` |
| **amazon_address**  string | IP address assigned to the Amazon interface.  Returned: always  Sample: `"169.254.255.1/30"` |
| **asn**  integer | The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.  Returned: always  Sample: `65000` |
| **auth_key**  string | The authentication key for BGP configuration.  Returned: always  Sample: `"0xZ59Y1JZ2oDOSh6YriIlyRE"` |
| **bgp_peers**  complex | A list of the BGP peers configured on this virtual interface.  Returned: always |
| **address_family**  string | The address family for the BGP peer.  Returned: always  Sample: `"ipv4"` |
| **amazon_address**  string | IP address assigned to the Amazon interface.  Returned: always  Sample: `"169.254.255.1/30"` |
| **asn**  integer | The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.  Returned: always  Sample: `65000` |
| **auth_key**  string | The authentication key for BGP configuration.  Returned: always  Sample: `"0xZ59Y1JZ2oDOSh6YriIlyRE"` |
| **bgp_peer_state**  string | The state of the BGP peer (verifying, pending, available)  Returned: always  Sample: `"available"` |
| **bgp_status**  string | The up/down state of the BGP peer.  Returned: always  Sample: `"up"` |
| **customer_address**  string | IP address assigned to the customer interface.  Returned: always  Sample: `"169.254.255.2/30"` |
| **changed**  boolean | Indicated if the virtual interface has been created/modified/deleted  Returned: always  Sample: `false` |
| **connection_id**  string | The ID of the connection. This field is also used as the ID type for operations that use multiple connection types (LAG, interconnect, and/or connection).  Returned: always  Sample: `"dxcon-fgb175av"` |
| **customer_address**  string | IP address assigned to the customer interface.  Returned: always  Sample: `"169.254.255.2/30"` |
| **customer_router_config**  string | Information for generating the customer router configuration.  Returned: always |
| **direct_connect_gateway_id**  string | The ID of the Direct Connect gateway. This only applies to private virtual interfaces.  Returned: when *public=False*  Sample: `"f7593767-eded-44e8-926d-a2234175835d"` |
| **location**  string | Where the connection is located.  Returned: always  Sample: `"EqDC2"` |
| **owner_account**  string | The AWS account that will own the new virtual interface.  Returned: always  Sample: `"123456789012"` |
| **route_filter_prefixes**  complex | A list of routes to be advertised to the AWS network in this region (public virtual interface).  Returned: always |
| **cidr**  string | A routes to be advertised to the AWS network in this region.  Returned: always  Sample: `"54.227.92.216/30"` |
| **virtual_gateway_id**  string | The ID of the virtual private gateway to a VPC. This only applies to private virtual interfaces.  Returned: when *public=False*  Sample: `"vgw-f3ce259a"` |
| **virtual_interface_id**  string | The ID of the virtual interface.  Returned: always  Sample: `"dxvif-fh0w7cex"` |
| **virtual_interface_name**  string | The name of the virtual interface assigned by the customer.  Returned: always  Sample: `"test_virtual_interface"` |
| **virtual_interface_state**  string | State of the virtual interface (confirming, verifying, pending, available, down, rejected).  Returned: always  Sample: `"available"` |
| **virtual_interface_type**  string | The type of virtual interface (private, public).  Returned: always  Sample: `"private"` |
| **vlan**  integer | The VLAN ID.  Returned: always  Sample: `100` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
