---
collection: ansible
version: "6"
title: "amazon.aws.aws_account_attribute lookup – Look up AWS account attributes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/aws_account_attribute_lookup.html
fetched_at: 2026-07-27T16:43:56+00:00
---
# amazon.aws.aws_account_attribute lookup – Look up AWS account attributes.

> **Note:**
>
> This lookup plugin is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
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
- [Examples](aws_account_attribute_lookup.md#examples)
- [Return Value](aws_account_attribute_lookup.md#return-value)

## [Synopsis](aws_account_attribute_lookup.md#id1)

- Describes attributes of your AWS account. You can specify one of the listed attribute choices or omit it to see all attributes.

## [Requirements](aws_account_attribute_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Keyword parameters](aws_account_attribute_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('amazon.aws.aws_account_attribute', key1=value1, key2=value2, ...)` and `query('amazon.aws.aws_account_attribute', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **attribute**  string | The attribute for which to get the value(s).  Choices:   - `"supported-platforms"` - `"default-vpc"` - `"max-instances"` - `"vpc-max-security-groups-per-interface"` - `"max-elastic-ips"` - `"vpc-max-elastic-ips"` - `"has-ec2-classic"` |
| **aws_access_key**  aliases: aws_access_key_id  string | The AWS access key to use.  Configuration:   - Environment variable: [`EC2_ACCESS_KEY`](../../environment_variables.md#envvar-EC2_ACCESS_KEY) - Environment variable: [`AWS_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_ACCESS_KEY) - Environment variable: [`AWS_ACCESS_KEY_ID`](../../environment_variables.md#envvar-AWS_ACCESS_KEY_ID) |
| **aws_profile**  aliases: boto_profile  string | The AWS profile  Configuration:   - Environment variable: [`AWS_DEFAULT_PROFILE`](../../environment_variables.md#envvar-AWS_DEFAULT_PROFILE) - Environment variable: [`AWS_PROFILE`](../../environment_variables.md#envvar-AWS_PROFILE) |
| **aws_secret_key**  aliases: aws_secret_access_key  string | The AWS secret key that corresponds to the access key.  Configuration:   - Environment variable: [`EC2_SECRET_KEY`](../../environment_variables.md#envvar-EC2_SECRET_KEY) - Environment variable: [`AWS_SECRET_KEY`](../../environment_variables.md#envvar-AWS_SECRET_KEY) - Environment variable: [`AWS_SECRET_ACCESS_KEY`](../../environment_variables.md#envvar-AWS_SECRET_ACCESS_KEY) |
| **aws_security_token**  string | The AWS security token if using temporary access and secret keys.  Configuration:   - Environment variable: [`EC2_SECURITY_TOKEN`](../../environment_variables.md#envvar-EC2_SECURITY_TOKEN) - Environment variable: [`AWS_SESSION_TOKEN`](../../environment_variables.md#envvar-AWS_SESSION_TOKEN) - Environment variable: [`AWS_SECURITY_TOKEN`](../../environment_variables.md#envvar-AWS_SECURITY_TOKEN) |
| **region**  string | The region for which to create the connection.  Configuration:   - Environment variable: [`EC2_REGION`](../../environment_variables.md#envvar-EC2_REGION) - Environment variable: [`AWS_REGION`](../../environment_variables.md#envvar-AWS_REGION) |

## [Examples](aws_account_attribute_lookup.md#id4)

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

## [Return Value](aws_account_attribute_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | Returns a boolean when *attribute* is check_ec2_classic. Otherwise returns the value(s) of the attribute (or all attributes if one is not specified).  Returned: success |

### Authors

- Sloane Hertel (@s-hertel)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
