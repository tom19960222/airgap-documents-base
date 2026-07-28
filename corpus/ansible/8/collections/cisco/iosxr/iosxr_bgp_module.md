---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_bgp module – Module to configure BGP protocol settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_bgp_module.html
fetched_at: 2026-07-28T01:26:35+00:00
---
# cisco.iosxr.iosxr_bgp module – Module to configure BGP protocol settings.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_bgp`.

New in cisco.iosxr 1.0.0

- [DEPRECATED](iosxr_bgp_module.md#deprecated)
- [Synopsis](iosxr_bgp_module.md#synopsis)
- [Parameters](iosxr_bgp_module.md#parameters)
- [Notes](iosxr_bgp_module.md#notes)
- [Examples](iosxr_bgp_module.md#examples)
- [Return Values](iosxr_bgp_module.md#return-values)
- [Status](iosxr_bgp_module.md#status)

## [DEPRECATED](iosxr_bgp_module.md#id1)

Removed in:
:   major release after 2023-01-29

Why:
:   Updated module released with more functionality.

Alternative:
:   iosxr_bgp_global

## [Synopsis](iosxr_bgp_module.md#id2)

- This module provides configuration management of global BGP parameters on devices running Cisco IOS-XR

Aliases: bgp

## [Parameters](iosxr_bgp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies the BGP related configuration. |
| **address_family**  list / elements=dictionary | Specifies BGP address family related configurations. |
| **afi**  string / required | Type of address family to configure.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **networks**  list / elements=dictionary | Specify networks to announce via BGP.  For operation replace, this option is mutually exclusive with root level networks option. |
| **masklen**  integer / required | Subnet mask length for the network to announce(e.g, 8, 16, 24, etc.). |
| **network**  aliases: prefix  string / required | Network ID to announce via BGP. |
| **route_map**  string | Route map to modify the attributes. |
| **redistribute**  list / elements=dictionary | Specifies the redistribute information from another routing protocol. |
| **id**  string | Identifier for the routing protocol for configuring redistribute information.  Valid for protocols ‘ospf’, ‘eigrp’, ‘isis’ and ‘ospfv3’. |
| **metric**  integer | Specifies the metric for redistributed routes. |
| **protocol**  string / required | Specifies the protocol for configuring redistribute information.  **Choices:**   - `"ospf"` - `"ospfv3"` - `"eigrp"` - `"isis"` - `"static"` - `"connected"` - `"lisp"` - `"mobile"` - `"rip"` - `"subscriber"` |
| **route_map**  string | Specifies the route map reference. |
| **safi**  string | Specifies the type of cast for the address family.  **Choices:**   - `"flowspec"` - `"unicast"` ← (default) - `"multicast"` - `"labeled-unicast"` |
| **bgp_as**  integer / required | Specifies the BGP Autonomous System (AS) number to configure on the device. |
| **log_neighbor_changes**  boolean | Enable/disable logging neighbor up/down and reset reason.  **Choices:**   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor related configurations. |
| **advertisement_interval**  integer | Specifies the minimum interval (in seconds) between sending BGP routing updates.  The range is from 0 to 600. |
| **description**  string | Neighbor specific description. |
| **ebgp_multihop**  integer | Specifies the maximum hop count for EBGP neighbors not on directly connected networks.  The range is from 0 to 255. |
| **enabled**  boolean | Administratively shutdown or enable a neighbor.  **Choices:**   - `false` - `true` |
| **neighbor**  string / required | Neighbor router address. |
| **password**  string | Password to authenticate the BGP peer connection. |
| **remote_as**  integer / required | Remote AS of the BGP neighbor to configure. |
| **tcp_mss**  integer | Specifies the TCP initial maximum segment size to use.  The range is from 68 to 10000. |
| **timers**  dictionary | Specifies BGP neighbor timer related configurations. |
| **holdtime**  integer | Interval after not receiving a keepalive message that the software declares a peer dead.  The range is from 3 to 65535. |
| **keepalive**  integer | Frequency with which the Cisco IOS-XR software sends keepalive messages to its peer.  The range is from 0 to 65535. |
| **min_neighbor_holdtime**  integer | Interval specifying the minimum acceptable hold-time from a BGP neighbor.  The minimum acceptable hold-time must be less than, or equal to, the interval specified in the holdtime argument.  The range is from 3 to 65535. |
| **update_source**  string | Source of the routing updates. |
| **router_id**  string | Configures the BGP routing process router-id value. |
| **operation**  string | Specifies the operation to be performed on the BGP process configured on the device.  In case of merge, the input configuration will be merged with the existing BGP configuration on the device.  In case of replace, if there is a diff between the existing configuration and the input configuration, the existing configuration will be replaced by the input configuration for every option that has the diff.  In case of override, all the existing BGP configuration will be removed from the device and replaced with the input configuration.  In case of delete the existing BGP configuration will be removed from the device.  **Choices:**   - `"merge"` ← (default) - `"replace"` - `"override"` - `"delete"` |

## [Notes](iosxr_bgp_module.md#id4)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_bgp_module.md#id5)

```yaml+jinja
- name: configure global bgp as 65000
  cisco.iosxr.iosxr_bgp:
    bgp_as: 65000
    router_id: 1.1.1.1
    neighbors:
    - neighbor: 182.168.10.1
      remote_as: 500
      description: PEER_1
    - neighbor: 192.168.20.1
      remote_as: 500
      update_source: GigabitEthernet 0/0/0/0
    address_family:
    - name: ipv4
      cast: unicast
      networks:
      - network: 192.168.2.0/23
      - network: 10.0.0.0/8
      redistribute:
      - protocol: ospf
        id: 400
        metric: 110

- name: remove bgp as 65000 from config
  ios_bgp:
    bgp_as: 65000
    state: absent
```

## [Return Values](iosxr_bgp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["router bgp 65000", "bgp router-id 1.1.1.1", "neighbor 182.168.10.1 remote-as 500", "neighbor 182.168.10.1 description PEER_1", "neighbor 192.168.20.1 remote-as 500", "neighbor 192.168.20.1 update-source GigabitEthernet0/0/0/0", "address-family ipv4 unicast", "redistribute ospf 400 metric 110", "network 192.168.2.0/23", "network 10.0.0.0/8", "exit"]` |

## [Status](iosxr_bgp_module.md#id7)

- This module will be removed in a major release after 2023-01-29.
  *[deprecated]*
- For more information see [DEPRECATED](iosxr_bgp_module.md#deprecated).

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
