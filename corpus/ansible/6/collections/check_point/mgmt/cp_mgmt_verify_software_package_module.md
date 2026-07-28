---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_verify_software_package module – Verifies the software package on target machines."
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_verify_software_package_module.html
fetched_at: 2026-07-27T16:48:54+00:00
---
# check_point.mgmt.cp_mgmt_verify_software_package module – Verifies the software package on target machines.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_verify_software_package`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_verify_software_package_module.md#synopsis)
- [Parameters](cp_mgmt_verify_software_package_module.md#parameters)
- [Examples](cp_mgmt_verify_software_package_module.md#examples)
- [Return Values](cp_mgmt_verify_software_package_module.md#return-values)

## [Synopsis](cp_mgmt_verify_software_package_module.md#id1)

- Verifies the software package on target machines.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_verify_software_package_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **concurrency_limit**  integer | The number of targets, on which the same package is installed at the same time. |
| **download_package**  boolean | NOTE, Supported from Check Point version R81  Should the package be downloaded before verification.  Choices:   - `false` - `true` |
| **download_package_from**  string | NOTE, Supported from Check Point version R81  Where is the package located.  Choices:   - `"automatic"` - `"central"` - `"target-machine"` |
| **name**  string | The name of the software package. |
| **targets**  list / elements=string | On what targets to execute this command. Targets may be identified by their name, or object unique identifier. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_verify_software_package_module.md#id3)

```yaml+jinja
- name: verify-software-package
  cp_mgmt_verify_software_package:
    download_package: 'true'
    download_package_from: target-machine
    name: Check_Point_R80_40_JHF_MCD_DEMO_019_MAIN_Bundle_T1_VISIBLE_FULL.tgz
    targets.1: corporate-gateway
```

## [Return Values](cp_mgmt_verify_software_package_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_verify_software_package**  dictionary | The checkpoint verify-software-package output.  Returned: always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
