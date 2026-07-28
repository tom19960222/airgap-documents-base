---
collection: ansible
version: "6"
title: "Become plugins"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/become.html
fetched_at: 2026-07-27T16:40:38+00:00
---
# Become plugins

- [Enabling Become Plugins](become.md#enabling-become-plugins)
- [Using Become Plugins](become.md#using-become-plugins)
- [Plugin List](become.md#plugin-list)

New in version 2.8.

Become plugins work to ensure that Ansible can use certain privilege escalation systems when running the basic
commands to work with the target machine as well as the modules required to execute the tasks specified in
the play.

These utilities (`sudo`, `su`, `doas`, and so on) generally let you ‘become’ another user to execute a command
with the permissions of that user.

## [Enabling Become Plugins](become.md#id2)

The become plugins shipped with Ansible are already enabled. Custom plugins can be added by placing
them into a `become_plugins` directory adjacent to your play, inside a role, or by placing them in one of
the become plugin directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

## [Using Become Plugins](become.md#id3)

In addition to the default configuration settings in [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings) or the
`--become-method` command line option, you can use the `become_method` keyword in a play or, if you need
to be ‘host specific’, the connection variable `ansible_become_method` to select the plugin to use.

You can further control the settings for each plugin via other configuration options detailed in the plugin
themselves (linked below).

## [Plugin List](become.md#id4)

You can use `ansible-doc -t become -l` to see the list of available plugins.
Use `ansible-doc -t become <plugin name>` to see specific documentation and examples.

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
