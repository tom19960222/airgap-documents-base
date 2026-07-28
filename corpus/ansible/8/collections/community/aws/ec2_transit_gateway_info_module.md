---
collection: ansible
version: "8"
title: "community.aws.ec2_transit_gateway_info module – Gather information about ec2 transit gateways in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ec2_transit_gateway_info_module.html
fetched_at: 2026-07-28T01:40:45+00:00
---
# community.aws.ec2_transit_gateway_info module – Gather information about ec2 transit gateways in AWS

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
> see [Requirements](ec2_transit_gateway_info_module.md#ansible-collections-community-aws-ec2-transit-gateway-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_transit_gateway_info`.

New in community.aws 1.0.0

- [Synopsis](ec2_transit_gateway_info_module.md#synopsis)
- [Requirements](ec2_transit_gateway_info_module.md#requirements)
- [Parameters](ec2_transit_gateway_info_module.md#parameters)
- [Notes](ec2_transit_gateway_info_module.md#notes)
- [Examples](ec2_transit_gateway_info_module.md#examples)
- [Return Values](ec2_transit_gateway_info_module.md#return-values)

## [Synopsis](ec2_transit_gateway_info_module.md#id1)

- Gather information about ec2 transit gateways in AWS

## [Requirements](ec2_transit_gateway_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_transit_gateway_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html> for filters.  **Default:** `{}` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **transit_gateway_ids**  aliases: transit_gateway_id  list / elements=string | A list of transit gateway IDs to gather information for.  **Default:** `[]` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_transit_gateway_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_transit_gateway_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather info about all transit gateways
  community.aws.ec2_transit_gateway_info:

- name: Gather info about a particular transit gateway using filter transit gateway ID
  community.aws.ec2_transit_gateway_info:
    filters:
      transit-gateway-id: tgw-02c42332e6b7da829

- name: Gather info about a particular transit gateway using multiple option filters
  community.aws.ec2_transit_gateway_info:
    filters:
      options.dns-support: enable
      options.vpn-ecmp-support: enable

- name: Gather info about multiple transit gateways using module param
  community.aws.ec2_transit_gateway_info:
    transit_gateway_ids:
      - tgw-02c42332e6b7da829
      - tgw-03c53443d5a8cb716
```

## [Return Values](ec2_transit_gateway_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **transit_gateways**  complex | Transit gateways that match the provided filters. Each element consists of a dict with all the information related to that transit gateway.  **Returned:** on success |
| **creation_time**  string | The creation time.  **Returned:** always  **Sample:** `"2019-02-05T16:19:58+00:00"` |
| **description**  string | The description of the transit gateway.  **Returned:** always  **Sample:** `"A transit gateway"` |
| **options**  complex | A dictionary of the transit gateway options.  **Returned:** always |
| **amazon_side_asn**  integer | A private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is 64512 to 65534 for 16-bit ASNs and 4200000000 to 4294967294 for 32-bit ASNs.  **Returned:** always  **Sample:** `64512` |
| **association_default_route_table_id**  string | The ID of the default association route table.  **Returned:** when present  **Sample:** `"rtb-11223344"` |
| **auto_accept_shared_attachments**  string | Indicates whether attachment requests are automatically accepted.  **Returned:** always  **Sample:** `"enable"` |
| **default_route_table_association**  string | Indicates whether resource attachments are automatically associated with the default association route table.  **Returned:** always  **Sample:** `"disable"` |
| **default_route_table_propagation**  string | Indicates whether resource attachments automatically propagate routes to the default propagation route table.  **Returned:** always  **Sample:** `"disable"` |
| **dns_support**  string | Indicates whether DNS support is enabled.  **Returned:** always  **Sample:** `"enable"` |
| **propagation_default_route_table_id**  string | The ID of the default propagation route table.  **Returned:** when present  **Sample:** `"rtb-11223344"` |
| **vpn_ecmp_support**  string | Indicates whether Equal Cost Multipath Protocol support is enabled.  **Returned:** always  **Sample:** `"enable"` |
| **owner_id**  string | The AWS account number ID which owns the transit gateway.  **Returned:** always  **Sample:** `"123456789012"` |
| **state**  string | The state of the transit gateway.  **Returned:** always  **Sample:** `"available"` |
| **tags**  dictionary | A dict of tags associated with the transit gateway.  **Returned:** always  **Sample:** `{"Name": "A sample TGW"}` |
| **transit_gateway_arn**  string | The Amazon Resource Name (ARN) of the transit gateway.  **Returned:** always  **Sample:** `"arn:aws:ec2:us-west-2:123456789012:transit-gateway/tgw-02c42332e6b7da829"` |
| **transit_gateway_id**  string | The ID of the transit gateway.  **Returned:** always  **Sample:** `"tgw-02c42332e6b7da829"` |

### Authors

- Bob Boldin (@BobBoldin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
