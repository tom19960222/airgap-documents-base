---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_logging module – Manage logging on network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_logging_module.html
fetched_at: 2026-07-28T02:39:43+00:00
---
# junipernetworks.junos.junos_logging module – Manage logging on network devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_logging_module.md#ansible-collections-junipernetworks-junos-junos-logging-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_logging`.

New in junipernetworks.junos 1.0.0

- [DEPRECATED](junos_logging_module.md#deprecated)
- [Synopsis](junos_logging_module.md#synopsis)
- [Requirements](junos_logging_module.md#requirements)
- [Parameters](junos_logging_module.md#parameters)
- [Notes](junos_logging_module.md#notes)
- [Examples](junos_logging_module.md#examples)
- [Return Values](junos_logging_module.md#return-values)
- [Status](junos_logging_module.md#status)

## [DEPRECATED](junos_logging_module.md#id1)

Removed in:
:   major release after 2023-08-01

Why:
:   Updated module released with more functionality.

Alternative:
:   junos_logging_global

## [Synopsis](junos_logging_module.md#id2)

- This module provides declarative management of logging on Juniper JUNOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: logging

## [Requirements](junos_logging_module.md#id3)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_logging_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  **Choices:**   - `false` - `true` ← (default) |
| **aggregate**  list / elements=dictionary | List of logging definitions. |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  **Choices:**   - `false` - `true` |
| **dest**  string | Destination of the logs.  **Choices:**   - `"console"` - `"host"` - `"file"` - `"user"` |
| **facility**  string | Set logging facility. |
| **files**  integer | Number of files to be archived, this is applicable if value of *dest* is `file`. The acceptable value is in range from 1 to 1000. |
| **level**  string | Set logging severity levels. |
| **name**  string | If value of `dest` is *file* it indicates file-name, for *user* it indicates username and for *host* indicates the host name to be notified. |
| **rotate_frequency**  integer | Rotate log frequency in minutes, this is applicable if value of *dest* is `file`. The acceptable value is in range of 1 to 59. This controls the frequency after which log file is rotated. |
| **size**  integer | Size of the file in archive, this is applicable if value of *dest* is `file`. The acceptable value is in range from 65536 to 1073741824 bytes. |
| **state**  string | State of the logging configuration.  **Choices:**   - `"present"` - `"absent"` |
| **dest**  string | Destination of the logs.  **Choices:**   - `"console"` - `"host"` - `"file"` - `"user"` |
| **facility**  string | Set logging facility. |
| **files**  integer | Number of files to be archived, this is applicable if value of *dest* is `file`. The acceptable value is in range from 1 to 1000. |
| **level**  string | Set logging severity levels. |
| **name**  string | If value of `dest` is *file* it indicates file-name, for *user* it indicates username and for *host* indicates the host name to be notified. |
| **rotate_frequency**  integer | Rotate log frequency in minutes, this is applicable if value of *dest* is `file`. The acceptable value is in range of 1 to 59. This controls the frequency after which log file is rotated. |
| **size**  integer | Size of the file in archive, this is applicable if value of *dest* is `file`. The acceptable value is in range from 65536 to 1073741824 bytes. |
| **state**  string | State of the logging configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](junos_logging_module.md#id5)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_logging_module.md#id6)

```yaml+jinja
- name: configure console logging
  junipernetworks.junos.junos_logging:
    dest: console
    facility: any
    level: critical

- name: remove console logging configuration
  junipernetworks.junos.junos_logging:
    dest: console
    state: absent

- name: configure file logging
  junipernetworks.junos.junos_logging:
    dest: file
    name: test
    facility: pfe
    level: error

- name: configure logging parameter
  junipernetworks.junos.junos_logging:
    files: 30
    size: 65536
    rotate_frequency: 10

- name: Configure file logging using aggregate
  junipernetworks.junos.junos_logging:
    dest: file
    aggregate:
      - name: test-1
        facility: pfe
        level: critical
      - name: test-2
        facility: kernel
        level: emergency
    active: true

- name: Delete file logging using aggregate
  junipernetworks.junos.junos_logging:
    aggregate:
      - {dest: file, name: test-1, facility: pfe, level: critical}
      - {dest: file, name: test-2, facility: kernel, level: emergency}
    state: absent
```

## [Return Values](junos_logging_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff.prepared**  string | Configuration difference before and after applying change.  **Returned:** when configuration is changed and diff option is enabled.  **Sample:** `"[edit system syslog] +    [edit system syslog]\n     file interactive-commands { ... }\n+    file test { +        pfe critical; +    }\n"` |

## [Status](junos_logging_module.md#id8)

- This module will be removed in a major release after 2023-08-01.
  *[deprecated]*
- For more information see [DEPRECATED](junos_logging_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
