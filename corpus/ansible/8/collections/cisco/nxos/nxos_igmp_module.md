---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_igmp module – Manages IGMP global configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_igmp_module.html
fetched_at: 2026-07-28T01:38:43+00:00
---
# cisco.nxos.nxos_igmp module – Manages IGMP global configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_igmp`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_igmp_module.md#synopsis)
- [Parameters](nxos_igmp_module.md#parameters)
- [Notes](nxos_igmp_module.md#notes)
- [Examples](nxos_igmp_module.md#examples)
- [Return Values](nxos_igmp_module.md#return-values)

## [Synopsis](nxos_igmp_module.md#id1)

- Manages IGMP global configuration configuration settings.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: igmp

## [Parameters](nxos_igmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **enforce_rtr_alert**  boolean | Enables or disables the enforce router alert option check for IGMPv2 and IGMPv3 packets.  **Choices:**   - `false` - `true` |
| **flush_routes**  boolean | Removes routes when the IGMP process is restarted. By default, routes are not flushed.  **Choices:**   - `false` - `true` |
| **restart**  boolean | Restarts the igmp process (using an exec config command).  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Manages desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"default"` |

## [Notes](nxos_igmp_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - When `state=default`, all supported params will be reset to a default state.
> - If restart is set to true with other params set, the restart will happen last, i.e. after the configuration takes place.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_igmp_module.md#id4)

```yaml+jinja
- name: Default igmp global params (all params except restart)
  cisco.nxos.nxos_igmp:
    state: default

- name: Ensure the following igmp global config exists on the device
  cisco.nxos.nxos_igmp:
    flush_routes: true
    enforce_rtr_alert: true

- name: Restart the igmp process
  cisco.nxos.nxos_igmp:
    restart: true
```

## [Return Values](nxos_igmp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["ip igmp flush-routes"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
