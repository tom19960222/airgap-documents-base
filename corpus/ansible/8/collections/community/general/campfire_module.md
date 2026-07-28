---
collection: ansible
version: "8"
title: "community.general.campfire module – Send a message to Campfire"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/campfire_module.html
fetched_at: 2026-07-28T01:44:55+00:00
---
# community.general.campfire module – Send a message to Campfire

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
> To use it in a playbook, specify: `community.general.campfire`.

- [Synopsis](campfire_module.md#synopsis)
- [Parameters](campfire_module.md#parameters)
- [Attributes](campfire_module.md#attributes)
- [Examples](campfire_module.md#examples)

## [Synopsis](campfire_module.md#id1)

- Send a message to Campfire.
- Messages with newlines will result in a “Paste” message being sent.

Aliases: notification.campfire

## [Parameters](campfire_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **msg**  string / required | The message body. |
| **notify**  string | Send a notification sound before the message.  **Choices:**   - `"56k"` - `"bell"` - `"bezos"` - `"bueller"` - `"clowntown"` - `"cottoneyejoe"` - `"crickets"` - `"dadgummit"` - `"dangerzone"` - `"danielsan"` - `"deeper"` - `"drama"` - `"greatjob"` - `"greyjoy"` - `"guarantee"` - `"heygirl"` - `"horn"` - `"horror"` - `"inconceivable"` - `"live"` - `"loggins"` - `"makeitso"` - `"noooo"` - `"nyan"` - `"ohmy"` - `"ohyeah"` - `"pushit"` - `"rimshot"` - `"rollout"` - `"rumble"` - `"sax"` - `"secret"` - `"sexyback"` - `"story"` - `"tada"` - `"tmyk"` - `"trololo"` - `"trombone"` - `"unix"` - `"vuvuzela"` - `"what"` - `"whoomp"` - `"yeah"` - `"yodel"` |
| **room**  string / required | Room number to which the message should be sent. |
| **subscription**  string / required | The subscription name to use. |
| **token**  string / required | API token. |

## [Attributes](campfire_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](campfire_module.md#id4)

```yaml+jinja
- name: Send a message to Campfire
  community.general.campfire:
    subscription: foo
    token: 12345
    room: 123
    msg: Task completed.

- name: Send a message to Campfire
  community.general.campfire:
    subscription: foo
    token: 12345
    room: 123
    notify: loggins
    msg: Task completed ... with feeling.
```

### Authors

- Adam Garside (@fabulops)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
