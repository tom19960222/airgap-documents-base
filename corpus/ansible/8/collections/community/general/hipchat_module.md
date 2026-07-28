---
collection: ansible
version: "8"
title: "community.general.hipchat module – Send a message to Hipchat"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hipchat_module.html
fetched_at: 2026-07-28T01:46:00+00:00
---
# community.general.hipchat module – Send a message to Hipchat

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
> To use it in a playbook, specify: `community.general.hipchat`.

- [Synopsis](hipchat_module.md#synopsis)
- [Parameters](hipchat_module.md#parameters)
- [Attributes](hipchat_module.md#attributes)
- [Examples](hipchat_module.md#examples)

## [Synopsis](hipchat_module.md#id1)

- Send a message to a Hipchat room, with options to control the formatting.

Aliases: notification.hipchat

## [Parameters](hipchat_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api**  string | API url if using a self-hosted hipchat server. For Hipchat API version 2 use the default URI with `/v2` instead of `/v1`.  **Default:** `"https://api.hipchat.com/v1"` |
| **color**  string | Background color for the message.  **Choices:**   - `"yellow"` ← (default) - `"red"` - `"green"` - `"purple"` - `"gray"` - `"random"` |
| **msg**  string / required | The message body. |
| **msg_format**  string | Message format.  **Choices:**   - `"text"` ← (default) - `"html"` |
| **msg_from**  aliases: from  string | Name the message will appear to be sent from. Max length is 15 characters - above this it will be truncated.  **Default:** `"Ansible"` |
| **notify**  boolean | If true, a notification will be triggered for users in the room.  **Choices:**   - `false` - `true` ← (default) |
| **room**  string / required | ID or name of the room. |
| **token**  string / required | API token. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](hipchat_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](hipchat_module.md#id4)

```yaml+jinja
- name: Send a message to a Hipchat room
  community.general.hipchat:
    room: notif
    msg: Ansible task finished

- name: Send a message to a Hipchat room using Hipchat API version 2
  community.general.hipchat:
    api: https://api.hipchat.com/v2/
    token: OAUTH2_TOKEN
    room: notify
    msg: Ansible task finished
```

### Authors

- Shirou Wakayama (@shirou)
- Paul Bourdel (@pb8226)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
