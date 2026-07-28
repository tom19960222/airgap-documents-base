---
collection: ansible
version: "6"
title: "community.aws.rds_instance module – Manage RDS instances"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/rds_instance_module.html
fetched_at: 2026-07-27T17:04:50+00:00
---
# community.aws.rds_instance module – Manage RDS instances

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
> see [Requirements](rds_instance_module.md#ansible-collections-community-aws-rds-instance-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.rds_instance`.

New in community.aws 1.0.0

- [Synopsis](rds_instance_module.md#synopsis)
- [Requirements](rds_instance_module.md#requirements)
- [Parameters](rds_instance_module.md#parameters)
- [Notes](rds_instance_module.md#notes)
- [Examples](rds_instance_module.md#examples)
- [Return Values](rds_instance_module.md#return-values)

## [Synopsis](rds_instance_module.md#id1)

- Create, modify, and delete RDS instances.

## [Requirements](rds_instance_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](rds_instance_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allocated_storage**  integer | The amount of storage (in gibibytes) to allocate for the DB instance. |
| **allow_major_version_upgrade**  boolean | Whether to allow major version upgrades.  Choices:   - `false` - `true` |
| **apply_immediately**  boolean | A value that specifies whether modifying an instance with *new_db_instance_identifier* and *master_user_password* should be applied as soon as possible, regardless of the *preferred_maintenance_window* setting. If false, changes are applied during the next maintenance window.  Choices:   - `false` ← (default) - `true` |
| **auto_minor_version_upgrade**  boolean | Whether minor version upgrades are applied automatically to the DB instance during the maintenance window.  Choices:   - `false` - `true` |
| **availability_zone**  aliases: az, zone  string | A list of EC2 Availability Zones that the DB instance can be created in. May be used when creating an instance or when restoring from S3 or a snapshot. Mutually exclusive with *multi_az*. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **backup_retention_period**  integer | The number of days for which automated backups are retained.  When set to `0`, automated backups will be disabled. (Not applicable if the DB instance is a source to read replicas)  May be used when creating a new instance, when restoring from S3, or when modifying an instance. |
| **ca_certificate_identifier**  string | The identifier of the CA certificate for the DB instance. |
| **character_set_name**  string | The character set to associate with the DB instance. |
| **copy_tags_to_snapshot**  boolean | Whether or not to copy all tags from the DB instance to snapshots of the instance. When initially creating a DB instance the RDS API defaults this to false if unspecified.  Choices:   - `false` - `true` |
| **creation_source**  string | Which source to use if restoring from a template (an existing instance, S3 bucket, or snapshot).  Choices:   - `"snapshot"` - `"s3"` - `"instance"` |
| **db_cluster_identifier**  aliases: cluster_id  string | The DB cluster (lowercase) identifier to add the aurora DB instance to. The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens. |
| **db_instance_class**  aliases: class, instance_type  string | The compute and memory capacity of the DB instance, for example db.t2.micro. |
| **db_instance_identifier**  aliases: instance_id, id  string / required | The DB instance (lowercase) identifier. The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens. |
| **db_name**  string | The name for your database. If a name is not provided Amazon RDS will not create a database. |
| **db_parameter_group_name**  string | The name of the DB parameter group to associate with this DB instance. When creating the DB instance if this argument is omitted the default DBParameterGroup for the specified engine is used. |
| **db_security_groups**  list / elements=string | (EC2-Classic platform) A list of DB security groups to associate with this DB instance. |
| **db_snapshot_identifier**  aliases: snapshot_identifier, snapshot_id  string | The identifier or ARN of the DB snapshot to restore from when using *creation_source=snapshot*. |
| **db_subnet_group_name**  aliases: subnet_group  string | The DB subnet group name to use for the DB instance. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **deletion_protection**  boolean  added in community.aws 3.3.0 | A value that indicates whether the DB instance has deletion protection enabled. The database can’t be deleted when deletion protection is enabled. By default, deletion protection is disabled.  Choices:   - `false` - `true` |
| **domain**  string | The Active Directory Domain to restore the instance in. |
| **domain_iam_role_name**  string | The name of the IAM role to be used when making API calls to the Directory Service. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **enable_cloudwatch_logs_exports**  aliases: cloudwatch_log_exports  list / elements=string | A list of log types that need to be enabled for exporting to CloudWatch Logs. |
| **enable_iam_database_authentication**  boolean | Enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. If this option is omitted when creating the instance, Amazon RDS sets this to False.  Choices:   - `false` - `true` |
| **enable_performance_insights**  boolean | Whether to enable Performance Insights for the DB instance.  Choices:   - `false` - `true` |
| **engine**  string | The name of the database engine to be used for this DB instance. This is required to create an instance.  Choices:   - `"aurora"` - `"aurora-mysql"` - `"aurora-postgresql"` - `"mariadb"` - `"mysql"` - `"oracle-ee"` - `"oracle-ee-cdb"` - `"oracle-se2"` - `"oracle-se2-cdb"` - `"postgres"` - `"sqlserver-ee"` - `"sqlserver-se"` - `"sqlserver-ex"` - `"sqlserver-web"` |
| **engine_version**  string | The version number of the database engine to use. For Aurora MySQL that could be 5.6.10a , 5.7.12. Aurora PostgreSQL example, 9.6.3 |
| **final_db_snapshot_identifier**  aliases: final_snapshot_identifier  string | The DB instance snapshot identifier of the new DB instance snapshot created when *skip_final_snapshot* is false. |
| **force_failover**  boolean | Set to true to conduct the reboot through a MultiAZ failover.  Choices:   - `false` - `true` |
| **force_update_password**  boolean | Set to `True` to update your instance password with *master_user_password*. Since comparing passwords to determine if it needs to be updated is not possible this is set to False by default to allow idempotence.  Choices:   - `false` ← (default) - `true` |
| **iam_roles**  list / elements=dictionary  added in community.aws 3.3.0 | List of Amazon Web Services Identity and Access Management (IAM) roles to associate with DB instance. |
| **feature_name**  string / required | The name of the feature associated with the IAM role. |
| **role_arn**  string / required | The ARN of the IAM role to associate with the DB instance. |
| **iops**  integer | The Provisioned IOPS (I/O operations per second) value. Is only set when using *storage_type* is set to io1. |
| **kms_key_id**  string | The ARN of the AWS KMS key identifier for an encrypted DB instance. If you are creating a DB instance with the same AWS account that owns the KMS encryption key used to encrypt the new DB instance, then you can use the KMS key alias instead of the ARN for the KM encryption key.  If *storage_encrypted* is true and and this option is not provided, the default encryption key is used. |
| **license_model**  string | The license model for the DB instance.  Several options are license-included, bring-your-own-license, and general-public-license.  This option can also be omitted to default to an accepted value. |
| **master_user_password**  aliases: password  string | An 8-41 character password for the master database user. The password can contain any printable ASCII character except “/”, “””, or “@”. To modify the password use *force_update_password*. Use *apply immediately* to change the password immediately, otherwise it is updated during the next maintenance window. |
| **master_username**  aliases: username  string | The name of the master user for the DB instance. Must be 1-16 letters or numbers and begin with a letter. |
| **max_allocated_storage**  integer | The upper limit to which Amazon RDS can automatically scale the storage of the DB instance. |
| **monitoring_interval**  integer | The interval, in seconds, when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting metrics, specify 0. Amazon RDS defaults this to 0 if omitted when initially creating a DB instance. |
| **monitoring_role_arn**  string | The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs. |
| **multi_az**  boolean | Specifies if the DB instance is a Multi-AZ deployment. Mutually exclusive with *availability_zone*.  Choices:   - `false` - `true` |
| **new_db_instance_identifier**  aliases: new_instance_id, new_id  string | The new DB instance (lowercase) identifier for the DB instance when renaming a DB instance. The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens. Use *apply_immediately* to rename immediately, otherwise it is updated during the next maintenance window. |
| **option_group_name**  string | The option group to associate with the DB instance. |
| **performance_insights_kms_key_id**  string | The AWS KMS key identifier (ARN, name, or alias) for encryption of Performance Insights data. |
| **performance_insights_retention_period**  integer | The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731. |
| **port**  integer | The port number on which the instances accept connections. |
| **preferred_backup_window**  aliases: backup_window  string | The daily time range (in UTC) of at least 30 minutes, during which automated backups are created if automated backups are enabled using *backup_retention_period*. The option must be in the format of “hh24:mi-hh24:mi” and not conflict with *preferred_maintenance_window*. |
| **preferred_maintenance_window**  aliases: maintenance_window  string | The weekly time range (in UTC) of at least 30 minutes, during which system maintenance can occur. The option must be in the format “ddd:hh24:mi-ddd:hh24:mi” where ddd is one of Mon, Tue, Wed, Thu, Fri, Sat, Sun. |
| **processor_features**  dictionary | A dictionary of Name, Value pairs to indicate the number of CPU cores and the number of threads per core for the DB instance class of the DB instance. Names are threadsPerCore and coreCount. Set this option to an empty dictionary to use the default processor features. |
| **coreCount**  string | The number of CPU cores |
| **threadsPerCore**  string | The number of threads per core |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **promotion_tier**  string | An integer that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance. |
| **publicly_accessible**  boolean | Specifies the accessibility options for the DB instance. A value of true specifies an Internet-facing instance with a publicly resolvable DNS name, which resolves to a public IP address. A value of false specifies an internal instance with a DNS name that resolves to a private IP address.  Choices:   - `false` - `true` |
| **purge_cloudwatch_logs_exports**  boolean | Set to False to retain any enabled cloudwatch logs that aren’t specified in the task and are associated with the instance.  Choices:   - `false` - `true` ← (default) |
| **purge_iam_roles**  boolean  added in community.aws 3.3.0 | Set to `True` to remove any IAM roles that aren’t specified in the task and are associated with the instance.  Choices:   - `false` ← (default) - `true` |
| **purge_security_groups**  boolean  added in community.aws 1.5.0 | Set to False to retain any enabled security groups that aren’t specified in the task and are associated with the instance.  Can be applied to *vpc_security_group_ids* and *db_security_groups*  Choices:   - `false` - `true` ← (default) |
| **purge_tags**  boolean | Set to False to retain any tags that aren’t specified in task and are associated with the instance.  Choices:   - `false` - `true` ← (default) |
| **read_replica**  boolean | Set to `False` to promote a read replica instance or true to create one. When creating a read replica `creation_source` should be set to ‘instance’ or not provided. `source_db_instance_identifier` must be provided with this option.  Choices:   - `false` - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **restore_time**  string | If using *creation_source=instance* this indicates the UTC date and time to restore from the source instance. For example, “2009-09-07T23:45:00Z”.  May alternatively set *use_latest_restore_time=True*.  Only one of *use_latest_restorable_time* and *restore_time* may be provided. |
| **s3_bucket_name**  string | The name of the Amazon S3 bucket that contains the data used to create the Amazon DB instance. |
| **s3_ingestion_role_arn**  string | The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon RDS to access the Amazon S3 bucket on your behalf. |
| **s3_prefix**  string | The prefix for all of the file names that contain the data used to create the Amazon DB instance. If you do not specify a SourceS3Prefix value, then the Amazon DB instance is created by using all of the files in the Amazon S3 bucket. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **skip_final_snapshot**  boolean | Whether a final DB instance snapshot is created before the DB instance is deleted. If this is false *final_db_snapshot_identifier* must be provided.  Choices:   - `false` ← (default) - `true` |
| **source_db_instance_identifier**  string | The identifier or ARN of the source DB instance from which to restore when creating a read replica or spinning up a point-in-time DB instance using *creation_source=instance*. If the source DB is not in the same region this should be an ARN. |
| **source_engine**  string | The identifier for the database engine that was backed up to create the files stored in the Amazon S3 bucket.  Choices:   - `"mysql"` |
| **source_engine_version**  string | The version of the database that the backup files were created from. |
| **source_region**  string | The region of the DB instance from which the replica is created. |
| **state**  string | Whether the snapshot should exist or not. *rebooted* is not idempotent and will leave the DB instance in a running state and start it prior to rebooting if it was stopped. *present* will leave the DB instance in the current running/stopped state, (running if creating the DB instance).  *state=running* and *state=started* are synonyms, as are *state=rebooted* and *state=restarted*. Note - rebooting the instance is not idempotent.  Choices:   - `"present"` ← (default) - `"absent"` - `"terminated"` - `"running"` - `"started"` - `"stopped"` - `"rebooted"` - `"restarted"` |
| **storage_encrypted**  boolean | Whether the DB instance is encrypted.  Choices:   - `false` - `true` |
| **storage_type**  string | The storage type to be associated with the DB instance. *storage_type* does not apply to Aurora DB instances.  Choices:   - `"standard"` - `"gp2"` - `"io1"` |
| **tags**  dictionary | A dictionary of key value pairs to assign the DB instance. |
| **tde_credential_arn**  aliases: transparent_data_encryption_arn  string | The ARN from the key store with which to associate the instance for Transparent Data Encryption. This is supported by Oracle or SQL Server DB instances and may be used in conjunction with `storage_encrypted` though it might slightly affect the performance of your database. |
| **tde_credential_password**  aliases: transparent_data_encryption_password  string | The password for the given ARN from the key store in order to access the device. |
| **timezone**  string | The time zone of the DB instance. |
| **use_latest_restorable_time**  aliases: restore_from_latest  boolean | Whether to restore the DB instance to the latest restorable backup time.  Only one of *use_latest_restorable_time* and *restore_time* may be provided.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_security_group_ids**  list / elements=string | A list of EC2 VPC security groups to associate with the DB instance. |
| **wait**  boolean | Whether to wait for the instance to be available, stopped, or deleted. At a later time a *wait_timeout* option may be added. Following each API call to create/modify/delete the instance a waiter is used with a 60 second delay 30 times until the instance reaches the expected state (available/stopped/deleted). The total task time may also be influenced by AWSRetry which helps stabilize if the instance is in an invalid state to operate on to begin with (such as if you try to stop it when it is in the process of rebooting). If setting this to False task retries and delays may make your playbook execution better handle timeouts for major modifications.  Choices:   - `false` - `true` ← (default) |

## [Notes](rds_instance_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](rds_instance_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.
- name: create minimal aurora instance in default VPC and default subnet group
  community.aws.rds_instance:
    engine: aurora
    db_instance_identifier: ansible-test-aurora-db-instance
    instance_type: db.t2.small
    password: "{{ password }}"
    username: "{{ username }}"
    cluster_id: ansible-test-cluster  # This cluster must exist - see rds_cluster to manage it

- name: Create a DB instance using the default AWS KMS encryption key
  community.aws.rds_instance:
    id: test-encrypted-db
    state: present
    engine: mariadb
    storage_encrypted: True
    db_instance_class: db.t2.medium
    username: "{{ username }}"
    password: "{{ password }}"
    allocated_storage: "{{ allocated_storage }}"

- name: remove the DB instance without a final snapshot
  community.aws.rds_instance:
    id: "{{ instance_id }}"
    state: absent
    skip_final_snapshot: True

- name: remove the DB instance with a final snapshot
  community.aws.rds_instance:
    id: "{{ instance_id }}"
    state: absent
    final_snapshot_identifier: "{{ snapshot_id }}"

- name: Add a new security group without purge
  community.aws.rds_instance:
    id: "{{ instance_id }}"
    state: present
    vpc_security_group_ids:
      - sg-0be17ba10c9286b0b
    purge_security_groups: false
  register: result

# Add IAM role to db instance
- name: Create IAM policy
  community.aws.iam_managed_policy:
    policy_name: "my-policy"
    policy: "{{ lookup('file','files/policy.json') }}"
    state: present
  register: iam_policy

- name: Create IAM role
  community.aws.iam_role:
    assume_role_policy_document: "{{ lookup('file','files/assume_policy.json') }}"
    name: "my-role"
    state: present
    managed_policy: "{{ iam_policy.policy.arn }}"
  register: iam_role

- name: Create DB instance with added IAM role
  community.aws.rds_instance:
    id: "my-instance-id"
    state: present
    engine: postgres
    engine_version: 14.2
    username: "{{ username }}"
    password: "{{ password }}"
    db_instance_class: db.m6g.large
    allocated_storage: "{{ allocated_storage }}"
    iam_roles:
      - role_arn: "{{ iam_role.arn }}"
        feature_name: 's3Export'

- name: Remove IAM role from DB instance
  community.aws.rds_instance:
    id: "my-instance-id"
    state: present
    purge_iam_roles: yes

# Restore DB instance from snapshot
- name: Create a snapshot and wait until completion
  community.aws.rds_instance_snapshot:
    instance_id: 'my-instance-id'
    snapshot_id: 'my-new-snapshot'
    state: present
    wait: yes
  register: snapshot

- name: Restore DB from snapshot
  community.aws.rds_instance:
    id: 'my-restored-db'
    creation_source: snapshot
    snapshot_identifier: 'my-new-snapshot'
    engine: mariadb
    state: present
  register: restored_db
```

## [Return Values](rds_instance_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocated_storage**  integer | The allocated storage size in gigabytes. This is always 1 for aurora database engines.  Returned: always  Sample: `20` |
| **associated_roles**  list / elements=string | The list of currently associated roles.  Returned: always  Sample: `[]` |
| **auto_minor_version_upgrade**  boolean | Whether minor engine upgrades are applied automatically to the DB instance during the maintenance window.  Returned: always  Sample: `true` |
| **availability_zone**  string | The availability zone for the DB instance.  Returned: always  Sample: `"us-east-1f"` |
| **backup_retention_period**  integer | The number of days for which automated backups are retained.  Returned: always  Sample: `1` |
| **ca_certificate_identifier**  string | The identifier of the CA certificate for the DB instance.  Returned: always  Sample: `"rds-ca-2015"` |
| **copy_tags_to_snapshot**  boolean | Whether tags are copied from the DB instance to snapshots of the DB instance.  Returned: always  Sample: `false` |
| **db_instance_arn**  string | The Amazon Resource Name (ARN) for the DB instance.  Returned: always  Sample: `"arn:aws:rds:us-east-1:123456789012:db:ansible-test"` |
| **db_instance_class**  string | The name of the compute and memory capacity class of the DB instance.  Returned: always  Sample: `"db.m4.large"` |
| **db_instance_identifier**  string | The identifier of the DB instance  Returned: always  Sample: `"ansible-test"` |
| **db_instance_port**  integer | The port that the DB instance listens on.  Returned: always  Sample: `0` |
| **db_instance_status**  string | The current state of this database.  Returned: always  Sample: `"stopped"` |
| **db_parameter_groups**  complex | The list of DB parameter groups applied to this DB instance.  Returned: always |
| **db_parameter_group_name**  string | The name of the DP parameter group.  Returned: always  Sample: `"default.mariadb10.0"` |
| **parameter_apply_status**  string | The status of parameter updates.  Returned: always  Sample: `"in-sync"` |
| **db_security_groups**  list / elements=string | A list of DB security groups associated with this DB instance.  Returned: always  Sample: `[]` |
| **db_subnet_group**  complex | The subnet group associated with the DB instance.  Returned: always |
| **db_subnet_group_description**  string | The description of the DB subnet group.  Returned: always  Sample: `"default"` |
| **db_subnet_group_name**  string | The name of the DB subnet group.  Returned: always  Sample: `"default"` |
| **subnet_group_status**  string | The status of the DB subnet group.  Returned: always  Sample: `"Complete"` |
| **subnets**  complex | A list of Subnet elements.  Returned: always |
| **subnet_availability_zone**  complex | The availability zone of the subnet.  Returned: always |
| **name**  string | The name of the Availability Zone.  Returned: always  Sample: `"us-east-1c"` |
| **subnet_identifier**  string | The ID of the subnet.  Returned: always  Sample: `"subnet-12345678"` |
| **subnet_status**  string | The status of the subnet.  Returned: always  Sample: `"Active"` |
| **vpc_id**  string | The VpcId of the DB subnet group.  Returned: always  Sample: `"vpc-12345678"` |
| **dbi_resource_id**  string | The AWS Region-unique, immutable identifier for the DB instance.  Returned: always  Sample: `"db-UHV3QRNWX4KB6GALCIGRML6QFA"` |
| **deletion_protection**  boolean  added in community.aws 3.3.0 | `True` if the DB instance has deletion protection enabled, `False` if not.  Returned: always  Sample: `false` |
| **domain_memberships**  list / elements=string | The Active Directory Domain membership records associated with the DB instance.  Returned: always  Sample: `[]` |
| **endpoint**  complex | The connection endpoint.  Returned: always |
| **address**  string | The DNS address of the DB instance.  Returned: always  Sample: `"ansible-test.cvlrtwiennww.us-east-1.rds.amazonaws.com"` |
| **hosted_zone_id**  string | The ID that Amazon Route 53 assigns when you create a hosted zone.  Returned: always  Sample: `"ZTR2ITUGPA61AM"` |
| **port**  integer | The port that the database engine is listening on.  Returned: always  Sample: `3306` |
| **engine**  string | The database engine version.  Returned: always  Sample: `"mariadb"` |
| **engine_version**  string | The database engine version.  Returned: always  Sample: `"10.0.35"` |
| **iam_database_authentication_enabled**  boolean | Whether mapping of AWS Identity and Access Management (IAM) accounts to database accounts is enabled.  Returned: always  Sample: `false` |
| **instance_create_time**  string | The date and time the DB instance was created.  Returned: always  Sample: `"2018-07-04T16:48:35.332000+00:00"` |
| **kms_key_id**  string | The AWS KMS key identifier for the encrypted DB instance when storage_encrypted is true.  Returned: When storage_encrypted is true  Sample: `"arn:aws:kms:us-east-1:123456789012:key/70c45553-ad2e-4a85-9f14-cfeb47555c33"` |
| **latest_restorable_time**  string | The latest time to which a database can be restored with point-in-time restore.  Returned: always  Sample: `"2018-07-04T16:50:50.642000+00:00"` |
| **license_model**  string | The License model information for this DB instance.  Returned: always  Sample: `"general-public-license"` |
| **master_username**  string | The master username for the DB instance.  Returned: always  Sample: `"test"` |
| **max_allocated_storage**  integer | The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.  Returned: When max allocated storage is present.  Sample: `100` |
| **monitoring_interval**  integer | The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. 0 means collecting Enhanced Monitoring metrics is disabled.  Returned: always  Sample: `0` |
| **multi_az**  boolean | Whether the DB instance is a Multi-AZ deployment.  Returned: always  Sample: `false` |
| **option_group_memberships**  complex | The list of option group memberships for this DB instance.  Returned: always |
| **option_group_name**  string | The name of the option group that the instance belongs to.  Returned: always  Sample: `"default:mariadb-10-0"` |
| **status**  string | The status of the DB instance’s option group membership.  Returned: always  Sample: `"in-sync"` |
| **pending_modified_values**  complex | The changes to the DB instance that are pending.  Returned: always |
| **performance_insights_enabled**  boolean | True if Performance Insights is enabled for the DB instance, and otherwise false.  Returned: always  Sample: `false` |
| **preferred_backup_window**  string | The daily time range during which automated backups are created if automated backups are enabled.  Returned: always  Sample: `"07:01-07:31"` |
| **preferred_maintenance_window**  string | The weekly time range (in UTC) during which system maintenance can occur.  Returned: always  Sample: `"sun:09:31-sun:10:01"` |
| **publicly_accessible**  boolean | True for an Internet-facing instance with a publicly resolvable DNS name, False to indicate an internal instance with a DNS name that resolves to a private IP address.  Returned: always  Sample: `true` |
| **read_replica_db_instance_identifiers**  list / elements=string | Identifiers of the Read Replicas associated with this DB instance.  Returned: always  Sample: `[]` |
| **storage_encrypted**  boolean | Whether the DB instance is encrypted.  Returned: always  Sample: `false` |
| **storage_type**  string | The storage type to be associated with the DB instance.  Returned: always  Sample: `"standard"` |
| **tags**  complex | A dictionary of tags associated with the DB instance.  Returned: always |
| **vpc_security_groups**  complex | A list of VPC security group elements that the DB instance belongs to.  Returned: always |
| **status**  string | The status of the VPC security group.  Returned: always  Sample: `"active"` |
| **vpc_security_group_id**  string | The name of the VPC security group.  Returned: always  Sample: `"sg-12345678"` |

### Authors

- Sloane Hertel (@s-hertel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
