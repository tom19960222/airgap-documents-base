---
collection: ansible
version: "8"
title: "amazon.aws.ec2_ami module – Create or destroy an image (AMI) in EC2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/amazon/aws/ec2_ami_module.html
fetched_at: 2026-07-28T01:06:21+00:00
---
# amazon.aws.ec2_ami module – Create or destroy an image (AMI) in EC2

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

- Registers or deregisters EC2 images.

## [Requirements](ec2_ami_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- boto3 >= 1.22.0
- botocore >= 1.25.0

## [Parameters](ec2_ami_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  aliases: aws_access_key_id, aws_access_key, ec2_access_key  string | AWS access key ID.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_ACCESS_KEY_ID`, `AWS_ACCESS_KEY` or `EC2_ACCESS_KEY` environment variables may also be used in decreasing order of preference.  The *aws_access_key* and *profile* options are mutually exclusive.  The *aws_access_key_id* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_access_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_ACCESS_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **architecture**  string | The target architecture of the image to register.  **Default:** `"x86_64"` |
| **aws_ca_bundle**  path | The location of a CA Bundle to use when validating SSL certificates.  The `AWS_CA_BUNDLE` environment variable may also be used. |
| **aws_config**  dictionary | A dictionary to modify the botocore configuration.  Parameters can be found in the AWS documentation <https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html#botocore.config.Config>. |
| **billing_products**  list / elements=string | A list of valid billing codes. To be used with valid accounts by AWS Marketplace vendors. |
| **boot_mode**  string  *added in amazon.aws 5.5.0* | The boot mode of the AMI.  See the AWS documentation for more detail <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html>.  **Choices:**   - `"legacy-bios"` - `"uefi"` |
| **debug_botocore_endpoint_logs**  boolean | Use a `botocore.endpoint` logger to parse the unique (rather than total) `"resource:action"` API calls made during a task, outputing the set to the resource_actions key in the task results. Use the `aws_resource_action` callback to output to total list made during a playbook.  The `ANSIBLE_DEBUG_BOTOCORE_LOGS` environment variable may also be used.  **Choices:**   - `false` ← (default) - `true` |
| **delete_snapshot**  boolean | Delete snapshots when deregistering the AMI.  **Choices:**   - `false` ← (default) - `true` |
| **description**  string | Human-readable string describing the contents and purpose of the AMI.  **Default:** `""` |
| **device_mapping**  list / elements=dictionary | List of device hashes/dictionaries with custom configurations (same block-device-mapping parameters). |
| **delete_on_termination**  boolean | Whether the device should be automatically deleted when the Instance is terminated.  **Choices:**   - `false` - `true` |
| **device_name**  string / required | The device name. For example `/dev/sda`. |
| **encrypted**  boolean | Whether the volume should be encrypted.  **Choices:**   - `false` - `true` |
| **iops**  integer | When using an `io1` *volume_type* this sets the number of IOPS provisioned for the volume. |
| **no_device**  boolean | Suppresses the specified device included in the block device mapping of the AMI.  **Choices:**   - `false` - `true` |
| **snapshot_id**  string | The ID of the Snapshot. |
| **virtual_name**  string | The virtual name for the device.  See the AWS documentation for more detail <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_BlockDeviceMapping.html>. |
| **volume_size**  aliases: size  integer | The size of the volume (in GiB). |
| **volume_type**  string | The volume type. Defaults to `gp2` when not set. |
| **endpoint_url**  aliases: ec2_url, aws_endpoint_url, s3_url  string | URL to connect to instead of the default AWS endpoints. While this can be used to connection to other AWS-compatible services the amazon.aws and community.aws collections are only tested against AWS.  The `AWS_URL` or `EC2_URL` environment variables may also be used, in decreasing order of preference.  The *ec2_url* and *s3_url* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_URL` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **enhanced_networking**  boolean | A boolean representing whether enhanced networking with ENA is enabled or not.  **Choices:**   - `false` - `true` |
| **image_id**  string | Image ID to be deregistered. |
| **image_location**  string | The S3 location of an image to use for the AMI. |
| **instance_id**  string | Instance ID to create the AMI from. |
| **kernel_id**  string | The target kernel id of the image to register. |
| **launch_permissions**  dictionary | Launch permissions for the AMI.  You must pass all desired launch permissions if you wish to modify existing launch permissions (passing just groups will remove all users). |
| **group_names**  list / elements=string | List of group names. |
| **org_arns**  list / elements=string  *added in amazon.aws 6.5.0* | List of The Amazon Resource Name(s) (ARN) of organization(s). |
| **org_unit_arns**  list / elements=string  *added in amazon.aws 6.5.0* | List of The Amazon Resource Name(s) (ARN) of an organizational unit(s) (OU). |
| **user_ids**  list / elements=string | List of account IDs. |
| **name**  string | The name of the new AMI. |
| **no_reboot**  boolean | Flag indicating that the bundling process should not attempt to shutdown the instance before bundling. If this flag is True, the responsibility of maintaining file system integrity is left to the owner of the instance.  **Choices:**   - `false` ← (default) - `true` |
| **profile**  aliases: aws_profile  string | A named AWS profile to use for authentication.  See the AWS documentation for more information about named profiles <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html>.  The `AWS_PROFILE` environment variable may also be used.  The *profile* option is mutually exclusive with the *aws_access_key*, *aws_secret_key* and *security_token* options. |
| **purge_tags**  boolean | If *purge_tags=true* and *tags* is set, existing tags will be purged from the resource to match exactly what is defined by *tags* parameter.  If the *tags* parameter is not set then tags will not be modified, even if *purge_tags=True*.  Tag keys beginning with `aws:` are reserved by Amazon and can not be modified. As such they will be ignored for the purposes of the *purge_tags* parameter. See the Amazon documentation for more information <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions>.  **Choices:**   - `false` - `true` ← (default) |
| **ramdisk_id**  string | The ID of the RAM disk. |
| **region**  aliases: aws_region, ec2_region  string | The AWS region to use.  For global services such as IAM, Route53 and CloudFront, *region* is ignored.  The `AWS_REGION` or `EC2_REGION` environment variables may also be used.  See the Amazon AWS documentation for more information <http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region>.  The `ec2_region` alias has been deprecated and will be removed in a release after 2024-12-01  Support for the `EC2_REGION` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **root_device_name**  string | The root device name of the image to register. |
| **secret_key**  aliases: aws_secret_access_key, aws_secret_key, ec2_secret_key  string | AWS secret access key.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, or `EC2_SECRET_KEY` environment variables may also be used in decreasing order of preference.  The *secret_key* and *profile* options are mutually exclusive.  The *aws_secret_access_key* alias was added in release 5.1.0 for consistency with the AWS botocore SDK.  The *ec2_secret_key* alias has been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` environment variable has been deprecated and will be removed in a release after 2024-12-01. |
| **session_token**  aliases: aws_session_token, security_token, aws_security_token, access_token  string | AWS STS session token for use with temporary credentials.  See the AWS documentation for more information about access tokens <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>.  The `AWS_SESSION_TOKEN`, `AWS_SECURITY_TOKEN` or `EC2_SECURITY_TOKEN` environment variables may also be used in decreasing order of preference.  The *security_token* and *profile* options are mutually exclusive.  Aliases *aws_session_token* and *session_token* were added in release 3.2.0, with the parameter being renamed from *security_token* to *session_token* in release 6.0.0.  The *security_token*, *aws_security_token*, and *access_token* aliases have been deprecated and will be removed in a release after 2024-12-01.  Support for the `EC2_SECRET_KEY` and `AWS_SECURITY_TOKEN` environment variables has been deprecated and will be removed in a release after 2024-12-01. |
| **sriov_net_support**  string | Set to simple to enable enhanced networking with the Intel 82599 Virtual Function interface for the AMI and any instances that you launch from the AMI. |
| **state**  string | Register or deregister an AMI.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **tags**  aliases: resource_tags  dictionary | A dictionary representing the tags to be applied to the resource.  If the *tags* parameter is not set then tags will not be modified. |
| **tpm_support**  string  *added in amazon.aws 5.5.0* | Set to v2.0 to enable Trusted Platform Module (TPM) support.  If the image is configured for NitroTPM support, the value is v2.0 .  Requires *boot_mode* to be set to ‘uefi’.  Requires an instance type that is compatible with Nitro.  Requires minimum botocore version 1.26.0.  See the AWS documentation for more detail <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html>. |
| **uefi_data**  string  *added in amazon.aws 5.5.0* | Base64 representation of the non-volatile UEFI variable store.  Requires minimum botocore version 1.26.0.  See the AWS documentation for more detail <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html>. |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated for communication with the AWS APIs.  Setting *validate_certs=false* is strongly discouraged, as an alternative, consider setting *aws_ca_bundle* instead.  **Choices:**   - `false` - `true` ← (default) |
| **virtualization_type**  string | The virtualization type of the image to register.  **Default:** `"hvm"` |
| **wait**  boolean | Wait for the AMI to be in state ‘available’ before returning.  **Choices:**   - `false` ← (default) - `true` |
| **wait_timeout**  integer | How long before wait gives up, in seconds.  **Default:** `1200` |

