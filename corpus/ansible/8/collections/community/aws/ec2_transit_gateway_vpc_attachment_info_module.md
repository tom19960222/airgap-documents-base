---
collection: ansible
version: "8"
title: "community.aws.ec2_transit_gateway_vpc_attachment_info module – describes AWS Transit Gateway VPC attachments"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/ec2_transit_gateway_vpc_attachment_info_module.html
fetched_at: 2026-07-28T01:40:46+00:00
---
# community.aws.ec2_transit_gateway_vpc_attachment_info module – describes AWS Transit Gateway VPC attachments

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
> see [Requirements](ec2_transit_gateway_vpc_attachment_info_module.md#ansible-collections-community-aws-ec2-transit-gateway-vpc-attachment-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.ec2_transit_gateway_vpc_attachment_info`.

New in community.aws 4.0.0

- [Synopsis](ec2_transit_gateway_vpc_attachment_info_module.md#synopsis)
- [Requirements](ec2_transit_gateway_vpc_attachment_info_module.md#requirements)
- [Parameters](ec2_transit_gateway_vpc_attachment_info_module.md#parameters)
- [Notes](ec2_transit_gateway_vpc_attachment_info_module.md#notes)
- [Examples](ec2_transit_gateway_vpc_attachment_info_module.md#examples)
- [Return Values](ec2_transit_gateway_vpc_attachment_info_module.md#return-values)

## [Synopsis](ec2_transit_gateway_vpc_attachment_info_module.md#id1)

- Describes AWS Transit Gateway VPC Attachments.

## [Requirements](ec2_transit_gateway_vpc_attachment_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_transit_gateway_vpc_attachment_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A dictionary of filters to apply. Each dict item consists of a filter key and a filter value.  Setting a `tag:Name` filter will override the *name* parameter. |
| **id**  aliases: attachment_id  string | The ID of the Transit Gateway Attachment.  Mutually exclusive with *name* and *filters* |
| **include_deleted**  boolean | If *include_deleted=True*, then attachments in a deleted state will also be returned.  Setting a `state` filter will override the *include_deleted* parameter.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The `Name` tag of the Transit Gateway attachment. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_transit_gateway_vpc_attachment_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_transit_gateway_vpc_attachment_info_module.md#id5)

```yaml+jinja
# Describe a specific Transit Gateway attachment.
- community.aws.ec2_transit_gateway_vpc_attachment_info:
    id: 'tgw-attach-0123456789abcdef0'

# Describe all attachments attached to a transit gateway.
- community.aws.ec2_transit_gateway_vpc_attachment_info:
    filters:
      transit-gateway-id: tgw-0fedcba9876543210'

# Describe all attachments in an account.
- community.aws.ec2_transit_gateway_vpc_attachment_info:
    filters:
      transit-gateway-id: tgw-0fedcba9876543210'
```

## [Return Values](ec2_transit_gateway_vpc_attachment_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **transit_gateway_attachments**  list / elements=dictionary | The attributes of the Transit Gateway attachments.  **Returned:** success |
| **creation_time**  string | An ISO 8601 date time stamp of when the attachment was created.  **Returned:** success  **Sample:** `"2022-03-10T16:40:26+00:00"` |
| **options**  dictionary | Additional VPC attachment options.  **Returned:** success |
| **appliance_mode_support**  string | Indicates whether appliance mode support is enabled.  **Returned:** success  **Sample:** `"enable"` |
| **dns_support**  string | Indicates whether DNS support is enabled.  **Returned:** success  **Sample:** `"disable"` |
| **ipv6_support**  string | Indicates whether IPv6 support is disabled.  **Returned:** success  **Sample:** `"disable"` |
| **state**  string | The state of the attachment.  **Returned:** success  **Sample:** `"deleting"` |
| **subnet_ids**  list / elements=string | The IDs of the subnets in use by the attachment.  **Returned:** success  **Sample:** `["subnet-0123456789abcdef0", "subnet-11111111111111111"]` |
| **tags**  dictionary | A dictionary representing the resource tags.  **Returned:** success |
| **transit_gateway_attachment_id**  string | The ID of the attachment.  **Returned:** success  **Sample:** `"tgw-attach-0c0c5fd0b0f01d1c9"` |
| **transit_gateway_id**  string | The ID of the transit gateway that the attachment is connected to.  **Returned:** success  **Sample:** `"tgw-0123456789abcdef0"` |
| **vpc_id**  string | The ID of the VPC that the attachment is connected to.  **Returned:** success  **Sample:** `"vpc-0123456789abcdef0"` |
| **vpc_owner_id**  string | The ID of the account that the VPC belongs to.  **Returned:** success  **Sample:** `"123456789012"` |

### Authors

- Mark Chappell (@tremble)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
