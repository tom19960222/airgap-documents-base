---
collection: ansible
version: "6"
title: "amazon.aws.ec2_vpc_route_table module – Manage route tables for AWS virtual private clouds"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_vpc_route_table_module.html
fetched_at: 2026-07-27T16:43:53+00:00
---
# amazon.aws.ec2_vpc_route_table module – Manage route tables for AWS virtual private clouds

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
> see [Requirements](ec2_vpc_route_table_module.md#ansible-collections-amazon-aws-ec2-vpc-route-table-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vpc_route_table`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vpc_route_table_module.md#synopsis)
- [Requirements](ec2_vpc_route_table_module.md#requirements)
- [Parameters](ec2_vpc_route_table_module.md#parameters)
- [Notes](ec2_vpc_route_table_module.md#notes)
- [Examples](ec2_vpc_route_table_module.md#examples)
- [Return Values](ec2_vpc_route_table_module.md#return-values)

## [Synopsis](ec2_vpc_route_table_module.md#id1)

- Manage route tables for AWS virtual private clouds

## [Requirements](ec2_vpc_route_table_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vpc_route_table_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **gateway_id**  string  added in amazon.aws 3.2.0 | The ID of the gateway to associate with the route table.  If *gateway_id* is `'None'` or `''`, gateway will be disassociated with the route table. |
| **lookup**  string | Look up route table by either tags or by route table ID. Non-unique tag lookup will fail. If no tags are specified then no lookup for an existing route table is performed and a new route table will be created. To change tags of a route table you must look up by id.  Choices:   - `"tag"` ← (default) - `"id"` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **propagating_vgw_ids**  list / elements=string | Enable route propagation from virtual gateways specified by ID. |
| **purge_routes**  boolean | Purge existing routes that are not found in routes.  Choices:   - `false` - `true` ← (default) |
| **purge_subnets**  boolean | Purge existing subnets that are not found in subnets. Ignored unless the subnets option is supplied.  Choices:   - `false` - `true` ← (default) |
| **purge_tags**  boolean | Purge existing tags that are not found in route table.  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **route_table_id**  string | The ID of the route table to update or delete.  Required when *lookup=id*. |
| **routes**  list / elements=dictionary | List of routes in the route table.  Routes are specified as dicts containing the keys `dest` and one of `gateway_id`, `instance_id`, `network_interface_id`, or `vpc_peering_connection_id`.  The value of `dest` is used for the destination match. It may be a IPv4 CIDR block or a IPv6 CIDR block.  If *gateway_id* is specified, you can refer to the VPC’s IGW by using the value `igw`.  Routes are required for present states. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Create or destroy the VPC route table.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string | An array of subnets to add to this route table. Subnets may be specified by either subnet ID, Name tag, or by a CIDR such as ‘10.0.0.0/24’ or ‘fd00::/8’. |
| **tags**  aliases: resource_tags  dictionary | A dictionary of resource tags of the form: `{ tag1: value1, tag2: value2 }`. Tags are used to uniquely identify route tables within a VPC when the route_table_id is not supplied. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_id**  string | VPC ID of the VPC in which to create the route table.  Required when *state=present* or *lookup=tag*. |

## [Notes](ec2_vpc_route_table_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vpc_route_table_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Basic creation example:
- name: Set up public subnet route table
  amazon.aws.ec2_vpc_route_table:
    vpc_id: vpc-1245678
    region: us-west-1
    tags:
      Name: Public
    subnets:
      - "{{ jumpbox_subnet.subnet.id }}"
      - "{{ frontend_subnet.subnet.id }}"
      - "{{ vpn_subnet.subnet_id }}"
    routes:
      - dest: 0.0.0.0/0
        gateway_id: "{{ igw.gateway_id }}"
      - dest: ::/0
        gateway_id: "{{ igw.gateway_id }}"
  register: public_route_table

- name: Create vpc gateway
  amazon.aws.ec2_vpc_igw:
    vpc_id: vpc-1245678
  register: vpc_igw

- name: Create gateway route table
  amazon.aws.ec2_vpc_route_table:
    vpc_id: vpc-1245678
    tags:
      Name: Gateway route table
    gateway_id: "{{ vpc_igw.gateway_id }}"
  register: gateway_route_table

- name: Disassociate gateway from route table
  amazon.aws.ec2_vpc_route_table:
    vpc_id: vpc-1245678
    tags:
      Name: Gateway route table
    gateway_id: None
  register: gateway_route_table

- name: Set up NAT-protected route table
  amazon.aws.ec2_vpc_route_table:
    vpc_id: vpc-1245678
    region: us-west-1
    tags:
      Name: Internal
    subnets:
      - "{{ application_subnet.subnet.id }}"
      - 'Database Subnet'
      - '10.0.0.0/8'
    routes:
      - dest: 0.0.0.0/0
        instance_id: "{{ nat.instance_id }}"
  register: nat_route_table

- name: delete route table
  amazon.aws.ec2_vpc_route_table:
    vpc_id: vpc-1245678
    region: us-west-1
    route_table_id: "{{ route_table.id }}"
    lookup: id
    state: absent
```

## [Return Values](ec2_vpc_route_table_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **route_table**  complex | Route Table result.  Returned: always |
| **associations**  complex | List of associations between the route table and one or more subnets or a gateway.  Returned: always |
| **association_state**  complex | The state of the association.  Returned: always |
| **state**  string | The state of the association.  Returned: always  Sample: `"associated"` |
| **state_message**  string | Additional information about the state of the association.  Returned: when available  Sample: `"Creating association"` |
| **gateway_id**  string | ID of the internet gateway or virtual private gateway.  Returned: when route table is a gateway route table  Sample: `"igw-03312309"` |
| **main**  boolean | Whether this is the main route table.  Returned: always  Sample: `false` |
| **route_table_association_id**  string | ID of association between route table and subnet.  Returned: always  Sample: `"rtbassoc-ab47cfc3"` |
| **route_table_id**  string | ID of the route table.  Returned: always  Sample: `"rtb-bf779ed7"` |
| **subnet_id**  string | ID of the subnet.  Returned: when route table is a subnet route table  Sample: `"subnet-82055af9"` |
| **id**  string | ID of the route table (same as route_table_id for backwards compatibility).  Returned: always  Sample: `"rtb-bf779ed7"` |
| **propagating_vgws**  list / elements=string | List of Virtual Private Gateways propagating routes.  Returned: always  Sample: `[]` |
| **route_table_id**  string | ID of the route table.  Returned: always  Sample: `"rtb-bf779ed7"` |
| **routes**  complex | List of routes in the route table.  Returned: always |
| **destination_cidr_block**  string | IPv4 CIDR block of destination  Returned: always  Sample: `"10.228.228.0/22"` |
| **destination_ipv6_cidr_block**  string | IPv6 CIDR block of destination  Returned: when the route includes an IPv6 destination  Sample: `"2600:1f1c:1b3:8f00:8000::/65"` |
| **gateway_id**  string | ID of the gateway.  Returned: when gateway is local or internet gateway  Sample: `"local"` |
| **instance_id**  string | ID of a NAT instance.  Returned: when the route is via an EC2 instance  Sample: `"i-abcd123456789"` |
| **instance_owner_id**  string | AWS account owning the NAT instance.  Returned: when the route is via an EC2 instance  Sample: `"123456789012"` |
| **nat_gateway_id**  string | ID of the NAT gateway.  Returned: when the route is via a NAT gateway  Sample: `"local"` |
| **origin**  string | mechanism through which the route is in the table.  Returned: always  Sample: `"CreateRouteTable"` |
| **state**  string | state of the route.  Returned: always  Sample: `"active"` |
| **tags**  dictionary | Tags applied to the route table.  Returned: always  Sample: `{"Name": "Public route table", "Public": "true"}` |
| **vpc_id**  string | ID for the VPC in which the route lives.  Returned: always  Sample: `"vpc-6e2d2407"` |

### Authors

- Robert Estelle (@erydo)
- Rob White (@wimnat)
- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
