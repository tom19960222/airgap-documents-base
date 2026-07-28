---
collection: ansible
version: "6"
title: "community.aws.rds_instance_info module – obtain information about one or more RDS instances"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/rds_instance_info_module.html
fetched_at: 2026-07-27T17:04:51+00:00
---
# community.aws.rds_instance_info module – obtain information about one or more RDS instances

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
> see [Requirements](rds_instance_info_module.md#ansible-collections-community-aws-rds-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.rds_instance_info`.

New in community.aws 1.0.0

- [Synopsis](rds_instance_info_module.md#synopsis)
- [Requirements](rds_instance_info_module.md#requirements)
- [Parameters](rds_instance_info_module.md#parameters)
- [Notes](rds_instance_info_module.md#notes)
- [Examples](rds_instance_info_module.md#examples)
- [Return Values](rds_instance_info_module.md#return-values)

## [Synopsis](rds_instance_info_module.md#id1)

- Obtain information about one or more RDS instances.

## [Requirements](rds_instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](rds_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **db_instance_identifier**  aliases: id  string | The RDS instance’s unique identifier. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filters**  dictionary | A filter that specifies one or more DB instances to describe. See <https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html> |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](rds_instance_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](rds_instance_info_module.md#id5)

```yaml+jinja
- name: Get information about an instance
  community.aws.rds_instance_info:
    db_instance_identifier: new-database
  register: new_database_info

- name: Get all RDS instances
  community.aws.rds_instance_info:
```

## [Return Values](rds_instance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instances**  complex | List of RDS instances  Returned: always |
| **allocated_storage**  integer | Gigabytes of storage allocated to the database  Returned: always  Sample: `10` |
| **auto_minor_version_upgrade**  boolean | Whether minor version upgrades happen automatically  Returned: always  Sample: `true` |
| **availability_zone**  string | Availability Zone in which the database resides  Returned: always  Sample: `"us-west-2b"` |
| **backup_retention_period**  integer | Days for which backups are retained  Returned: always  Sample: `7` |
| **ca_certificate_identifier**  string | ID for the CA certificate  Returned: always  Sample: `"rds-ca-2015"` |
| **copy_tags_to_snapshot**  boolean | Whether DB tags should be copied to the snapshot  Returned: always  Sample: `false` |
| **db_instance_arn**  string | ARN of the database instance  Returned: always  Sample: `"arn:aws:rds:us-west-2:111111111111:db:helloworld-rds"` |
| **db_instance_class**  string | Instance class of the database instance  Returned: always  Sample: `"db.t2.small"` |
| **db_instance_identifier**  string | Database instance identifier  Returned: always  Sample: `"helloworld-rds"` |
| **db_instance_port**  integer | Port used by the database instance  Returned: always  Sample: `0` |
| **db_instance_status**  string | Status of the database instance  Returned: always  Sample: `"available"` |
| **db_name**  string | Name of the database  Returned: always  Sample: `"management"` |
| **db_parameter_groups**  complex | List of database parameter groups  Returned: always |
| **db_parameter_group_name**  string | Name of the database parameter group  Returned: always  Sample: `"psql-pg-helloworld"` |
| **parameter_apply_status**  string | Whether the parameter group has been applied  Returned: always  Sample: `"in-sync"` |
| **db_security_groups**  list / elements=string | List of security groups used by the database instance  Returned: always  Sample: `[]` |
| **db_subnet_group**  complex | list of subnet groups  Returned: always |
| **db_subnet_group_description**  string | Description of the DB subnet group  Returned: always  Sample: `"My database subnet group"` |
| **db_subnet_group_name**  string | Name of the database subnet group  Returned: always  Sample: `"my-subnet-group"` |
| **subnet_group_status**  string | Subnet group status  Returned: always  Sample: `"Complete"` |
| **subnets**  complex | List of subnets in the subnet group  Returned: always |
| **subnet_availability_zone**  complex | Availability zone of the subnet  Returned: always |
| **name**  string | Name of the availability zone  Returned: always  Sample: `"us-west-2c"` |
| **subnet_identifier**  string | Subnet ID  Returned: always  Sample: `"subnet-abcd1234"` |
| **subnet_status**  string | Subnet status  Returned: always  Sample: `"Active"` |
| **vpc_id**  string | VPC id of the subnet group  Returned: always  Sample: `"vpc-abcd1234"` |
| **dbi_resource_id**  string | AWS Region-unique, immutable identifier for the DB instance  Returned: always  Sample: `"db-AAAAAAAAAAAAAAAAAAAAAAAAAA"` |
| **deletion_protection**  boolean  added in community.aws 3.3.0 | `True` if the DB instance has deletion protection enabled, `False` if not.  Returned: always  Sample: `false` |
| **domain_memberships**  list / elements=string | List of domain memberships  Returned: always  Sample: `[]` |
| **endpoint**  complex | Database endpoint  Returned: always |
| **address**  string | Database endpoint address  Returned: always  Sample: `"helloworld-rds.ctrqpe3so1sf.us-west-2.rds.amazonaws.com"` |
| **hosted_zone_id**  string | Route53 hosted zone ID  Returned: always  Sample: `"Z1PABCD0000000"` |
| **port**  integer | Database endpoint port  Returned: always  Sample: `5432` |
| **engine**  string | Database engine  Returned: always  Sample: `"postgres"` |
| **engine_version**  string | Database engine version  Returned: always  Sample: `"9.5.10"` |
| **iam_database_authentication_enabled**  boolean | Whether database authentication through IAM is enabled  Returned: always  Sample: `false` |
| **instance_create_time**  string | Date and time the instance was created  Returned: always  Sample: `"2017-10-10T04:00:07.434000+00:00"` |
| **iops**  integer | The Provisioned IOPS value for the DB instance.  Returned: always  Sample: `1000` |
| **kms_key_id**  string | KMS Key ID  Returned: always  Sample: `"arn:aws:kms:us-west-2:111111111111:key/abcd1234-0000-abcd-1111-0123456789ab"` |
| **latest_restorable_time**  string | Latest time to which a database can be restored with point-in-time restore  Returned: always  Sample: `"2018-05-17T00:03:56+00:00"` |
| **license_model**  string | License model  Returned: always  Sample: `"postgresql-license"` |
| **master_username**  string | Database master username  Returned: always  Sample: `"dbadmin"` |
| **monitoring_interval**  integer | Interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance  Returned: always  Sample: `0` |
| **multi_az**  boolean | Whether Multi-AZ is on  Returned: always  Sample: `false` |
| **option_group_memberships**  complex | List of option groups  Returned: always |
| **option_group_name**  string | Option group name  Returned: always  Sample: `"default:postgres-9-5"` |
| **status**  string | Status of option group  Returned: always  Sample: `"in-sync"` |
| **pending_modified_values**  complex | Modified values pending application  Returned: always |
| **performance_insights_enabled**  boolean | Whether performance insights are enabled  Returned: always  Sample: `false` |
| **preferred_backup_window**  string | Preferred backup window  Returned: always  Sample: `"04:00-05:00"` |
| **preferred_maintenance_window**  string | Preferred maintenance window  Returned: always  Sample: `"mon:05:00-mon:05:30"` |
| **publicly_accessible**  boolean | Whether the DB is publicly accessible  Returned: always  Sample: `false` |
| **read_replica_db_instance_identifiers**  list / elements=string | List of database instance read replicas  Returned: always  Sample: `[]` |
| **storage_encrypted**  boolean | Whether the storage is encrypted  Returned: always  Sample: `true` |
| **storage_type**  string | Storage type of the Database instance  Returned: always  Sample: `"gp2"` |
| **tags**  complex | Tags used by the database instance  Returned: always |
| **vpc_security_groups**  complex | List of VPC security groups  Returned: always |
| **status**  string | Status of the VPC security group  Returned: always  Sample: `"active"` |
| **vpc_security_group_id**  string | VPC Security Group ID  Returned: always  Sample: `"sg-abcd1234"` |

### Authors

- Will Thames (@willthames)
- Michael De La Rue (@mikedlr)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
