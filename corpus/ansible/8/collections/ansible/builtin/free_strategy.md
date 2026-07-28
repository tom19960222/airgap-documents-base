---
collection: ansible
version: "8"
title: "ansible.builtin.free strategy – Executes tasks without waiting for all hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/free_strategy.html
fetched_at: 2026-07-28T01:05:13+00:00
---
# ansible.builtin.free strategy – Executes tasks without waiting for all hosts

> **Note:**
>
> This strategy plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `free`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.free` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same strategy plugin name.

- [Synopsis](free_strategy.md#synopsis)

## [Synopsis](free_strategy.md#id1)

- Task execution is as fast as possible per batch as defined by `serial` (default all). Ansible will not wait for other hosts to finish the current task before queuing more tasks for other hosts. All hosts are still attempted for the current task, but it prevents blocking new tasks for hosts that have already finished.
- With the free strategy, unlike the default linear strategy, a host that is slow or stuck on a specific task won’t hold up the rest of the hosts and tasks.

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
