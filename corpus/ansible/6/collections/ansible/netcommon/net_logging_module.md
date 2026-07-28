---
collection: ansible
version: "6"
title: "ansible.netcommon.net_logging module – (deprecated, removed after 2022-06-01) Manage logging on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_logging_module.html
fetched_at: 2026-07-27T16:44:31+00:00
---
# ansible.netcommon.net_logging module – (deprecated, removed after 2022-06-01) Manage logging on network devices

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_logging`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_logging_module.md#deprecated)
- [Synopsis](net_logging_module.md#synopsis)
- [Parameters](net_logging_module.md#parameters)
- [Notes](net_logging_module.md#notes)
- [Examples](net_logging_module.md#examples)
- [Return Values](net_logging_module.md#return-values)
- [Status](net_logging_module.md#status)

## [DEPRECATED](net_logging_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_logging” module

## [Synopsis](net_logging_module.md#id2)

- This module provides declarative management of logging on network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_logging_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of logging definitions. |
| **dest**  string | Destination of the logs.  Choices:   - `"console"` - `"host"` |
| **facility**  string | Set logging facility. |
| **level**  string | Set logging severity levels. |
| **name**  string | If value of `dest` is *host* it indicates file-name the host name to be notified. |
| **purge**  string | Purge logging not defined in the *aggregate* parameter.  Default: `false` |
| **state**  string | State of the logging configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](net_logging_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_logging_module.md#id5)

```yaml+jinja
- name: configure console logging
  ansible.netcommon.net_logging:
    dest: console
    facility: any
    level: critical

- name: remove console logging configuration
  ansible.netcommon.net_logging:
    dest: console
    state: absent

- name: configure host logging
  ansible.netcommon.net_logging:
    dest: host
    name: 192.0.2.1
    facility: kernel
    level: critical

- name: Configure file logging using aggregate
  ansible.netcommon.net_logging:
    dest: file
    aggregate:
    - name: test-1
      facility: pfe
      level: critical
    - name: test-2
      facility: kernel
      level: emergency
- name: Delete file logging using aggregate
  ansible.netcommon.net_logging:
    dest: file
    aggregate:
    - name: test-1
      facility: pfe
      level: critical
    - name: test-2
      facility: kernel
      level: emergency
    state: absent
```

## [Return Values](net_logging_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["logging console critical"]` |

## [Status](net_logging_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_logging_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
