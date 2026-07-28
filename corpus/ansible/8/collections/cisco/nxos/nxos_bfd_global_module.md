---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_bfd_global module – Bidirectional Forwarding Detection (BFD) global-level configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_bfd_global_module.html
fetched_at: 2026-07-28T01:38:29+00:00
---
# cisco.nxos.nxos_bfd_global module – Bidirectional Forwarding Detection (BFD) global-level configuration

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_bfd_global`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_bfd_global_module.md#synopsis)
- [Parameters](nxos_bfd_global_module.md#parameters)
- [Notes](nxos_bfd_global_module.md#notes)
- [Examples](nxos_bfd_global_module.md#examples)
- [Return Values](nxos_bfd_global_module.md#return-values)

## [Synopsis](nxos_bfd_global_module.md#id1)

- Manages Bidirectional Forwarding Detection (BFD) global-level configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: bfd_global

## [Parameters](nxos_bfd_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **echo_interface**  string | Loopback interface used for echo frames.  Valid values are loopback interface name or ‘deleted’.  Not supported on N5K/N6K |
| **echo_rx_interval**  integer | BFD Echo receive interval in milliseconds. |
| **fabricpath_interval**  dictionary | BFD fabricpath interval timer values.  Value must be a dict defining values for keys (tx, min_rx, and multiplier). |
| **fabricpath_slow_timer**  integer | BFD fabricpath slow rate timer in milliseconds. |
| **fabricpath_vlan**  integer | BFD fabricpath control vlan. |
| **interval**  dictionary | BFD interval timer values.  Value must be a dict defining values for keys (tx, min_rx, and multiplier) |
| **ipv4_echo_rx_interval**  integer | BFD IPv4 session echo receive interval in milliseconds. |
| **ipv4_interval**  dictionary | BFD IPv4 interval timer values.  Value must be a dict defining values for keys (tx, min_rx, and multiplier). |
| **ipv4_slow_timer**  integer | BFD IPv4 slow rate timer in milliseconds. |
| **ipv6_echo_rx_interval**  integer | BFD IPv6 session echo receive interval in milliseconds. |
| **ipv6_interval**  dictionary | BFD IPv6 interval timer values.  Value must be a dict defining values for keys (tx, min_rx, and multiplier). |
| **ipv6_slow_timer**  integer | BFD IPv6 slow rate timer in milliseconds. |
| **slow_timer**  integer | BFD slow rate timer in milliseconds. |
| **startup_timer**  integer | BFD delayed startup timer in seconds.  Not supported on N5K/N6K/N7K |

## [Notes](nxos_bfd_global_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 9.2(2)
> - Unsupported for Cisco MDS
> - BFD global will automatically enable ‘feature bfd’ if it is disabled.
> - BFD global does not have a ‘state’ parameter. All of the BFD commands are unique and are defined if ‘feature bfd’ is enabled.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_bfd_global_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_bfd_global:
    echo_interface: Ethernet1/2
    echo_rx_interval: 50
    interval:
      tx: 50
      min_rx: 50
      multiplier: 4
```

## [Return Values](nxos_bfd_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmds**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["bfd echo-interface loopback1", "bfd slow-timer 2000"]` |

### Authors

- Chris Van Heuveln (@chrisvanheuveln)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
