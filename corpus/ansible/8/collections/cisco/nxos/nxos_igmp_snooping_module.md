---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_igmp_snooping module – Manages IGMP snooping global configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_igmp_snooping_module.html
fetched_at: 2026-07-28T01:38:45+00:00
---
# cisco.nxos.nxos_igmp_snooping module – Manages IGMP snooping global configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_igmp_snooping`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_igmp_snooping_module.md#synopsis)
- [Parameters](nxos_igmp_snooping_module.md#parameters)
- [Notes](nxos_igmp_snooping_module.md#notes)
- [Examples](nxos_igmp_snooping_module.md#examples)
- [Return Values](nxos_igmp_snooping_module.md#return-values)

## [Synopsis](nxos_igmp_snooping_module.md#id1)

- Manages IGMP snooping global configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: igmp_snooping

## [Parameters](nxos_igmp_snooping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **group_timeout**  string | Group membership timeout value for all VLANs on the device. Accepted values are integer in range 1-10080, *never* and *default*. |
| **link_local_grp_supp**  boolean | Global link-local groups suppression.  **Choices:**   - `false` - `true` |
| **report_supp**  boolean | Global IGMPv1/IGMPv2 Report Suppression.  **Choices:**   - `false` - `true` |
| **snooping**  boolean | Enables/disables IGMP snooping on the switch.  **Choices:**   - `false` - `true` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"default"` |
| **v3_report_supp**  boolean | Global IGMPv3 Report Suppression and Proxy Reporting.  **Choices:**   - `false` - `true` |

## [Notes](nxos_igmp_snooping_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - When `state=default`, params will be reset to a default state.
> - `group_timeout` also accepts *never* as an input.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_igmp_snooping_module.md#id4)

```yaml+jinja
# ensure igmp snooping params supported in this module are in there default state
- cisco.nxos.nxos_igmp_snooping:
    state: default

# ensure following igmp snooping params are in the desired state
- cisco.nxos.nxos_igmp_snooping:
    group_timeout: never
    snooping: true
    link_local_grp_supp: false
    optimize_mcast_flood: false
    report_supp: true
    v3_report_supp: true
```

## [Return Values](nxos_igmp_snooping_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["ip igmp snooping link-local-groups-suppression", "ip igmp snooping group-timeout 50", "no ip igmp snooping report-suppression", "no ip igmp snooping v3-report-suppression", "no ip igmp snooping"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
