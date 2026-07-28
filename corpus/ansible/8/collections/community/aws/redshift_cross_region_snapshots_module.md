---
collection: ansible
version: "8"
title: "community.aws.redshift_cross_region_snapshots module – Manage Redshift Cross Region Snapshots"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/redshift_cross_region_snapshots_module.html
fetched_at: 2026-07-28T01:41:44+00:00
---
# community.aws.redshift_cross_region_snapshots module – Manage Redshift Cross Region Snapshots

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
> see [Requirements](redshift_cross_region_snapshots_module.md#ansible-collections-community-aws-redshift-cross-region-snapshots-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.redshift_cross_region_snapshots`.

New in community.aws 1.0.0

- [Synopsis](redshift_cross_region_snapshots_module.md#synopsis)
- [Requirements](redshift_cross_region_snapshots_module.md#requirements)
- [Parameters](redshift_cross_region_snapshots_module.md#parameters)
- [Notes](redshift_cross_region_snapshots_module.md#notes)
- [Examples](redshift_cross_region_snapshots_module.md#examples)

## [Synopsis](redshift_cross_region_snapshots_module.md#id1)

- Manage Redshift Cross Region Snapshots. Supports KMS-Encrypted Snapshots.
- For more information, see <https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html#cross-region-snapshot-copy>

## [Requirements](redshift_cross_region_snapshots_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](redshift_cross_region_snapshots_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **cluster_name**  aliases: cluster  string / required | The name of the cluster to configure cross-region snapshots for. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **destination_region**  aliases: destination  string / required | The region to copy snapshots to. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: source  string / required | The cluster’s region. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **snapshot_copy_grant**  aliases: copy_grant  string | A grant for Amazon Redshift to use a master key in the *destination_region*.  See <http://boto3.readthedocs.io/en/latest/reference/services/redshift.html#Redshift.Client.create_snapshot_copy_grant> |
| **snapshot_retention_period**  aliases: retention_period  integer / required | The number of days to keep cross-region snapshots for. |
| **state**  string | Create or remove the cross-region snapshot configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](redshift_cross_region_snapshots_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](redshift_cross_region_snapshots_module.md#id5)

```yaml+jinja
- name: configure cross-region snapshot on cluster `johniscool`
  community.aws.redshift_cross_region_snapshots:
    cluster_name: johniscool
    state: present
    region: us-east-1
    destination_region: us-west-2
    retention_period: 1

- name: configure cross-region snapshot on kms-encrypted cluster
  community.aws.redshift_cross_region_snapshots:
    cluster_name: whatever
    state: present
    region: us-east-1
    destination: us-west-2
    copy_grant: 'my-grant-in-destination'
    retention_period: 10

- name: disable cross-region snapshots, necessary before most cluster modifications (rename, resize)
  community.aws.redshift_cross_region_snapshots:
    cluster_name: whatever
    state: absent
    region: us-east-1
    destination_region: us-west-2
```

### Authors

- JR Kerkstra (@captainkerk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
