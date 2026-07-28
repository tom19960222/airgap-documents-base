---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_encryption module – Manage the HPE Nimble Storage encryption"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_encryption_module.html
fetched_at: 2026-07-28T02:34:19+00:00
---
# hpe.nimble.hpe_nimble_encryption module – Manage the HPE Nimble Storage encryption

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
> see [Requirements](hpe_nimble_encryption_module.md#ansible-collections-hpe-nimble-hpe-nimble-encryption-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_encryption`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_encryption_module.md#synopsis)
- [Requirements](hpe_nimble_encryption_module.md#requirements)
- [Parameters](hpe_nimble_encryption_module.md#parameters)
- [Notes](hpe_nimble_encryption_module.md#notes)
- [Examples](hpe_nimble_encryption_module.md#examples)

## [Synopsis](hpe_nimble_encryption_module.md#id1)

- Manage the encryption on an Nimble Storage group.

## [Requirements](hpe_nimble_encryption_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_encryption_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Whether the master key is active or not.  **Choices:**   - `false` - `true` |
| **age**  integer | Minimum age (in hours) of inactive encryption keys to be purged. ‘0’ indicates to purge the keys immediately. |
| **encryption_config**  dictionary | How encryption is configured for this group. Group encryption settings. |
| **group_encrypt**  boolean | Flag for setting group encryption.  **Choices:**   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **name**  string / required | Name of the master key. The only allowed value is “default”. |
| **new_passphrase**  string | When changing the passphrase, this attribute specifies the new value of the passphrase. String with size from 8 to 64 printable characters. |
| **passphrase**  string | Passphrase used to protect the master key, required during creation, enabling/disabling the key and change the passphrase to a new value. String with size from 8 to 64 printable characters. |
| **password**  string / required | HPE Nimble Storage password. |
| **purge_inactive**  boolean | Purges encryption keys that have been inactive for the age or longer. If you do not specify an age, the keys will be purged immediately.  **Choices:**   - `false` - `true` |
| **state**  string / required | The encryption operation.  **Choices:**   - `"create"` - `"present"` - `"absent"` |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_encryption_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_encryption_module.md#id5)

```yaml+jinja
# if state is create, then create master key, fails if it exist or cannot create
# if state is present, then create master key if not present ,else success
- name: Create master key
  hpe.nimble.hpe_nimble_encryption:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "default"
    passphrase: "{{ passphrase }}"
    active: "{{ active | default('false') }}"
    state: "{{ state | default('present') }}"

- name: Delete master key
  hpe.nimble.hpe_nimble_encryption:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "default"
    state: "absent"

- name: Purge inactive master key
  hpe.nimble.hpe_nimble_encryption:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "default"
    age: "{{ age | mandatory }}"
    state: "present"
    purge_inactive: true

- name: Group encryption
  hpe.nimble.hpe_nimble_encryption:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    encryption_config: "{{ encryption_config | mandatory }}"
    state: "present"
    group_encrypt: true
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
