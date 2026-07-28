---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_volume_clone module – NetApp Element Software Create Volume Clone"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_volume_clone_module.html
fetched_at: 2026-07-28T02:41:32+00:00
---
# netapp.elementsw.na_elementsw_volume_clone module – NetApp Element Software Create Volume Clone

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/ui/repo/published/netapp/elementsw/) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_volume_clone_module.md#ansible-collections-netapp-elementsw-na-elementsw-volume-clone-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_volume_clone`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_volume_clone_module.md#synopsis)
- [Requirements](na_elementsw_volume_clone_module.md#requirements)
- [Parameters](na_elementsw_volume_clone_module.md#parameters)
- [Notes](na_elementsw_volume_clone_module.md#notes)
- [Examples](na_elementsw_volume_clone_module.md#examples)
- [Return Values](na_elementsw_volume_clone_module.md#return-values)

## [Synopsis](na_elementsw_volume_clone_module.md#id1)

- Create volume clones on Element OS

## [Requirements](na_elementsw_volume_clone_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_volume_clone_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access**  string | Access allowed for the volume.  If unspecified, the access settings of the clone will be the same as the source.  readOnly - Only read operations are allowed.  readWrite - Reads and writes are allowed.  locked - No reads or writes are allowed.  replicationTarget - Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  **Choices:**   - `"readOnly"` - `"readWrite"` - `"locked"` - `"replicationTarget"` |
| **account_id**  string / required | Account ID for the owner of this cloned volume. id may be a numeric identifier or an account name. |
| **attributes**  dictionary | A YAML dictionary of attributes that you would like to apply on this cloned volume. |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **name**  string / required | The name of the clone. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **size**  integer | The size of the cloned volume in (size_unit). |
| **size_unit**  string | The unit used to interpret the size parameter.  **Choices:**   - `"bytes"` - `"b"` - `"kb"` - `"mb"` - `"gb"` ← (default) - `"tb"` - `"pb"` - `"eb"` - `"zb"` - `"yb"` |
| **src_snapshot_id**  string | The id of the snapshot to clone. id may be a numeric identifier or a snapshot name. |
| **src_volume_id**  string / required | The id of the src volume to clone. id may be a numeric identifier or a volume name. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |

## [Notes](na_elementsw_volume_clone_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_volume_clone_module.md#id5)

```yaml+jinja
- name: Clone Volume
  na_elementsw_volume_clone:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    name: CloneAnsibleVol
    src_volume_id: 123
    src_snapshot_id: 41
    account_id: 3
    size: 1
    size_unit: gb
    access: readWrite
    attributes: {"virtual_network_id": 12345}
```

## [Return Values](na_elementsw_volume_clone_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  **Returned:** success |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
