---
collection: ansible
version: "8"
title: "community.network.cnos_logging module – Manage logging on network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/cnos_logging_module.html
fetched_at: 2026-07-28T01:56:15+00:00
---
# community.network.cnos_logging module – Manage logging on network devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_logging`.

- [Synopsis](cnos_logging_module.md#synopsis)
- [Parameters](cnos_logging_module.md#parameters)
- [Notes](cnos_logging_module.md#notes)
- [Examples](cnos_logging_module.md#examples)
- [Return Values](cnos_logging_module.md#return-values)

## [Synopsis](cnos_logging_module.md#id1)

- This module provides declarative management of logging on Cisco Cnos devices.

Aliases: network.cnos.cnos_logging

## [Parameters](cnos_logging_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of logging definitions. |
| **dest**  string | Destination of the logs. Lenovo uses the term server instead of host in its CLI.  **Choices:**   - `"server"` - `"console"` - `"monitor"` - `"logfile"` |
| **facility**  string | Set logging facility. This is applicable only for server logging |
| **level**  string | Set logging severity levels. 0-emerg;1-alert;2-crit;3-err;4-warn; 5-notif;6-inform;7-debug  **Default:** `5` |
| **name**  string | If value of `dest` is *file* it indicates file-name and for *server* indicates the server name to be notified. |
| **size**  string | Size of buffer. The acceptable value is in range from 4096 to 4294967295 bytes.  **Default:** `10485760` |
| **state**  string | State of the logging configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](cnos_logging_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.9.1

## [Examples](cnos_logging_module.md#id4)

```yaml+jinja
- name: Configure server logging
  community.network.cnos_logging:
    dest: server
    name: 10.241.107.224
    facility: local7
    state: present

- name: Remove server logging configuration
  community.network.cnos_logging:
    dest: server
    name: 10.241.107.224
    state: absent

- name: Configure console logging level and facility
  community.network.cnos_logging:
    dest: console
    level: 7
    state: present

- name: Configure buffer size
  community.network.cnos_logging:
    dest: logfile
    level: 5
    name: testfile
    size: 5000

- name: Configure logging using aggregate
  community.network.cnos_logging:
    aggregate:
      - { dest: console, level: 6 }
      - { dest: logfile, size: 9000 }

- name: Remove logging using aggregate
  community.network.cnos_logging:
    aggregate:
      - { dest: console, level: 6 }
      - { dest: logfile, name: anil, size: 9000 }
    state: absent
```

## [Return Values](cnos_logging_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["logging console 7", "logging server 10.241.107.224"]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
