---
collection: ansible
version: "6"
title: "community.general.matrix module – Send notifications to matrix"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/matrix_module.html
fetched_at: 2026-07-27T17:10:52+00:00
---
# community.general.matrix module – Send notifications to matrix

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](matrix_module.md#ansible-collections-community-general-matrix-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.matrix`.

- [Synopsis](matrix_module.md#synopsis)
- [Requirements](matrix_module.md#requirements)
- [Parameters](matrix_module.md#parameters)
- [Examples](matrix_module.md#examples)

## [Synopsis](matrix_module.md#id1)

- This module sends html formatted notifications to matrix rooms.

## [Requirements](matrix_module.md#id2)

The below requirements are needed on the host that executes this module.

- matrix-client (Python library)

## [Parameters](matrix_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hs_url**  string / required | URL of the homeserver, where the CS-API is reachable |
| **msg_html**  string / required | HTML form of the message to send to matrix |
| **msg_plain**  string / required | Plain text form of the message to send to matrix, usually markdown |
| **password**  string | The password to log in with |
| **room_id**  string / required | ID of the room to send the notification to |
| **token**  string | Authentication token for the API call. If provided, user_id and password are not required |
| **user_id**  string | The user id of the user |

## [Examples](matrix_module.md#id4)

```yaml+jinja
- name: Send matrix notification with token
  community.general.matrix:
    msg_plain: "**hello world**"
    msg_html: "<b>hello world</b>"
    room_id: "!12345678:server.tld"
    hs_url: "https://matrix.org"
    token: "{{ matrix_auth_token }}"

- name: Send matrix notification with user_id and password
  community.general.matrix:
    msg_plain: "**hello world**"
    msg_html: "<b>hello world</b>"
    room_id: "!12345678:server.tld"
    hs_url: "https://matrix.org"
    user_id: "ansible_notification_bot"
    password: "{{ matrix_auth_password }}"
```

### Authors

- Jan Christian Grünhage (@jcgruenhage)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
