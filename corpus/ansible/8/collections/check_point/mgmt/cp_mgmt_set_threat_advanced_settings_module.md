---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_set_threat_advanced_settings module – Edit Threat Prevention’s Blades’ Settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_set_threat_advanced_settings_module.html
fetched_at: 2026-07-28T01:17:34+00:00
---
# check_point.mgmt.cp_mgmt_set_threat_advanced_settings module – Edit Threat Prevention’s Blades’ Settings.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_set_threat_advanced_settings`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_set_threat_advanced_settings_module.md#synopsis)
- [Parameters](cp_mgmt_set_threat_advanced_settings_module.md#parameters)
- [Examples](cp_mgmt_set_threat_advanced_settings_module.md#examples)
- [Return Values](cp_mgmt_set_threat_advanced_settings_module.md#return-values)

## [Synopsis](cp_mgmt_set_threat_advanced_settings_module.md#id1)

- Edit Threat Prevention’s Blades’ Settings.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_set_threat_advanced_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **feed_retrieving_interval**  string | Feed retrieving intervals of External Feed, in the form of HH,MM. |
| **httpi_non_standard_ports**  boolean | Enable HTTP Inspection on non standard ports for Threat Prevention blades.  **Choices:**   - `false` - `true` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **internal_error_fail_mode**  string | In case of internal system error, allow or block all connections.  **Choices:**   - `"allow connections"` - `"block connections"` |
| **log_unification_timeout**  integer | Session unification timeout for logs (minutes). |
| **resource_classification**  dictionary | Allow (Background) or Block (Hold) requests until categorization is complete. |
| **custom_settings**  dictionary | On Custom mode, custom resources classification per service. |
| **anti_bot**  string | Custom Settings for Anti Bot Blade.  **Choices:**   - `"background"` - `"hold"` |
| **anti_virus**  string | Custom Settings for Anti Virus Blade.  **Choices:**   - `"background"` - `"hold"` |
| **zero_phishing**  string | Custom Settings for Zero Phishing Blade.  **Choices:**   - `"background"` - `"hold"` |
| **mode**  string | Set all services to the same mode or choose a custom mode.  **Choices:**   - `"background"` - `"hold"` - `"custom"` |
| **web_service_fail_mode**  string | Block connections when the web service is unavailable.  **Choices:**   - `"allow connections"` - `"block connections"` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_set_threat_advanced_settings_module.md#id3)

```yaml+jinja
- name: set-threat-advanced-settings
  cp_mgmt_set_threat_advanced_settings:
    feed_retrieving_interval: 00:05
    httpi_non_standard_ports: true
    internal_error_fail_mode: allow connections
    log_unification_timeout: 600
    resource_classification.mode: hold
    resource_classification.web_service_fail_mode: block connections
```

## [Return Values](cp_mgmt_set_threat_advanced_settings_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_set_threat_advanced_settings**  dictionary | The checkpoint set-threat-advanced-settings output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
