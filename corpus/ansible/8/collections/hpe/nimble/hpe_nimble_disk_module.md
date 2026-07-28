---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_disk module – Manage the HPE Nimble Storage disk"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_disk_module.html
fetched_at: 2026-07-28T02:34:18+00:00
---
# hpe.nimble.hpe_nimble_disk module – Manage the HPE Nimble Storage disk

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
> see [Requirements](hpe_nimble_disk_module.md#ansible-collections-hpe-nimble-hpe-nimble-disk-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_disk`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_disk_module.md#synopsis)
- [Requirements](hpe_nimble_disk_module.md#requirements)
- [Parameters](hpe_nimble_disk_module.md#parameters)
- [Notes](hpe_nimble_disk_module.md#notes)
- [Examples](hpe_nimble_disk_module.md#examples)

## [Synopsis](hpe_nimble_disk_module.md#id1)

- Manage disks on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_disk_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_disk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **disk_op**  string / required | The intended operation to be performed on the specified disk.  **Choices:**   - `"add"` - `"remove"` |
| **force**  boolean | Forcibly add a disk.  **Choices:**   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **password**  string / required | HPE Nimble Storage password. |
| **shelf_location**  string / required | Position of the shelf the disk belongs to. |
| **slot**  integer / required | Disk slot number. |
| **state**  string / required | The disk operation.  **Choices:**   - `"present"` |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_disk_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_disk_module.md#id5)

```yaml+jinja
- name: Update Disk
  hpe.nimble.hpe_nimble_disk:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    slot: "{{ slot | mandatory }}"
    shelf_location: "{{ shelf_location | mandatory }}"
    disk_op: "{{ disk_op | mandatory }}"
    force: "{{ force }}"
    state: present
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
