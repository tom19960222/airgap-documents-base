---
collection: ansible
version: "6"
title: "amazon.aws.ec2_vol module – Create and attach a volume, return volume id and device map"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_vol_module.html
fetched_at: 2026-07-27T16:43:47+00:00
---
# amazon.aws.ec2_vol module – Create and attach a volume, return volume id and device map

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
> see [Requirements](ec2_vol_module.md#ansible-collections-amazon-aws-ec2-vol-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_vol`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_vol_module.md#synopsis)
- [Requirements](ec2_vol_module.md#requirements)
- [Parameters](ec2_vol_module.md#parameters)
- [Notes](ec2_vol_module.md#notes)
- [Examples](ec2_vol_module.md#examples)
- [Return Values](ec2_vol_module.md#return-values)

## [Synopsis](ec2_vol_module.md#id1)

- Creates an EBS volume and optionally attaches it to an instance.
- If both *instance* and *name* are given and the instance has a device at the device name, then no volume is created and no attachment is made.

## [Requirements](ec2_vol_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_vol_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delete_on_termination**  boolean | When set to `true`, the volume will be deleted upon instance termination.  Choices:   - `false` ← (default) - `true` |
| **device_name**  string | Device id to override device mapping. Assumes /dev/sdf for Linux/UNIX and /dev/xvdf for Windows. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **encrypted**  boolean | Enable encryption at rest for this volume.  Choices:   - `false` ← (default) - `true` |
| **id**  string | Volume id if you wish to attach an existing volume (requires instance) or remove an existing volume |
| **instance**  string | Instance ID if you wish to attach the volume. Since 1.9 you can set to None to detach. |
| **iops**  integer | The provisioned IOPs you want to associate with this volume (integer). |
| **kms_key_id**  string | Specify the id of the KMS key to use. |
| **modify_volume**  boolean  added in amazon.aws 1.4.0 | The volume won’t be modified unless this key is `true`.  Choices:   - `false` ← (default) - `true` |
| **multi_attach**  boolean  added in amazon.aws 2.0.0 | If set to `yes`, Multi-Attach will be enabled when creating the volume.  When you create a new volume, Multi-Attach is disabled by default.  This parameter is supported with io1 and io2 volumes only.  Choices:   - `false` - `true` |
| **name**  string | Volume Name tag if you wish to attach an existing volume (requires instance) |
| **outpost_arn**  string  added in amazon.aws 3.1.0 | The Amazon Resource Name (ARN) of the Outpost.  If set, allows to create volume in an Outpost. |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean  added in amazon.aws 1.5.0 | Whether to remove existing tags that aren’t passed in the *tags* parameter  Choices:   - `false` ← (default) - `true` |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **snapshot**  string | Snapshot ID on which to base the volume. |
| **state**  string | Whether to ensure the volume is present or absent.  The use of *state=list* to interrogate the volume has been deprecated and will be removed after 2022-06-01. The ‘list’ functionality has been moved to a dedicated module [amazon.aws.ec2_vol_info](ec2_vol_info_module.md#ansible-collections-amazon-aws-ec2-vol-info-module).  Choices:   - `"absent"` - `"present"` ← (default) - `"list"` |
| **tags**  dictionary | <tag:value> pairs to add to the volume after creation.  Default: `{}` |
| **throughput**  integer  added in amazon.aws 1.4.0 | Volume throughput in MB/s.  This parameter is only valid for gp3 volumes.  Valid range is from 125 to 1000.  Requires at least botocore version 1.19.27. |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **volume_size**  integer | Size of volume (in GiB) to create. |
| **volume_type**  string | Type of EBS volume; standard (magnetic), gp2 (SSD), gp3 (SSD), io1 (Provisioned IOPS), io2 (Provisioned IOPS), st1 (Throughput Optimized HDD), sc1 (Cold HDD). “Standard” is the old EBS default and continues to remain the Ansible default for backwards compatibility.  Choices:   - `"standard"` ← (default) - `"gp2"` - `"io1"` - `"st1"` - `"sc1"` - `"gp3"` - `"io2"` |
| **zone**  aliases: availability_zone, aws_zone, ec2_zone  string | Zone in which to create the volume, if unset uses the zone the instance is in (if set). |

## [Notes](ec2_vol_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_vol_module.md#id5)

```yaml+jinja
# Simple attachment action
- amazon.aws.ec2_vol:
    instance: XXXXXX
    volume_size: 5
    device_name: sdd
    region: us-west-2

# Example using custom iops params
- amazon.aws.ec2_vol:
    instance: XXXXXX
    volume_size: 5
    iops: 100
    device_name: sdd
    region: us-west-2

# Example using snapshot id
- amazon.aws.ec2_vol:
    instance: XXXXXX
    snapshot: "{{ snapshot }}"

# Playbook example combined with instance launch
- amazon.aws.ec2:
    keypair: "{{ keypair }}"
    image: "{{ image }}"
    wait: yes
    count: 3
  register: ec2
- amazon.aws.ec2_vol:
    instance: "{{ item.id }}"
    volume_size: 5
  loop: "{{ ec2.instances }}"
  register: ec2_vol

# Example: Launch an instance and then add a volume if not already attached
#   * Volume will be created with the given name if not already created.
#   * Nothing will happen if the volume is already attached.

- amazon.aws.ec2:
    keypair: "{{ keypair }}"
    image: "{{ image }}"
    zone: YYYYYY
    id: my_instance
    wait: yes
    count: 1
  register: ec2

- amazon.aws.ec2_vol:
    instance: "{{ item.id }}"
    name: my_existing_volume_Name_tag
    device_name: /dev/xvdf
  loop: "{{ ec2.instances }}"
  register: ec2_vol

# Remove a volume
- amazon.aws.ec2_vol:
    id: vol-XXXXXXXX
    state: absent

# Detach a volume (since 1.9)
- amazon.aws.ec2_vol:
    id: vol-XXXXXXXX
    instance: None
    region: us-west-2

# List volumes for an instance
- amazon.aws.ec2_vol:
    instance: i-XXXXXX
    state: list
    region: us-west-2

# Create new volume using SSD storage
- amazon.aws.ec2_vol:
    instance: XXXXXX
    volume_size: 50
    volume_type: gp2
    device_name: /dev/xvdf

# Create new volume with multi-attach enabled
- amazon.aws.ec2_vol:
    zone: XXXXXX
    multi_attach: true
    volume_size: 4
    volume_type: io1
    iops: 102

# Attach an existing volume to instance. The volume will be deleted upon instance termination.
- amazon.aws.ec2_vol:
    instance: XXXXXX
    id: XXXXXX
    device_name: /dev/sdf
    delete_on_termination: yes
```

## [Return Values](ec2_vol_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **device**  string | device name of attached volume  Returned: when success  Sample: `"/def/sdf"` |
| **volume**  string | a dictionary containing detailed attributes of the volume  Returned: when success  Sample: `"{'attachment_set': [{'attach_time': '2015-10-23T00:22:29.000Z', 'deleteOnTermination': 'false', 'device': '/dev/sdf', 'instance_id': 'i-8356263c', 'status': 'attached'}], 'create_time': '2015-10-21T14:36:08.870Z', 'encrypted': False, 'id': 'vol-35b333d9', 'iops': None, 'size': 1, 'snapshot_id': '', 'status': 'in-use', 'tags': {'env': 'dev'}, 'type': 'standard', 'zone': 'us-east-1b'}"` |
| **volume_id**  string | the id of volume  Returned: when success  Sample: `"vol-35b333d9"` |
| **volume_type**  string | the volume type  Returned: when success  Sample: `"standard"` |

### Authors

- Lester Wade (@lwade)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
