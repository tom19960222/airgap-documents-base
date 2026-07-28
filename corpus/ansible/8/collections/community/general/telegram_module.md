---
collection: ansible
version: "8"
title: "community.general.telegram module – Send notifications via telegram"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/telegram_module.html
fetched_at: 2026-07-28T01:50:57+00:00
---
# community.general.telegram module – Send notifications via telegram

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
> To use it in a playbook, specify: `community.general.telegram`.

- [Synopsis](telegram_module.md#synopsis)
- [Parameters](telegram_module.md#parameters)
- [Attributes](telegram_module.md#attributes)
- [Notes](telegram_module.md#notes)
- [Examples](telegram_module.md#examples)
- [Return Values](telegram_module.md#return-values)

## [Synopsis](telegram_module.md#id1)

- Send notifications via telegram bot, to a verified group or user.
- Also, the user may try to use any other telegram bot API method, if you specify `api_method` argument.

Aliases: notification.telegram

## [Parameters](telegram_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_args**  dictionary  *added in community.general 2.0.0* | Any parameters for the method.  For reference to default method, `SendMessage`, see <https://core.telegram.org/bots/api#sendmessage>. |
| **api_method**  string  *added in community.general 2.0.0* | Bot API method.  For reference, see <https://core.telegram.org/bots/api>.  **Default:** `"SendMessage"` |
| **token**  string / required | Token identifying your telegram bot. |

## [Attributes](telegram_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](telegram_module.md#id4)

> **Note:**
>
> - You will require a telegram account and create telegram bot to use this module.

## [Examples](telegram_module.md#id5)

```yaml+jinja
- name: Send notify to Telegram
  community.general.telegram:
    token: '9999999:XXXXXXXXXXXXXXXXXXXXXXX'
    api_args:
      chat_id: 000000
      parse_mode: "markdown"
      text: "Your precious application has been deployed: https://example.com"
      disable_web_page_preview: true
      disable_notification: true

- name: Forward message to someone
  community.general.telegram:
    token: '9999999:XXXXXXXXXXXXXXXXXXXXXXX'
    api_method: forwardMessage
    api_args:
      chat_id: 000000
      from_chat_id: 111111
      disable_notification: true
      message_id: '{{ saved_msg_id }}'
```

## [Return Values](telegram_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The message you attempted to send  **Returned:** success  **Sample:** `"Ansible task finished"` |
| **telegram_error**  string | Error message gotten from Telegram API  **Returned:** failure  **Sample:** `"Bad Request: message text is empty"` |

### Authors

- Artem Feofanov (@tyouxa)
- Nikolai Lomov (@lomserman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
