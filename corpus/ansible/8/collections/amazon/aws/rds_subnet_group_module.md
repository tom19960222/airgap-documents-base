---
collection: ansible
version: "8"
title: "amazon.aws.rds_subnet_group module – manage RDS database subnet groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/rds_subnet_group_module.html
fetched_at: 2026-07-28T01:07:10+00:00
---
# amazon.aws.rds_subnet_group module – manage RDS database subnet groups

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
> see [Requirements](rds_subnet_group_module.md#ansible-collections-amazon-aws-rds-subnet-group-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.rds_subnet_group`.

New in amazon.aws 5.0.0

- [Synopsis](rds_subnet_group_module.md#synopsis)
- [Requirements](rds_subnet_group_module.md#requirements)
- [Parameters](rds_subnet_group_module.md#parameters)
- [Notes](rds_subnet_group_module.md#notes)
- [Examples](rds_subnet_group_module.md#examples)
- [Return Values](rds_subnet_group_module.md#return-values)

## [Synopsis](rds_subnet_group_module.md#id1)

- Creates, modifies, and deletes RDS database subnet groups.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](rds_subnet_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](rds_subnet_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Database subnet group description.  Required when *state=present*. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **name**  string / required | Database subnet group identifier. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string / required | Specifies whether the subnet should be present or absent.  **Choices:**   - `"present"` - `"absent"` |
| **subnets**  list / elements=string | List of subnet IDs that make up the database subnet group.  Required when *state=present*. |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](rds_subnet_group_module.md#id4)

> **Note:**
>
> - Support for *tags* and *purge_tags* was added in release 3.2.0.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](rds_subnet_group_module.md#id5)

```yaml+jinja
- name: Add or change a subnet group
  amazon.aws.rds_subnet_group:
    state: present
    name: norwegian-blue
    description: My Fancy Ex Parrot Subnet Group
    subnets:
      - subnet-aaaaaaaa
      - subnet-bbbbbbbb

- name: Add or change a subnet group and associate tags
  amazon.aws.rds_subnet_group:
    state: present
    name: norwegian-blue
    description: My Fancy Ex Parrot Subnet Group
    subnets:
      - subnet-aaaaaaaa
      - subnet-bbbbbbbb
    tags:
      tag1: Tag1
      tag2: Tag2

- name: Remove a subnet group
  amazon.aws.rds_subnet_group:
    state: absent
    name: norwegian-blue
```

## [Return Values](rds_subnet_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if listing the RDS subnet group succeeds.  **Returned:** always  **Sample:** `false` |
| **subnet_group**  complex | Dictionary of DB subnet group values  **Returned:** *state=present* |
| **db_subnet_group_arn**  string | The ARN of the DB subnet group  **Returned:** *state=present*  **Sample:** `"arn:aws:rds:eu-north-1:123456789012:subgrp:ansible-test-13950442"` |
| **db_subnet_group_description**  string | The description of the DB subnet group  **Returned:** *state=present*  **Sample:** `"Simple description."` |
| **db_subnet_group_name**  string | The name of the DB subnet group  **Returned:** *state=present*  **Sample:** `"ansible-test-mbp-13950442"` |
| **description**  string | The description of the DB subnet group (maintained for backward compatibility)  **Returned:** *state=present*  **Sample:** `"Simple description."` |
| **name**  string | The name of the DB subnet group (maintained for backward compatibility)  **Returned:** *state=present*  **Sample:** `"ansible-test-mbp-13950442"` |
| **status**  string | The status of the DB subnet group (maintained for backward compatibility)  **Returned:** *state=present*  **Sample:** `"Complete"` |
| **subnet_group_status**  string | The status of the DB subnet group  **Returned:** *state=present*  **Sample:** `"Complete"` |
| **subnet_ids**  list / elements=string | Contains a list of Subnet IDs  **Returned:** *state=present*  **Sample:** `["subnet-08c94870f4480797e"]` |
| **subnets**  list / elements=string | Contains a list of Subnet elements (@see <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_subnet_groups>)  **Returned:** *state=present* |
| **subnet_availability_zone**  dictionary  *added in community.aws 3.2.0* | Contains Availability Zone information.  **Returned:** *state=present*  **Sample:** `{"name": "eu-north-1b"}` |
| **subnet_identifier**  string  *added in community.aws 3.2.0* | The identifier of the subnet.  **Returned:** *state=present*  **Sample:** `"subnet-08c94870f4480797e"` |
| **subnet_outpost**  dictionary  *added in community.aws 3.2.0* | This value specifies the Outpost.  **Returned:** *state=present*  **Sample:** `{}` |
| **subnet_status**  string  *added in community.aws 3.2.0* | The status of the subnet.  **Returned:** *state=present*  **Sample:** `"Active"` |
| **tags**  dictionary  *added in community.aws 3.2.0* | The tags associated with the subnet group  **Returned:** *state=present*  **Sample:** `{"tag1": "Tag1", "tag2": "Tag2"}` |
| **vpc_id**  string | The VpcId of the DB subnet group  **Returned:** *state=present*  **Sample:** `"vpc-0acb0ba033ff2119c"` |

### Authors

- Scott Anderson (@tastychutney)
- Alina Buzachis (@alinabuzachis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
