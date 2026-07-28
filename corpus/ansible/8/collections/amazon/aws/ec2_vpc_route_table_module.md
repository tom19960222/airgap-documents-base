---
collection: ansible
version: "8"
title: "amazon.aws.ec2_vpc_route_table module – Manage route tables for AWS Virtual Private Clouds"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_vpc_route_table_module.html
fetched_at: 2026-07-28T01:06:44+00:00
---
# amazon.aws.ec2_vpc_route_table module – Manage route tables for AWS Virtual Private Clouds

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

- Manage route tables for AWS Virtual Private Clouds (VPCs).

## [Requirements](ec2_vpc_route_table_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_route_table_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **gateway_id**  string  *added in amazon.aws 3.2.0* | The ID of the gateway to associate with the route table.  If *gateway_id* is `'None'` or `''`, gateway will be disassociated with the route table. |
| **lookup**  string | Look up route table by either *tags* or by *route_table_id*.  If *lookup=tag* and *tags* is not specified then no lookup for an existing route table is performed and a new route table will be created.  When using *lookup=tag*, multiple matches being found will result in a failure and no changes will be made.  To change the tags of a route table use *lookup=id*.  *vpc_id* must be specified when *lookup=tag*.  **Choices:**   - `"tag"` ← (default) - `"id"` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **propagating_vgw_ids**  list / elements=string | Enable route propagation from virtual gateways specified by ID. |
| **purge_routes**  boolean | Purge existing routes that are not found in routes.  **Choices:**   - `false` - `true` ← (default) |
| **purge_subnets**  boolean | Purge existing subnets that are not found in subnets.  Ignored unless the subnets option is supplied.  **Choices:**   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **route_table_id**  string | The ID of the route table to update or delete.  Required when *lookup=id*. |
| **routes**  list / elements=dictionary | List of routes in the route table.  Routes are specified as dicts containing the keys `dest` and one of `gateway_id`, `instance_id`, `network_interface_id`, or `vpc_peering_connection_id`.  The value of `dest` is used for the destination match. It may be a IPv4 CIDR block or a IPv6 CIDR block.  If *gateway_id* is specified, you can refer to the VPC’s IGW by using the value `igw`.  Routes are required for present states.  **Default:** `[]` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create or destroy the VPC route table.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string | An array of subnets to add to this route table. Subnets may be specified by either subnet ID, Name tag, or by a CIDR such as ‘10.0.0.0/24’ or ‘fd00::/8’. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_id**  string | VPC ID of the VPC in which to create the route table.  Required when *state=present* or *lookup=tag*. |

## [Notes](ec2_vpc_route_table_module.md#id4)

> **Note:**
>
> - Tags are used to uniquely identify route tables within a VPC when the *route_table_id* is not supplied.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

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

- name: Create VPC gateway
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
| **route_table**  complex | Route Table result.  **Returned:** always |
| **associations**  complex | List of associations between the route table and one or more subnets or a gateway.  **Returned:** always |
| **association_state**  complex | The state of the association.  **Returned:** always |
| **state**  string | The state of the association.  **Returned:** always  **Sample:** `"associated"` |
| **state_message**  string | Additional information about the state of the association.  **Returned:** when available  **Sample:** `"Creating association"` |
| **gateway_id**  string | ID of the internet gateway or virtual private gateway.  **Returned:** when route table is a gateway route table  **Sample:** `"igw-03312309"` |
| **main**  boolean | Whether this is the main route table.  **Returned:** always  **Sample:** `false` |
| **route_table_association_id**  string | ID of association between route table and subnet.  **Returned:** always  **Sample:** `"rtbassoc-ab47cfc3"` |
| **route_table_id**  string | ID of the route table.  **Returned:** always  **Sample:** `"rtb-bf779ed7"` |
| **subnet_id**  string | ID of the subnet.  **Returned:** when route table is a subnet route table  **Sample:** `"subnet-82055af9"` |
| **id**  string | ID of the route table (same as route_table_id for backwards compatibility).  **Returned:** always  **Sample:** `"rtb-bf779ed7"` |
| **propagating_vgws**  list / elements=string | List of Virtual Private Gateways propagating routes.  **Returned:** always  **Sample:** `[]` |
| **route_table_id**  string | ID of the route table.  **Returned:** always  **Sample:** `"rtb-bf779ed7"` |
| **routes**  complex | List of routes in the route table.  **Returned:** always |
| **carrier_gateway_id**  string  *added in amazon.aws 6.0.0* | ID of the Carrier gateway.  **Returned:** when the route is via a Carrier gateway  **Sample:** `"local"` |
| **destination_cidr_block**  string | IPv4 CIDR block of destination  **Returned:** always  **Sample:** `"10.228.228.0/22"` |
| **destination_ipv6_cidr_block**  string | IPv6 CIDR block of destination  **Returned:** when the route includes an IPv6 destination  **Sample:** `"2600:1f1c:1b3:8f00:8000::/65"` |
| **gateway_id**  string | ID of the gateway.  **Returned:** when gateway is local or internet gateway  **Sample:** `"local"` |
| **instance_id**  string | ID of a NAT instance.  **Returned:** when the route is via an EC2 instance  **Sample:** `"i-abcd123456789"` |
| **instance_owner_id**  string | AWS account owning the NAT instance.  **Returned:** when the route is via an EC2 instance  **Sample:** `"123456789012"` |
| **nat_gateway_id**  string | ID of the NAT gateway.  **Returned:** when the route is via a NAT gateway  **Sample:** `"local"` |
| **origin**  string | mechanism through which the route is in the table.  **Returned:** always  **Sample:** `"CreateRouteTable"` |
| **state**  string | state of the route.  **Returned:** always  **Sample:** `"active"` |
| **tags**  dictionary | Tags applied to the route table.  **Returned:** always  **Sample:** `{"Name": "Public route table", "Public": "true"}` |
| **vpc_id**  string | ID for the VPC in which the route lives.  **Returned:** always  **Sample:** `"vpc-6e2d2407"` |

### Authors

- Robert Estelle (@erydo)
- Rob White (@wimnat)
- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
