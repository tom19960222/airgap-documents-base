---
collection: ansible
version: "6"
title: "community.general.jabber module – Send a message to jabber user or chat room"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/jabber_module.html
fetched_at: 2026-07-27T17:10:09+00:00
---
# community.general.jabber module – Send a message to jabber user or chat room

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
> see [Requirements](jabber_module.md#ansible-collections-community-general-jabber-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.jabber`.

- [Synopsis](jabber_module.md#synopsis)
- [Requirements](jabber_module.md#requirements)
- [Parameters](jabber_module.md#parameters)
- [Examples](jabber_module.md#examples)

## [Synopsis](jabber_module.md#id1)

- Send a message to jabber

## [Requirements](jabber_module.md#id2)

The below requirements are needed on the host that executes this module.

- python xmpp (xmpppy)

## [Parameters](jabber_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **encoding**  string | message encoding |
| **host**  string | host to connect, overrides user info |
| **msg**  string / required | The message body. |
| **password**  string / required | password for user to connect |
| **port**  integer | port to connect to, overrides default  Default: `5222` |
| **to**  string / required | user ID or name of the room, when using room use a slash to indicate your nick. |
| **user**  string / required | User as which to connect |

## [Examples](jabber_module.md#id4)

```yaml+jinja
- name: Send a message to a user
  community.general.jabber:
    user: mybot@example.net
    password: secret
    to: friend@example.net
    msg: Ansible task finished

- name: Send a message to a room
  community.general.jabber:
    user: mybot@example.net
    password: secret
    to: mychaps@conference.example.net/ansiblebot
    msg: Ansible task finished

- name: Send a message, specifying the host and port
  community.general.jabber:
    user: mybot@example.net
    host: talk.example.net
    port: 5223
    password: secret
    to: mychaps@example.net
    msg: Ansible task finished
```

### Authors

- Brian Coca (@bcoca)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
