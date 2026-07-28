---
collection: ansible
version: "6"
title: "community.general.irc module – Send a message to an IRC channel or a nick"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/irc_module.html
fetched_at: 2026-07-27T17:10:06+00:00
---
# community.general.irc module – Send a message to an IRC channel or a nick

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
> see [Requirements](irc_module.md#ansible-collections-community-general-irc-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.irc`.

- [Synopsis](irc_module.md#synopsis)
- [Requirements](irc_module.md#requirements)
- [Parameters](irc_module.md#parameters)
- [Examples](irc_module.md#examples)

## [Synopsis](irc_module.md#id1)

- Send a message to an IRC channel or a nick. This is a very simplistic implementation.

## [Requirements](irc_module.md#id2)

The below requirements are needed on the host that executes this module.

- socket

## [Parameters](irc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **channel**  string | Channel name. One of nick_to or channel needs to be set. When both are set, the message will be sent to both of them. |
| **color**  aliases: colour  string | Text color for the message. (“none” is a valid option in 1.6 or later, in 1.6 and prior, the default color is black, not “none”). Added 11 more colors in version 2.0.  Choices:   - `"none"` ← (default) - `"white"` - `"black"` - `"blue"` - `"green"` - `"red"` - `"brown"` - `"purple"` - `"orange"` - `"yellow"` - `"light_green"` - `"teal"` - `"light_cyan"` - `"light_blue"` - `"pink"` - `"gray"` - `"light_gray"` |
| **key**  string | Channel key |
| **msg**  string / required | The message body. |
| **nick**  string | Nickname to send the message from. May be shortened, depending on server’s NICKLEN setting.  Default: `"ansible"` |
| **nick_to**  list / elements=string | A list of nicknames to send the message to. One of nick_to or channel needs to be set. When both are defined, the message will be sent to both of them. |
| **part**  boolean | Designates whether user should part from channel after sending message or not. Useful for when using a faux bot and not wanting join/parts between messages.  Choices:   - `false` - `true` ← (default) |
| **passwd**  string | Server password |
| **port**  integer | IRC server port number  Default: `6667` |
| **server**  string | IRC server name/address  Default: `"localhost"` |
| **style**  string | Text style for the message. Note italic does not work on some clients  Choices:   - `"bold"` - `"underline"` - `"reverse"` - `"italic"` - `"none"` ← (default) |
| **timeout**  integer | Timeout to use while waiting for successful registration and join messages, this is to prevent an endless loop  Default: `30` |
| **topic**  string | Set the channel topic |
| **use_ssl**  boolean | Designates whether TLS/SSL should be used when connecting to the IRC server  Choices:   - `false` ← (default) - `true` |

## [Examples](irc_module.md#id4)

```yaml+jinja
- name: Send a message to an IRC channel from nick ansible
  community.general.irc:
    server: irc.example.net
    channel: #t1
    msg: Hello world

- name: Send a message to an IRC channel
  local_action:
    module: irc
    port: 6669
    server: irc.example.net
    channel: #t1
    msg: 'All finished at {{ ansible_date_time.iso8601 }}'
    color: red
    nick: ansibleIRC

- name: Send a message to an IRC channel
  local_action:
    module: irc
    port: 6669
    server: irc.example.net
    channel: #t1
    nick_to:
      - nick1
      - nick2
    msg: 'All finished at {{ ansible_date_time.iso8601 }}'
    color: red
    nick: ansibleIRC
```

### Authors

- Jan-Piet Mens (@jpmens)
- Matt Martz (@sivel)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
