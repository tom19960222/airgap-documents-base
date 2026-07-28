---
collection: ansible
version: "6"
title: "hpe.nimble.hpe_nimble_snapshot module – Manage the HPE Nimble Storage snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hpe/nimble/hpe_nimble_snapshot_module.html
fetched_at: 2026-07-27T17:50:08+00:00
---
# hpe.nimble.hpe_nimble_snapshot module – Manage the HPE Nimble Storage snapshots

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
> see [Requirements](hpe_nimble_snapshot_module.md#ansible-collections-hpe-nimble-hpe-nimble-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_snapshot`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_snapshot_module.md#synopsis)
- [Requirements](hpe_nimble_snapshot_module.md#requirements)
- [Parameters](hpe_nimble_snapshot_module.md#parameters)
- [Notes](hpe_nimble_snapshot_module.md#notes)
- [Examples](hpe_nimble_snapshot_module.md#examples)

## [Synopsis](hpe_nimble_snapshot_module.md#id1)

- Manage the snapshots on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **agent_type**  string | External management agent type.  Choices:   - `"none"` - `"smis"` - `"vvol"` - `"openstack"` - `"openstackv2"` |
| **app_uuid**  string | Application identifier of snapshot. |
| **change_name**  string | Change name of the existing snapshot. |
| **description**  string | Text description of snapshot. |
| **expiry_after**  integer | Number of seconds after which this snapshot is considered expired by snapshot TTL. A value of 0 indicates that snapshot never expires. |
| **force**  boolean | Forcibly delete the specified snapshot even if it is the last replicated collection. Doing so could lead to full re-seeding at the next replication.  Choices:   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **metadata**  dictionary | Key-value pairs that augment a snapshot’s attributes. List of key-value pairs. Keys must be unique and non-empty. |
| **name**  string / required | Name of the snapshot. |
| **online**  boolean | Online state for a snapshot means it could be mounted for data restore.  Choices:   - `false` - `true` |
| **password**  string / required | HPE Nimble Storage password. |
| **state**  string / required | The snapshot state.  Choices:   - `"present"` - `"absent"` - `"create"` |
| **username**  string / required | HPE Nimble Storage user name. |
| **volume**  string / required | Parent volume name. |
| **writable**  boolean | Allow snapshot to be writable. Mandatory and must be set to ‘true’ for VSS application synchronized snapshots.  Choices:   - `false` - `true` |

## [Notes](hpe_nimble_snapshot_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_snapshot_module.md#id5)

```yaml+jinja
# if state is create , then create a snapshot if not present. Fails if already present.
# if state is present, then create a snapshot if not present. Succeeds if it already exists.
- name: Create snapshot if not present
  hpe.nimble.hpe_nimble_snapshot:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: "{{ state | default('present') }}"
    volume: "{{ volume }}"
    name: "{{ name }}"
    online: "{{ online | default(true) }}"
    writable: "{{ writable | default(false) }}"

- name: Delete snapshot  (must be offline)
  hpe.nimble.hpe_nimble_snapshot:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    volume: "{{ volume }}"
    name: "{{ name }}"
    state: absent
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

[Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
[Homepage](http://hpe.com/storage/nimble)
[Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
