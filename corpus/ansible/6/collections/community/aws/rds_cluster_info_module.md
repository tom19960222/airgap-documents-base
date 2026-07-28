---
collection: ansible
version: "6"
title: "community.aws.rds_cluster_info module – Obtain information about one or more RDS clusters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/rds_cluster_info_module.html
fetched_at: 2026-07-27T17:04:49+00:00
---
# community.aws.rds_cluster_info module – Obtain information about one or more RDS clusters

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
> see [Requirements](rds_cluster_info_module.md#ansible-collections-community-aws-rds-cluster-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.rds_cluster_info`.

New in community.aws 3.2.0

- [Synopsis](rds_cluster_info_module.md#synopsis)
- [Requirements](rds_cluster_info_module.md#requirements)
- [Parameters](rds_cluster_info_module.md#parameters)
- [Notes](rds_cluster_info_module.md#notes)
- [Examples](rds_cluster_info_module.md#examples)
- [Return Values](rds_cluster_info_module.md#return-values)

## [Synopsis](rds_cluster_info_module.md#id1)

- Obtain information about one or more RDS clusters.

## [Requirements](rds_cluster_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](rds_cluster_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **db_cluster_identifier**  aliases: cluster_id, id, cluster_name  string | The user-supplied DB cluster identifier.  If this parameter is specified, information from only the specific DB cluster is returned. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filters**  dictionary | A filter that specifies one or more DB clusters to describe. See <https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html>. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](rds_cluster_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](rds_cluster_info_module.md#id5)

```yaml+jinja
- name: Get info of all existing DB clusters
  community.aws.rds_cluster_info:
  register: _result_cluster_info

- name: Get info on a specific DB cluster
  community.aws.rds_cluster_info:
    cluster_id: "{{ cluster_id }}"
  register: _result_cluster_info

- name: Get info all DB clusters with specific engine
  community.aws.rds_cluster_info:
    engine: "aurora"
  register: _result_cluster_info
```

## [Return Values](rds_cluster_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **clusters**  list / elements=string | List of RDS clusters.  Returned: always |
| **activity_stream_status**  string | The status of the database activity stream.  Returned: success  Sample: `"stopped"` |
| **allocated_storage**  integer | The allocated storage size in gigabytes. Since aurora storage size is not fixed this is always 1 for aurora database engines.  Returned: success  Sample: `1` |
| **associated_roles**  list / elements=string | A list of dictionaries of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. Each dictionary contains the role_arn and the status of the role.  Returned: success  Sample: `[]` |
| **availability_zones**  list / elements=string | The list of availability zones that instances in the DB cluster can be created in.  Returned: success  Sample: `["us-east-1c", "us-east-1a", "us-east-1e"]` |
| **backup_retention_period**  integer | The number of days for which automatic DB snapshots are retained.  Returned: success  Sample: `1` |
| **cluster_create_time**  string | The time in UTC when the DB cluster was created.  Returned: success  Sample: `"2018-06-29T14:08:58.491000+00:00"` |
| **copy_tags_to_snapshot**  boolean | Specifies whether tags are copied from the DB cluster to snapshots of the DB cluster.  Returned: success  Sample: `false` |
| **cross_account_clone**  boolean | Specifies whether the DB cluster is a clone of a DB cluster owned by a different Amazon Web Services account.  Returned: success  Sample: `false` |
| **db_cluster_arn**  string | The Amazon Resource Name (ARN) for the DB cluster.  Returned: success  Sample: `"arn:aws:rds:us-east-1:123456789012:cluster:rds-cluster-demo"` |
| **db_cluster_identifier**  string | The lowercase user-supplied DB cluster identifier.  Returned: success  Sample: `"rds-cluster-demo"` |
| **db_cluster_members**  list / elements=string | A list of dictionaries containing information about the instances in the cluster. Each dictionary contains the *db_instance_identifier*, *is_cluster_writer* (bool), *db_cluster_parameter_group_status*, and *promotion_tier* (int).  Returned: success  Sample: `[]` |
| **db_cluster_parameter_group**  string | The parameter group associated with the DB cluster.  Returned: success  Sample: `"default.aurora5.6"` |
| **db_cluster_resource_id**  string | The AWS Region-unique, immutable identifier for the DB cluster.  Returned: success  Sample: `"cluster-D2MEQDN3BQNXDF74K6DQJTHASU"` |
| **db_subnet_group**  string | The name of the subnet group associated with the DB Cluster.  Returned: success  Sample: `"default"` |
| **deletion_protection**  boolean | Indicates if the DB cluster has deletion protection enabled. The database can’t be deleted when deletion protection is enabled.  Returned: success  Sample: `false` |
| **domain_memberships**  list / elements=string | The Active Directory Domain membership records associated with the DB cluster.  Returned: success  Sample: `[]` |
| **earliest_restorable_time**  string | The earliest time to which a database can be restored with point-in-time restore.  Returned: success  Sample: `"2018-06-29T14:09:34.797000+00:00"` |
| **endpoint**  string | The connection endpoint for the primary instance of the DB cluster.  Returned: success  Sample: `"rds-cluster-demo.cluster-cvlrtwiennww.us-east-1.rds.amazonaws.com"` |
| **engine**  string | The database engine of the DB cluster.  Returned: success  Sample: `"aurora"` |
| **engine_mode**  string | The DB engine mode of the DB cluster.  Returned: success  Sample: `"provisioned"` |
| **engine_version**  string | The database engine version.  Returned: success  Sample: `"5.6.10a"` |
| **hosted_zone_id**  string | The ID that Amazon Route 53 assigns when you create a hosted zone.  Returned: success  Sample: `"Z2R2ITUGPM61AM"` |
| **http_endpoint_enabled**  boolean | A value that indicates whether the HTTP endpoint for an Aurora Serverless DB cluster is enabled.  Returned: success  Sample: `false` |
| **iam_database_authentication_enabled**  boolean | Whether IAM accounts may be mapped to database accounts.  Returned: success  Sample: `false` |
| **latest_restorable_time**  string | The latest time to which a database can be restored with point-in-time restore.  Returned: success  Sample: `"2018-06-29T14:09:34.797000+00:00"` |
| **master_username**  string | The master username for the DB cluster.  Returned: success  Sample: `"username"` |
| **multi_az**  boolean | Whether the DB cluster has instances in multiple availability zones.  Returned: success  Sample: `false` |
| **port**  integer | The port that the database engine is listening on.  Returned: success  Sample: `3306` |
| **preferred_backup_window**  string | The UTC weekly time range during which system maintenance can occur.  Returned: success  Sample: `"10:18-10:48"` |
| **preferred_maintenance_window**  string | The UTC weekly time range during which system maintenance can occur.  Returned: success  Sample: `"tue:03:23-tue:03:53"` |
| **read_replica_identifiers**  list / elements=string | A list of read replica ID strings associated with the DB cluster.  Returned: success  Sample: `[]` |
| **reader_endpoint**  string | The reader endpoint for the DB cluster.  Returned: success  Sample: `"rds-cluster-demo.cluster-ro-cvlrtwiennww.us-east-1.rds.amazonaws.com"` |
| **status**  string | The status of the DB cluster.  Returned: success  Sample: `"available"` |
| **storage_encrypted**  boolean | Whether the DB cluster is storage encrypted.  Returned: success  Sample: `false` |
| **tag_list**  list / elements=dictionary | A list of tags consisting of key-value pairs.  Returned: success  Sample: `[{"key": "Created_By", "value": "Ansible_rds_cluster_integration_test"}]` |
| **tags**  dictionary | A dictionary of key value pairs.  Returned: success  Sample: `{"Name": "rds-cluster-demo"}` |
| **vpc_security_groups**  complex | A list of the DB cluster’s security groups and their status.  Returned: success |
| **status**  string | Status of the security group.  Returned: success  Sample: `"active"` |
| **vpc_security_group_id**  string | Security group of the cluster.  Returned: success  Sample: `"sg-12345678"` |

### Authors

- Alina Buzachis (@alinabuzachis)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
