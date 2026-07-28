---
collection: ansible
version: "6"
title: "community.aws.rds_snapshot_info module – obtain information about one or more RDS snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/rds_snapshot_info_module.html
fetched_at: 2026-07-27T17:04:54+00:00
---
# community.aws.rds_snapshot_info module – obtain information about one or more RDS snapshots

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
> see [Requirements](rds_snapshot_info_module.md#ansible-collections-community-aws-rds-snapshot-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.rds_snapshot_info`.

New in community.aws 1.0.0

- [Synopsis](rds_snapshot_info_module.md#synopsis)
- [Requirements](rds_snapshot_info_module.md#requirements)
- [Parameters](rds_snapshot_info_module.md#parameters)
- [Notes](rds_snapshot_info_module.md#notes)
- [Examples](rds_snapshot_info_module.md#examples)
- [Return Values](rds_snapshot_info_module.md#return-values)

## [Synopsis](rds_snapshot_info_module.md#id1)

- Obtain information about one or more RDS snapshots. These can be for unclustered snapshots or snapshots of clustered DBs (Aurora).
- Aurora snapshot information may be obtained if no identifier parameters are passed or if one of the cluster parameters are passed.

## [Requirements](rds_snapshot_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](rds_snapshot_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **db_cluster_identifier**  string | RDS cluster name for which to find snapshots.  Mutually exclusive with *db_snapshot_identifier*, *db_instance_identifier*, *db_cluster_snapshot_identifier* |
| **db_cluster_snapshot_identifier**  string | Name of an RDS cluster snapshot.  Mutually exclusive with *db_instance_identifier*, *db_snapshot_identifier*, *db_cluster_identifier* |
| **db_instance_identifier**  string | RDS instance name for which to find snapshots.  Mutually exclusive with *db_snapshot_identifier*, *db_cluster_identifier*, *db_cluster_snapshot_identifier* |
| **db_snapshot_identifier**  aliases: snapshot_name  string | Name of an RDS (unclustered) snapshot.  Mutually exclusive with *db_instance_identifier*, *db_cluster_identifier*, *db_cluster_snapshot_identifier* |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **snapshot_type**  string | Type of snapshot to find.  By default both automated and manual snapshots will be returned.  Choices:   - `"automated"` - `"manual"` - `"shared"` - `"public"` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](rds_snapshot_info_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](rds_snapshot_info_module.md#id5)

```yaml+jinja
- name: Get information about an snapshot
  community.aws.rds_snapshot_info:
    db_snapshot_identifier: snapshot_name
  register: new_database_info

- name: Get all RDS snapshots for an RDS instance
  community.aws.rds_snapshot_info:
    db_instance_identifier: helloworld-rds-master
```

## [Return Values](rds_snapshot_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cluster_snapshots**  complex | List of cluster snapshots  Returned: always |
| **allocated_storage**  integer | How many gigabytes of storage are allocated  Returned: always  Sample: `1` |
| **availability_zones**  list / elements=string | The availability zones of the database from which the snapshot was taken  Returned: always  Sample: `["ca-central-1a", "ca-central-1b"]` |
| **cluster_create_time**  string | Date and time the cluster was created  Returned: always  Sample: `"2018-05-17T00:13:40.223000+00:00"` |
| **db_cluster_identifier**  string | Database cluster identifier  Returned: always  Sample: `"test-aurora-cluster"` |
| **db_cluster_snapshot_arn**  string | ARN of the database snapshot  Returned: always  Sample: `"arn:aws:rds:ca-central-1:111111111111:cluster-snapshot:test-aurora-snapshot"` |
| **db_cluster_snapshot_identifier**  string | Snapshot identifier  Returned: always  Sample: `"test-aurora-snapshot"` |
| **engine**  string | Database engine  Returned: always  Sample: `"aurora"` |
| **engine_version**  string | Database engine version  Returned: always  Sample: `"5.6.10a"` |
| **iam_database_authentication_enabled**  boolean | Whether database authentication through IAM is enabled  Returned: always  Sample: `false` |
| **kms_key_id**  string | ID of the KMS Key encrypting the snapshot  Returned: always  Sample: `"arn:aws:kms:ca-central-1:111111111111:key/abcd1234-abcd-1111-aaaa-0123456789ab"` |
| **license_model**  string | License model  Returned: always  Sample: `"aurora"` |
| **master_username**  string | Database master username  Returned: always  Sample: `"shertel"` |
| **percent_progress**  integer | Percent progress of snapshot  Returned: always  Sample: `0` |
| **port**  integer | Database port  Returned: always  Sample: `0` |
| **snapshot_create_time**  string | Date and time when the snapshot was created  Returned: always  Sample: `"2018-05-17T00:23:23.731000+00:00"` |
| **snapshot_type**  string | Type of snapshot  Returned: always  Sample: `"manual"` |
| **status**  string | Status of snapshot  Returned: always  Sample: `"creating"` |
| **storage_encrypted**  boolean | Whether the snapshot is encrypted  Returned: always  Sample: `true` |
| **tags**  complex | Tags of the snapshot  Returned: when snapshot is not shared |
| **vpc_id**  string | VPC of the database  Returned: always  Sample: `"vpc-abcd1234"` |
| **snapshots**  complex | List of non-clustered snapshots  Returned: When cluster parameters are not passed |
| **allocated_storage**  integer | How many gigabytes of storage are allocated  Returned: always  Sample: `10` |
| **availability_zone**  string | The availability zone of the database from which the snapshot was taken  Returned: always  Sample: `"us-west-2b"` |
| **db_instance_identifier**  string | Database instance identifier  Returned: always  Sample: `"hello-world-rds"` |
| **db_snapshot_arn**  string | Snapshot ARN  Returned: always  Sample: `"arn:aws:rds:us-west-2:111111111111:snapshot:rds:hello-world-rds-us1-2018-05-16-04-03"` |
| **db_snapshot_identifier**  string | Snapshot name  Returned: always  Sample: `"rds:hello-world-rds-us1-2018-05-16-04-03"` |
| **encrypted**  boolean | Whether the snapshot was encrypted  Returned: always  Sample: `true` |
| **engine**  string | Database engine  Returned: always  Sample: `"postgres"` |
| **engine_version**  string | Database engine version  Returned: always  Sample: `"9.5.10"` |
| **iam_database_authentication_enabled**  boolean | Whether database authentication through IAM is enabled  Returned: always  Sample: `false` |
| **instance_create_time**  string | Time the Instance was created  Returned: always  Sample: `"2017-10-10T04:00:07.434000+00:00"` |
| **kms_key_id**  string | ID of the KMS Key encrypting the snapshot  Returned: always  Sample: `"arn:aws:kms:us-west-2:111111111111:key/abcd1234-1234-aaaa-0000-1234567890ab"` |
| **license_model**  string | License model  Returned: always  Sample: `"postgresql-license"` |
| **master_username**  string | Database master username  Returned: always  Sample: `"dbadmin"` |
| **option_group_name**  string | Database option group name  Returned: always  Sample: `"default:postgres-9-5"` |
| **percent_progress**  integer | Percent progress of snapshot  Returned: always  Sample: `100` |
| **snapshot_create_time**  string | Time snapshot was created  Returned: always  Sample: `"2018-05-16T04:03:33.871000+00:00"` |
| **snapshot_type**  string | Type of snapshot  Returned: always  Sample: `"automated"` |
| **status**  string | Status of snapshot  Returned: always  Sample: `"available"` |
| **storage_type**  string | Storage type of underlying DB  Returned: always  Sample: `"gp2"` |
| **tags**  complex | Snapshot tags  Returned: when snapshot is not shared |
| **vpc_id**  string | ID of VPC containing the DB  Returned: always  Sample: `"vpc-abcd1234"` |

### Authors

- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
