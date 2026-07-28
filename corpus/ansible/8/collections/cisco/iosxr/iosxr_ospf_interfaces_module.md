---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_ospf_interfaces module – Resource module to configure OSPF interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_ospf_interfaces_module.html
fetched_at: 2026-07-28T01:26:53+00:00
---
# cisco.iosxr.iosxr_ospf_interfaces module – Resource module to configure OSPF interfaces.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_ospf_interfaces`.

New in cisco.iosxr 1.2.0

- [Synopsis](iosxr_ospf_interfaces_module.md#synopsis)
- [Parameters](iosxr_ospf_interfaces_module.md#parameters)
- [Notes](iosxr_ospf_interfaces_module.md#notes)
- [Examples](iosxr_ospf_interfaces_module.md#examples)

## [Synopsis](iosxr_ospf_interfaces_module.md#id1)

- This module manages OSPF(v2/v3) configuration of interfaces on devices running Cisco IOS-XR.

Aliases: ospf_interfaces

## [Parameters](iosxr_ospf_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of OSPF configuration for interfaces. |
| **address_family**  list / elements=dictionary | OSPF settings on the interfaces in address-family context. |
| **afi**  string / required | Address Family Identifier (AFI) for OSPF settings on the interfaces.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **apply_group_option**  dictionary | Specify configuration from a group |
| **group_name**  string | Specify the name of the group |
| **operation**  string | Specify the group config operation  **Choices:**   - `"add"` - `"remove"` - `"append"` |
| **authentication**  dictionary | Enable authentication |
| **message_digest**  dictionary | Use message-digest authentication |
| **keychain**  string | Specify keychain name |
| **null_auth**  boolean | Use no authentication  **Choices:**   - `false` - `true` |
| **authentication_key**  dictionary | Specify authentication password (key) |
| **clear**  string | Specifies an UNENCRYPTED password (key) will follow |
| **encrypted**  string | Specifies an ENCRYPTED password (key) will follow |
| **password**  string | The OSPFv2 password (key) |
| **bfd**  dictionary | Configure BFD parameters |
| **fast_detect**  dictionary | Configure fast detection |
| **set**  boolean | Enable fast detection only  **Choices:**   - `false` - `true` |
| **strict_mode**  boolean | Hold down neighbor session until BFD session is up  **Choices:**   - `false` - `true` |
| **minimum_interval**  integer | Hello interval in milli-seconds |
| **multiplier**  integer | Detect multiplier |
| **cost**  integer | Specify Interface cost |
| **cost_fallback**  dictionary | Specify Cost when cumulative bandwidth goes below the theshold |
| **cost**  integer | Specify cost w.r.t cummulative bandwidth |
| **threshold**  integer | Specify threshold bandwidth when cost-fallback is applied |
| **database_filter**  dictionary | Filter OSPF LSAs during synchronization and flooding |
| **all_outgoing_lsa**  boolean | Filter all outgoing LSA  **Choices:**   - `false` - `true` |
| **dead_interval**  integer | Specify interval after which a neighbor is declared dead |
| **demand_circuit**  boolean | Enable/Disable demand circuits  **Choices:**   - `false` - `true` |
| **fast_reroute**  dictionary | Specify IP Fast Reroute |
| **disabled**  boolean | Disable IP fast reroute  **Choices:**   - `false` - `true` |
| **per_link**  dictionary | Specify per-prefix computation |
| **information_type**  string | Specify per-link LFA exclusion or FRR LFA candidate information  **Choices:**   - `"exclude"` - `"lfa_candidate"` |
| **interface**  dictionary | Specify Per-link LFA exclusion information |
| **bundle_ether**  list / elements=dictionary | Specify Aggregated Ethernet interface(s) |
| **name**  integer | Specify the interface id |
| **bvi**  list / elements=dictionary | Specify Bridge-Group Virtual Interface |
| **name**  integer | Specify the interface id |
| **fast_ethernet**  list / elements=dictionary | Specify FastEthernet/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **fiftygige**  list / elements=dictionary | Specify FiftyGigE/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **fortygige**  list / elements=dictionary | Specify FortyGigE/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **fourhundredgige**  list / elements=dictionary | Specify FourHundredGigE/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **gigabitethernet**  list / elements=dictionary | Specify GigabitEthernet/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **hundredgige**  list / elements=dictionary | Specify HundredGigE/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **mgmteth**  list / elements=dictionary | Specify MgmtEth/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **multilink**  list / elements=dictionary | Specify Multilink network interface(s) |
| **name**  string | Specify the interface id |
| **nve**  list / elements=dictionary | Specify Network Virtualization Endpoint Interface(s) |
| **name**  integer | Specify the interface id |
| **pos_int**  list / elements=dictionary | Specify Aggregated pos interface(s) |
| **name**  integer | Specify the interface id |
| **pw_ether**  list / elements=dictionary | Specify PWHE Ethernet Interface |
| **name**  integer | Specify the interface id |
| **pw_iw**  list / elements=dictionary | Specify PWHE VC11 IP Interworking Interface |
| **name**  integer | Specify the interface id |
| **serial**  list / elements=dictionary | Specify Serial network interface(s) |
| **name**  string | Specify the interface id |
| **srp**  list / elements=dictionary | Specify SRP interface(s) |
| **name**  string | Specify the interface id |
| **tengige**  list / elements=dictionary | Specify TenGigabitEthernet/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **tunnel_ip**  list / elements=dictionary | Specify GRE/IPinIP Tunnel Interface(s) |
| **name**  integer | Specify the interface id |
| **tunnel_ipsec**  list / elements=dictionary | Specify IPSec Tunnel interface(s) |
| **name**  integer | Specify the interface id |
| **tunnel_mpls**  list / elements=dictionary | MPLS Transport Protocol Tunnel interface |
| **name**  string | Specify the interface id |
| **tunnel_mte**  list / elements=dictionary | Specify MPLS Traffic Engineering P2MP Tunnel interface(s) |
| **name**  integer | Specify the interface id |
| **twentyfivegige**  list / elements=dictionary | Specify TwentyFiveGigabitEthernet/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **twohundredgige**  list / elements=dictionary | Specify TwoHundredGigE/IEEE 802.3 interface(s) |
| **name**  string | Specify the interface id |
| **use_candidate_only**  boolean | Enable/Disable backup selection from candidate-list only  **Choices:**   - `false` - `true` |
| **flood_reduction**  boolean | Enable/Disable flood reduction  **Choices:**   - `false` - `true` |
| **hello_interval**  integer | Specify Time between HELLO packets |
| **link_down_fast_detect**  boolean | Configure interface down parameters  **Choices:**   - `false` - `true` |
| **message_digest_key**  dictionary | Message digest authentication password (key) |
| **id**  integer / required | Key ID |
| **md5**  dictionary / required | Use MD5 Algorithm |
| **clear**  boolean | Specifies an UNENCRYPTED password (key) will follow  **Choices:**   - `false` - `true` |
| **encrypted**  boolean | Specifies an ENCRYPTED password (key) will follow  **Choices:**   - `false` - `true` |
| **password**  string | The OSPFv2 password (key) |
| **mpls_ldp_sync**  boolean | Enable/Disable MPLS LDP Sync  **Choices:**   - `false` - `true` |
| **mtu_ignore**  boolean | Enable/Disable ignoring of MTU in DBD packets  **Choices:**   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Specify a neighbor routers |
| **cost**  integer | Specify OSPF cost for point-to-multipoint neighbor |
| **db_filter_all_out**  boolean | Specify Filter OSPF LSA during synchronization and flooding for point-to-multipoint neighbor  **Choices:**   - `false` - `true` |
| **neighbor_id**  string | Specify Neighbor address (name) |
| **poll_interval**  integer | Specify OSPF dead-router polling interval |
| **priority**  integer | Specify OSPF priority of non-broadcast neighbor |
| **network**  string | Specify Network type  **Choices:**   - `"broadcast"` - `"non-broadcast"` - `"point-to-multipoint"` - `"point-to-point"` |
| **packet_size**  integer | Customize size of OSPF packets upto MTU |
| **passive**  boolean | Enable/Disable passive  **Choices:**   - `false` - `true` |
| **prefix_suppression**  boolean | Suppress advertisement of the prefixes  **Choices:**   - `false` - `true` |
| **priority**  integer | Specify Router priority |
| **processes**  list / elements=dictionary | Interfaces configuration for an OSPF process. |
| **area**  dictionary | Specify the area-id |
| **area_id**  string | OSPF interfaces area ID as a decimal value. Please refer vendor documentation of Valid values.  OSPF interfaces area ID in IP address format(e.g. A.B.C.D) |
| **process_id**  string / required | OSPF process tag. |
| **retransmit_interval**  integer | Specify time between retransmitting lost link state advertisements |
| **security_ttl**  dictionary | Enable security |
| **hops**  integer | Maximum number of IP hops allowed <1-254> |
| **set**  boolean | Enable ttl security  **Choices:**   - `false` - `true` |
| **transmit_delay**  integer | Specify estimated time needed to send link-state update packet |
| **name**  string / required | Name/Identifier of the interface. |
| **type**  string / required | Type of the interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config router ospf’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](iosxr_ospf_interfaces_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md)

## [Examples](iosxr_ospf_interfaces_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# % No such configuration item(s)
#

- name: Merge provided OSPF interfaces configuration with the existing configuration
  cisco.iosxr.iosxr_ospf_interfaces:
    config:
      - name: GigabitEthernet0/0/0/0
        type: gigabitethernet
        address_family:
          - afi: ipv4
            processes:
              - process_id: "LAB3"
                area:
                  area_id: 0.0.0.3
            cost: 20
            authentication:
              message_digest:
                keychain: cisco
          - afi: ipv6
            processes:
              - process_id: "LAB3"
                area:
                  area_id: 0.0.0.2
            cost: 30
    state: merged

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": []
#
#  "commands": [
#        "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 cost 20",
#        "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 authentication message-digest",
#        "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 authentication message-digest keychain cisco",
#        "router ospfv3 LAB3 area 0.0.0.2 interface GigabitEthernet 0/0/0/0 cost 30"
#     ]
#
#  "after": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "message_digest": {
#                             "keychain": "cisco"
#                         }
#                     },
#                     "cost": 20,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.3"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 },
#                 {
#                     "afi": "ipv6",
#                     "cost": 30,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.2"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/0",
#             "type": "gigabitethernet"
#         }
#     ]
#
#
# ------------
# After state
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config router ospf
# Thu Oct 23 06:00:57.217 UTC
# router ospf LAB
#  area 0.0.0.0
#  !
#  area 0.0.0.9
#  !
# !
# router ospf LAB1
#  area 0.0.0.1
#  !
#  area 0.0.0.3
#  !
# !
# router ospf LAB3
#  area 0.0.0.3
#   interface GigabitEthernet0/0/0/0
#    cost 20
#    authentication message-digest keychain cisco
#   !
#  !
# !
# router ospf ipv4
# !

# Using replaced
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr-02#show running-config router ospf
# Thu Oct 23 06:00:57.217 UTC
# router ospf LAB
#  area 0.0.0.0
#  !
#  area 0.0.0.9
#  !
# !
# router ospf LAB1
#  area 0.0.0.1
#  !
#  area 0.0.0.3
#  !
# !
# router ospf LAB3
#  area 0.0.0.3
#   interface GigabitEthernet0/0/0/0
#    cost 20
#    authentication message-digest keychain cisco
#   !
#  !
# !
# router ospf ipv4
# !

- name: Replace OSPF interfaces configuration
  cisco.iosxr.iosxr_ospf_interfaces:
    config:
      - name: GigabitEthernet0/0/0/0
        type: gigabitethernet
        address_family:
          - afi: ipv4
            processes:
              - process_id: "LAB3"
                area:
                  area_id: 0.0.0.3
            cost: 30
            authentication:
              message_digest:
                keychain: ciscoiosxr
          - afi: ipv6
            processes:
              - process_id: "LAB3"
                area:
                  area_id: 0.0.0.2
            cost: 30
    state: replaced

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "message_digest": {
#                             "keychain": "cisco"
#                         }
#                     },
#                     "cost": 20,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.3"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 },
#                 {
#                     "afi": "ipv6",
#                     "cost": 30,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.2"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/0",
#             "type": "gigabitethernet"
#         }
#     ]
#
#  "commands": [
#    "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 cost 30",
#    "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 authentication message-digest",
#    "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 authentication message-digest keychain ciscoiosxr"
#     ]
#
#  "after": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "message_digest": {
#                             "keychain": "ciscoiosxr"
#                         }
#                     },
#                     "cost": 30,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.3"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 },
#                 {
#                     "afi": "ipv6",
#                     "cost": 30,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.2"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/0",
#             "type": "gigabitethernet"
#         }
#     ]
#
#
# -----------
# After state
# -----------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config router ospf
# Thu Oct 23 06:10:39.827 UTC
# router ospf LAB
#  area 0.0.0.0
#  !
#  area 0.0.0.9
#  !
# !
# router ospf LAB1
#  area 0.0.0.1
#  !
#  area 0.0.0.3
#  !
# !
# router ospf LAB3
#  area 0.0.0.3
#   interface GigabitEthernet0/0/0/0
#    cost 30
#    authentication message-digest keychain ciscoiosxr
#   !
#  !
# !
# router ospf ipv4
# !

- name: Override existing OSPF interfaces configuration
  cisco.iosxr.iosxr_ospf_interfaces:
    config:
      - name: GigabitEthernet0/0/0/1
        type: gigabitethernet
        address_family:
          - afi: ipv4
            processes:
              - process_id: "LAB1"
                area:
                  area_id: 0.0.0.3
            cost: 10
            authentication:
              message_digest:
                keychain: iosxr
    state: overridden

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "message_digest": {
#                             "keychain": "ciscoiosxr"
#                         }
#                     },
#                     "cost": 30,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.3"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 },
#                 {
#                     "afi": "ipv6",
#                     "cost": 30,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.2"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/0",
#             "type": "gigabitethernet"
#         }
#     ]
#
#  "commands": [
#         "no router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0",
#         "no router ospfv3 LAB3 area 0.0.0.2 interface GigabitEthernet 0/0/0/0",
#         "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 cost 10",
#         "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 authentication message-digest",
#         "router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1 authentication message-digest keychain iosxr"
#     ]
#
#  "after": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "message_digest": {
#                             "keychain": "iosxr"
#                         }
#                     },
#                     "cost": 10,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.3"
#                             },
#                             "process_id": "LAB1"
#                         }
#                     ]
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/1",
#             "type": "gigabitethernet"
#         }
#     ]
#
#
# -----------
# After state
# -----------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config router ospf
# Thu Oct 23 06:28:15.025 UTC
# router ospf LAB
#  area 0.0.0.0
#  !
#  area 0.0.0.9
#  !
# !
# router ospf LAB1
#  area 0.0.0.1
#  !
#  area 0.0.0.3
#   interface GigabitEthernet0/0/0/1
#    cost 10
#    authentication message-digest keychain iosxr
#   !
#  !
# !
# router ospf LAB3
#  area 0.0.0.3
#  !
# !
# router ospf ipv4
# !

# Using deleted
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr-02#show running-config router ospf
# Thu Oct 23 06:28:15.025 UTC
# router ospf LAB
#  area 0.0.0.0
#  !
#  area 0.0.0.9
#  !
# !
# router ospf LAB1
#  area 0.0.0.1
#  !
#  area 0.0.0.3
#   interface GigabitEthernet0/0/0/1
#    cost 10
#    authentication message-digest keychain iosxr
#   !
#  !
# !
# router ospf LAB3
#  area 0.0.0.3
#  !
# !
# router ospf ipv4
# !

- name: Deleted existing OSPF interfaces from the device
  cisco.iosxr.iosxr_ospf_interfaces:
    config:
      - name: GigabitEthernet0/0/0/1
        type: gigabitethernet
    state: deleted

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "message_digest": {
#                             "keychain": "iosxr"
#                         }
#                     },
#                     "cost": 10,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.3"
#                             },
#                             "process_id": "LAB1"
#                         }
#                     ]
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/1",
#             "type": "gigabitethernet"
#         }
#     ],
#
#  "commands": [
#         "no router ospf LAB1 area 0.0.0.3 interface GigabitEthernet 0/0/0/1"
#     ]
#
#  "after": []
#
#
# -----------
# After state
# -----------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config router ospf
# Thu Oct 23 06:34:38.319 UTC
# router ospf LAB
#  area 0.0.0.0
#  !
#  area 0.0.0.9
#  !
# !
# router ospf LAB1
#  area 0.0.0.1
#  !
#  area 0.0.0.3
#  !
# !
# router ospf LAB3
#  area 0.0.0.3
#  !
# !
# router ospf ipv4
# !

# Using parsed
# parsed.cfg
# ------------
# router ospf LAB
#  area 0.0.0.0
#  !
#  area 0.0.0.9
#  !
# !
# router ospf LAB1
#  area 0.0.0.1
#  !
#  area 0.0.0.3
#  !
# !
# router ospf LAB3
#  area 0.0.0.3
#   interface GigabitEthernet0/0/0/0
#    cost 20
#    authentication message-digest keychain cisco
#   !
#  !
# !
# router ospf ipv4
# !
- name: Parsed the device configuration to get output commands
  cisco.iosxr.iosxr_ospf_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "message_digest": {
#                             "keychain": "cisco"
#                         }
#                     },
#                     "cost": 20,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.3"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/0",
#             "type": "gigabitethernet"
#         }
#     ]
#
# Using rendered
#
#
- name: Render the commands for provided  configuration
  cisco.iosxr.iosxr_ospf_interfaces:
    config:
      - name: GigabitEthernet0/0/0/0
        type: gigabitethernet
        address_family:
          - afi: ipv4
            processes:
             - process_id: "LAB3"
               area:
                 area_id: 0.0.0.3
            cost: 20
            authentication:
              message_digest:
                keychain: cisco
          - afi: ipv6
            processes:
             - process_id: "LAB3"
               area:
                 area_id: 0.0.0.2
            cost: 30
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 cost 20",
#        "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 authentication message-digest",
#        "router ospf LAB3 area 0.0.0.3 interface GigabitEthernet 0/0/0/0 authentication message-digest keychain cisco",
#        "router ospfv3 LAB3 area 0.0.0.2 interface GigabitEthernet 0/0/0/0 cost 30"
#     ]

# Using gathered
#
# Before state:
# -------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config router ospf
# Thu Oct 23 06:50:38.743 UTC
# router ospf LAB
#  area 0.0.0.0
#  !
#  area 0.0.0.9
#  !
# !
# router ospf LAB1
#  area 0.0.0.1
#  !
#  area 0.0.0.3
#  !
# !
# router ospf LAB3
#  area 0.0.0.3
#   interface GigabitEthernet0/0/0/0
#    cost 20
#    authentication message-digest keychain cisco
#   !
#  !
# !
# router ospf ipv4
# !

- name: Gather ospf_interfaces routes configuration
  cisco.iosxr.iosxr_ospf_interfaces:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#         {
#             "address_family": [
#                 {
#                     "afi": "ipv4",
#                     "authentication": {
#                         "message_digest": {
#                             "keychain": "cisco"
#                         }
#                     },
#                     "cost": 20,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.3"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 },
#                 {
#                     "afi": "ipv6",
#                     "cost": 30,
#                     "processes": [
#                         {
#                             "area": {
#                                 "area_id": "0.0.0.2"
#                             },
#                             "process_id": "LAB3"
#                         }
#                     ]
#                 }
#             ],
#             "name": "GigabitEthernet0/0/0/0",
#             "type": "gigabitethernet"
#         }
#     ]
#
```

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
