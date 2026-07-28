---
collection: ansible
version: "6"
title: "ansible.builtin.group_by module – Create Ansible groups based on facts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/group_by_module.html
fetched_at: 2026-07-27T16:43:04+00:00
---
# ansible.builtin.group_by module – Create Ansible groups based on facts

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `group_by` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](group_by_module.md#synopsis)
- [Parameters](group_by_module.md#parameters)
- [Attributes](group_by_module.md#attributes)
- [Notes](group_by_module.md#notes)
- [See Also](group_by_module.md#see-also)
- [Examples](group_by_module.md#examples)

## [Synopsis](group_by_module.md#id1)

- Use facts to create ad-hoc groups that can be used later in a playbook.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](group_by_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **key**  string / required | The variables whose values will be used as groups. |
| **parents**  list / elements=string | The list of the parent groups.  Default: `["all"]` |

## [Attributes](group_by_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: full | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **become** | Support: none | Is usable alongside become keywords |
| **bypass_host_loop** | Support: full | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | Support: none | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | Support: partial  While this makes no changes to target systems the ‘in memory’ inventory will still be altered | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | Support: none | Uses the target’s configured connection information to execute code on it |
| **core** | Support: partial  While parts of this action are implemented in core, other parts are still available as normal plugins and can be partially overridden | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | Support: none | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | Support: none | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | Platforms: all | Target OS/families that can be operated against |
| **tags** | Support: full | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | Support: full | Denotes if this action objeys until/retry/poll keywords |

## [Notes](group_by_module.md#id4)

> **Note:**
>
> - Spaces in group names are converted to dashes ‘-‘.
> - Though this module does not change the remote host, we do provide ‘changed’ status as it can be useful for those trying to track inventory changes.

## [See Also](group_by_module.md#id5)

> **See also:**
>
> [ansible.builtin.add_host](add_host_module.md#ansible-collections-ansible-builtin-add-host-module)
> :   Add a host (and alternatively a group) to the ansible-playbook in-memory inventory.

## [Examples](group_by_module.md#id6)

```yaml+jinja
- name: Create groups based on the machine architecture
  ansible.builtin.group_by:
    key: machine_{{ ansible_machine }}

- name: Create groups like 'virt_kvm_host'
  ansible.builtin.group_by:
    key: virt_{{ ansible_virtualization_type }}_{{ ansible_virtualization_role }}

- name: Create nested groups
  ansible.builtin.group_by:
    key: el{{ ansible_distribution_major_version }}-{{ ansible_architecture }}
    parents:
      - el{{ ansible_distribution_major_version }}

- name: Add all active hosts to a static group
  ansible.builtin.group_by:
    key: done
```

### Authors

- Jeroen Hoekx (@jhoekx)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
