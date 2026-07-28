---
collection: ansible
version: "8"
title: "community.general.say callback – notify using software speech synthesizer"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/say_callback.html
fetched_at: 2026-07-28T01:52:03+00:00
---
# community.general.say callback – notify using software speech synthesizer

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](say_callback.md#ansible-collections-community-general-say-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.say`.

- [Callback plugin](say_callback.md#callback-plugin)
- [Synopsis](say_callback.md#synopsis)
- [Requirements](say_callback.md#requirements)
- [Notes](say_callback.md#notes)

## [Callback plugin](say_callback.md#id1)

This plugin is a **notification callback**. It sends information for a playbook run to other applications, services, or systems.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](say_callback.md#id2)

- This plugin will use the `say` or `espeak` program to “speak” about play events.

Aliases: osx_say

## [Requirements](say_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelisting in configuration
- the `/usr/bin/say` command line program (standard on macOS) or `espeak` command line program

## [Notes](say_callback.md#id4)

> **Note:**
>
> - In Ansible 2.8, this callback has been renamed from `osx_say` into [community.general.say](say_module.md#ansible-collections-community-general-say-module).

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
