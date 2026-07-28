---
collection: ansible
version: "6"
title: "Working With Modules"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/modules.html
fetched_at: 2026-07-27T16:40:30+00:00
---
# Working With Modules

- [Introduction to modules](modules_intro.md)
- [Module Maintenance & Support](modules_support.md)
- [Return Values](../reference_appendices/common_return_values.md)

Ansible ships with a number of modules (called the ‘module library’)
that can be executed directly on remote hosts or through [Playbooks](playbooks.md#working-with-playbooks).

Users can also write their own modules. These modules can control system resources,
like services, packages, or files (anything really), or handle executing system commands.

> **See also:**
>
> [Introduction to ad hoc commands](intro_adhoc.md#intro-adhoc)
> :   Examples of using modules in /usr/bin/ansible
>
> [Intro to playbooks](playbooks_intro.md#playbooks-intro)
> :   Introduction to using modules with /usr/bin/ansible-playbook
>
> [Developing modules](../dev_guide/developing_modules_general.md#developing-modules-general)
> :   How to write your own modules
>
> [Python API](../dev_guide/developing_api.md#developing-api)
> :   Examples of using modules with the Python API
>
> [Interpreter Discovery](../reference_appendices/interpreter_discovery.md#interpreter-discovery)
> :   Configuring the right Python interpreter on target hosts
>
> [Mailing List](https://groups.google.com/group/ansible-project)
> :   Questions? Help? Ideas? Stop by the list on Google Groups
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
