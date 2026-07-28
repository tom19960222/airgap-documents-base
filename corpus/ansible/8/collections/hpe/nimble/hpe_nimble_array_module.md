---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_array module – Manage the HPE Nimble Storage array"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_array_module.html
fetched_at: 2026-07-28T02:34:17+00:00
---
# hpe.nimble.hpe_nimble_array module – Manage the HPE Nimble Storage array

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
> see [Requirements](hpe_nimble_array_module.md#ansible-collections-hpe-nimble-hpe-nimble-array-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_array`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_array_module.md#synopsis)
- [Requirements](hpe_nimble_array_module.md#requirements)
- [Parameters](hpe_nimble_array_module.md#parameters)
- [Notes](hpe_nimble_array_module.md#notes)
- [Examples](hpe_nimble_array_module.md#examples)

## [Synopsis](hpe_nimble_array_module.md#id1)

- Manage the array on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_array_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_array_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_lower_limits**  boolean | A True setting will allow you to add an array with lower limits to a pool with higher limits.  **Choices:**   - `false` - `true` |
| **change_name**  string | Change the name of the existing array. |
| **create_pool**  boolean | Whether to create an associated pool during the array creation.  **Choices:**   - `false` - `true` |
| **ctrlr_a_support_ip**  string | Controller A Support IP Address. Four numbers in the range (0,255) separated by periods. |
| **ctrlr_b_support_ip**  string | Controller B Support IP Address. Four numbers in the range (0,255) separated by periods. |
| **failover**  boolean | Perform a failover on the specified array.  **Choices:**   - `false` - `true` |
| **force**  boolean | Forcibly delete the specified array.  **Choices:**   - `false` - `true` |
| **halt**  boolean | Halt the specified array. Restarting the array will require physically powering it back on.  **Choices:**   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **name**  string / required | The user-provided name of the array. It is also the array’s hostname. |
| **nic_list**  list / elements=dictionary | List NICs information. Used when creating an array. |
| **password**  string / required | HPE Nimble Storage password. |
| **pool_description**  string | Text description of the pool to be created during array creation. |
| **pool_name**  string | Name of pool to which this is a member. |
| **reboot**  boolean | Reboot the specified array.  **Choices:**   - `false` - `true` |
| **secondary_mgmt_ip**  string | Secondary management IP address for the group. |
| **serial**  string | Serial number of the array. |
| **state**  string / required | The array operation  **Choices:**   - `"create"` - `"present"` - `"absent"` |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_array_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_array_module.md#id5)

```yaml+jinja
# if state is create , then create a array if not present. Fails if already present.
# if state is present, then create a array if not present. Succeed if it already exists.
- name: Create array if not present
  hpe.nimble.hpe_nimble_array:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: "{{ state | default('present') }}"
    name: "{{ name }}"
    ctrlr_b_support_ip: "{{ ctrlr_b_support_ip | mandatory}}"
    ctrlr_a_support_ip: "{{ ctrlr_a_support_ip | mandatory}}"
    serial: "{{ serial | mandatory}}"
    nic_list: "{{ nic_list | mandatory}}"
    pool_name: "{{ pool_name | mandatory}}"

- name: Delete array
  hpe.nimble.hpe_nimble_array:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    vol_name: "{{ansible_default_ipv4['address']}}-{{ vol_name }}"
    name: "{{ name }}"
    state: absent

- name: Failover array
  hpe.nimble.hpe_nimble_array:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    failover: true
    state: present

- name: Halt array
  hpe.nimble.hpe_nimble_array:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: present
    halt: true

- name: Reboot array
  hpe.nimble.hpe_nimble_array:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    state: present
    reboot: true
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
