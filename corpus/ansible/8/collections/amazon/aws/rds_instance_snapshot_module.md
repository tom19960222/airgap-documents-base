---
collection: ansible
version: "8"
title: "amazon.aws.rds_instance_snapshot module – Manage Amazon RDS instance snapshots"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/rds_instance_snapshot_module.html
fetched_at: 2026-07-28T01:07:06+00:00
---
# amazon.aws.rds_instance_snapshot module – Manage Amazon RDS instance snapshots

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
> see [Requirements](rds_instance_snapshot_module.md#ansible-collections-amazon-aws-rds-instance-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.rds_instance_snapshot`.

New in amazon.aws 5.0.0

- [Synopsis](rds_instance_snapshot_module.md#synopsis)
- [Requirements](rds_instance_snapshot_module.md#requirements)
- [Parameters](rds_instance_snapshot_module.md#parameters)
- [Notes](rds_instance_snapshot_module.md#notes)
- [Examples](rds_instance_snapshot_module.md#examples)
- [Return Values](rds_instance_snapshot_module.md#return-values)

## [Synopsis](rds_instance_snapshot_module.md#id1)

- Creates or deletes RDS snapshots.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](rds_instance_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](rds_instance_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **copy_tags**  boolean  *added in community.aws 3.3.0* | Whether to copy all tags from *source_db_snapshot_identifier* to *db_instance_identifier*.  **Choices:**   - `false` ← (default) - `true` |
| **db_instance_identifier**  aliases: instance_id  string | Database instance identifier. Required when creating a snapshot. |
| **db_snapshot_identifier**  aliases: id, snapshot_id  string / required | The snapshot to manage. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **source_db_snapshot_identifier**  aliases: source_id, source_snapshot_id  string  *added in community.aws 3.3.0* | The identifier of the source DB snapshot.  Required when copying a snapshot.  If the source snapshot is in the same AWS region as the copy, specify the snapshot’s identifier.  If the source snapshot is in a different AWS region as the copy, specify the snapshot’s ARN. |
| **source_region**  string  *added in community.aws 3.3.0* | The region that contains the snapshot to be copied. |
| **state**  string | Specify the desired state of the snapshot.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **wait**  boolean | Whether or not to wait for snapshot creation or deletion.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | how long before wait gives up, in seconds.  **Default:** `300` |

## [Notes](rds_instance_snapshot_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](rds_instance_snapshot_module.md#id5)

```yaml+jinja
- name: Create snapshot
  amazon.aws.rds_instance_snapshot:
    db_instance_identifier: new-database
    db_snapshot_identifier: new-database-snapshot
  register: snapshot

- name: Copy snapshot from a different region and copy its tags
  amazon.aws.rds_instance_snapshot:
    id: new-database-snapshot-copy
    region: us-east-1
    source_id: "{{ snapshot.db_snapshot_arn }}"
    source_region: us-east-2
    copy_tags: true

- name: Delete snapshot
  amazon.aws.rds_instance_snapshot:
    db_snapshot_identifier: new-database-snapshot
    state: absent
```

## [Return Values](rds_instance_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allocated_storage**  integer | How much storage is allocated in GB.  **Returned:** always  **Sample:** `20` |
| **availability_zone**  string | Availability zone of the database from which the snapshot was created.  **Returned:** always  **Sample:** `"us-west-2a"` |
| **db_instance_identifier**  string | Database from which the snapshot was created.  **Returned:** always  **Sample:** `"ansible-test-16638696"` |
| **db_snapshot_arn**  string | Amazon Resource Name for the snapshot.  **Returned:** always  **Sample:** `"arn:aws:rds:us-west-2:123456789012:snapshot:ansible-test-16638696-test-snapshot"` |
| **db_snapshot_identifier**  string | Name of the snapshot.  **Returned:** always  **Sample:** `"ansible-test-16638696-test-snapshot"` |
| **dbi_resource_id**  string | The identifier for the source DB instance, which can’t be changed and which is unique to an AWS Region.  **Returned:** always  **Sample:** `"db-MM4P2U35RQRAMWD3QDOXWPZP4U"` |
| **encrypted**  boolean | Whether the snapshot is encrypted.  **Returned:** always  **Sample:** `false` |
| **engine**  string | Engine of the database from which the snapshot was created.  **Returned:** always  **Sample:** `"mariadb"` |
| **engine_version**  string | Version of the database from which the snapshot was created.  **Returned:** always  **Sample:** `"10.2.21"` |
| **iam_database_authentication_enabled**  boolean | Whether IAM database authentication is enabled.  **Returned:** always  **Sample:** `false` |
| **instance_create_time**  string | Creation time of the instance from which the snapshot was created.  **Returned:** always  **Sample:** `"2019-06-15T10:15:56.221000+00:00"` |
| **license_model**  string | License model of the database.  **Returned:** always  **Sample:** `"general-public-license"` |
| **master_username**  string | Master username of the database.  **Returned:** always  **Sample:** `"test"` |
| **option_group_name**  string | Option group of the database.  **Returned:** always  **Sample:** `"default:mariadb-10-2"` |
| **percent_progress**  integer | How much progress has been made taking the snapshot. Will be 100 for an available snapshot.  **Returned:** always  **Sample:** `100` |
| **port**  integer | Port on which the database is listening.  **Returned:** always  **Sample:** `3306` |
| **processor_features**  list / elements=string | List of processor features of the database.  **Returned:** always  **Sample:** `[]` |
| **snapshot_create_time**  string | Creation time of the snapshot.  **Returned:** always  **Sample:** `"2019-06-15T10:46:23.776000+00:00"` |
| **snapshot_type**  string | How the snapshot was created (always manual for this module!).  **Returned:** always  **Sample:** `"manual"` |
| **source_db_snapshot_identifier**  string  *added in community.aws 3.3.0* | The DB snapshot ARN that the DB snapshot was copied from.  **Returned:** when snapshot is a copy  **Sample:** `"arn:aws:rds:us-west-2:123456789012:snapshot:ansible-test-16638696-test-snapshot-source"` |
| **status**  string | Status of the snapshot.  **Returned:** always  **Sample:** `"available"` |
| **storage_type**  string | Storage type of the database.  **Returned:** always  **Sample:** `"gp2"` |
| **tags**  complex | Tags applied to the snapshot.  **Returned:** always |
| **vpc_id**  string | ID of the VPC in which the DB lives.  **Returned:** always  **Sample:** `"vpc-09ff232e222710ae0"` |

### Authors

- Will Thames (@willthames)
- Michael De La Rue (@mikedlr)
- Alina Buzachis (@alinabuzachis)
- Joseph Torcasso (@jatorcasso)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
