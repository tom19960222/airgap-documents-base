---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_volume_pair module – NetApp Element Software Volume Pair"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_volume_pair_module.html
fetched_at: 2026-07-28T02:41:33+00:00
---
# netapp.elementsw.na_elementsw_volume_pair module – NetApp Element Software Volume Pair

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
> see [Requirements](na_elementsw_volume_pair_module.md#ansible-collections-netapp-elementsw-na-elementsw-volume-pair-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_volume_pair`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_volume_pair_module.md#synopsis)
- [Requirements](na_elementsw_volume_pair_module.md#requirements)
- [Parameters](na_elementsw_volume_pair_module.md#parameters)
- [Notes](na_elementsw_volume_pair_module.md#notes)
- [Examples](na_elementsw_volume_pair_module.md#examples)

## [Synopsis](na_elementsw_volume_pair_module.md#id1)

- Create, delete volume pair

## [Requirements](na_elementsw_volume_pair_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_volume_pair_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dest_account**  string / required | Destination account name or ID |
| **dest_mvip**  string / required | Destination IP address of the paired cluster. |
| **dest_password**  string | Destination password for the paired cluster  Optional if this is same as source cluster password. |
| **dest_username**  string | Destination username for the paired cluster  Optional if this is same as source cluster username. |
| **dest_volume**  string / required | Destination volume name or volume ID |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **mode**  string | Mode to start the volume pairing  **Choices:**   - `"async"` ← (default) - `"sync"` - `"snapshotsonly"` |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **src_account**  string / required | Source account name or ID |
| **src_volume**  string / required | Source volume name or volume ID |
| **state**  string | Whether the specified volume pair should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |

## [Notes](na_elementsw_volume_pair_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_volume_pair_module.md#id5)

```yaml+jinja
- name: Create volume pair
  na_elementsw_volume_pair:
    hostname: "{{ src_cluster_hostname }}"
    username: "{{ src_cluster_username }}"
    password: "{{ src_cluster_password }}"
    state: present
    src_volume: test1
    src_account: test2
    dest_volume: test3
    dest_account: test4
    mode: sync
    dest_mvip: "{{ dest_cluster_hostname }}"

- name: Delete volume pair
  na_elementsw_volume_pair:
    hostname: "{{ src_cluster_hostname }}"
    username: "{{ src_cluster_username }}"
    password: "{{ src_cluster_password }}"
    state: absent
    src_volume: 3
    src_account: 1
    dest_volume: 2
    dest_account: 1
    dest_mvip: "{{ dest_cluster_hostname }}"
    dest_username: "{{ dest_cluster_username }}"
    dest_password: "{{ dest_cluster_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
