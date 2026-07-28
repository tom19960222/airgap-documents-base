---
collection: ansible
version: "8"
title: "hpe.nimble.hpe_nimble_shelf module – Manage the HPE Nimble Storage shelves"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hpe/nimble/hpe_nimble_shelf_module.html
fetched_at: 2026-07-28T02:34:27+00:00
---
# hpe.nimble.hpe_nimble_shelf module – Manage the HPE Nimble Storage shelves

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
> see [Requirements](hpe_nimble_shelf_module.md#ansible-collections-hpe-nimble-hpe-nimble-shelf-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_shelf`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_shelf_module.md#synopsis)
- [Requirements](hpe_nimble_shelf_module.md#requirements)
- [Parameters](hpe_nimble_shelf_module.md#parameters)
- [Notes](hpe_nimble_shelf_module.md#notes)
- [Examples](hpe_nimble_shelf_module.md#examples)

## [Synopsis](hpe_nimble_shelf_module.md#id1)

- Manage the shelves on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_shelf_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_shelf_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accept_dedupe_impact**  boolean | Accept the reduction or elimination of deduplication capability on the system as a result of activating a shelf that does not meet the necessary deduplication requirements.  **Choices:**   - `false` - `true` |
| **accept_foreign**  boolean | Accept the removal of data on the shelf disks and activate foreign shelf.  **Choices:**   - `false` - `true` |
| **activated**  boolean / required | Activated state for shelf or disk set means it is available to store date on. An activated shelf may not be deactivated.  **Choices:**   - `false` - `true` |
| **driveset**  integer | Driveset to activate. |
| **force**  boolean | Forcibly activate shelf.  **Choices:**   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **last_request**  boolean | Indicates this is the last request in a series of shelf add requests.  **Choices:**   - `false` - `true` |
| **password**  string / required | HPE Nimble Storage password. |
| **shelf_serial**  string / required | Serial number of shelf. |
| **state**  string / required | The shelf operation.  **Choices:**   - `"present"` |
| **username**  string / required | HPE Nimble Storage user name. |

## [Notes](hpe_nimble_shelf_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_shelf_module.md#id5)

```yaml+jinja
- name: Update shelf
  hpe.nimble.hpe_nimble_shelf:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    shelf_serial: "{{ shelf_serial | mandatory }}"
    accept_foreign: "{{ accept_foreign }}"
    force: "{{ force }}"
    activated: "{{ activated }}"
    state: present
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

- [Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
- [Homepage](http://hpe.com/storage/nimble)
- [Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
