---
collection: ansible
version: "8"
title: "ansible.posix.profile_roles callback – adds timing information to roles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/profile_roles_callback.html
fetched_at: 2026-07-28T01:09:36+00:00
---
# ansible.posix.profile_roles callback – adds timing information to roles

> **Note:**
>
> This callback plugin is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](profile_roles_callback.md#ansible-collections-ansible-posix-profile-roles-callback-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.profile_roles`.

- [Callback plugin](profile_roles_callback.md#callback-plugin)
- [Synopsis](profile_roles_callback.md#synopsis)
- [Requirements](profile_roles_callback.md#requirements)

## [Callback plugin](profile_roles_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](profile_roles_callback.md#id2)

- This callback module provides profiling for ansible roles.

## [Requirements](profile_roles_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
