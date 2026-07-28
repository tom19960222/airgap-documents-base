---
collection: ansible
version: "6"
title: "community.general.cisco_webex module – Send a message to a Cisco Webex Teams Room or Individual"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/cisco_webex_module.html
fetched_at: 2026-07-27T17:08:22+00:00
---
# community.general.cisco_webex module – Send a message to a Cisco Webex Teams Room or Individual

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.cisco_webex`.

- [Synopsis](cisco_webex_module.md#synopsis)
- [Parameters](cisco_webex_module.md#parameters)
- [Notes](cisco_webex_module.md#notes)
- [Examples](cisco_webex_module.md#examples)
- [Return Values](cisco_webex_module.md#return-values)

## [Synopsis](cisco_webex_module.md#id1)

- Send a message to a Cisco Webex Teams Room or Individual with options to control the formatting.

## [Parameters](cisco_webex_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **msg**  string / required | The message you would like to send. |
| **msg_type**  aliases: message_type  string | Specifies how you would like the message formatted.  Choices:   - `"text"` ← (default) - `"markdown"` |
| **personal_token**  aliases: token  string / required | Your personal access token required to validate the Webex Teams API. |
| **recipient_id**  string / required | The unique identifier associated with the supplied `recipient_type`. |
| **recipient_type**  string / required | The request parameter you would like to send the message to.  Messages can be sent to either a room or individual (by ID or E-Mail).  Choices:   - `"roomId"` - `"toPersonEmail"` - `"toPersonId"` |

## [Notes](cisco_webex_module.md#id3)

> **Note:**
>
> - The `recipient_id` type must be valid for the supplied `recipient_id`.
> - Full API documentation can be found at <https://developer.webex.com/docs/api/basics>.

## [Examples](cisco_webex_module.md#id4)

```yaml+jinja
# Note: The following examples assume a variable file has been imported
# that contains the appropriate information.

- name: Cisco Webex Teams - Markdown Message to a Room
  community.general.cisco_webex:
    recipient_type: roomId
    recipient_id: "{{ room_id }}"
    msg_type: markdown
    personal_token: "{{ token }}"
    msg: "**Cisco Webex Teams Ansible Module - Room Message in Markdown**"

- name: Cisco Webex Teams - Text Message to a Room
  community.general.cisco_webex:
    recipient_type: roomId
    recipient_id: "{{ room_id }}"
    msg_type: text
    personal_token: "{{ token }}"
    msg: "Cisco Webex Teams Ansible Module - Room Message in Text"

- name: Cisco Webex Teams - Text Message by an Individuals ID
  community.general.cisco_webex:
    recipient_type: toPersonId
    recipient_id: "{{ person_id}}"
    msg_type: text
    personal_token: "{{ token }}"
    msg: "Cisco Webex Teams Ansible Module - Text Message to Individual by ID"

- name: Cisco Webex Teams - Text Message by an Individuals E-Mail Address
  community.general.cisco_webex:
    recipient_type: toPersonEmail
    recipient_id: "{{ person_email }}"
    msg_type: text
    personal_token: "{{ token }}"
    msg: "Cisco Webex Teams Ansible Module - Text Message to Individual by E-Mail"
```

## [Return Values](cisco_webex_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **message**  string | The Response Message returned by the Webex Teams API.  Full Response Code explanations can be found at <https://developer.webex.com/docs/api/basics>.  Returned: always  Sample: `"OK (585 bytes)"` |
| **status_code**  integer | The Response Code returned by the Webex Teams API.  Full Response Code explanations can be found at <https://developer.webex.com/docs/api/basics>.  Returned: always  Sample: `200` |

### Authors

- Drew Rusell (@drew-russell)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
