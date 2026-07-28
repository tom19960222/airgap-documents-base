---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_set_policy_settings module – Edit Policy settings, the changes will be applied after publish."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_set_policy_settings_module.html
fetched_at: 2026-07-28T01:17:33+00:00
---
# check_point.mgmt.cp_mgmt_set_policy_settings module – Edit Policy settings, the changes will be applied after publish.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_set_policy_settings`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_set_policy_settings_module.md#synopsis)
- [Parameters](cp_mgmt_set_policy_settings_module.md#parameters)
- [Examples](cp_mgmt_set_policy_settings_module.md#examples)
- [Return Values](cp_mgmt_set_policy_settings_module.md#return-values)

## [Synopsis](cp_mgmt_set_policy_settings_module.md#id1)

- Edit Policy settings, the changes will be applied after publish.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_set_policy_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **last_in_cell**  string | Added object after removing the last object in cell.  **Choices:**   - `"none"` - `"restore to default"` |
| **none_object_behavior**  string | a ‘None’ object behavior. Rules with object ‘None’ will never be matched.  **Choices:**   - `"warning"` - `"error"` - `"none"` |
| **security_access_defaults**  dictionary | Access Policy default values. |
| **destination**  string | Destination default value for new rule creation. Any or None. |
| **service**  string | Service and Applications default value for new rule creation. Any or None. |
| **source**  string | Source default value for new rule creation. Any or None. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_set_policy_settings_module.md#id3)

```yaml+jinja
- name: set-policy-settings
  cp_mgmt_set_policy_settings:
    last_in_cell: any
    none_object_behavior: none
    security_access_defaults:
      destination: any
      service: any
      source: any
```

## [Return Values](cp_mgmt_set_policy_settings_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_set_policy_settings**  dictionary | The checkpoint set-policy-settings output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
