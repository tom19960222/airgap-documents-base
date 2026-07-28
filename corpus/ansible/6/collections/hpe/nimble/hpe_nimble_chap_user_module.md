---
collection: ansible
version: "6"
title: "hpe.nimble.hpe_nimble_chap_user module – Manage the HPE Nimble Storage CHAP user"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hpe/nimble/hpe_nimble_chap_user_module.html
fetched_at: 2026-07-27T17:49:58+00:00
---
# hpe.nimble.hpe_nimble_chap_user module – Manage the HPE Nimble Storage CHAP user

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/hpe/nimble) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_chap_user_module.md#ansible-collections-hpe-nimble-hpe-nimble-chap-user-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_chap_user`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_chap_user_module.md#synopsis)
- [Requirements](hpe_nimble_chap_user_module.md#requirements)
- [Parameters](hpe_nimble_chap_user_module.md#parameters)
- [Notes](hpe_nimble_chap_user_module.md#notes)
- [Examples](hpe_nimble_chap_user_module.md#examples)

## [Synopsis](hpe_nimble_chap_user_module.md#id1)

- Manage the CHAP user on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_chap_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_chap_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **change_name**  string | Change the name of the existing CHAP user. |
| **description**  string | Text description of CHAP user. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **initiator_iqns**  list / elements=dictionary | List of iSCSI initiators. To be configured with this CHAP user for iSCSI Group Target CHAP authentication. This attribute cannot be modified at the same time with other attributes. If any specified initiator is already associated with another CHAP user, it will be replaced by this CHAP user for future CHAP authentication. |
| **name**  string / required | The CHAP user name. |
| **password**  string / required | HPE Nimble Storage password. |
| **state**  string / required | The CHAP user operation.  Choices:   - `"create"` - `"present"` - `"absent"` |
| **user_password**  string | CHAP secret. The CHAP secret should be between 12-16 characters and cannot contain spaces or most punctuation. string of 12 to 16 printable ASCII characters excluding ampersand and ^[];` |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_chap_user_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_chap_user_module.md#id5)

```yaml+jinja
# if state is create, then create chap user, fails if it exist or cannot create
# if state is present, then create chap user if not present, else success
- name: Create Chap User
  hpe.nimble.hpe_nimble_chap_user:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    description: "{{ description }}"
    user_password: "{{ user_password | mandatory }}"
    state: "{{ state | default('present') }}"

- name: Delete Chap User
  hpe.nimble.hpe_nimble_chap_user:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "absent"
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

[Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
[Homepage](http://hpe.com/storage/nimble)
[Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
