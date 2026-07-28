---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_vpc_interface module – Manages interface VPC configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_vpc_interface_module.html
fetched_at: 2026-07-28T01:39:19+00:00
---
# cisco.nxos.nxos_vpc_interface module – Manages interface VPC configuration

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vpc_interface`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vpc_interface_module.md#synopsis)
- [Parameters](nxos_vpc_interface_module.md#parameters)
- [Notes](nxos_vpc_interface_module.md#notes)
- [Examples](nxos_vpc_interface_module.md#examples)
- [Return Values](nxos_vpc_interface_module.md#return-values)

## [Synopsis](nxos_vpc_interface_module.md#id1)

- Manages interface VPC configuration

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: vpc_interface

## [Parameters](nxos_vpc_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **peer_link**  boolean | Set to true/false for peer link config on associated portchannel.  **Choices:**   - `false` - `true` |
| **portchannel**  string / required | Group number of the portchannel that will be configured. |
| **state**  string | Manages desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vpc**  string | VPC group/id that will be configured on associated portchannel. |

## [Notes](nxos_vpc_interface_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - Either vpc or peer_link param is required, but not both.
> - `state=absent` removes whatever VPC config is on a port-channel if one exists.
> - Re-assigning a vpc or peerlink from one portchannel to another is not supported. The module will force the user to unconfigure an existing vpc/pl before configuring the same value on a new portchannel
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vpc_interface_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_vpc_interface:
    portchannel: 10
    vpc: 100
```

## [Return Values](nxos_vpc_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["interface port-channel100", "vpc 10"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
