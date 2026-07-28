---
collection: ansible
version: "8"
title: "amazon.aws.rds_snapshot_info module – obtain information about one or more RDS snapshots"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/rds_snapshot_info_module.html
fetched_at: 2026-07-28T01:07:09+00:00
---
# amazon.aws.rds_snapshot_info module – obtain information about one or more RDS snapshots

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
> see [Requirements](rds_snapshot_info_module.md#ansible-collections-amazon-aws-rds-snapshot-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.rds_snapshot_info`.

New in amazon.aws 5.0.0

- [Synopsis](rds_snapshot_info_module.md#synopsis)
- [Requirements](rds_snapshot_info_module.md#requirements)
- [Parameters](rds_snapshot_info_module.md#parameters)
- [Notes](rds_snapshot_info_module.md#notes)
- [Examples](rds_snapshot_info_module.md#examples)
- [Return Values](rds_snapshot_info_module.md#return-values)

## [Synopsis](rds_snapshot_info_module.md#id1)

- Obtain information about one or more RDS snapshots. These can be for unclustered snapshots or snapshots of clustered DBs (Aurora).
- Aurora snapshot information may be obtained if no identifier parameters are passed or if one of the cluster parameters are passed.
- This module was originally added to `community.aws` in release 1.0.0.

## [Requirements](rds_snapshot_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](rds_snapshot_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **db_cluster_identifier**  string | RDS cluster name for which to find snapshots.  Mutually exclusive with *db_snapshot_identifier*, *db_instance_identifier*, *db_cluster_snapshot_identifier* |
| **db_cluster_snapshot_identifier**  string | Name of an RDS cluster snapshot.  Mutually exclusive with *db_instance_identifier*, *db_snapshot_identifier*, *db_cluster_identifier* |
| **db_instance_identifier**  string | RDS instance name for which to find snapshots.  Mutually exclusive with *db_snapshot_identifier*, *db_cluster_identifier*, *db_cluster_snapshot_identifier* |
| **db_snapshot_identifier**  aliases: snapshot_name  string | Name of an RDS (unclustered) snapshot.  Mutually exclusive with *db_instance_identifier*, *db_cluster_identifier*, *db_cluster_snapshot_identifier* |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **snapshot_type**  string | Type of snapshot to find.  By default both automated and manual snapshots will be returned.  **Choices:**   - `"automated"` - `"manual"` - `"shared"` - `"public"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](rds_snapshot_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](rds_snapshot_info_module.md#id5)

```yaml+jinja
- name: Get information about an snapshot
  amazon.aws.rds_snapshot_info:
    db_snapshot_identifier: snapshot_name
  register: new_database_info

- name: Get all RDS snapshots for an RDS instance
  amazon.aws.rds_snapshot_info:
    db_instance_identifier: helloworld-rds-master
```

## [Return Values](rds_snapshot_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cluster_snapshots**  complex | List of cluster snapshots  **Returned:** always |
| **allocated_storage**  integer | How many gigabytes of storage are allocated  **Returned:** always  **Sample:** `1` |
| **availability_zones**  list / elements=string | The availability zones of the database from which the snapshot was taken  **Returned:** always  **Sample:** `["ca-central-1a", "ca-central-1b"]` |
| **cluster_create_time**  string | Date and time the cluster was created  **Returned:** always  **Sample:** `"2018-05-17T00:13:40.223000+00:00"` |
| **db_cluster_identifier**  string | Database cluster identifier  **Returned:** always  **Sample:** `"test-aurora-cluster"` |
| **db_cluster_snapshot_arn**  string | ARN of the database snapshot  **Returned:** always  **Sample:** `"arn:aws:rds:ca-central-1:123456789012:cluster-snapshot:test-aurora-snapshot"` |
| **db_cluster_snapshot_identifier**  string | Snapshot identifier  **Returned:** always  **Sample:** `"test-aurora-snapshot"` |
| **engine**  string | Database engine  **Returned:** always  **Sample:** `"aurora"` |
| **engine_version**  string | Database engine version  **Returned:** always  **Sample:** `"5.6.10a"` |
| **iam_database_authentication_enabled**  boolean | Whether database authentication through IAM is enabled  **Returned:** always  **Sample:** `false` |
| **kms_key_id**  string | ID of the KMS Key encrypting the snapshot  **Returned:** always  **Sample:** `"arn:aws:kms:ca-central-1:123456789012:key/abcd1234-abcd-1111-aaaa-0123456789ab"` |
| **license_model**  string | License model  **Returned:** always  **Sample:** `"aurora"` |
| **master_username**  string | Database master username  **Returned:** always  **Sample:** `"shertel"` |
| **percent_progress**  integer | Percent progress of snapshot  **Returned:** always  **Sample:** `0` |
| **port**  integer | Database port  **Returned:** always  **Sample:** `0` |
| **snapshot_create_time**  string | Date and time when the snapshot was created  **Returned:** always  **Sample:** `"2018-05-17T00:23:23.731000+00:00"` |
| **snapshot_type**  string | Type of snapshot  **Returned:** always  **Sample:** `"manual"` |
| **status**  string | Status of snapshot  **Returned:** always  **Sample:** `"creating"` |
| **storage_encrypted**  boolean | Whether the snapshot is encrypted  **Returned:** always  **Sample:** `true` |
| **tags**  complex | Tags of the snapshot  **Returned:** when snapshot is not shared |
| **vpc_id**  string | VPC of the database  **Returned:** always  **Sample:** `"vpc-abcd1234"` |
| **snapshots**  complex | List of non-clustered snapshots  **Returned:** When cluster parameters are not passed |
| **allocated_storage**  integer | How many gigabytes of storage are allocated  **Returned:** always  **Sample:** `10` |
| **availability_zone**  string | The availability zone of the database from which the snapshot was taken  **Returned:** always  **Sample:** `"us-west-2b"` |
| **db_instance_identifier**  string | Database instance identifier  **Returned:** always  **Sample:** `"hello-world-rds"` |
| **db_snapshot_arn**  string | Snapshot ARN  **Returned:** always  **Sample:** `"arn:aws:rds:us-west-2:123456789012:snapshot:rds:hello-world-rds-us1-2018-05-16-04-03"` |
| **db_snapshot_identifier**  string | Snapshot name  **Returned:** always  **Sample:** `"rds:hello-world-rds-us1-2018-05-16-04-03"` |
| **encrypted**  boolean | Whether the snapshot was encrypted  **Returned:** always  **Sample:** `true` |
| **engine**  string | Database engine  **Returned:** always  **Sample:** `"postgres"` |
| **engine_version**  string | Database engine version  **Returned:** always  **Sample:** `"9.5.10"` |
| **iam_database_authentication_enabled**  boolean | Whether database authentication through IAM is enabled  **Returned:** always  **Sample:** `false` |
| **instance_create_time**  string | Time the Instance was created  **Returned:** always  **Sample:** `"2017-10-10T04:00:07.434000+00:00"` |
| **kms_key_id**  string | ID of the KMS Key encrypting the snapshot  **Returned:** always  **Sample:** `"arn:aws:kms:us-west-2:123456789012:key/abcd1234-1234-aaaa-0000-1234567890ab"` |
| **license_model**  string | License model  **Returned:** always  **Sample:** `"postgresql-license"` |
| **master_username**  string | Database master username  **Returned:** always  **Sample:** `"dbadmin"` |
| **option_group_name**  string | Database option group name  **Returned:** always  **Sample:** `"default:postgres-9-5"` |
| **percent_progress**  integer | Percent progress of snapshot  **Returned:** always  **Sample:** `100` |
| **snapshot_create_time**  string | Time snapshot was created  **Returned:** always  **Sample:** `"2018-05-16T04:03:33.871000+00:00"` |
| **snapshot_type**  string | Type of snapshot  **Returned:** always  **Sample:** `"automated"` |
| **status**  string | Status of snapshot  **Returned:** always  **Sample:** `"available"` |
| **storage_type**  string | Storage type of underlying DB  **Returned:** always  **Sample:** `"gp2"` |
| **tags**  complex | Snapshot tags  **Returned:** when snapshot is not shared |
| **vpc_id**  string | ID of VPC containing the DB  **Returned:** always  **Sample:** `"vpc-abcd1234"` |

### Authors

- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
