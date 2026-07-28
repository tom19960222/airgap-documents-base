---
collection: ansible
version: "8"
title: "ansible.builtin.import_playbook module – Import a playbook"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/import_playbook_module.html
fetched_at: 2026-07-28T01:07:34+00:00
---
# ansible.builtin.import_playbook module – Import a playbook

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `import_playbook` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.import_playbook` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](import_playbook_module.md#synopsis)
- [Parameters](import_playbook_module.md#parameters)
- [Attributes](import_playbook_module.md#attributes)
- [Notes](import_playbook_module.md#notes)
- [See Also](import_playbook_module.md#see-also)
- [Examples](import_playbook_module.md#examples)

## [Synopsis](import_playbook_module.md#id1)

- Includes a file with a list of plays to be executed.
- Files with a list of plays can only be included at the top level.
- You cannot use this action inside a play.

## [Parameters](import_playbook_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **free-form**  string | The name of the imported playbook is specified directly without any other option. |

## [Attributes](import_playbook_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **none**  While this action executes locally on the controller it is not governed by an action plugin | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **become** | **Support:** **none** | Is usable alongside become keywords |
| **bypass_host_loop** | **Support:** **partial**  While the import can be host specific and runs per host it is not dealing with all available host variables, use an include instead for those cases | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | **Support:** **partial**  The task itself is not looped, but the loop is applied to each imported task | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | **Support:** **none** | Uses the target’s configured connection information to execute code on it |
| **core** | **Support:** **full** | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | **Support:** **none**  Since there are no connection nor facts, there is no sense in delegating imports | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | **Support:** **none**  While the action itself will ignore the conditional, it will be inherited by the imported tasks themselves | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | **Platforms:** **all** | Target OS/families that can be operated against |
| **tags** | **Support:** **full**  Tags are not interpreted for this action, they are applied to the imported tasks | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | **Support:** **full** | Denotes if this action objeys until/retry/poll keywords |

## [Notes](import_playbook_module.md#id4)

> **Note:**
>
> - This is a core feature of Ansible, rather than a module, and cannot be overridden like a module.

## [See Also](import_playbook_module.md#id5)

> **See also:**
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
> [Including and importing](https://docs.ansible.com/ansible/6/user_guide/playbooks_reuse_includes.html#playbooks-reuse-includes "(in Ansible v6)")
> :   More information related to including and importing playbooks, roles and tasks.

## [Examples](import_playbook_module.md#id6)

```yaml+jinja
- hosts: localhost
  tasks:
    - ansible.builtin.debug:
        msg: play1

- name: Include a play after another play
  ansible.builtin.import_playbook: otherplays.yaml

- name: Set variables on an imported playbook
  ansible.builtin.import_playbook: otherplays.yml
  vars:
    service: httpd

- name: Include a playbook from a collection
  ansible.builtin.import_playbook: my_namespace.my_collection.my_playbook

- name: This DOES NOT WORK
  hosts: all
  tasks:
    - ansible.builtin.debug:
        msg: task1

    - name: This fails because I'm inside a play already
      ansible.builtin.import_playbook: stuff.yaml
```

### Authors

- Ansible Core Team (@ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
