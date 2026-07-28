---
collection: ansible
version: "6"
title: "community.aws.rds_instance_snapshot module – Manage Amazon RDS instance snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/aws/rds_instance_snapshot_module.html
fetched_at: 2026-07-27T17:04:51+00:00
---
# community.aws.rds_instance_snapshot module – Manage Amazon RDS instance snapshots

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
> see [Requirements](rds_instance_snapshot_module.md#ansible-collections-community-aws-rds-instance-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.rds_instance_snapshot`.

New in community.aws 1.0.0

- [Synopsis](rds_instance_snapshot_module.md#synopsis)
- [Requirements](rds_instance_snapshot_module.md#requirements)
- [Parameters](rds_instance_snapshot_module.md#parameters)
- [Notes](rds_instance_snapshot_module.md#notes)
- [Examples](rds_instance_snapshot_module.md#examples)
- [Return Values](rds_instance_snapshot_module.md#return-values)

## [Synopsis](rds_instance_snapshot_module.md#id1)

- Creates or deletes RDS snapshots.

## [Requirements](rds_instance_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](rds_instance_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **copy_tags**  boolean  added in community.aws 3.3.0 | Whether to copy all tags from *source_db_snapshot_identifier* to *db_instance_identifier*.  Choices:   - `false` ← (default) - `true` |
| **db_instance_identifier**  aliases: instance_id  string | Database instance identifier. Required when creating a snapshot. |
| **db_snapshot_identifier**  aliases: id, snapshot_id  string / required | The snapshot to manage. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | whether to remove tags not present in the *tags* parameter.  Choices:   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **source_db_snapshot_identifier**  aliases: source_id, source_snapshot_id  string  added in community.aws 3.3.0 | The identifier of the source DB snapshot.  Required when copying a snapshot.  If the source snapshot is in the same AWS region as the copy, specify the snapshot’s identifier.  If the source snapshot is in a different AWS region as the copy, specify the snapshot’s ARN. |
| **source_region**  string  added in community.aws 3.3.0 | The region that contains the snapshot to be copied. |
| **state**  string | Specify the desired state of the snapshot.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  dictionary | tags dict to apply to a snapshot. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **wait**  boolean | Whether or not to wait for snapshot creation or deletion.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | how long before wait gives up, in seconds.  Default: `300` |

## [Notes](rds_instance_snapshot_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](rds_instance_snapshot_module.md#id5)

```yaml+jinja
- name: Create snapshot
  community.aws.rds_instance_snapshot:
    db_instance_identifier: new-database
    db_snapshot_identifier: new-database-snapshot
  register: snapshot

- name: Copy snapshot from a different region and copy its tags
  community.aws.rds_instance_snapshot:
    id: new-database-snapshot-copy
    region: us-east-1
    source_id: "{{ snapshot.db_snapshot_arn }}"
    source_region: us-east-2
    copy_tags: yes

- name: Delete snapshot
  community.aws.rds_instance_snapshot:
    db_snapshot_identifier: new-database-snapshot
    state: absent
```

## [Return Values](rds_instance_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocated_storage**  integer | How much storage is allocated in GB.  Returned: always  Sample: `20` |
| **availability_zone**  string | Availability zone of the database from which the snapshot was created.  Returned: always  Sample: `"us-west-2a"` |
| **db_instance_identifier**  string | Database from which the snapshot was created.  Returned: always  Sample: `"ansible-test-16638696"` |
| **db_snapshot_arn**  string | Amazon Resource Name for the snapshot.  Returned: always  Sample: `"arn:aws:rds:us-west-2:123456789012:snapshot:ansible-test-16638696-test-snapshot"` |
| **db_snapshot_identifier**  string | Name of the snapshot.  Returned: always  Sample: `"ansible-test-16638696-test-snapshot"` |
| **dbi_resource_id**  string | The identifier for the source DB instance, which can’t be changed and which is unique to an AWS Region.  Returned: always  Sample: `"db-MM4P2U35RQRAMWD3QDOXWPZP4U"` |
| **encrypted**  boolean | Whether the snapshot is encrypted.  Returned: always  Sample: `false` |
| **engine**  string | Engine of the database from which the snapshot was created.  Returned: always  Sample: `"mariadb"` |
| **engine_version**  string | Version of the database from which the snapshot was created.  Returned: always  Sample: `"10.2.21"` |
| **iam_database_authentication_enabled**  boolean | Whether IAM database authentication is enabled.  Returned: always  Sample: `false` |
| **instance_create_time**  string | Creation time of the instance from which the snapshot was created.  Returned: always  Sample: `"2019-06-15T10:15:56.221000+00:00"` |
| **license_model**  string | License model of the database.  Returned: always  Sample: `"general-public-license"` |
| **master_username**  string | Master username of the database.  Returned: always  Sample: `"test"` |
| **option_group_name**  string | Option group of the database.  Returned: always  Sample: `"default:mariadb-10-2"` |
| **percent_progress**  integer | How much progress has been made taking the snapshot. Will be 100 for an available snapshot.  Returned: always  Sample: `100` |
| **port**  integer | Port on which the database is listening.  Returned: always  Sample: `3306` |
| **processor_features**  list / elements=string | List of processor features of the database.  Returned: always  Sample: `[]` |
| **snapshot_create_time**  string | Creation time of the snapshot.  Returned: always  Sample: `"2019-06-15T10:46:23.776000+00:00"` |
| **snapshot_type**  string | How the snapshot was created (always manual for this module!).  Returned: always  Sample: `"manual"` |
| **source_db_snapshot_identifier**  string  added in community.aws 3.3.0 | The DB snapshot ARN that the DB snapshot was copied from.  Returned: when snapshot is a copy  Sample: `"arn:aws:rds:us-west-2:123456789012:snapshot:ansible-test-16638696-test-snapshot-source"` |
| **status**  string | Status of the snapshot.  Returned: always  Sample: `"available"` |
| **storage_type**  string | Storage type of the database.  Returned: always  Sample: `"gp2"` |
| **tags**  complex | Tags applied to the snapshot.  Returned: always |
| **vpc_id**  string | ID of the VPC in which the DB lives.  Returned: always  Sample: `"vpc-09ff232e222710ae0"` |

### Authors

- Will Thames (@willthames)
- Michael De La Rue (@mikedlr)
- Alina Buzachis (@alinabuzachis)
- Joseph Torcasso (@jatorcasso)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/community.aws)
[Communication](index.md#communication-for-community-aws)
