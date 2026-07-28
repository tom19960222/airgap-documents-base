---
collection: ansible
version: "8"
title: "ansible.builtin.host_pinned strategy – Executes tasks on each host without interruption"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/host_pinned_strategy.html
fetched_at: 2026-07-28T01:08:42+00:00
---
# ansible.builtin.host_pinned strategy – Executes tasks on each host without interruption

> **Note:**
>
> This strategy plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `host_pinned`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.host_pinned` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same strategy plugin name.

New in Ansible 2.7

- [Synopsis](host_pinned_strategy.md#synopsis)

## [Synopsis](host_pinned_strategy.md#id1)

- Task execution is as fast as possible per host in batch as defined by `serial` (default all). Ansible will not start a play for a host unless the play can be finished without interruption by tasks for another host, i.e. the number of hosts with an active play does not exceed the number of forks. Ansible will not wait for other hosts to finish the current task before queuing the next task for a host that has finished. Once a host is done with the play, it opens it’s slot to a new host that was waiting to start. Other than that, it behaves just like the “free” strategy.

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
