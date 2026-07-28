---
collection: ansible
version: "6"
title: "ansible.builtin.include module – Include a task list"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/include_module.html
fetched_at: 2026-07-27T16:43:05+00:00
---
# ansible.builtin.include module – Include a task list

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `include` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [DEPRECATED](include_module.md#deprecated)
- [Synopsis](include_module.md#synopsis)
- [Parameters](include_module.md#parameters)
- [Notes](include_module.md#notes)
- [See Also](include_module.md#see-also)
- [Examples](include_module.md#examples)
- [Status](include_module.md#status)

## [DEPRECATED](include_module.md#id1)

Removed in:
:   version 2.16

Why:
:   it has too many conflicting behaviours depending on keyword combinations and it was unclear how it should behave in each case. new actions were developed that were specific about each case and related behaviours.

Alternative:
:   include_tasks, import_tasks, import_playbook

## [Synopsis](include_module.md#id2)

- Includes a file with a list of tasks to be executed in the current playbook.
- Lists of tasks can only be included where tasks normally run (in play).
- Before Ansible 2.0, all includes were ‘static’ and were executed when the play was compiled.
- Static includes are not subject to most directives. For example, loops or conditionals are applied instead to each inherited task.
- Since Ansible 2.0, task includes are dynamic and behave more like real tasks. This means they can be looped, skipped and use variables from any source. Ansible tries to auto detect this, but you can use the `static` directive (which was added in Ansible 2.1) to bypass autodetection.
- This module is also supported for Windows targets.

## [Parameters](include_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **free-form**  string | This module allows you to specify the name of the file directly without any other options. |

## [Notes](include_module.md#id4)

> **Note:**
>
> - This is a core feature of Ansible, rather than a module, and cannot be overridden like a module.
> - Include has some unintuitive behaviours depending on if it is running in a static or dynamic in play or in playbook context, in an effort to clarify behaviours we are moving to a new set modules ([ansible.builtin.include_tasks](include_tasks_module.md#ansible-collections-ansible-builtin-include-tasks-module), [ansible.builtin.include_role](include_role_module.md#ansible-collections-ansible-builtin-include-role-module), [ansible.builtin.import_playbook](import_playbook_module.md#ansible-collections-ansible-builtin-import-playbook-module), [ansible.builtin.import_tasks](import_tasks_module.md#ansible-collections-ansible-builtin-import-tasks-module)) that have well established and clear behaviours.
> - This module no longer supporst including plays. Use [ansible.builtin.import_playbook](import_playbook_module.md#ansible-collections-ansible-builtin-import-playbook-module) instead.

## [See Also](include_module.md#id5)

> **See also:**
>
> [ansible.builtin.import_playbook](import_playbook_module.md#ansible-collections-ansible-builtin-import-playbook-module)
> :   Import a playbook.
>
> [ansible.builtin.import_role](import_role_module.md#ansible-collections-ansible-builtin-import-role-module)
> :   Import a role into a play.
>
> [ansible.builtin.import_tasks](import_tasks_module.md#ansible-collections-ansible-builtin-import-tasks-module)
> :   Import a task list.
>
> [ansible.builtin.include_role](include_role_module.md#ansible-collections-ansible-builtin-include-role-module)
> :   Load and execute a role.
>
> [ansible.builtin.include_tasks](include_tasks_module.md#ansible-collections-ansible-builtin-include-tasks-module)
> :   Dynamically include a task list.
>
> [Including and importing](../../../user_guide/playbooks_reuse_includes.md#playbooks-reuse-includes)
> :   More information related to including and importing playbooks, roles and tasks.

## [Examples](include_module.md#id6)

```yaml+jinja
- hosts: all
  tasks:
    - ansible.builtin.debug:
        msg: task1

    - name: Include task list in play
      ansible.builtin.include: stuff.yaml

    - ansible.builtin.debug:
        msg: task10

- hosts: all
  tasks:
    - ansible.builtin.debug:
        msg: task1

    - name: Include task list in play only if the condition is true
      ansible.builtin.include: "{{ hostvar }}.yaml"
      static: no
      when: hostvar is defined
```

## [Status](include_module.md#id7)

- This module will be removed in version 2.16.
  *[deprecated]*
- For more information see [DEPRECATED](include_module.md#deprecated).

### Authors

- Ansible Core Team (@ansible)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
