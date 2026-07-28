---
collection: ansible
version: "6"
title: "Module utilities"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/module_util.html
fetched_at: 2026-07-27T16:40:42+00:00
---
# Module utilities

- [Enabling module utilities](module_util.md#enabling-module-utilities)
- [Using module utilities](module_util.md#using-module-utilities)

Module utilities contain shared code used by multiple plugins. You can write [custom module utilities](../dev_guide/developing_module_utilities.md#developing-module-utilities).

## [Enabling module utilities](module_util.md#id1)

You can add a custom module utility by dropping it into a `module_utils` directory adjacent to your collection or role, just like any other plugin.

## [Using module utilities](module_util.md#id2)

For information on using module utilities, see [Using and developing module utilities](../dev_guide/developing_module_utilities.md#developing-module-utilities).

> **See also:**
>
> [Developing modules](../dev_guide/developing_modules_general.md#developing-modules-general)
> :   An introduction to creating Ansible modules
>
> [Developing collections](../dev_guide/developing_collections.md#developing-collections)
> :   An guide to creating Ansible collections
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [irc.libera.chat](https://libera.chat/)
> :   #ansible-devel IRC chat channel
