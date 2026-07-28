---
collection: ansible
version: "8"
title: "amazon.aws.aws_account_attribute lookup – Look up AWS account attributes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/aws_account_attribute_lookup.html
fetched_at: 2026-07-28T01:07:18+00:00
---
# amazon.aws.aws_account_attribute lookup – Look up AWS account attributes

> **Note:**
>
> This lookup plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/ui/repo/published/amazon/aws/) (version 6.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install amazon.aws`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](aws_account_attribute_lookup.md#ansible-collections-amazon-aws-aws-account-attribute-lookup-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.aws_account_attribute`.

- [Synopsis](aws_account_attribute_lookup.md#synopsis)
- [Requirements](aws_account_attribute_lookup.md#requirements)
- [Keyword parameters](aws_account_attribute_lookup.md#keyword-parameters)
- [Notes](aws_account_attribute_lookup.md#notes)
- [Examples](aws_account_attribute_lookup.md#examples)
- [Return Value](aws_account_attribute_lookup.md#return-value)

## [Synopsis](aws_account_attribute_lookup.md#id1)

- Describes attributes of your AWS account. You can specify one of the listed attribute choices or omit it to see all attributes.

## [Requirements](aws_account_attribute_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Keyword parameters](aws_account_attribute_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('amazon.aws.aws_account_attribute', key1=value1, key2=value2, ...)` and `query('amazon.aws.aws_account_attribute', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) - Environment variable: [`AWS_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_ACCESS_KEY) - Environment variable: [`EC2_ACCESS_KEY`](../../environment_variables.md#envvar-EC2_ACCESS_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_ACCESS_KEY_ID |
| **attribute**  string | The attribute for which to get the value(s).  **Choices:**   - `"supported-platforms"` - `"default-vpc"` - `"max-instances"` - `"vpc-max-security-groups-per-interface"` - `"max-elastic-ips"` - `"vpc-max-elastic-ips"` - `"has-ec2-classic"` |
| **endpoint_url**  aliases: aws_endpoint_url, endpoint  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The *endpoint* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_URL`](../../environment_variables.md#envvar-AWS_URL) - Environment variable: [`EC2_URL`](../../environment_variables.md#envvar-EC2_URL)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_URL |
| **profile**  aliases: aws_profile, boto_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options.  The *boto_profile* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) - Environment variable: [`AWS_DEFAULT_PROFILE`](../../environment_variables.md#envvar-AWS_DEFAULT_PROFILE) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  **Configuration:**   - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) - Environment variable: [`EC2_REGION`](../../environment_variables.md#envvar-EC2_REGION)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources, when it is used for all connections  Alternative: |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) - Environment variable: [`AWS_SECRET_KEY`](../../environment_variables.md#envvar-AWS_SECRET_KEY) - Environment variable: [`EC2_SECRET_KEY`](../../environment_variables.md#envvar-EC2_SECRET_KEY)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SECRET_ACCESS_KEY |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  **Configuration:**   - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Environment variable: [`AWS_SECURITY_TOKEN`](../../environment_variables.md#envvar-AWS_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: AWS_SECURITY_TOKEN was used for compatibility with the original boto SDK, support for which has been dropped  Alternative: AWS_SESSION_TOKEN - Environment variable: [`EC2_SECURITY_TOKEN`](../../environment_variables.md#envvar-EC2_SECURITY_TOKEN)  Removed in: major release after 2024-12-01  Why: EC2 in the name implied it was limited to EC2 resources. However, it is used for all connections.  Alternative: AWS_SESSION_TOKEN |

## [Notes](aws_account_attribute_lookup.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](aws_account_attribute_lookup.md#id5)

```yaml+jinja
vars:
  has_ec2_classic: "{{ lookup('aws_account_attribute', attribute='has-ec2-classic') }}"
  # true | false

  default_vpc_id: "{{ lookup('aws_account_attribute', attribute='default-vpc') }}"
  # vpc-xxxxxxxx | none

  account_details: "{{ lookup('aws_account_attribute', wantlist='true') }}"
  # {'default-vpc': ['vpc-xxxxxxxx'], 'max-elastic-ips': ['5'], 'max-instances': ['20'],
  #  'supported-platforms': ['VPC', 'EC2'], 'vpc-max-elastic-ips': ['5'], 'vpc-max-security-groups-per-interface': ['5']}
```

## [Return Value](aws_account_attribute_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | Returns a boolean when *attribute* is check_ec2_classic. Otherwise returns the value(s) of the attribute (or all attributes if one is not specified).  **Returned:** success |

### Authors

- Sloane Hertel (@s-hertel)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
