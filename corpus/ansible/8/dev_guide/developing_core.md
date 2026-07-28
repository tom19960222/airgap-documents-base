---
collection: ansible
version: "8"
title: "Developing ansible-core"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/developing_core.html
fetched_at: 2026-07-28T00:59:15+00:00
---
# Developing `ansible-core`

Although `ansible-core` (the code hosted in the [ansible/ansible repository](https://github.com/ansible/ansible) on GitHub) includes a few plugins that can be swapped out by the playbook directives or configuration, much of the code there is not modular. The documents here give insight into how the parts of `ansible-core` work together.

- [`ansible-core` project branches and tags](core_branches_and_tags.md)
- [Ansible module architecture](developing_program_flow_modules.md)

> **See also:**
>
> [Python API](developing_api.md#developing-api)
> :   Learn about the Python API for task execution
>
> [Developing plugins](developing_plugins.md#developing-plugins)
> :   Learn about developing plugins
>
> [Mailing List](https://groups.google.com/group/ansible-devel)
> :   The development mailing list
>
> [irc.libera.chat](https://libera.chat)
> :   #ansible-devel IRC chat channel
