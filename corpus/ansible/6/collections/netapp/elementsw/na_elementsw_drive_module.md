---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_drive module – NetApp Element Software Manage Node Drives"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_drive_module.html
fetched_at: 2026-07-28T00:11:48+00:00
---
# netapp.elementsw.na_elementsw_drive module – NetApp Element Software Manage Node Drives

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
> see [Requirements](na_elementsw_drive_module.md#ansible-collections-netapp-elementsw-na-elementsw-drive-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_drive`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_drive_module.md#synopsis)
- [Requirements](na_elementsw_drive_module.md#requirements)
- [Parameters](na_elementsw_drive_module.md#parameters)
- [Notes](na_elementsw_drive_module.md#notes)
- [Examples](na_elementsw_drive_module.md#examples)
- [Return Values](na_elementsw_drive_module.md#return-values)

## [Synopsis](na_elementsw_drive_module.md#id1)

- Add, Erase or Remove drive for nodes on Element Software Cluster.

## [Requirements](na_elementsw_drive_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_drive_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **drive_ids**  aliases: drive_id  list / elements=string | List of Drive IDs or Serial Names of Node drives.  If not specified, add and remove action will be performed on all drives of node_id |
| **force_during_bin_sync**  boolean | Flag to force during a bin sync operation.  Not supported with latest version of SolidFire SDK (1.7.0.152)  Choices:   - `false` - `true` |
| **force_during_upgrade**  boolean | Flag to force drive operation during upgrade.  Not supported with latest version of SolidFire SDK (1.7.0.152)  Choices:   - `false` - `true` |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **node_ids**  aliases: node_id  list / elements=string | List of IDs or Names of cluster nodes.  If node_ids and drive_ids are not specified, all available drives in the cluster are added if state is present.  If node_ids and drive_ids are not specified, all active drives in the cluster are removed if state is absent. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **state**  string | Element SW Storage Drive operation state.  present - To add drive of node to participate in cluster data storage.  absent - To remove the drive from being part of active cluster.  clean - Clean-up any residual data persistent on a \*removed\* drive in a secured method.  Choices:   - `"present"` ← (default) - `"absent"` - `"clean"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_drive_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_drive_module.md#id5)

```yaml+jinja
- name: Add drive with status available to cluster
  tags:
  - elementsw_add_drive
  na_elementsw_drive:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    drive_ids: scsi-SATA_SAMSUNG_MZ7LM48S2UJNX0J3221807
    force_during_upgrade: false
    force_during_bin_sync: false
    node_ids: sf4805-meg-03

- name: Remove active drive from cluster
  tags:
  - elementsw_remove_drive
  na_elementsw_drive:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    force_during_upgrade: false
    drive_ids: scsi-SATA_SAMSUNG_MZ7LM48S2UJNX0J321208

- name: Secure Erase drive
  tags:
  - elemensw_clean_drive
  na_elementsw_drive:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: clean
    drive_ids: scsi-SATA_SAMSUNG_MZ7LM48S2UJNX0J432109
    node_ids: sf4805-meg-03

- name: Add all the drives of all nodes to cluster
  tags:
  - elementsw_add_node
  na_elementsw_drive:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    force_during_upgrade: false
    force_during_bin_sync: false
```

## [Return Values](na_elementsw_drive_module.md#id6)

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
