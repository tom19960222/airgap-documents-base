---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_snmp_traps module – (deprecated, removed after 2024-01-01) Manages SNMP traps."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_snmp_traps_module.html
fetched_at: 2026-07-28T01:39:12+00:00
---
# cisco.nxos.nxos_snmp_traps module – (deprecated, removed after 2024-01-01) Manages SNMP traps.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_snmp_traps`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_snmp_traps_module.md#deprecated)
- [Synopsis](nxos_snmp_traps_module.md#synopsis)
- [Parameters](nxos_snmp_traps_module.md#parameters)
- [Notes](nxos_snmp_traps_module.md#notes)
- [Examples](nxos_snmp_traps_module.md#examples)
- [Return Values](nxos_snmp_traps_module.md#return-values)
- [Status](nxos_snmp_traps_module.md#status)

## [DEPRECATED](nxos_snmp_traps_module.md#id1)

Removed in:
:   major release after 2024-01-01

Why:
:   Updated modules released with more functionality

Alternative:
:   nxos_snmp_server

## [Synopsis](nxos_snmp_traps_module.md#id2)

- Manages SNMP traps configurations.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: snmp_traps

## [Parameters](nxos_snmp_traps_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **group**  string / required | Case sensitive group.  **Choices:**   - `"aaa"` - `"bfd"` - `"bgp"` - `"bridge"` - `"callhome"` - `"cfs"` - `"config"` - `"eigrp"` - `"entity"` - `"feature-control"` - `"generic"` - `"hsrp"` - `"license"` - `"link"` - `"lldp"` - `"mmode"` - `"ospf"` - `"pim"` - `"rf"` - `"rmon"` - `"snmp"` - `"storm-control"` - `"stpx"` - `"switchfabric"` - `"syslog"` - `"sysmgr"` - `"system"` - `"upgrade"` - `"vtp"` - `"all"` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` |

## [Notes](nxos_snmp_traps_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Limited Support for Cisco MDS
> - This module works at the group level for traps. If you need to only enable/disable 1 specific trap within a group, use the [cisco.nxos.nxos_command](nxos_command_module.md#ansible-collections-cisco-nxos-nxos-command-module) module.
> - Be aware that you can set a trap only for an enabled feature.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_snmp_traps_module.md#id5)

```yaml+jinja
# ensure lldp trap configured
- cisco.nxos.nxos_snmp_traps:
    group: lldp
    state: enabled

# ensure lldp trap is not configured
- cisco.nxos.nxos_snmp_traps:
    group: lldp
    state: disabled
```

## [Return Values](nxos_snmp_traps_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["snmp-server enable traps lldp ;"]` |

## [Status](nxos_snmp_traps_module.md#id7)

- This module will be removed in a major release after 2024-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_snmp_traps_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
