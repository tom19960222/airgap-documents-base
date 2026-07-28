---
collection: ansible
version: "6"
title: "ansible.builtin.set_stats module – Define and display stats for the current ansible run"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/set_stats_module.html
fetched_at: 2026-07-27T16:44:07+00:00
---
# ansible.builtin.set_stats module – Define and display stats for the current ansible run

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `set_stats` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](set_stats_module.md#synopsis)
- [Parameters](set_stats_module.md#parameters)
- [Attributes](set_stats_module.md#attributes)
- [Notes](set_stats_module.md#notes)
- [Examples](set_stats_module.md#examples)

## [Synopsis](set_stats_module.md#id1)

- This module allows setting/accumulating stats on the current ansible run, either per host or for all hosts in the run.
- This module is also supported for Windows targets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](set_stats_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  boolean | Whether the provided value is aggregated to the existing stat `yes` or will replace it `no`.  Choices:   - `false` - `true` ← (default) |
| **data**  dictionary / required | A dictionary of which each key represents a stat (or variable) you want to keep track of. |
| **per_host**  boolean | whether the stats are per host or for all hosts in the run.  Choices:   - `false` ← (default) - `true` |

## [Attributes](set_stats_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: partial  While the action plugin does do some of the work it relies on the core engine to actually create the variables, that part cannot be overriden | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: none | Supports being used with the `async` keyword |
| **become** | Support: none | Is usable alongside become keywords |
| **bypass_host_loop** | Support: none | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **bypass_task_loop** | Support: none | These tasks ignore the `loop` and `with_` keywords |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **connection** | Support: none | Uses the target’s configured connection information to execute code on it |
| **core** | Support: partial  While parts of this action are implemented in core, other parts are still available as normal plugins and can be partially overridden | This is a ‘core engine’ feature and is not implemented like most task actions, so it is not overridable in any way via the plugin system. |
| **delegation** | Support: none | Can be used in conjunction with delegate_to and related keywords |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **ignore_conditional** | Support: none | The action is not subject to conditional execution so it will ignore the `when:` keyword |
| **platform** | Platforms: all | Target OS/families that can be operated against |
| **tags** | Support: full | Allows for the ‘tags’ keyword to control the selection of this action for execution |
| **until** | Support: full | Denotes if this action objeys until/retry/poll keywords |

## [Notes](set_stats_module.md#id4)

> **Note:**
>
> - In order for custom stats to be displayed, you must set `show_custom_stats` in section `[defaults]` in `ansible.cfg` or by defining environment variable `ANSIBLE_SHOW_CUSTOM_STATS` to `yes`. See the `default` callback plugin for details.

## [Examples](set_stats_module.md#id5)

```yaml+jinja
- name: Aggregating packages_installed stat per host
  ansible.builtin.set_stats:
    data:
      packages_installed: 31
    per_host: yes

- name: Aggregating random stats for all hosts using complex arguments
  ansible.builtin.set_stats:
    data:
      one_stat: 11
      other_stat: "{{ local_var * 2 }}"
      another_stat: "{{ some_registered_var.results | map(attribute='ansible_facts.some_fact') | list }}"
    per_host: no

- name: Setting stats (not aggregating)
  ansible.builtin.set_stats:
    data:
      the_answer: 42
    aggregate: no
```

### Authors

- Brian Coca (@bcoca)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
