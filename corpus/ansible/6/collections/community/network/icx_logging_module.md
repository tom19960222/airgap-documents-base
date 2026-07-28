---
collection: ansible
version: "6"
title: "community.network.icx_logging module – Manage logging on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/icx_logging_module.html
fetched_at: 2026-07-27T17:18:46+00:00
---
# community.network.icx_logging module – Manage logging on Ruckus ICX 7000 series switches

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.icx_logging`.

- [Synopsis](icx_logging_module.md#synopsis)
- [Parameters](icx_logging_module.md#parameters)
- [Notes](icx_logging_module.md#notes)
- [Examples](icx_logging_module.md#examples)
- [Return Values](icx_logging_module.md#return-values)

## [Synopsis](icx_logging_module.md#id1)

- This module provides declarative management of logging on Ruckus ICX 7000 series switches.

## [Parameters](icx_logging_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=string | List of logging definitions. |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  Choices:   - `false` - `true` |
| **dest**  string | Destination of the logs.  Choices:   - `"on"` - `"host"` - `"console"` - `"buffered"` - `"persistence"` - `"rfc5424"` |
| **facility**  string | Specifies log facility to log messages from the device.  Choices:   - `"auth"` - `"cron"` - `"daemon"` - `"kern"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` - `"user"` - `"lpr"` - `"mail"` - `"news"` - `"syslog"` - `"sys9"` - `"sys10"` - `"sys11"` - `"sys12"` - `"sys13"` - `"sys14"` - `"user"` - `"uucp"` |
| **level**  list / elements=string | Specifies the message level.  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **name**  string | ipv4 address/ipv6 address/name of syslog server. |
| **state**  string | State of the logging configuration.  Choices:   - `"present"` - `"absent"` |
| **udp_port**  string | UDP port of destination host(syslog server). |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  Choices:   - `false` - `true` ← (default) |
| **dest**  string | Destination of the logs.  Choices:   - `"on"` - `"host"` - `"console"` - `"buffered"` - `"persistence"` - `"rfc5424"` |
| **facility**  string | Specifies log facility to log messages from the device.  Choices:   - `"auth"` - `"cron"` - `"daemon"` - `"kern"` - `"local0"` - `"local1"` - `"local2"` - `"local3"` - `"local4"` - `"local5"` - `"local6"` - `"local7"` - `"user"` - `"lpr"` - `"mail"` - `"news"` - `"syslog"` - `"sys9"` - `"sys10"` - `"sys11"` - `"sys12"` - `"sys13"` - `"sys14"` - `"user"` - `"uucp"` |
| **level**  list / elements=string | Specifies the message level.  Choices:   - `"alerts"` - `"critical"` - `"debugging"` - `"emergencies"` - `"errors"` - `"informational"` - `"notifications"` - `"warnings"` |
| **name**  string | ipv4 address/ipv6 address/name of syslog server. |
| **state**  string | State of the logging configuration.  Choices:   - `"present"` ← (default) - `"absent"` |
| **udp_port**  string | UDP port of destination host(syslog server). |

## [Notes](icx_logging_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_logging_module.md#id4)

```yaml+jinja
- name: Configure host logging.
  community.network.icx_logging:
    dest: host
    name: 172.16.0.1
    udp_port: 5555
- name: Remove host logging configuration.
  community.network.icx_logging:
    dest: host
    name: 172.16.0.1
    udp_port: 5555
    state: absent
- name: Disables the real-time display of syslog messages.
  community.network.icx_logging:
    dest: console
    state: absent
- name: Enables local syslog logging.
  community.network.icx_logging:
    dest : on
    state: present
- name: Configure buffer level
  community.network.icx_logging:
    dest: buffered
    level: critical
- name: Configure logging using aggregate
  community.network.icx_logging:
    aggregate:
      - { dest: buffered, level: ['notifications','errors'] }
- name: Remove logging using aggregate
  community.network.icx_logging:
    aggregate:
      - { dest: console }
      - { dest: host, name: 172.16.0.1, udp_port: 5555 }
    state: absent
```

## [Return Values](icx_logging_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["logging host 172.16.0.1", "logging console"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
