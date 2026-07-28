---
collection: ansible
version: "8"
title: "check_point.mgmt.cp_mgmt_task_facts module – Get task objects facts on Checkpoint over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/check_point/mgmt/cp_mgmt_task_facts_module.html
fetched_at: 2026-07-28T01:18:07+00:00
---
# check_point.mgmt.cp_mgmt_task_facts module – Get task objects facts on Checkpoint over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_task_facts`.

New in check_point.mgmt 5.0.0

- [Synopsis](cp_mgmt_task_facts_module.md#synopsis)
- [Parameters](cp_mgmt_task_facts_module.md#parameters)
- [Examples](cp_mgmt_task_facts_module.md#examples)

## [Synopsis](cp_mgmt_task_facts_module.md#id1)

- Get task objects facts on Checkpoint devices.
- All operations are performed over Web Services API.
- This module handles both operations, get a specific object and get several objects, For getting a specific object use the parameter ‘name’.

## [Parameters](cp_mgmt_task_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **details_level**  string | The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.  **Choices:**   - `"uid"` - `"standard"` - `"full"` |
| **from_date**  string | The date from which tracking tasks is to be performed, by the task’s last update date. ISO 8601. If timezone isn’t specified in the input, the Management server’s timezone is used. |
| **initiator**  string | Initiator’s name. If name isn’t specified, tasks from all initiators will be shown. |
| **limit**  integer | The maximal number of returned results. This parameter is relevant only for getting few objects. |
| **offset**  integer | Number of the results to initially skip. This parameter is relevant only for getting few objects. |
| **order**  list / elements=dictionary | Sorts results by the given field. By default the results are sorted in the descending order by the task’s last update date. This parameter is relevant only for getting few objects. |
| **ASC**  string | Sorts results by the given field in ascending order.  **Choices:**   - `"name"` |
| **DESC**  string | Sorts results by the given field in descending order.  **Choices:**   - `"name"` |
| **status**  string | Status.  **Choices:**   - `"successful"` - `"failed"` - `"in-progress"` - `"all"` |
| **task_id**  list / elements=string | Unique identifier of one or more tasks. |
| **to_date**  string | The date until which tracking tasks is to be performed, by the task’s last update date. ISO 8601. If timezone isn’t specified in the input, the Management server’s timezone is used. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |

## [Examples](cp_mgmt_task_facts_module.md#id3)

```yaml+jinja
- name: show-task
  cp_mgmt_task_facts:
    task_id: 2eec70e5-78a8-4bdb-9a76-cfb5601d0bcb

- name: show-tasks
  cp_mgmt_task_facts:
    from_date: '2018-05-23T08:00:00'
    initiator: admin1
    status: successful
```

### Authors

- Eden Brillant (@chkp-edenbr)

### Collection links

- [Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
- [Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
