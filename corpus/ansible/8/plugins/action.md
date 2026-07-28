---
collection: ansible
version: "8"
title: "Action plugins"
source_url: https://docs.ansible.com/projects/ansible/8/plugins/action.html
fetched_at: 2026-07-28T01:00:10+00:00
---
# Action plugins

- [Enabling action plugins](action.md#enabling-action-plugins)
- [Using action plugins](action.md#using-action-plugins)
- [Plugin list](action.md#plugin-list)

Action plugins act in conjunction with [modules](https://docs.ansible.com/ansible/6/user_guide/modules.html#working-with-modules "(in Ansible v6)") to execute the actions required by playbook tasks. They usually execute automatically in the background doing prerequisite work before modules execute.

The ‘normal’ action plugin is used for modules that do not already have an action plugin. If necessary, you can [create custom action plugins](../dev_guide/developing_plugins.md#developing-actions).

## [Enabling action plugins](action.md#id2)

You can enable a custom action plugin by either dropping it into the `action_plugins` directory adjacent to your play, inside a role, or by putting it in one of the action plugin directory sources configured in [ansible.cfg](../reference_appendices/config.md#ansible-configuration-settings).

## [Using action plugins](action.md#id3)

Action plugin are executed by default when an associated module is used; no action is required.

## [Plugin list](action.md#id4)

You cannot list action plugins directly, they show up as their counterpart modules:

Use `ansible-doc -l` to see the list of available modules.
Use `ansible-doc <name>` to see plugin-specific documentation and examples. This should note if the module has a corresponding action plugin.

> **See also:**
>
> [Cache plugins](cache.md#cache-plugins)
> :   Cache plugins
>
> [Callback plugins](callback.md#callback-plugins)
> :   Callback plugins
>
> [Connection plugins](connection.md#connection-plugins)
> :   Connection plugins
>
> [Inventory plugins](inventory.md#inventory-plugins)
> :   Inventory plugins
>
> [Shell plugins](shell.md#shell-plugins)
> :   Shell plugins
>
> [Strategy plugins](strategy.md#strategy-plugins)
> :   Strategy plugins
>
> [Vars plugins](vars.md#vars-plugins)
> :   Vars plugins
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
