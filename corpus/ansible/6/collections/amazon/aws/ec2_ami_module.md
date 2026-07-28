---
collection: ansible
version: "6"
title: "amazon.aws.ec2_ami module – Create or destroy an image (AMI) in ec2"
source_url: https://docs.ansible.com/projects/ansible/6/collections/amazon/aws/ec2_ami_module.html
fetched_at: 2026-07-27T16:43:41+00:00
---
# amazon.aws.ec2_ami module – Create or destroy an image (AMI) in ec2

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
> see [Requirements](ec2_ami_module.md#ansible-collections-amazon-aws-ec2-ami-module-requirements) for details.
>
> To use it in a playbook, specify: `amazon.aws.ec2_ami`.

New in amazon.aws 1.0.0

- [Synopsis](ec2_ami_module.md#synopsis)
- [Requirements](ec2_ami_module.md#requirements)
- [Parameters](ec2_ami_module.md#parameters)
- [Notes](ec2_ami_module.md#notes)
- [Examples](ec2_ami_module.md#examples)
- [Return Values](ec2_ami_module.md#return-values)

## [Synopsis](ec2_ami_module.md#id1)

- Registers or deregisters ec2 images.

## [Requirements](ec2_ami_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.16.0
- botocore >= 1.19.0

## [Parameters](ec2_ami_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **architecture**  string | The target architecture of the image to register  Default: `"x86_64"` |
| **aws_access_key**  aliases: ec2_access_key, access_key  string | `AWS access key`. If not set then the value of the `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_access_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  Not used by boto 2 based modules.  Note: The CA Bundle is read ‘module’ side and may need to be explicitly copied from the controller if not run locally. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found at <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>.  Only the ‘user_agent’ key is used for boto modules. See <http://boto.cloudhackers.com/en/latest/boto_config_tut.html#boto> for more boto configuration. |
| **aws_secret_key**  aliases: ec2_secret_key, secret_key  string | `AWS secret key`. If not set then the value of the `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *aws_secret_key* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01. |
| **billing_products**  list / elements=string | A list of valid billing codes. To be used with valid accounts by aws marketplace vendors. |
| **debug_botocore_endpoint_logs**  boolean | Use a botocore.endpoint logger to parse the unique (rather than total) “resource:action” API calls made during a task, outputing the set to the resource_actions key in the task results. Use the aws_resource_action callback to output to total list made during a playbook. The ANSIBLE_DEBUG_BOTOCORE_LOGS environment variable may also be used.  Choices:   - `false` ← (default) - `true` |
| **delete_snapshot**  boolean | Delete snapshots when deregistering the AMI.  Choices:   - `false` ← (default) - `true` |
| **description**  string | Human-readable string describing the contents and purpose of the AMI. |
| **device_mapping**  list / elements=dictionary | List of device hashes/dictionaries with custom configurations (same block-device-mapping parameters). |
| **delete_on_termination**  boolean | Whether the device should be automatically deleted when the Instance is terminated.  Choices:   - `false` - `true` |
| **device_name**  aliases: DeviceName  string / required | The device name. For example `/dev/sda`. |
| **encrypted**  boolean | Whether the volume should be encrypted.  Choices:   - `false` - `true` |
| **iops**  integer | When using an `io1` *volume_type* this sets the number of IOPS provisioned for the volume |
| **no_device**  aliases: NoDevice  boolean | Suppresses the specified device included in the block device mapping of the AMI.  Alias `NoDevice` has been deprecated and will be removed after 2022-06-01.  Choices:   - `false` - `true` |
| **snapshot_id**  string | The ID of the Snapshot. |
| **virtual_name**  aliases: VirtualName  string | The virtual name for the device.  See the AWS documentation for more detail <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>.  Alias `VirtualName` has been deprecated and will be removed after 2022-06-01. |
| **volume_size**  aliases: size  integer | The size of the volume (in GiB) |
| **volume_type**  string | The volume type. Defaults to `gp2` when not set. |
| **ec2_url**  aliases: aws_endpoint_url, endpoint_url  string | URL to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used. |
| **enhanced_networking**  boolean | A boolean representing whether enhanced networking with ENA is enabled or not.  Choices:   - `false` - `true` |
| **image_id**  string | Image ID to be deregistered. |
| **image_location**  string | The s3 location of an image to use for the AMI. |
| **instance_id**  string | Instance ID to create the AMI from. |
| **kernel_id**  string | The target kernel id of the image to register. |
| **launch_permissions**  dictionary | Users and groups that should be able to launch the AMI. Expects dictionary with a key of user_ids and/or group_names. user_ids should be a list of account ids. group_name should be a list of groups, “all” is the only acceptable value currently.  You must pass all desired launch permissions if you wish to modify existing launch permissions (passing just groups will remove all users) |
| **name**  string | The name of the new AMI. |
| **no_reboot**  boolean | Flag indicating that the bundling process should not attempt to shutdown the instance before bundling. If this flag is True, the responsibility of maintaining file system integrity is left to the owner of the instance.  Choices:   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | Using *profile* will override *aws_access_key*, *aws_secret_key* and *security_token* and support for passing them at the same time as *profile* has been deprecated.  *aws_access_key*, *aws_secret_key* and *security_token* will be made mutually exclusive with *profile* after 2022-06-01. |
| **purge_tags**  boolean | Whether to remove existing tags that aren’t passed in the `tags` parameter  Choices:   - `false` ← (default) - `true` |
| **ramdisk_id**  string | The ID of the RAM disk. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region> |
| **root_device_name**  string | The root device name of the image to register. |
| **security_token**  aliases: aws_session_token, session_token, aws_security_token, access_token  string | `AWS STS security token`. If not set then the value of the `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variable is used.  If *profile* is set this parameter is ignored.  Passing the *security_token* and *profile* options at the same time has been deprecated and the options will be made mutually exclusive after 2022-06-01.  Aliases *aws_session_token* and *session_token* have been added in version 3.2.0. |
| **sriov_net_support**  string | Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI. |
| **state**  string | Register or deregister an AMI.  Choices:   - `"absent"` - `"present"` ← (default) |
| **tags**  dictionary | A dictionary of tags to add to the new image; ‘{“key”:”value”}’ and ‘{“key”:”value”,”key”:”value”}’ |
| **validate_certs**  boolean | When set to “no”, SSL certificates will not be validated for communication with the AWS APIs.  Choices:   - `false` - `true` ← (default) |
| **virtualization_type**  string | The virtualization type of the image to register.  Default: `"hvm"` |
| **wait**  boolean | Wait for the AMI to be in state ‘available’ before returning.  Choices:   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long before wait gives up, in seconds.  Default: `1200` |

## [Notes](ec2_ami_module.md#id4)

> **Note:**
>
> - If parameters are not set within the module, the following environment variables can be used in decreasing order of precedence `AWS_URL` or `EC2_URL`, `AWS_PROFILE` or `AWS_DEFAULT_PROFILE`, `AWS_ACCESS_KEY_ID` or `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY` or `AWS_SECRET_KEY` or `EC2_SECRET_KEY`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN`, `AWS_REGION` or `EC2_REGION`, `AWS_CA_BUNDLE`
> - When no credentials are explicitly provided the AWS SDK (boto3) that Ansible uses will fall back to its configuration files (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.
> - Modules based on the original AWS SDK (boto) may read their default configuration from different files. See <https://boto.readthedocs.io/en/latest/boto_config_tut.html> for more information.
> - `AWS_REGION` or `EC2_REGION` can be typically be used to specify the AWS region, when required, but this can also be defined in the configuration files.

## [Examples](ec2_ami_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Basic AMI Creation
  amazon.aws.ec2_ami:
    instance_id: i-xxxxxx
    wait: yes
    name: newtest
    tags:
      Name: newtest
      Service: TestService

- name: Basic AMI Creation, without waiting
  amazon.aws.ec2_ami:
    instance_id: i-xxxxxx
    wait: no
    name: newtest

- name: AMI Registration from EBS Snapshot
  amazon.aws.ec2_ami:
    name: newtest
    state: present
    architecture: x86_64
    virtualization_type: hvm
    root_device_name: /dev/xvda
    device_mapping:
      - device_name: /dev/xvda
        volume_size: 8
        snapshot_id: snap-xxxxxxxx
        delete_on_termination: true
        volume_type: gp2

- name: AMI Creation, with a custom root-device size and another EBS attached
  amazon.aws.ec2_ami:
    instance_id: i-xxxxxx
    name: newtest
    device_mapping:
        - device_name: /dev/sda1
          size: XXX
          delete_on_termination: true
          volume_type: gp2
        - device_name: /dev/sdb
          size: YYY
          delete_on_termination: false
          volume_type: gp2

- name: AMI Creation, excluding a volume attached at /dev/sdb
  amazon.aws.ec2_ami:
    instance_id: i-xxxxxx
    name: newtest
    device_mapping:
        - device_name: /dev/sda1
          size: XXX
          delete_on_termination: true
          volume_type: gp2
        - device_name: /dev/sdb
          no_device: yes

- name: Deregister/Delete AMI (keep associated snapshots)
  amazon.aws.ec2_ami:
    image_id: "{{ instance.image_id }}"
    delete_snapshot: False
    state: absent

- name: Deregister AMI (delete associated snapshots too)
  amazon.aws.ec2_ami:
    image_id: "{{ instance.image_id }}"
    delete_snapshot: True
    state: absent

- name: Update AMI Launch Permissions, making it public
  amazon.aws.ec2_ami:
    image_id: "{{ instance.image_id }}"
    state: present
    launch_permissions:
      group_names: ['all']

- name: Allow AMI to be launched by another account
  amazon.aws.ec2_ami:
    image_id: "{{ instance.image_id }}"
    state: present
    launch_permissions:
      user_ids: ['123456789012']
```

## [Return Values](ec2_ami_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **architecture**  string | Architecture of image.  Returned: when AMI is created or already exists  Sample: `"x86_64"` |
| **block_device_mapping**  dictionary | Block device mapping associated with image.  Returned: when AMI is created or already exists  Sample: `{"/dev/sda1": {"delete_on_termination": true, "encrypted": false, "size": 10, "snapshot_id": "snap-1a03b80e7", "volume_type": "standard"}}` |
| **creationDate**  string | Creation date of image.  Returned: when AMI is created or already exists  Sample: `"2015-10-15T22:43:44.000Z"` |
| **description**  string | Description of image.  Returned: when AMI is created or already exists  Sample: `"nat-server"` |
| **hypervisor**  string | Type of hypervisor.  Returned: when AMI is created or already exists  Sample: `"xen"` |
| **image_id**  string | ID of the image.  Returned: when AMI is created or already exists  Sample: `"ami-1234abcd"` |
| **is_public**  boolean | Whether image is public.  Returned: when AMI is created or already exists  Sample: `false` |
| **launch_permission**  list / elements=string | Permissions allowing other accounts to access the AMI.  Returned: when AMI is created or already exists  Sample: `[{"group": "all"}]` |
| **location**  string | Location of image.  Returned: when AMI is created or already exists  Sample: `"315210894379/nat-server"` |
| **name**  string | AMI name of image.  Returned: when AMI is created or already exists  Sample: `"nat-server"` |
| **ownerId**  string | Owner of image.  Returned: when AMI is created or already exists  Sample: `"435210894375"` |
| **platform**  string | Platform of image.  Returned: when AMI is created or already exists |
| **root_device_name**  string | Root device name of image.  Returned: when AMI is created or already exists  Sample: `"/dev/sda1"` |
| **root_device_type**  string | Root device type of image.  Returned: when AMI is created or already exists  Sample: `"ebs"` |
| **snapshots_deleted**  list / elements=string | A list of snapshot ids deleted after deregistering image.  Returned: after AMI is deregistered, if *delete_snapshot=true*  Sample: `["snap-fbcccb8f", "snap-cfe7cdb4"]` |
| **state**  string | State of image.  Returned: when AMI is created or already exists  Sample: `"available"` |
| **tags**  dictionary | A dictionary of tags assigned to image.  Returned: when AMI is created or already exists  Sample: `{"Env": "devel", "Name": "nat-server"}` |
| **virtualization_type**  string | Image virtualization type.  Returned: when AMI is created or already exists  Sample: `"hvm"` |

### Authors

- Evan Duffield (@scicoin-project)
- Constantin Bugneac (@Constantin07)
- Ross Williams (@gunzy83)
- Willem van Ketwich (@wilvk)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
[Communication](index.md#communication-for-amazon-aws)
