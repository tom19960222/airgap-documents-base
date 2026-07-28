---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_put_file module – put file on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_put_file_module.html
fetched_at: 2026-07-28T01:16:59+00:00
---
# check_point.mgmt.cp_mgmt_put_file module – put file on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_put_file`.

New in check_point.mgmt 1.0.0

- [Synopsis](cp_mgmt_put_file_module.md#synopsis)
- [Parameters](cp_mgmt_put_file_module.md#parameters)
- [Examples](cp_mgmt_put_file_module.md#examples)
- [Return Values](cp_mgmt_put_file_module.md#return-values)

## [Synopsis](cp_mgmt_put_file_module.md#id1)

- put file on Check Point over Web Services API
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_put_file_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **comments**  string | Comments string. |
| **file_content**  string | N/A |
| **file_name**  string | N/A |
| **file_path**  string | N/A |
| **targets**  list / elements=string | On what targets to execute this command. Targets may be identified by their name, or object unique identifier. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  **Choices:**   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  **Default:** `30` |

## [Examples](cp_mgmt_put_file_module.md#id3)

```yaml+jinja
- name: put-file
  cp_mgmt_put_file:
    file_content: 'vs ip 192.0.2.1
vs2 ip 192.0.2.2'
    file_name: vsx_conf
    file_path: /home/admin/
    targets:
    - corporate-gateway
```

## [Return Values](cp_mgmt_put_file_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_put_file**  dictionary | The checkpoint put-file output.  **Returned:** always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
