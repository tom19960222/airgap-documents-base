---
collection: ansible
version: "6"
title: "community.general.hwc_evs_disk module – Creates a resource of Evs/Disk in Huawei Cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/hwc_evs_disk_module.html
fetched_at: 2026-07-27T17:09:25+00:00
---
# community.general.hwc_evs_disk module – Creates a resource of Evs/Disk in Huawei Cloud

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](hwc_evs_disk_module.md#ansible-collections-community-general-hwc-evs-disk-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hwc_evs_disk`.

New in community.general 0.2.0

- [Synopsis](hwc_evs_disk_module.md#synopsis)
- [Requirements](hwc_evs_disk_module.md#requirements)
- [Parameters](hwc_evs_disk_module.md#parameters)
- [Notes](hwc_evs_disk_module.md#notes)
- [Examples](hwc_evs_disk_module.md#examples)
- [Return Values](hwc_evs_disk_module.md#return-values)

## [Synopsis](hwc_evs_disk_module.md#id1)

- block storage management.

## [Requirements](hwc_evs_disk_module.md#id2)

The below requirements are needed on the host that executes this module.

- keystoneauth1 >= 3.6.0

## [Parameters](hwc_evs_disk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **availability_zone**  string / required | Specifies the AZ where you want to create the disk. |
| **backup_id**  string | Specifies the ID of the backup that can be used to create a disk. This parameter is mandatory when you use a backup to create the disk. |
| **description**  string | Specifies the disk description. The value can contain a maximum of 255 bytes. |
| **domain**  string / required | The name of the Domain to scope to (Identity v3). (currently only domain names are supported, and not domain IDs). |
| **enable_full_clone**  boolean | If the disk is created from a snapshot and linked cloning needs to be used, set this parameter to True.  Choices:   - `false` - `true` |
| **enable_scsi**  boolean | If this parameter is set to True, the disk device type will be SCSI, which allows ECS OSs to directly access underlying storage media. SCSI reservation command is supported. If this parameter is set to False, the disk device type will be VBD, which supports only simple SCSI read/write commands.  If parameter enable_share is set to True and this parameter is not specified, shared SCSI disks are created. SCSI EVS disks cannot be created from backups, which means that this parameter cannot be True if backup_id has been specified.  Choices:   - `false` - `true` |
| **enable_share**  boolean | Specifies whether the disk is shareable. The default value is False.  Choices:   - `false` - `true` |
| **encryption_id**  string | Specifies the encryption ID. The length of it fixes at 36 bytes. |
| **enterprise_project_id**  string | Specifies the enterprise project ID. This ID is associated with the disk during the disk creation. If it is not specified, the disk is bound to the default enterprise project. |
| **id**  string | The id of resource to be managed. |
| **identity_endpoint**  string / required | The Identity authentication URL. |
| **image_id**  string | Specifies the image ID. If this parameter is specified, the disk is created from an image. BMS system disks cannot be created from BMS images. |
| **name**  string / required | Specifies the disk name. The value can contain a maximum of 255 bytes. |
| **password**  string / required | The password to login with. |
| **project**  string / required | The name of the Tenant (Identity v2) or Project (Identity v3). (currently only project names are supported, and not project IDs). |
| **region**  string | The region to which the project belongs. |
| **size**  integer | Specifies the disk size, in GB. Its values are as follows, System disk 1 GB to 1024 GB, Data disk 10 GB to 32768 GB. This parameter is mandatory when you create an empty disk or use an image or a snapshot to create a disk. If you use an image or a snapshot to create a disk, the disk size must be greater than or equal to the image or snapshot size. This parameter is optional when you use a backup to create a disk. If this parameter is not specified, the disk size is equal to the backup size. |
| **snapshot_id**  string | Specifies the snapshot ID. If this parameter is specified, the disk is created from a snapshot. |
| **state**  string | Whether the given object should exist in Huaweicloud Cloud.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeouts**  dictionary | The timeouts for each operations.  Default: `{}` |
| **create**  string | The timeouts for create operation.  Default: `"30m"` |
| **delete**  string | The timeouts for delete operation.  Default: `"30m"` |
| **update**  string | The timeouts for update operation.  Default: `"30m"` |
| **user**  string / required | The user name to login with (currently only user names are supported, and not user IDs). |
| **volume_type**  string / required | Specifies the disk type. Currently, the value can be SSD, SAS, or SATA.  SSD specifies the ultra-high I/O disk type.  SAS specifies the high I/O disk type.  SATA specifies the common I/O disk type.  If the specified disk type is not available in the AZ, the disk will fail to create. If the EVS disk is created from a snapshot, the volume_type field must be the same as that of the snapshot’s source disk. |

## [Notes](hwc_evs_disk_module.md#id4)

> **Note:**
>
> - For authentication, you can set identity_endpoint using the `ANSIBLE_HWC_IDENTITY_ENDPOINT` env variable.
> - For authentication, you can set user using the `ANSIBLE_HWC_USER` env variable.
> - For authentication, you can set password using the `ANSIBLE_HWC_PASSWORD` env variable.
> - For authentication, you can set domain using the `ANSIBLE_HWC_DOMAIN` env variable.
> - For authentication, you can set project using the `ANSIBLE_HWC_PROJECT` env variable.
> - For authentication, you can set region using the `ANSIBLE_HWC_REGION` env variable.
> - Environment variables values will only be used if the playbook values are not set.

## [Examples](hwc_evs_disk_module.md#id5)

```yaml+jinja
# test create disk
- name: Create a disk
  community.general.hwc_evs_disk:
    availability_zone: "cn-north-1a"
    name: "ansible_evs_disk_test"
    volume_type: "SATA"
    size: 10
```

## [Return Values](hwc_evs_disk_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **attachments**  complex | Specifies the disk attachment information.  Returned: success |
| **attached_at**  string | Specifies the time when the disk was attached. Time format is ‘UTC YYYY-MM-DDTHH:MM:SS’.  Returned: success |
| **attachment_id**  string | Specifies the ID of the attachment information.  Returned: success |
| **device**  string | Specifies the device name.  Returned: success |
| **server_id**  string | Specifies the ID of the server to which the disk is attached.  Returned: success |
| **availability_zone**  string | Specifies the AZ where you want to create the disk.  Returned: success |
| **backup_id**  string | Specifies the ID of the backup that can be used to create a disk. This parameter is mandatory when you use a backup to create the disk.  Returned: success |
| **backup_policy_id**  string | Specifies the backup policy ID.  Returned: success |
| **created_at**  string | Specifies the time when the disk was created. Time format is ‘UTC YYYY-MM-DDTHH:MM:SS’.  Returned: success |
| **description**  string | Specifies the disk description. The value can contain a maximum of 255 bytes.  Returned: success |
| **enable_full_clone**  boolean | If the disk is created from a snapshot and linked cloning needs to be used, set this parameter to True.  Returned: success |
| **enable_scsi**  boolean | If this parameter is set to True, the disk device type will be SCSI, which allows ECS OSs to directly access underlying storage media. SCSI reservation command is supported. If this parameter is set to False, the disk device type will be VBD, which supports only simple SCSI read/write commands.  If parameter enable_share is set to True and this parameter is not specified, shared SCSI disks are created. SCSI EVS disks cannot be created from backups, which means that this parameter cannot be True if backup_id has been specified.  Returned: success |
| **enable_share**  boolean | Specifies whether the disk is shareable. The default value is False.  Returned: success |
| **encryption_id**  string | Specifies the encryption ID. The length of it fixes at 36 bytes.  Returned: success |
| **enterprise_project_id**  string | Specifies the enterprise project ID. This ID is associated with the disk during the disk creation. If it is not specified, the disk is bound to the default enterprise project.  Returned: success |
| **image_id**  string | Specifies the image ID. If this parameter is specified, the disk is created from an image. BMS system disks cannot be created from BMS images.  Returned: success |
| **is_bootable**  boolean | Specifies whether the disk is bootable.  Returned: success |
| **is_readonly**  boolean | Specifies whether the disk is read-only or read/write. True indicates that the disk is read-only. False indicates that the disk is read/write.  Returned: success |
| **name**  string | Specifies the disk name. The value can contain a maximum of 255 bytes.  Returned: success |
| **size**  integer | Specifies the disk size, in GB. Its values are as follows, System disk 1 GB to 1024 GB, Data disk 10 GB to 32768 GB. This parameter is mandatory when you create an empty disk or use an image or a snapshot to create a disk. If you use an image or a snapshot to create a disk, the disk size must be greater than or equal to the image or snapshot size. This parameter is optional when you use a backup to create a disk. If this parameter is not specified, the disk size is equal to the backup size.  Returned: success |
| **snapshot_id**  string | Specifies the snapshot ID. If this parameter is specified, the disk is created from a snapshot.  Returned: success |
| **source_volume_id**  string | Specifies the source disk ID. This parameter has a value if the disk is created from a source disk.  Returned: success |
| **status**  string | Specifies the disk status.  Returned: success |
| **tags**  dictionary | Specifies the disk tags.  Returned: success |
| **volume_type**  string | Specifies the disk type. Currently, the value can be SSD, SAS, or SATA.  SSD specifies the ultra-high I/O disk type.  SAS specifies the high I/O disk type.  SATA specifies the common I/O disk type.  If the specified disk type is not available in the AZ, the disk will fail to create. If the EVS disk is created from a snapshot, the volume_type field must be the same as that of the snapshot’s source disk.  Returned: success |

### Authors

- Huawei Inc. (@huaweicloud)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
