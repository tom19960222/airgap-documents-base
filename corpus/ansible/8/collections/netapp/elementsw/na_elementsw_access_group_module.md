---
collection: ansible
version: "8"
title: "netapp.elementsw.na_elementsw_access_group module – NetApp Element Software Manage Access Groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/elementsw/na_elementsw_access_group_module.html
fetched_at: 2026-07-28T02:41:13+00:00
---
# netapp.elementsw.na_elementsw_access_group module – NetApp Element Software Manage Access Groups

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
> see [Requirements](na_elementsw_access_group_module.md#ansible-collections-netapp-elementsw-na-elementsw-access-group-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_access_group`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_access_group_module.md#synopsis)
- [Requirements](na_elementsw_access_group_module.md#requirements)
- [Parameters](na_elementsw_access_group_module.md#parameters)
- [Notes](na_elementsw_access_group_module.md#notes)
- [Examples](na_elementsw_access_group_module.md#examples)
- [Return Values](na_elementsw_access_group_module.md#return-values)

## [Synopsis](na_elementsw_access_group_module.md#id1)

- Create, destroy, or update access groups on Element Software Cluster.

## [Requirements](na_elementsw_access_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_access_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_id**  string  *added in netapp.elementsw 2.8.0* | Account ID for the owner of this volume.  It accepts either account_name or account_id  if account_id is digit, it will consider as account_id  If account_id is string, it will consider as account_name |
| **attributes**  dictionary | List of Name/Value pairs in JSON object format. |
| **from_name**  string  *added in netapp.elementsw 2.8.0* | ID or Name of the access group to rename.  Required to create a new access group called ‘name’ by renaming ‘from_name’. |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **initiators**  list / elements=string | List of initiators to include in the access group. If unspecified, the access group will start out without configured initiators. |
| **name**  aliases: src_access_group_id  string / required | Name for the access group for create, modify and delete operations. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **state**  string | Whether the specified access group should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US>. |
| **virtual_network_id**  integer | The ID of the Element SW Software Cluster Virtual Network to associate the access group with. |
| **virtual_network_tags**  list / elements=string | The tags of VLAN Virtual Network Tag to associate the access group with. |
| **volumes**  list / elements=string | List of volumes to initially include in the volume access group. If unspecified, the access group will start without any volumes.  It accepts either volume_name or volume_id |

## [Notes](na_elementsw_access_group_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_access_group_module.md#id5)

```yaml+jinja
- name: Create Access Group
  na_elementsw_access_group:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    name: AnsibleAccessGroup
    volumes: [7,8]
    account_id: 1

- name: Modify Access Group
  na_elementsw_access_group:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    name: AnsibleAccessGroup-Renamed
    account_id: 1
    attributes: {"volumes": [1,2,3], "virtual_network_id": 12345}

- name: Rename Access Group
  na_elementsw_access_group:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    from_name: AnsibleAccessGroup
    name: AnsibleAccessGroup-Renamed

- name: Delete Access Group
  na_elementsw_access_group:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    name: 1
```

## [Return Values](na_elementsw_access_group_module.md#id6)

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
