---
collection: ansible
version: "8"
title: "community.general.discord module – Send Discord messages"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/discord_module.html
fetched_at: 2026-07-28T01:45:23+00:00
---
# community.general.discord module – Send Discord messages

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
> To use it in a playbook, specify: `community.general.discord`.

New in community.general 3.1.0

- [Synopsis](discord_module.md#synopsis)
- [Parameters](discord_module.md#parameters)
- [Attributes](discord_module.md#attributes)
- [See Also](discord_module.md#see-also)
- [Examples](discord_module.md#examples)
- [Return Values](discord_module.md#return-values)

## [Synopsis](discord_module.md#id1)

- Sends a message to a Discord channel using the Discord webhook API.

Aliases: notification.discord

## [Parameters](discord_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **avatar_url**  string | Overrides the default avatar of the webhook. |
| **content**  string | Content of the message to the Discord channel.  At least one of `content` and `embeds` must be specified. |
| **embeds**  list / elements=dictionary | Send messages as Embeds to the Discord channel.  Embeds can have a colored border, embedded images, text fields and more.  Allowed parameters are described in the Discord Docs: <https://discord.com/developers/docs/resources/channel#embed-object>  At least one of `content` and `embeds` must be specified. |
| **tts**  boolean | Set this to `true` if this is a TTS (Text to Speech) message.  **Choices:**   - `false` ← (default) - `true` |
| **username**  string | Overrides the default username of the webhook. |
| **webhook_id**  string / required | The webhook ID.  Format from Discord webhook URL: `/webhooks/{webhook.id}/{webhook.token}`. |
| **webhook_token**  string / required | The webhook token.  Format from Discord webhook URL: `/webhooks/{webhook.id}/{webhook.token}`. |

## [Attributes](discord_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](discord_module.md#id4)

> **See also:**
>
> [API documentation](https://discord.com/developers/docs/resources/webhook#execute-webhook)
> :   Documentation for Discord API

## [Examples](discord_module.md#id5)

```yaml+jinja
- name: Send a message to the Discord channel
  community.general.discord:
    webhook_id: "00000"
    webhook_token: "XXXYYY"
    content: "This is a message from ansible"

- name: Send a message to the Discord channel with specific username and avatar
  community.general.discord:
    webhook_id: "00000"
    webhook_token: "XXXYYY"
    content: "This is a message from ansible"
    username: Ansible
    avatar_url: "https://docs.ansible.com/ansible/latest/_static/images/logo_invert.png"

- name: Send a embedded message to the Discord channel
  community.general.discord:
    webhook_id: "00000"
    webhook_token: "XXXYYY"
    embeds:
      - title: "Embedded message"
        description: "This is an embedded message"
        footer:
          text: "Author: Ansible"
        image:
          url: "https://docs.ansible.com/ansible/latest/_static/images/logo_invert.png"

- name: Send two embedded messages
  community.general.discord:
    webhook_id: "00000"
    webhook_token: "XXXYYY"
    embeds:
      - title: "First message"
        description: "This is my first embedded message"
        footer:
          text: "Author: Ansible"
        image:
          url: "https://docs.ansible.com/ansible/latest/_static/images/logo_invert.png"
      - title: "Second message"
        description: "This is my first second message"
        footer:
          text: "Author: Ansible"
          icon_url: "https://docs.ansible.com/ansible/latest/_static/images/logo_invert.png"
        fields:
          - name: "Field 1"
            value: "Value of my first field"
          - name: "Field 2"
            value: "Value of my second field"
        timestamp: "{{ ansible_date_time.iso8601 }}"
```

## [Return Values](discord_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **http_code**  integer | Response Code returned by Discord API.  **Returned:** always  **Sample:** `204` |

### Authors

- Christian Wollinger (@cwollinger)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
