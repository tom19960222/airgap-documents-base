---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_account module – NetApp Element Software Manage Accounts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_account_module.html
fetched_at: 2026-07-28T00:11:43+00:00
---
# netapp.elementsw.na_elementsw_account module – NetApp Element Software Manage Accounts

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
> see [Requirements](na_elementsw_account_module.md#ansible-collections-netapp-elementsw-na-elementsw-account-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_account`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_account_module.md#synopsis)
- [Requirements](na_elementsw_account_module.md#requirements)
- [Parameters](na_elementsw_account_module.md#parameters)
- [Notes](na_elementsw_account_module.md#notes)
- [Examples](na_elementsw_account_module.md#examples)

## [Synopsis](na_elementsw_account_module.md#id1)

- Create, destroy, or update accounts on Element SW

## [Requirements](na_elementsw_account_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_account_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | List of Name/Value pairs in JSON object format. |
| **element_username**  aliases: account_id  string / required | Unique username for this account. (May be 1 to 64 characters in length). |
| **from_name**  string  added in netapp.elementsw 2.8.0 | ID or Name of the account to rename.  Required to create an account called ‘element_username’ by renaming ‘from_name’. |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **initiator_secret**  string | CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable.  The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.  If not specified, a random secret is created. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **state**  string | Whether the specified account should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status**  string | Status of the account. |
| **target_secret**  string | CHAP secret to use for the target (mutual CHAP authentication).  Should be 12-16 characters long and impenetrable.  The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.  If not specified, a random secret is created. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_account_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_account_module.md#id5)

```yaml+jinja
- name: Create Account
  na_elementsw_account:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    element_username: TenantA

- name: Modify Account
  na_elementsw_account:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    status: locked
    element_username: TenantA

- name: Rename Account
  na_elementsw_account:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    element_username: TenantA_Renamed
    from_name: TenantA

- name: Rename and modify Account
  na_elementsw_account:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    status: locked
    element_username: TenantA_Renamed
    from_name: TenantA

- name: Delete Account
  na_elementsw_account:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    element_username: TenantA_Renamed
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
