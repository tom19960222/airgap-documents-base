---
collection: ansible
version: "8"
title: "amazon.aws.ec2_snapshot_info module – Gathers information about EC2 volume snapshots in AWS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_snapshot_info_module.html
fetched_at: 2026-07-28T01:06:31+00:00
---
# amazon.aws.ec2_snapshot_info module – Gathers information about EC2 volume snapshots in AWS

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
> see [Requirements](ec2_snapshot_info_module.md#ansible-collections-amazon-aws-ec2-snapshot-info-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_snapshot_info`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_snapshot_info_module.md#synopsis)
- [Requirements](ec2_snapshot_info_module.md#requirements)
- [Parameters](ec2_snapshot_info_module.md#parameters)
- [Notes](ec2_snapshot_info_module.md#notes)
- [Examples](ec2_snapshot_info_module.md#examples)
- [Return Values](ec2_snapshot_info_module.md#return-values)

## [Synopsis](ec2_snapshot_info_module.md#id1)

- Gathers information about EC2 volume snapshots in AWS.

## [Requirements](ec2_snapshot_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_snapshot_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html> for possible filters. Filter names and values are case sensitive.  **Default:** `{}` |
| **max_results**  integer | The maximum number of snapshot results returned in paginated output.  When used only a single page along with a `next_token_id` response element will be returned.  The remaining results of the initial request can be seen by sending another request with the returned `next_token_id` value.  This value can be between 5 and 1000; if *next_token_id* is given a value larger than 1000, only 1000 results are returned.  If this parameter is not used, then DescribeSnapshots returns all results.  This parameter is mutually exclusive with *snapshot_ids*. |
| **next_token_id**  string | Contains the value returned from a previous paginated request where *max_results* was used and the results exceeded the value of that parameter.  Pagination continues from the end of the previous results that returned the *next_token_id* value.  This parameter is mutually exclusive with *snapshot_ids* |
| **owner_ids**  list / elements=string | If you specify one or more snapshot owners, only snapshots from the specified owners and for which you have access are returned.  **Default:** `[]` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **restorable_by_user_ids**  list / elements=string | If you specify a list of restorable users, only snapshots with create snapshot permissions for those users are returned.  **Default:** `[]` |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **snapshot_ids**  list / elements=string | If you specify one or more snapshot IDs, only snapshots that have the specified IDs are returned.  **Default:** `[]` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ec2_snapshot_info_module.md#id4)

> **Note:**
>
> - By default, the module will return all snapshots, including public ones. To limit results to snapshots owned by the account use the filter ‘owner-id’.
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_snapshot_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather information about all snapshots, including public ones
- amazon.aws.ec2_snapshot_info:

# Gather information about all snapshots owned by the account 123456789012
- amazon.aws.ec2_snapshot_info:
    filters:
      owner-id: 123456789012

# Or alternatively...
- amazon.aws.ec2_snapshot_info:
    owner_ids:
      - 123456789012

# Gather information about a particular snapshot using ID
- amazon.aws.ec2_snapshot_info:
    filters:
      snapshot-id: snap-00112233

# Or alternatively...
- amazon.aws.ec2_snapshot_info:
    snapshot_ids:
      - snap-00112233

# Gather information about any snapshot with a tag key Name and value Example
- amazon.aws.ec2_snapshot_info:
    filters:
      "tag:Name": Example

# Gather information about any snapshot with an error status
- amazon.aws.ec2_snapshot_info:
    filters:
      status: error
```

## [Return Values](ec2_snapshot_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **next_token_id**  string | Contains the value returned from a previous paginated request where `max_results` was used and the results exceeded the value of that parameter.  This value is null when there are no more results to return.  **Returned:** when option `max_results` is set in input |
| **snapshots**  list / elements=dictionary | List of snapshots retrieved with their respective info.  **Returned:** success |
| **create_volume_permissions**  list / elements=dictionary | The users and groups that have the permissions for creating volumes from the snapshot.  The module will return empty list if the create volume permissions on snapshot are ‘private’.  **Returned:** success  **Sample:** `[{"group": "all"}]` |
| **data_encryption_key_id**  string | The data encryption key identifier for the snapshot. This value is a unique identifier that corresponds to the data encryption key that was used to encrypt the original volume or snapshot copy.  **Returned:** always  **Sample:** `"arn:aws:kms:ap-southeast-2:123456789012:key/74c9742a-a1b2-45cb-b3fe-abcdef123456"` |
| **description**  string | The description for the snapshot.  **Returned:** always  **Sample:** `"My important backup"` |
| **encrypted**  boolean | Indicates whether the snapshot is encrypted.  **Returned:** always  **Sample:** `true` |
| **kms_key_id**  string | The full ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the volume encryption key for the parent volume.  **Returned:** always  **Sample:** `"74c9742a-a1b2-45cb-b3fe-abcdef123456"` |
| **owner_alias**  string | The AWS account alias (for example, amazon, self) or AWS account ID that owns the snapshot.  **Returned:** always  **Sample:** `"123456789012"` |
| **owner_id**  string | The AWS account ID of the EBS snapshot owner.  **Returned:** always  **Sample:** `"123456789012"` |
| **progress**  string | The progress of the snapshot, as a percentage.  **Returned:** always  **Sample:** `"100%"` |
| **snapshot_id**  string | The ID of the snapshot. Each snapshot receives a unique identifier when it is created.  **Returned:** always  **Sample:** `"snap-01234567"` |
| **start_time**  string | The time stamp when the snapshot was initiated.  **Returned:** always  **Sample:** `"2015-02-12T02:14:02+00:00"` |
| **state**  string | The snapshot state (completed, pending or error).  **Returned:** always  **Sample:** `"completed"` |
| **state_message**  string | Encrypted Amazon EBS snapshots are copied asynchronously. If a snapshot copy operation fails (for example, if the proper AWS Key Management Service (AWS KMS) permissions are not obtained) this field displays error state details to help you diagnose why the error occurred.  **Returned:** always |
| **tags**  dictionary | Any tags assigned to the snapshot.  **Returned:** always  **Sample:** `{"my_tag_key": "my_tag_value"}` |
| **volume_id**  string | The ID of the volume that was used to create the snapshot.  **Returned:** always  **Sample:** `"vol-01234567"` |
| **volume_size**  integer | The size of the volume, in GiB.  **Returned:** always  **Sample:** `8` |

### Authors

- Rob White (@wimnat)
- Aubin Bikouo (@abikouo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
