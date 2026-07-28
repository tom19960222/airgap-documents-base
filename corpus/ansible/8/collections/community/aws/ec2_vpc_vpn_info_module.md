---
collection: ansible
version: "8"
title: "community.aws.ec2_vpc_vpn_info module – Gather information about VPN Connections in AWS."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ec2_vpc_vpn_info_module.html
fetched_at: 2026-07-28T01:40:53+00:00
---
# community.aws.ec2_vpc_vpn_info module – Gather information about VPN Connections in AWS.

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
> see [Requirements](ec2_vpc_vpn_info_module.md#ansible-collections-community-aws-ec2-vpc-vpn-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_vpc_vpn_info`.

New in community.aws 1.0.0

- [Synopsis](ec2_vpc_vpn_info_module.md#synopsis)
- [Requirements](ec2_vpc_vpn_info_module.md#requirements)
- [Parameters](ec2_vpc_vpn_info_module.md#parameters)
- [Notes](ec2_vpc_vpn_info_module.md#notes)
- [Examples](ec2_vpc_vpn_info_module.md#examples)
- [Return Values](ec2_vpc_vpn_info_module.md#return-values)

## [Synopsis](ec2_vpc_vpn_info_module.md#id1)

- Gather information about VPN Connections in AWS.

## [Requirements](ec2_vpc_vpn_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_vpn_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html> for possible filters.  **Default:** `{}` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpn_connection_ids**  list / elements=string | Get details of a specific VPN connections using vpn connection ID/IDs. This value should be provided as a list.  **Default:** `[]` |

## [Notes](ec2_vpc_vpn_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_vpc_vpn_info_module.md#id5)

```yaml+jinja
# # Note: These examples do not set authentication details, see the AWS Guide for details.
- name: Gather information about all vpn connections
  community.aws.ec2_vpc_vpn_info:

- name: Gather information about a filtered list of vpn connections, based on tags
  community.aws.ec2_vpc_vpn_info:
    filters:
      "tag:Name": test-connection
  register: vpn_conn_info

- name: Gather information about vpn connections by specifying connection IDs.
  community.aws.ec2_vpc_vpn_info:
    filters:
      vpn-gateway-id: vgw-cbe66beb
  register: vpn_conn_info
```

## [Return Values](ec2_vpc_vpn_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vpn_connections**  complex | List of one or more VPN Connections.  **Returned:** always |
| **category**  string | The category of the VPN connection.  **Returned:** always  **Sample:** `"VPN"` |
| **customer_gateway_id**  string | The ID of the customer gateway at your end of the VPN connection.  **Returned:** always  **Sample:** `"cgw-17a53c37"` |
| **customer_gatway_configuration**  string | The configuration information for the VPN connection’s customer gateway (in the native XML format).  **Returned:** always |
| **options**  dictionary | The VPN connection options.  **Returned:** always  **Sample:** `{"static_routes_only": false}` |
| **routes**  complex | List of static routes associated with the VPN connection.  **Returned:** always |
| **destination_cidr_block**  string | The CIDR block associated with the local subnet of the customer data center.  **Returned:** always  **Sample:** `"10.0.0.0/16"` |
| **state**  string | The current state of the static route.  **Returned:** always  **Sample:** `"available"` |
| **state**  string | The current state of the VPN connection.  **Returned:** always  **Sample:** `"available"` |
| **tags**  dictionary | Any tags assigned to the VPN connection.  **Returned:** always  **Sample:** `{"Name": "test-conn"}` |
| **type**  string | The type of VPN connection.  **Returned:** always  **Sample:** `"ipsec.1"` |
| **vgw_telemetry**  complex | Information about the VPN tunnel.  **Returned:** always |
| **accepted_route_count**  integer | The number of accepted routes.  **Returned:** always  **Sample:** `0` |
| **certificate_arn**  string | The Amazon Resource Name of the virtual private gateway tunnel endpoint certificate.  **Returned:** when a private certificate is used for authentication  **Sample:** `"arn:aws:acm:us-east-1:123456789012:certificate/c544d8ce-20b8-4fff-98b0-example"` |
| **last_status_change**  string | The date and time of the last change in status.  **Returned:** always  **Sample:** `"2018-02-09T14:35:27+00:00"` |
| **outside_ip_address**  string | The Internet-routable IP address of the virtual private gateway’s outside interface.  **Returned:** always  **Sample:** `"13.127.79.191"` |
| **status**  string | The status of the VPN tunnel.  **Returned:** always  **Sample:** `"DOWN"` |
| **status_message**  string | If an error occurs, a description of the error.  **Returned:** always  **Sample:** `"IPSEC IS DOWN"` |
| **vpn_connection_id**  string | The ID of the VPN connection.  **Returned:** always  **Sample:** `"vpn-f700d5c0"` |
| **vpn_gateway_id**  string | The ID of the virtual private gateway at the AWS side of the VPN connection.  **Returned:** always  **Sample:** `"vgw-cbe56bfb"` |

### Authors

- Madhura Naniwadekar (@Madhura-CSI)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
