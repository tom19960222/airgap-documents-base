---
collection: ansible
version: "6"
title: "community.aws.elasticache_subnet_group module – manage ElastiCache subnet groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/elasticache_subnet_group_module.html
fetched_at: 2026-07-27T17:04:26+00:00
---
# community.aws.elasticache_subnet_group module – manage ElastiCache subnet groups

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
> see [Requirements](elasticache_subnet_group_module.md#ansible-collections-community-aws-elasticache-subnet-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.elasticache_subnet_group`.

New in community.aws 1.0.0

- [Synopsis](elasticache_subnet_group_module.md#synopsis)
- [Requirements](elasticache_subnet_group_module.md#requirements)
- [Parameters](elasticache_subnet_group_module.md#parameters)
- [Notes](elasticache_subnet_group_module.md#notes)
- [Examples](elasticache_subnet_group_module.md#examples)
- [Return Values](elasticache_subnet_group_module.md#return-values)

## [Synopsis](elasticache_subnet_group_module.md#id1)

- Creates, modifies, and deletes ElastiCache subnet groups.

## [Requirements](elasticache_subnet_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](elasticache_subnet_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | ElastiCache subnet group description.  When not provided defaults to *name* on subnet group creation. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **name**  string / required | Database subnet group identifier.  This value is automatically converted to lowercase. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string | Specifies whether the subnet should be present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **subnets**  list / elements=string | List of subnet IDs that make up the ElastiCache subnet group.  At least one subnet must be provided when creating an ElastiCache subnet group. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](elasticache_subnet_group_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](elasticache_subnet_group_module.md#id5)

```yaml+jinja
- name: Add or change a subnet group
  community.aws.elasticache_subnet_group:
    state: present
    name: norwegian-blue
    description: My Fancy Ex Parrot Subnet Group
    subnets:
      - subnet-aaaaaaaa
      - subnet-bbbbbbbb

- name: Remove a subnet group
  community.aws.elasticache_subnet_group:
    state: absent
    name: norwegian-blue
```

## [Return Values](elasticache_subnet_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cache_subnet_group**  dictionary | Description of the Elasticache Subnet Group.  Returned: always |
| **arn**  string | The Amazon Resource Name (ARN) of the cache subnet group.  Returned: when the subnet group exists  Sample: `"arn:aws:elasticache:us-east-1:012345678901:subnetgroup:norwegian-blue"` |
| **description**  string | The description of the cache subnet group.  Returned: when the cache subnet group exists  Sample: `"My Fancy Ex Parrot Subnet Group"` |
| **name**  string | The name of the cache subnet group.  Returned: when the cache subnet group exists  Sample: `"norwegian-blue"` |
| **subnet_ids**  list / elements=string | The IDs of the subnets beloging to the cache subnet group.  Returned: when the cache subnet group exists  Sample: `["subnet-aaaaaaaa", "subnet-bbbbbbbb"]` |
| **vpc_id**  string | The VPC ID of the cache subnet group.  Returned: when the cache subnet group exists  Sample: `"norwegian-blue"` |

### Authors

- Tim Mahoney (@timmahoney)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
