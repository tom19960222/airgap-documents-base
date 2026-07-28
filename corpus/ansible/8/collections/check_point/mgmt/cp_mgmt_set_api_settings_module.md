---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_set_api_settings module – Edit API settings, the changes will be applied after publish followed by running ‘api restart’ command."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_set_api_settings_module.html
fetched_at: 2026-07-28T01:17:25+00:00
---
# check_point.mgmt.cp_mgmt_set_api_settings module – Edit API settings, the changes will be applied after publish followed by running ‘api restart’ command.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_set_api_settings`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_set_api_settings_module.md#synopsis)
- [Parameters](cp_mgmt_set_api_settings_module.md#parameters)
- [Examples](cp_mgmt_set_api_settings_module.md#examples)
- [Return Values](cp_mgmt_set_api_settings_module.md#return-values)

## [Synopsis](cp_mgmt_set_api_settings_module.md#id1)

- Edit API settings, the changes will be applied after publish followed by running ‘api restart’ command.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_set_api_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accepted_api_calls_from**  string | Clients allowed to connect to the API Server.  **Choices:**   - `"management server only"` - `"all ip addresses that can be used for gui clients"` - `"all ip addresses"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_set_api_settings_module.md#id3)

```yaml+jinja
- name: set-api-settings
  cp_mgmt_set_api_settings:
    accepted_api_calls_from: 'all ip addresses'
```

## [Return Values](cp_mgmt_set_api_settings_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_set_api_settings**  dictionary | The checkpoint set-api-settings output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
