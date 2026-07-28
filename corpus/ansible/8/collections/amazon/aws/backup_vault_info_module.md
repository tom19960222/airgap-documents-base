---
collection: ansible
version: "8"
title: "amazon.aws.backup_vault_info module – Describe AWS Backup Vaults"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/backup_vault_info_module.html
fetched_at: 2026-07-28T01:06:13+00:00
---
# amazon.aws.backup_vault_info module – Describe AWS Backup Vaults

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
> see [Requirements](backup_vault_info_module.md#ansible-collections-amazon-aws-backup-vault-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.backup_vault_info`.

New in amazon.aws 6.0.0

- [Synopsis](backup_vault_info_module.md#synopsis)
- [Requirements](backup_vault_info_module.md#requirements)
- [Parameters](backup_vault_info_module.md#parameters)
- [Notes](backup_vault_info_module.md#notes)
- [Examples](backup_vault_info_module.md#examples)
- [Return Values](backup_vault_info_module.md#return-values)

## [Synopsis](backup_vault_info_module.md#id1)

- Lists info about Backup Vault configuration.

## [Requirements](backup_vault_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](backup_vault_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **backup_vault_names**  list / elements=string | Specifies a list of vault names.  If an empty list is specified, information for the backup vaults in the current region is returned.  **Default:** `[]` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](backup_vault_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](backup_vault_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather information about all backup vaults
- amazon.aws.backup_vault_info

# Gather information about a particular backup vault
- amazon.aws.backup_vault_info:
    backup vault_names:
      - "arn:aws:backup_vault:us-east-2:123456789012:backup_vault/defaultvault"
```

## [Return Values](backup_vault_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_vaults**  list / elements=dictionary | List of backup vault objects. Each element consists of a dict with all the information related to that backup vault.  **Returned:** always |
| **backup_vault_arn**  string | ARN of the backup vault.  **Returned:** success  **Sample:** `"arn:aws:backup:us-west-2:111122223333:vault/1234abcd-12ab-34cd-56ef-1234567890ab"` |
| **backup_vault_name**  string | Name of the backup vault.  **Returned:** success  **Sample:** `"default vault"` |
| **creation_date**  string | The date and time a backup vault is created, in Unix format and Coordinated Universal Time (UTC).  **Returned:** success  **Sample:** `"1516925490.087 (represents Friday, January 26, 2018 12:11:30.087 AM)."` |
| **creator_request_id**  string | A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice.  **Returned:** success |
| **encryption_key_arn**  string | The server-side encryption key that is used to protect the backups.  **Returned:** success  **Sample:** `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"` |
| **lock_date**  string | The date and time when Backup Vault Lock configuration cannot be changed or deleted.  **Returned:** success  **Sample:** `"1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM."` |
| **locked**  boolean | Indicates whether Backup Vault Lock is currently protecting the backup vault.  True means that Vault Lock causes delete or update operations on the recovery points stored in the vault to fail.  **Returned:** success  **Sample:** `true` |
| **max_retention_days**  integer | The maximum retention period that the vault retains its recovery points.  If this parameter is not specified, Vault Lock does not enforce a maximum retention period (allowing indefinite storage).  **Returned:** success  **Sample:** `123` |
| **min_retention_days**  integer | The minimum retention period that the vault retains its recovery points.  If this parameter is not specified, Vault Lock does not enforce a minimum retention period.  **Returned:** success  **Sample:** `120` |
| **number_of_recovery_points**  integer | The number of recovery points that are stored in a backup vault.  **Returned:** success |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
