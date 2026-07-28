---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_logging module – Manage logging on network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_logging_module.html
fetched_at: 2026-07-28T02:59:18+00:00
---
# vyos.vyos.vyos_logging module – Manage logging on network devices

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_logging`.

New in vyos.vyos 1.0.0

- [DEPRECATED](vyos_logging_module.md#deprecated)
- [Synopsis](vyos_logging_module.md#synopsis)
- [Parameters](vyos_logging_module.md#parameters)
- [Notes](vyos_logging_module.md#notes)
- [Examples](vyos_logging_module.md#examples)
- [Return Values](vyos_logging_module.md#return-values)
- [Status](vyos_logging_module.md#status)

## [DEPRECATED](vyos_logging_module.md#id1)

Removed in:
:   major release after 2023-08-01

Why:
:   Updated module released with more functionality.

Alternative:
:   vyos_logging_global

## [Synopsis](vyos_logging_module.md#id2)

- This module provides declarative management of logging on Vyatta Vyos devices.

Aliases: logging

## [Parameters](vyos_logging_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of logging definitions. |
| **dest**  string | Destination of the logs.  **Choices:**   - `"console"` - `"file"` - `"global"` - `"host"` - `"user"` |
| **facility**  string | Set logging facility. |
| **level**  string | Set logging severity levels. |
| **name**  string | If value of `dest` is *file* it indicates file-name, for *user* it indicates username and for *host* indicates the host name to be notified. |
| **state**  string | State of the logging configuration.  **Choices:**   - `"present"` - `"absent"` |
| **dest**  string | Destination of the logs.  **Choices:**   - `"console"` - `"file"` - `"global"` - `"host"` - `"user"` |
| **facility**  string | Set logging facility. |
| **level**  string | Set logging severity levels. |
| **name**  string | If value of `dest` is *file* it indicates file-name, for *user* it indicates username and for *host* indicates the host name to be notified. |
| **state**  string | State of the logging configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](vyos_logging_module.md#id4)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_logging_module.md#id5)

```yaml+jinja
- name: configure console logging
  vyos.vyos.vyos_logging:
    dest: console
    facility: all
    level: crit

- name: remove console logging configuration
  vyos.vyos.vyos_logging:
    dest: console
    state: absent

- name: configure file logging
  vyos.vyos.vyos_logging:
    dest: file
    name: test
    facility: local3
    level: err

- name: Add logging aggregate
  vyos.vyos.vyos_logging:
    aggregate:
    - {dest: file, name: test1, facility: all, level: info}
    - {dest: file, name: test2, facility: news, level: debug}
    state: present

- name: Remove logging aggregate
  vyos.vyos.vyos_logging:
    aggregate:
    - {dest: console, facility: all, level: info}
    - {dest: console, facility: daemon, level: warning}
    - {dest: file, name: test2, facility: news, level: debug}
    state: absent
```

## [Return Values](vyos_logging_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["set system syslog global facility all level notice"]` |

## [Status](vyos_logging_module.md#id7)

- This module will be removed in a major release after 2023-08-01.
  *[deprecated]*
- For more information see [DEPRECATED](vyos_logging_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
