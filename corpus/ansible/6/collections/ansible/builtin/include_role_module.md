---
collection: ansible
version: "6"
title: "ansible.builtin.include_role module – Load and execute a role"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/include_role_module.html
fetched_at: 2026-07-27T16:42:45+00:00
---
# ansible.builtin.include_role module – Load and execute a role

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `include_role` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](include_role_module.md#synopsis)
- [Parameters](include_role_module.md#parameters)
- [Attributes](include_role_module.md#attributes)
- [Notes](include_role_module.md#notes)
- [See Also](include_role_module.md#see-also)
- [Examples](include_role_module.md#examples)

## [Synopsis](include_role_module.md#id1)

- Dynamically loads and executes a specified role as a task.
- May be used only where Ansible tasks are allowed - inside `pre_tasks`, `tasks`, or `post_tasks` play objects, or as a task inside a role.
- Task-level keywords, loops, and conditionals apply only to the `include_role` statement itself.
- To apply keywords to the tasks within the role, pass them using the `apply` option or use [ansible.builtin.import_role](import_role_module.md#ansible-collections-ansible-builtin-import-role-module) instead.
- Ignores some keywords, like `until` and `retries`.
- This module is also supported for Windows targets.
- Does not work in handlers.

## [Parameters](include_role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_duplicates**  boolean | Overrides the role’s metadata setting to allow using a role more than once with the same parameters.  Choices:   - `false` - `true` ← (default) |
| **apply**  string  added in Ansible 2.7 | Accepts a hash of task keywords (e.g. `tags`, `become`) that will be applied to all tasks within the included role. |
| **defaults_from**  string | File to load from a role’s `defaults/` directory.  Default: `"main"` |
| **handlers_from**  string  added in Ansible 2.8 | File to load from a role’s `handlers/` directory.  Default: `"main"` |
| **name**  string / required | The name of the role to be executed. |
| **public**  boolean  added in Ansible 2.7 | This option dictates whether the role’s `vars` and `defaults` are exposed to the play. If set to `yes` the variables will be available to tasks following the `include_role` task. This functionality differs from standard variable exposure for roles listed under the `roles` header or `import_role` as they are exposed to the play at playbook parsing time, and available to earlier roles and tasks as well.  Choices:   - `false` ← (default) - `true` |
| **rolespec_validate**  boolean  added in ansible-core 2.11 | Perform role argument spec validation if an argument spec is defined.  Choices:   - `false` - `true` ← (default) |
| **tasks_from**  string | File to load from a role’s `tasks/` directory.  Default: `"main"` |
| **vars_from**  string | File to load from a role’s `vars/` directory.  Default: `"main"` |

## [Attributes](include_role_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: none  While this action executes locally on the controller it is not governed by an action plugin | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **become** | Support: none | Is usable alongside become keywords |
| **bypass_host_loop** | Support: none | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | Support: none | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | Support: none | Uses the target’s configured connection information to execute code on it |
| **core** | Support: full | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | Support: none  Since there are no connection nor facts, there is no sense in delegating includes | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | Support: none | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | Platforms: all | Target OS/families that can be operated against |
| **tags** | Support: full  Tags are interpreted by this action but are not automatically inherited by the include tasks, see `apply` | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | Support: full | Denotes if this action objeys until/retry/poll keywords |

## [Notes](include_role_module.md#id4)

> **Note:**
>
> - Handlers and are made available to the whole play.
> - After Ansible 2.4, you can use [ansible.builtin.import_role](import_role_module.md#ansible-collections-ansible-builtin-import-role-module) for `static` behaviour and this action for `dynamic` one.

## [See Also](include_role_module.md#id5)

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
> [ansible.builtin.include_tasks](include_tasks_module.md#ansible-collections-ansible-builtin-include-tasks-module)
> :   Dynamically include a task list.
>
> [Including and importing](../../../user_guide/playbooks_reuse_includes.md#playbooks-reuse-includes)
> :   More information related to including and importing playbooks, roles and tasks.

## [Examples](include_role_module.md#id6)

```yaml+jinja
- ansible.builtin.include_role:
    name: myrole

- name: Run tasks/other.yaml instead of 'main'
  ansible.builtin.include_role:
    name: myrole
    tasks_from: other

- name: Pass variables to role
  ansible.builtin.include_role:
    name: myrole
  vars:
    rolevar1: value from task

- name: Use role in loop
  ansible.builtin.include_role:
    name: '{{ roleinputvar }}'
  loop:
    - '{{ roleinput1 }}'
    - '{{ roleinput2 }}'
  loop_control:
    loop_var: roleinputvar

- name: Conditional role
  ansible.builtin.include_role:
    name: myrole
  when: not idontwanttorun

- name: Apply tags to tasks within included file
  ansible.builtin.include_role:
    name: install
    apply:
      tags:
        - install
  tags:
    - always
```

### Authors

- Ansible Core Team (@ansible)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
