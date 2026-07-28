---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_delete_api_key module – Delete the API key. For the key to be invalid publish is needed."
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_delete_api_key_module.html
fetched_at: 2026-07-27T16:47:45+00:00
---
# check_point.mgmt.cp_mgmt_delete_api_key module – Delete the API key. For the key to be invalid publish is needed.

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/check_point/mgmt) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_delete_api_key`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_delete_api_key_module.md#synopsis)
- [Parameters](cp_mgmt_delete_api_key_module.md#parameters)
- [Examples](cp_mgmt_delete_api_key_module.md#examples)
- [Return Values](cp_mgmt_delete_api_key_module.md#return-values)

## [Synopsis](cp_mgmt_delete_api_key_module.md#id1)

- Delete the API key. For the key to be invalid publish is needed.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_delete_api_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_name**  string | Administrator name to generate API key for. |
| **admin_uid**  string | Administrator uid to generate API key for. |
| **api_key**  string | API key to be deleted. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_delete_api_key_module.md#id3)

```yaml+jinja
- name: delete-api-key
  cp_mgmt_delete_api_key:
    api_key: eea3be76f4a8eb740ee872bcedc692748ff256a2d21c9ffd2754facbde046d00
    state: absent
```

## [Return Values](cp_mgmt_delete_api_key_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_delete_api_key**  dictionary | The checkpoint delete-api-key output.  Returned: always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
