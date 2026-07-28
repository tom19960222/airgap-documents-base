---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_add_updatable_object module – Import an updatable object from the repository to the management server."
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_add_updatable_object_module.html
fetched_at: 2026-07-28T01:15:45+00:00
---
# check_point.mgmt.cp_mgmt_add_updatable_object module – Import an updatable object from the repository to the management server.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_add_updatable_object`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_add_updatable_object_module.md#synopsis)
- [Parameters](cp_mgmt_add_updatable_object_module.md#parameters)
- [Examples](cp_mgmt_add_updatable_object_module.md#examples)
- [Return Values](cp_mgmt_add_updatable_object_module.md#return-values)

## [Synopsis](cp_mgmt_add_updatable_object_module.md#id1)

- Import an updatable object from the repository to the management server. This operation takes effect immediately and doesn’t require publishing.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_add_updatable_object_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **color**  string | Color of the object. Should be one of existing colors.  **Choices:**   - `"aquamarine"` - `"black"` - `"blue"` - `"crete blue"` - `"burlywood"` - `"cyan"` - `"dark green"` - `"khaki"` - `"orchid"` - `"dark orange"` - `"dark sea green"` - `"pink"` - `"turquoise"` - `"dark blue"` - `"firebrick"` - `"brown"` - `"forest green"` - `"gold"` - `"dark gold"` - `"gray"` - `"dark gray"` - `"light green"` - `"lemon chiffon"` - `"coral"` - `"sea green"` - `"sky blue"` - `"magenta"` - `"purple"` - `"slate blue"` - `"violet red"` - `"navy blue"` - `"olive"` - `"orange"` - `"red"` - `"sienna"` - `"yellow"` |
| **comments**  string | Comments string. |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **ignore_errors**  boolean | Apply changes ignoring errors. You won’t be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.  **Choices:**   - `false` - `true` |
| **ignore_warnings**  boolean | Apply changes ignoring warnings.  **Choices:**   - `false` - `true` |
| **uid_in_updatable_objects_repository**  string | Unique identifier of the updatable object in the Updatable Objects Repository. |
| **uri**  string | URI of the updatable object in the Updatable Objects Repository. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_add_updatable_object_module.md#id3)

```yaml+jinja
- name: add-updatable-object
  cp_mgmt_add_updatable_object:
    uri: '{{uri}}'
```

## [Return Values](cp_mgmt_add_updatable_object_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_add_updatable_object**  dictionary | The checkpoint add-updatable-object output.  **Returned:** always. |

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
