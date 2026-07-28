---
collection: ansible
version: "6"
title: "amazon.aws.ec2_snapshot module – Creates a snapshot from an existing volume"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_snapshot_module.html
fetched_at: 2026-07-27T16:43:45+00:00
---
# amazon.aws.ec2_snapshot module – Creates a snapshot from an existing volume

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
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Description to be applied to the snapshot. |
| **device_name**  string | Device name of a mounted volume to be snapshotted. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **instance_id**  string | Instance that has the required volume to snapshot mounted. |
| **last_snapshot_min_age**  integer | If the volume’s most recent snapshot has started less than *last_snapshot_min_age* minutes ago, a new snapshot will not be created.  Default: `0` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **snapshot_id**  string | Snapshot id to remove. |
| **snapshot_tags**  dictionary | A dictionary of tags to add to the snapshot.  If the volume has a `Name` tag this will be automatically added to the snapshot. |
| **state**  string | Whether to add or create a snapshot.  Choices:   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **volume_id**  string | Volume from which to take the snapshot. |
| **wait**  boolean | Wait for the snapshot to be ready.  Choices:   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before wait gives up, in seconds.  Default: `600` |

## [Notes](ec2_snapshot_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

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
```

## [Return Values](ec2_snapshot_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **snapshot_id**  string | The ID of the snapshot. Each snapshot receives a unique identifier when it is created.  Returned: always  Sample: `"snap-01234567"` |
| **tags**  dictionary | Any tags assigned to the snapshot.  Returned: always  Sample: `{"Name": "instance-name"}` |
| **volume_id**  string | The ID of the volume that was used to create the snapshot.  Returned: always  Sample: `"vol-01234567"` |
| **volume_size**  integer | The size of the volume, in GiB.  Returned: always  Sample: `8` |

### Authors

- Will Thames (@willthames)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
