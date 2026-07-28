---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_lsm_run_script module – Executes the lsm-run-script on a given list of targets. Run the given script on the targets devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_lsm_run_script_module.html
fetched_at: 2026-07-28T01:16:44+00:00
---
# check_point.mgmt.cp_mgmt_lsm_run_script module – Executes the lsm-run-script on a given list of targets. Run the given script on the targets devices.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_lsm_run_script`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_lsm_run_script_module.md#synopsis)
- [Parameters](cp_mgmt_lsm_run_script_module.md#parameters)
- [Examples](cp_mgmt_lsm_run_script_module.md#examples)
- [Return Values](cp_mgmt_lsm_run_script_module.md#return-values)

## [Synopsis](cp_mgmt_lsm_run_script_module.md#id1)

- Executes the lsm-run-script on a given list of targets. Run the given script on the targets devices.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_lsm_run_script_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **script**  string | The entire content of the script. |
| **script_base64**  string | The entire content of the script encoded in Base64. |
| **targets**  list / elements=string | On what targets to execute this command. Targets may be identified by their name, or object unique identifier. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_lsm_run_script_module.md#id3)

```yaml+jinja
- name: lsm-run-script
  cp_mgmt_lsm_run_script:
    script: ls -l /
    targets:
    - lsm_gateway
```

## [Return Values](cp_mgmt_lsm_run_script_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_lsm_run_script**  dictionary | The checkpoint lsm-run-script output.  **Returned:** always. |

### Authors

- Shiran Golzar (@chkp-shirango)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
