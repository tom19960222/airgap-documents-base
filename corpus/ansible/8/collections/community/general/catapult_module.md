---
collection: ansible
version: "8"
title: "community.general.catapult module – Send a sms / mms using the catapult bandwidth api"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/catapult_module.html
fetched_at: 2026-07-28T01:44:57+00:00
---
# community.general.catapult module – Send a sms / mms using the catapult bandwidth api

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
> To use it in a playbook, specify: `community.general.catapult`.

- [Synopsis](catapult_module.md#synopsis)
- [Parameters](catapult_module.md#parameters)
- [Attributes](catapult_module.md#attributes)
- [Notes](catapult_module.md#notes)
- [Examples](catapult_module.md#examples)
- [Return Values](catapult_module.md#return-values)

## [Synopsis](catapult_module.md#id1)

- Allows notifications to be sent using sms / mms via the catapult bandwidth api.

Aliases: notification.catapult

## [Parameters](catapult_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_secret**  string / required | Api Secret from Api account page. |
| **api_token**  string / required | Api Token from Api account page. |
| **dest**  list / elements=string / required | The phone number or numbers the message should be sent to (must be in E.164 format, like `+19195551212`). |
| **media**  string | For MMS messages, a media url to the location of the media to be sent with the message. |
| **msg**  string / required | The contents of the text message (must be 2048 characters or less). |
| **src**  string / required | One of your catapult telephone numbers the message should come from (must be in E.164 format, like `+19195551212`). |
| **user_id**  string / required | User Id from Api account page. |

## [Attributes](catapult_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](catapult_module.md#id4)

> **Note:**
>
> - Will return changed even if the media url is wrong.
> - Will return changed if the destination number is invalid.

## [Examples](catapult_module.md#id5)

```yaml+jinja
- name: Send a mms to multiple users
  community.general.catapult:
    src: "+15035555555"
    dest:
      - "+12525089000"
      - "+12018994225"
    media: "http://example.com/foobar.jpg"
    msg: "Task is complete"
    user_id: "{{ user_id }}"
    api_token: "{{ api_token }}"
    api_secret: "{{ api_secret }}"

- name: Send a sms to a single user
  community.general.catapult:
    src: "+15035555555"
    dest: "+12018994225"
    msg: "Consider yourself notified"
    user_id: "{{ user_id }}"
    api_token: "{{ api_token }}"
    api_secret: "{{ api_secret }}"
```

## [Return Values](catapult_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether the api accepted the message.  **Returned:** always  **Sample:** `true` |

### Authors

- Jonathan Mainguy (@Jmainguy)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
