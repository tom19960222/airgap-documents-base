---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_snapshot_restore module – NetApp Element Software Restore Snapshot"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_snapshot_restore_module.html
fetched_at: 2026-07-28T00:11:54+00:00
---
# netapp.elementsw.na_elementsw_snapshot_restore module – NetApp Element Software Restore Snapshot

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/netapp/elementsw) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_snapshot_restore_module.md#ansible-collections-netapp-elementsw-na-elementsw-snapshot-restore-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_snapshot_restore`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_snapshot_restore_module.md#synopsis)
- [Requirements](na_elementsw_snapshot_restore_module.md#requirements)
- [Parameters](na_elementsw_snapshot_restore_module.md#parameters)
- [Notes](na_elementsw_snapshot_restore_module.md#notes)
- [Examples](na_elementsw_snapshot_restore_module.md#examples)
- [Return Values](na_elementsw_snapshot_restore_module.md#return-values)

## [Synopsis](na_elementsw_snapshot_restore_module.md#id1)

- Element OS Cluster restore snapshot to volume.

## [Requirements](na_elementsw_snapshot_restore_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_snapshot_restore_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_id**  string / required | Account ID or Name of Parent/Source Volume. |
| **dest_volume_name**  string / required | New Name of destination for restoring the snapshot |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **src_snapshot_id**  string / required | ID or Name of an existing snapshot. |
| **src_volume_id**  string / required | ID or Name of source active volume. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_snapshot_restore_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_snapshot_restore_module.md#id5)

```yaml+jinja
- name: Restore snapshot to volume
  tags:
  - elementsw_create_snapshot_restore
  na_elementsw_snapshot_restore:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    account_id: ansible-1
    src_snapshot_id: snapshot_20171021
    src_volume_id: volume-playarea
    dest_volume_name: dest-volume-area
```

## [Return Values](na_elementsw_snapshot_restore_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
