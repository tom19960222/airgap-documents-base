---
collection: ansible
version: "6"
title: "hpe.nimble.hpe_nimble_fc module – Manage the HPE Nimble Storage Fibre Channel"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hpe/nimble/hpe_nimble_fc_module.html
fetched_at: 2026-07-27T17:50:00+00:00
---
# hpe.nimble.hpe_nimble_fc module – Manage the HPE Nimble Storage Fibre Channel

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
> see [Requirements](hpe_nimble_fc_module.md#ansible-collections-hpe-nimble-hpe-nimble-fc-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_fc`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_fc_module.md#synopsis)
- [Requirements](hpe_nimble_fc_module.md#requirements)
- [Parameters](hpe_nimble_fc_module.md#parameters)
- [Notes](hpe_nimble_fc_module.md#notes)
- [Examples](hpe_nimble_fc_module.md#examples)

## [Synopsis](hpe_nimble_fc_module.md#id1)

- Manage storage Fibre Channel on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_fc_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_fc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **array_name_or_serial**  string / required | Name or serial number of array where the interface is hosted. |
| **controller**  string | Name (A or B) of the controller where the interface is hosted. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **hw_upgrade**  boolean | Update fibre channel configuration after hardware changes. Possible values:- ‘true’ ‘false’.  Choices:   - `false` - `true` |
| **name**  string | Name of fibre channel interface |
| **online**  boolean | Identify whether the fibre channel interface is online. Possible values:- ‘true’ ‘false’.  Choices:   - `false` - `true` |
| **password**  string / required | HPE Nimble Storage password. |
| **precheck**  boolean | Check if the interfaces are offline before regenerating the WWNN. Possible values:- ‘true’ ‘false’.  Choices:   - `false` - `true` |
| **regenerate**  boolean | Regenerate fibre channel configuration. Possible values:- ‘true’ ‘false’.  Choices:   - `false` - `true` |
| **state**  string / required | The fibre channel operation.  Choices:   - `"present"` |
| **username**  string / required | HPE Nimble Storage user name. |
| **wwnn_base_str**  string | Base WWNN. Six bytes expressed in hex separated by colons. Example:- ‘af:32:f1’. |

## [Notes](hpe_nimble_fc_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_fc_module.md#id5)

```yaml+jinja
- name: Update fibre channel interface
  hpe.nimble.hpe_nimble_fc:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    array_name_or_serial: "{{ array_name_or_serial | mandatory }}"
    name: "{{ name | mandatory }}"
    controller: "{{ controller | mandatory }}"
    online: "{{ online | mandatory }}"
    state: "{{ 'present' }}"

- name: Regenerate fibre channel config
  hpe.nimble.hpe_nimble_fc:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    array_name_or_serial: "{{ array_name_or_serial | mandatory }}" # provide the group_leader_array name
    wwnn_base_str: "{{ wwnn_base_str | mandatory }}"
    regenerate: true
    precheck: true
    state: "{{ 'present' }}"

- name: Hardware upgrade for fibre channel
  hpe.nimble.hpe_nimble_fc:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    array_name_or_serial: "{{ array_name_or_serial | mandatory }}"
    hw_upgrade: true
    state: "{{ 'present' }}"
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

[Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
[Homepage](http://hpe.com/storage/nimble)
[Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
