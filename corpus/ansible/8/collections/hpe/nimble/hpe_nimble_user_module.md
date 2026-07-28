---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_user module – Manage the HPE Nimble Storage users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_user_module.html
fetched_at: 2026-07-28T02:34:29+00:00
---
# hpe.nimble.hpe_nimble_user module – Manage the HPE Nimble Storage users

> **Note:**
>
> This module is part of the [hpe.nimble collection](https://galaxy.ansible.com/ui/repo/published/hpe/nimble/) (version 1.1.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hpe.nimble`.
> You need further requirements to be able to use this module,
> see [Requirements](hpe_nimble_user_module.md#ansible-collections-hpe-nimble-hpe-nimble-user-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_user`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_user_module.md#synopsis)
- [Requirements](hpe_nimble_user_module.md#requirements)
- [Parameters](hpe_nimble_user_module.md#parameters)
- [Notes](hpe_nimble_user_module.md#notes)
- [Examples](hpe_nimble_user_module.md#examples)

## [Synopsis](hpe_nimble_user_module.md#id1)

- Manage the users on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth_password**  string | Authorization password for changing password. |
| **change_name**  string | Change name of the existing user. |
| **description**  string | Description of the user. |
| **disabled**  boolean | User is currently disabled.  **Choices:**   - `false` - `true` |
| **email_addr**  string | Email address of the user. |
| **full_name**  string | Fully qualified name of the user. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **inactivity_timeout**  integer | The amount of time that the user session is inactive before timing out. A value of 0 indicates that the timeout is taken from the group setting.  **Default:** `0` |
| **name**  string / required | Name of the user. |
| **password**  string / required | HPE Nimble Storage password. |
| **role**  string | Role of the user. Default is ‘guest’.  **Choices:**   - `"administrator"` - `"poweruser"` - `"operator"` - `"guest"` |
| **state**  string / required | The user operation.  **Choices:**   - `"create"` - `"present"` - `"absent"` |
| **unlock**  boolean | Unlock the user.  **Choices:**   - `false` - `true` |
| **user_password**  string | User’s login password. |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_user_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_user_module.md#id5)

```yaml+jinja
# if state is create, then create user, fails if it exist or cannot create
# if state is present, then create user if not present, else success
- name: Create user
  hpe.nimble.hpe_nimble_user:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    description: "{{ description }}"
    state: "{{ state | default('present') }}"

- name: Delete user
  hpe.nimble.hpe_nimble_user:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "absent"

- name: Unlock user
  hpe.nimble.hpe_nimble_user:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: "present"
    unlock: true
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
