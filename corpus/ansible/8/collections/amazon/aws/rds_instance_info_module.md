---
collection: ansible
version: "8"
title: "amazon.aws.rds_instance_info module – obtain information about one or more RDS instances"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/rds_instance_info_module.html
fetched_at: 2026-07-28T01:07:06+00:00
---
# amazon.aws.rds_instance_info module – obtain information about one or more RDS instances

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
> see [Requirements](rds_instance_info_module.md#ansible-collections-amazon-aws-rds-instance-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.rds_instance_info`.

New in amazon.aws 5.0.0

- [Synopsis](rds_instance_info_module.md#synopsis)
- [Requirements](rds_instance_info_module.md#requirements)
- [Parameters](rds_instance_info_module.md#parameters)
- [Notes](rds_instance_info_module.md#notes)
- [Examples](rds_instance_info_module.md#examples)
- [Return Values](rds_instance_info_module.md#return-values)

## [Synopsis](rds_instance_info_module.md#id1)

- Obtain information about one or more RDS instances.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](rds_instance_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](rds_instance_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **db_instance_identifier**  aliases: id  string | The RDS instance’s unique identifier. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A filter that specifies one or more DB instances to describe. See <https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html> |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](rds_instance_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](rds_instance_info_module.md#id5)

```yaml+jinja
- name: Get information about an instance
  amazon.aws.rds_instance_info:
    db_instance_identifier: new-database
  register: new_database_info

- name: Get all RDS instances
  amazon.aws.rds_instance_info:
```

## [Return Values](rds_instance_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instances**  complex | List of RDS instances  **Returned:** always |
| **allocated_storage**  integer | Gigabytes of storage allocated to the database  **Returned:** always  **Sample:** `10` |
| **auto_minor_version_upgrade**  boolean | Whether minor version upgrades happen automatically  **Returned:** always  **Sample:** `true` |
| **availability_zone**  string | Availability Zone in which the database resides  **Returned:** always  **Sample:** `"us-west-2b"` |
| **backup_retention_period**  integer | Days for which backups are retained  **Returned:** always  **Sample:** `7` |
| **ca_certificate_identifier**  string | ID for the CA certificate  **Returned:** always  **Sample:** `"rds-ca-2015"` |
| **copy_tags_to_snapshot**  boolean | Whether DB tags should be copied to the snapshot  **Returned:** always  **Sample:** `false` |
| **db_instance_arn**  string | ARN of the database instance  **Returned:** always  **Sample:** `"arn:aws:rds:us-west-2:123456789012:db:helloworld-rds"` |
| **db_instance_class**  string | Instance class of the database instance  **Returned:** always  **Sample:** `"db.t2.small"` |
| **db_instance_identifier**  string | Database instance identifier  **Returned:** always  **Sample:** `"helloworld-rds"` |
| **db_instance_port**  integer | Port used by the database instance  **Returned:** always  **Sample:** `0` |
| **db_instance_status**  string | Status of the database instance  **Returned:** always  **Sample:** `"available"` |
| **db_name**  string | Name of the database  **Returned:** always  **Sample:** `"management"` |
| **db_parameter_groups**  complex | List of database parameter groups  **Returned:** always |
| **db_parameter_group_name**  string | Name of the database parameter group  **Returned:** always  **Sample:** `"psql-pg-helloworld"` |
| **parameter_apply_status**  string | Whether the parameter group has been applied  **Returned:** always  **Sample:** `"in-sync"` |
| **db_security_groups**  list / elements=string | List of security groups used by the database instance  **Returned:** always  **Sample:** `[]` |
| **db_subnet_group**  complex | list of subnet groups  **Returned:** always |
| **db_subnet_group_description**  string | Description of the DB subnet group  **Returned:** always  **Sample:** `"My database subnet group"` |
| **db_subnet_group_name**  string | Name of the database subnet group  **Returned:** always  **Sample:** `"my-subnet-group"` |
| **subnet_group_status**  string | Subnet group status  **Returned:** always  **Sample:** `"Complete"` |
| **subnets**  complex | List of subnets in the subnet group  **Returned:** always |
| **subnet_availability_zone**  complex | Availability zone of the subnet  **Returned:** always |
| **name**  string | Name of the availability zone  **Returned:** always  **Sample:** `"us-west-2c"` |
| **subnet_identifier**  string | Subnet ID  **Returned:** always  **Sample:** `"subnet-abcd1234"` |
| **subnet_status**  string | Subnet status  **Returned:** always  **Sample:** `"Active"` |
| **vpc_id**  string | VPC id of the subnet group  **Returned:** always  **Sample:** `"vpc-abcd1234"` |
| **dbi_resource_id**  string | AWS Region-unique, immutable identifier for the DB instance  **Returned:** always  **Sample:** `"db-AAAAAAAAAAAAAAAAAAAAAAAAAA"` |
| **deletion_protection**  boolean  *added in community.aws 3.3.0* | `True` if the DB instance has deletion protection enabled, `False` if not.  **Returned:** always  **Sample:** `false` |
| **domain_memberships**  list / elements=string | List of domain memberships  **Returned:** always  **Sample:** `[]` |
| **endpoint**  complex | Database endpoint  **Returned:** always |
| **address**  string | Database endpoint address  **Returned:** always  **Sample:** `"helloworld-rds.ctrqpe3so1sf.us-west-2.rds.amazonaws.com"` |
| **hosted_zone_id**  string | Route53 hosted zone ID  **Returned:** always  **Sample:** `"Z1PABCD0000000"` |
| **port**  integer | Database endpoint port  **Returned:** always  **Sample:** `5432` |
| **engine**  string | Database engine  **Returned:** always  **Sample:** `"postgres"` |
| **engine_version**  string | Database engine version  **Returned:** always  **Sample:** `"9.5.10"` |
| **iam_database_authentication_enabled**  boolean | Whether database authentication through IAM is enabled  **Returned:** always  **Sample:** `false` |
| **instance_create_time**  string | Date and time the instance was created  **Returned:** always  **Sample:** `"2017-10-10T04:00:07.434000+00:00"` |
| **iops**  integer | The Provisioned IOPS value for the DB instance.  **Returned:** always  **Sample:** `1000` |
| **kms_key_id**  string | KMS Key ID  **Returned:** always  **Sample:** `"arn:aws:kms:us-west-2:123456789012:key/abcd1234-0000-abcd-1111-0123456789ab"` |
| **latest_restorable_time**  string | Latest time to which a database can be restored with point-in-time restore  **Returned:** always  **Sample:** `"2018-05-17T00:03:56+00:00"` |
| **license_model**  string | License model  **Returned:** always  **Sample:** `"postgresql-license"` |
| **master_username**  string | Database master username  **Returned:** always  **Sample:** `"dbadmin"` |
| **monitoring_interval**  integer | Interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance  **Returned:** always  **Sample:** `0` |
| **multi_az**  boolean | Whether Multi-AZ is on  **Returned:** always  **Sample:** `false` |
| **option_group_memberships**  complex | List of option groups  **Returned:** always |
| **option_group_name**  string | Option group name  **Returned:** always  **Sample:** `"default:postgres-9-5"` |
| **status**  string | Status of option group  **Returned:** always  **Sample:** `"in-sync"` |
| **pending_modified_values**  complex | Modified values pending application  **Returned:** always |
| **performance_insights_enabled**  boolean | Whether performance insights are enabled  **Returned:** always  **Sample:** `false` |
| **preferred_backup_window**  string | Preferred backup window  **Returned:** always  **Sample:** `"04:00-05:00"` |
| **preferred_maintenance_window**  string | Preferred maintenance window  **Returned:** always  **Sample:** `"mon:05:00-mon:05:30"` |
| **publicly_accessible**  boolean | Whether the DB is publicly accessible  **Returned:** always  **Sample:** `false` |
| **read_replica_db_instance_identifiers**  list / elements=string | List of database instance read replicas  **Returned:** always  **Sample:** `[]` |
| **storage_encrypted**  boolean | Whether the storage is encrypted  **Returned:** always  **Sample:** `true` |
| **storage_type**  string | Storage type of the Database instance  **Returned:** always  **Sample:** `"gp2"` |
| **tags**  complex | Tags used by the database instance  **Returned:** always |
| **vpc_security_groups**  complex | List of VPC security groups  **Returned:** always |
| **status**  string | Status of the VPC security group  **Returned:** always  **Sample:** `"active"` |
| **vpc_security_group_id**  string | VPC Security Group ID  **Returned:** always  **Sample:** `"sg-abcd1234"` |

### Authors

- Will Thames (@willthames)
- Michael De La Rue (@mikedlr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
