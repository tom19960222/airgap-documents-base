---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_access_control_record module – Manage the HPE Nimble Storage access control records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_access_control_record_module.html
fetched_at: 2026-07-28T02:34:16+00:00
---
# hpe.nimble.hpe_nimble_access_control_record module – Manage the HPE Nimble Storage access control records

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
> see [Requirements](hpe_nimble_access_control_record_module.md#ansible-collections-hpe-nimble-hpe-nimble-access-control-record-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_access_control_record`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_access_control_record_module.md#synopsis)
- [Requirements](hpe_nimble_access_control_record_module.md#requirements)
- [Parameters](hpe_nimble_access_control_record_module.md#parameters)
- [Notes](hpe_nimble_access_control_record_module.md#notes)
- [Examples](hpe_nimble_access_control_record_module.md#examples)

## [Synopsis](hpe_nimble_access_control_record_module.md#id1)

- Manage the access control records on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_access_control_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_access_control_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply_to**  string | The type of object to which this access control record applies.  **Choices:**   - `"volume"` - `"snapshot"` - `"both"` |
| **chap_user**  string | Name for the CHAP user. |
| **host**  string / required | HPE Nimble Storage IP address. |
| **initiator_group**  string / required | The initiator group name. |
| **lun**  integer | If this access control record applies to a regular volume, this attribute is the volume’s LUN (Logical Unit Number).  If the access protocol is iSCSI, the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. |
| **password**  string / required | HPE Nimble Storage password. |
| **state**  string / required | The access control record operation.  **Choices:**   - `"present"` - `"absent"` - `"create"` |
| **username**  string / required | HPE Nimble Storage user name. |
| **volume**  string / required | The name of the volume that this access control record applies to. |

## [Notes](hpe_nimble_access_control_record_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_access_control_record_module.md#id5)

```yaml+jinja
# If state is "create", create access control record for given volume, fails if it exist.
# if state is present, create access control record if not already present.
- name: Create access control record for volume
  hpe.nimble.hpe_nimble_access_control_record:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    volume: "{{ volume }}"
    initiator_group: "{{ initiator_group }}"
    state: "{{ state | default('present') }}"

# Delete the access control record for a given volume name
- name: Delete access control record for volume
  hpe.nimble.hpe_nimble_access_control_record:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    volume: "{{ volume }}"
    initiator_group: "{{ initiator_group }}"
    state: "absent" # fail if volume does not exist
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
