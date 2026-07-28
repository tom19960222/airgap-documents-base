---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_show_global_domain module – Retrieve existing object using object name or uid."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_show_global_domain_module.html
fetched_at: 2026-07-28T01:17:41+00:00
---
# check_point.mgmt.cp_mgmt_show_global_domain module – Retrieve existing object using object name or uid.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_show_global_domain`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_show_global_domain_module.md#synopsis)
- [Parameters](cp_mgmt_show_global_domain_module.md#parameters)
- [Examples](cp_mgmt_show_global_domain_module.md#examples)
- [Return Values](cp_mgmt_show_global_domain_module.md#return-values)

## [Synopsis](cp_mgmt_show_global_domain_module.md#id1)

- Retrieve existing object using object name or uid.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_show_global_domain_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **name**  string | Object name. This parameter is relevant only for getting a specific object. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_show_global_domain_module.md#id3)

```yaml+jinja
- name: show-global-domain
  cp_mgmt_show_global_domain:
    name: Global
```

## [Return Values](cp_mgmt_show_global_domain_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_show_global_domain**  dictionary | The checkpoint show-global-domain output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
