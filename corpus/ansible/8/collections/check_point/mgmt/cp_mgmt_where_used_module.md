---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_where_used module – Searches for usage of the target object in other objects and rules."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_where_used_module.html
fetched_at: 2026-07-28T01:18:33+00:00
---
# check_point.mgmt.cp_mgmt_where_used module – Searches for usage of the target object in other objects and rules.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_where_used`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_where_used_module.md#synopsis)
- [Parameters](cp_mgmt_where_used_module.md#parameters)
- [Examples](cp_mgmt_where_used_module.md#examples)
- [Return Values](cp_mgmt_where_used_module.md#return-values)

## [Synopsis](cp_mgmt_where_used_module.md#id1)

- Searches for usage of the target object in other objects and rules.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_where_used_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **async_response**  boolean | Run command in asynchronous mode and return task UID. Use show-task command to check the progress of the task.  **Choices:**   - `false` - `true` |
| **dereference_group_members**  boolean | Indicates whether to dereference “members” field by details level for every object in reply.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **domains_to_process**  list / elements=string | Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are, CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER. |
| **indirect**  boolean | Search for indirect usage.  **Choices:**   - `false` - `true` |
| **indirect_max_depth**  integer | Maximum nesting level during indirect usage search. |
| **name**  string | Object name. |
| **show_membership**  boolean | Indicates whether to calculate and show “groups” field for every object in reply.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_where_used_module.md#id3)

```yaml+jinja
- name: where-used
  cp_mgmt_where_used:
    name: Host 1
```

## [Return Values](cp_mgmt_where_used_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_where_used**  dictionary | The checkpoint where-used output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
