---
collection: ansible
version: "6"
title: "check_point.mgmt.checkpoint_task_facts module – Get task objects facts on Check Point over Web Services API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/checkpoint_task_facts_module.html
fetched_at: 2026-07-27T16:47:32+00:00
---
# check_point.mgmt.checkpoint_task_facts module – Get task objects facts on Check Point over Web Services API

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
> To use it in a playbook, specify: `check_point.mgmt.checkpoint_task_facts`.

New in check_point.mgmt 2.7

- [Synopsis](checkpoint_task_facts_module.md#synopsis)
- [Parameters](checkpoint_task_facts_module.md#parameters)
- [Examples](checkpoint_task_facts_module.md#examples)

## [Synopsis](checkpoint_task_facts_module.md#id1)

- Get task objects facts on Check Point devices. All operations are performed over Web Services API.

## [Parameters](checkpoint_task_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **task_id**  string / required | ID of the task object. |

## [Examples](checkpoint_task_facts_module.md#id3)

```yaml+jinja
- name: Get task facts
  checkpoint_task_facts:
    task_id: 2eec70e5-78a8-4bdb-9a76-cfb5601d0bcb
```

### Authors

- Ansible by Red Hat (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
