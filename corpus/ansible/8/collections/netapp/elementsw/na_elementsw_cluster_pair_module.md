---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_cluster_pair module – NetApp Element Software Manage Cluster Pair"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_cluster_pair_module.html
fetched_at: 2026-07-28T02:41:21+00:00
---
# netapp.elementsw.na_elementsw_cluster_pair module – NetApp Element Software Manage Cluster Pair

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
> see [Requirements](na_elementsw_cluster_pair_module.md#ansible-collections-netapp-elementsw-na-elementsw-cluster-pair-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_cluster_pair`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_cluster_pair_module.md#synopsis)
- [Requirements](na_elementsw_cluster_pair_module.md#requirements)
- [Parameters](na_elementsw_cluster_pair_module.md#parameters)
- [Notes](na_elementsw_cluster_pair_module.md#notes)
- [Examples](na_elementsw_cluster_pair_module.md#examples)

## [Synopsis](na_elementsw_cluster_pair_module.md#id1)

- Create, delete cluster pair

## [Requirements](na_elementsw_cluster_pair_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_cluster_pair_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dest_mvip**  string / required | Destination IP address of the cluster to be paired. |
| **dest_password**  string | Destination password for the cluster to be paired.  Optional if this is same as source cluster password. |
| **dest_username**  string | Destination username for the cluster to be paired.  Optional if this is same as source cluster username. |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **state**  string | Whether the specified cluster pair should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |

## [Notes](na_elementsw_cluster_pair_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_cluster_pair_module.md#id5)

```yaml+jinja
- name: Create cluster pair
  na_elementsw_cluster_pair:
    hostname: "{{ src_hostname }}"
    username: "{{ src_username }}"
    password: "{{ src_password }}"
    state: present
    dest_mvip: "{{ dest_hostname }}"

- name: Delete cluster pair
  na_elementsw_cluster_pair:
    hostname: "{{ src_hostname }}"
    username: "{{ src_username }}"
    password: "{{ src_password }}"
    state: absent
    dest_mvip: "{{ dest_hostname }}"
    dest_username: "{{ dest_username }}"
    dest_password: "{{ dest_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
