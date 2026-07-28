---
collection: ansible
version: "6"
title: "community.aws.rds_cluster module – rds_cluster module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/rds_cluster_module.html
fetched_at: 2026-07-27T17:04:49+00:00
---
# community.aws.rds_cluster module – rds_cluster module

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
> see [Requirements](rds_cluster_module.md#ansible-collections-community-aws-rds-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.rds_cluster`.

New in community.aws 3.2.0

- [Synopsis](rds_cluster_module.md#synopsis)
- [Requirements](rds_cluster_module.md#requirements)
- [Parameters](rds_cluster_module.md#parameters)
- [Notes](rds_cluster_module.md#notes)
- [Examples](rds_cluster_module.md#examples)
- [Return Values](rds_cluster_module.md#return-values)

## [Synopsis](rds_cluster_module.md#id1)

- Create, modify, and delete RDS clusters.

## [Requirements](rds_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](rds_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply_immediately**  boolean | A value that specifies whether modifying a cluster with *new_db_cluster_identifier* and *master_user_password* should be applied as soon as possible, regardless of the *preferred_maintenance_window* setting. If `false`, changes are applied during the next maintenance window.  Choices:   - `false` ← (default) - `true` |
| **availability_zones**  aliases: zones, az  list / elements=string | A list of EC2 Availability Zones that instances in the DB cluster can be created in. May be used when creating a cluster or when restoring from S3 or a snapshot. |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **backtrack_to**  string | The timestamp of the time to backtrack the DB cluster to in ISO 8601 format, such as “2017-07-08T18:00Z”. |
| **backtrack_window**  integer | The target backtrack window, in seconds. To disable backtracking, set this value to `0`.  If specified, this value must be set to a number from `0` to `259,200` (72 hours).  Default: `0` |
| **backup_retention_period**  integer | The number of days for which automated backups are retained (must be within `1` to `35`). May be used when creating a new cluster, when restoring from S3, or when modifying a cluster.  Default: `1` |
| **character_set_name**  string | The character set to associate with the DB cluster. |
| **copy_tags_to_snapshot**  boolean | Indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.  Choices:   - `false` - `true` |
| **creation_source**  string | Which source to use if creating from a template (an existing cluster, S3 bucket, or snapshot).  Choices:   - `"snapshot"` - `"s3"` - `"cluster"` |
| **database_name**  aliases: db_name  string | The name for your database. If a name is not provided Amazon RDS will not create a database. |
| **db_cluster_identifier**  aliases: cluster_id, id, cluster_name  string / required | The DB cluster (lowercase) identifier. The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens. |
| **db_cluster_parameter_group_name**  string | The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted when creating a cluster, the default DB cluster parameter group for the specified DB engine and version is used. |
| **db_subnet_group_name**  string | A DB subnet group to associate with this DB cluster if not using the default. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **deletion_protection**  boolean | A value that indicates whether the DB cluster has deletion protection enabled. The database can’t be deleted when deletion protection is enabled. By default, deletion protection is disabled.  Choices:   - `false` - `true` |
| **domain**  string | The Active Directory directory ID to create the DB cluster in. |
| **domain_iam_role_name**  string | Specify the name of the IAM role to be used when making API calls to the Directory Service. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **enable_cloudwatch_logs_exports**  list / elements=string | A list of log types that need to be enabled for exporting to CloudWatch Logs.  Engine aurora-mysql supports `audit`, `error`, `general` and `slowquery`.  Engine aurora-postgresql supports `postgresql`. |
| **enable_global_write_forwarding**  boolean | A value that indicates whether to enable this DB cluster to forward write operations to the primary cluster of an Aurora global database. By default, write operations are not allowed on Aurora DB clusters that are secondary clusters in an Aurora global database.  This value can be only set on Aurora DB clusters that are members of an Aurora global database.  Choices:   - `false` - `true` |
| **enable_http_endpoint**  boolean | A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.  Choices:   - `false` - `true` |
| **enable_iam_database_authentication**  boolean | Enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. If this option is omitted when creating the cluster, Amazon RDS sets this to `false`.  Choices:   - `false` - `true` |
| **engine**  string | The name of the database engine to be used for this DB cluster. This is required to create a cluster.  Choices:   - `"aurora"` - `"aurora-mysql"` - `"aurora-postgresql"` |
| **engine_version**  string | The version number of the database engine to use.  For Aurora MySQL that could be `5.6.10a`, `5.7.12`.  Aurora PostgreSQL example, `9.6.3`. |
| **final_snapshot_identifier**  string | The DB cluster snapshot identifier of the new DB cluster snapshot created when *skip_final_snapshot=false*. |
| **force_backtrack**  boolean | A boolean to indicate if the DB cluster should be forced to backtrack when binary logging is enabled. Otherwise, an error occurs when binary logging is enabled.  Choices:   - `false` - `true` |
| **force_update_password**  boolean | Set to `true` to update your cluster password with *master_user_password*.  Since comparing passwords to determine if it needs to be updated is not possible this is set to `false` by default to allow idempotence.  Choices:   - `false` ← (default) - `true` |
| **global_cluster_identifier**  string | The global cluster ID of an Aurora cluster that becomes the primary cluster in the new global database cluster. |
| **kms_key_id**  string | The AWS KMS key identifier (the ARN, unless you are creating a cluster in the same account that owns the KMS key, in which case the KMS key alias may be used).  If *replication_source_identifier* specifies an encrypted source Amazon RDS will use the key used toe encrypt the source.  If *storage_encrypted=true* and and *replication_source_identifier* is not provided, the default encryption key is used. |
| **master_user_password**  aliases: password  string | An 8-41 character password for the master database user.  The password can contain any printable ASCII character except “/”, “””, or “@”.  To modify the password use *force_password_update*. Use *apply immediately* to change the password immediately, otherwise it is updated during the next maintenance window. |
| **master_username**  aliases: username  string | The name of the master user for the DB cluster. Must be 1-16 letters or numbers and begin with a letter. |
| **new_db_cluster_identifier**  aliases: new_cluster_id, new_id, new_cluster_name  string | The new DB cluster (lowercase) identifier for the DB cluster when renaming a DB cluster.  The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens.  Use *apply_immediately* to rename immediately, otherwise it is updated during the next maintenance window. |
| **option_group_name**  string | The option group to associate with the DB cluster. |
| **port**  integer | The port number on which the instances in the DB cluster accept connections. If not specified, Amazon RDS defaults this to `3306` if the *engine* is `aurora` and c(5432) if the *engine* is `aurora-postgresql`. |
| **preferred_backup_window**  aliases: backup_window  string | The daily time range (in UTC) of at least 30 minutes, during which automated backups are created if automated backups are enabled using *backup_retention_period*. The option must be in the format of “hh24:mi-hh24:mi” and not conflict with *preferred_maintenance_window*. |
| **preferred_maintenance_window**  aliases: maintenance_window  string | The weekly time range (in UTC) of at least 30 minutes, during which system maintenance can occur. The option must be in the format “ddd:hh24:mi-ddd:hh24:mi” where ddd is one of Mon, Tue, Wed, Thu, Fri, Sat, Sun. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **promote**  boolean | Set to `true` to promote a read replica cluster.  Choices:   - `false` ← (default) - `true` |
| **purge_cloudwatch_logs_exports**  boolean | Whether or not to disable Cloudwatch logs enabled for the DB cluster that are not provided in *enable_cloudwatch_logs_exports*. Set *enable_cloudwatch_logs_exports* to an empty list to disable all.  Choices:   - `false` - `true` ← (default) |
| **purge_security_groups**  boolean | Set to `false` to retain any enabled security groups that aren’t specified in the task and are associated with the cluster.  Can be applied to *vpc_security_group_ids*  Choices:   - `false` - `true` ← (default) |
| **purge_tags**  boolean | Whether or not to remove tags assigned to the DB cluster if not specified in the playbook. To remove all tags set *tags* to an empty dictionary in conjunction with this.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **replication_source_identifier**  aliases: replication_src_id  string | The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica. |
| **restore_to_time**  string | The UTC date and time to restore the DB cluster to. Must be in the format “2015-03-07T23:45:00Z”.  If this is not provided while restoring a cluster, *use_latest_restorable_time* must be. May not be specified if *restore_type* is copy-on-write. |
| **restore_type**  string | The type of restore to be performed. If not provided, Amazon RDS uses full-copy.  Choices:   - `"full-copy"` - `"copy-on-write"` |
| **role_arn**  string | The Amazon Resource Name (ARN) of the IAM role to associate with the Aurora DB cluster, for example “arn:aws:iam::123456789012:role/AuroraAccessRole” |
| **s3_bucket_name**  string | The name of the Amazon S3 bucket that contains the data used to create the Amazon Aurora DB cluster. |
| **s3_ingestion_role_arn**  string | The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon RDS to access the Amazon S3 bucket on your behalf. |
| **s3_prefix**  string | The prefix for all of the file names that contain the data used to create the Amazon Aurora DB cluster.  If you do not specify a SourceS3Prefix value, then the Amazon Aurora DB cluster is created by using all of the files in the Amazon S3 bucket. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **skip_final_snapshot**  boolean | Whether a final DB cluster snapshot is created before the DB cluster is deleted.  If this is `false`, *final_snapshot_identifier* must be provided.  Choices:   - `false` ← (default) - `true` |
| **snapshot_identifier**  string | The identifier for the DB snapshot or DB cluster snapshot to restore from.  You can use either the name or the ARN to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot. |
| **source_db_cluster_identifier**  string | The identifier of the source DB cluster from which to restore. |
| **source_engine**  string | The identifier for the database engine that was backed up to create the files stored in the Amazon S3 bucket.  Choices:   - `"mysql"` |
| **source_engine_version**  string | The version of the database that the backup files were created from. |
| **source_region**  string | The ID of the region that contains the source for the DB cluster. |
| **state**  string | Whether the snapshot should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **storage_encrypted**  boolean | Whether the DB cluster is encrypted.  Choices:   - `false` - `true` |
| **tags**  dictionary | A dictionary of key value pairs to assign the DB cluster. |
| **use_earliest_time_on_point_in_time_unavailable**  boolean | If *backtrack_to* is set to a timestamp earlier than the earliest backtrack time, this value backtracks the DB cluster to the earliest possible backtrack time. Otherwise, an error occurs.  Choices:   - `false` - `true` |
| **use_latest_restorable_time**  boolean | Whether to restore the DB cluster to the latest restorable backup time. Only one of *use_latest_restorable_time* and *restore_to_time* may be provided.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **vpc_security_group_ids**  list / elements=string | A list of EC2 VPC security groups to associate with the DB cluster. |
| **wait**  boolean | Whether to wait for the cluster to be available or deleted.  Choices:   - `false` - `true` ← (default) |

## [Notes](rds_cluster_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](rds_cluster_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.
- name: Create minimal aurora cluster in default VPC and default subnet group
  community.aws.rds_cluster:
    cluster_id: "{{ cluster_id }}"
    engine: "aurora"
    password: "{{ password }}"
    username: "{{ username }}"

- name: Add a new security group without purge
  community.aws.rds_cluster:
    id: "{{ cluster_id }}"
    state: present
    vpc_security_group_ids:
      - sg-0be17ba10c9286b0b
    purge_security_groups: false

- name: Modify password
  community.aws.rds_cluster:
    id: "{{ cluster_id }}"
    state: present
    password: "{{ new_password }}"
    force_update_password: true
    apply_immediately: true

- name: Rename the cluster
  community.aws.rds_cluster:
    engine: aurora
    password: "{{ password }}"
    username: "{{ username }}"
    cluster_id: "cluster-{{ resource_prefix }}"
    new_cluster_id: "cluster-{{ resource_prefix }}-renamed"
    apply_immediately: true

- name: Delete aurora cluster without creating a final snapshot
  community.aws.rds_cluster:
    engine: aurora
    password: "{{ password }}"
    username: "{{ username }}"
    cluster_id: "{{ cluster_id }}"
    skip_final_snapshot: True
    tags:
      Name: "cluster-{{ resource_prefix }}"
      Created_By: "Ansible_rds_cluster_integration_test"
    state: absent

- name: Restore cluster from source snapshot
  community.aws.rds_cluster:
    engine: aurora
    password: "{{ password }}"
    username: "{{ username }}"
    cluster_id: "cluster-{{ resource_prefix }}-restored"
    snapshot_identifier: "cluster-{{ resource_prefix }}-snapshot"
```

## [Return Values](rds_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **activity_stream_status**  string | The status of the database activity stream.  Returned: always  Sample: `"stopped"` |
| **allocated_storage**  integer | The allocated storage size in gigabytes. Since aurora storage size is not fixed this is always 1 for aurora database engines.  Returned: always  Sample: `1` |
| **associated_roles**  list / elements=string | A list of dictionaries of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. Each dictionary contains the role_arn and the status of the role.  Returned: always  Sample: `[]` |
| **availability_zones**  list / elements=string | The list of availability zones that instances in the DB cluster can be created in.  Returned: always  Sample: `["us-east-1c", "us-east-1a", "us-east-1e"]` |
| **backup_retention_period**  integer | The number of days for which automatic DB snapshots are retained.  Returned: always  Sample: `1` |
| **changed**  boolean | If the RDS cluster has changed.  Returned: always  Sample: `true` |
| **cluster_create_time**  string | The time in UTC when the DB cluster was created.  Returned: always  Sample: `"2018-06-29T14:08:58.491000+00:00"` |
| **copy_tags_to_snapshot**  boolean | Specifies whether tags are copied from the DB cluster to snapshots of the DB cluster.  Returned: always  Sample: `false` |
| **cross_account_clone**  boolean | Specifies whether the DB cluster is a clone of a DB cluster owned by a different Amazon Web Services account.  Returned: always  Sample: `false` |
| **db_cluster_arn**  string | The Amazon Resource Name (ARN) for the DB cluster.  Returned: always  Sample: `"arn:aws:rds:us-east-1:123456789012:cluster:rds-cluster-demo"` |
| **db_cluster_identifier**  string | The lowercase user-supplied DB cluster identifier.  Returned: always  Sample: `"rds-cluster-demo"` |
| **db_cluster_members**  list / elements=string | A list of dictionaries containing information about the instances in the cluster. Each dictionary contains the db_instance_identifier, is_cluster_writer (bool), db_cluster_parameter_group_status, and promotion_tier (int).  Returned: always  Sample: `[]` |
| **db_cluster_parameter_group**  string | The parameter group associated with the DB cluster.  Returned: always  Sample: `"default.aurora5.6"` |
| **db_cluster_resource_id**  string | The AWS Region-unique, immutable identifier for the DB cluster.  Returned: always  Sample: `"cluster-D2MEQDN3BQNXDF74K6DQJTHASU"` |
| **db_subnet_group**  string | The name of the subnet group associated with the DB Cluster.  Returned: always  Sample: `"default"` |
| **deletion_protection**  boolean | Indicates if the DB cluster has deletion protection enabled. The database can’t be deleted when deletion protection is enabled.  Returned: always  Sample: `false` |
| **domain_memberships**  list / elements=string | The Active Directory Domain membership records associated with the DB cluster.  Returned: always  Sample: `[]` |
| **earliest_restorable_time**  string | The earliest time to which a database can be restored with point-in-time restore.  Returned: always  Sample: `"2018-06-29T14:09:34.797000+00:00"` |
| **endpoint**  string | The connection endpoint for the primary instance of the DB cluster.  Returned: always  Sample: `"rds-cluster-demo.cluster-cvlrtwiennww.us-east-1.rds.amazonaws.com"` |
| **engine**  string | The database engine of the DB cluster.  Returned: always  Sample: `"aurora"` |
| **engine_mode**  string | The DB engine mode of the DB cluster.  Returned: always  Sample: `"provisioned"` |
| **engine_version**  string | The database engine version.  Returned: always  Sample: `"5.6.10a"` |
| **hosted_zone_id**  string | The ID that Amazon Route 53 assigns when you create a hosted zone.  Returned: always  Sample: `"Z2R2ITUGPM61AM"` |
| **http_endpoint_enabled**  boolean | A value that indicates whether the HTTP endpoint for an Aurora Serverless DB cluster is enabled.  Returned: always  Sample: `false` |
| **iam_database_authentication_enabled**  boolean | Whether IAM accounts may be mapped to database accounts.  Returned: always  Sample: `false` |
| **latest_restorable_time**  string | The latest time to which a database can be restored with point-in-time restore.  Returned: always  Sample: `"2018-06-29T14:09:34.797000+00:00"` |
| **master_username**  string | The master username for the DB cluster.  Returned: always  Sample: `"username"` |
| **multi_az**  boolean | Whether the DB cluster has instances in multiple availability zones.  Returned: always  Sample: `false` |
| **port**  integer | The port that the database engine is listening on.  Returned: always  Sample: `3306` |
| **preferred_backup_window**  string | The UTC weekly time range during which system maintenance can occur.  Returned: always  Sample: `"10:18-10:48"` |
| **preferred_maintenance_window**  string | The UTC weekly time range during which system maintenance can occur.  Returned: always  Sample: `"tue:03:23-tue:03:53"` |
| **read_replica_identifiers**  list / elements=string | A list of read replica ID strings associated with the DB cluster.  Returned: always  Sample: `[]` |
| **reader_endpoint**  string | The reader endpoint for the DB cluster.  Returned: always  Sample: `"rds-cluster-demo.cluster-ro-cvlrtwiennww.us-east-1.rds.amazonaws.com"` |
| **status**  string | The status of the DB cluster.  Returned: always  Sample: `"available"` |
| **storage_encrypted**  boolean | Whether the DB cluster is storage encrypted.  Returned: always  Sample: `false` |
| **tag_list**  list / elements=dictionary | A list of tags consisting of key-value pairs.  Returned: always  Sample: `[{"key": "Created_By", "value": "Ansible_rds_cluster_integration_test"}]` |
| **tags**  dictionary | A dictionary of key value pairs.  Returned: always  Sample: `{"Name": "rds-cluster-demo"}` |
| **vpc_security_groups**  complex | A list of the DB cluster’s security groups and their status.  Returned: always |
| **status**  string | Status of the security group.  Returned: always  Sample: `"active"` |
| **vpc_security_group_id**  string | Security group of the cluster.  Returned: always  Sample: `"sg-12345678"` |

### Authors

- Sloane Hertel (@s-hertel)
- Alina Buzachis (@alinabuzachis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
