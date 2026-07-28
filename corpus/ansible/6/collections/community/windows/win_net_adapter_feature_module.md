---
collection: ansible
version: "6"
title: "community.windows.win_net_adapter_feature module – Enable or disable certain network adapters."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_net_adapter_feature_module.html
fetched_at: 2026-07-27T17:23:37+00:00
---
# community.windows.win_net_adapter_feature module – Enable or disable certain network adapters.

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_net_adapter_feature`.

New in community.windows 1.2.0

- [Synopsis](win_net_adapter_feature_module.md#synopsis)
- [Parameters](win_net_adapter_feature_module.md#parameters)
- [Examples](win_net_adapter_feature_module.md#examples)

## [Synopsis](win_net_adapter_feature_module.md#id1)

- Enable or disable some network components of a certain network adapter or all the network adapters.

## [Parameters](win_net_adapter_feature_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **component_id**  list / elements=string / required | Specify the below component_id of network adapters.  component_id (DisplayName)  `ms_implat` (Microsoft Network Adapter Multiplexor Protocol)  `ms_lltdio` (Link-Layer Topology Discovery Mapper I/O Driver)  `ms_tcpip6` (Internet Protocol Version 6 (TCP/IPv6))  `ms_tcpip` (Internet Protocol Version 4 (TCP/IPv4))  `ms_lldp` (Microsoft LLDP Protocol Driver)  `ms_rspndr` (Link-Layer Topology Discovery Responder)  `ms_msclient` (Client for Microsoft Networks)  `ms_pacer` (QoS Packet Scheduler)  If you’d like to set custom adapters like ‘Juniper Network Service’, get the *component_id* by running the `Get-NetAdapterBinding` cmdlet. |
| **interface**  list / elements=string / required | Name of Network Adapter Interface. For example, `Ethernet0` or `*`. |
| **state**  string | Specify the state of ms_tcpip6 of interfaces.  Choices:   - `"enabled"` ← (default) - `"disabled"` |

## [Examples](win_net_adapter_feature_module.md#id3)

```yaml+jinja
- name: enable multiple interfaces of multiple interfaces
  community.windows.win_net_adapter_feature:
    interface:
    - 'Ethernet0'
    - 'Ethernet1'
    state: enabled
    component_id:
    - ms_tcpip6
    - ms_server

- name: Enable ms_tcpip6 of all the Interface
  community.windows.win_net_adapter_feature:
    interface: '*'
    state: enabled
    component_id:
    - ms_tcpip6
```

### Authors

- ライトウェルの人 (@jirolin)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
