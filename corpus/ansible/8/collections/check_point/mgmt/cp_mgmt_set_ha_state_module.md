---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_set_ha_state module – Switch domain server high availability state."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_set_ha_state_module.html
fetched_at: 2026-07-28T01:17:28+00:00
---
# check_point.mgmt.cp_mgmt_set_ha_state module – Switch domain server high availability state.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_set_ha_state`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_set_ha_state_module.md#synopsis)
- [Parameters](cp_mgmt_set_ha_state_module.md#parameters)
- [Examples](cp_mgmt_set_ha_state_module.md#examples)
- [Return Values](cp_mgmt_set_ha_state_module.md#return-values)

## [Synopsis](cp_mgmt_set_ha_state_module.md#id1)

- Switch domain server high availability state. </br>After switching domain server to standby state, the session expires and you need to login again. <br/>You can run this command from a user or global domain on Multi Domain Server and from the user domain on Security Management Server.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_set_ha_state_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ignore_errors**  boolean | Apply changes ignoring errors.  **Choices:**   - `false` - `true` |
| **new_state**  string | Domain server new state.  **Choices:**   - `"active"` - `"standby"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_set_ha_state_module.md#id3)

```yaml+jinja
- name: set-ha-state
  cp_mgmt_set_ha_state:
    new_state: active
```

## [Return Values](cp_mgmt_set_ha_state_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_set_ha_state**  dictionary | The checkpoint set-ha-state output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
