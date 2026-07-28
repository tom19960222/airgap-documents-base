---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_show_changes module – Show changes between two sessions."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_show_changes_module.html
fetched_at: 2026-07-28T01:17:38+00:00
---
# check_point.mgmt.cp_mgmt_show_changes module – Show changes between two sessions.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_show_changes`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_show_changes_module.md#synopsis)
- [Parameters](cp_mgmt_show_changes_module.md#parameters)
- [Examples](cp_mgmt_show_changes_module.md#examples)
- [Return Values](cp_mgmt_show_changes_module.md#return-values)

## [Synopsis](cp_mgmt_show_changes_module.md#id1)

- Show changes between two sessions.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_show_changes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dereference_group_members**  boolean | Indicates whether to dereference “members” field by details level for every object in reply.  **Choices:**   - `false` - `true` |
| **dereference_max_depth**  integer | When details level is full you can choose the number of levels in the API reply. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **from_date**  string | The date from which tracking changes is to be performed. ISO 8601. If timezone isn’t specified in the input, the Management server’s timezone is used. |
| **from_session**  string | The session UID from which tracking changes is to be performed. |
| **limit**  integer | Maximum number of sessions to analyze. |
| **offset**  integer | Number of sessions to skip (beginning with from-session). |
| **show_membership**  boolean | Indicates whether to calculate and show “groups” field for every object in reply.  **Choices:**   - `false` - `true` |
| **to_date**  string | The date until which tracking changes is to be performed. ISO 8601. If timezone isn’t specified in the input, the Management server’s timezone is used. |
| **to_session**  string | The session UID until which tracking changes is to be performed. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_show_changes_module.md#id3)

```yaml+jinja
- name: show-changes
  cp_mgmt_show_changes:
    from_date: '2017-02-01T08:20:50'
    to_date: '2017-02-21'
```

## [Return Values](cp_mgmt_show_changes_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_show_changes**  dictionary | The checkpoint show-changes output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
