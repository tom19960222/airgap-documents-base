---
collection: ansible
version: "8"
title: "community.general.logentries_msg module – Send a message to logentries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/logentries_msg_module.html
fetched_at: 2026-07-28T01:47:35+00:00
---
# community.general.logentries_msg module – Send a message to logentries

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.logentries_msg`.

- [Synopsis](logentries_msg_module.md#synopsis)
- [Parameters](logentries_msg_module.md#parameters)
- [Attributes](logentries_msg_module.md#attributes)
- [Examples](logentries_msg_module.md#examples)

## [Synopsis](logentries_msg_module.md#id1)

- Send a message to logentries

Aliases: notification.logentries_msg

## [Parameters](logentries_msg_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api**  string | API endpoint  **Default:** `"data.logentries.com"` |
| **msg**  string / required | The message body. |
| **port**  integer | API endpoint port  **Default:** `80` |
| **token**  string / required | Log token. |

## [Attributes](logentries_msg_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](logentries_msg_module.md#id4)

```yaml+jinja
- name: Send a message to logentries
  community.general.logentries_msg:
    token=00000000-0000-0000-0000-000000000000
    msg="{{ ansible_hostname }}"
```

### Authors

- Jimmy Tang (@jcftang)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
