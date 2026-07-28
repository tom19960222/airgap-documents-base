---
collection: ansible
version: "8"
title: "community.general.flowdock module – Send a message to a flowdock"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/flowdock_module.html
fetched_at: 2026-07-28T01:45:35+00:00
---
# community.general.flowdock module – Send a message to a flowdock

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
> To use it in a playbook, specify: `community.general.flowdock`.

- [DEPRECATED](flowdock_module.md#deprecated)
- [Synopsis](flowdock_module.md#synopsis)
- [Parameters](flowdock_module.md#parameters)
- [Attributes](flowdock_module.md#attributes)
- [Examples](flowdock_module.md#examples)
- [Status](flowdock_module.md#status)

## [DEPRECATED](flowdock_module.md#id1)

Removed in:
:   version 9.0.0

Why:
:   the endpoints this module relies on do not exist any more and do not resolve to IPs in DNS.

Alternative:
:   no known alternative at this point

## [Synopsis](flowdock_module.md#id2)

- Send a message to a flowdock team inbox or chat using the push API (see <https://www.flowdock.com/api/team-inbox> and <https://www.flowdock.com/api/chat>)

Aliases: notification.flowdock

## [Parameters](flowdock_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **external_user_name**  string | (chat only - required) Name of the “user” sending the message |
| **from_address**  string | (inbox only - required) Email address of the message sender |
| **from_name**  string | (inbox only) Name of the message sender |
| **link**  string | (inbox only) Link associated with the message. This will be used to link the message subject in Team Inbox. |
| **msg**  string / required | Content of the message |
| **project**  string | (inbox only) Human readable identifier for more detailed message categorization |
| **reply_to**  string | (inbox only) Email address for replies |
| **source**  string | (inbox only - required) Human readable identifier of the application that uses the Flowdock API |
| **subject**  string | (inbox only - required) Subject line of the message |
| **tags**  string | tags of the message, separated by commas |
| **token**  string / required | API token. |
| **type**  string / required | Whether to post to ‘inbox’ or ‘chat’  **Choices:**   - `"inbox"` - `"chat"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](flowdock_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](flowdock_module.md#id5)

```yaml+jinja
- name: Send a message to a flowdock
  community.general.flowdock:
    type: inbox
    token: AAAAAA
    from_address: user@example.com
    source: my cool app
    msg: test from ansible
    subject: test subject

- name: Send a message to a flowdock
  community.general.flowdock:
    type: chat
    token: AAAAAA
    external_user_name: testuser
    msg: test from ansible
    tags: tag1,tag2,tag3
```

## [Status](flowdock_module.md#id6)

- This module will be removed in version 9.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](flowdock_module.md#deprecated).

### Authors

- Matt Coddington (@mcodd)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
