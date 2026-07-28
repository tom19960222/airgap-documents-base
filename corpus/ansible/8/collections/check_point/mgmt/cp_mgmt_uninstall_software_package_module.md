---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_uninstall_software_package module – Uninstalls the software package from target machines."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_uninstall_software_package_module.html
fetched_at: 2026-07-28T01:18:22+00:00
---
# check_point.mgmt.cp_mgmt_uninstall_software_package module – Uninstalls the software package from target machines.

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/ui/repo/published/check_point/mgmt/) (version 5.1.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_uninstall_software_package`.

New in check_point.mgmt 2.0.0

- [Synopsis](cp_mgmt_uninstall_software_package_module.md#synopsis)
- [Parameters](cp_mgmt_uninstall_software_package_module.md#parameters)
- [Examples](cp_mgmt_uninstall_software_package_module.md#examples)
- [Return Values](cp_mgmt_uninstall_software_package_module.md#return-values)

## [Synopsis](cp_mgmt_uninstall_software_package_module.md#id1)

- Uninstalls the software package from target machines.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_uninstall_software_package_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cluster_installation_settings**  dictionary | Installation settings for cluster. |
| **cluster_delay**  integer | The delay between end of installation on one cluster members and start of installation on the next cluster member. |
| **cluster_strategy**  string | The cluster installation strategy. |
| **concurrency_limit**  integer | The number of targets, on which the same package is installed at the same time. |
| **name**  string | The name of the software package. |
| **targets**  list / elements=string | On what targets to execute this command. Targets may be identified by their name, or object unique identifier. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_uninstall_software_package_module.md#id3)

```yaml+jinja
- name: uninstall-software-package
  cp_mgmt_uninstall_software_package:
    name: Check_Point_R80_40_JHF_MCD_DEMO_019_MAIN_Bundle_T1_VISIBLE_FULL.tgz
    targets.1: corporate-gateway
```

## [Return Values](cp_mgmt_uninstall_software_package_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_uninstall_software_package**  dictionary | The checkpoint uninstall-software-package output.  **Returned:** always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
