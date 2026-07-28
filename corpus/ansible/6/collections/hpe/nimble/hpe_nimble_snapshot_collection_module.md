---
collection: ansible
version: "6"
title: "hpe.nimble.hpe_nimble_snapshot_collection module – Manage the HPE Nimble Storage snapshot collections"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hpe/nimble/hpe_nimble_snapshot_collection_module.html
fetched_at: 2026-07-27T17:50:09+00:00
---
# hpe.nimble.hpe_nimble_snapshot_collection module – Manage the HPE Nimble Storage snapshot collections

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
> see [Requirements](hpe_nimble_snapshot_collection_module.md#ansible-collections-hpe-nimble-hpe-nimble-snapshot-collection-module-requirements) for details.
>
> To use it in a playbook, specify: `hpe.nimble.hpe_nimble_snapshot_collection`.

New in hpe.nimble 1.0.0

- [Synopsis](hpe_nimble_snapshot_collection_module.md#synopsis)
- [Requirements](hpe_nimble_snapshot_collection_module.md#requirements)
- [Parameters](hpe_nimble_snapshot_collection_module.md#parameters)
- [Notes](hpe_nimble_snapshot_collection_module.md#notes)
- [Examples](hpe_nimble_snapshot_collection_module.md#examples)

## [Synopsis](hpe_nimble_snapshot_collection_module.md#id1)

- Manage the snapshot collections on an HPE Nimble Storage group.

## [Requirements](hpe_nimble_snapshot_collection_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later
- Python 3.6 or later
- HPE Nimble Storage SDK for Python
- HPE Nimble Storage arrays running NimbleOS 5.0 or later

## [Parameters](hpe_nimble_snapshot_collection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **agent_type**  string | External management agent type for snapshots being created as part of snapshot collection. |
| **allow_writes**  boolean | Allow applications to write to created snapshot(s). Mandatory and must be set to ‘true’ for VSS application synchronized snapshots.  Choices:   - `false` - `true` |
| **change_name**  string | Change name of the existing snapshot collection. |
| **description**  string | Text description of snapshot collection. |
| **disable_appsync**  boolean | Do not perform application synchronization for this snapshot. Create a crash-consistent snapshot instead.  Choices:   - `false` - `true` |
| **expiry_after**  integer | Number of seconds after which this snapcoll is considered expired by the snapshot TTL. A value of 0 indicates that the snapshot never expires, 1 indicates that the snapshot uses a group-level configured TTL value and any other value indicates the number of seconds. |
| **force**  boolean | Forcibly delete the specified snapshot collection even if it is the last replicated snapshot. Doing so could lead to full re-seeding at the next replication.  Choices:   - `false` - `true` |
| **host**  string / required | HPE Nimble Storage IP address. |
| **invoke_on_upstream_partner**  boolean | Invoke snapshot request on upstream partner. This operation is not supported for synchronous replication volume collections.  Choices:   - `false` - `true` |
| **is_external_trigger**  boolean | Is externally triggered.  Choices:   - `false` - `true` |
| **metadata**  dictionary | Key-value pairs that augment a snapshot collection attributes. List of key-value pairs. Keys must be unique and non-empty. |
| **name**  string / required | Name of the snapshot collection. |
| **password**  string / required | HPE Nimble Storage password. |
| **replicate_to**  string | Specifies the partner name that the snapshots in this snapshot collection are replicated to. |
| **skip_db_consistency_check**  boolean | Skip consistency check for database files on this snapshot. This option only applies to volume collections with application synchronization set to VSS, application ID set to MS Exchange 2010 or later with Database Availability Group (DAG), snap_verify option set to true, and disable_appsync option set to false.  Choices:   - `false` - `true` |
| **snap_verify**  boolean | Run verification tool on this snapshot. This option can only be used with a volume collection that has application synchronization.  Choices:   - `false` - `true` |
| **start_online**  boolean | Start with snapshot set online.  Choices:   - `false` - `true` |
| **state**  string / required | The snapshot collection operation.  Choices:   - `"present"` - `"absent"` - `"create"` |
| **username**  string / required | HPE Nimble Storage user name. |
| **vol_snap_attr_list**  list / elements=dictionary | List of snapshot attributes for snapshots being created as part of snapshot collection creation. List of volumes with per snapshot attributes. |
| **volcoll**  string / required | Parent volume collection name. |

## [Notes](hpe_nimble_snapshot_collection_module.md#id4)

> **Note:**
>
> - This module does not support `check_mode`.

## [Examples](hpe_nimble_snapshot_collection_module.md#id5)

```yaml+jinja
# if state is create , then create a snapshot collection if not present. Fails if already present.
# if state is present, then create a snapshot collection if not present. Succeeds if it already exists
- name: Create snapshot collection if not present
  hpe.nimble.hpe_nimble_snapshot_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: "{{ state | default('present') }}"
    name: "{{ name | mandatory}}"
    volcoll: "{{ volcoll | mandatory}}"
    description: "{{ description }}"

- name: Delete snapshot collection (must be offline)
  hpe.nimble.hpe_nimble_snapshot_collection:
    host: "{{ host }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "{{ name }}"
    volcoll: "{{ volcoll }}"
    state: absent
```

### Authors

- HPE Nimble Storage Ansible Team (@ar-india)

### Collection links

[Issue Tracker](https://github.com/hpe-storage/nimble-ansible-modules/issues)
[Homepage](http://hpe.com/storage/nimble)
[Repository (Sources)](https://github.com/hpe-storage/nimble-ansible-modules)
