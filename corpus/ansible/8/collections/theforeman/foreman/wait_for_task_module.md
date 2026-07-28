---
collection: ansible
version: "8"
title: "theforeman.foreman.wait_for_task module – Wait for a task"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/wait_for_task_module.html
fetched_at: 2026-07-28T02:56:49+00:00
---
# theforeman.foreman.wait_for_task module – Wait for a task

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](wait_for_task_module.md#ansible-collections-theforeman-foreman-wait-for-task-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.wait_for_task`.

New in theforeman.foreman 3.13.0

- [Synopsis](wait_for_task_module.md#synopsis)
- [Requirements](wait_for_task_module.md#requirements)
- [Parameters](wait_for_task_module.md#parameters)
- [Attributes](wait_for_task_module.md#attributes)
- [Examples](wait_for_task_module.md#examples)
- [Return Values](wait_for_task_module.md#return-values)

## [Synopsis](wait_for_task_module.md#id1)

- Wait for a task to finish

## [Requirements](wait_for_task_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](wait_for_task_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **task**  string / required | Task id to wait for. |
| **timeout**  integer | How much time the task should take to be finished  **Default:** `60` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](wait_for_task_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](wait_for_task_module.md#id5)

```yaml+jinja
- name: Wait for a task to finish
  theforeman.foreman.wait_for_task:
    server_url:  "https://foreman.example.com"
    password: changeme
    username: admin
    task: a03ba49f-4dc2-4ad6-a48b-b271b46f3347
    timeout: 60

- name: Sarch for previously created tasks
  resource_info:
    server_url:  "https://foreman.example.com"
    password: changeme
    username: admin
    resource: foreman_tasks
    search: "(label = Actions::Katello::Product::Destroy and action ~ 'Test Product' and state = running)"
  register: tasks

- name: Wait for all found tasks to finish
  wait_for_task:
    server_url:  "https://foreman.example.com"
    password: changeme
    username: admin
    task: "{{ item }}"
    timeout: 900
  loop: "{{ tasks.resources | map(attribute='id') | list }}"
```

## [Return Values](wait_for_task_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **task**  dictionary | The finished task  **Returned:** success |

### Authors

- Julien Godin (@JGodin-C2C)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
