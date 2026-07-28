---
collection: ansible
version: "8"
title: "amazon.aws.backup_plan module – Manage AWS Backup Plans"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/backup_plan_module.html
fetched_at: 2026-07-28T01:06:07+00:00
---
# amazon.aws.backup_plan module – Manage AWS Backup Plans

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
> see [Requirements](backup_plan_module.md#ansible-collections-amazon-aws-backup-plan-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.backup_plan`.

New in amazon.aws 6.0.0

- [Synopsis](backup_plan_module.md#synopsis)
- [Requirements](backup_plan_module.md#requirements)
- [Parameters](backup_plan_module.md#parameters)
- [Notes](backup_plan_module.md#notes)
- [Examples](backup_plan_module.md#examples)
- [Return Values](backup_plan_module.md#return-values)

## [Synopsis](backup_plan_module.md#id1)

- Creates, updates, or deletes AWS Backup Plans
- For more information see the AWS documentation for Backup plans <https://docs.aws.amazon.com/aws-backup/latest/devguide/about-backup-plans.html>.

## [Requirements](backup_plan_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](backup_plan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **advanced_backup_settings**  list / elements=dictionary | Specifies a list of advanced backup settings for each resource type.  These settings are only available for Windows Volume Shadow Copy Service (VSS) backup jobs. |
| **backup_options**  dictionary | Specifies the backup option for a selected resource.  This option is only available for Windows VSS backup jobs.  **Choices:**   - `{"WindowsVSS": "enabled"}` - `{"WindowsVSS": "disabled"}` |
| **resource_type**  string | Specifies an object containing resource type and backup options.  The only supported resource type is Amazon EC2 instances with Windows Volume Shadow Copy Service (VSS).  **Choices:**   - `"EC2"` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **backup_plan_name**  aliases: name  string / required | The display name of a backup plan. Must contain 1 to 50 alphanumeric or ‘-_.’ characters. |
| **creator_request_id**  string | Identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a CreatorRequestId that matches an existing backup plan, that plan is returned. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **rules**  list / elements=dictionary | An array of BackupRule objects, each of which specifies a scheduled task that is used to back up a selection of resources.  Required when *state=present*. |
| **completion_window_minutes**  integer | A value in minutes after a backup job is successfully started before it must be completed or it will be canceled by Backup.  AWS default if not supplied is 10080  **Default:** `10080` |
| **copy_actions**  list / elements=dictionary | An array of copy_action objects, which contains the details of the copy operation. |
| **destination_backup_vault_arn**  string / required | An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. |
| **lifecycle**  dictionary | Contains an array of Transition objects specifying how long in days before a recovery point transitions to cold storage or is deleted.  Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. |
| **delete_after_days**  integer | Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus move_to_cold_storage_after_days. |
| **move_to_cold_storage_after_days**  integer | Specifies the number of days after creation that a recovery point is moved to cold storage. |
| **enable_continuous_backup**  boolean | Specifies whether Backup creates continuous backups. True causes Backup to create continuous backups capable of point-in-time restore (PITR). False (or not specified) causes Backup to create snapshot backups.  AWS default if not supplied is false.  **Choices:**   - `false` ← (default) - `true` |
| **lifecycle**  dictionary | The lifecycle defines when a protected resource is transitioned to cold storage and when it expires. Backup will transition and expire backups automatically according to the lifecycle that you define.  Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, the “retention” setting must be 90 days greater than the “transition to cold after days” setting. The “transition to cold after days” setting cannot be changed after a backup has been transitioned to cold. |
| **delete_after_days**  integer | Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus move_to_cold_storage_after_days. |
| **move_to_cold_storage_after_days**  integer | Specifies the number of days after creation that a recovery point is moved to cold storage. |
| **recovery_point_tags**  dictionary | To help organize your resources, you can assign your own metadata to the resources that you create. |
| **rule_name**  string / required | Name of the rule. |
| **schedule_expression**  string | A CRON expression in UTC specifying when Backup initiates a backup job. AWS default is used if not supplied.  **Default:** `"cron(0 5 ? * * *)"` |
| **start_window_minutes**  integer | A value in minutes after a backup is scheduled before a job will be canceled if it doesn’t start successfully. If this value is included, it must be at least 60 minutes to avoid errors.  AWS default if not supplied is 480.  **Default:** `480` |
| **target_backup_vault_name**  string / required | Name of the Backup Vault this rule should target. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **state**  string | Create/update or delete a backup plan.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: resource_tags, backup_plan_tags  dictionary | To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. The specified tags are assigned to all backups created with this plan. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](backup_plan_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](backup_plan_module.md#id5)

```yaml+jinja
- name: Create an AWSbackup plan
  amazon.aws.backup_plan:
    state: present
    backup_plan_name: elastic
    rules:
      - rule_name: daily
        target_backup_vault_name: "{{ backup_vault_name }}"
        schedule_expression: 'cron(0 5 ? * * *)'
        start_window_minutes: 60
        completion_window_minutes: 1440
- name: Delete an AWS Backup plan
  amazon.aws.backup_plan:
    backup_plan_name: elastic
    state: absent
```

## [Return Values](backup_plan_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_plan**  dictionary | Backup plan details.  **Returned:** on create/update |
| **advanced_backup_settings**  list / elements=dictionary | Advanced backup settings of the backup plan.  **Returned:** when configured |
| **backup_options**  dictionary | Backup options of the advanced settings.  **Returned:** success |
| **resource_type**  string | Resource type of the advanced settings.  **Returned:** success |
| **backup_plan_name**  string | Name of the backup plan.  **Returned:** always  **Sample:** `"elastic"` |
| **rules**  list / elements=dictionary | An array of BackupRule objects, each of which specifies a scheduled task that is used to back up a selection of resources.  **Returned:** always |
| **tags**  string | Tags of the backup plan.  **Returned:** on create/update |
| **backup_plan_arn**  string | ARN of the backup plan.  **Returned:** always  **Sample:** `"arn:aws:backup:eu-central-1:111122223333:backup-plan:1111f877-1ecf-4d79-9718-a861cd09df3b"` |
| **backup_plan_id**  string | ID of the backup plan.  **Returned:** always  **Sample:** `"1111f877-1ecf-4d79-9718-a861cd09df3b"` |
| **backup_plan_name**  string | Name of the backup plan.  **Returned:** always  **Sample:** `"elastic"` |
| **creation_date**  string | Creation date of the backup plan.  **Returned:** on create/update  **Sample:** `"2023-01-24T10:08:03.193000+01:00"` |
| **deletion_date**  string | Date the backup plan was deleted.  **Returned:** on delete  **Sample:** `"2023-05-05T16:24:51.987000-04:00"` |
| **exists**  boolean | Whether the resource exists.  **Returned:** always  **Sample:** `true` |
| **version_id**  string | Version ID of the backup plan.  **Returned:** always  **Sample:** `"ODM3MjVjNjItYWFkOC00NjExLWIwZTYtZDNiNGI5M2I0ZTY1"` |

### Authors

- Kristof Imre Szabo (@krisek)
- Alina Buzachis (@alinabuzachis)
- Helen Bailey (@hakbailey)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
