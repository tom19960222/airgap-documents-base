---
collection: ansible
version: "6"
title: "cisco.ios.ios_ntp_global module – Resource module to configure NTP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_ntp_global_module.html
fetched_at: 2026-07-27T16:55:22+00:00
---
# cisco.ios.ios_ntp_global module – Resource module to configure NTP.

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
> To use it in a playbook, specify: `cisco.ios.ios_ntp_global`.

New in cisco.ios 2.5.0

- [Synopsis](ios_ntp_global_module.md#synopsis)
- [Parameters](ios_ntp_global_module.md#parameters)
- [Notes](ios_ntp_global_module.md#notes)
- [Examples](ios_ntp_global_module.md#examples)
- [Return Values](ios_ntp_global_module.md#return-values)

## [Synopsis](ios_ntp_global_module.md#id1)

- This module provides declarative management of ntp on Cisco IOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_ntp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of ntp options |
| **access_group**  dictionary | Control NTP access |
| **peer**  list / elements=dictionary | Provide full access |
| **access_list**  string | name or number of access list |
| **ipv4**  boolean | ipv4 access lists (Default not idempotent)  Choices:   - `false` - `true` |
| **ipv6**  boolean | ipv6 access lists (Default not idempotent)  Choices:   - `false` - `true` |
| **kod**  boolean | Send a Kiss-o-Death packet for failing peers  Choices:   - `false` - `true` |
| **query_only**  list / elements=dictionary | Allow only control queries |
| **access_list**  string | name or number of access list |
| **ipv4**  boolean | ipv4 access lists (Default not idempotent)  Choices:   - `false` - `true` |
| **ipv6**  boolean | ipv6 access lists (Default not idempotent)  Choices:   - `false` - `true` |
| **kod**  boolean | Send a Kiss-o-Death packet for failing peers  Choices:   - `false` - `true` |
| **serve**  list / elements=dictionary | Provide server and query access |
| **access_list**  string | name or number of access list |
| **ipv4**  boolean | ipv4 access lists (Default not idempotent)  Choices:   - `false` - `true` |
| **ipv6**  boolean | ipv6 access lists (Default not idempotent)  Choices:   - `false` - `true` |
| **kod**  boolean | Send a Kiss-o-Death packet for failing peers  Choices:   - `false` - `true` |
| **serve_only**  list / elements=dictionary | Provide only server access |
| **access_list**  string | name or number of access list |
| **ipv4**  boolean | ipv4 access lists (Default not idempotent)  Choices:   - `false` - `true` |
| **ipv6**  boolean | ipv6 access lists (Default not idempotent)  Choices:   - `false` - `true` |
| **kod**  boolean | Send a Kiss-o-Death packet for failing peers  Choices:   - `false` - `true` |
| **allow**  dictionary | Allow processing of packets |
| **control**  dictionary | Allow processing control mode packets |
| **rate_limit**  integer | Rate-limit delay. |
| **private**  boolean | Allow processing private mode packets  Choices:   - `false` - `true` |
| **authenticate**  boolean | Authenticate time sources  Choices:   - `false` - `true` |
| **authentication_keys**  list / elements=dictionary | Authentication key for trusted time sources |
| **algorithm**  string | Authentication type |
| **encryption**  integer | Authentication key encryption type |
| **id**  integer | Key number |
| **key**  string | Password |
| **broadcast_delay**  integer | Estimated round-trip delay |
| **clock_period**  integer | Length of hardware clock tick, clock period in 2^-32 seconds |
| **logging**  boolean | Enable NTP message logging  Choices:   - `false` - `true` |
| **master**  dictionary | Act as NTP master clock |
| **enabled**  boolean | Enable master clock  Choices:   - `false` - `true` |
| **stratum**  integer | Stratum number |
| **max_associations**  integer | Set maximum number of associations |
| **max_distance**  integer | Maximum Distance for synchronization |
| **min_distance**  integer | Minimum distance to consider for clockhop |
| **orphan**  integer | Threshold Stratum for orphan mode |
| **panic_update**  boolean | Reject time updates > panic threshold (default 1000Sec)  Choices:   - `false` - `true` |
| **passive**  boolean | NTP passive mode  Choices:   - `false` - `true` |
| **peers**  list / elements=dictionary | Configure NTP peer |
| **burst**  boolean | Send a burst when peer is reachable (Default)  Choices:   - `false` - `true` |
| **iburst**  boolean | Send a burst when peer is unreachable (Default)  Choices:   - `false` - `true` |
| **key_id**  aliases: key  integer | Configure peer authentication key |
| **maxpoll**  integer | Maximum poll interval Poll value in Log2 |
| **minpoll**  integer | Minimum poll interval Poll value in Log2 |
| **normal_sync**  boolean | Disable rapid sync at startup  Choices:   - `false` - `true` |
| **peer**  string | ipv4/ipv6 address or hostname of the peer |
| **prefer**  boolean | Prefer this peer when possible  Choices:   - `false` - `true` |
| **source**  string | Interface for source address |
| **use_ipv4**  boolean | Use IP for DNS resolution  Choices:   - `false` - `true` |
| **use_ipv6**  boolean | Use IPv6 for DNS resolution  Choices:   - `false` - `true` |
| **version**  integer | Configure NTP version |
| **vrf**  string | VPN Routing/Forwarding Information |
| **servers**  list / elements=dictionary | Configure NTP server |
| **burst**  boolean | Send a burst when peer is reachable (Default)  Choices:   - `false` - `true` |
| **iburst**  boolean | Send a burst when peer is unreachable (Default)  Choices:   - `false` - `true` |
| **key_id**  aliases: key  integer | Configure peer authentication key |
| **maxpoll**  integer | Maximum poll interval Poll value in Log2 |
| **minpoll**  integer | Minimum poll interval Poll value in Log2 |
| **normal_sync**  boolean | Disable rapid sync at startup  Choices:   - `false` - `true` |
| **prefer**  boolean | Prefer this peer when possible  Choices:   - `false` - `true` |
| **server**  string | ipv4/ipv6 address or hostname of the server |
| **source**  string | Interface for source address |
| **use_ipv4**  boolean | Use IP for DNS resolution  Choices:   - `false` - `true` |
| **use_ipv6**  boolean | Use IPv6 for DNS resolution  Choices:   - `false` - `true` |
| **version**  integer | Configure NTP version |
| **vrf**  string | VPN Routing/Forwarding Information |
| **source**  string | Configure interface for source address |
| **trusted_keys**  list / elements=dictionary | Key numbers for trusted time sources |
| **range_end**  integer | End key number |
| **range_start**  integer | Start / key number |
| **update_calendar**  boolean | Periodically update calendar with NTP time  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^ntp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The states *replaced* and *overridden* have identical behaviour for this module.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | section ^ntp* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](ios_ntp_global_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.6.
> - This module works with connection `network_cli`.

## [Examples](ios_ntp_global_module.md#id4)

```yaml+jinja
# Using state: merged

# Before state:
# -------------

# router-ios#show running-config | section ^ntp
# --------------------- EMPTY -----------------

# Merged play:
# ------------

- name: Apply the provided configuration
  cisco.ios.ios_ntp_global:
    config:
      access_group:
        peer:
          - access_list: DHCP-Server
            ipv4: true
            kod: true
          - access_list: preauth_ipv6_acl
            ipv6: true
            kod: true
          - access_list: '2'
            kod: true
        query_only:
          - access_list: '10'
      allow:
        control:
          rate_limit: 4
        private: true
      authenticate: true
      authentication_keys:
        - algorithm: md5
          encryption: 22
          id: 2
          key: SomeSecurePassword
      broadcast_delay: 22
      clock_period: 5
      logging: true
      master:
        stratum: 4
      max_associations: 34
      max_distance: 3
      min_distance: 10
      orphan: 4
      panic_update: true
      peers:
        - peer: 172.16.1.10
          version: 2
        - key: 2
          minpoll: 5
          peer: 172.16.1.11
          prefer: true
          version: 2
        - peer: checkPeerDomainIpv4.com
          prefer: true
          use_ipv4: true
        - peer: checkPeerDomainIpv6.com
          use_ipv6: true
        - peer: testPeerDomainIpv6.com
          prefer: true
          use_ipv6: true
      servers:
        - server: 172.16.1.12
          version: 2
        - server: checkServerDomainIpv6.com
          use_ipv6: true
        - server: 172.16.1.13
          source: GigabitEthernet0/1
      source: GigabitEthernet0/1
      trusted_keys:
        - range_end: 3
          range_start: 3
        - range_start: 21
    state: merged

# Commands Fired:
# ---------------

# "commands": [
#     "ntp allow mode control 4",
#     "ntp allow mode private",
#     "ntp authenticate",
#     "ntp broadcastdelay 22",
#     "ntp clock-period 5",
#     "ntp logging",
#     "ntp master 4",
#     "ntp max-associations 34",
#     "ntp maxdistance 3",
#     "ntp mindistance 10",
#     "ntp orphan 4",
#     "ntp panic update",
#     "ntp source GigabitEthernet0/1",
#     "ntp access-group ipv4 peer DHCP-Server kod",
#     "ntp access-group ipv6 peer preauth_ipv6_acl kod",
#     "ntp access-group peer 2 kod",
#     "ntp access-group query-only 10",
#     "ntp authentication-key 2 md5 SomeSecurePassword 22",
#     "ntp peer 172.16.1.10 version 2",
#     "ntp peer 172.16.1.11 key 2 minpoll 5 prefer  version 2",
#     "ntp peer ip checkPeerDomainIpv4.com prefer",
#     "ntp peer ipv6 checkPeerDomainIpv6.com",
#     "ntp peer ipv6 testPeerDomainIpv6.com prefer",
#     "ntp server 172.16.1.12 version 2",
#     "ntp server ipv6 checkServerDomainIpv6.com",
#     "ntp server 172.16.1.13 source GigabitEthernet0/1",
#     "ntp trusted-key 3 - 3",
#     "ntp trusted-key 21"
# ],

# After state:
# ------------

# router-ios#show running-config | section ^ntp
# ntp max-associations 34
# ntp logging
# ntp allow mode control 4
# ntp panic update
# ntp authentication-key 2 md5 0635002C497D0C1A1005173B0D17393C2B3A37 7
# ntp authenticate
# ntp trusted-key 3 - 3
# ntp trusted-key 21
# ntp orphan 4
# ntp mindistance 10
# ntp maxdistance 3
# ntp broadcastdelay 22
# ntp source GigabitEthernet0/1
# ntp access-group peer 2 kod
# ntp access-group ipv6 peer preauth_ipv6_acl kod
# ntp master 4
# ntp peer 172.16.1.10 version 2
# ntp peer 172.16.1.11 key 2 minpoll 5 prefer version 2
# ntp server 172.16.1.12 version 2
# ntp server 172.16.1.13 source GigabitEthernet0/1
# ntp peer ip checkPeerDomainIpv4.com prefer
# ntp peer ipv6 checkPeerDomainIpv6.com
# ntp peer ipv6 testPeerDomainIpv6.com prefer
# ntp server ipv6 checkServerDomainIpv6.com

# Using state: deleted

# Before state:
# -------------

# router-ios#show running-config | section ^ntp
# ntp max-associations 34
# ntp logging
# ntp allow mode control 4
# ntp panic update
# ntp authentication-key 2 md5 0635002C497D0C1A1005173B0D17393C2B3A37 7
# ntp authenticate
# ntp trusted-key 3 - 3
# ntp trusted-key 21
# ntp orphan 4
# ntp mindistance 10
# ntp maxdistance 3
# ntp broadcastdelay 22
# ntp source GigabitEthernet0/1
# ntp access-group peer 2 kod
# ntp access-group ipv6 peer preauth_ipv6_acl kod
# ntp master 4
# ntp peer 172.16.1.10 version 2
# ntp peer 172.16.1.11 key 2 minpoll 5 prefer version 2
# ntp server 172.16.1.12 version 2
# ntp server 172.16.1.13 source GigabitEthernet0/1
# ntp peer ip checkPeerDomainIpv4.com prefer
# ntp peer ipv6 checkPeerDomainIpv6.com
# ntp peer ipv6 testPeerDomainIpv6.com prefer
# ntp server ipv6 checkServerDomainIpv6.com

# Deleted play:
# -------------

- name: Remove all existing configuration
  cisco.ios.ios_ntp_global:
    state: deleted

# Commands Fired:
# ---------------

# "commands": [
#     "no ntp allow mode control 4",
#     "no ntp authenticate",
#     "no ntp broadcastdelay 22",
#     "no ntp logging",
#     "no ntp master 4",
#     "no ntp max-associations 34",
#     "no ntp maxdistance 3",
#     "no ntp mindistance 10",
#     "no ntp orphan 4",
#     "no ntp panic update",
#     "no ntp source GigabitEthernet0/1",
#     "no ntp access-group peer 2 kod",
#     "no ntp access-group ipv6 peer preauth_ipv6_acl kod",
#     "no ntp authentication-key 2 md5 0635002C497D0C1A1005173B0D17393C2B3A37 7",
#     "no ntp peer 172.16.1.10 version 2",
#     "no ntp peer 172.16.1.11 key 2 minpoll 5 prefer version 2",
#     "no ntp peer ip checkPeerDomainIpv4.com prefer",
#     "no ntp peer ipv6 checkPeerDomainIpv6.com",
#     "no ntp peer ipv6 testPeerDomainIpv6.com prefer",
#     "no ntp server 172.16.1.12 version 2",
#     "no ntp server 172.16.1.13 source GigabitEthernet0/1",
#     "no ntp server ipv6 checkServerDomainIpv6.com",
#     "no ntp trusted-key 21",
#     "no ntp trusted-key 3 - 3"
# ],

# After state:
# ------------

# router-ios#show running-config | section ^ntp
# --------------------- EMPTY -----------------

# Using state: overridden

# Before state:
# -------------

# router-ios#show running-config | section ^ntp
# ntp panic update
# ntp authentication-key 2 md5 00371C0B01680E051A33497E080A16001D1908 7
# ntp authenticate
# ntp trusted-key 3 - 4
# ntp trusted-key 21
# ntp source GigabitEthernet0/1
# ntp peer 172.16.1.10 version 2
# ntp server 172.16.1.12 version 2
# ntp peer ip checkPeerDomainIpv4.com prefer
# ntp server ipv6 checkServerDomainIpv6.com

# Overridden play:
# ----------------

- name: Override commands with provided configuration
  cisco.ios.ios_ntp_global:
    config:
      peers:
        - peer: ipv6DomainNew.com
          use_ipv6: true
        - peer: 172.16.1.100
          prefer: true
          use_ipv4: true
      access_group:
        peer:
        - access_list: DHCP-Server
          ipv6: true
    state: overridden

# Commands Fired:
# ---------------
# "commands": [
#       "no ntp authenticate",
#       "no ntp panic update",
#       "no ntp source GigabitEthernet0/1",
#       "ntp access-group ipv6 peer DHCP-Server",
#       "no ntp authentication-key 2 md5 00371C0B01680E051A33497E080A16001D1908 7",
#       "ntp peer ipv6 ipv6DomainNew.com",
#       "ntp peer 172.16.1.100 prefer",
#       "no ntp peer 172.16.1.10 version 2",
#       "no ntp peer ip checkPeerDomainIpv4.com prefer",
#       "no ntp server 172.16.1.12 version 2",
#       "no ntp server ipv6 checkServerDomainIpv6.com",
#       "no ntp trusted-key 21",
#       "no ntp trusted-key 3 - 4"
#     ],

# After state:
# ------------

# router-ios#show running-config | section ^ntp
# ntp access-group ipv6 peer DHCP-Server
# ntp peer ipv6 ipv6DomainNew.com
# ntp peer 172.16.1.100 prefer

# Using state: replaced

# Before state:
# -------------

# router-ios#show running-config | section ^ntp
# ntp access-group ipv6 peer DHCP-Server
# ntp peer ipv6 ipv6DomainNew.com
# ntp peer 172.16.1.100 prefer

# Replaced play:
# --------------

- name: Replace commands with provided configuration
  cisco.ios.ios_ntp_global:
    config:
      broadcast_delay: 22
      clock_period: 5
      logging: true
      master:
        stratum: 4
      max_associations: 34
      max_distance: 3
      min_distance: 10
      orphan: 4
    state: replaced

# Commands Fired:
# ---------------

# "commands": [
#        "ntp broadcastdelay 22",
#        "ntp clock-period 5",
#        "ntp logging",
#        "ntp master 4",
#        "ntp max-associations 34",
#        "ntp maxdistance 3",
#        "ntp mindistance 10",
#        "ntp orphan 4",
#        "no ntp access-group ipv6 peer DHCP-Server",
#        "no ntp peer 172.16.1.100 prefer",
#        "no ntp peer ipv6 ipv6DomainNew.com"
#     ],

# After state:
# ------------

# router-ios#show running-config | section ^ntp
# ntp max-associations 34
# ntp logging
# ntp orphan 4
# ntp mindistance 10
# ntp maxdistance 3
# ntp broadcastdelay 22
# ntp master 4

# Using state: gathered

# Before state:
# -------------

#router-ios#show running-config | section ^ntp
# ntp max-associations 34
# ntp logging
# ntp allow mode control 4
# ntp panic update
# ntp authentication-key 2 md5 0635002C497D0C1A1005173B0D17393C2B3A37 7
# ntp authenticate
# ntp trusted-key 3 - 3
# ntp trusted-key 21
# ntp orphan 4
# ntp mindistance 10
# ntp maxdistance 3
# ntp broadcastdelay 22
# ntp source GigabitEthernet0/1
# ntp access-group peer 2 kod
# ntp access-group ipv6 peer preauth_ipv6_acl kod
# ntp master 4
# ntp update-calendar
# ntp peer 172.16.1.10 version 2
# ntp peer 172.16.1.11 key 2 minpoll 5 prefer version 2
# ntp server 172.16.1.12 version 2
# ntp server 172.16.1.13 source GigabitEthernet0/1
# ntp peer ip checkPeerDomainIpv4.com prefer
# ntp peer ipv6 checkPeerDomainIpv6.com
# ntp peer ipv6 testPeerDomainIpv6.com prefer
# ntp server ipv6 checkServerDomainIpv6.com

# Gathered play:
# --------------

- name: Gather listed ntp config
  cisco.ios.ios_ntp_global:
    state: gathered

# Module Execution Result:
# ------------------------

# "gathered": {
#   "access_group": {
#       "peer": [
#           {
#               "access_list": "2",
#               "kod": true
#           },
#           {
#               "access_list": "preauth_ipv6_acl",
#               "ipv6": true,
#               "kod": true
#           }
#       ]
#   },
#   "allow": {
#       "control": {
#           "rate_limit": 4
#       }
#   },
#   "authenticate": true,
#   "authentication_keys": [
#       {
#           "algorithm": "md5",
#           "encryption": 7,
#           "id": 2,
#           "key": "0635002C497D0C1A1005173B0D17393C2B3A37"
#       }
#   ],
#   "broadcast_delay": 22,
#   "logging": true,
#   "master": {
#       "stratum": 4
#   },
#   "max_associations": 34,
#   "max_distance": 3,
#   "min_distance": 10,
#   "orphan": 4,
#   "panic_update": true,
#   "peers": [
#       {
#           "peer": "172.16.1.10",
#           "version": 2
#       },
#       {
#           "key": 2,
#           "minpoll": 5,
#           "peer": "172.16.1.11",
#           "prefer": true,
#           "version": 2
#       },
#       {
#           "peer": "checkPeerDomainIpv4.com",
#           "prefer": true,
#           "use_ipv4": true
#       },
#       {
#           "peer": "checkPeerDomainIpv6.com",
#           "use_ipv6": true
#       },
#       {
#           "peer": "testPeerDomainIpv6.com",
#           "prefer": true,
#           "use_ipv6": true
#       }
#   ],
#   "servers": [
#       {
#           "server": "172.16.1.12",
#           "version": 2
#       },
#       {
#           "server": "172.16.1.13",
#           "source": "GigabitEthernet0/1"
#       },
#       {
#           "server": "checkServerDomainIpv6.com",
#           "use_ipv6": true
#       }
#   ],
#   "source": "GigabitEthernet0/1",
#   "trusted_keys": [
#       {
#           "range_start": 21
#       },
#       {
#           "range_end": 3,
#           "range_start": 3
#       }
#   ],
#   "update_calendar": true
# },

# After state:
# -------------

# router-ios#show running-config | section ^ntp
# ntp max-associations 34
# ntp logging
# ntp allow mode control 4
# ntp panic update
# ntp authentication-key 2 md5 0635002C497D0C1A1005173B0D17393C2B3A37 7
# ntp authenticate
# ntp trusted-key 3 - 3
# ntp trusted-key 21
# ntp orphan 4
# ntp mindistance 10
# ntp maxdistance 3
# ntp broadcastdelay 22
# ntp source GigabitEthernet0/1
# ntp access-group peer 2 kod
# ntp access-group ipv6 peer preauth_ipv6_acl kod
# ntp master 4
# ntp update-calendar
# ntp peer 172.16.1.10 version 2
# ntp peer 172.16.1.11 key 2 minpoll 5 prefer version 2
# ntp server 172.16.1.12 version 2
# ntp server 172.16.1.13 source GigabitEthernet0/1
# ntp peer ip checkPeerDomainIpv4.com prefer
# ntp peer ipv6 checkPeerDomainIpv6.com
# ntp peer ipv6 testPeerDomainIpv6.com prefer
# ntp server ipv6 checkServerDomainIpv6.com

# Using state: rendered

# Rendered play:
# --------------

- name: Render the commands for provided configuration
  cisco.ios.ios_ntp_global:
    config:
      access_group:
        peer:
          - access_list: DHCP-Server
            ipv4: true
            kod: true
          - access_list: preauth_ipv6_acl
            ipv6: true
            kod: true
          - access_list: '2'
            kod: true
        query_only:
          - access_list: '10'
      allow:
        control:
          rate_limit: 4
        private: true
      authenticate: true
      authentication_keys:
        - algorithm: md5
          encryption: 22
          id: 2
          key: SomeSecurePassword
      broadcast_delay: 22
      clock_period: 5
      logging: true
      master:
        stratum: 4
      max_associations: 34
      max_distance: 3
      min_distance: 10
      orphan: 4
      panic_update: true
      peers:
        - peer: 172.16.1.10
          version: 2
        - key: 2
          minpoll: 5
          peer: 172.16.1.11
          prefer: true
          version: 2
        - peer: checkPeerDomainIpv4.com
          prefer: true
          use_ipv4: true
        - peer: checkPeerDomainIpv6.com
          use_ipv6: true
        - peer: testPeerDomainIpv6.com
          prefer: true
          use_ipv6: true
      servers:
        - server: 172.16.1.12
          version: 2
        - server: checkServerDomainIpv6.com
          use_ipv6: true
        - server: 172.16.1.13
          source: GigabitEthernet0/1
      source: GigabitEthernet0/1
      trusted_keys:
        - range_end: 3
          range_start: 10
        - range_start: 21
      update_calendar: True
    state: rendered

# Module Execution Result:
# ------------------------

# "rendered": [
#       "ntp allow mode control 4",
#       "ntp allow mode private",
#       "ntp authenticate",
#       "ntp broadcastdelay 22",
#       "ntp clock-period 5",
#       "ntp logging",
#       "ntp master 4",
#       "ntp max-associations 34",
#       "ntp maxdistance 3",
#       "ntp mindistance 10",
#       "ntp orphan 4",
#       "ntp panic update",
#       "ntp source GigabitEthernet0/1",
#       "ntp update-calendar",
#       "ntp access-group ipv4 peer DHCP-Server kod",
#       "ntp access-group ipv6 peer preauth_ipv6_acl kod",
#       "ntp access-group peer 2 kod",
#       "ntp access-group query-only 10",
#       "ntp authentication-key 2 md5 SomeSecurePassword 22",
#       "ntp peer 172.16.1.10 version 2",
#       "ntp peer 172.16.1.11 key 2 minpoll 5 prefer version 2",
#       "ntp peer ip checkPeerDomainIpv4.com prefer",
#       "ntp peer ipv6 checkPeerDomainIpv6.com",
#       "ntp peer ipv6 testPeerDomainIpv6.com prefer",
#       "ntp server 172.16.1.12 version 2",
#       "ntp server ipv6 checkServerDomainIpv6.com",
#       "ntp server 172.16.1.13 source GigabitEthernet0/1",
#       "ntp trusted-key 3 - 3",
#       "ntp trusted-key 21"
#     ]

# Using state: parsed

# File: parsed.cfg
# ----------------

# ntp allow mode control 4
# ntp allow mode private
# ntp authenticate
# ntp broadcastdelay 22
# ntp clock-period 5
# ntp logging
# ntp master 4
# ntp max-associations 34
# ntp maxdistance 3
# ntp mindistance 10
# ntp orphan 4
# ntp panic update
# ntp source GigabitEthernet0/1
# ntp update-calendar
# ntp access-group ipv4 peer DHCP-Server kod
# ntp access-group ipv6 peer preauth_ipv6_acl kod
# ntp access-group peer 2 kod
# ntp access-group query-only 10
# ntp authentication-key 2 md5 SomeSecurePassword 22
# ntp peer 172.16.1.10 version 2
# ntp peer 172.16.1.11 key 2 minpoll 5 prefer version 2
# ntp peer ip checkPeerDomainIpv4.com prefer
# ntp peer ipv6 checkPeerDomainIpv6.com
# ntp peer ipv6 testPeerDomainIpv6.com prefer
# ntp server 172.16.1.12 version 2
# ntp server ipv6 checkServerDomainIpv6.com
# ntp server 172.16.1.13 source GigabitEthernet0/1
# ntp trusted-key 3 - 13
# ntp trusted-key 21

# Parsed play:
# ------------

- name: Parse the provided configuration with the existing running configuration
  cisco.ios.ios_ntp_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------

# "parsed": {
#     "access_group": {
#         "peer": [
#             {
#                 "access_list": "2",
#                 "kod": true
#             },
#             {
#                 "access_list": "DHCP-Server",
#                 "ipv4": true,
#                 "kod": true
#             },
#             {
#                 "access_list": "preauth_ipv6_acl",
#                 "ipv6": true,
#                 "kod": true
#             }
#         ],
#         "query_only": [
#             {
#                 "access_list": "10"
#             }
#         ]
#     },
#     "allow": {
#         "control": {
#             "rate_limit": 4
#         },
#         "private": true
#     },
#     "authenticate": true,
#     "authentication_keys": [
#         {
#             "algorithm": "md5",
#             "encryption": 22,
#             "id": 2,
#             "key": "SomeSecurePassword"
#         }
#     ],
#     "broadcast_delay": 22,
#     "clock_period": 5,
#     "logging": true,
#     "master": {
#         "stratum": 4
#     },
#     "max_associations": 34,
#     "max_distance": 3,
#     "min_distance": 10,
#     "orphan": 4,
#     "panic_update": true,
#     "peers": [
#         {
#             "peer": "172.16.1.10",
#             "version": 2
#         },
#         {
#             "peer": "checkPeerDomainIpv6.com",
#             "use_ipv6": true
#         }
#     ],
#     "servers": [
#         {
#             "server": "172.16.1.12",
#             "version": 2
#         },
#         {
#             "server": "172.16.1.13",
#             "source": "GigabitEthernet0/1"
#         },
#         {
#             "server": "checkServerDomainIpv6.com",
#             "use_ipv6": true
#         }
#     ],
#     "source": "GigabitEthernet0/1",
#     "trusted_keys": [
#         {
#             "range_start": 21
#         },
#         {
#             "range_end": 13,
#             "range_start": 3
#         }
#     ],
#     "update_calendar": true
# }
```

## [Return Values](ios_ntp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  Returned: when changed  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `["ntp peer 20.18.11.3 key 6 minpoll 15 prefer version 2", "ntp access-group ipv4 peer DHCP-Server kod", "ntp trusted-key 9 - 96", "ntp master stratum 2", "ntp orphan 4", "ntp panic update"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  Returned: when *state* is `gathered`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  Returned: when *state* is `parsed`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  Returned: when state is *rendered*  Sample: `["ntp master stratum 2", "ntp server ip testserver.com prefer", "ntp authentication-key 2 md5 testpass 22", "ntp allow mode control 4", "ntp max-associations 34", "ntp broadcastdelay 22"]` |

### Authors

- Sagar Paul (@KB-perByte)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
