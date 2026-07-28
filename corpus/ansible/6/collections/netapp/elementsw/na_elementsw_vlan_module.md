---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_vlan module – NetApp Element Software Manage VLAN"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_vlan_module.html
fetched_at: 2026-07-28T00:11:55+00:00
---
# netapp.elementsw.na_elementsw_vlan module – NetApp Element Software Manage VLAN

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
> see [Requirements](na_elementsw_vlan_module.md#ansible-collections-netapp-elementsw-na-elementsw-vlan-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_vlan`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_vlan_module.md#synopsis)
- [Requirements](na_elementsw_vlan_module.md#requirements)
- [Parameters](na_elementsw_vlan_module.md#parameters)
- [Notes](na_elementsw_vlan_module.md#notes)
- [Examples](na_elementsw_vlan_module.md#examples)

## [Synopsis](na_elementsw_vlan_module.md#id1)

- Create, delete, modify VLAN

## [Requirements](na_elementsw_vlan_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address_blocks**  list / elements=dictionary | List of address blocks for the VLAN  Each address block contains the starting IP address and size for the block  Required for create |
| **attributes**  dictionary | Dictionary of attributes with name and value for each attribute |
| **gateway**  string | Gateway for the VLAN |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **name**  string | User defined name for the new VLAN  Name of the vlan is unique  Required for create |
| **namespace**  boolean | Enable or disable namespaces  Choices:   - `false` - `true` |
| **netmask**  string | Netmask for the VLAN  Required for create |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **state**  string | Whether the specified vlan should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **svip**  string | Storage virtual IP which is unique  Required for create |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |
| **vlan_tag**  string / required | Virtual Network Tag |

## [Notes](na_elementsw_vlan_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_vlan_module.md#id5)

```yaml+jinja
- name: Create vlan
  na_elementsw_vlan:
    state: present
    name: test
    vlan_tag: 1
    svip: "{{ ip address }}"
    netmask: "{{ netmask }}"
    address_blocks:
      - start: "{{ starting ip_address }}"
        size: 5
      - start: "{{ starting ip_address }}"
        size: 5
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete Lun
  na_elementsw_vlan:
    state: absent
    vlan_tag: 1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
