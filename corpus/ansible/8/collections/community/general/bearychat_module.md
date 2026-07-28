---
collection: ansible
version: "8"
title: "community.general.bearychat module – Send BearyChat notifications"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/bearychat_module.html
fetched_at: 2026-07-28T01:44:47+00:00
---
# community.general.bearychat module – Send BearyChat notifications

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
> To use it in a playbook, specify: `community.general.bearychat`.

- [Synopsis](bearychat_module.md#synopsis)
- [Parameters](bearychat_module.md#parameters)
- [Attributes](bearychat_module.md#attributes)
- [Examples](bearychat_module.md#examples)
- [Return Values](bearychat_module.md#return-values)

## [Synopsis](bearychat_module.md#id1)

- The [community.general.bearychat](bearychat_module.md#ansible-collections-community-general-bearychat-module) module sends notifications to <https://bearychat.com> via the Incoming Robot integration.

Aliases: notification.bearychat

## [Parameters](bearychat_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attachments**  list / elements=dictionary | Define a list of attachments. For more information, see <https://github.com/bearyinnovative/bearychat-tutorial/blob/master/robots/incoming.md#attachments> |
| **channel**  string | Channel to send the message to. If absent, the message goes to the default channel selected by the `url`. |
| **markdown**  boolean | If `true`, text will be parsed as markdown.  **Choices:**   - `false` - `true` ← (default) |
| **text**  string | Message to send. |
| **url**  string / required | BearyChat WebHook URL. This authenticates you to the bearychat service. It looks like `https://hook.bearychat.com/=ae2CF/incoming/e61bd5c57b164e04b11ac02e66f47f60`. |

## [Attributes](bearychat_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](bearychat_module.md#id4)

```yaml+jinja
- name: Send notification message via BearyChat
  local_action:
    module: bearychat
    url: |
      https://hook.bearychat.com/=ae2CF/incoming/e61bd5c57b164e04b11ac02e66f47f60
    text: "{{ inventory_hostname }} completed"

- name: Send notification message via BearyChat all options
  local_action:
    module: bearychat
    url: |
      https://hook.bearychat.com/=ae2CF/incoming/e61bd5c57b164e04b11ac02e66f47f60
    text: "{{ inventory_hostname }} completed"
    markdown: false
    channel: "#ansible"
    attachments:
      - title: "Ansible on {{ inventory_hostname }}"
        text: "May the Force be with you."
        color: "#ffffff"
        images:
          - http://example.com/index.png
```

## [Return Values](bearychat_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | execution result  **Returned:** success  **Sample:** `"OK"` |

### Authors

- Jiangge Zhang (@tonyseek)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
