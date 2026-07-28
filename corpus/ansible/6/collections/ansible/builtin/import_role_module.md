---
collection: ansible
version: "6"
title: "ansible.builtin.import_role module – Import a role into a play"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/import_role_module.html
fetched_at: 2026-07-27T16:42:45+00:00
---
# ansible.builtin.import_role module – Import a role into a play

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `import_role` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](import_role_module.md#synopsis)
- [Parameters](import_role_module.md#parameters)
- [Attributes](import_role_module.md#attributes)
- [Notes](import_role_module.md#notes)
- [See Also](import_role_module.md#see-also)
- [Examples](import_role_module.md#examples)

## [Synopsis](import_role_module.md#id1)

- Much like the `roles:` keyword, this task loads a role, but it allows you to control when the role tasks run in between other tasks of the play.
- Most keywords, loops and conditionals will only be applied to the imported tasks, not to this statement itself. If you want the opposite behavior, use [ansible.builtin.include_role](include_role_module.md#ansible-collections-ansible-builtin-include-role-module) instead.
- Does not work in handlers.

## [Parameters](import_role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_duplicates**  boolean | Overrides the role’s metadata setting to allow using a role more than once with the same parameters.  Choices:   - `false` - `true` ← (default) |
| **defaults_from**  string | File to load from a role’s `defaults/` directory.  Default: `"main"` |
| **handlers_from**  string  added in Ansible 2.8 | File to load from a role’s `handlers/` directory.  Default: `"main"` |
| **name**  string / required | The name of the role to be executed. |
| **rolespec_validate**  boolean  added in ansible-core 2.11 | Perform role argument spec validation if an argument spec is defined.  Choices:   - `false` - `true` ← (default) |
| **tasks_from**  string | File to load from a role’s `tasks/` directory.  Default: `"main"` |
| **vars_from**  string | File to load from a role’s `vars/` directory.  Default: `"main"` |

## [Attributes](import_role_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: none  While this action executes locally on the controller it is not governed by an action plugin | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **become** | Support: none | Is usable alongside become keywords |
| **bypass_host_loop** | Support: partial  While the import can be host specific and runs per host it is not dealing with all available host variables, use an include instead for those cases | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | Support: partial  The task itself is not looped, but the loop is applied to each imported task | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | Support: none | Uses the target’s configured connection information to execute code on it |
| **core** | Support: full | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | Support: none  Since there are no connection nor facts, there is no sense in delegating imports | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | Support: none  While the action itself will ignore the conditional, it will be inherited by the imported tasks themselves | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | Platforms: all | Target OS/families that can be operated against |
| **tags** | Support: full  Tags are not interpreted for this action, they are applied to the imported tasks | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | Support: full | Denotes if this action objeys until/retry/poll keywords |

## [Notes](import_role_module.md#id4)

> **Note:**
>
> - Handlers are made available to the whole play.
> - Since Ansible 2.7 variables defined in `vars` and `defaults` for the role are exposed to the play at playbook parsing time. Due to this, these variables will be accessible to roles and tasks executed before the location of the [ansible.builtin.import_role](import_role_module.md#ansible-collections-ansible-builtin-import-role-module) task.
> - Unlike [ansible.builtin.include_role](include_role_module.md#ansible-collections-ansible-builtin-include-role-module) variable exposure is not configurable, and will always be exposed.

## [See Also](import_role_module.md#id5)

> **See also:**
>
> [ansible.builtin.import_playbook](import_playbook_module.md#ansible-collections-ansible-builtin-import-playbook-module)
> :   Import a playbook.
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

## [Examples](import_role_module.md#id6)

```yaml+jinja
- hosts: all
  tasks:
    - ansible.builtin.import_role:
        name: myrole

    - name: Run tasks/other.yaml instead of 'main'
      ansible.builtin.import_role:
        name: myrole
        tasks_from: other

    - name: Pass variables to role
      ansible.builtin.import_role:
        name: myrole
      vars:
        rolevar1: value from task

    - name: Apply condition to each task in role
      ansible.builtin.import_role:
        name: myrole
      when: not idontwanttorun
```

### Authors

- Ansible Core Team (@ansible)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
