---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_syslog_remote module – Configure remote syslog module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_syslog_remote_module.html
fetched_at: 2026-07-27T17:55:42+00:00
---
# mellanox.onyx.onyx_syslog_remote module – Configure remote syslog module

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_syslog_remote`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_syslog_remote_module.md#synopsis)
- [Parameters](onyx_syslog_remote_module.md#parameters)
- [Examples](onyx_syslog_remote_module.md#examples)
- [Return Values](onyx_syslog_remote_module.md#return-values)

## [Synopsis](onyx_syslog_remote_module.md#id1)

- This module provides declarative management of syslog on Mellanox ONYX network devices.

## [Parameters](onyx_syslog_remote_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Disable/Enable logging to given remote host  Choices:   - `false` - `true` ← (default) |
| **filter**  string | Specify a filter type  Choices:   - `"include"` - `"exclude"` |
| **filter_str**  string | Specify a regex filter string |
| **host**  string / required | <IP4/IP6 Hostname> Send event logs to this server using the syslog protocol |
| **port**  integer | Set remote server destination port for log messages |
| **trap**  string | Minimum severity level for messages to this syslog server  Choices:   - `"none"` - `"debug"` - `"info"` - `"notice"` - `"alert"` - `"warning"` - `"err"` - `"emerg"` - `"crit"` |
| **trap_override**  list / elements=string | Override log levels for this sink on a per-class basis |
| **override_class**  string / required | Specify a class whose log level to override  Choices:   - `"mgmt-front"` - `"mgmt-back"` - `"mgmt-core"` - `"events"` - `"debug-module"` - `"sx-sdk"` - `"mlx-daemons"` - `"protocol-stack"` |
| **override_enabled**  boolean | disable override priorities for specific class.  Choices:   - `false` - `true` ← (default) |
| **override_priority**  string | -Specify a priority whose log level to override  Choices:   - `"none"` - `"debug"` - `"info"` - `"notice"` - `"alert"` - `"warning"` - `"err"` - `"emerg"` - `"crit"` |

## [Examples](onyx_syslog_remote_module.md#id3)

```yaml+jinja
- name: Remote logging port 8080
- onyx_syslog_remote:
    host: 10.10.10.10
    port: 8080

- name: Remote logging trap override
- onyx_syslog_remote:
    host: 10.10.10.10
    trap_override:
        - override_class: events
          override_priority: emerg

- name: Remote logging trap emerg
- onyx_syslog_remote:
    host: 10.10.10.10
    trap: emerg

- name: Remote logging filter include 'ERR'
- onyx_syslog_remote:
    host: 10.10.10.10
    filter: include
    filter_str: /ERR/

- name: Disable remote logging with class events
- onyx_syslog_remote:
    enabled: False
    host: 10.10.10.10
    class: events
- name : disable remote logging
- onyx_syslog_remote:
    enabled: False
    host: 10.10.10.10

- name : enable/disable override class
- onyx_syslog_remote:
    host: 10.7.144.71
    trap_override:
        - override_class: events
          override_priority: emerg
          override_enabled: False
        - override_class: mgmt-front
          override_priority: alert
```

## [Return Values](onyx_syslog_remote_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["logging x port 8080", "logging 10.10.10.10 trap override class events priority emerg", "no logging 10.10.10.10 trap override class events", "logging 10.10.10.10 trap emerg", "logging 10.10.10.10 filter [include | exclude] ERR"]` |

### Authors

- Anas Shami (@anass)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
