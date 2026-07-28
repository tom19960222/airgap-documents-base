---
collection: ansible
version: "6"
title: "community.aws.rds_subnet_group module – manage RDS database subnet groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/rds_subnet_group_module.html
fetched_at: 2026-07-27T17:04:55+00:00
---
# community.aws.rds_subnet_group module – manage RDS database subnet groups

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/community/aws) (version 3.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](rds_subnet_group_module.md#ansible-collections-community-aws-rds-subnet-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.rds_subnet_group`.

New in community.aws 1.0.0

- [Synopsis](rds_subnet_group_module.md#synopsis)
- [Requirements](rds_subnet_group_module.md#requirements)
- [Parameters](rds_subnet_group_module.md#parameters)
- [Notes](rds_subnet_group_module.md#notes)
- [Examples](rds_subnet_group_module.md#examples)
- [Return Values](rds_subnet_group_module.md#return-values)

## [Synopsis](rds_subnet_group_module.md#id1)

- Creates, modifies, and deletes RDS database subnet groups.

## [Requirements](rds_subnet_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](rds_subnet_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Database subnet group description.  Required when *state=present*. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string / required | Database subnet group identifier. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in community.aws 3.2.0 | Whether or not to remove tags assigned to the RDS subnet group if not specified in the playbook.  To remove all tags set *tags* to an empty dictionary in conjunction with this.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Specifies whether the subnet should be present or absent.  Choices:   - `"present"` - `"absent"` |
| **subnets**  list / elements=string | List of subnet IDs that make up the database subnet group.  Required when *state=present*. |
| **tags**  dictionary  added in community.aws 3.2.0 | A hash/dictionary of tags to add to the new RDS subnet group or to add/remove from an existing one. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](rds_subnet_group_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](rds_subnet_group_module.md#id5)

```yaml+jinja
- name: Add or change a subnet group
  community.aws.rds_subnet_group:
    state: present
    name: norwegian-blue
    description: My Fancy Ex Parrot Subnet Group
    subnets:
      - subnet-aaaaaaaa
      - subnet-bbbbbbbb

- name: Add or change a subnet group and associate tags
  community.aws.rds_subnet_group:
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
  community.aws.rds_subnet_group:
    state: absent
    name: norwegian-blue
```

## [Return Values](rds_subnet_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | True if listing the RDS subnet group succeeds.  Returned: always  Sample: `false` |
| **subnet_group**  complex | Dictionary of DB subnet group values  Returned: *state=present* |
| **db_subnet_group_arn**  string | The ARN of the DB subnet group  Returned: *state=present*  Sample: `"arn:aws:rds:eu-north-1:721066863947:subgrp:ansible-test-13950442"` |
| **db_subnet_group_description**  string | The description of the DB subnet group  Returned: *state=present*  Sample: `"Simple description."` |
| **db_subnet_group_name**  string | The name of the DB subnet group  Returned: *state=present*  Sample: `"ansible-test-mbp-13950442"` |
| **description**  string | The description of the DB subnet group (maintained for backward compatibility)  Returned: *state=present*  Sample: `"Simple description."` |
| **name**  string | The name of the DB subnet group (maintained for backward compatibility)  Returned: *state=present*  Sample: `"ansible-test-mbp-13950442"` |
| **status**  string | The status of the DB subnet group (maintained for backward compatibility)  Returned: *state=present*  Sample: `"Complete"` |
| **subnet_group_status**  string | The status of the DB subnet group  Returned: *state=present*  Sample: `"Complete"` |
| **subnet_ids**  list / elements=string | Contains a list of Subnet IDs  Returned: *state=present*  Sample: `["subnet-08c94870f4480797e"]` |
| **subnets**  list / elements=string | Contains a list of Subnet elements (@see <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rds.html#RDS.Client.describe_db_subnet_groups>)  Returned: *state=present* |
| **subnet_availability_zone**  dictionary  added in community.aws 3.2.0 | Contains Availability Zone information.  Returned: *state=present*  Sample: `{"name": "eu-north-1b"}` |
| **subnet_identifier**  string  added in community.aws 3.2.0 | The identifier of the subnet.  Returned: *state=present*  Sample: `"subnet-08c94870f4480797e"` |
| **subnet_outpost**  dictionary  added in community.aws 3.2.0 | This value specifies the Outpost.  Returned: *state=present*  Sample: `{}` |
| **subnet_status**  string  added in community.aws 3.2.0 | The status of the subnet.  Returned: *state=present*  Sample: `"Active"` |
| **tags**  dictionary  added in community.aws 3.2.0 | The tags associated with the subnet group  Returned: *state=present*  Sample: `{"tag1": "Tag1", "tag2": "Tag2"}` |
| **vpc_id**  string | The VpcId of the DB subnet group  Returned: *state=present*  Sample: `"vpc-0acb0ba033ff2119c"` |

### Authors

- Scott Anderson (@tastychutney)
- Alina Buzachis (@alinabuzachis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
