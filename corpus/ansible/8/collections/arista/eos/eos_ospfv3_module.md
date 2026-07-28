---
collection: ansible
version: "8"
title: "arista.eos.eos_ospfv3 module – OSPFv3 resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_ospfv3_module.html
fetched_at: 2026-07-28T01:11:12+00:00
---
# arista.eos.eos_ospfv3 module – OSPFv3 resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_ospfv3`.

New in arista.eos 1.1.0

- [Synopsis](eos_ospfv3_module.md#synopsis)
- [Parameters](eos_ospfv3_module.md#parameters)
- [Notes](eos_ospfv3_module.md#notes)
- [Examples](eos_ospfv3_module.md#examples)
- [Return Values](eos_ospfv3_module.md#return-values)

## [Synopsis](eos_ospfv3_module.md#id1)

- This module configures and manages the attributes of ospfv3 on Arista EOS platforms.

Aliases: ospfv3

## [Parameters](eos_ospfv3_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of configurations for ospfv3. |
| **processes**  list / elements=dictionary | A list of dictionary specifying the ospfv3 processes. |
| **address_family**  list / elements=dictionary | Enable address family and enter its config mode |
| **adjacency**  dictionary | Configure adjacency options for OSPF instance. |
| **exchange_start**  dictionary | Configure exchange-start options for OSPF instance. |
| **threshold**  integer | Number of peers to bring up simultaneously. |
| **afi**  string | address family .  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **areas**  list / elements=dictionary | Specifies the configuration for OSPF areas |
| **area_id**  string | Specifies a 32 bit number expressed in decimal or dotted-decimal notation. |
| **authentication**  dictionary | Configure authentication for the area incase of ospfv3. |
| **algorithm**  string | Name of algorithm to be used.  **Choices:**   - `"md5"` - `"sha1"` |
| **encrypt_key**  boolean | If false, key string is not encrypted  **Choices:**   - `false` - `true` |
| **hidden_key**  boolean | If true, Specifies that a HIDDEN key will follow.  **Choices:**   - `false` - `true` |
| **key**  string | 128 bit MD5 key or 140 bit SHA1 key. |
| **passphrase**  string | Passphrase String for deriving keys for authentication and encryption. |
| **spi**  integer | Specify the SPI value |
| **default_cost**  integer | Specify the cost for default summary route in stub/NSSA area. |
| **encryption**  dictionary | Configure encryption for the area |
| **algorithm**  string | name of the algorithm to be used.  **Choices:**   - `"sha1"` - `"md5"` |
| **encrypt_key**  boolean | If false, key string is not encrypted  **Choices:**   - `false` - `true` |
| **encryption**  string | name of encryption to be used.  **Choices:**   - `"3des-cbc"` - `"aes-128-cbc"` - `"aes-192-cbc"` - `"aes-256-cbc"` - `"null"` |
| **hidden_key**  boolean | If true, Specifies that a HIDDEN key will follow.  **Choices:**   - `false` - `true` |
| **key**  string | 128 bit MD5 key or 140 bit SHA1 key. |
| **passphrase**  string | Passphrase String for deriving keys for authentication and encryption. |
| **spi**  integer | Specify the SPI value |
| **nssa**  dictionary | Configures NSSA parameters. |
| **default_information_originate**  dictionary | Originate default Type 7 LSA. |
| **metric**  integer | Metric for default route. |
| **metric_type**  integer | Metric type for default route. |
| **nssa_only**  boolean | Limit default advertisement to this NSSA area.  **Choices:**   - `false` - `true` |
| **set**  boolean | true if only default information orignate is set  **Choices:**   - `false` - `true` |
| **no_summary**  boolean | Filter all type-3 LSAs in the nssa area.  **Choices:**   - `false` - `true` |
| **nssa_only**  boolean | Disable Type-7 LSA p-bit setting  **Choices:**   - `false` - `true` |
| **set**  boolean | true if only nssa is set  **Choices:**   - `false` - `true` |
| **translate**  boolean | Enable LSA translation.  **Choices:**   - `false` - `true` |
| **ranges**  list / elements=dictionary | Configure route summarization. |
| **address**  string | IP address. |
| **advertise**  boolean | Enable Advertisement of the range.  **Choices:**   - `false` - `true` |
| **cost**  integer | Configures the metric. |
| **subnet_address**  string | IP address with mask length |
| **subnet_mask**  string | IP subnet mask |
| **stub**  dictionary | Stub area. |
| **set**  boolean | true if only stub is set  **Choices:**   - `false` - `true` |
| **summary_lsa**  boolean | If false , Filter all type-3 LSAs in the stub area.  **Choices:**   - `false` - `true` |
| **auto_cost**  dictionary | Set auto-cost. |
| **reference_bandwidth**  integer | reference bandwidth in megabits per sec. |
| **bfd**  dictionary | Enable BFD. |
| **all_interfaces**  boolean | Enable BFD on all interfaces.  **Choices:**   - `false` - `true` |
| **default_information**  dictionary | Control distribution of default information. |
| **always**  boolean | Always advertise default route.  **Choices:**   - `false` - `true` |
| **metric**  integer | Metric for default route. |
| **metric_type**  integer | Metric type for default route. |
| **originate**  boolean | Distribute a default route.  **Choices:**   - `false` - `true` |
| **route_map**  string | Specify which route-map to use. |
| **default_metric**  integer | Configure the default metric for redistributed routes. |
| **distance**  integer | Specifies the administrative distance for routes. |
| **fips_restrictions**  boolean | Use FIPS compliant algorithms  **Choices:**   - `false` - `true` |
| **graceful_restart**  dictionary | Enable graceful restart mode. |
| **grace_period**  integer | Specify maximum time to wait for graceful-restart to complete. |
| **set**  boolean | When true sets the grace_fulrestart config alone.  **Choices:**   - `false` - `true` |
| **graceful_restart_helper**  boolean | If true, Enable graceful restart helper.  **Choices:**   - `false` - `true` |
| **log_adjacency_changes**  dictionary | To configure link-state changes and transitions of OSPFv3 neighbors. |
| **detail**  boolean | If true , configures the switch to log all link-state changes.  **Choices:**   - `false` - `true` |
| **set**  boolean | When true sets the log_adjacency_changes config alone.  **Choices:**   - `false` - `true` |
| **max_metric**  dictionary | Set maximum metric. |
| **router_lsa**  dictionary | Maximum metric in self-originated router-LSAs. |
| **external_lsa**  dictionary | Override external-lsa metric with max-metric value. |
| **max_metric_value**  integer | Set max metric value for external LSAs. |
| **set**  boolean | Set external-lsa attribute.  **Choices:**   - `false` - `true` |
| **include_stub**  boolean | Set maximum metric for stub links in router-LSAs.  **Choices:**   - `false` - `true` |
| **on_startup**  dictionary | Set maximum metric temporarily after reboot. |
| **wait_for_bgp**  boolean | Let BGP decide when to originate router-LSA with normal metric  **Choices:**   - `false` - `true` |
| **wait_period**  integer | Wait period in seconds after startup. |
| **set**  boolean | Set router-lsa attribute.  **Choices:**   - `false` - `true` |
| **summary_lsa**  dictionary | Override summary-lsa metric with max-metric value. |
| **max_metric_value**  integer | Set max metric value for external LSAs. |
| **set**  boolean | Set external-lsa attribute.  **Choices:**   - `false` - `true` |
| **maximum_paths**  integer | Maximum number of next-hops in an ECMP route. |
| **passive_interface**  boolean | Include interface but without actively running OSPF.  **Choices:**   - `false` - `true` |
| **redistribute**  list / elements=dictionary | Specifies the routes to be redistributed. |
| **route_map**  string | Specify which route map to use. |
| **routes**  string | Route types (BGP,static,connected)  **Choices:**   - `"bgp"` - `"connected"` - `"static"` |
| **router_id**  string | 32-bit number assigned to a router running OSPFv3. |
| **shutdown**  boolean | Disable the OSPF instance.  **Choices:**   - `false` - `true` |
| **timers**  dictionary | Configure OSPF timers. |
| **lsa**  any | Configure OSPFv3 LSA timers. |
| **direction**  string | Configure OSPFv3 LSA receiving/transmission timers.  **Choices:**   - `"rx"` - `"tx"` |
| **initial**  integer | Initial SPF schedule delay in msecs. |
| **max**  integer | Max wait time between two SPFs in msecs. |
| **min**  integer | Min Hold time between two SPFs in msecs |
| **out_delay**  integer | Configure out-delay timer. |
| **pacing**  integer | Configure OSPF packet pacing. |
| **spf**  dictionary | Configure OSPFv3 spf timers. |
| **initial**  integer | Initial SPF schedule delay in msecs. |
| **max**  integer | Max wait time between two SPFs in msecs. |
| **min**  integer | Min Hold time between two SPFs in msecs |
| **throttle**  dictionary | This command is deprecated by ‘timers lsa’ or ‘timers spf’. |
| **initial**  integer | Initial SPF schedule delay in msecs. |
| **lsa**  boolean | Configure threshold for retransmission of lsa  **Choices:**   - `false` - `true` |
| **max**  integer | Max wait time between two SPFs in msecs. |
| **min**  integer | Min Hold time between two SPFs in msecs |
| **spf**  boolean | Configure time between SPF calculations  **Choices:**   - `false` - `true` |
| **adjacency**  dictionary | Configure adjacency options for OSPF instance. |
| **exchange_start**  dictionary | Configure exchange-start options for OSPF instance. |
| **threshold**  integer | Number of peers to bring up simultaneously. |
| **areas**  list / elements=dictionary | Specifies the configuration for OSPF areas |
| **area_id**  string | Specifies a 32 bit number expressed in decimal or dotted-decimal notation. |
| **authentication**  dictionary | Configure authentication for the area incase of ospfv3. |
| **algorithm**  string | Name of algorithm to be used.  **Choices:**   - `"md5"` - `"sha1"` |
| **encrypt_key**  boolean | If false, key string is not encrypted  **Choices:**   - `false` - `true` |
| **hidden_key**  boolean | If true, Specifies that a HIDDEN key will follow.  **Choices:**   - `false` - `true` |
| **key**  string | 128 bit MD5 key or 140 bit SHA1 key. |
| **passphrase**  string | Passphrase String for deriving keys for authentication and encryption. |
| **spi**  integer | Specify the SPI value |
| **default_cost**  integer | Specify the cost for default summary route in stub/NSSA area. |
| **encryption**  dictionary | Configure encryption for the area |
| **algorithm**  string | name of the algorithm to be used.  **Choices:**   - `"sha1"` - `"md5"` |
| **encrypt_key**  boolean | If false, key string is not encrypted  **Choices:**   - `false` - `true` |
| **encryption**  string | name of encryption to be used.  **Choices:**   - `"3des-cbc"` - `"aes-128-cbc"` - `"aes-192-cbc"` - `"aes-256-cbc"` - `"null"` |
| **hidden_key**  boolean | If true, Specifies that a HIDDEN key will follow.  **Choices:**   - `false` - `true` |
| **key**  string | 128 bit MD5 key or 140 bit SHA1 key. |
| **passphrase**  string | Passphrase String for deriving keys for authentication and encryption. |
| **spi**  integer | Specify the SPI value |
| **nssa**  dictionary | Configures NSSA parameters. |
| **default_information_originate**  dictionary | Originate default Type 7 LSA. |
| **metric**  integer | Metric for default route. |
| **metric_type**  integer | Metric type for default route. |
| **nssa_only**  boolean | Limit default advertisement to this NSSA area.  **Choices:**   - `false` - `true` |
| **set**  boolean | true if only default information orignate is set  **Choices:**   - `false` - `true` |
| **no_summary**  boolean | Filter all type-3 LSAs in the nssa area.  **Choices:**   - `false` - `true` |
| **nssa_only**  boolean | Disable Type-7 LSA p-bit setting  **Choices:**   - `false` - `true` |
| **set**  boolean | true if only nssa is set  **Choices:**   - `false` - `true` |
| **translate**  boolean | Enable LSA translation.  **Choices:**   - `false` - `true` |
| **stub**  dictionary | Stub area. |
| **set**  boolean | true if only stub is set.  **Choices:**   - `false` - `true` |
| **summary_lsa**  boolean | If false , Filter all type-3 LSAs in the stub area.  **Choices:**   - `false` - `true` |
| **auto_cost**  dictionary | Set auto-cost. |
| **reference_bandwidth**  integer | reference bandwidth in megabits per sec. |
| **bfd**  dictionary | Enable BFD. |
| **all_interfaces**  boolean | Enable BFD on all interfaces.  **Choices:**   - `false` - `true` |
| **fips_restrictions**  boolean | Use FIPS compliant algorithms  **Choices:**   - `false` - `true` |
| **graceful_restart**  dictionary | Enable graceful restart mode. |
| **grace_period**  integer | Specify maximum time to wait for graceful-restart to complete. |
| **set**  boolean | When true sets the grace_fulrestart config alone.  **Choices:**   - `false` - `true` |
| **graceful_restart_helper**  boolean | If true, Enable graceful restart helper.  **Choices:**   - `false` - `true` |
| **log_adjacency_changes**  dictionary | To configure link-state changes and transitions of OSPFv3 neighbors. |
| **detail**  boolean | If true , configures the switch to log all link-state changes.  **Choices:**   - `false` - `true` |
| **set**  boolean | When true sets the log_adjacency_changes config alone.  **Choices:**   - `false` - `true` |
| **max_metric**  dictionary | Set maximum metric. |
| **router_lsa**  dictionary | Maximum metric in self-originated router-LSAs. |
| **external_lsa**  dictionary | Override external-lsa metric with max-metric value. |
| **max_metric_value**  integer | Set max metric value for external LSAs. |
| **set**  boolean | Set external-lsa attribute.  **Choices:**   - `false` - `true` |
| **include_stub**  boolean | Set maximum metric for stub links in router-LSAs.  **Choices:**   - `false` - `true` |
| **on_startup**  dictionary | Set maximum metric temporarily after reboot. |
| **wait_for_bgp**  boolean | Let BGP decide when to originate router-LSA with normal metric  **Choices:**   - `false` - `true` |
| **wait_period**  integer | Wait period in seconds after startup. |
| **set**  boolean | Set router-lsa attribute.  **Choices:**   - `false` - `true` |
| **summary_lsa**  dictionary | Override summary-lsa metric with max-metric value. |
| **max_metric_value**  integer | Set max metric value for external LSAs. |
| **set**  boolean | Set external-lsa attribute.  **Choices:**   - `false` - `true` |
| **passive_interface**  boolean | Include interface but without actively running OSPF.  **Choices:**   - `false` - `true` |
| **router_id**  string | 32-bit number assigned to a router running OSPFv3. |
| **shutdown**  boolean | Disable the OSPF instance.  **Choices:**   - `false` - `true` |
| **timers**  dictionary | Configure OSPF timers. |
| **lsa**  any | Configure OSPFv3 LSA timers. |
| **direction**  string | Configure OSPFv3 LSA receiving/transmission timers.  **Choices:**   - `"rx"` - `"tx"` |
| **initial**  integer | Initial SPF schedule delay in msecs. |
| **max**  integer | Max wait time between two SPFs in msecs. |
| **min**  integer | Min Hold time between two SPFs in msecs |
| **out_delay**  integer | Configure out-delay timer. |
| **pacing**  integer | Configure OSPF packet pacing. |
| **spf**  dictionary | Configure OSPFv3 spf timers. |
| **initial**  integer | Initial SPF schedule delay in msecs. |
| **max**  integer | Max wait time between two SPFs in msecs. |
| **min**  integer | Min Hold time between two SPFs in msecs |
| **throttle**  dictionary | This command is deprecated by ‘timers lsa’ or ‘timers spf’. |
| **initial**  integer | Initial SPF schedule delay in msecs. |
| **lsa**  boolean | Configure threshold for retransmission of lsa  **Choices:**   - `false` - `true` |
| **max**  integer | Max wait time between two SPFs in msecs. |
| **min**  integer | Min Hold time between two SPFs in msecs |
| **spf**  boolean | Configure time between SPF calculations  **Choices:**   - `false` - `true` |
| **vrf**  string | VRF name . |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ospfv3**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_ospfv3_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_ospfv3_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# veos#show running-config | section ospfv3
# veos#

- name: Merge the provided configuration with the existing running configuration
  arista.eos.eos_ospfv3:
    config:
      processes:
        - address_family:
            - timers:
                lsa: 22
              graceful_restart:
                grace_period: 35
              afi: "ipv6"
          timers:
            pacing: 55
          fips_restrictions: true
          router_id: "2.2.2.2"
          vrf: "vrfmerge"
    state: merged

# Task output:
# ------------
# before: {}
#
# commands:
# - router ospfv3 vrf vrfmerge
# - address-family ipv6
# - graceful-restart grace-period 35
# - timers lsa arrival 22
# - exit
# - timers pacing flood 55
# - fips restrictions
# - router-id 2.2.2.2
# - exit
#
# after:
#     processes:
#     - address_family:
#       - afi: ipv6
#         fips_restrictions: true
#         graceful_restart:
#           grace_period: 35
#       fips_restrictions: true
#       router_id: 2.2.2.2
#       timers:
#         pacing: 55
#       vrf: vrfmerge

# After state:
# ------------
# veos#show running-config | section ospfv3
# router ospfv3 vrf vrfmerge
#    router-id 2.2.2.2
# test
#    fips restrictions
#    timers pacing flood 55
#    !
#    address-family ipv6
#       fips restrictions
#       timers lsa arrival 22
#       graceful-restart grace-period 35

# using replaced

# Before state:
# -------------
# veos#show running-config | section ospfv3
# router ospfv3
#    fips restrictions
#    area 0.0.0.0 encryption ipsec spi 43 esp null md5 passphrase 7 h8pZp9eprTYjjoY/NKFFe0Ei7x03Y7dyLotRhI0a5t4=
# !
# router ospfv3 vrf vrfmerge
#    router-id 2.2.2.2
#    fips restrictions
#    timers pacing flood 55
#    !
#    address-family ipv6
#       fips restrictions
#       timers lsa arrival 22
#       graceful-restart grace-period 35

- name: Replace a section of running config with provided config
  arista.eos.eos_ospfv3:
    config:
      processes:
        - areas:
            - area_id: "0.0.0.0"
              encryption:
                spi: 43
                encryption: "null"
                algorithm: "md5"
                encrypt_key: false
                passphrase: "7hl8FV3lZ6H1mAKpjL47hQ=="
          vrf: "default"
          address_family:
            - afi: "ipv4"
              router_id: "7.1.1.1"
    state: replaced

# Task output:
# ------------
# before:
#     processes:
#     - areas:
#       - area_id: 0.0.0.0
#         encryption:
#           algorithm: md5
#           encryption: 'null'
#           hidden_key: true
#           passphrase: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
#           spi: 43
#       fips_restrictions: true
#       vrf: default
#     - address_family:
#       - afi: ipv6
#         fips_restrictions: true
#         graceful_restart:
#           grace_period: 35
#       fips_restrictions: true
#       router_id: 2.2.2.2
#       timers:
#         pacing: 55
#       vrf: vrfmerge
#
# commands:
# - router ospfv3 vrf vrfmerge
# - address-family ipv6
# - no fips restrictions
# - no graceful-restart
# - no timers lsa arrival 22
# - area 0.0.0.3 range 10.1.2.2/24 advertise
# - area 0.0.0.3 range 60.1.1.1 255.255.0.0 cost 30
# - exit
# - passive-interface default
# - no router-id
# - no fips restrictions
# - no timers pacing flood 55
# - exit
#
# after:
#     processes:
#     - areas:
#       - area_id: 0.0.0.0
#         encryption:
#           algorithm: md5
#           encryption: 'null'
#           hidden_key: true
#           passphrase: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
#           spi: 43
#       vrf: default
#     - address_family:
#       - afi: ipv6
#         areas:
#         - area_id: 0.0.0.3
#           ranges:
#           - address: 10.1.2.0/24
#           - address: 60.1.0.0/16
#             cost: 30
#       passive_interface: true
#       vrf: vrfmerge

# After state:
# ------------
# veos#show running-config | section ospfv3
# router ospfv3
#    area 0.0.0.0 encryption ipsec spi 43 esp null md5 passphrase 7 h8pZp9eprTYjjoY/NKFFe0Ei7x03Y7dyLotRhI0a5t4=
# !
# router ospfv3 vrf vrfmerge
#    passive-interface default
#    !
#    address-family ipv6
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30

# using overridden

# Before state:
# -------------
# veos#show running-config | section ospfv3
# router ospfv3
#    area 0.0.0.0 encryption ipsec spi 43 esp null md5 passphrase 7 h8pZp9eprTYjjoY/NKFFe0Ei7x03Y7dyLotRhI0a5t4=
# !
# router ospfv3 vrf vrfmerge
#    passive-interface default
#    !
#    address-family ipv6
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30

- name: Override running config with provided config
  arista.eos.eos_ospfv3:
    config:
      processes:
        - address_family:
            - areas:
                - area_id: "0.0.0.3"
                  ranges:
                    - address: 10.1.2.2/24
                      advertise: true
                    - address: 60.1.1.1
                      subnet_mask: 255.255.0.0
                      cost: 30
              afi: "ipv6"
          passive_interface: true
          vrf: "vrfmerge"
    state: overridden

# Task output:
# ------------
# before:
#     processes:
#     - areas:
#       - area_id: 0.0.0.0
#         encryption:
#           algorithm: md5
#           encryption: 'null'
#           hidden_key: true
#           passphrase: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
#           spi: 43
#       vrf: default
#     - address_family:
#       - afi: ipv6
#         areas:
#         - area_id: 0.0.0.3
#           ranges:
#           - address: 10.1.2.0/24
#           - address: 60.1.0.0/16
#             cost: 30
#       passive_interface: true
#       vrf: vrfmerge
#
# commands:
# - no router ospfv3
# - router ospfv3 vrf vrfmerge
# - address-family ipv6
# - no area 0.0.0.3 range 10.1.2.0/24
# - no area 0.0.0.3 range 60.1.0.0/16 cost 30
# - area 0.0.0.3 range 10.1.2.2/24 advertise
# - area 0.0.0.3 range 60.1.1.1 255.255.0.0 cost 30
# - exit
# - exit
#
# after:
#     processes:
#     - address_family:
#       - afi: ipv6
#         areas:
#         - area_id: 0.0.0.3
#           ranges:
#           - address: 10.1.2.0/24
#           - address: 60.1.0.0/16
#             cost: 30
#       passive_interface: true
#       vrf: vrfmerge

# After state:
# ------------
# veos#show running-config | section ospfv3
# router ospfv3 vrf vrfmerge
#    passive-interface default
#    !
#    address-family ipv6
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30

# using deleted

# Before state:
# -------------
# veos#show running-config | section ospfv3
# router ospfv3
#    area 0.0.0.0 encryption ipsec spi 43 esp null md5 passphrase 7 h8pZp9eprTYjjoY/NKFFe0Ei7x03Y7dyLotRhI0a5t4=
# !
# router ospfv3 vrf vrfmerge
#    passive-interface default
#    !
#    address-family ipv4
#       redistribute connected
#       redistribute static route-map MAP01
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30
#    !
#    address-family ipv6
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30

- name: Delete OSPFv3 config
  arista.eos.eos_ospfv3:
    config:
    state: deleted

# Task output:
# ------------

# before:
#     processes:
#     - areas:
#       - area_id: 0.0.0.0
#         encryption:
#           algorithm: md5
#           encryption: 'null'
#           hidden_key: true
#           passphrase: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
#           spi: 43
#       vrf: default
#     - address_family:
#       - afi: ipv4
#         areas:
#         - area_id: 0.0.0.3
#           ranges:
#           - address: 10.1.2.0/24
#           - address: 60.1.0.0/16
#             cost: 30
#         redistribute:
#         - routes: connected
#         - route_map: MAP01
#           routes: static
#       - afi: ipv6
#         areas:
#         - area_id: 0.0.0.3
#           ranges:
#           - address: 10.1.2.0/24
#           - address: 60.1.0.0/16
#             cost: 30
#       passive_interface: true
#       vrf: vrfmerge
#
# commands:
#
# - no router ospfv3
#
# after: {}

# After state:
# ------------
# veos#show running-config | section ospfv3
# router ospfv3 vrf vrfmerge
#    passive-interface default
#    !
#    address-family ipv4
#       redistribute connected
#       redistribute static route-map MAP01
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30
#    !
#    address-family ipv6
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30

# using parsed

# parsed_ospfv3.cfg
# router ospfv3
#    fips restrictions
#    area 0.0.0.20 stub
#    area 0.0.0.20 authentication ipsec spi 33 sha1 passphrase 7 4O8T3zo4xBdRWXBnsnK934o9SEb+jEhHUN6+xzZgCo2j9EnQBUvtwNxxLEmYmm6w
#    area 0.0.0.40 default-cost 45
#    area 0.0.0.40 stub
#    timers pacing flood 7
#    adjacency exchange-start threshold 11
#    !
#    address-family ipv4
#       fips restrictions
#       redistribute connected
#    !
#    address-family ipv6
#       router-id 10.1.1.1
#       fips restrictions
# !
# router ospfv3 vrf vrf01
#    bfd all-interfaces
#    fips restrictions
#    area 0.0.0.0 encryption ipsec spi 256 esp null sha1 passphrase 7 7hl8FV3lZ6H1mAKpjL47hQ==
#    log-adjacency-changes detail
#    !
#    address-family ipv4
#       passive-interface default
#       fips restrictions
#       redistribute connected route-map MAP01
#       maximum-paths 100
#    !
#    address-family ipv6
#       fips restrictions
#       area 0.0.0.10 nssa no-summary
#       default-information originate route-map DefaultRouteFilter
#       max-metric router-lsa external-lsa 25 summary-lsa
# !
# router ospfv3 vrf vrf02
#    fips restrictions
#    !
#    address-family ipv6
#       router-id 10.17.0.3
#       distance ospf intra-area 200
#       fips restrictions
#       area 0.0.0.1 stub
#       timers spf delay initial 56 56 56
#       timers out-delay 10

- name: Parse the provided config
  arista.eos.eos_ospfv3:
    running_config: "{{ lookup('file', './parsed_ospfv3.cfg') }}"
    state: parsed

# Task output:
# ------------
# parsed:
#     processes:
#     - address_family:
#       - afi: ipv4
#         fips_restrictions: true
#         redistribute:
#         - routes: connected
#       - afi: ipv6
#         fips_restrictions: true
#         router_id: 10.1.1.1
#       adjacency:
#         exchange_start:
#           threshold: 11
#       areas:
#       - area_id: 0.0.0.20
#         authentication:
#           algorithm: sha1
#           hidden_key: true
#           passphrase: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
#           spi: 33
#         stub:
#           set: true
#       - area_id: 0.0.0.40
#         default_cost: 45
#         stub:
#           set: true
#       fips_restrictions: true
#       timers:
#         pacing: 7
#       vrf: default
#     - address_family:
#       - afi: ipv4
#         fips_restrictions: true
#         maximum_paths: 100
#         passive_interface: true
#         redistribute:
#         - route_map: MAP01
#           routes: connected
#       - afi: ipv6
#         areas:
#         - area_id: 0.0.0.10
#           nssa:
#             no_summary: true
#         default_information:
#           originate: true
#           route_map: DefaultRouteFilter
#         fips_restrictions: true
#         max_metric:
#           router_lsa:
#             external_lsa:
#               max_metric_value: 25
#             summary_lsa:
#               set: true
#       areas:
#       - area_id: 0.0.0.0
#         encryption:
#           algorithm: sha1
#           encryption: 'null'
#           hidden_key: true
#           passphrase: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
#           spi: 256
#       bfd:
#         all_interfaces: true
#       fips_restrictions: true
#       log_adjacency_changes:
#         detail: true
#       vrf: vrf01
#     - address_family:
#       - afi: ipv6
#         areas:
#         - area_id: 0.0.0.1
#           stub:
#             set: true
#         distance: 200
#         fips_restrictions: true
#         router_id: 10.17.0.3
#         timers:
#           out_delay: 10
#           spf:
#             initial: 56
#             max: 56
#             min: 56
#       fips_restrictions: true
#       vrf: vrf02

# using gathered

# native config:
# veos#show running-config | section ospfv3
# router ospfv3 vrf vrfmerge
#    passive-interface default
#    !
#    address-family ipv4
#       redistribute connected
#       redistribute static route-map MAP01
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30
#    !
#    address-family ipv6
#       area 0.0.0.3 range 10.1.2.0/24
#       area 0.0.0.3 range 60.1.0.0/16 cost 30

- name: Gather running configuration
  arista.eos.eos_ospfv3:
    state: gathered

# Task output:
# ------------
# gathered:
#     processes:
#     - address_family:
#       - afi: ipv4
#         areas:
#         - area_id: 0.0.0.3
#           ranges:
#           - address: 10.1.2.0/24
#           - address: 60.1.0.0/16
#             cost: 30
#         redistribute:
#         - routes: connected
#         - route_map: MAP01
#           routes: static
#       - afi: ipv6
#         areas:
#         - area_id: 0.0.0.3
#           ranges:
#           - address: 10.1.2.0/24
#           - address: 60.1.0.0/16
#             cost: 30
#       passive_interface: true
#       vrf: vrfmerge

# using rendered

- name: render CLI commands for provided config
  arista.eos.eos_ospfv3:
    config:
      processes:
        - address_family:
            - timers:
                lsa: 22
              graceful_restart:
                grace_period: 35
              afi: "ipv6"
          timers:
            pacing: 55
          fips_restrictions: true
          router_id: "2.2.2.2"
          vrf: "vrfmerge"
    state: rendered

# Task output:
# ------------
# rendered:
# - router ospfv3 vrf vrfmerge
# - address-family ipv6
# - graceful-restart grace-period 35
# - timers lsa arrival 22
# - exit
# - timers pacing flood 55
# - fips restrictions
# - router-id 2.2.2.2
# - exit
```

## [Return Values](eos_ospfv3_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["router ospfv3 vrf vrfmerge", "address-family ipv6", "graceful-restart grace-period 35"]` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **parsed**  dictionary | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["router ospfv3 vrf vrfmerge", "address-family ipv6", "graceful-restart grace-period 35"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
