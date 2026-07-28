---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_snapshot module – Manage snapshots of the running states of selected features."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_snapshot_module.html
fetched_at: 2026-07-28T01:39:07+00:00
---
# cisco.nxos.nxos_snapshot module – Manage snapshots of the running states of selected features.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_snapshot`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_snapshot_module.md#synopsis)
- [Parameters](nxos_snapshot_module.md#parameters)
- [Notes](nxos_snapshot_module.md#notes)
- [Examples](nxos_snapshot_module.md#examples)
- [Return Values](nxos_snapshot_module.md#return-values)

## [Synopsis](nxos_snapshot_module.md#id1)

- Create snapshots of the running states of selected features, add new show commands for snapshot creation, delete and compare existing snapshots.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: snapshot

## [Parameters](nxos_snapshot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string / required | Define what snapshot action the module would perform.  **Choices:**   - `"add"` - `"compare"` - `"create"` - `"delete"` - `"delete_all"` |
| **compare_option**  string | Snapshot options to be used when `action=compare`.  **Choices:**   - `"summary"` - `"ipv4routes"` - `"ipv6routes"` |
| **comparison_results_file**  string | Name of the file where snapshots comparison will be stored when `action=compare`. |
| **description**  string | Snapshot description to be used when `action=create`. |
| **element_key1**  string | Specify the tags used to distinguish among row entries, to be used when `action=add`. |
| **element_key2**  string | Specify the tags used to distinguish among row entries, to be used when `action=add`. |
| **path**  string | Specify the path of the file where new created snapshot or snapshots comparison will be stored, to be used when `action=create` and `save_snapshot_locally=true` or `action=compare`.  **Default:** `"./"` |
| **row_id**  string | Specifies the tag of each row entry of the show command’s XML output, to be used when `action=add`. |
| **save_snapshot_locally**  boolean | Specify to locally store a new created snapshot, to be used when `action=create`.  **Choices:**   - `false` ← (default) - `true` |
| **section**  string | Used to name the show command output, to be used when `action=add`. |
| **show_command**  string | Specify a new show command, to be used when `action=add`. |
| **snapshot1**  string | First snapshot to be used when `action=compare`. |
| **snapshot2**  string | Second snapshot to be used when `action=compare`. |
| **snapshot_name**  string | Snapshot name, to be used when `action=create` or `action=delete`. |

## [Notes](nxos_snapshot_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `transport=cli` may cause timeout errors.
> - The `element_key1` and `element_key2` parameter specify the tags used to distinguish among row entries. In most cases, only the element_key1 parameter needs to specified to be able to distinguish among row entries.
> - `action=compare` will always store a comparison report on a local file.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_snapshot_module.md#id4)

```yaml+jinja
# Create a snapshot and store it locally
- cisco.nxos.nxos_snapshot:
    action: create
    snapshot_name: test_snapshot
    description: Done with Ansible
    save_snapshot_locally: true
    path: /home/user/snapshots/

# Delete a snapshot
- cisco.nxos.nxos_snapshot:
    action: delete
    snapshot_name: test_snapshot

# Delete all existing snapshots
- cisco.nxos.nxos_snapshot:
    action: delete_all

# Add a show command for snapshots creation
- cisco.nxos.nxos_snapshot:
    section: myshow
    show_command: show ip interface brief
    row_id: ROW_intf
    element_key1: intf-name

# Compare two snapshots
- cisco.nxos.nxos_snapshot:
    action: compare
    snapshot1: pre_snapshot
    snapshot2: post_snapshot
    comparison_results_file: compare_snapshots.txt
    compare_option: summary
    path: ../snapshot_reports/
```

## [Return Values](nxos_snapshot_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** verbose mode  **Sample:** `["snapshot create post_snapshot Post-snapshot"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
