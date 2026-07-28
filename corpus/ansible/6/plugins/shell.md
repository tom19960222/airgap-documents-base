---
collection: ansible
version: "6"
title: "Shell plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/shell.html
fetched_at: 2026-07-27T16:40:43+00:00
---
# Shell plugins

- [Enabling shell plugins](shell.md#enabling-shell-plugins)
- [Using shell plugins](shell.md#using-shell-plugins)

Shell plugins work to ensure that the basic commands Ansible runs are properly formatted to work with
the target machine and allow the user to configure certain behaviors related to how Ansible executes tasks.

## [Enabling shell plugins](shell.md#id2)

You can add a custom shell plugin by dropping it into a `shell_plugins` directory adjacent to your play, inside a role,
or by putting it in one of the shell plugin directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

> **Warning:**
>
> You should not alter which plugin is used unless you have a setup in which the default `/bin/sh`
> is not a POSIX compatible shell or is not available for execution.

## [Using shell plugins](shell.md#id3)

In addition to the default configuration settings in [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings), you can use
the connection variable [ansible_shell_type](../user_guide/intro_inventory.md#ansible-shell-type) to select the plugin to use.
In this case, you will also want to update the [ansible_shell_executable](../user_guide/intro_inventory.md#ansible-shell-executable) to match.

You can further control the settings for each plugin via other configuration options
detailed in the plugin themselves (linked below).

> **See also:**
>
> [Intro to playbooks](../user_guide/playbooks_intro.md#about-playbooks)
> :   An introduction to playbooks
>
> [Inventory plugins](inventory.md#inventory-plugins)
> :   Inventory plugins
>
> [Callback plugins](callback.md#callback-plugins)
> :   Callback plugins
>
> [Filter plugins](filter.md#filter-plugins)
> :   Filter plugins
>
> [Test plugins](test.md#test-plugins)
> :   Test plugins
>
> [Lookup plugins](lookup.md#lookup-plugins)
> :   Lookup plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
