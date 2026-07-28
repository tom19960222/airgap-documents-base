---
collection: ansible
version: "8"
title: "Should you develop a module?"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/developing_modules.html
fetched_at: 2026-07-28T00:59:05+00:00
---
# Should you develop a module?

Developing Ansible modules is easy, but often it is not necessary. Before you start writing a new module, ask:

1. Does a similar module already exist?

An existing module may cover the functionality you want. Ansible collections include thousands of modules. Search our [list of included collections](../collections/index.md#list-of-collections) or [Ansible Galaxy](https://galaxy.ansible.com) to see if an existing module does what you need.

2. Should you use or develop an action plugin instead of a module?

An action plugin may be the best way to get the functionality you want. Action plugins run on the control node instead of on the managed node, and their functionality is available to all modules. For more information about developing plugins, read the [developing plugins page](developing_plugins.md#developing-plugins).

3. Should you use a role instead of a module?

A combination of existing modules may cover the functionality you want. You can write a role for this type of use case. Check out the [roles documentation](../playbook_guide/playbooks_reuse_roles.md#playbooks-reuse-roles).

4. Should you create a collection instead of a single module?

The functionality you want may be too large for a single module. If you want to connect Ansible to a new cloud provider, database, or network platform, you may need to [develop a new collection](developing_modules_in_groups.md#developing-modules-in-groups).

- Each module should have a concise and well defined functionality. Basically, follow the UNIX philosophy of doing one thing well.
- A module should not require that a user know all the underlying options of an API/tool to be used. For example, if the legal values for a required module parameter cannot be documented, that’s a sign that the module would be rejected.
- Modules should typically encompass much of the logic for interacting with a resource. A lightweight wrapper around an API that does not contain much logic would likely cause users to offload too much logic into a playbook, and for this reason the module would be rejected. Instead try creating multiple modules for interacting with smaller individual pieces of the API.

If your use case isn’t covered by an existing module, an action plugin, or a role, and you don’t need to create multiple modules, then you’re ready to start developing a new module. Choose from the topics below for next steps:

- I want to [get started on a new module](developing_modules_general.md#developing-modules-general).
- I want to review [tips and conventions for developing good modules](developing_modules_best_practices.md#developing-modules-best-practices).
- I want to [write a Windows module](developing_modules_general_windows.md#developing-modules-general-windows).
- I want [an overview of Ansible’s architecture](developing_program_flow_modules.md#developing-program-flow-modules).
- I want to [document my module](developing_modules_documenting.md#developing-modules-documenting).
- I want to [contribute my module to an existing Ansible collection](developing_modules_checklist.md#developing-modules-checklist).
- I want to [add unit and integration tests to my module](testing.md#developing-testing).
- I want to [add Python 3 support to my module](developing_python_3.md#developing-python-3).
- I want to [write multiple modules](developing_modules_in_groups.md#developing-modules-in-groups).

> **See also:**
>
> [Collection Index](../collections/index.md#list-of-collections)
> :   Browse existing collections, modules, and plugins
>
> [Mailing List](https://groups.google.com/group/ansible-devel)
> :   Development mailing list
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