## [Notes](ec2_ami_module.md#id4)

> **Note:**
>
> - **Caution:** For modules, environment variables and configuration files are read from the Ansible ‘host’ context and not the ‘controller’ context. As such, files may need to be explicitly copied to the ‘host’. For lookup and connection plugins, environment variables and configuration files are read from the Ansible ‘controller’ context and not the ‘host’ context.
> - The AWS SDK (boto3) that Ansible uses may also read defaults for credentials and other settings, such as the region, from its configuration files in the Ansible ‘host’ context (typically `~/.aws/credentials`). See <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html> for more information.

## [Examples](ec2_ami_module.md#id5)

```yaml+jinja
# Note: These examples do not set authentication details, see the AWS Guide for details.

- name: Basic AMI Creation
  amazon.aws.ec2_ami:
    instance_id: i-xxxxxx
    wait: true
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
          no_device: true

- name: AMI Creation with boot_mode and tpm_support
  amazon.aws.ec2_ami:
    name: newtest
    state: present
    architecture: x86_64
    virtualization_type: hvm
    root_device_name: /dev/sda1
    device_mapping:
        - device_name: /dev/sda1
          snapshot_id: "{{ snapshot_id }}"
    wait: yes
    region: us-east-1
    boot_mode: uefi
    uefi_data: data_file.bin
    tpm_support: v2.0

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

- name: Update AMI Launch Permissions, share AMI across an Organization and Organizational Units
  amazon.aws.ec2_ami:
    image_id: "{{ instance.image_id }}"
    state: present
    launch_permissions:
      org_arns: ['arn:aws:organizations::123456789012:organization/o-123ab4cdef']
      org_unit_arns: ['arn:aws:organizations::123456789012:ou/o-123example/ou-1234-5example']
```

