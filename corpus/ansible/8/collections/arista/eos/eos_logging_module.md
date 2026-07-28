---
collection: ansible
version: "8"
title: "arista.eos.eos_logging module – Manage logging on network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_logging_module.html
fetched_at: 2026-07-28T01:11:08+00:00
---
# arista.eos.eos_logging module – Manage logging on network devices

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_logging`.

New in arista.eos 1.0.0

- [DEPRECATED](eos_logging_module.md#deprecated)
- [Synopsis](eos_logging_module.md#synopsis)
- [Parameters](eos_logging_module.md#parameters)
- [Notes](eos_logging_module.md#notes)
- [Examples](eos_logging_module.md#examples)
- [Return Values](eos_logging_module.md#return-values)
- [Status](eos_logging_module.md#status)

## [DEPRECATED](eos_logging_module.md#id1)

Removed in:
:   major release after 2024-01-01

Why:
:   Updated module released with more functionality.

Alternative:
:   eos_logging_global

## [Synopsis](eos_logging_module.md#id2)

- This module provides declarative management of logging on Arista Eos devices.

Aliases: logging

## [Parameters](eos_logging_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of logging definitions. |
| **dest**  string | Destination of the logs.  **Choices:**   - `"on"` - `"host"` - `"console"` - `"monitor"` - `"buffered"` |
| **facility**  string | Set logging facility. |
| **level**  string | Set logging severity levels.  **Choices:**   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warnings"` - `"notifications"` - `"informational"` - `"debugging"` |
| **name**  string | The hostname or IP address of the destination.  Required when *dest=host*. |
| **size**  integer | Size of buffer. The acceptable value is in range from 10 to 2147483647 bytes. |
| **state**  string | State of the logging configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **dest**  string | Destination of the logs.  **Choices:**   - `"on"` - `"host"` - `"console"` - `"monitor"` - `"buffered"` |
| **facility**  string | Set logging facility. |
| **level**  string | Set logging severity levels.  **Choices:**   - `"emergencies"` - `"alerts"` - `"critical"` - `"errors"` - `"warnings"` - `"notifications"` - `"informational"` - `"debugging"` |
| **name**  string | The hostname or IP address of the destination.  Required when *dest=host*. |
| **size**  integer | Size of buffer. The acceptable value is in range from 10 to 2147483647 bytes. |
| **state**  string | State of the logging configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](eos_logging_module.md#id4)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F

## [Examples](eos_logging_module.md#id5)

```yaml+jinja
- name: configure host logging
  arista.eos.eos_logging:
    dest: host
    name: 172.16.0.1
    state: present

- name: remove host logging configuration
  arista.eos.eos_logging:
    dest: host
    name: 172.16.0.1
    state: absent

- name: configure console logging level and facility
  arista.eos.eos_logging:
    dest: console
    facility: local7
    level: debugging
    state: present

- name: enable logging to all
  arista.eos.eos_logging:
    dest: on

- name: configure buffer size
  arista.eos.eos_logging:
    dest: buffered
    size: 5000

- name: Configure logging using aggregate
  arista.eos.eos_logging:
    aggregate:
      - {dest: console, level: warnings}
      - {dest: buffered, size: 480000}
    state: present
```

## [Return Values](eos_logging_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["logging facility local7", "logging host 172.16.0.1"]` |

## [Status](eos_logging_module.md#id7)

- This module will be removed in a major release after 2024-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](eos_logging_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
