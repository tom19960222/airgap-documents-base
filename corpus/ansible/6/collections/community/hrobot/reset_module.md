---
collection: ansible
version: "6"
title: "community.hrobot.reset module – Reset a dedicated server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/reset_module.html
fetched_at: 2026-07-27T17:15:53+00:00
---
# community.hrobot.reset module – Reset a dedicated server

> **Note:**
>
> This module is part of the [community.hrobot collection](https://galaxy.ansible.com/community/hrobot) (version 1.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hrobot`.
>
> To use it in a playbook, specify: `community.hrobot.reset`.

New in community.hrobot 1.2.0

- [Synopsis](reset_module.md#synopsis)
- [Parameters](reset_module.md#parameters)
- [Attributes](reset_module.md#attributes)
- [Examples](reset_module.md#examples)

## [Synopsis](reset_module.md#id1)

- Reset a dedicated server with a software or hardware reset, or by requesting a manual reset.

## [Parameters](reset_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **reset_type**  string / required | How to reset the server.  `software` is a software reset. This should be similar to pressing Ctrl+Alt+Del on the keyboard.  `power` is a hardware reset similar to pressing the Power button. An ACPI signal is sent, and if the server is configured correctly, this will trigger a regular shutdown.  `hardware` is a hardware reset similar to pressing the Restart button. The power is cycled for the server.  `manual` is a manual reset. This requests a technician to manually do the shutdown while looking at the screen output. **Be careful** and only use this when really necessary!  Note that not every server supports every reset method!  Choices:   - `"software"` - `"hardware"` - `"power"` - `"manual"` |
| **server_number**  integer / required | The server number of the server to reset. |

## [Attributes](reset_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](reset_module.md#id4)

```yaml+jinja
- name: Send ACPI signal to server to request controlled shutdown
  community.hrobot.reset:
    hetzner_user: foo
    hetzner_password: bar
    failover_ip: 1.2.3.4
    state: power

- name: Make sure that the server supports manual reset
  community.hrobot.reset:
    hetzner_user: foo
    hetzner_password: bar
    server_number: 1234
    reset_type: manual
  check_mode: true

- name: Request a manual reset (by a technican)
  community.hrobot.reset:
    hetzner_user: foo
    hetzner_password: bar
    server_number: 1234
    reset_type: manual
```

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
