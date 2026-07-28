---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_bgp_neighbors module – Manage a BGP neighbor and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_bgp_neighbors_module.html
fetched_at: 2026-07-28T02:03:31+00:00
---
# dellemc.enterprise_sonic.sonic_bgp_neighbors module – Manage a BGP neighbor and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_bgp_neighbors`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_bgp_neighbors_module.md#synopsis)
- [Parameters](sonic_bgp_neighbors_module.md#parameters)
- [Notes](sonic_bgp_neighbors_module.md#notes)
- [Examples](sonic_bgp_neighbors_module.md#examples)
- [Return Values](sonic_bgp_neighbors_module.md#return-values)

## [Synopsis](sonic_bgp_neighbors_module.md#id1)

- This module provides configuration management of global BGP_NEIGHBORS parameters on devices running Enterprise SONiC.
- bgp_as and vrf_name must be created on the device in advance.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_bgp_neighbors_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the BGP neighbors related configuration. |
| **bgp_as**  string / required | Specifies the BGP autonomous system (AS) number which is already configured on the device. |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor-related configurations. |
| **advertisement_interval**  integer | Specifies the minimum interval between sending BGP routing updates.  The range is from 0 to 600. |
| **auth_pwd**  dictionary | Configuration for neighbor group authentication password. |
| **encrypted**  boolean | Indicates whether the password is encrypted text.  **Choices:**   - `false` ← (default) - `true` |
| **pwd**  string / required | Authentication password for the neighbor group. |
| **bfd**  dictionary | Enables or disables BFD. |
| **check_failure**  boolean | Link dataplane status with control plane.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | Enables BFD liveliness check for a BGP neighbor.  **Choices:**   - `false` - `true` |
| **profile**  string | BFD Profile name. |
| **capability**  dictionary | Specifies capability attributes to this neighbor. |
| **dynamic**  boolean | Enables or disables dynamic capability to this neighbor.  **Choices:**   - `false` - `true` |
| **extended_nexthop**  boolean | Enables or disables advertise extended next-hop capability to the peer.  **Choices:**   - `false` - `true` |
| **disable_connected_check**  boolean | Disables EBGP conntected route check.  **Choices:**   - `false` - `true` |
| **dont_negotiate_capability**  boolean | Disables capability negotiation.  **Choices:**   - `false` - `true` |
| **ebgp_multihop**  dictionary | Allow EBGP neighbors not on directly connected networks. |
| **enabled**  boolean | Enables the referenced group or neighbors to be indirectly connected.  **Choices:**   - `false` ← (default) - `true` |
| **multihop_ttl**  integer | Time-to-live value to use when packets are sent to the referenced group or neighbors and ebgp-multihop is enabled. |
| **enforce_first_as**  boolean | Enforces the first AS for EBGP routes.  **Choices:**   - `false` - `true` |
| **enforce_multihop**  boolean | Enforces EBGP multihop performance for neighbor.  **Choices:**   - `false` - `true` |
| **local_address**  string | Set the local IP address to use for the session when sending BGP update messages. |
| **local_as**  dictionary | Specifies local autonomous system number. |
| **as**  integer / required | Local autonomous system number. |
| **no_prepend**  boolean | Do not prepend the local-as number in AS-Path advertisements.  **Choices:**   - `false` - `true` |
| **replace_as**  boolean | Replace the configured AS Number with the local-as number in AS-Path advertisements.  **Choices:**   - `false` - `true` |
| **nbr_description**  string | A textual description of the neighbor. |
| **neighbor**  string / required | Neighbor router address. |
| **override_capability**  boolean | Override capability negotiation result.  **Choices:**   - `false` - `true` |
| **passive**  boolean | Do not send open messages to this neighbor.  **Choices:**   - `false` ← (default) - `true` |
| **peer_group**  string | The name of the peer group that the neighbor is a member of. |
| **port**  integer | Neighbor’s BGP port. |
| **remote_as**  dictionary | Remote AS of the BGP neighbor to configure.  peer_as and peer_type are mutually exclusive. |
| **peer_as**  integer | Specifies remote AS number.  The range is from 1 to 4294967295. |
| **peer_type**  string | Specifies the type of BGP peer.  **Choices:**   - `"internal"` - `"external"` |
| **shutdown_msg**  string | Add a shutdown message. |
| **solo**  boolean | Indicates that routes advertised by the peer should not be reflected back to the peer.  **Choices:**   - `false` - `true` |
| **strict_capability_match**  boolean | Enables strict capability negotiation match.  **Choices:**   - `false` - `true` |
| **timers**  dictionary | Specifies BGP neighbor timer-related configurations. |
| **connect_retry**  integer | Time interval in seconds between attempts to establish a session with the peer.  The range is from 1 to 65535. |
| **holdtime**  integer | Interval after not receiving a keepalive message that SONiC declares a peer dead, in seconds.  The range is from 0 to 65535. |
| **keepalive**  integer | Frequency with which the device sends keepalive messages to its peer, in seconds.  The range is from 0 to 65535. |
| **ttl_security**  integer | Enforces only the neighbors that are specified number of hops away will be allowed to become neighbors. |
| **v6only**  boolean | Enables BGP with v6 link-local only.  **Choices:**   - `false` - `true` |
| **peer_group**  list / elements=dictionary | Specifies the list of peer groups. |
| **address_family**  dictionary | Holds of list of address families associated to the peergroup. |
| **afis**  list / elements=dictionary | List of address families with afi, safi, activate and allowas-in parameters.  afi and safi are required together. |
| **activate**  boolean | Enable or disable activate.  **Choices:**   - `false` - `true` |
| **afi**  string | Holds afi mode.  **Choices:**   - `"ipv4"` - `"ipv6"` - `"l2vpn"` |
| **allowas_in**  dictionary | Holds AS value.  The origin and value are mutually exclusive. |
| **origin**  boolean | Set AS as the origin.  **Choices:**   - `false` - `true` |
| **value**  integer | Holds AS number in the range 1-10. |
| **ip_afi**  dictionary | Common configuration attributes for IPv4 and IPv6 unicast address families. |
| **default_policy_name**  string | Specifies routing policy definition. |
| **send_default_route**  boolean | Enable or disable sending of default-route to the peer.  **Choices:**   - `false` ← (default) - `true` |
| **prefix_limit**  dictionary | Specifies prefix limit attributes. |
| **max_prefixes**  integer | Maximum number of prefixes that will be accepted from the peer. |
| **prevent_teardown**  boolean | Enable or disable teardown of BGP session when maximum prefix limit is exceeded.  **Choices:**   - `false` ← (default) - `true` |
| **restart_timer**  integer | Time interval in seconds after which the BGP session is re-established after being torn down. |
| **warning_threshold**  integer | Threshold on number of prefixes that can be received from a peer before generation of warning messages.  Expressed as a percentage of max-prefixes. |
| **prefix_list_in**  string | Inbound route filtering policy for a peer. |
| **prefix_list_out**  string | Outbound route filtering policy for a peer. |
| **safi**  string | Holds safi mode.  **Choices:**   - `"unicast"` - `"evpn"` |
| **advertisement_interval**  integer | Specifies the minimum interval between sending BGP routing updates.  The range is from 0 to 600. |
| **auth_pwd**  dictionary | Configuration for peer group authentication password. |
| **encrypted**  boolean | Indicates whether the password is encrypted text.  **Choices:**   - `false` ← (default) - `true` |
| **pwd**  string / required | Authentication password for the peer group. |
| **bfd**  dictionary | Enables or disables BFD. |
| **check_failure**  boolean | Link dataplane status with control plane.  **Choices:**   - `false` - `true` |
| **enabled**  boolean | Enables BFD liveliness check for a BGP peer.  **Choices:**   - `false` - `true` |
| **profile**  string | BFD Profile name. |
| **capability**  dictionary | Specifies capability attributes to this peer group. |
| **dynamic**  boolean | Enables or disables dynamic capability to this peer group.  **Choices:**   - `false` - `true` |
| **extended_nexthop**  boolean | Enables or disables advertise extended next-hop capability to the peer.  **Choices:**   - `false` - `true` |
| **disable_connected_check**  boolean | Disables EBGP conntected route check.  **Choices:**   - `false` - `true` |
| **dont_negotiate_capability**  boolean | Disables capability negotiation.  **Choices:**   - `false` - `true` |
| **ebgp_multihop**  dictionary | Allow EBGP peers not on directly connected networks. |
| **enabled**  boolean | Enables the referenced group or peers to be indirectly connected.  **Choices:**   - `false` ← (default) - `true` |
| **multihop_ttl**  integer | Time-to-live value to use when packets are sent to the referenced group or peers and ebgp-multihop is enabled. |
| **enforce_first_as**  boolean | Enforces the first AS for EBGP routes.  **Choices:**   - `false` - `true` |
| **enforce_multihop**  boolean | Enforces EBGP multihop performance for peer.  **Choices:**   - `false` - `true` |
| **local_address**  string | Set the local IP address to use for the session when sending BGP update messages. |
| **local_as**  dictionary | Specifies local autonomous system number. |
| **as**  integer / required | Local autonomous system number. |
| **no_prepend**  boolean | Do not prepend the local-as number in AS-Path advertisements.  **Choices:**   - `false` - `true` |
| **replace_as**  boolean | Replace the configured AS Number with the local-as number in AS-Path advertisements.  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the peer group. |
| **override_capability**  boolean | Override capability negotiation result.  **Choices:**   - `false` - `true` |
| **passive**  boolean | Do not send open messages to this peer.  **Choices:**   - `false` ← (default) - `true` |
| **pg_description**  string | A textual description of the peer group. |
| **remote_as**  dictionary | Remote AS of the BGP peer group to configure.  peer_as and peer_type are mutually exclusive. |
| **peer_as**  integer | Specifies remote AS number.  The range is from 1 to 4294967295. |
| **peer_type**  string | Specifies the type of BGP peer.  **Choices:**   - `"internal"` - `"external"` |
| **shutdown_msg**  string | Add a shutdown message. |
| **solo**  boolean | Indicates that routes advertised by the peer should not be reflected back to the peer.  **Choices:**   - `false` - `true` |
| **strict_capability_match**  boolean | Enables strict capability negotiation match.  **Choices:**   - `false` - `true` |
| **timers**  dictionary | Specifies BGP peer group timer related configurations. |
| **connect_retry**  integer | Time interval in seconds between attempts to establish a session with the peer.  The range is from 1 to 65535. |
| **holdtime**  integer | Interval after not receiving a keepalive message that Enterprise SONiC declares a peer dead, in seconds.  The range is from 0 to 65535. |
| **keepalive**  integer | Frequency with which the device sends keepalive messages to its peer, in seconds.  The range is from 0 to 65535. |
| **ttl_security**  integer | Enforces only the peers that are specified number of hops away will be allowed to become peers. |
| **vrf_name**  string | Specifies the VRF name which is already configured on the device.  **Default:** `"default"` |
| **state**  string | Specifies the operation to be performed on the BGP process that is configured on the device.  In case of merged, the input configuration is merged with the existing BGP configuration on the device.  In case of deleted, the existing BGP configuration is removed from the device.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_bgp_neighbors_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_bgp_neighbors_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# neighbor interface Eth1/3
#!
#router bgp 11
# network import-check
# timers 60 180
# !
# neighbor 192.168.1.4
# !
# peer-group SP1
#  bfd
#  capability dynamic
# !
# peer-group SP2
# !
#
- name: Deletes all BGP neighbors
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
    state: deleted

#
# After state:
# -------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
#!
#router bgp 11
# network import-check
# timers 60 180
# !
#
# Using merged
#
# Before state:
# ------------
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
#!
#router bgp 11
# network import-check
# timers 60 180
# !

- name: "Adds sonic_bgp_neighbors"
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
     - bgp_as: 51
       neighbors:
         - neighbor: Eth1/2
           auth_pwd:
             pwd: 'pw123'
             encrypted: false
           dont_negotiate_capability: true
           ebgp_multihop:
             enabled: true
             multihop_ttl: 1
           enforce_first_as: true
           enforce_multihop: true
           local_address: 'Ethernet4'
           local_as:
             as: 2
             no_prepend: true
             replace_as: true
           nbr_description: "description 1"
           override_capability: true
           passive: true
           port: 3
           shutdown_msg: 'msg1'
           solo: true
         - neighbor: 1.1.1.1
           disable_connected_check: true
           ttl_security: 5
     - bgp_as: 51
       vrf_name: VrfReg1
       peer_group:
         - name: SPINE
           bfd:
             check_failure: true
             enabled: true
             profile: 'profile 1'
           capability:
             dynamic: true
             extended_nexthop: true
           auth_pwd:
             pwd: 'U2FsdGVkX1/4sRsZ624wbAJfDmagPLq2LsGDOcW/47M='
             encrypted: true
           dont_negotiate_capability: true
           ebgp_multihop:
             enabled: true
             multihop_ttl: 1
           enforce_first_as: true
           enforce_multihop: true
           local_address: 'Ethernet4'
           local_as:
             as: 2
             no_prepend: true
             replace_as: true
           pg_description: 'description 1'
           override_capability: true
           passive: true
           solo: true
           remote_as:
             peer_as: 4
         - name: SPINE1
           disable_connected_check: true
           shutdown_msg: "msg1"
           strict_capability_match: true
           timers:
             keepalive: 30
             holdtime: 15
             connect_retry: 25
           ttl_security: 5
           address_family:
             afis:
               - afi: ipv4
                 safi: unicast
                 activate: true
                 allowas_in:
                   origin: true
               - afi: ipv6
                 safi: unicast
                 activate: true
                 allowas_in:
                   value: 5
       neighbors:
         - neighbor: Eth1/3
           remote_as:
             peer_as: 10
           peer_group: SPINE
           advertisement_interval: 15
           timers:
             keepalive: 30
             holdtime: 15
             connect_retry: 25
           bfd:
             check_failure: true
             enabled: true
             profile: 'profile 1'
           capability:
             dynamic: true
             extended_nexthop: true
           auth_pwd:
               pwd: 'U2FsdGVkX199MZ7YOPkOR9O6wEZmtGSgiDfnlcN9hBg='
               encrypted: true
           nbr_description: 'description 2'
           strict_capability_match: true
           v6only: true
         - neighbor: 192.168.1.4
    state: merged
#
# After state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE1
#  timers 15 30
#  timers connect 25
#  shutdown message msg1
#  disable-connected-check
#  strict-capability-match
#  ttl-security hops 5
# !
# peer-group SPINE
#  description "description 1"
#  ebgp-multihop 1
#  remote-as 4
#  bfd check-control-plane-failure profile "profile 1"
#  update-source interface Ethernet4
#  capability dynamic
#  capability extended-nexthop
#  dont-capability-negotiate
#  enforce-first-as
#  enforce-multihop
#  local-as 2 no-prepend replace-as
#  override-capability
#  passive
#  password U2FsdGVkX1/4sRsZ624wbAJfDmagPLq2LsGDOcW/47M= encrypted
#  solo
#  address-family ipv4 unicast
#   activate
#   allowas-in origin
#   send-community both
# !
#  address-family ipv6 unicast
#   activate
#   allowas-in 5
#   send-community both
# !
# neighbor interface Eth1/3
#  description "description 2"
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  timers connect 25
#  bfd check-control-plane-failure profile "profile 1"
#  advertisement-interval 15
#  capability extended-nexthop
#  capability dynamic
#  v6only
#  password U2FsdGVkX199MZ7YOPkOR9O6wEZmtGSgiDfnlcN9hBg= encrypted
#  strict-capability-match
# !
# neighbor 192.168.1.4
#!
# router bgp 51
#  timers 60 180
# neighbor interface Eth1/2
#  description "description 1"
#  shutdown message msg1
#  ebgp-multihop 1
#  remote-as external
#  update-source interface Ethernet4
#  dont-capability-negotiate
#  enforce-first-as
#  enforce-multihop
#  local-as 2 no-prepend replace-as
#  override-capability
#  passive
#  password U2FsdGVkX1+bxMf9TKOhaXRNNaHmywiEVDF2lJ2c000= encrypted
#  port 3
#  solo
# neighbor 1.1.1.1
#  disable-connected-check
#  ttl-security hops 5
#router bgp 11
# network import-check
# timers 60 180
#
# Using deleted
#
# Before state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
#  bfd
#  remote-as 4
# !
# neighbor interface Eth1/3
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
#!
#router bgp 11
# network import-check
# timers 60 18
# !
# peer-group SP
# !
# neighbor interface Eth1/3
#
- name: "Deletes sonic_bgp_neighbors and peer-groups specific to vrfname"
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
     - bgp_as: 51
       vrf_name: VrfReg1
    state: deleted

# After state:
# ------------
#!
#router bgp 11 vrf VrfCheck2
# network import-check
# timers 60 180
#!
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
#router bgp 11
# network import-check
# timers 60 18
# !
# peer-group SP
# !
# neighbor interface Eth1/3
#
# Using deleted
#
# Before state:
# -------------
#
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE
#  bfd
#  remote-as 4
# !
# neighbor interface Eth1/3
#  peer-group SPINE
#  remote-as 10
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
# !

- name: "Deletes specific sonic_bgp_neighbors"
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
     - bgp_as: 51
       neighbors:
         - neighbor: Eth1/2
           auth_pwd:
             pwd: 'pw123'
             encrypted: false
           dont_negotiate_capability: true
           ebgp_multihop:
             enabled: true
             multihop_ttl: 1
           enforce_first_as: true
           enforce_multihop: true
           local_address: 'Ethernet4'
           local_as:
             as: 2
             no_prepend: true
             replace_as: true
           nbr_description: 'description 1'
           override_capability: true
           passive: true
           port: 3
           shutdown_msg: 'msg1'
           solo: true
         - neighbor: 1.1.1.1
           disable_connected_check: true
           ttl_security: 5
     - bgp_as: 51
       vrf_name: VrfReg1
       peer_group:
         - name: SPINE
           bfd:
             check_failure: true
             enabled: true
             profile: 'profile 1'
           capability:
             dynamic: true
             extended_nexthop: true
           auth_pwd:
             pwd: 'U2FsdGVkX1/4sRsZ624wbAJfDmagPLq2LsGDOcW/47M='
             encrypted: true
           dont_negotiate_capability: true
           ebgp_multihop:
             enabled: true
             multihop_ttl: 1
           enforce_first_as: true
           enforce_multihop: true
           local_address: 'Ethernet4'
           local_as:
             as: 2
             no_prepend: true
             replace_as: true
           pg_description: 'description 1'
           override_capability: true
           passive: true
           solo: true
           remote_as:
             peer_as: 4
         - name: SPINE1
           disable_connected_check: true
           shutdown_msg: "msg1"
           strict_capability_match: true
           timers:
             keepalive: 30
             holdtime: 15
             connect_retry: 25
           ttl_security: 5
       neighbors:
         - neighbor: Eth1/3
           remote_as:
             peer_as: 10
           peer_group: SPINE
           advertisement_interval: 15
           timers:
             keepalive: 30
             holdtime: 15
             connect_retry: 25
           bfd:
             check_failure: true
             enabled: true
             profile: 'profile 1'
           capability:
             dynamic: true
             extended_nexthop: true
           auth_pwd:
             pwd: 'U2FsdGVkX199MZ7YOPkOR9O6wEZmtGSgiDfnlcN9hBg='
             encrypted: true
           nbr_description: 'description 2'
           strict_capability_match: true
           v6only: true
         - neighbor: 192.168.1.4
    state: deleted
#
# After state:
# -------------
#
#router bgp 51 vrf VrfReg1
# network import-check
# timers 60 180
# !
# peer-group SPINE1
# !
# peer-group SPINE
# !
# neighbor interface Eth1/3
# !
# neighbor interface Eth1/2
# neighbor 1.1.1.1
#
# Using merged
#
# Before state:
# -------------
#
# sonic# show running-configuration bgp peer-group vrf default
# (No bgp peer-group configuration present)

- name: "Configure BGP peer-group prefix-list attributes"
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
     - bgp_as: 51
       peer_group:
         - name: SPINE
           address_family:
             afis:
               - afi: ipv4
                 safi: unicast
                 ip_afi:
                   default_policy_name: rmap_reg1
                   send_default_route: true
                 prefix_limit:
                   max_prefixes: 1
                   prevent_teardown: true
                   warning_threshold: 80
                 prefix_list_in: p1
                 prefix_list_out: p2
    state: merged

# After state:
# ------------
#
# sonic# show running-configuration bgp peer-group vrf default
# !
# peer-group SPINE
#  !
#  address-family ipv4 unicast
#   default-originate route-map rmap_reg1
#   prefix-list p1 in
#   prefix-list p2 out
#   send-community both
#   maximum-prefix 1 80 warning-only
#
# Using deleted
#
# Before state:
# -------------
#
# sonic# show running-configuration bgp peer-group vrf default
# !
# peer-group SPINE
#  !
#  address-family ipv6 unicast
#   default-originate route-map rmap_reg2
#   prefix-list p1 in
#   prefix-list p2 out
#   send-community both
#   maximum-prefix 5 90 restart 2

- name: "Delete BGP peer-group prefix-list attributes"
  dellemc.enterprise_sonic.sonic_bgp_neighbors:
    config:
     - bgp_as: 51
       peer_group:
         - name: SPINE
           address_family:
             afis:
               - afi: ipv6
                 safi: unicast
                 ip_afi:
                   default_policy_name: rmap_reg2
                   send_default_route: true
                 prefix_limit:
                   max_prefixes: 5
                   warning_threshold: 90
                   restart-timer: 2
                 prefix_list_in: p1
                 prefix_list_out: p2
    state: deleted

# sonic# show running-configuration bgp peer-group vrf default
# (No bgp peer-group configuration present)
```

## [Return Values](sonic_bgp_neighbors_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
