---
collection: ansible
version: "6"
title: "community.aws.rds_option_group module – rds_option_group module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/rds_option_group_module.html
fetched_at: 2026-07-27T17:04:52+00:00
---
# community.aws.rds_option_group module – rds_option_group module

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
> see [Requirements](rds_option_group_module.md#ansible-collections-community-aws-rds-option-group-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.rds_option_group`.

New in community.aws 2.1.0

- [Synopsis](rds_option_group_module.md#synopsis)
- [Requirements](rds_option_group_module.md#requirements)
- [Parameters](rds_option_group_module.md#parameters)
- [Notes](rds_option_group_module.md#notes)
- [Examples](rds_option_group_module.md#examples)
- [Return Values](rds_option_group_module.md#return-values)

## [Synopsis](rds_option_group_module.md#id1)

- Manages the creation, modification, deletion of RDS option groups.

## [Requirements](rds_option_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](rds_option_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply_immediately**  boolean | Indicates whether the changes should be applied immediately, or during the next maintenance window.  Choices:   - `false` ← (default) - `true` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **engine_name**  string | Specifies the name of the engine that this option group should be associated with. |
| **major_engine_version**  string | Specifies the major version of the engine that this option group should be associated with. |
| **option_group_description**  string | The description of the option group. |
| **option_group_name**  string / required | Specifies the name of the option group to be created. |
| **options**  list / elements=dictionary | Options in this list are added to the option group.  If already present, the specified configuration is used to update the existing configuration.  If none are supplied, any existing options are removed. |
| **db_security_group_memberships**  list / elements=string | A list of `DBSecurityGroupMembership` name strings used for this option. |
| **option_name**  string | The configuration of options to include in a group. |
| **option_settings**  list / elements=dictionary | The option settings to include in an option group. |
| **allowed_values**  string | The allowed values of the option setting. |
| **apply_type**  string | The DB engine specific parameter type. |
| **data_type**  string | The data type of the option setting. |
| **default_value**  string | The default value of the option setting. |
| **description**  string | The description of the option setting. |
| **is_collection**  boolean | Indicates if the option setting is part of a collection.  Choices:   - `false` - `true` |
| **is_modifiable**  boolean | A Boolean value that, when `true`, indicates the option setting can be modified from the default.  Choices:   - `false` - `true` |
| **name**  string | The name of the option that has settings that you can set. |
| **value**  string | The current value of the option setting. |
| **option_version**  string | The version for the option. |
| **port**  integer | The optional port for the option. |
| **vpc_security_group_memberships**  list / elements=string | A list of `VpcSecurityGroupMembership` name strings used for this option. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | Remove tags not listed in *tags*.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **state**  string / required | Specifies whether the option group should be `present` or `absent`.  Choices:   - `"present"` - `"absent"` |
| **tags**  dictionary | A dictionary of key value pairs to assign the option group.  To remove all tags set *tags={}* and *purge_tags=true*. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Whether to wait for the cluster to be available or deleted.  Choices:   - `false` - `true` ← (default) |

## [Notes](rds_option_group_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](rds_option_group_module.md#id5)

```yaml+jinja
# Create an RDS Mysql Option group
- name: Create an RDS Mysql option group
  community.aws.rds_option_group:
    state: present
    option_group_name: test-mysql-option-group
    engine_name: mysql
    major_engine_version: 5.6
    option_group_description: test mysql option group
    apply_immediately: true
    options:
        - option_name: MEMCACHED
          port: 11211
          vpc_security_group_memberships:
            - "sg-d188c123"
          option_settings:
            - name: MAX_SIMULTANEOUS_CONNECTIONS
              value: "20"
            - name: CHUNK_SIZE_GROWTH_FACTOR
              value: "1.25"
  register: new_rds_mysql_option_group

# Remove currently configured options for an option group by removing options argument
- name: Create an RDS Mysql option group
  community.aws.rds_option_group:
    state: present
    option_group_name: test-mysql-option-group
    engine_name: mysql
    major_engine_version: 5.6
    option_group_description: test mysql option group
    apply_immediately: true
  register: rds_mysql_option_group

- name: Create an RDS Mysql option group using tags
  community.aws.rds_option_group:
    state: present
    option_group_name: test-mysql-option-group
    engine_name: mysql
    major_engine_version: 5.6
    option_group_description: test mysql option group
    apply_immediately: true
    tags:
        Tag1: tag1
        Tag2: tag2
  register: rds_mysql_option_group

# Delete an RDS Mysql Option group
- name: Delete an RDS Mysql option group
  community.aws.rds_option_group:
    state: absent
    option_group_name: test-mysql-option-group
  register: deleted_rds_mysql_option_group
```

## [Return Values](rds_option_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allows_vpc_and_non_vpc_instance_memberships**  boolean | Indicates whether this option group can be applied to both VPC and non-VPC instances.  Returned: always  Sample: `false` |
| **changed**  boolean | If the Option Group has changed.  Returned: always  Sample: `true` |
| **engine_name**  string | Indicates the name of the engine that this option group can be applied to.  Returned: always  Sample: `"mysql"` |
| **major_engine_version**  string | Indicates the major engine version associated with this option group.  Returned: always  Sample: `"5.6"` |
| **option_group_arn**  string | The Amazon Resource Name (ARN) for the option group.  Returned: always  Sample: `"arn:aws:rds:ap-southeast-2:721066863947:og:ansible-test-option-group"` |
| **option_group_description**  string | Provides a description of the option group.  Returned: always  Sample: `"test mysql option group"` |
| **option_group_name**  string | Specifies the name of the option group.  Returned: always  Sample: `"test-mysql-option-group"` |
| **options**  list / elements=dictionary | Indicates what options are available in the option group.  Returned: always |
| **db_security_group_memberships**  list / elements=dictionary | If the option requires access to a port, then this DB security group allows access to the port.  Returned: always |
| **db_security_group_name**  string | The name of the DB security group.  Returned: always  Sample: `"mydbsecuritygroup"` |
| **status**  string | The status of the DB security group.  Returned: always  Sample: `"available"` |
| **option_description**  string | The description of the option.  Returned: always  Sample: `"Innodb Memcached for MySQL"` |
| **option_name**  string | The name of the option.  Returned: always  Sample: `"MEMCACHED"` |
| **option_settings**  list / elements=string | The name of the option.  Returned: always |
| **allowed_values**  string | The allowed values of the option setting.  Returned: always  Sample: `"1-2048"` |
| **apply_type**  string | The DB engine specific parameter type.  Returned: always  Sample: `"STATIC"` |
| **data_type**  string | The data type of the option setting.  Returned: always  Sample: `"INTEGER"` |
| **default_value**  string | The default value of the option setting.  Returned: always  Sample: `"1024"` |
| **description**  string | The description of the option setting.  Returned: always  Sample: `"Verbose level for memcached."` |
| **is_collection**  boolean | Indicates if the option setting is part of a collection.  Returned: always  Sample: `true` |
| **is_modifiable**  boolean | A Boolean value that, when true, indicates the option setting can be modified from the default.  Returned: always  Sample: `true` |
| **name**  string | The name of the option that has settings that you can set.  Returned: always  Sample: `"INNODB_API_ENABLE_MDL"` |
| **value**  string | The current value of the option setting.  Returned: always  Sample: `"0"` |
| **permanent**  boolean | Indicate if this option is permanent.  Returned: always  Sample: `true` |
| **persistent**  boolean | Indicate if this option is persistent.  Returned: always  Sample: `true` |
| **port**  integer | If required, the port configured for this option to use.  Returned: always  Sample: `11211` |
| **vpc_security_group_memberships**  list / elements=dictionary | If the option requires access to a port, then this VPC security group allows access to the port.  Returned: always |
| **status**  string | The status of the VPC security group.  Returned: always  Sample: `"available"` |
| **vpc_security_group_id**  string | The name of the VPC security group.  Returned: always  Sample: `"sg-0cd636a23ae76e9a4"` |
| **tags**  dictionary | The tags associated the Internet Gateway.  Returned: always  Sample: `{"Ansible": "Test"}` |
| **vpc_id**  string | If present, this option group can only be applied to instances that are in the VPC indicated by this field.  Returned: always  Sample: `"vpc-bf07e9d6"` |

### Authors

- Nick Aslanidis (@naslanidis)
- Will Thames (@willthames)
- Alina Buzachis (@alinabuzachis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
