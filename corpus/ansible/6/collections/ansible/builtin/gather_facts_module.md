---
collection: ansible
version: "6"
title: "ansible.builtin.gather_facts module – Gathers facts about remote hosts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/gather_facts_module.html
fetched_at: 2026-07-27T16:44:01+00:00
---
# ansible.builtin.gather_facts module – Gathers facts about remote hosts

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `gather_facts` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

New in Ansible 2.8

- [Synopsis](gather_facts_module.md#synopsis)
- [Parameters](gather_facts_module.md#parameters)
- [Attributes](gather_facts_module.md#attributes)
- [Notes](gather_facts_module.md#notes)
- [Examples](gather_facts_module.md#examples)

## [Synopsis](gather_facts_module.md#id1)

- This module takes care of executing the [configured facts modules](../../../reference_appendices/config.md#facts-modules), the default is to use the [ansible.builtin.setup](setup_module.md#ansible-collections-ansible-builtin-setup-module) module.
- This module is automatically called by playbooks to gather useful variables about remote hosts that can be used in playbooks.
- It can also be executed directly by `/usr/bin/ansible` to check what variables are available to a host.
- Ansible provides many *facts* about the system, automatically.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](gather_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **parallel**  boolean | A toggle that controls if the fact modules are executed in parallel or serially and in order. This can guarantee the merge order of module facts at the expense of performance.  By default it will be true if more than one fact module is used.  Choices:   - `false` - `true` |

## [Attributes](gather_facts_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | Support: full | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | Support: partial  multiple modules can be executed in parallel or serially, but the action itself will not be async | Supports being used with the `async` keyword |
| **bypass_host_loop** | Support: none | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | Support: full  since this action should just query the target system info it always runs in check mode | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **facts** | Support: full | Action returns an `ansible_facts` dictionary that will update existing host facts |
| **platform** | Platforms: all  The action plugin should be able to automatically select the specific platform modules automatically or can be configured manually | Target OS/families that can be operated against |

## [Notes](gather_facts_module.md#id4)

> **Note:**
>
> - This is mostly a wrapper around other fact gathering modules.
> - Options passed into this action must be supported by all the underlying fact modules configured.
> - Facts returned by each module will be merged, conflicts will favor ‘last merged’. Order is not guaranteed, when doing parallel gathering on multiple modules.

## [Examples](gather_facts_module.md#id5)

```yaml+jinja
# Display facts from all hosts and store them indexed by hostname at /tmp/facts.
# ansible all -m ansible.builtin.gather_facts --tree /tmp/facts
```

### Authors

- Ansible Core Team

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
