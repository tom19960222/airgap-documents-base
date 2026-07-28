---
collection: ansible
version: "8"
title: "ansible.posix.timer callback – Adds time to play stats"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/timer_callback.html
fetched_at: 2026-07-28T01:09:38+00:00
---
# ansible.posix.timer callback – Adds time to play stats

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
> see [Requirements](timer_callback.md#ansible-collections-ansible-posix-timer-callback-requirements) for details.
>
> To use it in a playbook, specify: `ansible.posix.timer`.

- [Callback plugin](timer_callback.md#callback-plugin)
- [Synopsis](timer_callback.md#synopsis)
- [Requirements](timer_callback.md#requirements)

## [Callback plugin](timer_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](timer_callback.md#id2)

- This callback just adds total play duration to the play stats.

## [Requirements](timer_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelist in configuration

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
