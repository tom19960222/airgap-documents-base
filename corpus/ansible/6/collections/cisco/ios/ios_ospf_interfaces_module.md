---
collection: ansible
version: "6"
title: "cisco.ios.ios_ospf_interfaces module – Resource module to configure OSPF interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_ospf_interfaces_module.html
fetched_at: 2026-07-27T16:55:23+00:00
---
# cisco.ios.ios_ospf_interfaces module – Resource module to configure OSPF interfaces.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_ospf_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_ospf_interfaces_module.md#synopsis)
- [Parameters](ios_ospf_interfaces_module.md#parameters)
- [Notes](ios_ospf_interfaces_module.md#notes)
- [Examples](ios_ospf_interfaces_module.md#examples)
- [Return Values](ios_ospf_interfaces_module.md#return-values)

## [Synopsis](ios_ospf_interfaces_module.md#id1)

- This module configures and manages the Open Shortest Path First (OSPF) version 2 on IOS platforms.

## [Parameters](ios_ospf_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of OSPF interfaces options. |
| **address_family**  list / elements=dictionary | OSPF interfaces settings on the interfaces in address-family context. |
| **adjacency**  boolean | Adjacency staggering  Choices:   - `false` - `true` |
| **afi**  string / required | Address Family Identifier (AFI) for OSPF interfaces settings on the interfaces.  Choices:   - `"ipv4"` - `"ipv6"` |
| **authentication**  dictionary | Enable authentication |
| **key_chain**  string | Use a key-chain for cryptographic authentication keys |
| **message_digest**  boolean | Use message-digest authentication  Choices:   - `false` - `true` |
| **null**  boolean | Use no authentication  Choices:   - `false` - `true` |
| **bfd**  boolean | BFD configuration commands  Enable/Disable BFD on this interface  Choices:   - `false` - `true` |
| **cost**  dictionary | Interface cost |
| **dynamic_cost**  dictionary | Specify dynamic cost options  Valid only with IPv6 OSPF config |
| **default**  integer | Specify default link metric value |
| **hysteresis**  dictionary | Specify hysteresis value for LSA dampening |
| **percent**  integer | Specify hysteresis percent changed. Please refer vendor documentation of Valid values. |
| **threshold**  integer | Specify hysteresis threshold value. Please refer vendor documentation of Valid values. |
| **weight**  dictionary | Specify weight to be placed on individual metrics |
| **l2_factor**  integer | Specify weight to be given to L2-factor metric  Percentage weight of L2-factor metric. Please refer vendor documentation of Valid values. |
| **latency**  integer | Specify weight to be given to latency metric.  Percentage weight of latency metric. Please refer vendor documentation of Valid values. |
| **oc**  boolean | Specify weight to be given to cdr/mdr for oc  Give 100 percent weightage for current data rate(0 for maxdatarate)  Choices:   - `false` - `true` |
| **resources**  integer | Specify weight to be given to resources metric  Percentage weight of resources metric. Please refer vendor documentation of Valid values. |
| **throughput**  integer | Specify weight to be given to throughput metric  Percentage weight of throughput metric. Please refer vendor documentation of Valid values. |
| **interface_cost**  integer | Interface cost or Route cost of this interface |
| **database_filter**  boolean | Filter OSPF LSA during synchronization and flooding  Choices:   - `false` - `true` |
| **dead_interval**  dictionary | Interval after which a neighbor is declared dead |
| **minimal**  integer | Set to 1 second and set multiplier for Hellos  Number of Hellos sent within 1 second. Please refer vendor documentation of Valid values.  Valid only with IP OSPF config |
| **time**  integer | time in seconds |
| **demand_circuit**  dictionary | OSPF Demand Circuit, enable or disable the demand circuit’ |
| **disable**  boolean | Disable demand circuit on this interface  Valid only with IPv6 OSPF config  Choices:   - `false` - `true` |
| **enable**  boolean | Enable Demand Circuit  Choices:   - `false` - `true` |
| **ignore**  boolean | Ignore demand circuit auto-negotiation requests  Choices:   - `false` - `true` |
| **flood_reduction**  boolean | OSPF Flood Reduction  Choices:   - `false` - `true` |
| **hello_interval**  integer | Time between HELLO packets  Please refer vendor documentation of Valid values. |
| **lls**  boolean | Link-local Signaling (LLS) support  Valid only with IP OSPF config  Choices:   - `false` - `true` |
| **manet**  dictionary | Mobile Adhoc Networking options  MANET Peering options  Valid only with IPv6 OSPF config |
| **cost**  dictionary | Redundant path cost improvement required to peer |
| **percent**  integer | Relative incremental path cost. Please refer vendor documentation of Valid values. |
| **threshold**  integer | Absolute incremental path cost. Please refer vendor documentation of Valid values. |
| **link_metrics**  dictionary | Redundant path cost improvement required to peer |
| **cost_threshold**  integer | Minimum link cost threshold. Please refer vendor documentation of Valid values. |
| **set**  boolean | Enable link-metrics  Choices:   - `false` - `true` |
| **mtu_ignore**  boolean | Ignores the MTU in DBD packets  Choices:   - `false` - `true` |
| **multi_area**  dictionary | Set the OSPF multi-area ID  Valid only with IP OSPF config |
| **cost**  integer | Interface cost |
| **id**  integer | OSPF multi-area ID as a decimal value. Please refer vendor documentation of Valid values.  OSPF multi-area ID in IP address format(e.g. A.B.C.D) |
| **neighbor**  dictionary | OSPF neighbor link-local IPv6 address (X:X:X:X::X)  Valid only with IPv6 OSPF config |
| **address**  string | Neighbor link-local IPv6 address |
| **cost**  integer | OSPF cost for point-to-multipoint neighbor |
| **database_filter**  boolean | Filter OSPF LSA during synchronization and flooding for point-to-multipoint neighbor  Choices:   - `false` - `true` |
| **poll_interval**  integer | OSPF dead-router polling interval |
| **priority**  integer | OSPF priority of non-broadcast neighbor |
| **network**  dictionary | Network type |
| **broadcast**  boolean | Specify OSPF broadcast multi-access network  Choices:   - `false` - `true` |
| **manet**  boolean | Specify MANET OSPF interface type  Valid only with IPv6 OSPF config  Choices:   - `false` - `true` |
| **non_broadcast**  boolean | Specify OSPF NBMA network  Choices:   - `false` - `true` |
| **point_to_multipoint**  boolean | Specify OSPF point-to-multipoint network  Choices:   - `false` - `true` |
| **point_to_point**  boolean | Specify OSPF point-to-point network  Choices:   - `false` - `true` |
| **prefix_suppression**  boolean | Enable/Disable OSPF prefix suppression  Choices:   - `false` - `true` |
| **priority**  integer | Router priority. Please refer vendor documentation of Valid values. |
| **process**  dictionary | OSPF interfaces process config |
| **area_id**  string | OSPF interfaces area ID as a decimal value. Please refer vendor documentation of Valid values.  OSPF interfaces area ID in IP address format(e.g. A.B.C.D) |
| **id**  integer | Address Family Identifier (AFI) for OSPF interfaces settings on the interfaces. Please refer vendor documentation of Valid values. |
| **instance_id**  integer | Set the OSPF instance based on ID  Valid only with IPv6 OSPF config |
| **secondaries**  boolean | Include or exclude secondary IP addresses.  Valid only with IPv4 config  Choices:   - `false` - `true` |
| **resync_timeout**  integer | Interval after which adjacency is reset if oob-resync is not started. Please refer vendor documentation of Valid values. |
| **retransmit_interval**  integer | Time between retransmitting lost link state advertisements. Please refer vendor documentation of Valid values. |
| **shutdown**  boolean | Set OSPF protocol’s state to disable under current interface  Choices:   - `false` - `true` |
| **transmit_delay**  integer | Link state transmit delay. Please refer vendor documentation of Valid values. |
| **ttl_security**  dictionary | TTL security check  Valid only with IPV4 OSPF config |
| **hops**  integer | Maximum number of IP hops allowed  Please refer vendor documentation of Valid values. |
| **set**  boolean | Enable TTL Security on all interfaces  Choices:   - `false` - `true` |
| **name**  string / required | Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh running-config | section ^interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](ios_ospf_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.2 on VIRL.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_ospf_interfaces_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ipv6 ospf 55 area 105
#  ipv6 ospf priority 20
#  ipv6 ospf transmit-delay 30
#  ipv6 ospf adjacency stagger disable
# interface GigabitEthernet0/2
#  ip ospf priority 40
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf 10 area 20
#  ip ospf cost 30

- name: Delete provided OSPF Interface config
  cisco.ios.ios_ospf_interfaces:
    config:
      - name: GigabitEthernet0/1
    state: deleted

#  Commands Fired:
#  ---------------
#
#  "commands": [
#         "interface GigabitEthernet0/1",
#         "no ipv6 ospf 55 area 105",
#         "no ipv6 ospf adjacency stagger disable",
#         "no ipv6 ospf priority 20",
#         "no ipv6 ospf transmit-delay 30"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
# interface GigabitEthernet0/2
#  ip ospf priority 40
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf 10 area 20
#  ip ospf cost 30

# Using deleted without any config passed (NOTE: This will delete all OSPF Interfaces configuration from device)

# Before state:
# -------------
#
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ipv6 ospf 55 area 105
#  ipv6 ospf priority 20
#  ipv6 ospf transmit-delay 30
#  ipv6 ospf adjacency stagger disable
# interface GigabitEthernet0/2
#  ip ospf priority 40
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf 10 area 20
#  ip ospf cost 30

- name: Delete all OSPF config from interfaces
  cisco.ios.ios_ospf_interfaces:
    state: deleted

# Commands Fired:
# ---------------
#
#  "commands": [
#         "interface GigabitEthernet0/2",
#         "no ip ospf 10 area 20",
#         "no ip ospf adjacency stagger disable",
#         "no ip ospf cost 30",
#         "no ip ospf priority 40",
#         "no ip ospf ttl-security hops 50",
#         "interface GigabitEthernet0/1",
#         "no ipv6 ospf 55 area 105",
#         "no ipv6 ospf adjacency stagger disable",
#         "no ipv6 ospf priority 20",
#         "no ipv6 ospf transmit-delay 30"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
# interface GigabitEthernet0/2

# Using merged

# Before state:
# -------------
#
# router-ios#sh running-config | section ^interface
# router-ios#

- name: Merge provided OSPF Interfaces configuration
  cisco.ios.ios_ospf_interfaces:
    config:
      - name: GigabitEthernet0/1
        address_family:
          - afi: ipv4
            process:
              id: 10
              area_id: 30
            adjacency: true
            bfd: true
            cost:
              interface_cost: 5
            dead_interval:
              time: 5
            demand_circuit:
              ignore: true
            network:
              broadcast: true
            priority: 25
            resync_timeout: 10
            shutdown: true
            ttl_security:
              hops: 50
          - afi: ipv6
            process:
              id: 35
              area_id: 45
            adjacency: true
            database_filter: true
            manet:
              link_metrics:
                cost_threshold: 10
            priority: 55
            transmit_delay: 45
    state: merged

#  Commands Fired:
#  ---------------
#
#   "commands": [
#         "interface GigabitEthernet0/1",
#         "ip ospf 10 area 30",
#         "ip ospf adjacency stagger disable",
#         "ip ospf bfd",
#         "ip ospf cost 5",
#         "ip ospf dead-interval 5",
#         "ip ospf demand-circuit ignore",
#         "ip ospf network broadcast",
#         "ip ospf priority 25",
#         "ip ospf resync-timeout 10",
#         "ip ospf shutdown",
#         "ip ospf ttl-security hops 50",
#         "ipv6 ospf 35 area 45",
#         "ipv6 ospf adjacency stagger disable",
#         "ipv6 ospf database-filter all out",
#         "ipv6 ospf manet peering link-metrics 10",
#         "ipv6 ospf priority 55",
#         "ipv6 ospf transmit-delay 45"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip ospf network broadcast
#  ip ospf resync-timeout 10
#  ip ospf dead-interval 5
#  ip ospf priority 25
#  ip ospf demand-circuit ignore
#  ip ospf bfd
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf shutdown
#  ip ospf 10 area 30
#  ip ospf cost 5
#  ipv6 ospf 35 area 45
#  ipv6 ospf priority 55
#  ipv6 ospf transmit-delay 45
#  ipv6 ospf database-filter all out
#  ipv6 ospf adjacency stagger disable
#  ipv6 ospf manet peering link-metrics 10
# interface GigabitEthernet0/2

# Using overridden

# Before state:
# -------------
#
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip ospf network broadcast
#  ip ospf resync-timeout 10
#  ip ospf dead-interval 5
#  ip ospf priority 25
#  ip ospf demand-circuit ignore
#  ip ospf bfd
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf shutdown
#  ip ospf 10 area 30
#  ip ospf cost 5
#  ipv6 ospf 35 area 45
#  ipv6 ospf priority 55
#  ipv6 ospf transmit-delay 45
#  ipv6 ospf database-filter all out
#  ipv6 ospf adjacency stagger disable
#  ipv6 ospf manet peering link-metrics 10
# interface GigabitEthernet0/2

- name: Override provided OSPF Interfaces configuration
  cisco.ios.ios_ospf_interfaces:
    config:
      - name: GigabitEthernet0/1
        address_family:
          - afi: ipv6
            process:
              id: 55
              area_id: 105
            adjacency: true
            priority: 20
            transmit_delay: 30
      - name: GigabitEthernet0/2
        address_family:
          - afi: ipv4
            process:
              id: 10
              area_id: 20
            adjacency: true
            cost:
              interface_cost: 30
            priority: 40
            ttl_security:
              hops: 50
    state: overridden

# Commands Fired:
# ---------------
#
#  "commands": [
#         "interface GigabitEthernet0/2",
#         "ip ospf 10 area 20",
#         "ip ospf adjacency stagger disable",
#         "ip ospf cost 30",
#         "ip ospf priority 40",
#         "ip ospf ttl-security hops 50",
#         "interface GigabitEthernet0/1",
#         "ipv6 ospf 55 area 105",
#         "no ipv6 ospf database-filter all out",
#         "no ipv6 ospf manet peering link-metrics 10",
#         "ipv6 ospf priority 20",
#         "ipv6 ospf transmit-delay 30",
#         "no ip ospf 10 area 30",
#         "no ip ospf adjacency stagger disable",
#         "no ip ospf bfd",
#         "no ip ospf cost 5",
#         "no ip ospf dead-interval 5",
#         "no ip ospf demand-circuit ignore",
#         "no ip ospf network broadcast",
#         "no ip ospf priority 25",
#         "no ip ospf resync-timeout 10",
#         "no ip ospf shutdown",
#         "no ip ospf ttl-security hops 50"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ipv6 ospf 55 area 105
#  ipv6 ospf priority 20
#  ipv6 ospf transmit-delay 30
#  ipv6 ospf adjacency stagger disable
# interface GigabitEthernet0/2
#  ip ospf priority 40
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf 10 area 20
#  ip ospf cost 30

# Using replaced

# Before state:
# -------------
#
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip ospf network broadcast
#  ip ospf resync-timeout 10
#  ip ospf dead-interval 5
#  ip ospf priority 25
#  ip ospf demand-circuit ignore
#  ip ospf bfd
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf shutdown
#  ip ospf 10 area 30
#  ip ospf cost 5
#  ipv6 ospf 35 area 45
#  ipv6 ospf priority 55
#  ipv6 ospf transmit-delay 45
#  ipv6 ospf database-filter all out
#  ipv6 ospf adjacency stagger disable
#  ipv6 ospf manet peering link-metrics 10
# interface GigabitEthernet0/2

- name: Replaced provided OSPF Interfaces configuration
  cisco.ios.ios_ospf_interfaces:
    config:
      - name: GigabitEthernet0/2
        address_family:
          - afi: ipv6
            process:
              id: 55
              area_id: 105
            adjacency: true
            priority: 20
            transmit_delay: 30
    state: replaced

# Commands Fired:
# ---------------
#  "commands": [
#         "interface GigabitEthernet0/2",
#         "ipv6 ospf 55 area 105",
#         "ipv6 ospf adjacency stagger disable",
#         "ipv6 ospf priority 20",
#         "ipv6 ospf transmit-delay 30"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip ospf network broadcast
#  ip ospf resync-timeout 10
#  ip ospf dead-interval 5
#  ip ospf priority 25
#  ip ospf demand-circuit ignore
#  ip ospf bfd
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf shutdown
#  ip ospf 10 area 30
#  ip ospf cost 5
#  ipv6 ospf 35 area 45
#  ipv6 ospf priority 55
#  ipv6 ospf transmit-delay 45
#  ipv6 ospf database-filter all out
#  ipv6 ospf adjacency stagger disable
#  ipv6 ospf manet peering link-metrics 10
# interface GigabitEthernet0/2
#  ipv6 ospf 55 area 105
#  ipv6 ospf priority 20
#  ipv6 ospf transmit-delay 30
#  ipv6 ospf adjacency stagger disable

# Using Gathered

# Before state:
# -------------
#
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip ospf network broadcast
#  ip ospf resync-timeout 10
#  ip ospf dead-interval 5
#  ip ospf priority 25
#  ip ospf demand-circuit ignore
#  ip ospf bfd
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf shutdown
#  ip ospf 10 area 30
#  ip ospf cost 5
#  ipv6 ospf 35 area 45
#  ipv6 ospf priority 55
#  ipv6 ospf transmit-delay 45
#  ipv6 ospf database-filter all out
#  ipv6 ospf adjacency stagger disable
#  ipv6 ospf manet peering link-metrics 10
# interface GigabitEthernet0/2

- name: Gather OSPF Interfaces provided configurations
  cisco.ios.ios_ospf_interfaces:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
#  "gathered": [
#         {
#             "name": "GigabitEthernet0/2"
#         },
#         {
#             "address_family": [
#                 {
#                     "adjacency": true,
#                     "afi": "ipv4",
#                     "bfd": true,
#                     "cost": {
#                         "interface_cost": 5
#                     },
#                     "dead_interval": {
#                         "time": 5
#                     },
#                     "demand_circuit": {
#                         "ignore": true
#                     },
#                     "network": {
#                         "broadcast": true
#                     },
#                     "priority": 25,
#                     "process": {
#                         "area_id": "30",
#                         "id": 10
#                     },
#                     "resync_timeout": 10,
#                     "shutdown": true,
#                     "ttl_security": {
#                         "hops": 50
#                     }
#                 },
#                 {
#                     "adjacency": true,
#                     "afi": "ipv6",
#                     "database_filter": true,
#                     "manet": {
#                         "link_metrics": {
#                             "cost_threshold": 10
#                         }
#                     },
#                     "priority": 55,
#                     "process": {
#                         "area_id": "45",
#                         "id": 35
#                     },
#                     "transmit_delay": 45
#                 }
#             ],
#             "name": "GigabitEthernet0/1"
#         },
#         {
#             "name": "GigabitEthernet0/0"
#         }
#  ]

# After state:
# ------------
#
# router-ios#sh running-config | section ^interface
# interface GigabitEthernet0/0
# interface GigabitEthernet0/1
#  ip ospf network broadcast
#  ip ospf resync-timeout 10
#  ip ospf dead-interval 5
#  ip ospf priority 25
#  ip ospf demand-circuit ignore
#  ip ospf bfd
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf shutdown
#  ip ospf 10 area 30
#  ip ospf cost 5
#  ipv6 ospf 35 area 45
#  ipv6 ospf priority 55
#  ipv6 ospf transmit-delay 45
#  ipv6 ospf database-filter all out
#  ipv6 ospf adjacency stagger disable
#  ipv6 ospf manet peering link-metrics 10
# interface GigabitEthernet0/2

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_ospf_interfaces:
    config:
      - name: GigabitEthernet0/1
        address_family:
          - afi: ipv4
            process:
              id: 10
              area_id: 30
            adjacency: true
            bfd: true
            cost:
              interface_cost: 5
            dead_interval:
              time: 5
            demand_circuit:
              ignore: true
            network:
              broadcast: true
            priority: 25
            resync_timeout: 10
            shutdown: true
            ttl_security:
              hops: 50
          - afi: ipv6
            process:
              id: 35
              area_id: 45
            adjacency: true
            database_filter: true
            manet:
              link_metrics:
                cost_threshold: 10
            priority: 55
            transmit_delay: 45
    state: rendered

# Module Execution Result:
# ------------------------
#
#  "rendered": [
#         "interface GigabitEthernet0/1",
#         "ip ospf 10 area 30",
#         "ip ospf adjacency stagger disable",
#         "ip ospf bfd",
#         "ip ospf cost 5",
#         "ip ospf dead-interval 5",
#         "ip ospf demand-circuit ignore",
#         "ip ospf network broadcast",
#         "ip ospf priority 25",
#         "ip ospf resync-timeout 10",
#         "ip ospf shutdown",
#         "ip ospf ttl-security hops 50",
#         "ipv6 ospf 35 area 45",
#         "ipv6 ospf adjacency stagger disable",
#         "ipv6 ospf database-filter all out",
#         "ipv6 ospf manet peering link-metrics 10",
#         "ipv6 ospf priority 55",
#         "ipv6 ospf transmit-delay 45"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# interface GigabitEthernet0/2
# interface GigabitEthernet0/1
#  ip ospf network broadcast
#  ip ospf resync-timeout 10
#  ip ospf dead-interval 5
#  ip ospf priority 25
#  ip ospf demand-circuit ignore
#  ip ospf bfd
#  ip ospf adjacency stagger disable
#  ip ospf ttl-security hops 50
#  ip ospf shutdown
#  ip ospf 10 area 30
#  ip ospf cost 5
#  ipv6 ospf 35 area 45
#  ipv6 ospf priority 55
#  ipv6 ospf transmit-delay 45
#  ipv6 ospf database-filter all out
#  ipv6 ospf adjacency stagger disable
#  ipv6 ospf manet peering link-metrics 10
# interface GigabitEthernet0/0

- name: Parse the provided configuration with the existing running configuration
  cisco.ios.ios_ospf_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
#  "parsed": [
#         },
#         {
#             "name": "GigabitEthernet0/2"
#         },
#         {
#             "address_family": [
#                 {
#                     "adjacency": true,
#                     "afi": "ipv4",
#                     "bfd": true,
#                     "cost": {
#                         "interface_cost": 5
#                     },
#                     "dead_interval": {
#                         "time": 5
#                     },
#                     "demand_circuit": {
#                         "ignore": true
#                     },
#                     "network": {
#                         "broadcast": true
#                     },
#                     "priority": 25,
#                     "process": {
#                         "area_id": "30",
#                         "id": 10
#                     },
#                     "resync_timeout": 10,
#                     "shutdown": true,
#                     "ttl_security": {
#                         "hops": 50
#                     }
#                 },
#                 {
#                     "adjacency": true,
#                     "afi": "ipv6",
#                     "database_filter": true,
#                     "manet": {
#                         "link_metrics": {
#                             "cost_threshold": 10
#                         }
#                     },
#                     "priority": 55,
#                     "process": {
#                         "area_id": "45",
#                         "id": 35
#                     },
#                     "transmit_delay": 45
#                 }
#             ],
#             "name": "GigabitEthernet0/1"
#         },
#         {
#             "name": "GigabitEthernet0/0"
#         }
#     ]
```

## [Return Values](ios_ospf_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface GigabitEthernet0/1", "ip ospf 10 area 30", "ip ospf cost 5", "ip ospf priority 25"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
