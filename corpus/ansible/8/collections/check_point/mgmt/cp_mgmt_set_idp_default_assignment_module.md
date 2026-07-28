---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_set_idp_default_assignment module – Set default Identity Provider assignment to be use for Management server administrator access."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_set_idp_default_assignment_module.html
fetched_at: 2026-07-28T01:17:29+00:00
---
# check_point.mgmt.cp_mgmt_set_idp_default_assignment module – Set default Identity Provider assignment to be use for Management server administrator access.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_set_idp_default_assignment`.

New in check_point.mgmt 3.0.0

- [Synopsis](cp_mgmt_set_idp_default_assignment_module.md#synopsis)
- [Parameters](cp_mgmt_set_idp_default_assignment_module.md#parameters)
- [Examples](cp_mgmt_set_idp_default_assignment_module.md#examples)
- [Return Values](cp_mgmt_set_idp_default_assignment_module.md#return-values)

## [Synopsis](cp_mgmt_set_idp_default_assignment_module.md#id1)

- Set default Identity Provider assignment to be use for Management server administrator access.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_set_idp_default_assignment_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_publish_session**  boolean | Publish the current session if changes have been performed after task completes.  **Choices:**   - `false` - `true` |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **identity_provider**  string | Represents the Identity Provider to be used for Login by this assignment identified by the name or UID, to cancel existing assignment should set to ‘none’. |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_set_idp_default_assignment_module.md#id3)

```yaml+jinja
- name: set-idp-default-assignment
  cp_mgmt_set_idp_default_assignment:
    identity_provider: azure
```

## [Return Values](cp_mgmt_set_idp_default_assignment_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_set_idp_default_assignment**  dictionary | The checkpoint set-idp-default-assignment output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
