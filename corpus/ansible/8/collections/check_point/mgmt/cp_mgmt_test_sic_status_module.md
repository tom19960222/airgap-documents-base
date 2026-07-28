---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_test_sic_status module – Test SIC Status reflects the state of the gateway after it has received the certificate issued by the ICA. If the SIC status is Unknown then there is no connection between the gateway and the Security Management Server. If the SIC status is No Communication, an error message will appear. It may contain specific instructions on how to fix the situation."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_test_sic_status_module.html
fetched_at: 2026-07-28T01:18:08+00:00
---
# check_point.mgmt.cp_mgmt_test_sic_status module – Test SIC Status reflects the state of the gateway after it has received the certificate issued by the ICA. If the SIC status is Unknown then there is no connection between the gateway and the Security Management Server. If the SIC status is No Communication, an error message will appear. It may contain specific instructions on how to fix the situation.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_test_sic_status`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_test_sic_status_module.md#synopsis)
- [Parameters](cp_mgmt_test_sic_status_module.md#parameters)
- [Examples](cp_mgmt_test_sic_status_module.md#examples)
- [Return Values](cp_mgmt_test_sic_status_module.md#return-values)

## [Synopsis](cp_mgmt_test_sic_status_module.md#id1)

- Test SIC Status reflects the state of the gateway after it has received the certificate issued by the ICA. If the SIC status is Unknown then there is no connection between the gateway and the Security Management Server. If the SIC status is No Communication, an error message will appear. It may contain specific instructions on how to fix the situation.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_test_sic_status_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string | Gateway, cluster member or Check Point host name. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_test_sic_status_module.md#id3)

```yaml+jinja
- name: test-sic-status
  cp_mgmt_test_sic_status:
    name: gw1
```

## [Return Values](cp_mgmt_test_sic_status_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_test_sic_status**  dictionary | The checkpoint test-sic-status output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
