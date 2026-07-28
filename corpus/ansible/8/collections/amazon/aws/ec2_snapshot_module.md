---
collection: ansible
version: "8"
title: "amazon.aws.ec2_snapshot module – Creates a snapshot from an existing volume"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_snapshot_module.html
fetched_at: 2026-07-28T01:06:31+00:00
---
# amazon.aws.ec2_snapshot module – Creates a snapshot from an existing volume

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
> see [Requirements](ec2_snapshot_module.md#ansible-collections-amazon-aws-ec2-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_snapshot`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_snapshot_module.md#synopsis)
- [Requirements](ec2_snapshot_module.md#requirements)
- [Parameters](ec2_snapshot_module.md#parameters)
- [Notes](ec2_snapshot_module.md#notes)
- [Examples](ec2_snapshot_module.md#examples)
- [Return Values](ec2_snapshot_module.md#return-values)

## [Synopsis](ec2_snapshot_module.md#id1)

- Creates an EC2 snapshot from an existing EBS volume.

## [Requirements](ec2_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Description to be applied to the snapshot. |
| **device_name**  string | Device name of a mounted volume to be snapshotted. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **group_names**  list / elements=string  *added in amazon.aws 6.1.0* | The group to be added or removed. The possible value is `all`.  Mutually exclusive with *user_ids*.  **Choices:**   - `"all"` |
| **instance_id**  string | Instance that has the required volume to snapshot mounted. |
| **last_snapshot_min_age**  integer | If the volume’s most recent snapshot has started less than *last_snapshot_min_age* minutes ago, a new snapshot will not be created.  **Default:** `0` |
| **modify_create_vol_permission**  boolean  *added in amazon.aws 6.1.0* | If set to `true`, ec2 snapshot’s createVolumePermissions can be modified.  **Choices:**   - `false` - `true` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_create_vol_permission**  boolean  *added in amazon.aws 6.1.0* | Whether unspecified group names or user IDs should be removed from the snapshot createVolumePermission.  Must set *modify_create_vol_permission* to `True` for when *purge_create_vol_permission* is set to `True`.  **Choices:**   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **snapshot_id**  string | Snapshot id to remove. |
| **snapshot_tags**  dictionary | A dictionary of tags to add to the snapshot.  If the volume has a `Name` tag this will be automatically added to the snapshot.  **Default:** `{}` |
| **state**  string | Whether to add or create a snapshot.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **user_ids**  list / elements=string  *added in amazon.aws 6.1.0* | The account user IDs to be added or removed.  If createVolumePermission on snapshot is currently set to Public i.e. *group_names=all*, providing *user_ids* will not make createVolumePermission Private unless *create_volume_permission* is set to `true`.  Mutually exclusive with *group_names*. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **volume_id**  string | Volume from which to take the snapshot. |
| **wait**  boolean | Wait for the snapshot to be ready.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before wait gives up, in seconds.  **Default:** `600` |

## [Notes](ec2_snapshot_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_snapshot_module.md#id5)

```yaml+jinja
# Simple snapshot of volume using volume_id
- amazon.aws.ec2_snapshot:
    volume_id: vol-abcdef12
    description: snapshot of /data from DB123 taken 2013/11/28 12:18:32

# Snapshot of volume mounted on device_name attached to instance_id
- amazon.aws.ec2_snapshot:
    instance_id: i-12345678
    device_name: /dev/sdb1
    description: snapshot of /data from DB123 taken 2013/11/28 12:18:32

# Snapshot of volume with tagging
- amazon.aws.ec2_snapshot:
    instance_id: i-12345678
    device_name: /dev/sdb1
    snapshot_tags:
        frequency: hourly
        source: /data

# Remove a snapshot
- amazon.aws.ec2_snapshot:
    snapshot_id: snap-abcd1234
    state: absent

# Create a snapshot only if the most recent one is older than 1 hour
- amazon.aws.ec2_snapshot:
    volume_id: vol-abcdef12
    last_snapshot_min_age: 60

- name: Reset snapshot createVolumePermission (change permission to "Private")
  amazon.aws.ec2_snapshot:
    snapshot_id: snap-06a6f641234567890
    modify_create_vol_permission: true
    purge_create_vol_permission: true

- name: Modify snapshot createVolmePermission to add user IDs (specify purge_create_vol_permission=true to change permssion to "Private")
  amazon.aws.ec2_snapshot:
    snapshot_id: snap-06a6f641234567890
    modify_create_vol_permission: true
    user_ids:
      - '123456789012'
      - '098765432109'

- name: Modify snapshot createVolmePermission - remove all except specified user_ids
  amazon.aws.ec2_snapshot:
    snapshot_id: snap-06a6f641234567890
    modify_create_vol_permission: true
    purge_create_vol_permission: true
    user_ids:
      - '123456789012'

- name: Replace (purge existing) snapshot createVolmePermission annd add user IDs
  amazon.aws.ec2_snapshot:
    snapshot_id: snap-06a6f641234567890
    modify_create_vol_permission: true
    purge_create_vol_permission: true
    user_ids:
      - '111111111111'

- name: Modify snapshot createVolmePermission - make createVolumePermission "Public"
  amazon.aws.ec2_snapshot:
    snapshot_id: snap-06a6f641234567890
    modify_create_vol_permission: true
    purge_create_vol_permission: true
    group_names:
      - all
```

## [Return Values](ec2_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **snapshot_id**  string | The ID of the snapshot. Each snapshot receives a unique identifier when it is created.  **Returned:** always  **Sample:** `"snap-01234567"` |
| **tags**  dictionary | Any tags assigned to the snapshot.  **Returned:** always  **Sample:** `{"Name": "instance-name"}` |
| **volume_id**  string | The ID of the volume that was used to create the snapshot.  **Returned:** always  **Sample:** `"vol-01234567"` |
| **volume_size**  integer | The size of the volume, in GiB.  **Returned:** always  **Sample:** `8` |

### Authors

- Will Thames (@willthames)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
