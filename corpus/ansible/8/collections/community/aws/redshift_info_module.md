---
collection: ansible
version: "8"
title: "community.aws.redshift_info module – Gather information about Redshift cluster(s)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/redshift_info_module.html
fetched_at: 2026-07-28T01:41:44+00:00
---
# community.aws.redshift_info module – Gather information about Redshift cluster(s)

> **Note:**
>
> This module is part of the [community.aws collection](https://galaxy.ansible.com/ui/repo/published/community/aws/) (version 6.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.aws`.
> You need further requirements to be able to use this module,
> see [Requirements](redshift_info_module.md#ansible-collections-community-aws-redshift-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.redshift_info`.

New in community.aws 1.0.0

- [Synopsis](redshift_info_module.md#synopsis)
- [Requirements](redshift_info_module.md#requirements)
- [Parameters](redshift_info_module.md#parameters)
- [Notes](redshift_info_module.md#notes)
- [Examples](redshift_info_module.md#examples)
- [Return Values](redshift_info_module.md#return-values)

## [Synopsis](redshift_info_module.md#id1)

- Gather information about Redshift cluster(s).

## [Requirements](redshift_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](redshift_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cluster_identifier**  aliases: name, identifier  string | The prefix of cluster identifier of the Redshift cluster you are searching for.  This is a regular expression match with implicit ‘^’. Append ‘$’ for a complete match. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **tags**  dictionary | A dictionary/hash of tags in the format { tag1_name: ‘tag1_value’, tag2_name: ‘tag2_value’ } to match against the security group(s) you are searching for. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](redshift_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](redshift_info_module.md#id5)

```yaml+jinja
# Note: These examples do net set authentication details, see the AWS guide for details.

- name: Find all clusters
  community.aws.redshift_info:
  register: redshift

- name: Find cluster(s) with matching tags
  community.aws.redshift_info:
    tags:
      env: prd
      stack: monitoring
  register: redshift_tags

- name: Find cluster(s) with matching name/prefix and tags
  community.aws.redshift_info:
    tags:
      env: dev
      stack: web
    name: user-
  register: redshift_web

- name: Fail if no cluster(s) is/are found
  community.aws.redshift_info:
    tags:
      env: stg
      stack: db
  register: redshift_user
  failed_when: "{{ redshift_user.results | length == 0 }}"
```

## [Return Values](redshift_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **allow_version_upgrade**  boolean | A Boolean value that, if true, indicates that major version upgrades will be applied automatically to the cluster during the maintenance window.  **Returned:** success  **Sample:** `"true|false"` |
| **automated_snapshot_retention_period**  integer | The number of days that automatic cluster snapshots are retained.  **Returned:** success  **Sample:** `1` |
| **availability_zone**  string | The name of the Availability Zone in which the cluster is located.  **Returned:** success  **Sample:** `"us-east-1b"` |
| **cluster_create_time**  string | The date and time that the cluster was created.  **Returned:** success  **Sample:** `"2016-05-10T08:33:16.629000+00:00"` |
| **cluster_identifier**  string | Unique key to identify the cluster.  **Returned:** success  **Sample:** `"redshift-identifier"` |
| **cluster_nodes**  list / elements=string | The nodes in the cluster.  **Returned:** success  **Sample:** `[{"node_role": "LEADER", "private_ip_address": "10.0.0.1", "public_ip_address": "x.x.x.x"}, {"node_role": "COMPUTE-1", "private_ip_address": "10.0.0.3", "public_ip_address": "x.x.x.x"}]` |
| **cluster_paramater_groups**  list / elements=string | The list of cluster parameters that are associated with this cluster.  **Returned:** success  **Sample:** `[{"cluster_parameter_status_list": [{"parameter_apply_status": "in-sync", "parameter_name": "statement_timeout"}, {"parameter_apply_status": "in-sync", "parameter_name": "require_ssl"}], "parameter_apply_status": "in-sync", "parameter_group_name": "tuba"}]` |
| **cluster_public_keys**  string | The public key for the cluster.  **Returned:** success  **Sample:** `"ssh-rsa anjigfam Amazon-Redshift\n"` |
| **cluster_revision_number**  string | The specific revision number of the database in the cluster.  **Returned:** success  **Sample:** `"1231"` |
| **cluster_security_groups**  list / elements=string | A list of cluster security groups that are associated with the cluster.  **Returned:** success  **Sample:** `[]` |
| **cluster_snapshot_copy_status**  dictionary | A value that returns the destination region and retention period that are configured for cross-region snapshot copy.  **Returned:** success  **Sample:** `{}` |
| **cluster_status**  string | Current state of the cluster.  **Returned:** success  **Sample:** `"available"` |
| **cluster_subnet_group_name**  string | The name of the subnet group that is associated with the cluster.  **Returned:** success  **Sample:** `"redshift-subnet"` |
| **cluster_version**  string | The version ID of the Amazon Redshift engine that is running on the cluster.  **Returned:** success  **Sample:** `"1.0"` |
| **db_name**  string | The name of the initial database that was created when the cluster was created.  **Returned:** success  **Sample:** `"dev"` |
| **elastic_ip_status**  dictionary | The status of the elastic IP (EIP) address.  **Returned:** success  **Sample:** `{}` |
| **encrypted**  boolean | Boolean value that, if true , indicates that data in the cluster is encrypted at rest.  **Returned:** success  **Sample:** `"true|false"` |
| **endpoint**  string | The connection endpoint.  **Returned:** success  **Sample:** `"{'address': 'cluster-ds2.ocmugla0rf.us-east-1.redshift.amazonaws.com', 'port': 5439}"` |
| **enhanced_vpc_routing**  boolean | An option that specifies whether to create the cluster with enhanced VPC routing enabled.  **Returned:** success  **Sample:** `"true|false"` |
| **hsm_status**  dictionary | A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.  **Returned:** success  **Sample:** `{}` |
| **iam_roles**  list / elements=string | List of IAM roles attached to the cluster.  **Returned:** success  **Sample:** `[]` |
| **kms_key_id**  string | The AWS Key Management Service (AWS KMS) key ID of the encryption key used to encrypt data in the cluster.  **Returned:** success  **Sample:** `""` |
| **master_username**  string | The master user name for the cluster.  **Returned:** success  **Sample:** `"admin"` |
| **modify_status**  string | The status of a modify operation.  **Returned:** optional  **Sample:** `""` |
| **node_type**  string | The node type for nodes in the cluster.  **Returned:** success  **Sample:** `"ds2.xlarge"` |
| **number_of_nodes**  integer | The number of compute nodes in the cluster.  **Returned:** success  **Sample:** `12` |
| **pending_modified_values**  dictionary | A value that, if present, indicates that changes to the cluster are pending.  **Returned:** success  **Sample:** `{}` |
| **preferred_maintenance_window**  string | The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.  **Returned:** success  **Sample:** `"tue:07:30-tue:08:00"` |
| **publicly_accessible**  boolean | A Boolean value that, if true , indicates that the cluster can be accessed from a public network.  **Returned:** success  **Sample:** `"true|false"` |
| **restore_status**  dictionary | A value that describes the status of a cluster restore action.  **Returned:** success  **Sample:** `{}` |
| **tags**  list / elements=string | The list of tags for the cluster.  **Returned:** success  **Sample:** `[]` |
| **vpc_id**  string | The identifier of the VPC the cluster is in, if the cluster is in a VPC.  **Returned:** success  **Sample:** `"vpc-1234567"` |
| **vpc_security_groups**  list / elements=string | A list of VPC security groups the are associated with the cluster.  **Returned:** success  **Sample:** `[{"status": "active", "vpc_security_group_id": "sg-12cghhg"}]` |

### Authors

- Jens Carl (@j-carl)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
