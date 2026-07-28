---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_snapshot module – NetApp Element Software Manage Snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_snapshot_module.html
fetched_at: 2026-07-28T00:11:53+00:00
---
# netapp.elementsw.na_elementsw_snapshot module – NetApp Element Software Manage Snapshots

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
> see [Requirements](na_elementsw_snapshot_module.md#ansible-collections-netapp-elementsw-na-elementsw-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_snapshot`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_snapshot_module.md#synopsis)
- [Requirements](na_elementsw_snapshot_module.md#requirements)
- [Parameters](na_elementsw_snapshot_module.md#parameters)
- [Notes](na_elementsw_snapshot_module.md#notes)
- [Examples](na_elementsw_snapshot_module.md#examples)
- [Return Values](na_elementsw_snapshot_module.md#return-values)

## [Synopsis](na_elementsw_snapshot_module.md#id1)

- Create, Modify or Delete Snapshot on Element OS Cluster.

## [Requirements](na_elementsw_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_id**  string / required | Account ID or Name of Parent/Source Volume. |
| **enable_remote_replication**  boolean | Flag, whether to replicate the snapshot created to a remote replication cluster.  To enable specify ‘true’ value.  Choices:   - `false` - `true` |
| **expiration_time**  string | The date and time (format ISO 8601 date string) at which this snapshot will expire. |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **name**  string | Name of new snapshot create.  If unspecified, date and time when the snapshot was taken is used. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **retention**  string | Retention period for the snapshot.  Format is ‘HH:mm:ss’. |
| **snap_mirror_label**  string | Label used by SnapMirror software to specify snapshot retention policy on SnapMirror endpoint. |
| **src_snapshot_id**  string | ID or Name of an existing snapshot.  Required when `state=present`, to modify snapshot properties.  Required when `state=present`, to create snapshot from another snapshot in the volume.  Required when `state=absent`, to delete snapshot. |
| **src_volume_id**  string / required | ID or Name of active volume. |
| **state**  string | Whether the specified snapshot should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_snapshot_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_snapshot_module.md#id5)

```yaml+jinja
- name: Create snapshot
  tags:
  - elementsw_create_snapshot
  na_elementsw_snapshot:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    src_volume_id: 118
    account_id: sagarsh
    name: newsnapshot-1

- name: Modify Snapshot
  tags:
  - elementsw_modify_snapshot
  na_elementsw_snapshot:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    src_volume_id: sagarshansivolume
    src_snapshot_id: test1
    account_id: sagarsh
    expiration_time: '2018-06-16T12:24:56Z'
    enable_remote_replication: false

- name: Delete Snapshot
  tags:
  - elementsw_delete_snapshot
  na_elementsw_snapshot:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    src_snapshot_id: deltest1
    account_id: sagarsh
    src_volume_id: sagarshansivolume
```

## [Return Values](na_elementsw_snapshot_module.md#id6)

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
