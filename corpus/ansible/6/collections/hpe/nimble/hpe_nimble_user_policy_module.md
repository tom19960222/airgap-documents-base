---
collection: ansible
version: "6"
title: "hpe.nimble.hpe_nimble_user_policy module – Manage the HPE Nimble Storage user policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hpe/nimble/hpe_nimble_user_policy_module.html
fetched_at: 2026-07-27T17:50:10+00:00
---
# hpe.nimble.hpe_nimble_user_policy module – Manage the HPE Nimble Storage user policies

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
> see [Requirements](hpe_nimble_user_policy_module.md#ansible-collections-hpe-nimble-hpe-nimble-user-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_user_policy`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_user_policy_module.md#synopsis)
- [Requirements](hpe_nimble_user_policy_module.md#requirements)
- [Parameters](hpe_nimble_user_policy_module.md#parameters)
- [Notes](hpe_nimble_user_policy_module.md#notes)
- [Examples](hpe_nimble_user_policy_module.md#examples)

## [Synopsis](hpe_nimble_user_policy_module.md#id1)

- Manage the user policies on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_user_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_user_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowed_attempts**  integer | Number of authentication attempts allowed before the user account is locked. Allowed range is [1, 10] inclusive. ‘0’ indicates no limit. |
| **digit**  integer | Number of numerical characters required in user passwords. Allowed range is [0, 255] inclusive. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **lower**  integer | Number of lowercase characters required in user passwords. Allowed range is [0, 255] inclusive. |
| **max_sessions**  integer | Maximum number of sessions allowed for a group. Allowed range is [10, 1000] inclusive. |
| **min_length**  integer | Minimum length for user passwords. Allowed range is [8, 255] inclusive. |
| **no_reuse**  integer | Number of times that a password must change before you can reuse a previous password. Allowed range is [1,20] inclusive. |
| **password**  string / required | HPE Nimble Storage password. |
| **previous_diff**  integer | Number of characters that must be different from the previous password. Allowed range is [1, 255] inclusive. |
| **special**  integer | Number of special characters required in user passwords. Allowed range is [0, 255] inclusive. |
| **state**  string / required | The user policy operation.  Choices:   - `"present"` |
| **upper**  integer | Number of uppercase characters required in user passwords. Allowed range is [0, 255] inclusive. |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_user_policy_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_user_policy_module.md#id5)

```yaml+jinja
- name: Update user policy
  hpe.nimble.hpe_nimble_user_policy:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    upper: "{{ upper }}"
    allowed_attempts: 2
    min_length: 10
    state: "present"
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

[Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
[Homepage](http://hpe.com/storage/nimble)
[Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
