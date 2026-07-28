---
collection: ansible
version: "8"
title: "community.general.pushover module – Send notifications via https://pushover.net"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pushover_module.html
fetched_at: 2026-07-28T01:49:29+00:00
---
# community.general.pushover module – Send notifications via <https://pushover.net>

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
> To use it in a playbook, specify: `community.general.pushover`.

- [Synopsis](pushover_module.md#synopsis)
- [Parameters](pushover_module.md#parameters)
- [Attributes](pushover_module.md#attributes)
- [Notes](pushover_module.md#notes)
- [Examples](pushover_module.md#examples)

## [Synopsis](pushover_module.md#id1)

- Send notifications via pushover, to subscriber list of devices, and email addresses. Requires pushover app on devices.

Aliases: notification.pushover

## [Parameters](pushover_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **app_token**  string / required | Pushover issued token identifying your pushover app. |
| **device**  string  *added in community.general 1.2.0* | A device the message should be sent to. Multiple devices can be specified, separated by a comma. |
| **msg**  string / required | What message you wish to send. |
| **pri**  string | Message priority (see <https://pushover.net> for details).  **Choices:**   - `"-2"` - `"-1"` - `"0"` ← (default) - `"1"` - `"2"` |
| **title**  string | Message title. |
| **user_key**  string / required | Pushover issued authentication key for your user. |

## [Attributes](pushover_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](pushover_module.md#id4)

> **Note:**
>
> - You will require a pushover.net account to use this module. But no account is required to receive messages.

## [Examples](pushover_module.md#id5)

```yaml+jinja
- name: Send notifications via pushover.net
  community.general.pushover:
    msg: '{{ inventory_hostname }} is acting strange ...'
    app_token: wxfdksl
    user_key: baa5fe97f2c5ab3ca8f0bb59
  delegate_to: localhost

- name: Send notifications via pushover.net
  community.general.pushover:
    title: 'Alert!'
    msg: '{{ inventory_hostname }} has exploded in flames, It is now time to panic'
    pri: 1
    app_token: wxfdksl
    user_key: baa5fe97f2c5ab3ca8f0bb59
  delegate_to: localhost

- name: Send notifications via pushover.net to a specific device
  community.general.pushover:
    msg: '{{ inventory_hostname }} has been lost somewhere'
    app_token: wxfdksl
    user_key: baa5fe97f2c5ab3ca8f0bb59
    device: admins-iPhone
  delegate_to: localhost
```

### Authors

- Jim Richardson (@weaselkeeper)
- Bernd Arnold (@wopfel)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
