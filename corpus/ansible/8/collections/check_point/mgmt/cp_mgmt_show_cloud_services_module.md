---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_show_cloud_services module – Show the connection status of the Management Server to Check Point’s Infinity Portal."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_show_cloud_services_module.html
fetched_at: 2026-07-28T01:17:39+00:00
---
# check_point.mgmt.cp_mgmt_show_cloud_services module – Show the connection status of the Management Server to Check Point’s Infinity Portal.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_show_cloud_services`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_show_cloud_services_module.md#synopsis)
- [Parameters](cp_mgmt_show_cloud_services_module.md#parameters)
- [Examples](cp_mgmt_show_cloud_services_module.md#examples)
- [Return Values](cp_mgmt_show_cloud_services_module.md#return-values)

## [Synopsis](cp_mgmt_show_cloud_services_module.md#id1)

- Show the connection status of the Management Server to Check Point’s Infinity Portal.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_show_cloud_services_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_show_cloud_services_module.md#id3)

```yaml+jinja
- name: show-cloud-services
  cp_mgmt_show_cloud_services:
```

## [Return Values](cp_mgmt_show_cloud_services_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_show_cloud_services**  dictionary | The checkpoint show-cloud-services output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
