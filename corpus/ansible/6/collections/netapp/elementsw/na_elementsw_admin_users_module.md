---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_admin_users module – NetApp Element Software Manage Admin Users"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_admin_users_module.html
fetched_at: 2026-07-28T00:11:44+00:00
---
# netapp.elementsw.na_elementsw_admin_users module – NetApp Element Software Manage Admin Users

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
> see [Requirements](na_elementsw_admin_users_module.md#ansible-collections-netapp-elementsw-na-elementsw-admin-users-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_admin_users`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_admin_users_module.md#synopsis)
- [Requirements](na_elementsw_admin_users_module.md#requirements)
- [Parameters](na_elementsw_admin_users_module.md#parameters)
- [Notes](na_elementsw_admin_users_module.md#notes)
- [Examples](na_elementsw_admin_users_module.md#examples)

## [Synopsis](na_elementsw_admin_users_module.md#id1)

- Create, destroy, or update admin users on SolidFire

## [Requirements](na_elementsw_admin_users_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_admin_users_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **acceptEula**  boolean | Boolean, true for accepting Eula, False Eula  Choices:   - `false` - `true` |
| **access**  list / elements=string | A list of types the admin has access to |
| **element_password**  string | The password for the new admin account. Setting the password attribute will always reset your password, even if the password is the same |
| **element_username**  string / required | Unique username for this account. (May be 1 to 64 characters in length). |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **state**  string | Whether the specified account should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_admin_users_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_admin_users_module.md#id5)

```yaml+jinja
- name: Add admin user
  na_elementsw_admin_users:
    state: present
    username: "{{ admin_user_name }}"
    password: "{{ admin_password }}"
    hostname: "{{ hostname }}"
    element_username: carchi8py
    element_password: carchi8py
    acceptEula: True
    access: accounts,drives

- name: modify admin user
  na_elementsw_admin_users:
    state: present
    username: "{{ admin_user_name }}"
    password: "{{ admin_password }}"
    hostname: "{{ hostname }}"
    element_username: carchi8py
    element_password: carchi8py12
    acceptEula: True
    access: accounts,drives,nodes

- name: delete admin user
  na_elementsw_admin_users:
    state: absent
    username: "{{ admin_user_name }}"
    password: "{{ admin_password }}"
    hostname: "{{ hostname }}"
    element_username: carchi8py
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
