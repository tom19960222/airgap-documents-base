---
collection: ansible
version: "8"
title: "amazon.aws.backup_restore_job_info module – List information about backup restore jobs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/backup_restore_job_info_module.html
fetched_at: 2026-07-28T01:06:08+00:00
---
# amazon.aws.backup_restore_job_info module – List information about backup restore jobs

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
> see [Requirements](backup_restore_job_info_module.md#ansible-collections-amazon-aws-backup-restore-job-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.backup_restore_job_info`.

New in amazon.aws 6.0.0

- [Synopsis](backup_restore_job_info_module.md#synopsis)
- [Requirements](backup_restore_job_info_module.md#requirements)
- [Parameters](backup_restore_job_info_module.md#parameters)
- [Notes](backup_restore_job_info_module.md#notes)
- [Examples](backup_restore_job_info_module.md#examples)
- [Return Values](backup_restore_job_info_module.md#return-values)

## [Synopsis](backup_restore_job_info_module.md#id1)

- List detailed information about AWS Backup restore jobs initiated to restore a saved resource.

## [Requirements](backup_restore_job_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](backup_restore_job_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **account_id**  string | The account ID to list the restore jobs from. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **completed_after**  string | Specified date to filter result based on the restore job completion datetime.  If specified, only the restore jobs created after the specified datetime will be returned.  The date must be in Unix format and Coordinated Universal Time (UTC), example “2023-02-25T00:05:36.309Z”. |
| **completed_before**  string | Specified date to filter result based on the restore job completion datetime.  If specified, only the restore jobs created before the specified datetime will be returned.  The date must be in Unix format and Coordinated Universal Time (UTC), example “2023-02-25T00:05:36.309Z”. |
| **created_after**  string | Specified date to filter result based on the restore job creation datetime.  If specified, only the restore jobs created after the specified datetime will be returned.  The date must be in Unix format and Coordinated Universal Time (UTC), example “2023-02-25T00:05:36.309Z”. |
| **created_before**  string | Specified date to filter result based on the restore job creation datetime.  If specified, only the restore jobs created before the specified datetime will be returned.  The date must be in Unix format and Coordinated Universal Time (UTC), example “2023-02-25T00:05:36.309Z”. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **restore_job_id**  string | ID of the restore job to get information about.  This parameter is mutually exlusive with all other parameters. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **status**  string | Status of restore jobs to filter the result based on job status.  **Choices:**   - `"PENDING"` - `"RUNNING"` - `"COMPLETED"` - `"ABORTED"` - `"FAILED"` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](backup_restore_job_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](backup_restore_job_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: List all restore jobs
  amazon.aws.backup_restore_job_info:

- name: List specific restore job's info by job ID
  amazon.aws.backup_restore_job_info:
    restore_job_id: "52BEE289-xxxx-xxxx-xxxx-47DCAA2E7ACD"

- name: List restore jobs based on Account ID
  amazon.aws.backup_restore_job_info:
    account_id: xx1234567890

- name: List restore jobs based on status and created_before time
  amazon.aws.backup_restore_job_info:
    status: completed
    created_before: "2023-02-25T00:05:36.309Z"
```

## [Return Values](backup_restore_job_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **restore_jobs**  list / elements=dictionary | restore jobs that match the provided filters.  Each element consists of a dict with details related to that restore job.  **Returned:** always |
| **account_id**  string | The account ID that owns the restore job.  **Returned:** if restore job exists  **Sample:** `"123456789012"` |
| **created_resource_arn**  string | An Amazon Resource Name (ARN) that uniquely identifies a resource whose recovery point is being restored.  The format of the ARN depends on the resource type of the backed-up resource.  **Returned:** if restore job exists  **Sample:** `"arn:aws:ec2:us-east-2:xxxxxxxxxx..."` |
| **creation_date**  string | The date and time that a restore job is created, in Unix format and Coordinated Universal Time (UTC).  **Returned:** if restore job exists  **Sample:** `"2023-03-13T15:53:07.172000-07:00"` |
| **iam_role_arn**  string | The IAM role ARN used to create the target recovery point.  **Returned:** if restore job exists  **Sample:** `"arn:aws:ec2:us-east-2:xxxxxxxxxx..."` |
| **percent_done**  string | The estimated percentage that is complete of a job at the time the job status was queried.  **Returned:** if restore job exists  **Sample:** `"0.00%"` |
| **recovery_point_arn**  string | An ARN that uniquely identifies a recovery point.  **Returned:** if restore job exists  **Sample:** `"arn:aws:ec2:us-east-2:xxxxxxxxxx..."` |
| **restore_job_id**  string | The ID of the job that restores a recovery point.  **Returned:** if restore job exists  **Sample:** `"AAAA1234-1D1D-1234-3F8E-1EB111EEEE00"` |
| **status**  string | The state of the job initiated by Backup to restore a recovery point.  **Returned:** if restore job exists  **Sample:** `"COMPLETED"` |

### Authors

- Mandar Vijay Kulkarni (@mandar242)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
