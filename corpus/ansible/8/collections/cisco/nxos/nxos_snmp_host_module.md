---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_snmp_host module – (deprecated, removed after 2024-01-01) Manages SNMP host configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_snmp_host_module.html
fetched_at: 2026-07-28T01:39:09+00:00
---
# cisco.nxos.nxos_snmp_host module – (deprecated, removed after 2024-01-01) Manages SNMP host configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_snmp_host`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_snmp_host_module.md#deprecated)
- [Synopsis](nxos_snmp_host_module.md#synopsis)
- [Parameters](nxos_snmp_host_module.md#parameters)
- [Notes](nxos_snmp_host_module.md#notes)
- [Examples](nxos_snmp_host_module.md#examples)
- [Return Values](nxos_snmp_host_module.md#return-values)
- [Status](nxos_snmp_host_module.md#status)

## [DEPRECATED](nxos_snmp_host_module.md#id1)

Removed in:
:   major release after 2024-01-01

Why:
:   Updated modules released with more functionality

Alternative:
:   nxos_snmp_server

## [Synopsis](nxos_snmp_host_module.md#id2)

- Manages SNMP host configuration parameters.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: snmp_host

## [Parameters](nxos_snmp_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **community**  string | Community string or v3 username. |
| **snmp_host**  string / required | IP address of hostname of target host. |
| **snmp_type**  string | type of message to send to host. If this is not specified, trap type is used.  **Choices:**   - `"trap"` - `"inform"` |
| **src_intf**  string | Source interface. Must be fully qualified interface name. If state = absent, the interface is removed. |
| **state**  string | Manage the state of the resource. If state = present, the host is added to the configuration. If only vrf and/or vrf_filter and/or src_intf are given, they will be added to the existing host configuration. If state = absent, the host is removed if community parameter is given. It is possible to remove only vrf and/or src_int and/or vrf_filter by providing only those parameters and no community parameter.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **udp**  string | UDP port number (0-65535).  **Default:** `"162"` |
| **v3**  string | Use this when verion is v3. SNMPv3 Security level.  **Choices:**   - `"noauth"` - `"auth"` - `"priv"` |
| **version**  string | SNMP version. If this is not specified, v1 is used.  **Choices:**   - `"v1"` - `"v2c"` - `"v3"` |
| **vrf**  string | VRF to use to source traffic to source. If state = absent, the vrf is removed. |
| **vrf_filter**  string | Name of VRF to filter. If state = absent, the vrf is removed from the filter. |

## [Notes](nxos_snmp_host_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Limited Support for Cisco MDS
> - `state=absent` removes the host configuration if it is configured.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_snmp_host_module.md#id5)

```yaml+jinja
# ensure snmp host is configured
- cisco.nxos.nxos_snmp_host:
    snmp_host: 192.0.2.3
    community: TESTING
    state: present
```

## [Return Values](nxos_snmp_host_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["snmp-server host 192.0.2.3 filter-vrf another_test_vrf"]` |

## [Status](nxos_snmp_host_module.md#id7)

- This module will be removed in a major release after 2024-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_snmp_host_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
