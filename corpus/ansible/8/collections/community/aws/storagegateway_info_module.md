---
collection: ansible
version: "8"
title: "community.aws.storagegateway_info module – Fetch AWS Storage Gateway information"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/aws/storagegateway_info_module.html
fetched_at: 2026-07-28T01:42:02+00:00
---
# community.aws.storagegateway_info module – Fetch AWS Storage Gateway information

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
> see [Requirements](storagegateway_info_module.md#ansible-collections-community-aws-storagegateway-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.aws.storagegateway_info`.

New in community.aws 1.0.0

- [Synopsis](storagegateway_info_module.md#synopsis)
- [Requirements](storagegateway_info_module.md#requirements)
- [Parameters](storagegateway_info_module.md#parameters)
- [Notes](storagegateway_info_module.md#notes)
- [Examples](storagegateway_info_module.md#examples)
- [Return Values](storagegateway_info_module.md#return-values)

## [Synopsis](storagegateway_info_module.md#id1)

- Fetch AWS Storage Gateway information
- Prior to release 5.0.0 this module was called `community.aws.aws_sgw_info`. The usage did not change.

Aliases: aws_sgw_info

## [Requirements](storagegateway_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](storagegateway_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **gather_file_shares**  boolean | Gather file share information for storage gateways in s3 mode.  **Choices:**   - `false` - `true` ← (default) |
| **gather_local_disks**  boolean | Gather local disks attached to the storage gateway.  **Choices:**   - `false` - `true` ← (default) |
| **gather_tapes**  boolean | Gather tape information for storage gateways in tape mode.  **Choices:**   - `false` - `true` ← (default) |
| **gather_volumes**  boolean | Gather volume information for storage gateways in iSCSI (cached & stored) modes.  **Choices:**   - `false` - `true` ← (default) |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](storagegateway_info_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](storagegateway_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: "Get AWS storage gateway information"
  community.aws.storagegateway_info:

- name: "Get AWS storage gateway information for region eu-west-3"
  community.aws.storagegateway_info:
    region: eu-west-3
```

## [Return Values](storagegateway_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **gateways**  complex | list of gateway objects  **Returned:** always |
| **file_shares**  complex | Storage gateway file shares  **Returned:** when gateway_type == “FILE_S3” |
| **file_share_arn**  string | File share ARN  **Returned:** always  **Sample:** `"arn:aws:storagegateway:eu-west-1:123456789012:share/share-AF999C88"` |
| **file_share_id**  string | File share ID  **Returned:** always  **Sample:** `"share-AF999C88"` |
| **file_share_status**  string | File share status  **Returned:** always  **Sample:** `"AVAILABLE"` |
| **gateway_arn**  string | Storage Gateway ARN  **Returned:** always  **Sample:** `"arn:aws:storagegateway:eu-west-1:123456789012:gateway/sgw-9999F888"` |
| **gateway_id**  string | Storage Gateway ID  **Returned:** always  **Sample:** `"sgw-9999F888"` |
| **gateway_name**  string | Storage Gateway friendly name  **Returned:** always  **Sample:** `"my-sgw-01"` |
| **gateway_operational_state**  string | Storage Gateway operational state  **Returned:** always  **Sample:** `"ACTIVE"` |
| **gateway_type**  string | Storage Gateway type  **Returned:** always  **Sample:** `"FILE_S3"` |
| **local_disks**  complex | Storage gateway local disks  **Returned:** always |
| **disk_allocation_type**  string | Disk allocation type  **Returned:** always  **Sample:** `"CACHE STORAGE"` |
| **disk_id**  string | Disk ID on the system  **Returned:** always  **Sample:** `"pci-0000:00:1f.0"` |
| **disk_node**  string | Disk parent block device  **Returned:** always  **Sample:** `"/dev/sdb"` |
| **disk_path**  string | Disk path used for the cache  **Returned:** always  **Sample:** `"/dev/nvme1n1"` |
| **disk_size_in_bytes**  integer | Disk size in bytes  **Returned:** always  **Sample:** `107374182400` |
| **disk_status**  string | Disk status  **Returned:** always  **Sample:** `"present"` |
| **tapes**  complex | Storage Gateway tapes  **Returned:** when gateway_type == “VTL” |
| **tape_arn**  string | Tape ARN  **Returned:** always  **Sample:** `"arn:aws:storagegateway:eu-west-1:123456789012:tape/tape-AF999C88"` |
| **tape_barcode**  string | Tape ARN  **Returned:** always  **Sample:** `"tape-AF999C88"` |
| **tape_size_in_bytes**  integer | Tape ARN  **Returned:** always  **Sample:** `555887569` |
| **tape_status**  string | Tape ARN  **Returned:** always  **Sample:** `"AVAILABLE"` |

### Authors

- Loic Blot (@nerzhul)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/community.aws)
- [Communication](index.md#communication-for-community-aws)
