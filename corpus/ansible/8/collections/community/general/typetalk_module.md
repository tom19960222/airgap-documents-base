---
collection: ansible
version: "8"
title: "community.general.typetalk module – Send a message to typetalk"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/typetalk_module.html
fetched_at: 2026-07-28T01:51:00+00:00
---
# community.general.typetalk module – Send a message to typetalk

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](typetalk_module.md#ansible-collections-community-general-typetalk-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.typetalk`.

- [Synopsis](typetalk_module.md#synopsis)
- [Requirements](typetalk_module.md#requirements)
- [Parameters](typetalk_module.md#parameters)
- [Attributes](typetalk_module.md#attributes)
- [Examples](typetalk_module.md#examples)

## [Synopsis](typetalk_module.md#id1)

- Send a message to typetalk using typetalk API

Aliases: notification.typetalk

## [Requirements](typetalk_module.md#id2)

The below requirements are needed on the host that executes this module.

- json

## [Parameters](typetalk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_id**  string / required | OAuth2 client ID |
| **client_secret**  string / required | OAuth2 client secret |
| **msg**  string / required | message body |
| **topic**  integer / required | topic id to post message |

## [Attributes](typetalk_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](typetalk_module.md#id5)

```yaml+jinja
- name: Send a message to typetalk
  community.general.typetalk:
    client_id: 12345
    client_secret: 12345
    topic: 1
    msg: install completed
```

### Authors

- Takashi Someda (@tksmd)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
