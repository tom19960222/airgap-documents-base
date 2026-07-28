---
collection: ansible
version: "6"
title: "community.general.null callback – Don’t display stuff to screen"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/null_callback.html
fetched_at: 2026-07-27T17:14:34+00:00
---
# community.general.null callback – Don’t display stuff to screen

> **Note:**
>
> This callback plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this callback plugin,
> see [Requirements](null_callback.md#ansible-collections-community-general-null-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.null`.

- [Callback plugin](null_callback.md#callback-plugin)
- [Synopsis](null_callback.md#synopsis)
- [Requirements](null_callback.md#requirements)

## [Callback plugin](null_callback.md#id1)

This plugin is a **stdout callback**. You can use only use one stdout callback at a time. Additional aggregate or notification callbacks can be enabled though.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](null_callback.md#id2)

- This callback prevents outputing events to screen

## [Requirements](null_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- set as main display callback

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
