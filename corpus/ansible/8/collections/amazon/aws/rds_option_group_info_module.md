---
collection: ansible
version: "8"
title: "amazon.aws.rds_option_group_info module – rds_option_group_info module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/rds_option_group_info_module.html
fetched_at: 2026-07-28T01:07:08+00:00
---
# amazon.aws.rds_option_group_info module – rds_option_group_info module

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
> see [Requirements](rds_option_group_info_module.md#ansible-collections-amazon-aws-rds-option-group-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.rds_option_group_info`.

New in amazon.aws 5.0.0

- [Synopsis](rds_option_group_info_module.md#synopsis)
- [Requirements](rds_option_group_info_module.md#requirements)
- [Parameters](rds_option_group_info_module.md#parameters)
- [Notes](rds_option_group_info_module.md#notes)
- [Examples](rds_option_group_info_module.md#examples)
- [Return Values](rds_option_group_info_module.md#return-values)

## [Synopsis](rds_option_group_info_module.md#id1)

- Gather information about RDS option groups.
- This module was originally added to `community.aws` in release 2.1.0.

## [Requirements](rds_option_group_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](rds_option_group_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **engine_name**  string | Filters the list of option groups to only include groups associated with a specific database engine.  **Default:** `""` |
| **major_engine_version**  string | Filters the list of option groups to only include groups associated with a specific database engine version.  If specified, then *engine_name* must also be specified.  **Default:** `""` |
| **marker**  string | If this parameter is specified, the response includes only records beyond the marker, up to the value specified by *max_records*.  Allowed values are between `20` and `100`. |
| **max_records**  integer | The maximum number of records to include in the response.  **Default:** `100` |
| **option_group_name**  string | The name of the option group to describe.  Can’t be supplied together with *engine_name* or *major_engine_version*.  **Default:** `""` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](rds_option_group_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](rds_option_group_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: List an option group
  amazon.aws.rds_option_group_info:
    option_group_name: test-mysql-option-group
  register: option_group

- name: List all the option groups
  amazon.aws.rds_option_group_info:
    region: ap-southeast-2
    profile: production
  register: option_group
```

## [Return Values](rds_option_group_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if listing the RDS option group succeeds.  **Returned:** always  **Sample:** `false` |
| **option_groups_list**  complex | The available RDS option groups.  **Returned:** always |
| **allows_vpc_and_non_vpc_instance_memberships**  boolean | Indicates whether this option group can be applied to both VPC and non-VPC instances.  **Returned:** always  **Sample:** `false` |
| **engine_name**  string | Indicates the name of the engine that this option group can be applied to.  **Returned:** always  **Sample:** `"mysql"` |
| **major_engine_version**  string | Indicates the major engine version associated with this option group.  **Returned:** always  **Sample:** `"5.6"` |
| **option_group_arn**  string | The Amazon Resource Name (ARN) for the option group.  **Returned:** always  **Sample:** `"arn:aws:rds:ap-southeast-2:123456789012:og:ansible-test-option-group"` |
| **option_group_description**  string | Provides a description of the option group.  **Returned:** always  **Sample:** `"test mysql option group"` |
| **option_group_name**  string | Specifies the name of the option group.  **Returned:** always  **Sample:** `"test-mysql-option-group"` |
| **options**  complex | Indicates what options are available in the option group.  **Returned:** always |
| **db_security_group_memberships**  complex | If the option requires access to a port, then this DB security group allows access to the port.  **Returned:** always  **Sample:** `"list"` |
| **db_security_group_name**  string | The name of the DB security group.  **Returned:** always  **Sample:** `"mydbsecuritygroup"` |
| **status**  string | The status of the DB security group.  **Returned:** always  **Sample:** `"available"` |
| **option_description**  string | The description of the option.  **Returned:** always  **Sample:** `"Innodb Memcached for MySQL"` |
| **option_name**  string | The name of the option.  **Returned:** always  **Sample:** `"MEMCACHED"` |
| **option_settings**  complex | The name of the option.  **Returned:** always |
| **allowed_values**  string | The allowed values of the option setting.  **Returned:** always  **Sample:** `"1-2048"` |
| **apply_type**  string | The DB engine specific parameter type.  **Returned:** always  **Sample:** `"STATIC"` |
| **data_type**  string | The data type of the option setting.  **Returned:** always  **Sample:** `"INTEGER"` |
| **default_value**  string | The default value of the option setting.  **Returned:** always  **Sample:** `"1024"` |
| **description**  string | The description of the option setting.  **Returned:** always  **Sample:** `"Verbose level for memcached."` |
| **is_collection**  boolean | Indicates if the option setting is part of a collection.  **Returned:** always  **Sample:** `true` |
| **is_modifiable**  boolean | A Boolean value that, when true, indicates the option setting can be modified from the default.  **Returned:** always  **Sample:** `true` |
| **name**  string | The name of the option that has settings that you can set.  **Returned:** always  **Sample:** `"INNODB_API_ENABLE_MDL"` |
| **value**  string | The current value of the option setting.  **Returned:** always  **Sample:** `"0"` |
| **permanent**  boolean | Indicate if this option is permanent.  **Returned:** always  **Sample:** `true` |
| **persistent**  boolean | Indicate if this option is persistent.  **Returned:** always  **Sample:** `true` |
| **port**  integer | If required, the port configured for this option to use.  **Returned:** always  **Sample:** `11211` |
| **vpc_security_group_memberships**  list / elements=dictionary | If the option requires access to a port, then this VPC security group allows access to the port.  **Returned:** always |
| **status**  string | The status of the VPC security group.  **Returned:** always  **Sample:** `"available"` |
| **vpc_security_group_id**  string | The name of the VPC security group.  **Returned:** always  **Sample:** `"sg-0cd636a23ae76e9a4"` |
| **tags**  dictionary | The tags associated the Internet Gateway.  **Returned:** always  **Sample:** `{"Ansible": "Test"}` |
| **vpc_id**  string | If present, this option group can only be applied to instances that are in the VPC indicated by this field.  **Returned:** always  **Sample:** `"vpc-bf07e9d6"` |

### Authors

- Alina Buzachis (@alinabuzachis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
