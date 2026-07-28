---
collection: ansible
version: "8"
title: "amazon.aws.rds_cluster module – rds_cluster module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/rds_cluster_module.html
fetched_at: 2026-07-28T01:07:02+00:00
---
# amazon.aws.rds_cluster module – rds_cluster module

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
> see [Requirements](rds_cluster_module.md#ansible-collections-amazon-aws-rds-cluster-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.rds_cluster`.

New in amazon.aws 5.0.0

- [Synopsis](rds_cluster_module.md#synopsis)
- [Requirements](rds_cluster_module.md#requirements)
- [Parameters](rds_cluster_module.md#parameters)
- [Notes](rds_cluster_module.md#notes)
- [Examples](rds_cluster_module.md#examples)
- [Return Values](rds_cluster_module.md#return-values)

## [Synopsis](rds_cluster_module.md#id1)

- Create, modify, and delete RDS clusters.
- This module was originally added to `community.aws` in release 3.2.0.

## [Requirements](rds_cluster_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](rds_cluster_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **allocated_storage**  integer  *added in amazon.aws 5.5.0* | The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.  This setting is required to create a Multi-AZ DB cluster.  *allocated_storage* require botocore >= 1.23.44. |
| **apply_immediately**  boolean | A value that specifies whether modifying a cluster with *new_db_cluster_identifier* and *master_user_password* should be applied as soon as possible, regardless of the *preferred_maintenance_window* setting. If `false`, changes are applied during the next maintenance window.  **Choices:**   - `false` ← (default) - `true` |
| **availability_zones**  aliases: zones, az  list / elements=string | A list of EC2 Availability Zones that instances in the DB cluster can be created in. May be used when creating a cluster or when restoring from S3 or a snapshot. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **backtrack_to**  string | The timestamp of the time to backtrack the DB cluster to in ISO 8601 format, such as “2017-07-08T18:00Z”. |
| **backtrack_window**  integer | The target backtrack window, in seconds. To disable backtracking, set this value to `0`.  If specified, this value must be set to a number from `0` to `259,200` (72 hours). |
| **backup_retention_period**  integer | The number of days for which automated backups are retained (must be within `1` to `35`). May be used when creating a new cluster, when restoring from S3, or when modifying a cluster.  **Default:** `1` |
| **character_set_name**  string | The character set to associate with the DB cluster. |
| **copy_tags_to_snapshot**  boolean | Indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.  **Choices:**   - `false` - `true` |
| **creation_source**  string | Which source to use if creating from a template (an existing cluster, S3 bucket, or snapshot).  **Choices:**   - `"snapshot"` - `"s3"` - `"cluster"` |
| **database_name**  aliases: db_name  string | The name for your database. If a name is not provided Amazon RDS will not create a database. |
| **db_cluster_identifier**  aliases: cluster_id, id, cluster_name  string / required | The DB cluster (lowercase) identifier. The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens. |
| **db_cluster_instance_class**  string  *added in amazon.aws 5.5.0* | The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example `db.m6gd.xlarge`.  Not all DB instance classes are available in all Amazon Web Services Regions, or for all database engines.  For the full list of DB instance classes and availability for your engine visit <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html>.  This setting is required to create a Multi-AZ DB cluster.  *db_cluster_instance_class* require botocore >= 1.23.44. |
| **db_cluster_parameter_group_name**  string | The name of the DB cluster parameter group to associate with this DB cluster. If this argument is omitted when creating a cluster, the default DB cluster parameter group for the specified DB engine and version is used. |
| **db_subnet_group_name**  string | A DB subnet group to associate with this DB cluster if not using the default. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **deletion_protection**  boolean | A value that indicates whether the DB cluster has deletion protection enabled. The database can’t be deleted when deletion protection is enabled. By default, deletion protection is disabled.  **Choices:**   - `false` - `true` |
| **domain**  string | The Active Directory directory ID to create the DB cluster in. |
| **domain_iam_role_name**  string | Specify the name of the IAM role to be used when making API calls to the Directory Service. |
| **enable_cloudwatch_logs_exports**  list / elements=string | A list of log types that need to be enabled for exporting to CloudWatch Logs.  Engine aurora-mysql supports `audit`, `error`, `general` and `slowquery`.  Engine aurora-postgresql supports `postgresql`. |
| **enable_global_write_forwarding**  boolean | A value that indicates whether to enable this DB cluster to forward write operations to the primary cluster of an Aurora global database. By default, write operations are not allowed on Aurora DB clusters that are secondary clusters in an Aurora global database.  This value can be only set on Aurora DB clusters that are members of an Aurora global database.  **Choices:**   - `false` - `true` |
| **enable_http_endpoint**  boolean | A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.  **Choices:**   - `false` - `true` |
| **enable_iam_database_authentication**  boolean | Enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. If this option is omitted when creating the cluster, Amazon RDS sets this to `false`.  **Choices:**   - `false` - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **engine**  string | The name of the database engine to be used for this DB cluster. This is required to create a cluster.  The combinaison of *engine* and *engine_mode* may not be supported.  See AWS documentation for details: [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html).  When *engine=mysql*, *allocated_storage*, *iops* and *db_cluster_instance_class* must also be specified.  When *engine=postgres*, *allocated_storage*, *iops* and *db_cluster_instance_class* must also be specified.  Support for `postgres` and `mysql` was added in amazon.aws 5.5.0.  **Choices:**   - `"aurora"` - `"aurora-mysql"` - `"aurora-postgresql"` - `"mysql"` - `"postgres"` |
| **engine_mode**  string  *added in amazon.aws 5.5.0* | The DB engine mode of the DB cluster. The combination of *engine* and *engine_mode* may not be supported.  See AWS documentation for details: [Amazon RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html).  **Choices:**   - `"provisioned"` - `"serverless"` - `"parallelquery"` - `"global"` - `"multimaster"` |
| **engine_version**  string | The version number of the database engine to use.  For Aurora MySQL that could be `5.6.10a`, `5.7.12`.  Aurora PostgreSQL example, `9.6.3`. |
| **final_snapshot_identifier**  string | The DB cluster snapshot identifier of the new DB cluster snapshot created when *skip_final_snapshot=false*. |
| **force_backtrack**  boolean | A boolean to indicate if the DB cluster should be forced to backtrack when binary logging is enabled. Otherwise, an error occurs when binary logging is enabled.  **Choices:**   - `false` - `true` |
| **force_update_password**  boolean | Set to `true` to update your cluster password with *master_user_password*.  Since comparing passwords to determine if it needs to be updated is not possible this is set to `false` by default to allow idempotence.  **Choices:**   - `false` ← (default) - `true` |
| **global_cluster_identifier**  string | The global cluster ID of an Aurora cluster that becomes the primary cluster in the new global database cluster. |
| **iops**  integer  *added in amazon.aws 5.5.0* | The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.  This setting is required to create a Multi-AZ DB cluster  Must be a multiple between .5 and 50 of the storage amount for the DB cluster.  *iops* require botocore >= 1.23.44. |
| **kms_key_id**  string | The AWS KMS key identifier (the ARN, unless you are creating a cluster in the same account that owns the KMS key, in which case the KMS key alias may be used).  If *replication_source_identifier* specifies an encrypted source Amazon RDS will use the key used toe encrypt the source.  If *storage_encrypted=true* and and *replication_source_identifier* is not provided, the default encryption key is used. |
| **master_user_password**  aliases: password  string | An 8-41 character password for the master database user.  The password can contain any printable ASCII character except `/`, `"`, or `@`.  To modify the password use *force_password_update*. Use *apply immediately* to change the password immediately, otherwise it is updated during the next maintenance window. |
| **master_username**  aliases: username  string | The name of the master user for the DB cluster. Must be 1-16 letters or numbers and begin with a letter. |
| **new_db_cluster_identifier**  aliases: new_cluster_id, new_id, new_cluster_name  string | The new DB cluster (lowercase) identifier for the DB cluster when renaming a DB cluster.  The identifier must contain from 1 to 63 letters, numbers, or hyphens and the first character must be a letter and may not end in a hyphen or contain consecutive hyphens.  Use *apply_immediately* to rename immediately, otherwise it is updated during the next maintenance window. |
| **option_group_name**  string | The option group to associate with the DB cluster. |
| **port**  integer | The port number on which the instances in the DB cluster accept connections. If not specified, Amazon RDS defaults this to `3306` if the *engine* is `aurora` and c(5432) if the *engine* is `aurora-postgresql`. |
| **preferred_backup_window**  aliases: backup_window  string | The daily time range (in UTC) of at least 30 minutes, during which automated backups are created if automated backups are enabled using *backup_retention_period*. The option must be in the format of “hh24:mi-hh24:mi” and not conflict with *preferred_maintenance_window*. |
| **preferred_maintenance_window**  aliases: maintenance_window  string | The weekly time range (in UTC) of at least 30 minutes, during which system maintenance can occur. The option must be in the format “ddd:hh24:mi-ddd:hh24:mi” where ddd is one of Mon, Tue, Wed, Thu, Fri, Sat, Sun. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **promote**  boolean | Set to `true` to promote a read replica cluster.  **Choices:**   - `false` ← (default) - `true` |
| **purge_cloudwatch_logs_exports**  boolean | Whether or not to disable Cloudwatch logs enabled for the DB cluster that are not provided in *enable_cloudwatch_logs_exports*. Set *enable_cloudwatch_logs_exports* to an empty list to disable all.  **Choices:**   - `false` - `true` ← (default) |
| **purge_security_groups**  boolean | Set to `false` to retain any enabled security groups that aren’t specified in the task and are associated with the cluster.  Can be applied to *vpc_security_group_ids*  **Choices:**   - `false` - `true` ← (default) |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **replication_source_identifier**  aliases: replication_src_id  string | The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica. |
| **restore_to_time**  string | The UTC date and time to restore the DB cluster to. Must be in the format “2015-03-07T23:45:00Z”.  If this is not provided while restoring a cluster, *use_latest_restorable_time* must be. May not be specified if *restore_type* is copy-on-write. |
| **restore_type**  string | The type of restore to be performed. If not provided, Amazon RDS uses full-copy.  **Choices:**   - `"full-copy"` - `"copy-on-write"` |
| **role_arn**  string | The Amazon Resource Name (ARN) of the IAM role to associate with the Aurora DB cluster, for example “arn:aws:iam::123456789012:role/AuroraAccessRole” |
| **s3_bucket_name**  string | The name of the Amazon S3 bucket that contains the data used to create the Amazon Aurora DB cluster. |
| **s3_ingestion_role_arn**  string | The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that authorizes Amazon RDS to access the Amazon S3 bucket on your behalf. |
| **s3_prefix**  string | The prefix for all of the file names that contain the data used to create the Amazon Aurora DB cluster.  If you do not specify a SourceS3Prefix value, then the Amazon Aurora DB cluster is created by using all of the files in the Amazon S3 bucket. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **skip_final_snapshot**  boolean | Whether a final DB cluster snapshot is created before the DB cluster is deleted.  If this is `false`, *final_snapshot_identifier* must be provided.  **Choices:**   - `false` ← (default) - `true` |
| **snapshot_identifier**  string | The identifier for the DB snapshot or DB cluster snapshot to restore from.  You can use either the name or the ARN to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot. |
| **source_db_cluster_identifier**  string | The identifier of the source DB cluster from which to restore. |
| **source_engine**  string | The identifier for the database engine that was backed up to create the files stored in the Amazon S3 bucket.  **Choices:**   - `"mysql"` |
| **source_engine_version**  string | The version of the database that the backup files were created from. |
| **source_region**  string | The ID of the region that contains the source for the DB cluster. |
| **state**  string | Whether the snapshot should exist or not.  `started` and `stopped` can only be used with aurora clusters  Support for `started` and `stopped` was added in release 6.3.0.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"started"` - `"stopped"` |
| **storage_encrypted**  boolean | Whether the DB cluster is encrypted.  **Choices:**   - `false` - `true` |
| **storage_type**  string  *added in amazon.aws 5.5.0* | Specifies the storage type to be associated with the DB cluster.  This setting is required to create a Multi-AZ DB cluster.  When specified, a value for the *iops* parameter is required.  *storage_type* require botocore >= 1.23.44.  Defaults to `io1`.  **Choices:**   - `"io1"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **use_earliest_time_on_point_in_time_unavailable**  boolean | If *backtrack_to* is set to a timestamp earlier than the earliest backtrack time, this value backtracks the DB cluster to the earliest possible backtrack time. Otherwise, an error occurs.  **Choices:**   - `false` - `true` |
| **use_latest_restorable_time**  boolean | Whether to restore the DB cluster to the latest restorable backup time. Only one of *use_latest_restorable_time* and *restore_to_time* may be provided.  **Choices:**   - `false` - `true` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_security_group_ids**  list / elements=string | A list of EC2 VPC security groups to associate with the DB cluster. |
| **wait**  boolean | Whether to wait for the cluster to be available or deleted.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](rds_cluster_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](rds_cluster_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.
- name: Create minimal aurora cluster in default VPC and default subnet group
  amazon.aws.rds_cluster:
    cluster_id: "{{ cluster_id }}"
    engine: "aurora"
    password: "{{ password }}"
    username: "{{ username }}"

- name: Add a new security group without purge
  amazon.aws.rds_cluster:
    id: "{{ cluster_id }}"
    state: present
    vpc_security_group_ids:
      - sg-0be17ba10c9286b0b
    purge_security_groups: false

- name: Modify password
  amazon.aws.rds_cluster:
    id: "{{ cluster_id }}"
    state: present
    password: "{{ new_password }}"
    force_update_password: true
    apply_immediately: true

- name: Rename the cluster
  amazon.aws.rds_cluster:
    engine: aurora
    password: "{{ password }}"
    username: "{{ username }}"
    cluster_id: "cluster-{{ resource_prefix }}"
    new_cluster_id: "cluster-{{ resource_prefix }}-renamed"
    apply_immediately: true

- name: Delete aurora cluster without creating a final snapshot
  amazon.aws.rds_cluster:
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
  amazon.aws.rds_cluster:
    engine: aurora
    password: "{{ password }}"
    username: "{{ username }}"
    cluster_id: "cluster-{{ resource_prefix }}-restored"
    snapshot_identifier: "cluster-{{ resource_prefix }}-snapshot"

- name: Create an Aurora PostgreSQL cluster and attach an intance
  amazon.aws.rds_cluster:
    state: present
    engine: aurora-postgresql
    engine_mode: provisioned
    cluster_id: '{{ cluster_id }}'
    username: '{{ username }}'
    password: '{{ password }}'

- name: Attach a new instance to the cluster
  amazon.aws.rds_instance:
    id: '{{ instance_id }}'
    cluster_id: '{{ cluster_id }}'
    engine: aurora-postgresql
    state: present
    db_instance_class: 'db.t3.medium'
```

## [Return Values](rds_cluster_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **activity_stream_status**  string | The status of the database activity stream.  **Returned:** always  **Sample:** `"stopped"` |
| **allocated_storage**  integer | The allocated storage size in gigabytes. Since aurora storage size is not fixed this is always 1 for aurora database engines.  **Returned:** always  **Sample:** `1` |
| **associated_roles**  list / elements=string | A list of dictionaries of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. Each dictionary contains the role_arn and the status of the role.  **Returned:** always  **Sample:** `[]` |
| **availability_zones**  list / elements=string | The list of availability zones that instances in the DB cluster can be created in.  **Returned:** always  **Sample:** `["us-east-1c", "us-east-1a", "us-east-1e"]` |
| **backup_retention_period**  integer | The number of days for which automatic DB snapshots are retained.  **Returned:** always  **Sample:** `1` |
| **changed**  boolean | If the RDS cluster has changed.  **Returned:** always  **Sample:** `true` |
| **cluster_create_time**  string | The time in UTC when the DB cluster was created.  **Returned:** always  **Sample:** `"2018-06-29T14:08:58.491000+00:00"` |
| **copy_tags_to_snapshot**  boolean | Specifies whether tags are copied from the DB cluster to snapshots of the DB cluster.  **Returned:** always  **Sample:** `false` |
| **cross_account_clone**  boolean | Specifies whether the DB cluster is a clone of a DB cluster owned by a different Amazon Web Services account.  **Returned:** always  **Sample:** `false` |
| **db_cluster_arn**  string | The Amazon Resource Name (ARN) for the DB cluster.  **Returned:** always  **Sample:** `"arn:aws:rds:us-east-1:123456789012:cluster:rds-cluster-demo"` |
| **db_cluster_identifier**  string | The lowercase user-supplied DB cluster identifier.  **Returned:** always  **Sample:** `"rds-cluster-demo"` |
| **db_cluster_members**  list / elements=string | A list of dictionaries containing information about the instances in the cluster. Each dictionary contains the db_instance_identifier, is_cluster_writer (bool), db_cluster_parameter_group_status, and promotion_tier (int).  **Returned:** always  **Sample:** `[]` |
| **db_cluster_parameter_group**  string | The parameter group associated with the DB cluster.  **Returned:** always  **Sample:** `"default.aurora5.6"` |
| **db_cluster_resource_id**  string | The AWS Region-unique, immutable identifier for the DB cluster.  **Returned:** always  **Sample:** `"cluster-D2MEQDN3BQNXDF74K6DQJTHASU"` |
| **db_subnet_group**  string | The name of the subnet group associated with the DB Cluster.  **Returned:** always  **Sample:** `"default"` |
| **deletion_protection**  boolean | Indicates if the DB cluster has deletion protection enabled. The database can’t be deleted when deletion protection is enabled.  **Returned:** always  **Sample:** `false` |
| **domain_memberships**  list / elements=string | The Active Directory Domain membership records associated with the DB cluster.  **Returned:** always  **Sample:** `[]` |
| **earliest_restorable_time**  string | The earliest time to which a database can be restored with point-in-time restore.  **Returned:** always  **Sample:** `"2018-06-29T14:09:34.797000+00:00"` |
| **endpoint**  string | The connection endpoint for the primary instance of the DB cluster.  **Returned:** always  **Sample:** `"rds-cluster-demo.cluster-cvlrtwiennww.us-east-1.rds.amazonaws.com"` |
| **engine**  string | The database engine of the DB cluster.  **Returned:** always  **Sample:** `"aurora"` |
| **engine_mode**  string | The DB engine mode of the DB cluster.  **Returned:** always  **Sample:** `"provisioned"` |
| **engine_version**  string | The database engine version.  **Returned:** always  **Sample:** `"5.6.10a"` |
| **hosted_zone_id**  string | The ID that Amazon Route 53 assigns when you create a hosted zone.  **Returned:** always  **Sample:** `"Z2R2ITUGPM61AM"` |
| **http_endpoint_enabled**  boolean | A value that indicates whether the HTTP endpoint for an Aurora Serverless DB cluster is enabled.  **Returned:** always  **Sample:** `false` |
| **iam_database_authentication_enabled**  boolean | Whether IAM accounts may be mapped to database accounts.  **Returned:** always  **Sample:** `false` |
| **latest_restorable_time**  string | The latest time to which a database can be restored with point-in-time restore.  **Returned:** always  **Sample:** `"2018-06-29T14:09:34.797000+00:00"` |
| **master_username**  string | The master username for the DB cluster.  **Returned:** always  **Sample:** `"username"` |
| **multi_az**  boolean | Whether the DB cluster has instances in multiple availability zones.  **Returned:** always  **Sample:** `false` |
| **port**  integer | The port that the database engine is listening on.  **Returned:** always  **Sample:** `3306` |
| **preferred_backup_window**  string | The UTC weekly time range during which system maintenance can occur.  **Returned:** always  **Sample:** `"10:18-10:48"` |
| **preferred_maintenance_window**  string | The UTC weekly time range during which system maintenance can occur.  **Returned:** always  **Sample:** `"tue:03:23-tue:03:53"` |
| **read_replica_identifiers**  list / elements=string | A list of read replica ID strings associated with the DB cluster.  **Returned:** always  **Sample:** `[]` |
| **reader_endpoint**  string | The reader endpoint for the DB cluster.  **Returned:** always  **Sample:** `"rds-cluster-demo.cluster-ro-cvlrtwiennww.us-east-1.rds.amazonaws.com"` |
| **status**  string | The status of the DB cluster.  **Returned:** always  **Sample:** `"available"` |
| **storage_encrypted**  boolean | Whether the DB cluster is storage encrypted.  **Returned:** always  **Sample:** `false` |
| **tag_list**  list / elements=dictionary | A list of tags consisting of key-value pairs.  **Returned:** always  **Sample:** `[{"key": "Created_By", "value": "Ansible_rds_cluster_integration_test"}]` |
| **tags**  dictionary | A dictionary of key value pairs.  **Returned:** always  **Sample:** `{"Name": "rds-cluster-demo"}` |
| **vpc_security_groups**  complex | A list of the DB cluster’s security groups and their status.  **Returned:** always |
| **status**  string | Status of the security group.  **Returned:** always  **Sample:** `"active"` |
| **vpc_security_group_id**  string | Security group of the cluster.  **Returned:** always  **Sample:** `"sg-12345678"` |

### Authors

- Sloane Hertel (@s-hertel)
- Alina Buzachis (@alinabuzachis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
