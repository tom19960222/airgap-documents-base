---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_install_database module – Copies the user database and network objects information to specified targets."
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_install_database_module.html
fetched_at: 2026-07-27T16:48:04+00:00
---
# check_point.mgmt.cp_mgmt_install_database module – Copies the user database and network objects information to specified targets.

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/check_point/mgmt) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_install_database`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_install_database_module.md#synopsis)
- [Parameters](cp_mgmt_install_database_module.md#parameters)
- [Examples](cp_mgmt_install_database_module.md#examples)
- [Return Values](cp_mgmt_install_database_module.md#return-values)

## [Synopsis](cp_mgmt_install_database_module.md#id1)

- Copies the user database and network objects information to specified targets.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_install_database_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **targets**  list / elements=string | Check Point host(s) with one or more Management Software Blades enabled. The targets can be identified by their name or unique identifier. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_install_database_module.md#id3)

```yaml+jinja
- name: install-database
  cp_mgmt_install_database:
    targets:
    - checkpointhost1
    - checkpointhost2
```

## [Return Values](cp_mgmt_install_database_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_install_database**  dictionary | The checkpoint install-database output.  Returned: always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
