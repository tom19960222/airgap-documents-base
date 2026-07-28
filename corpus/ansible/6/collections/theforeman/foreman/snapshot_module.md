---
collection: ansible
version: "6"
title: "theforeman.foreman.snapshot module – Manage Snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/snapshot_module.html
fetched_at: 2026-07-28T00:21:11+00:00
---
# theforeman.foreman.snapshot module – Manage Snapshots

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](snapshot_module.md#ansible-collections-theforeman-foreman-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.snapshot`.

New in theforeman.foreman 1.0.0

- [Synopsis](snapshot_module.md#synopsis)
- [Requirements](snapshot_module.md#requirements)
- [Parameters](snapshot_module.md#parameters)
- [Examples](snapshot_module.md#examples)
- [Return Values](snapshot_module.md#return-values)

## [Synopsis](snapshot_module.md#id1)

- Manage Snapshots for Host Entities
- This module can create, update, revert and delete snapshots
- This module requires the foreman_snapshot_management plugin set up in the server
- See: <https://github.com/ATIX-AG/foreman_snapshot_management>

## [Requirements](snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of Snapshot |
| **host**  string / required | Name of related Host |
| **include_ram**  boolean | Option to add RAM (only available for VMWare compute-resource)  Choices:   - `false` - `true` |
| **name**  string / required | Name of Snapshot |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of Snapshot  Choices:   - `"present"` ← (default) - `"reverted"` - `"absent"` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](snapshot_module.md#id4)

```yaml+jinja
- name: "Create a Snapshot"
  theforeman.foreman.snapshot:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "snapshot_before_software_upgrade"
    host: "server.example.com"
    state: present

- name: "Update a Snapshot"
  theforeman.foreman.snapshot:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "snapshot_before_software_upgrade"
    host: "server.example.com"
    description: "description of snapshot"
    state: present

- name: "Revert a Snapshot"
  theforeman.foreman.snapshot:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "snapshot_before_software_upgrade"
    host: "server.example.com"
    state: reverted

- name: "Delete a Snapshot"
  theforeman.foreman.snapshot:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "snapshot_before_software_upgrade"
    host: "server.example.com"
    state: absent
```

## [Return Values](snapshot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **snapshots**  list / elements=dictionary | List of snapshots.  Returned: success |

### Authors

- Manisha Singhal (@Manisha15) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
