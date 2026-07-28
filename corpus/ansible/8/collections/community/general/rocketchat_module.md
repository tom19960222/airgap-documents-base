---
collection: ansible
version: "8"
title: "community.general.rocketchat module – Send notifications to Rocket Chat"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/rocketchat_module.html
fetched_at: 2026-07-28T01:50:01+00:00
---
# community.general.rocketchat module – Send notifications to Rocket Chat

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
> To use it in a playbook, specify: `community.general.rocketchat`.

- [Synopsis](rocketchat_module.md#synopsis)
- [Parameters](rocketchat_module.md#parameters)
- [Attributes](rocketchat_module.md#attributes)
- [Examples](rocketchat_module.md#examples)
- [Return Values](rocketchat_module.md#return-values)

## [Synopsis](rocketchat_module.md#id1)

- The `rocketchat` module sends notifications to Rocket Chat via the Incoming WebHook integration

Aliases: notification.rocketchat

## [Parameters](rocketchat_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attachments**  list / elements=dictionary | Define a list of attachments. |
| **channel**  string | Channel to send the message to. If absent, the message goes to the channel selected for the `token` specified during the creation of webhook. |
| **color**  string | Allow text to use default colors - use the default of ‘normal’ to not send a custom color bar at the start of the message  **Choices:**   - `"normal"` ← (default) - `"good"` - `"warning"` - `"danger"` |
| **domain**  string / required | The domain for your environment without protocol. (For example `example.com` or `chat.example.com`.) |
| **icon_emoji**  string | Emoji for the message sender. The representation for the available emojis can be got from Rocket Chat.  For example `:thumbsup:`.  If `icon_emoji` is set, `icon_url` will not be used. |
| **icon_url**  string | URL for the message sender’s icon.  **Default:** `"https://docs.ansible.com/favicon.ico"` |
| **link_names**  integer | Automatically create links for channels and usernames in `msg`.  **Choices:**   - `1` ← (default) - `0` |
| **msg**  string | Message to be sent. |
| **protocol**  string | Specify the protocol used to send notification messages before the webhook URL (that is, `http` or `https`).  **Choices:**   - `"http"` - `"https"` ← (default) |
| **token**  string / required | Rocket Chat Incoming Webhook integration token. This provides authentication to Rocket Chat’s Incoming webhook for posting messages. |
| **username**  string | This is the sender of the message.  **Default:** `"Ansible"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](rocketchat_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](rocketchat_module.md#id4)

```yaml+jinja
- name: Send notification message via Rocket Chat
  community.general.rocketchat:
    token: thetoken/generatedby/rocketchat
    domain: chat.example.com
    msg: '{{ inventory_hostname }} completed'
  delegate_to: localhost

- name: Send notification message via Rocket Chat all options
  community.general.rocketchat:
    domain: chat.example.com
    token: thetoken/generatedby/rocketchat
    msg: '{{ inventory_hostname }} completed'
    channel: #ansible
    username: 'Ansible on {{ inventory_hostname }}'
    icon_url: http://www.example.com/some-image-file.png
    link_names: 0
  delegate_to: localhost

- name: Insert a color bar in front of the message for visibility purposes and use the default webhook icon and name configured in rocketchat
  community.general.rocketchat:
    token: thetoken/generatedby/rocketchat
    domain: chat.example.com
    msg: '{{ inventory_hostname }} is alive!'
    color: good
    username: ''
    icon_url: ''
  delegate_to: localhost

- name: Use the attachments API
  community.general.rocketchat:
    token: thetoken/generatedby/rocketchat
    domain: chat.example.com
    attachments:
      - text: Display my system load on host A and B
        color: #ff00dd
        title: System load
        fields:
          - title: System A
            value: 'load average: 0,74, 0,66, 0,63'
            short: true
          - title: System B
            value: 'load average: 5,16, 4,64, 2,43'
            short: true
  delegate_to: localhost
```

## [Return Values](rocketchat_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | A flag indicating if any change was made or not.  **Returned:** success  **Sample:** `false` |

### Authors

- Ramon de la Fuente (@ramondelafuente)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
