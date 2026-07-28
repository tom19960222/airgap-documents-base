---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_ospfv3 module – Resource module to configure OSPFv3."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_ospfv3_module.html
fetched_at: 2026-07-27T16:55:53+00:00
---
# cisco.iosxr.iosxr_ospfv3 module – Resource module to configure OSPFv3.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_ospfv3`.

New in cisco.iosxr 1.1.0

- [Synopsis](iosxr_ospfv3_module.md#synopsis)
- [Parameters](iosxr_ospfv3_module.md#parameters)
- [Notes](iosxr_ospfv3_module.md#notes)
- [Examples](iosxr_ospfv3_module.md#examples)

## [Synopsis](iosxr_ospfv3_module.md#id1)

- This module manages global ospfv3 configuration on devices running Cisco IOS-XR

## [Parameters](iosxr_ospfv3_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of ospfv3 process configuration |
| **processes**  list / elements=dictionary | A list of ospfv3 instances configuration |
| **address_family_unicast**  boolean | Enable unicast topology for ipv4 address family  Choices:   - `false` - `true` |
| **areas**  list / elements=dictionary | Configure ospfv3 areas’ properties |
| **area_id**  string / required | Area ID as IP address or integer |
| **authentication**  dictionary | Enable authentication |
| **disable**  boolean | Do not authenticate OSPFv3 packets  Choices:   - `false` ← (default) - `true` |
| **ipsec**  dictionary | Specify IPSec AH authentication attributes |
| **algorithim_type**  string | Specify the type of algorithim  Choices:   - `"md5"` - `"sha1"` |
| **clear_key**  string | Specify key in cleartext form |
| **key**  string | Specify key |
| **password_key**  string | Specify key in encrypted form |
| **spi**  integer | Specify the Security Parameter Index value |
| **bfd**  dictionary | Configure BFD parameters |
| **fast_detect**  dictionary | Configure fast detection |
| **set**  boolean | Enable fast detection only  Choices:   - `false` - `true` |
| **strict_mode**  boolean | Hold down neighbor session until BFD session is up  Choices:   - `false` - `true` |
| **minimum_interval**  integer | Hello interval in milli-seconds |
| **multiplier**  integer | Detect multiplier |
| **cost**  integer | Interface cost |
| **database_filter**  dictionary | Filter LSAs during synchronization and flooding |
| **all_outgoing_lsa**  boolean | Filter all outgoing LSA  Choices:   - `false` - `true` |
| **dead_interval**  integer | Interval after which a neighbor is declared dead |
| **default_cost**  integer | Set the summary default-cost of a NSSA/stub area. Stub’s advertised external route metric |
| **demand_circuit**  boolean | Enable/Disable ospfv3 demand circuit  Choices:   - `false` - `true` |
| **distrinbute_rib_prefix_list_name**  string | Filter LSAs during synchronization and flooding |
| **encryption**  dictionary | Encrypt and authenticate OSPFv3 packets |
| **disable**  boolean | Do not encrypt OSPFv3 packets  Choices:   - `false` ← (default) - `true` |
| **ipsec**  dictionary | Specify IPSec ESP encryption and authentication |
| **esp**  dictionary | Specify encryption parameters |
| **aes**  dictionary | This specify the aes algorithim |
| **algorithim_type**  string | Specify the bit encryption for aes algorithim  Choices:   - `"192"` - `"256"` |
| **clear_key**  string | Specify AES key in cleartext form |
| **key**  string | Cleartext AES key |
| **password_key**  string | Specify AES key in encrypted form |
| **des**  dictionary | This specify the des algorithim |
| **clear_key**  string | Specify AES key in cleartext form |
| **key**  string | Cleartext AES key |
| **password_key**  string | Specify AES key in encrypted form |
| **null_encryption**  dictionary | Specify null encryption attributes |
| **authentication**  dictionary | Specify authentication parameters |
| **algorithim_type**  string | Specify the type of algorithim  Choices:   - `"md5"` - `"sha1"` |
| **clear_key**  string | Specify key in cleartext form |
| **key**  string | Specify key |
| **password_key**  string | Specify key in encrypted form |
| **triple_des**  dictionary | This specify the triple DES algorithim |
| **clear_key**  string | Specify 3DES key in cleartext form |
| **key**  string | Cleartext 3DES key |
| **password_key**  string | Specify 3DES key in encrypted form |
| **spi**  integer | Specify the Security Parameter Index value |
| **fast_reroute**  dictionary | Specify IP Fast Reroute |
| **disabled**  boolean | Disable IP fast reroute  Choices:   - `false` - `true` |
| **per_link**  dictionary | Specify per-prefix computation |
| **information_type**  string | Specify per-link LFA exclusion or FRR LFA candidate information  Choices:   - `"exclude"` - `"lfa_candidate"` |
| **interface**  dictionary | Specify Per-link LFA exclusion information |
| **bundle_ether**  list / elements=integer | Specify Aggregated Ethernet interface(s) |
| **bvi**  list / elements=integer | Specify Bridge-Group Virtual Interface |
| **fast_ethernet**  list / elements=string | Specify FastEthernet/IEEE 802.3 interface(s) |
| **fiftygige**  list / elements=string | Specify FiftyGigE/IEEE 802.3 interface(s) |
| **fortygige**  list / elements=string | Specify FortyGigE/IEEE 802.3 interface(s) |
| **fourhundredgige**  list / elements=string | Specify FourHundredGigE/IEEE 802.3 interface(s) |
| **gigabitethernet**  list / elements=string | Specify GigabitEthernet/IEEE 802.3 interface(s) |
| **hundredgige**  list / elements=string | Specify HundredGigE/IEEE 802.3 interface(s) |
| **mgmteth**  list / elements=string | Specify MgmtEth/IEEE 802.3 interface(s) |
| **multilink**  list / elements=string | Specify Multilink network interface(s) |
| **nve**  list / elements=integer | Specify Network Virtualization Endpoint Interface(s) |
| **pos_int**  list / elements=integer | Specify Aggregated pos interface(s) |
| **pw_ether**  list / elements=integer | Specify PWHE Ethernet Interface |
| **pw_iw**  list / elements=integer | Specify PWHE VC11 IP Interworking Interface |
| **serial**  list / elements=string | Specify Serial network interface(s) |
| **srp**  list / elements=string | Specify SRP interface(s) |
| **tengige**  list / elements=string | Specify TenGigabitEthernet/IEEE 802.3 interface(s) |
| **tunnel_ip**  list / elements=integer | Specify GRE/IPinIP Tunnel Interface(s) |
| **tunnel_ipsec**  list / elements=integer | Specify IPSec Tunnel interface(s) |
| **tunnel_mpls**  integer | MPLS Transport Protocol Tunnel interface |
| **tunnel_mte**  list / elements=integer | Specify MPLS Traffic Engineering P2MP Tunnel interface(s) |
| **twentyfivegige**  list / elements=string | Specify TwentyFiveGigabitEthernet/IEEE 802.3 interface(s) |
| **twohundredgige**  list / elements=string | Specify TwoHundredGigE/IEEE 802.3 interface(s) |
| **use_candidate_only**  boolean | Enable/Disable backup selection from candidate-list only  Choices:   - `false` - `true` |
| **per_prefix**  dictionary | Specify per-prefix computation |
| **information_type**  string | Specify per_prefix LFA exclusion or FRR LFA candidate information  Choices:   - `"exclude"` - `"lfa_candidate"` |
| **interface**  dictionary | Specify Per-link LFA exclusion information |
| **bundle_ether**  list / elements=integer | Specify Aggregated Ethernet interface(s) |
| **bvi**  list / elements=integer | Specify Bridge-Group Virtual Interface |
| **fast_ethernet**  list / elements=string | Specify FastEthernet/IEEE 802.3 interface(s) |
| **fiftygige**  list / elements=string | Specify FiftyGigE/IEEE 802.3 interface(s) |
| **fortygige**  list / elements=string | Specify FortyGigE/IEEE 802.3 interface(s) |
| **fourhundredgige**  list / elements=string | Specify FourHundredGigE/IEEE 802.3 interface(s) |
| **gigabitethernet**  list / elements=string | Specify GigabitEthernet/IEEE 802.3 interface(s) |
| **hundredgige**  list / elements=string | Specify HundredGigE/IEEE 802.3 interface(s) |
| **mgmteth**  list / elements=string | Specify MgmtEth/IEEE 802.3 interface(s) |
| **multilink**  list / elements=string | Specify Multilink network interface(s) |
| **nve**  list / elements=integer | Specify Network Virtualization Endpoint Interface(s) |
| **pos_int**  list / elements=integer | Specify Aggregated pos interface(s) |
| **pw_ether**  list / elements=integer | Specify PWHE Ethernet Interface |
| **pw_iw**  list / elements=integer | Specify PWHE VC11 IP Interworking Interface |
| **serial**  list / elements=string | Specify Serial network interface(s) |
| **srp**  list / elements=string | Specify SRP interface(s) |
| **tengige**  list / elements=string | Specify TenGigabitEthernet/IEEE 802.3 interface(s) |
| **tunnel_ip**  list / elements=integer | Specify GRE/IPinIP Tunnel Interface(s) |
| **tunnel_ipsec**  list / elements=integer | Specify IPSec Tunnel interface(s) |
| **tunnel_mpls**  integer | MPLS Transport Protocol Tunnel interface |
| **tunnel_mte**  list / elements=integer | Specify MPLS Traffic Engineering P2MP Tunnel interface(s) |
| **twentyfivegige**  list / elements=string | Specify TwentyFiveGigabitEthernet/IEEE 802.3 interface(s) |
| **twohundredgige**  list / elements=string | Specify TwoHundredGigE/IEEE 802.3 interface(s) |
| **use_candidate_only**  boolean | Enable/Disable backup selection from candidate-list only  Choices:   - `false` - `true` |
| **flood_reduction**  boolean | Enable/Disable flood reduction  Choices:   - `false` - `true` |
| **hello_interval**  integer | Specify Time between HELLO packets |
| **instance_id**  integer | Specify instance ID |
| **mpls_ldp_sync**  boolean | Enable/Disable MPLS LDP Sync  Choices:   - `false` - `true` |
| **mtu_ignore**  boolean | Enable/Disable ignoring of MTU in DBD packets  Choices:   - `false` - `true` |
| **network**  string | Specify Network type  Choices:   - `"broadcast"` - `"non-broadcast"` - `"point-to-multipoint"` - `"point-to-point"` |
| **nssa**  dictionary | NSSA settings for the area |
| **default_information_originate**  dictionary | Originate default Type 7 LSA |
| **metric**  integer | ospfv3 default metric |
| **metric_type**  integer | Metric type for default routes |
| **set**  boolean | Set nssa to default information originate  Choices:   - `false` - `true` |
| **no_redistribution**  boolean | Do not send redistributed LSAs into NSSA area  Choices:   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSAs into NSSA area  Choices:   - `false` - `true` |
| **set**  boolean | Configure area as NSSA  Choices:   - `false` - `true` |
| **translate**  dictionary | Translate LSA |
| **type7**  dictionary | Translate from Type 7 to Type 5 |
| **always**  boolean / required | Always translate LSAs  Choices:   - `false` - `true` |
| **packet_size**  integer | Specify limit size of OSPFv3 packets |
| **passive**  boolean | Enable/Disable routing updates on an interface  Choices:   - `false` - `true` |
| **prefix_suppression**  boolean | Hide all transit addresses on this interface  Choices:   - `false` - `true` |
| **priority**  integer | Specify Router priority |
| **ranges**  list / elements=dictionary | Summarize routes matching address/mask (border routers only) |
| **address**  string / required | IP in Prefix format (X:X::X/length) |
| **advertise**  boolean | Advertise this range (default)  Choices:   - `false` - `true` |
| **cost**  integer | Specify user specified metric for this range |
| **not_advertise**  boolean | DoNotAdvertise this range  Choices:   - `false` - `true` |
| **retransmit_interval**  integer | Specify Delay between LSA retransmissions |
| **stub**  dictionary | Settings for configuring the area as a stub |
| **no_summary**  boolean | Do not send summary LSA into stub area  Choices:   - `false` - `true` |
| **set**  boolean | Configure the area as a stub  Choices:   - `false` - `true` |
| **transmit_delay**  integer | Specify estimated time needed to send link-state update packet |
| **virtual_link**  list / elements=dictionary | Define a virtual link |
| **authentication**  dictionary | Enable authentication |
| **disable**  boolean | Do not authenticate OSPFv3 packets  Choices:   - `false` ← (default) - `true` |
| **ipsec**  dictionary | Specify IPSec AH authentication attributes |
| **algorithim_type**  string | Specify the type of algorithim  Choices:   - `"md5"` - `"sha1"` |
| **clear_key**  string | Specify key in cleartext form |
| **key**  string | Specify key |
| **password_key**  string | Specify key in encrypted form |
| **spi**  integer | Specify the Security Parameter Index value |
| **dead_interval**  integer | Interval after which a neighbor is declared dead |
| **encryption**  dictionary | Encrypt and authenticate OSPFv3 packets |
| **disable**  boolean | Do not encrypt OSPFv3 packets  Choices:   - `false` ← (default) - `true` |
| **ipsec**  dictionary | Specify IPSec ESP encryption and authentication |
| **esp**  dictionary | Specify encryption parameters |
| **aes**  dictionary | This specify the aes algorithim |
| **algorithim_type**  string | Specify the bit encryption for aes algorithim  Choices:   - `"192"` - `"256"` |
| **clear_key**  string | Specify AES key in cleartext form |
| **key**  string | Cleartext AES key |
| **password_key**  string | Specify AES key in encrypted form |
| **des**  dictionary | This specify the des algorithim |
| **clear_key**  string | Specify AES key in cleartext form |
| **key**  string | Cleartext AES key |
| **password_key**  string | Specify AES key in encrypted form |
| **null_encryption**  dictionary | Specify null encryption attributes |
| **authentication**  dictionary | Specify authentication parameters |
| **algorithim_type**  string | Specify the type of algorithim  Choices:   - `"md5"` - `"sha1"` |
| **clear_key**  string | Specify key in cleartext form |
| **key**  string | Specify key |
| **password_key**  string | Specify key in encrypted form |
| **triple_des**  dictionary | This specify the triple DES algorithim |
| **clear_key**  string | Specify 3DES key in cleartext form |
| **key**  string | Cleartext 3DES key |
| **password_key**  string | Specify 3DES key in encrypted form |
| **spi**  integer | Specify the Security Parameter Index value |
| **hello_interval**  integer | Time between HELLO packets |
| **id**  string / required | Router-ID of virtual link neighbor (A.B.C.D) |
| **retransmit_interval**  integer | Delay between LSA retransmissions |
| **transmit_delay**  integer | Link state transmit delay |
| **authentication**  dictionary | Enable authentication |
| **disable**  boolean | Do not authenticate OSPFv3 packets  Choices:   - `false` ← (default) - `true` |
| **ipsec**  dictionary | Specify IPSec AH authentication attributes |
| **algorithim_type**  string | Specify the type of algorithim  Choices:   - `"md5"` - `"sha1"` |
| **clear_key**  string | Specify key in cleartext form |
| **key**  string | Specify key |
| **password_key**  string | Specify key in encrypted form |
| **spi**  integer | Specify the Security Parameter Index value |
| **auto_cost**  dictionary | Calculate ospfv3 interface cost according to bandwidth |
| **disable**  boolean | Assign ospfv3 cost based on interface type  Choices:   - `false` - `true` |
| **reference_bandwidth**  integer | Specify reference bandwidth in megabits per sec |
| **bfd**  dictionary | Configure BFD parameters |
| **fast_detect**  dictionary | Configure fast detection |
| **set**  boolean | Enable fast detection only  Choices:   - `false` - `true` |
| **strict_mode**  boolean | Hold down neighbor session until BFD session is up  Choices:   - `false` - `true` |
| **minimum_interval**  integer | Hello interval in milli-seconds |
| **multiplier**  integer | Detect multiplier |
| **capability**  dictionary | Enable specific OSPFv3 feature |
| **type7**  dictionary | Specify type7 nssa capability |
| **prefer**  boolean | Prefer type7 externals over type5  Choices:   - `false` - `true` |
| **translate**  boolean | Translate type7 to type5  Choices:   - `false` - `true` |
| **cost**  integer | Specify Interface cost |
| **database_filter**  dictionary | Filter LSAs during synchronization and flooding |
| **all_outgoing_lsa**  boolean | Filter all outgoing LSA  Choices:   - `false` - `true` |
| **dead_interval**  integer | Interval after which a neighbor is declared dead |
| **default_information_originate**  dictionary | Control distribution of default information |
| **always**  boolean | Always advertise default route  Choices:   - `false` - `true` |
| **metric**  integer | ospfv3 default metric |
| **metric_type**  integer | ospfv3 metric type for default routes |
| **route_policy**  string | Apply route-policy to default-information origination |
| **set**  boolean | Enable distribution of default route  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for default route |
| **default_metric**  integer | Set metric of redistributed routes |
| **demand_circuit**  boolean | Enable/Disable ospfv3 demand circuit  Choices:   - `false` - `true` |
| **distance**  dictionary | Define an administrative distance |
| **admin_distance**  integer | Administrative distance |
| **ospfv3_distance**  dictionary | ospfv3 administrative distance |
| **external**  integer | Distance for external routes |
| **inter_area**  integer | Distance for inter-area routes |
| **intra_area**  integer | Distance for intra-area routes |
| **distribute_list**  dictionary | Filter prefixes to/from RIB |
| **prefix_list**  list / elements=string | Filter prefixes based on an IPv6 prefix-list |
| **in**  boolean | Filter prefixes installed to RIB  Choices:   - `false` - `true` |
| **name**  string | Specify Prefix-list name |
| **out**  boolean | Filter prefixes redistributed from RIB  Choices:   - `false` - `true` |
| **encryption**  dictionary | Encrypt and authenticate OSPFv3 packets |
| **disable**  boolean | Do not encrypt OSPFv3 packets  Choices:   - `false` ← (default) - `true` |
| **ipsec**  dictionary | Specify IPSec ESP encryption and authentication |
| **esp**  dictionary | Specify encryption parameters |
| **aes**  dictionary | This specify the aes algorithim |
| **algorithim_type**  string | Specify the bit encryption for aes algorithim  Choices:   - `"192"` - `"256"` |
| **clear_key**  string | Specify AES key in cleartext form |
| **key**  string | Cleartext AES key |
| **password_key**  string | Specify AES key in encrypted form |
| **des**  dictionary | This specify the des algorithim |
| **clear_key**  string | Specify AES key in cleartext form |
| **key**  string | Cleartext AES key |
| **password_key**  string | Specify AES key in encrypted form |
| **null_encryption**  dictionary | Specify null encryption attributes |
| **authentication**  dictionary | Specify authentication parameters |
| **algorithim_type**  string | Specify the type of algorithim  Choices:   - `"md5"` - `"sha1"` |
| **clear_key**  string | Specify key in cleartext form |
| **key**  string | Specify key |
| **password_key**  string | Specify key in encrypted form |
| **triple_des**  dictionary | This specify the triple DES algorithim |
| **clear_key**  string | Specify 3DES key in cleartext form |
| **key**  string | Cleartext 3DES key |
| **password_key**  string | Specify 3DES key in encrypted form |
| **spi**  integer | Specify the Security Parameter Index value |
| **fast_reroute**  dictionary | Specify IP Fast Reroute |
| **disabled**  boolean | Disable IP fast reroute  Choices:   - `false` - `true` |
| **per_link**  dictionary | Specify per-prefix computation |
| **information_type**  string | Specify per-link LFA exclusion or FRR LFA candidate information  Choices:   - `"exclude"` - `"lfa_candidate"` |
| **interface**  dictionary | Specify Per-link LFA exclusion information |
| **bundle_ether**  list / elements=integer | Specify Aggregated Ethernet interface(s) |
| **bvi**  list / elements=integer | Specify Bridge-Group Virtual Interface |
| **fast_ethernet**  list / elements=string | Specify FastEthernet/IEEE 802.3 interface(s) |
| **fiftygige**  list / elements=string | Specify FiftyGigE/IEEE 802.3 interface(s) |
| **fortygige**  list / elements=string | Specify FortyGigE/IEEE 802.3 interface(s) |
| **fourhundredgige**  list / elements=string | Specify FourHundredGigE/IEEE 802.3 interface(s) |
| **gigabitethernet**  list / elements=string | Specify GigabitEthernet/IEEE 802.3 interface(s) |
| **hundredgige**  list / elements=string | Specify HundredGigE/IEEE 802.3 interface(s) |
| **mgmteth**  list / elements=string | Specify MgmtEth/IEEE 802.3 interface(s) |
| **multilink**  list / elements=string | Specify Multilink network interface(s) |
| **nve**  list / elements=integer | Specify Network Virtualization Endpoint Interface(s) |
| **pos_int**  list / elements=integer | Specify Aggregated pos interface(s) |
| **pw_ether**  list / elements=integer | Specify PWHE Ethernet Interface |
| **pw_iw**  list / elements=integer | Specify PWHE VC11 IP Interworking Interface |
| **serial**  list / elements=string | Specify Serial network interface(s) |
| **srp**  list / elements=string | Specify SRP interface(s) |
| **tengige**  list / elements=string | Specify TenGigabitEthernet/IEEE 802.3 interface(s) |
| **tunnel_ip**  list / elements=integer | Specify GRE/IPinIP Tunnel Interface(s) |
| **tunnel_ipsec**  list / elements=integer | Specify IPSec Tunnel interface(s) |
| **tunnel_mpls**  integer | MPLS Transport Protocol Tunnel interface |
| **tunnel_mte**  list / elements=integer | Specify MPLS Traffic Engineering P2MP Tunnel interface(s) |
| **twentyfivegige**  list / elements=string | Specify TwentyFiveGigabitEthernet/IEEE 802.3 interface(s) |
| **twohundredgige**  list / elements=string | Specify TwoHundredGigE/IEEE 802.3 interface(s) |
| **use_candidate_only**  boolean | Enable/Disable backup selection from candidate-list only  Choices:   - `false` - `true` |
| **per_prefix**  dictionary | Specify per-prefix computation |
| **information_type**  string | Specify per_prefix LFA exclusion or FRR LFA candidate information  Choices:   - `"exclude"` - `"lfa_candidate"` |
| **interface**  dictionary | Specify Per-link LFA exclusion information |
| **bundle_ether**  list / elements=integer | Specify Aggregated Ethernet interface(s) |
| **bvi**  list / elements=integer | Specify Bridge-Group Virtual Interface |
| **fast_ethernet**  list / elements=string | Specify FastEthernet/IEEE 802.3 interface(s) |
| **fiftygige**  list / elements=string | Specify FiftyGigE/IEEE 802.3 interface(s) |
| **fortygige**  list / elements=string | Specify FortyGigE/IEEE 802.3 interface(s) |
| **fourhundredgige**  list / elements=string | Specify FourHundredGigE/IEEE 802.3 interface(s) |
| **gigabitethernet**  list / elements=string | Specify GigabitEthernet/IEEE 802.3 interface(s) |
| **hundredgige**  list / elements=string | Specify HundredGigE/IEEE 802.3 interface(s) |
| **mgmteth**  list / elements=string | Specify MgmtEth/IEEE 802.3 interface(s) |
| **multilink**  list / elements=string | Specify Multilink network interface(s) |
| **nve**  list / elements=integer | Specify Network Virtualization Endpoint Interface(s) |
| **post_int**  list / elements=integer | Specify Aggregated pos interface(s) |
| **pw_ether**  list / elements=integer | Specify PWHE Ethernet Interface |
| **pw_iw**  list / elements=integer | Specify PWHE VC11 IP Interworking Interface |
| **serial**  list / elements=string | Specify Serial network interface(s) |
| **srp**  list / elements=string | Specify SRP interface(s) |
| **tengige**  list / elements=string | Specify TenGigabitEthernet/IEEE 802.3 interface(s) |
| **tunnel_ip**  list / elements=integer | Specify GRE/IPinIP Tunnel Interface(s) |
| **tunnel_ipsec**  list / elements=integer | Specify IPSec Tunnel interface(s) |
| **tunnel_mpls**  integer | MPLS Transport Protocol Tunnel interface |
| **tunnel_mte**  list / elements=integer | Specify MPLS Traffic Engineering P2MP Tunnel interface(s) |
| **twentyfivegige**  list / elements=string | Specify TwentyFiveGigabitEthernet/IEEE 802.3 interface(s) |
| **twohundredgige**  list / elements=string | Specify TwoHundredGigE/IEEE 802.3 interface(s) |
| **use_candidate_only**  boolean | Enable/Disable backup selection from candidate-list only  Choices:   - `false` - `true` |
| **flood_reduction**  boolean | Enable/Disable flood reduction  Choices:   - `false` - `true` |
| **graceful_restart**  dictionary | Enable Graceful-Restart |
| **helper_disable**  boolean | Disable router’s helper support level  Choices:   - `false` - `true` |
| **max_interval**  integer | Maximum route lifetime following restart |
| **min_interval**  integer | Minimum interval between Graceful Restarts |
| **set**  boolean | Set graceful restart  Choices:   - `false` - `true` |
| **hello_interval**  integer | Specify Time between HELLO packets |
| **ignore_mospf_type6_lsa**  boolean | Ignore MOSPF Type 6 LSA  Choices:   - `false` - `true` |
| **instance_id**  integer | Specify instance ID |
| **log_adjacency_changes**  dictionary | Log adjacency state changes |
| **detail**  boolean | Log all state changes  Choices:   - `false` - `true` |
| **disable**  boolean | Disable log adjacency changes  Choices:   - `false` - `true` |
| **set**  boolean | Set log adjacency  Choices:   - `false` - `true` |
| **maximum**  dictionary | Set OSPFv3 limits |
| **interfaces**  integer | Specify limit for number of interfaces |
| **paths**  integer | Specify limit for number of paths |
| **redistributed_prefixes**  integer | Specify limit for number of redistributed prefixes |
| **mpls_ldp_sync**  boolean | Enable/Disable MPLS LDP Sync  Choices:   - `false` - `true` |
| **mtu_ignore**  boolean | Enable/Disable ignoring of MTU in DBD packets  Choices:   - `false` - `true` |
| **network**  string | Specify Network type  Choices:   - `"broadcast"` - `"non-broadcast"` - `"point-to-multipoint"` - `"point-to-point"` |
| **nsr**  boolean | Enable/Disable NSR for all VRFs in this process  Choices:   - `false` - `true` |
| **packet_size**  integer | Specify limit size of OSPFv3 packets |
| **passive**  boolean | Enable/Disable routing updates on an interface  Choices:   - `false` - `true` |
| **prefix_suppression**  boolean | Hide all transit addresses on this interface  Choices:   - `false` - `true` |
| **priority**  integer | Specify Router priority |
| **process_id**  string / required | The OSPFv3 Process ID |
| **protocol_shutdown**  boolean | Gracefully shutdown the OSPFv3 protocol  Choices:   - `false` - `true` |
| **redistribute**  dictionary | Redistribute information from another routing Protocol |
| **application**  list / elements=dictionary | Specify application routes |
| **id**  string / required | OnePK Application name |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set application route  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **bgp**  list / elements=dictionary | Specify bgp routes |
| **id**  integer / required | BGP process name |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **preserved_med**  string | Specify preserve med of BGP routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set bgp route number  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **connected**  dictionary | Specify connected routes |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set connected route  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **eigrp**  list / elements=dictionary | Specify eigrp routes |
| **id**  integer / required | EIGRP process name |
| **match**  string | Redistribution of EIGRP routes  Choices:   - `"external"` - `"internal"` |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set bgp route number  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **isis**  list / elements=dictionary | Specify IS-IS routes |
| **id**  string / required | IS-IS name |
| **level**  string | Specify IS-IS level routes  Choices:   - `"level-1"` - `"level-1-2"` - `"level-2"` |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set IS-IS route number  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **mobile**  dictionary | Specify mobile routes |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set mobile route number  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **ospfv3**  list / elements=dictionary | Specify ospfv3 routes |
| **id**  string / required | OSPFv3 process name |
| **match**  dictionary | Redistribution of OSPFv3 routes |
| **external**  integer | Redistribute OSPFv3 external routes  Choices:   - `1` - `2` |
| **internal**  boolean | Redistribute OSPFv3 internal routes  Choices:   - `false` - `true` |
| **nssa_external**  integer | Redistribute NSSA OSPFv3 external routes  Choices:   - `1` - `2` |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set ospfv3 route number  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **static**  dictionary | Specify static routes |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set static route  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **subscriber**  dictionary | Specify subscriber routes |
| **metric**  integer | Specify metric for redistributed routes |
| **metric_type**  integer | Specify OSPFv3 exterior metric type for redistributed routes |
| **route_policy**  string | Apply route policy to redistribution |
| **set**  boolean | Set static route  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for routes redistributed into OSPFv3 |
| **retransmit_interval**  integer | Delay between LSA retransmissions |
| **router_id**  string | ospfv3 router-id in IPv4 address format (A.B.C.D) |
| **spf_prefix_priority**  dictionary | Specify SPF configuration |
| **disable**  boolean | Disable SPF prefix priority  Choices:   - `false` - `true` |
| **route_policy**  list / elements=dictionary | Specify the route-policy to prioritize route install |
| **name**  string | Specify name of the policy |
| **value**  string | Specify parameter values for the policy () |
| **stub_router**  dictionary | Enter stub router configuration submode |
| **router_lsa**  dictionary | Modify self originated router LSAs |
| **advertise_with**  string | Advertise LSAs with specified type  Choices:   - `"max-metric"` - `"r-bit"` - `"v6-bit"` |
| **always**  boolean | Force ospfv3 stub router mode unconditionally  Choices:   - `false` - `true` |
| **external_lsa**  dictionary | Override External LSA metric in stub router mode |
| **metric**  integer | Metric to use while in stub router mode |
| **set**  boolean | Set external lsa  Choices:   - `false` - `true` |
| **include_stub**  boolean | Set maximum metric for stub links in stub router mode  Choices:   - `false` - `true` |
| **on_proc_migration**  integer | Enter stub router mode on ospfv3 process migration |
| **on_proc_restart**  integer | Enter stub router mode on ospfv3 process restart |
| **on_startup**  dictionary | Enter stub router mode on startup |
| **time**  integer | Time in seconds to stay in stub router mode |
| **wait_for_bgp**  boolean | Exit stub router mode when BGP converges  Choices:   - `false` - `true` |
| **on_switchover**  integer | Enter stub router mode on RP switchover |
| **summary_lsa**  dictionary | Override Summary LSA metric in stub router mode |
| **metric**  integer | Metric to use while in stub router mode |
| **set**  boolean | Enable summary LSA  Choices:   - `false` - `true` |
| **summary_prefix**  list / elements=dictionary | Configure IP address summaries |
| **not_advertise**  boolean | Suppress routes that match the specified prefix/mask pair  Choices:   - `false` - `true` |
| **prefix**  string / required | IP summary address/mask (A.B.C.D/prefix) |
| **tag**  integer | Set tag |
| **timers**  dictionary | Adjust routing timers |
| **lsa_arrival**  integer | Specify LSA arrival timers |
| **pacing**  dictionary | Specify pacing timers |
| **flood**  integer | Flood pacing timer |
| **lsa_group**  integer | LSA group pacing timer |
| **retransmission**  integer | LSA group pacing timer |
| **throttle**  dictionary | Adjust throttle timers |
| **lsa**  dictionary | Specify LSA throttle timers |
| **all_lsa_initial**  integer | Delay to generate first occurrence of LSA in milliseconds |
| **all_lsa_minimum**  integer | Minimum delay between originating the same LSA in milliseconds |
| **spf**  dictionary | Specify SPF throttle timers |
| **spf_initial**  integer | Delay to generate first occurrence of SPF in ms |
| **spf_minimum**  integer | Minimum delay between originating the same SPF in ms |
| **trace**  dictionary | Specify OSPF tracing options |
| **size**  string | Delete existing buffer and create one with N entries |
| **value**  integer | Specify trace entry |
| **transmit_delay**  integer | Estimated time needed to send link-state update packet |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config router ospfv3**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](iosxr_ospfv3_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md)

## [Examples](iosxr_ospfv3_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# RP/0/RP0/CPU0:anton#show running-config router ospfv3
# Thu Jun 11 15:54:44.569 UTC
# % No such configuration item(s)
#

- name: Merge provided OSPFv3 configuration with the existing configuration
  cisco.iosxr.iosxr_ospfv3:
    config:
      processes:
        - process_id: 27
          areas:
            - area_id: 10
              hello_interval: 2
        - process_id: 26
          authentication:
            disable: true
        - process_id: 10
          areas:
            - area_id: 11
              default_cost: 5
              cost: 11
            - area_id: 22
              default_cost: 6
        - process_id: 30
          areas:
            - area_id: 11
              default_cost: 5
            - area_id: 22
              default_cost: 6
          cost: 2
          default_metric: 10
          transmit_delay: 2
          hello_interval: 1
          dead_interval: 2
          retransmit_interval: 2
          packet_size: 577
          priority: 1
          router_id: '2.2.2.2'
          demand_circuit: true
          mtu_ignore: true
    state: merged

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {}
#
#  "commands": [
#         "router ospfv3 10",
#         "area 11 default-cost 5",
#         "area 11 cost 11",
#         "area 22 default-cost 6",
#         "router ospfv3 26",
#         "authentication disable",
#         "router ospfv3 27",
#         "area 10 hello-interval 2",
#         "router ospfv3 30",
#         "cost 2",
#         "priority 1",
#         "default-metric 10",
#         "router-id 2.2.2.2",
#         "demand-circuit",
#         "packet-size 577",
#         "transmit-delay 2",
#         "dead-interval 2",
#         "hello-interval 1",
#         "retransmit-interval 2",
#         "mtu-ignore",
#         "area 11 default-cost 5",
#         "area 22 default-cost 6"
#    ]
#
#  "after": {
#         "processes": [
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "cost": 11,
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "process_id": "10"
#             },
#             {
#                 "authentication": {
#                     "disable": true
#                 },
#                 "process_id": "26"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 2
#                     }
#                 ],
#                 "process_id": "27"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "cost": 2,
#                 "dead_interval": 2,
#                 "default_metric": 10,
#                 "demand_circuit": true,
#                 "hello_interval": 1,
#                 "mtu_ignore": true,
#                 "packet_size": 577,
#                 "priority": 1,
#                 "process_id": "30",
#                 "retransmit_interval": 2,
#                 "router_id": "2.2.2.2",
#                 "transmit_delay": 2
#             }
#         ]
#     }
#
#
# ------------
# After state
# ------------
#
# RP/0/RP0/CPU0:anton#show running-config router ospfv3
# router ospfv3 10
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospfv3 26
#  authentication disable
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#  !
#  area 30
#  !
# !
# router ospfv3 30
#  cost 2
#  priority 1
#  mtu-ignore
#  packet-size 577
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit
#  hello-interval 1
#  transmit-delay 2
#  router-id 2.2.2.2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# router ospfv3 10
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospfv3 26
#  authentication disable
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#  !
#  area 30
#  !
# !
# router ospfv3 30
#  cost 2
#  priority 1
#  mtu-ignore
#  packet-size 577
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit
#  hello-interval 1
#  transmit-delay 2
#  router-id 2.2.2.2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !

# Using replaced
#
# ------------
# Before state
# ------------
#
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# router ospfv3 10
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospfv3 26
#  authentication disable
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#  !
#  area 30
#  !
# !
# router ospfv3 30
#  cost 2
#  priority 1
#  mtu-ignore
#  packet-size 577
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit
#  hello-interval 1
#  transmit-delay 2
#  router-id 2.2.2.2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# router ospfv3 10
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospfv3 26
#  authentication disable
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#  !
#  area 30
#  !
# !
# router ospfv3 30
#  cost 2
#  priority 1
#  mtu-ignore
#  packet-size 577
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit
#  hello-interval 1
#  transmit-delay 2
#  router-id 2.2.2.2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !

- name: Replace OSPFv3 routes configurations from the device
  cisco.iosxr.iosxr_ospfv3:
    config:
      processes:
        - process_id: 27
          areas:
            - area_id: 10
              hello_interval: 2
            - area_id: 20
              cost: 2
              default_cost: 2
        - process_id: 26
          authentication:
            disable: true
    state: replaced

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {
#         "processes": [
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "cost": 11,
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "process_id": "10"
#             },
#             {
#                 "authentication": {
#                     "disable": true
#                 },
#                 "process_id": "26"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 2
#                     }
#                 ],
#                 "process_id": "27"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "cost": 2,
#                 "dead_interval": 2,
#                 "default_metric": 10,
#                 "demand_circuit": true,
#                 "hello_interval": 1,
#                 "mtu_ignore": true,
#                 "packet_size": 577,
#                 "priority": 1,
#                 "process_id": "30",
#                 "retransmit_interval": 2,
#                 "router_id": "2.2.2.2",
#                 "transmit_delay": 2
#             }
#         ]
#     }
#
#  "commands": [
#         "router ospfv3 27",
#         "area 20 default-cost 2",
#         "area 20 cost 2"
#     ]
#
#  "after": {
#         "processes": [
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "cost": 11,
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "process_id": "10"
#             },
#             {
#                 "authentication": {
#                     "disable": true
#                 },
#                 "process_id": "26"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 2
#                     },
#                     {
#                         "area_id": "20",
#                         "cost": 2,
#                         "default_cost": 2
#                     }
#                 ],
#                 "process_id": "27"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "cost": 2,
#                 "dead_interval": 2,
#                 "default_metric": 10,
#                 "demand_circuit": true,
#                 "hello_interval": 1,
#                 "mtu_ignore": true,
#                 "packet_size": 577,
#                 "priority": 1,
#                 "process_id": "30",
#                 "retransmit_interval": 2,
#                 "router_id": "2.2.2.2",
#                 "transmit_delay": 2
#             }
#         ]
#     }
#
#
# -----------
# After state
# -----------
#
# RP/0/RP0/CPU0:anton(config)#do show running-config router ospfv3
# router ospfv3 10
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospfv3 26
#  authentication disable
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#   cost 2
#   default-cost 2
#  !
#  area 30
#  !
# !
# router ospfv3 30
#  cost 2
#  priority 1
#  mtu-ignore
#  packet-size 577
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit
#  hello-interval 1
#  transmit-delay 2
#  router-id 2.2.2.2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !

- name: Override existing OSPFv3 configurations from the device
  cisco.iosxr.iosxr_ospfv3:
    config:
      processes:
        - process_id: 27
          areas:
            - area_id: 10
              hello_interval: 2
              authentication:
                disable: true
            - area_id: 20
              cost: 2
              default_cost: 2
              authentication:
                disable: true
        - process_id: 26
          areas:
            - area_id: 10
              hello_interval: 2
              authentication:
                disable: true
    state: overridden

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {
#         "processes": [
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "cost": 11,
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "process_id": "10"
#             },
#             {
#                 "authentication": {
#                     "disable": true
#                 },
#                 "process_id": "26"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 2
#                     },
#                     {
#                         "area_id": "20",
#                         "cost": 2,
#                         "default_cost": 2
#                     }
#                 ],
#                 "process_id": "27"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "cost": 2,
#                 "dead_interval": 2,
#                 "default_metric": 10,
#                 "demand_circuit": true,
#                 "hello_interval": 1,
#                 "mtu_ignore": true,
#                 "packet_size": 577,
#                 "priority": 1,
#                 "process_id": "30",
#                 "retransmit_interval": 2,
#                 "router_id": "2.2.2.2",
#                 "transmit_delay": 2
#             }
#         ]
#     }
#
#  "commands": [
#         "router ospfv3 10",
#         "no area 11 default-cost 5",
#         "no area 11 cost 11",
#         "no area 22 default-cost 6",
#         "router ospfv3 30",
#         "no cost 2",
#         "no priority 1",
#         "no default-metric 10",
#         "no router-id 2.2.2.2",
#         "no demand-circuit",
#         "no packet-size 577",
#         "no transmit-delay 2",
#         "no dead-interval 2",
#         "no hello-interval 1",
#         "no retransmit-interval 2",
#         "no mtu-ignore",
#         "no area 11 default-cost 5",
#         "no area 22 default-cost 6",
#         "router ospfv3 26",
#         "area 10 hello-interval 4"
#     ]
#
#  "after": {
#         "processes": [
#             {
#                 "process_id": "10"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 4
#                     }
#                 ],
#                 "authentication": {
#                     "disable": true
#                 },
#                 "process_id": "26"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 2
#                     },
#                     {
#                         "area_id": "20",
#                         "cost": 2,
#                         "default_cost": 2
#                     }
#                 ],
#                 "process_id": "27"
#             },
#             {
#                 "process_id": "30"
#             }
#         ]
#     }
#
#
# -----------
# After state
# -----------
#
# RP/0/RP0/CPU0:anton#show running-config router ospfv3
# router ospfv3 10
#  area 11
#  !
#  area 22
#  !
# !
# router ospfv3 26
#  authentication disable
#  area 10
#   hello-interval 4
#  !
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#   cost 2
#   default-cost 2
#  !
#  area 30
#  !
# !
# router ospfv3 30
#  area 11
#  !
#  area 22
#  !
# !

# Using deleted
#
# ------------
# Before state
# ------------
#
#
# RP/0/RP0/CPU0:anton#show running-config router ospfv3
# router ospfv3 10
#  area 11
#  !
#  area 22
#  !
# !
# router ospfv3 26
#  authentication disable
#  area 10
#   hello-interval 4
#  !
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#   cost 2
#   default-cost 2
#  !
#  area 30
#  !
# !
# router ospfv3 30
#  area 11
#  !
#  area 22
#  !
# !

- name: Deleted existing OSPFv3 configurations from the device
  cisco.iosxr.iosxr_ospfv3:
    config:
      processes:
      - process_id: '10'
      - process_id: '26'
      - process_id: '27'
      - process_id: '30'
    state: deleted

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {
#         "processes": [
#             {
#                 "process_id": "10"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 4
#                     }
#                 ],
#                 "authentication": {
#                     "disable": true
#                 },
#                 "process_id": "26"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 2
#                     },
#                     {
#                         "area_id": "20",
#                         "cost": 2,
#                         "default_cost": 2
#                     }
#                 ],
#                 "process_id": "27"
#             },
#             {
#                 "process_id": "30"
#             }
#         ]
#     },
#
#  "commands": [
#         "router ospfv3 26",
#         "no authentication disable",
#         "no area 10 hello-interval 4",
#         "router ospfv3 27",
#         "no area 10 hello-interval 2",
#         "no area 20 default-cost 2",
#         "no area 20 cost 2"
#     ]
#
#  "after": {
#        "processes": [
#            {
#                "process_id": "10"
#            },
#            {
#                "process_id": "26"
#            },
#            {
#                "process_id": "27"
#            },
#            {
#                "process_id": "30"
#            }
#        ]
#    }
#
#
# -----------
# After state
# -----------
#
# RP/0/RP0/CPU0:anton(config)#show running-config router ospfv3
# router ospfv3 10
# !
# router ospfv3 26
# !
# router ospfv3 27
# !
# router ospfv3 30
# !

# Using parsed
# parsed.cfg
# ------------
# router ospfv3 10
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospfv3 26
#  authentication disable
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
# !
# router ospfv3 30
#  router-id 2.2.2.2
#  cost 2
#  packet-size 577
#  priority 1
#  mtu-ignore
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit
#  hello-interval 1
#  transmit-delay 2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
- name: Parsed the device configuration to get output commands
  cisco.iosxr.iosxr_ospfv3:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#         "processes": [
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "cost": 11,
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "process_id": "10"
#             },
#             {
#                 "authentication": {
#                     "disable": true
#                 },
#                 "process_id": "26"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 2
#                     }
#                 ],
#                 "process_id": "27"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "cost": 2,
#                 "dead_interval": 2,
#                 "default_metric": 10,
#                 "demand_circuit": true,
#                 "hello_interval": 1,
#                 "mtu_ignore": true,
#                 "packet_size": 577,
#                 "priority": 1,
#                 "process_id": "30",
#                 "retransmit_interval": 2,
#                 "router_id": "2.2.2.2",
#                 "transmit_delay": 2
#             }
#         ]
#     }
#
# Using rendered
#
#
- name: Render the commands for provided  configuration
  cisco.iosxr.iosxr_ospfv3:
    config:
      processes:
        - process_id: 27
          areas:
            - area_id: 10
              hello_interval: 2
        - process_id: 26
          authentication:
            disable: true
        - process_id: 10
          areas:
            - area_id: 11
              default_cost: 5
              cost: 11
            - area_id: 22
              default_cost: 6
        - process_id: 30
          areas:
            - area_id: 11
              default_cost: 5
            - area_id: 22
              default_cost: 6
          cost: 2
          default_metric: 10
          transmit_delay: 2
          hello_interval: 1
          dead_interval: 2
          retransmit_interval: 2
          packet_size: 577
          priority: 1
          router_id: '2.2.2.2'
          demand_circuit: true
          mtu_ignore: true
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#         "router ospfv3 27",
#         "area 10 hello-interval 2",
#         "router ospfv3 26",
#         "authentication disable",
#         "router ospfv3 10",
#         "area 11 default-cost 5",
#         "area 11 cost 11",
#         "area 22 default-cost 6",
#         "router ospfv3 30",
#         "cost 2",
#         "priority 1",
#         "default-metric 10",
#         "router-id 2.2.2.2",
#         "demand-circuit",
#         "packet-size 577",
#         "transmit-delay 2",
#         "dead-interval 2",
#         "hello-interval 1",
#         "retransmit-interval 2",
#         "mtu-ignore",
#         "area 11 default-cost 5",
#         "area 22 default-cost 6"
#     ]

# Using gathered
#
# Before state:
# -------------
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# router ospfv3 10
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospfv3 26
#  authentication disable
#  area 10
#  !
# !
# router ospfv3 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#  !
#  area 30
#  !
# !
# router ospfv3 30
#  cost 2
#  priority 1
#  mtu-ignore
#  packet-size 577
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit
#  hello-interval 1
#  transmit-delay 2
#  router-id 2.2.2.2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !

- name: Gather ospfv3 routes configuration
  cisco.iosxr.iosxr_ospfv3:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#         "processes": [
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "cost": 11,
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "process_id": "10"
#             },
#             {
#                 "authentication": {
#                     "disable": true
#                 },
#                 "process_id": "26"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "hello_interval": 2
#                     }
#                 ],
#                 "process_id": "27"
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "11",
#                         "default_cost": 5
#                     },
#                     {
#                         "area_id": "22",
#                         "default_cost": 6
#                     }
#                 ],
#                 "cost": 2,
#                 "dead_interval": 2,
#                 "default_metric": 10,
#                 "demand_circuit": true,
#                 "hello_interval": 1,
#                 "mtu_ignore": true,
#                 "packet_size": 577,
#                 "priority": 1,
#                 "process_id": "30",
#                 "retransmit_interval": 2,
#                 "router_id": "2.2.2.2",
#                 "transmit_delay": 2
#             }
#         ]
#     }
#
```

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
