---
collection: ansible
version: "8"
title: "amazon.aws.ec2_vpc_dhcp_option_info module – Gather information about DHCP options sets in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_vpc_dhcp_option_info_module.html
fetched_at: 2026-07-28T01:06:37+00:00
---
# amazon.aws.ec2_vpc_dhcp_option_info module – Gather information about DHCP options sets in AWS

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
> see [Requirements](ec2_vpc_dhcp_option_info_module.md#ansible-collections-amazon-aws-ec2-vpc-dhcp-option-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vpc_dhcp_option_info`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vpc_dhcp_option_info_module.md#synopsis)
- [Requirements](ec2_vpc_dhcp_option_info_module.md#requirements)
- [Parameters](ec2_vpc_dhcp_option_info_module.md#parameters)
- [Notes](ec2_vpc_dhcp_option_info_module.md#notes)
- [Examples](ec2_vpc_dhcp_option_info_module.md#examples)
- [Return Values](ec2_vpc_dhcp_option_info_module.md#return-values)

## [Synopsis](ec2_vpc_dhcp_option_info_module.md#id1)

- Gather information about DHCP options sets in AWS.

## [Requirements](ec2_vpc_dhcp_option_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_vpc_dhcp_option_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **dhcp_options_ids**  list / elements=string | Get details of specific DHCP option IDs. |
| **dry_run**  boolean | Checks whether you have the required permissions to view the DHCP options.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeDhcpOptions.html> for possible filters.  **Default:** `{}` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_vpc_dhcp_option_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_vpc_dhcp_option_info_module.md#id5)

```yaml+jinja
# # Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Gather information about all DHCP Option sets for an account or profile
  amazon.aws.ec2_vpc_dhcp_option_info:
    region: ap-southeast-2
    profile: production
  register: dhcp_info

- name: Gather information about a filtered list of DHCP Option sets
  amazon.aws.ec2_vpc_dhcp_option_info:
    region: ap-southeast-2
    profile: production
    filters:
        "tag:Name": "abc-123"
  register: dhcp_info

- name: Gather information about a specific DHCP Option set by DhcpOptionId
  amazon.aws.ec2_vpc_dhcp_option_info:
    region: ap-southeast-2
    profile: production
    dhcp_options_ids: dopt-123fece2
  register: dhcp_info
```

## [Return Values](ec2_vpc_dhcp_option_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if listing the dhcp options succeeds.  **Returned:** always |
| **dhcp_config**  list / elements=dictionary | The boto2-style DHCP options created, associated or found. Provided for consistency with ec2_vpc_dhcp_option’s `dhcp_config`.  **Returned:** always |
| **domain-name**  list / elements=string | The domain name for hosts in the DHCP option sets.  **Returned:** when available  **Sample:** `["my.example.com"]` |
| **domain-name-servers**  list / elements=string | The IP addresses of up to four domain name servers, or AmazonProvidedDNS.  **Returned:** when available  **Sample:** `["10.0.0.1", "10.0.1.1"]` |
| **netbios-name-servers**  list / elements=string | The IP addresses of up to four NetBIOS name servers.  **Returned:** when available  **Sample:** `["10.0.0.1", "10.0.1.1"]` |
| **netbios-node-type**  string | The NetBIOS node type (1, 2, 4, or 8).  **Returned:** when available  **Sample:** `"2"` |
| **ntp-servers**  list / elements=string | The IP addresses of up to four Network Time Protocol (NTP) servers.  **Returned:** when available  **Sample:** `["10.0.0.1", "10.0.1.1"]` |
| **dhcp_options**  list / elements=dictionary | The DHCP options created, associated or found.  **Returned:** always |
| **dhcp_configurations**  list / elements=dictionary | The DHCP configuration for the option set.  **Returned:** success  **Sample:** `[{"key": "ntp-servers", "values": [{"value": "10.0.1.2"}]}, "{\"key\": \"netbios-name-servers\", \"values\": [{value\": \"10.0.0.1\"}, {\"value\": \"10.0.1.1\" }]}"]` |
| **key**  string | The name of a DHCP option.  **Returned:** always |
| **values**  list / elements=dictionary | List of values for the DHCP option.  **Returned:** always |
| **value**  string | The attribute value. This value is case-sensitive.  **Returned:** always |
| **dhcp_options_id**  string | The aws resource id of the primary DHCP options set created or found.  **Returned:** success  **Sample:** `"dopt-0955331de6a20dd07"` |
| **owner_id**  string | The ID of the AWS account that owns the DHCP options set.  **Returned:** success  **Sample:** `"012345678912"` |
| **tags**  list / elements=dictionary | The tags to be applied to a DHCP options set.  **Returned:** success  **Sample:** `[{"Key": "CreatedBy", "Value": "ansible-test"}, {"Key": "Collection", "Value": "amazon.aws"}]` |

### Authors

- Nick Aslanidis (@naslanidis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
