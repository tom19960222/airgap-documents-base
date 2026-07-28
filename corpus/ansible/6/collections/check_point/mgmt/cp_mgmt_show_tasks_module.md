---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_show_tasks module – Retrieve all tasks and show their progress and details."
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_show_tasks_module.html
fetched_at: 2026-07-27T16:48:39+00:00
---
# check_point.mgmt.cp_mgmt_show_tasks module – Retrieve all tasks and show their progress and details.

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_show_tasks`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_show_tasks_module.md#synopsis)
- [Parameters](cp_mgmt_show_tasks_module.md#parameters)
- [Examples](cp_mgmt_show_tasks_module.md#examples)
- [Return Values](cp_mgmt_show_tasks_module.md#return-values)

## [Synopsis](cp_mgmt_show_tasks_module.md#id1)

- Retrieve all tasks and show their progress and details.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_show_tasks_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  Choices:   - `"uid"` - `"standard"` - `"full"` |
| **from_date**  string | The date from which tracking tasks is to be performed, by the task’s last update date. ISO 8601. If timezone isn’t specified in the input, the Management server’s timezone is used. |
| **initiator**  string | Initiator’s name. If name isn’t specified, tasks from all initiators will be shown. |
| **limit**  integer | The maximal number of returned results. |
| **offset**  integer | Number of the results to initially skip. |
| **order**  list / elements=string | Sorts results by the given field. By default the results are sorted in the descending order by the task’s last update date. |
| **ASC**  string | Sorts results by the given field in ascending order.  Choices:   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  Choices:   - `"name"` |
| **status**  string | Status.  Choices:   - `"successful"` - `"failed"` - `"in-progress"` - `"all"` |
| **to_date**  string | The date until which tracking tasks is to be performed, by the task’s last update date. ISO 8601. If timezone isn’t specified in the input, the Management server’s timezone is used. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_show_tasks_module.md#id3)

```yaml+jinja
- name: show-tasks
  cp_mgmt_show_tasks:
    from_date: '2018-05-23T08:00:00'
    initiator: admin1
    status: successful
```

## [Return Values](cp_mgmt_show_tasks_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_show_tasks**  dictionary | The checkpoint show-tasks output.  Returned: always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
