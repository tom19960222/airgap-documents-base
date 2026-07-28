---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_bgp_neighbors module – Manage a BGP neighbor and its parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_bgp_neighbors_module.html
fetched_at: 2026-07-27T17:24:50+00:00
---
# dellemc.enterprise_sonic.sonic_bgp_neighbors module – Manage a BGP neighbor and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
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
| **auth_pwd**  dictionary | Configuration for neighbor group authentication password |
| **encrypted**  boolean | Indicates whether the password is encrypted text  Choices:   - `false` ← (default) - `true` |
| **pwd**  string | Authentication password for the neighbor group |
| **bfd**  boolean | Enables or disables BFD.  Choices:   - `false` - `true` |
| **capability**  dictionary | Specifies capability attributes to this neighbor. |
| **dynamic**  boolean | Enables or disables dynamic capability to this neighbor.  Choices:   - `false` - `true` |
| **extended_nexthop**  boolean | Enables or disables advertise extended next-hop capability to the peer.  Choices:   - `false` - `true` |
| **nbr_description**  string | A textual description of the interface |
| **neighbor**  string / required | Neighbor router address. |
| **peer_group**  string | The name of the peer group that the neighbor is a member of. |
| **remote_as**  dictionary | Remote AS of the BGP neighbor to configure.  peer_as and peer_type are mutually exclusive. |
| **peer_as**  integer | Specifies remote AS number.  The range is from 1 to 4294967295. |
| **peer_type**  string | Specifies the type of BGP peer.  Choices:   - `"internal"` - `"external"` |
| **timers**  dictionary | Specifies BGP neighbor timer-related configurations. |
| **holdtime**  integer | Interval after not receiving a keepalive message that SONiC declares a peer dead, in seconds.  The range is from 0 to 65535. |
| **keepalive**  integer | Frequency with which the device sends keepalive messages to its peer, in seconds.  The range is from 0 to 65535. |
| **peer_group**  list / elements=dictionary | Specifies the list of peer groups. |
| **address_family**  dictionary | Holds of list of address families associated to the peergroup. |
| **afis**  list / elements=dictionary | List of address families with afi, safi, activate and allowas-in parameters.  afi and safi are required together. |
| **activate**  boolean | Enable or disable activate.  Choices:   - `false` - `true` |
| **afi**  string | Holds afi mode.  Choices:   - `"ipv4"` - `"ipv6"` - `"l2vpn"` |
| **allowas_in**  dictionary | Holds AS value.  The origin and value are mutually exclusive. |
| **origin**  boolean | Set AS as the origin.  Choices:   - `false` - `true` |
| **value**  integer | Holds AS number in the range 1-10. |
| **safi**  string | Holds safi mode.  Choices:   - `"unicast"` - `"evpn"` |
| **advertisement_interval**  integer | Specifies the minimum interval between sending BGP routing updates.  The range is from 0 to 600. |
| **bfd**  boolean | Enables or disables BFD.  Choices:   - `false` - `true` |
| **capability**  dictionary | Specifies capability attributes to this peer group. |
| **dynamic**  boolean | Enables or disables dynamic capability to this peer group.  Choices:   - `false` - `true` |
| **extended_nexthop**  boolean | Enables or disables advertise extended next-hop capability to the peer.  Choices:   - `false` - `true` |
| **name**  string / required | Name of the peer group. |
| **remote_as**  dictionary | Remote AS of the BGP peer group to configure.  peer_as and peer_type are mutually exclusive. |
| **peer_as**  integer | Specifies remote AS number.  The range is from 1 to 4294967295. |
| **peer_type**  string | Specifies the type of BGP peer.  Choices:   - `"internal"` - `"external"` |
| **timers**  dictionary | Specifies BGP peer group timer related configurations. |
| **holdtime**  integer | Interval after not receiving a keepalive message that Enterprise SONiC declares a peer dead, in seconds.  The range is from 0 to 65535. |
| **keepalive**  integer | Frequency with which the device sends keepalive messages to its peer, in seconds.  The range is from 0 to 65535. |
| **vrf_name**  string | Specifies the VRF name which is already configured on the device.  Default: `"default"` |
| **state**  string | Specifies the operation to be performed on the BGP process that is configured on the device.  In case of merged, the input configuration is merged with the existing BGP configuration on the device.  In case of deleted, the existing BGP configuration is removed from the device.  Choices:   - `"merged"` ← (default) - `"deleted"` |

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
             pwd: "pw123"
             encrypted: false
           nbr_description: "description 1"
     - bgp_as: 51
       vrf_name: VrfReg1
       peer_group:
         - name: SPINE
           bfd: true
           capability:
             dynamic: true
             extended_nexthop: true
           remote_as:
             peer_as: 4
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
           bfd: true
           capability:
             dynamic: true
             extended_nexthop: true
           auth_pwd:
             pwd: "U2FsdGVkX199MZ7YOPkOR9O6wEZmtGSgiDfnlcN9hBg="
             encrypted: true
           nbr_description: "description 1"
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
# peer-group SPINE
#  remote-as 4
#  bfd
#  capability dynamic
#  capability extended-nexthop
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
#  description "description 1"
#  peer-group SPINE
#  remote-as 10
#  password U2FsdGVkX199MZ7YOPkOR9O6wEZmtGSgiDfnlcN9hBg= encrypted
#  timers 15 30
#  advertisement-interval 15
#  bfd
#  capability extended-nexthop
#  capability dynamic
# !
# neighbor 192.168.1.4
#!
# router bgp 51
#  timers 60 180
#   neighbor interface Eth1/2
#   description "description 1"
#   password U2FsdGVkX1+bxMf9TKOhaXRNNaHmywiEVDF2lJ2c000= encrypted
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
             pwd: "pw123"
             encrypted: false
           nbr_description: "description 1"
     - bgp_as: 51
       vrf_name: VrfReg1
       peer_group:
         - name: SPINE
           bfd: true
           remote_as:
             peer_as: 4
       neighbors:
         - neighbor: Eth1/3
           remote_as:
             peer_as: 10
           peer_group: SPINE
           advertisement_interval: 15
           timers:
             keepalive: 30
             holdtime: 15
           bfd: true
           capability:
             dynamic: true
             extended_nexthop: true
           auth_pwd:
             pwd: "U2FsdGVkX199MZ7YOPkOR9O6wEZmtGSgiDfnlcN9hBg="
             encrypted: true
           nbr_description: "description 1"
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
# peer-group SPINE
# !
# neighbor interface Eth1/3
# !
```

## [Return Values](sonic_bgp_neighbors_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
