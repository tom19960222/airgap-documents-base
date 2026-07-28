---
collection: ansible
version: "8"
title: "ansible.builtin.include_tasks module – Dynamically include a task list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/include_tasks_module.html
fetched_at: 2026-07-28T01:05:07+00:00
---
# ansible.builtin.include_tasks module – Dynamically include a task list

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `include_tasks` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.include_tasks` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](include_tasks_module.md#synopsis)
- [Parameters](include_tasks_module.md#parameters)
- [Attributes](include_tasks_module.md#attributes)
- [See Also](include_tasks_module.md#see-also)
- [Examples](include_tasks_module.md#examples)

## [Synopsis](include_tasks_module.md#id1)

- Includes a file with a list of tasks to be executed in the current playbook.

## [Parameters](include_tasks_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **apply**  string  *added in Ansible 2.7* | Accepts a hash of task keywords (e.g. `tags`, `become`) that will be applied to the tasks within the include. |
| **file**  string  *added in Ansible 2.7* | Specifies the name of the file that lists tasks to add to the current playbook. |
| **free-form**  string | Specifies the name of the imported file directly without any other option `- include_tasks: file.yml`.  Is the equivalent of specifying an argument for the *file* parameter.  Most keywords, including loop, with_items, and conditionals, apply to this statement unlike [ansible.builtin.import_tasks](import_tasks_module.md#ansible-collections-ansible-builtin-import-tasks-module).  The do-until loop is not supported. |

## [Attributes](include_tasks_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **none**  While this action executes locally on the controller it is not governed by an action plugin | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **become** | **Support:** **none** | Is usable alongside become keywords |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | **Support:** **none** | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | **Support:** **none** | Uses the target’s configured connection information to execute code on it |
| **core** | **Support:** **full** | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | **Support:** **none**  Since there are no connection nor facts, there is no sense in delegating includes | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | **Support:** **none** | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against |
| **tags** | **Support:** **full**  Tags are interpreted by this action but are not automatically inherited by the include tasks, see `apply` | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | **Support:** **full** | Denotes if this action objeys until/retry/poll keywords |

## [See Also](include_tasks_module.md#id4)

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
> [Including and importing](https://docs.ansible.com/ansible/6/user_guide/playbooks_reuse_includes.html#playbooks-reuse-includes "(in Ansible v6)")
> :   More information related to including and importing playbooks, roles and tasks.

## [Examples](include_tasks_module.md#id5)

```yaml+jinja
- hosts: all
  tasks:
    - ansible.builtin.debug:
        msg: task1

    - name: Include task list in play
      ansible.builtin.include_tasks:
        file: stuff.yaml

    - ansible.builtin.debug:
        msg: task10

- hosts: all
  tasks:
    - ansible.builtin.debug:
        msg: task1

    - name: Include task list in play only if the condition is true
      ansible.builtin.include_tasks: "{{ hostvar }}.yaml"
      when: hostvar is defined

- name: Apply tags to tasks within included file
  ansible.builtin.include_tasks:
    file: install.yml
    apply:
      tags:
        - install
  tags:
    - always

- name: Apply tags to tasks within included file when using free-form
  ansible.builtin.include_tasks: install.yml
  args:
    apply:
      tags:
        - install
  tags:
    - always
```

### Authors

- Ansible Core Team (@ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
