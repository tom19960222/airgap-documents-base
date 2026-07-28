---
collection: ansible
version: "8"
title: "community.general.context_demo callback – demo callback that adds play/task context"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/context_demo_callback.html
fetched_at: 2026-07-28T01:51:52+00:00
---
# community.general.context_demo callback – demo callback that adds play/task context

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
> see [Requirements](context_demo_callback.md#ansible-collections-community-general-context-demo-callback-requirements) for details.
>
> To use it in a playbook, specify: `community.general.context_demo`.

- [Callback plugin](context_demo_callback.md#callback-plugin)
- [Synopsis](context_demo_callback.md#synopsis)
- [Requirements](context_demo_callback.md#requirements)

## [Callback plugin](context_demo_callback.md#id1)

This plugin is an **aggregate callback**. It adds additional console output next to the configured stdout callback.
See [Callback plugins](../../../plugins/callback.md#callback-plugins) for more information on callback plugins.

## [Synopsis](context_demo_callback.md#id2)

- Displays some play and task context along with normal output.
- This is mostly for demo purposes.

## [Requirements](context_demo_callback.md#id3)

The below requirements are needed on the local controller node that executes this callback.

- whitelist in configuration

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