## [Return Values](ec2_ami_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **architecture**  string | Architecture of image.  **Returned:** when AMI is created or already exists  **Sample:** `"x86_64"` |
| **block_device_mapping**  dictionary | Block device mapping associated with image.  **Returned:** when AMI is created or already exists  **Sample:** `{"/dev/sda1": {"delete_on_termination": true, "encrypted": false, "size": 10, "snapshot_id": "snap-1a03b80e7", "volume_type": "standard"}}` |
| **creationDate**  string | Creation date of image.  **Returned:** when AMI is created or already exists  **Sample:** `"2015-10-15T22:43:44.000Z"` |
| **description**  string | Description of image.  **Returned:** when AMI is created or already exists  **Sample:** `"nat-server"` |
| **hypervisor**  string | Type of hypervisor.  **Returned:** when AMI is created or already exists  **Sample:** `"xen"` |
| **image_id**  string | ID of the image.  **Returned:** when AMI is created or already exists  **Sample:** `"ami-1234abcd"` |
| **is_public**  boolean | Whether image is public.  **Returned:** when AMI is created or already exists  **Sample:** `false` |
| **launch_permission**  list / elements=string | Permissions allowing other accounts to access the AMI.  **Returned:** when AMI is created or already exists  **Sample:** `[{"group": "all"}]` |
| **location**  string | Location of image.  **Returned:** when AMI is created or already exists  **Sample:** `"123456789012/nat-server"` |
| **name**  string | AMI name of image.  **Returned:** when AMI is created or already exists  **Sample:** `"nat-server"` |
| **ownerId**  string | Owner of image.  **Returned:** when AMI is created or already exists  **Sample:** `"123456789012"` |
| **platform**  string | Platform of image.  **Returned:** when AMI is created or already exists |
| **root_device_name**  string | Root device name of image.  **Returned:** when AMI is created or already exists  **Sample:** `"/dev/sda1"` |
| **root_device_type**  string | Root device type of image.  **Returned:** when AMI is created or already exists  **Sample:** `"ebs"` |
| **snapshots_deleted**  list / elements=string | A list of snapshot ids deleted after deregistering image.  **Returned:** after AMI is deregistered, if *delete_snapshot=true*  **Sample:** `["snap-fbcccb8f", "snap-cfe7cdb4"]` |
| **state**  string | State of image.  **Returned:** when AMI is created or already exists  **Sample:** `"available"` |
| **tags**  dictionary | A dictionary of tags assigned to image.  **Returned:** when AMI is created or already exists  **Sample:** `{"Env": "devel", "Name": "nat-server"}` |
| **virtualization_type**  string | Image virtualization type.  **Returned:** when AMI is created or already exists  **Sample:** `"hvm"` |

### Authors

- Evan Duffield (@scicoin-project)
- Constantin Bugneac (@Constantin07)
- Ross Williams (@gunzy83)
- Willem van Ketwich (@wilvk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/amazon.aws/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/amazon.aws)
- [Communication](index.md#communication-for-amazon-aws)
