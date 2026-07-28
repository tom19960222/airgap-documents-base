---
collection: ansible
version: "8"
title: "ovirt.ovirt.stdout callback – Output the log of ansible"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ovirt/ovirt/stdout_callback.html
fetched_at: 2026-07-28T02:50:19+00:00
---
# ovirt.ovirt.stdout callback – Output the log of ansible

> **Note:**
>
> This callback plugin is part of the [ovirt.ovirt collection](https://galaxy.ansible.com/ui/repo/published/ovirt/ovirt/) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ovirt.ovirt`.
>
> To use it in a playbook, specify: `ovirt.ovirt.stdout`.

New in ovirt.ovirt 2.0

- [Callback plugin](stdout_callback.md#callback-plugin)
- [Synopsis](stdout_callback.md#synopsis)

## [Callback plugin](stdout_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](stdout_callback.md#id2)

- This callback output the log of ansible play tasks.

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ovirt/ovirt-ansible-collection/issues)
- [Homepage](https://www.ovirt.org/)
- [Repository (Sources)](https://github.com/ovirt/ovirt-ansible-collection)
