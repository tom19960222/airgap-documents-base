---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_access_group_volumes module – NetApp Element Software Add/Remove Volumes to/from Access Group"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_access_group_volumes_module.html
fetched_at: 2026-07-28T00:11:42+00:00
---
# netapp.elementsw.na_elementsw_access_group_volumes module – NetApp Element Software Add/Remove Volumes to/from Access Group

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
> see [Requirements](na_elementsw_access_group_volumes_module.md#ansible-collections-netapp-elementsw-na-elementsw-access-group-volumes-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_access_group_volumes`.

New in netapp.elementsw 20.1.0

- [Synopsis](na_elementsw_access_group_volumes_module.md#synopsis)
- [Requirements](na_elementsw_access_group_volumes_module.md#requirements)
- [Parameters](na_elementsw_access_group_volumes_module.md#parameters)
- [Notes](na_elementsw_access_group_volumes_module.md#notes)
- [Examples](na_elementsw_access_group_volumes_module.md#examples)
- [Return Values](na_elementsw_access_group_volumes_module.md#return-values)

## [Synopsis](na_elementsw_access_group_volumes_module.md#id1)

- Add or remove volumes to/from access group on Element Software Cluster.

## [Requirements](na_elementsw_access_group_volumes_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_access_group_volumes_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_group**  string / required | Name or id for the access group to add volumes to, or remove volumes from |
| **account_id**  string / required | Account ID for the owner of this volume.  It accepts either account_name or account_id  if account_id is numeric, look up for account_id first, then look up for account_name  If account_id is not numeric, look up for account_name |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **state**  string | Whether the specified volumes should exist or not for this access group.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |
| **volumes**  list / elements=string / required | List of volumes to add/remove from/to the access group.  It accepts either volume_name or volume_id |

## [Notes](na_elementsw_access_group_volumes_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_access_group_volumes_module.md#id5)

```yaml+jinja
- name:  Add Volumes to Access Group
  na_elementsw_access_group:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    access_group: AnsibleAccessGroup
    volumes: ['vol7','vol8','vol9']
    account_id: '1'

- name:  Remove Volumes from Access Group
  na_elementsw_access_group:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    access_group: AnsibleAccessGroup
    volumes: ['vol7','vol9']
    account_id: '1'
```

## [Return Values](na_elementsw_access_group_volumes_module.md#id6)

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
