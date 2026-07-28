---
collection: ansible
version: "6"
title: "ansible.builtin.linear strategy – Executes tasks in a linear fashion"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/linear_strategy.html
fetched_at: 2026-07-27T16:43:08+00:00
---
# ansible.builtin.linear strategy – Executes tasks in a linear fashion

> **Note:**
>
> This strategy plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `linear` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same strategy plugin name.

- [Synopsis](linear_strategy.md#synopsis)
- [Notes](linear_strategy.md#notes)

## [Synopsis](linear_strategy.md#id1)

- Task execution is in lockstep per host batch as defined by `serial` (default all). Up to the fork limit of hosts will execute each task at the same time and then the next series of hosts until the batch is done, before going on to the next task.

## [Notes](linear_strategy.md#id2)

> **Note:**
>
> - This was the default Ansible behaviour before ‘strategy plugins’ were introduced in 2.0.

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
