---
collection: ansible
version: "6"
title: "amazon.aws.ec2_snapshot_info module – Gathers information about EC2 volume snapshots in AWS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_snapshot_info_module.html
fetched_at: 2026-07-27T16:43:46+00:00
---
# amazon.aws.ec2_snapshot_info module – Gathers information about EC2 volume snapshots in AWS

> **Note:**
>
> This module is part of the [amazon.aws collection](https://galaxy.ansible.com/amazon/aws) (version 3.5.0).
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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_snapshot_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **filters**  dictionary | A dict of filters to apply. Each dict item consists of a filter key and a filter value. See <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSnapshots.html> for possible filters. Filter names and values are case sensitive.  Default: `{}` |
| **max_results**  integer | The maximum number of snapshot results returned in paginated output.  When used only a single page along with a `next_token_id` response element will be returned.  The remaining results of the initial request can be seen by sending another request with the returned `next_token_id` value.  This value can be between 5 and 1000; if *next_token_id* is given a value larger than 1000, only 1000 results are returned.  If this parameter is not used, then DescribeSnapshots returns all results.  This parameter is mutually exclusive with *snapshot_ids*. |
| **next_token_id**  string | Contains the value returned from a previous paginated request where *max_results* was used and the results exceeded the value of that parameter.  Pagination continues from the end of the previous results that returned the *next_token_id* value.  This parameter is mutually exclusive with *snapshot_ids* |
| **owner_ids**  list / elements=string | If you specify one or more snapshot owners, only snapshots from the specified owners and for which you have access are returned.  Default: `[]` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **restorable_by_user_ids**  list / elements=string | If you specify a list of restorable users, only snapshots with create snapshot permissions for those users are returned.  Default: `[]` |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **snapshot_ids**  list / elements=string | If you specify one or more snapshot IDs, only snapshots that have the specified IDs are returned.  Default: `[]` |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |

## [Notes](ec2_snapshot_info_module.md#id4)

> **Note:**
>
> - By default, the module will return all snapshots, including public ones. To limit results to snapshots owned by the account use the filter ‘owner-id’.
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_snapshot_info_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

# Gather information about all snapshots, including public ones
- amazon.aws.ec2_snapshot_info:

# Gather information about all snapshots owned by the account 0123456789
- amazon.aws.ec2_snapshot_info:
    filters:
      owner-id: 0123456789

# Or alternatively...
- amazon.aws.ec2_snapshot_info:
    owner_ids:
      - 0123456789

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
| **next_token_id**  string | Contains the value returned from a previous paginated request where `max_results` was used and the results exceeded the value of that parameter.  This value is null when there are no more results to return.  Returned: when option `max_results` is set in input |
| **snapshots**  list / elements=dictionary | snapshots retrieved  Returned: success |
| **data_encryption_key_id**  string | The data encryption key identifier for the snapshot. This value is a unique identifier that corresponds to the data encryption key that was used to encrypt the original volume or snapshot copy.  Returned: always  Sample: `"arn:aws:kms:ap-southeast-2:012345678900:key/74c9742a-a1b2-45cb-b3fe-abcdef123456"` |
| **description**  string | The description for the snapshot.  Returned: always  Sample: `"My important backup"` |
| **encrypted**  boolean | Indicates whether the snapshot is encrypted.  Returned: always  Sample: `true` |
| **kms_key_id**  string | The full ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) that was used to protect the volume encryption key for the parent volume.  Returned: always  Sample: `"74c9742a-a1b2-45cb-b3fe-abcdef123456"` |
| **owner_alias**  string | The AWS account alias (for example, amazon, self) or AWS account ID that owns the snapshot.  Returned: always  Sample: `"033440102211"` |
| **owner_id**  string | The AWS account ID of the EBS snapshot owner.  Returned: always  Sample: `"099720109477"` |
| **progress**  string | The progress of the snapshot, as a percentage.  Returned: always  Sample: `"100%"` |
| **snapshot_id**  string | The ID of the snapshot. Each snapshot receives a unique identifier when it is created.  Returned: always  Sample: `"snap-01234567"` |
| **start_time**  string | The time stamp when the snapshot was initiated.  Returned: always  Sample: `"2015-02-12T02:14:02+00:00"` |
| **state**  string | The snapshot state (completed, pending or error).  Returned: always  Sample: `"completed"` |
| **state_message**  string | Encrypted Amazon EBS snapshots are copied asynchronously. If a snapshot copy operation fails (for example, if the proper AWS Key Management Service (AWS KMS) permissions are not obtained) this field displays error state details to help you diagnose why the error occurred.  Returned: always |
| **tags**  dictionary | Any tags assigned to the snapshot.  Returned: always  Sample: `{"my_tag_key": "my_tag_value"}` |
| **volume_id**  string | The ID of the volume that was used to create the snapshot.  Returned: always  Sample: `"vol-01234567"` |
| **volume_size**  integer | The size of the volume, in GiB.  Returned: always  Sample: `8` |

### Authors

- Rob White (@wimnat)
- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
