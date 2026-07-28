---
collection: ansible
version: "8"
title: "ansible.posix.at module – Schedule the execution of a command or script file via the at command"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/at_module.html
fetched_at: 2026-07-28T01:09:25+00:00
---
# ansible.posix.at module – Schedule the execution of a command or script file via the at command

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this module,
> see [Requirements](at_module.md#ansible-collections-ansible-posix-at-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.at`.

New in ansible.posix 1.0.0

- [Synopsis](at_module.md#synopsis)
- [Requirements](at_module.md#requirements)
- [Parameters](at_module.md#parameters)
- [Examples](at_module.md#examples)

## [Synopsis](at_module.md#id1)

- Use this module to schedule a command or script file to run once in the future.
- All jobs are executed in the ‘a’ queue.

## [Requirements](at_module.md#id2)

The below requirements are needed on the host that executes this module.

- at

## [Parameters](at_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **command**  string | A command to be executed in the future. |
| **count**  integer | The count of units in the future to execute the command or script file. |
| **script_file**  string | An existing script file to be executed in the future. |
| **state**  string | The state dictates if the command or script file should be evaluated as present(added) or absent(deleted).  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **unique**  boolean | If a matching job is present a new job will not be added.  **Choices:**   - `false` ← (default) - `true` |
| **units**  string | The type of units in the future to execute the command or script file.  **Choices:**   - `"minutes"` - `"hours"` - `"days"` - `"weeks"` |

## [Examples](at_module.md#id4)

```yaml+jinja
- name: Schedule a command to execute in 20 minutes as root
  ansible.posix.at:
    command: ls -d / >/dev/null
    count: 20
    units: minutes

- name: Match a command to an existing job and delete the job
  ansible.posix.at:
    command: ls -d / >/dev/null
    state: absent

- name: Schedule a command to execute in 20 minutes making sure it is unique in the queue
  ansible.posix.at:
    command: ls -d / >/dev/null
    count: 20
    units: minutes
    unique: true
```

### Authors

- Richard Isaacson (@risaacson)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
