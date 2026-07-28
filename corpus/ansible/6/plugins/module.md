---
collection: ansible
version: "6"
title: "Modules"
source_url: https://docs.ansible.com/projects/ansible/6/plugins/module.html
fetched_at: 2026-07-27T16:40:42+00:00
---
# Modules

- [Enabling modules](module.md#enabling-modules)
- [Using modules](module.md#using-modules)

Modules are the main building blocks of Ansible playbooks. Although we do not generally speak of “module plugins”, a module is a type of plugin. For a developer-focused description of the differences between modules and other plugins, see [Modules and plugins: what is the difference?](../dev_guide/developing_locally.md#modules-vs-plugins).

## [Enabling modules](module.md#id3)

You can enable a custom module by dropping it into one of these locations:

- any directory added to the `ANSIBLE_LIBRARY` environment variable (`$ANSIBLE_LIBRARY` takes a colon-separated list like `$PATH`)
- `~/.ansible/plugins/modules/`
- `/usr/share/ansible/plugins/modules/`

For more information on using local custom modules, see [Adding a module outside of a collection](../dev_guide/developing_locally.md#local-modules).

## [Using modules](module.md#id4)

For information on using modules in ad hoc tasks, see [Introduction to ad hoc commands](../user_guide/intro_adhoc.md#intro-adhoc). For information on using modules in playbooks, see [Intro to playbooks](../user_guide/playbooks_intro.md#playbooks-intro).

> **See also:**
>
> [Intro to playbooks](../user_guide/playbooks_intro.md#about-playbooks)
> :   An introduction to playbooks
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
