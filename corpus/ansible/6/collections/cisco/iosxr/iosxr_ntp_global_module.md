---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_ntp_global module – Resource module to configure NTP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_ntp_global_module.html
fetched_at: 2026-07-27T16:55:51+00:00
---
# cisco.iosxr.iosxr_ntp_global module – Resource module to configure NTP.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_ntp_global`.

New in cisco.iosxr 2.5.0

- [Synopsis](iosxr_ntp_global_module.md#synopsis)
- [Parameters](iosxr_ntp_global_module.md#parameters)
- [Notes](iosxr_ntp_global_module.md#notes)
- [Examples](iosxr_ntp_global_module.md#examples)
- [Return Values](iosxr_ntp_global_module.md#return-values)

## [Synopsis](iosxr_ntp_global_module.md#id1)

- This module configures and manages the attributes of ntp on Cisco IOSXR platforms.

## [Parameters](iosxr_ntp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of ntp options |
| **access_group**  dictionary | Control NTP access |
| **ipv4**  dictionary | Configure IPv4 access |
| **peer**  string | Provide full access |
| **query_only**  string | Allow only control queries. |
| **serve**  string | Provide server and query access. |
| **serve_only**  string | Provide only server access. |
| **ipv6**  dictionary | Configure IPv6 access |
| **peer**  string | Provide full access |
| **query_only**  string | Allow only control queries. |
| **serve**  string | Provide server and query access. |
| **serve_only**  string | Provide only server access. |
| **vrfs**  list / elements=dictionary | Specify non-default VRF. |
| **ipv4**  dictionary | Configure IPv4 access |
| **peer**  string | Provide full access |
| **query_only**  string | Allow only control queries. |
| **serve**  string | Provide server and query access. |
| **serve_only**  string | Provide only server access. |
| **ipv6**  dictionary | Configure IPv6 access |
| **peer**  string | Provide full access |
| **query_only**  string | Allow only control queries. |
| **serve**  string | Provide server and query access. |
| **serve_only**  string | Provide only server access. |
| **name**  string | Specify non-default VRF. |
| **authenticate**  boolean | Authenticate time sources  Choices:   - `false` - `true` |
| **authentication_keys**  list / elements=dictionary | Authentication key for trusted time sources |
| **encryption**  boolean | Type of key encrypted or clear-text.  Choices:   - `false` - `true` |
| **id**  integer | <1-65535> Key number |
| **key**  string | Authentication key. |
| **broadcastdelay**  integer | Estimated round-trip delay in microseconds. |
| **drift**  dictionary | Drift(cisco-support) |
| **aging_time**  integer | Aging time in hours. |
| **file**  string | File for drift values. |
| **interfaces**  list / elements=dictionary | Configure NTP on an interface. |
| **broadcast_client**  boolean | Listen to NTP broadcasts  Choices:   - `false` - `true` |
| **broadcast_destination**  string | Configure broadcast destination address. |
| **broadcast_key**  integer | Broadcast key number. |
| **broadcast_version**  integer | <2-4> NTP version number. |
| **multicast_client**  string | Configure multicast client |
| **multicast_destination**  string | Configure multicast destination |
| **multicast_key**  integer | Configure multicast authentication key. |
| **multicast_ttl**  integer | Configure TTL to use. |
| **multicast_version**  integer | <2-4> NTP version number. |
| **name**  string | Name of the interface. |
| **vrf**  string | Name of the vrf. |
| **ipv4**  dictionary | Mark the dscp/precedence bit for ipv4 packets. |
| **dscp**  string | Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries. |
| **precedence**  string | Set precedence Please refer vendor document for valid entries.  Choices:   - `"critical"` - `"flash"` - `"flash-override"` - `"immediate"` - `"internet"` - `"network"` - `"priority"` - `"routine"` |
| **ipv6**  dictionary | Mark the dscp/precedence bit for ipv4 packets. |
| **dscp**  string | Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries. |
| **precedence**  string | Set precedence Please refer vendor document for valid entries.  Choices:   - `"critical"` - `"flash"` - `"flash-override"` - `"immediate"` - `"internet"` - `"network"` - `"priority"` - `"routine"` |
| **log_internal_sync**  boolean | Logs internal synchronization changes.  Choices:   - `false` - `true` |
| **master**  dictionary | Act as NTP master clock |
| **stratum**  integer | Use NTP as clock source with stratum number <1-15> |
| **max_associations**  integer | <0-4294967295> Number of associations. |
| **passive**  boolean | Enable the passive associations.  Choices:   - `false` - `true` |
| **peers**  list / elements=dictionary | Configure NTP peer. |
| **burst**  boolean | Use burst mode.  Choices:   - `false` - `true` |
| **iburst**  boolean | Use initial burst mode.  Choices:   - `false` - `true` |
| **key_id**  integer | SConfigure peer authentication key |
| **maxpoll**  integer | configure Maximum poll interval. |
| **minpoll**  integer | configure Minimum poll interval. |
| **peer**  string / required | Hostname or A.B.C.D or A:B:C:D:E:F:G:H. |
| **prefer**  boolean | Prefer this peer when possible  Choices:   - `false` - `true` |
| **source**  string | Interface for source address. |
| **version**  integer | NTP version. |
| **vrf**  string | vrf name. |
| **servers**  list / elements=dictionary | Configure NTP server. |
| **burst**  boolean | Use burst mode.  Choices:   - `false` - `true` |
| **iburst**  boolean | Use initial burst mode.  Choices:   - `false` - `true` |
| **key_id**  integer | SConfigure peer authentication key |
| **maxpoll**  integer | configure Maximum poll interval. |
| **minpoll**  integer | configure Minimum poll interval. |
| **prefer**  boolean | Prefer this peer when possible  Choices:   - `false` - `true` |
| **server**  string / required | Hostname or A.B.C.D or A:B:C:D:E:F:G:H. |
| **source**  string | Interface for source address. |
| **version**  integer | NTP version. |
| **vrf**  string | vrf name. |
| **source_interface**  string | Configure default interface. |
| **source_vrfs**  list / elements=dictionary | Configure default interface. |
| **name**  string | Name of source interface. |
| **vrf**  string | vrf name. |
| **trusted_keys**  list / elements=dictionary | list of Key numbers for trusted time sources. |
| **key_id**  integer | Key numbers for trusted time sources. |
| **update_calendar**  boolean | Periodically update calendar with NTP time.  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOSXR device by executing the command **show running-config ntp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](iosxr_ntp_global_module.md#id3)

> **Note:**
>
> - Tested against IOSXR 7.0.2.
> - This module works with connection `network_cli`.

## [Examples](iosxr_ntp_global_module.md#id4)

```yaml+jinja
# Using state: merged
# Before state:
# -------------
# RP/0/0/CPU0:10#show running-config ntp
# --------------------- EMPTY -----------------
# Merged play:
# ------------
- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_ntp_global:
      config:
          access_group:
            ipv4:
              peer: PeerAcl1
              query_only: QueryOnlyAcl1
              serve: ServeAcl1
              serve_only: ServeOnlyAcl1
            vrfs:
              - ipv4:
                  peer: PeerAcl3
                  serve: ServeAcl2
                name: siteA
          authenticate: true
          broadcastdelay: 1
          drift:
            aging_time: 0
            file: apphost
          interfaces:
            - name: GigabitEthernet0/0/0/0
              multicast_client: 224.0.0.8
              multicast_destination: 224.0.0.8
              broadcast_client: true
          ipv4:
            dscp: af11
          ipv6:
            precedence: routine
          log_internal_sync: true
          master: 1
          max_associations: 10
          passive: true
          peers:
            - iburst: true
              peer: 192.0.2.1
              vrf: siteC
          servers:
            - burst: true
              server: 192.0.2.2
              vrf: siteD
          source: GigabitEthernet0/0/0/0
          source_vrfs:
            - name: GigabitEthernet0/0/0/0
              vrf: siteE
          trusted_keys:
            - key_id: 1
          update_calendar: true
# Commands Fired:
# ------------
# "commands": [
#         "ntp peer vrf siteC 192.0.2.1 iburst ",
#         "ntp server vrf siteD 192.0.2.2 burst ",
#         "ntp trusted-key 1",
#         "ntp interface GigabitEthernet0/0/0/0 broadcast client",
#         "ntp interface GigabitEthernet0/0/0/0 multicast destination 224.0.0.8",
#         "ntp interface GigabitEthernet0/0/0/0 multicast client 224.0.0.8",
#         "ntp vrf siteE source GigabitEthernet0/0/0/0",
#         "ntp access-group vrf siteA ipv4 serve ServeAcl2",
#         "ntp access-group vrf siteA ipv4 peer PeerAcl3",
#         "ntp access-group ipv4 peer PeerAcl1",
#         "ntp access-group ipv4 serve ServeAcl1",
#         "ntp access-group ipv4 serve-only ServeOnlyAcl1",
#         "ntp access-group ipv4 query-only QueryOnlyAcl1",
#         "ntp authenticate",
#         "ntp log-internal-sync",
#         "ntp broadcastdelay 1",
#         "ntp drift aging time 0",
#         "ntp drift file apphost",
#         "ntp ipv4 dscp af11",
#         "ntp ipv6 precedence routine",
#         "ntp max-associations 10",
#         "ntp master 1",
#         "ntp passive",
#         "ntp update-calendar",
#         "ntp source GigabitEthernet0/0/0/0"
#     ],
# After state:
# ------------
# RP/0/0/CPU0:10#show running-config ntp
# ntp
#  max-associations 10
#  interface GigabitEthernet0/0/0/0
#   broadcast client
#   multicast client 224.0.0.8
#   multicast destination 224.0.0.8
#  !
#  authenticate
#  trusted-key 1
#  ipv4 dscp af11
#  ipv6 precedence routine
#  peer vrf siteC 192.0.2.1 iburst
#  server vrf siteD 192.0.2.2 burst
#  drift file apphost
#  drift aging time 0
#  master 1
#  access-group vrf siteA ipv4 peer PeerAcl3
#  access-group vrf siteA ipv4 serve ServeAcl2
#  access-group ipv4 peer PeerAcl1
#  access-group ipv4 serve ServeAcl1
#  access-group ipv4 serve-only ServeOnlyAcl1
#  access-group ipv4 query-only QueryOnlyAcl1
#  source vrf siteE GigabitEthernet0/0/0/0
#  source GigabitEthernet0/0/0/0
#  passive
#  broadcastdelay 1
#  update-calendar
#  log-internal-sync
# !
# Using state: deleted
# Before state:
# -------------
# RP/0/0/CPU0:10#show running-config ntp
# ntp
#  max-associations 10
#  interface GigabitEthernet0/0/0/0
#   broadcast client
#   multicast client 224.0.0.8
#   multicast destination 224.0.0.8
#  !
#  authenticate
#  trusted-key 1
#  ipv4 dscp af11
#  ipv6 precedence routine
#  peer vrf siteC 192.0.2.1 iburst
#  server vrf siteD 192.0.2.2 burst
#  drift file apphost
#  drift aging time 0
#  master 1
#  access-group vrf siteA ipv4 peer PeerAcl3
#  access-group vrf siteA ipv4 serve ServeAcl2
#  access-group ipv4 peer PeerAcl1
#  access-group ipv4 serve ServeAcl1
#  access-group ipv4 serve-only ServeOnlyAcl1
#  access-group ipv4 query-only QueryOnlyAcl1
#  source vrf siteE GigabitEthernet0/0/0/0
#  source GigabitEthernet0/0/0/0
#  passive
#  broadcastdelay 1
#  update-calendar
#  log-internal-sync
# !
# Deleted play:
# -------------
- name: Remove all existing configuration
  cisco.iosxr.iosxr_ntp_global:
    state: deleted
# Commands Fired:
# ---------------
# "commands": [
#         "no ntp peer vrf siteC 192.0.2.1 iburst ",
#         "no ntp server vrf siteD 192.0.2.2 burst ",
#         "no ntp trusted-key 1",
#         "no ntp interface GigabitEthernet0/0/0/0",
#         "no ntp vrf siteE source GigabitEthernet0/0/0/0",
#         "no ntp access-group vrf siteA ipv4 serve ServeAcl2",
#         "no ntp access-group vrf siteA ipv4 peer PeerAcl3",
#         "no ntp access-group ipv4 peer PeerAcl1",
#         "no ntp access-group ipv4 serve ServeAcl1",
#         "no ntp access-group ipv4 serve-only ServeOnlyAcl1",
#         "no ntp access-group ipv4 query-only QueryOnlyAcl1",
#         "no ntp authenticate",
#         "no ntp log-internal-sync",
#         "no ntp broadcastdelay 1",
#         "no ntp drift aging time 0",
#         "no ntp drift file apphost",
#         "no ntp ipv4 dscp af11",
#         "no ntp ipv6 precedence routine",
#         "no ntp max-associations 10",
#         "no ntp master 1",
#         "no ntp passive",
#         "no ntp update-calendar",
#         "no ntp source GigabitEthernet0/0/0/0"
#     ],
# After state:
# ------------
# RP/0/0/CPU0:10#show running-config ntp
# --------------------- EMPTY -----------------
# Using state: overridden
# Before state:
# -------------
# RP/0/0/CPU0:10#show running-config ntp
# ntp
#  max-associations 10
#  interface GigabitEthernet0/0/0/0
#   broadcast client
#   multicast client 224.0.0.8
#   multicast destination 224.0.0.8
#  !
#  authenticate
#  trusted-key 1
#  ipv4 dscp af11
#  ipv6 precedence routine
#  peer vrf siteC 192.0.2.1 iburst
#  server vrf siteD 192.0.2.2 burst
#  drift file apphost
#  drift aging time 0
#  master 1
#  access-group vrf siteA ipv4 peer PeerAcl3
#  access-group vrf siteA ipv4 serve ServeAcl2
#  access-group ipv4 peer PeerAcl1
#  access-group ipv4 serve ServeAcl1
#  access-group ipv4 serve-only ServeOnlyAcl1
#  access-group ipv4 query-only QueryOnlyAcl1
#  source vrf siteE GigabitEthernet0/0/0/0
#  source GigabitEthernet0/0/0/0
#  passive
#  broadcastdelay 1
#  update-calendar
#  log-internal-sync
# !
# Overridden play:
# ----------------
- name: Override BGP configuration with provided configuration
  cisco.iosxr.iosxr_ntp_global:
        state: overridden
        config:
          access_group:
            ipv4:
              peer: PeerAcl1
              query_only: QueryOnlyAcl1
              serve: ServeAcl4
              serve_only: ServeOnlyAcl1
            vrfs:
              - ipv4:
                  peer: PeerAcl3
                  serve: ServeAcl2
                name: siteA
          authenticate: true
          broadcastdelay: 1
          drift:
            aging_time: 0
            file: apphost
          interfaces:
            - name: GigabitEthernet0/0/0/1
              multicast_client: 224.0.0.8
              multicast_destination: 224.0.0.8
              broadcast_client: true
          ipv4:
            dscp: af12
          ipv6:
            precedence: routine
          log_internal_sync: true
          master: 1
          max_associations: 10
          passive: true
          peers:
            - iburst: true
              peer: 192.0.2.3
              vrf: siteC
          servers:
            - burst: true
              server: 192.0.2.2
              vrf: siteD
          source: GigabitEthernet0/0/0/1
          source_vrfs:
            - name: GigabitEthernet0/0/0/0
              vrf: siteE
          trusted_keys:
            - key_id: 1
          update_calendar: true
# Commands Fired:
# ---------------
# "commands": [
#         "no ntp peer vrf siteC 192.0.2.1 iburst ",
#         "no ntp interface GigabitEthernet0/0/0/0",
#         "ntp peer vrf siteC 192.0.2.3 iburst ",
#         "ntp interface GigabitEthernet0/0/0/1 broadcast client",
#         "ntp interface GigabitEthernet0/0/0/1 multicast destination 224.0.0.8",
#         "ntp interface GigabitEthernet0/0/0/1 multicast client 224.0.0.8",
#         "ntp access-group ipv4 serve ServeAcl4",
#         "ntp ipv4 dscp af12",
#         "ntp source GigabitEthernet0/0/0/1"
#     ],
# After state:
# ------------
# RP/0/RP0/CPU0:ios#show running-config ntp
# Mon Sep 13 10:38:22.690 UTC
# ntp
#  max-associations 10
#  interface GigabitEthernet0/0/0/1
#   broadcast client
#   multicast client 224.0.0.8
#   multicast destination 224.0.0.8
#  !
#  authentication-key 1 md5 encrypted testkey
#  authenticate
#  trusted-key 1
#  ipv4 dscp af12
#  ipv6 precedence routine
#  peer vrf siteC 192.0.2.3 iburst
#  server vrf siteD 192.0.2.2 burst
#  drift file apphost
#  drift aging time 0
#  master 1
#  access-group vrf siteA ipv4 peer PeerAcl3
#  access-group vrf siteA ipv4 serve ServeAcl2
#  access-group ipv4 peer PeerAcl1
#  access-group ipv4 serve ServeAcl4
#  access-group ipv4 serve-only ServeOnlyAcl1
#  access-group ipv4 query-only QueryOnlyAcl1
#  source vrf siteE GigabitEthernet0/0/0/0
#  source GigabitEthernet0/0/0/1
#  passive
#  broadcastdelay 1
#  update-calendar
#  log-internal-sync
# !
#
# Using state: replaced
# Before state:
# -------------
# RP/0/0/CPU0:10#show running-config ntp
# ntp
#  max-associations 10
#  interface GigabitEthernet0/0/0/0
#   broadcast client
#   multicast client 224.0.0.8
#   multicast destination 224.0.0.8
#  !
#  authenticate
#  trusted-key 1
#  ipv4 dscp af11
#  ipv6 precedence routine
#  peer vrf siteC 192.0.2.1 iburst
#  server vrf siteD 192.0.2.2 burst
#  drift file apphost
#  drift aging time 0
#  master 1
#  access-group vrf siteA ipv4 peer PeerAcl3
#  access-group vrf siteA ipv4 serve ServeAcl2
#  access-group ipv4 peer PeerAcl1
#  access-group ipv4 serve ServeAcl1
#  access-group ipv4 serve-only ServeOnlyAcl1
#  access-group ipv4 query-only QueryOnlyAcl1
#  source vrf siteE GigabitEthernet0/0/0/0
#  source GigabitEthernet0/0/0/0
#  passive
#  broadcastdelay 1
#  update-calendar
#  log-internal-sync
# !
# Replaced play:
# ----------------
- name: Replaced BGP configuration with provided configuration
  cisco.iosxr.iosxr_ntp_global:
        state: replaced
        config:
          access_group:
            ipv4:
              peer: PeerAcl1
              query_only: QueryOnlyAcl1
              serve: ServeAcl4
              serve_only: ServeOnlyAcl1
            vrfs:
              - ipv4:
                  peer: PeerAcl3
                  serve: ServeAcl2
                name: siteA
          authenticate: true
          broadcastdelay: 1
          drift:
            aging_time: 0
            file: apphost
          interfaces:
            - name: GigabitEthernet0/0/0/1
              multicast_client: 224.0.0.8
              multicast_destination: 224.0.0.8
              broadcast_client: true
          ipv4:
            dscp: af12
          ipv6:
            precedence: routine
          log_internal_sync: true
          master: 1
          max_associations: 10
          passive: true
          peers:
            - iburst: true
              peer: 192.0.2.3
              vrf: siteC
          servers:
            - burst: true
              server: 192.0.2.2
              vrf: siteD
          source: GigabitEthernet0/0/0/1
          source_vrfs:
            - name: GigabitEthernet0/0/0/0
              vrf: siteE
          trusted_keys:
            - key_id: 1
          update_calendar: true
# Commands Fired:
# ---------------
# "commands": [
#         "no ntp peer vrf siteC 192.0.2.1 iburst ",
#         "no ntp interface GigabitEthernet0/0/0/0",
#         "ntp peer vrf siteC 192.0.2.3 iburst ",
#         "ntp interface GigabitEthernet0/0/0/1 broadcast client",
#         "ntp interface GigabitEthernet0/0/0/1 multicast destination 224.0.0.8",
#         "ntp interface GigabitEthernet0/0/0/1 multicast client 224.0.0.8",
#         "ntp access-group ipv4 serve ServeAcl4",
#         "ntp ipv4 dscp af12",
#         "ntp source GigabitEthernet0/0/0/1"
#     ],
# After state:
# ------------
# RP/0/RP0/CPU0:ios#show running-config ntp
# Mon Sep 13 10:38:22.690 UTC
# ntp
#  max-associations 10
#  interface GigabitEthernet0/0/0/1
#   broadcast client
#   multicast client 224.0.0.8
#   multicast destination 224.0.0.8
#  !
#  authentication-key 1 md5 encrypted testkey
#  authenticate
#  trusted-key 1
#  ipv4 dscp af12
#  ipv6 precedence routine
#  peer vrf siteC 192.0.2.3 iburst
#  server vrf siteD 192.0.2.2 burst
#  drift file apphost
#  drift aging time 0
#  master 1
#  access-group vrf siteA ipv4 peer PeerAcl3
#  access-group vrf siteA ipv4 serve ServeAcl2
#  access-group ipv4 peer PeerAcl1
#  access-group ipv4 serve ServeAcl4
#  access-group ipv4 serve-only ServeOnlyAcl1
#  access-group ipv4 query-only QueryOnlyAcl1
#  source vrf siteE GigabitEthernet0/0/0/0
#  source GigabitEthernet0/0/0/1
#  passive
#  broadcastdelay 1
#  update-calendar
#  log-internal-sync
# !
# Using state: gathered
# Before state:
# -------------
# RP/0/0/CPU0:10#show running-config ntp
# ntp
#  max-associations 10
#  interface GigabitEthernet0/0/0/0
#   broadcast client
#   multicast client 224.0.0.8
#   multicast destination 224.0.0.8
#  !
#  authenticate
#  trusted-key 1
#  ipv4 dscp af11
#  ipv6 precedence routine
#  peer vrf siteC 192.0.2.1 iburst
#  server vrf siteD 192.0.2.2 burst
#  drift file apphost
#  drift aging time 0
#  master 1
#  access-group vrf siteA ipv4 peer PeerAcl3
#  access-group vrf siteA ipv4 serve ServeAcl2
#  access-group ipv4 peer PeerAcl1
#  access-group ipv4 serve ServeAcl1
#  access-group ipv4 serve-only ServeOnlyAcl1
#  access-group ipv4 query-only QueryOnlyAcl1
#  source vrf siteE GigabitEthernet0/0/0/0
#  source GigabitEthernet0/0/0/0
#  passive
#  broadcastdelay 1
#  update-calendar
#  log-internal-sync
# !
# Gathered play:
# --------------
- name: Gather listed ntp config
  cisco.iosxr.iosxr_ntp_global:
    state: gathered
# Module Execution Result:
# ------------------------
# "gathered":{
#         "access_group": {
#             "ipv4": {
#                 "peer": "PeerAcl1",
#                 "query_only": "QueryOnlyAcl1",
#                 "serve": "ServeAcl1",
#                 "serve_only": "ServeOnlyAcl1"
#             },
#             "vrfs": [
#                 {
#                     "ipv4": {
#                         "peer": "PeerAcl3",
#                         "serve": "ServeAcl2"
#                     },
#                     "name": "siteA"
#                 }
#             ]
#         },
#         "authenticate": true,
#         "broadcastdelay": 1,
#         "drift": {
#             "aging_time": 0,
#             "file": "apphost"
#         },
#         "interfaces": [
#             {
#                 "broadcast_client": true,
#                 "multicast_client": "224.0.0.8",
#                 "multicast_destination": "224.0.0.8",
#                 "name": "GigabitEthernet0/0/0/0"
#             }
#         ],
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "ipv6": {
#             "precedence": "routine"
#         },
#         "log_internal_sync": true,
#         "master": 1,
#         "max_associations": 10,
#         "passive": true,
#         "peers": [
#             {
#                 "iburst": true,
#                 "peer": "192.0.2.1",
#                 "vrf": "siteC"
#             }
#         ],
#         "servers": [
#             {
#                 "burst": true,
#                 "server": "192.0.2.2",
#                 "vrf": "siteD"
#             }
#         ],
#         "source": "GigabitEthernet0/0/0/0",
#         "source_vrfs": [
#             {
#                 "name": "GigabitEthernet0/0/0/0",
#                 "vrf": "siteE"
#             }
#         ],
#         "trusted_keys": [
#             {
#                 "key_id": 1
#             }
#         ],
#         "update_calendar": true
#     }
# Using state: rendered
# Rendered play:
# --------------
- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.iosxr.iosxr_ntp_global:
    state: rendered
    config:
      access_group:
        ipv4:
          peer: PeerAcl1
          query_only: QueryOnlyAcl1
          serve: ServeAcl1
          serve_only: ServeOnlyAcl1
        vrfs:
          - ipv4:
              peer: PeerAcl3
              serve: ServeAcl2
            name: siteA
      authenticate: true
      broadcastdelay: 1
      drift:
        aging_time: 0
        file: apphost
      interfaces:
        - name: GigabitEthernet0/0/0/0
          multicast_client: 224.0.0.8
          multicast_destination: 224.0.0.8
          broadcast_client: true
      ipv4:
        dscp: af11
      ipv6:
        precedence: routine
      log_internal_sync: true
      master: 1
      max_associations: 10
      passive: true
      peers:
        - iburst: true
          peer: 192.0.2.1
          vrf: siteC
      servers:
        - burst: true
          server: 192.0.2.2
          vrf: siteD
      source: GigabitEthernet0/0/0/0
      source_vrfs:
        - name: GigabitEthernet0/0/0/0
          vrf: siteE
      trusted_keys:
        - key_id: 1
      update_calendar: true
  register: result
# Module Execution Result:
# ------------------------
# "rendered": [
#         "ntp peer vrf siteC 192.0.2.1 iburst ",
#         "ntp server vrf siteD 192.0.2.2 burst ",
#         "ntp trusted-key 1",
#         "ntp interface GigabitEthernet0/0/0/0 broadcast client",
#         "ntp interface GigabitEthernet0/0/0/0 multicast destination 224.0.0.8",
#         "ntp interface GigabitEthernet0/0/0/0 multicast client 224.0.0.8",
#         "ntp vrf siteE source GigabitEthernet0/0/0/0",
#         "ntp access-group vrf siteA ipv4 serve ServeAcl2",
#         "ntp access-group vrf siteA ipv4 peer PeerAcl3",
#         "ntp access-group ipv4 peer PeerAcl1",
#         "ntp access-group ipv4 serve ServeAcl1",
#         "ntp access-group ipv4 serve-only ServeOnlyAcl1",
#         "ntp access-group ipv4 query-only QueryOnlyAcl1",
#         "ntp authenticate",
#         "ntp log-internal-sync",
#         "ntp broadcastdelay 1",
#         "ntp drift aging time 0",
#         "ntp drift file apphost",
#         "ntp ipv4 dscp af11",
#         "ntp ipv6 precedence routine",
#         "ntp max-associations 10",
#         "ntp master 1",
#         "ntp passive",
#         "ntp update-calendar",
#         "ntp source GigabitEthernet0/0/0/0"
#     ],
# Using state: parsed
# File: parsed.cfg
# ----------------
# ntp
#  max-associations 10
#  interface GigabitEthernet0/0/0/0
#   broadcast client
#   multicast client 224.0.0.8
#   multicast destination 224.0.0.8
#  !
#  authenticate
#  trusted-key 1
#  ipv4 dscp af11
#  ipv6 precedence routine
#  peer vrf siteC 192.0.2.1 iburst
#  server vrf siteD 192.0.2.2 burst
#  drift file apphost
#  drift aging time 0
#  master 1
#  access-group vrf siteA ipv4 peer PeerAcl3
#  access-group vrf siteA ipv4 serve ServeAcl2
#  access-group ipv4 peer PeerAcl1
#  access-group ipv4 serve ServeAcl1
#  access-group ipv4 serve-only ServeOnlyAcl1
#  access-group ipv4 query-only QueryOnlyAcl1
#  source vrf siteE GigabitEthernet0/0/0/0
#  source GigabitEthernet0/0/0/0
#  passive
#  broadcastdelay 1
#  update-calendar
#  log-internal-sync
# !
# Parsed play:
# ------------
- name: Parse the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_ntp_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed
# Module Execution Result:
# ------------------------
# "parsed":{
#         "access_group": {
#             "ipv4": {
#                 "peer": "PeerAcl1",
#                 "query_only": "QueryOnlyAcl1",
#                 "serve": "ServeAcl1",
#                 "serve_only": "ServeOnlyAcl1"
#             },
#             "vrfs": [
#                 {
#                     "ipv4": {
#                         "peer": "PeerAcl3",
#                         "serve": "ServeAcl2"
#                     },
#                     "name": "siteA"
#                 }
#             ]
#         },
#         "authenticate": true,
#         "broadcastdelay": 1,
#         "drift": {
#             "aging_time": 0,
#             "file": "apphost"
#         },
#         "interfaces": [
#             {
#                 "broadcast_client": true,
#                 "multicast_client": "224.0.0.8",
#                 "multicast_destination": "224.0.0.8",
#                 "name": "GigabitEthernet0/0/0/0"
#             }
#         ],
#         "ipv4": {
#             "dscp": "af11"
#         },
#         "ipv6": {
#             "precedence": "routine"
#         },
#         "log_internal_sync": true,
#         "master": 1,
#         "max_associations": 10,
#         "passive": true,
#         "peers": [
#             {
#                 "iburst": true,
#                 "peer": "192.0.2.1",
#                 "vrf": "siteC"
#             }
#         ],
#         "servers": [
#             {
#                 "burst": true,
#                 "server": "192.0.2.2",
#                 "vrf": "siteD"
#             }
#         ],
#         "source": "GigabitEthernet0/0/0/0",
#         "source_vrfs": [
#             {
#                 "name": "GigabitEthernet0/0/0/0",
#                 "vrf": "siteE"
#             }
#         ],
#         "trusted_keys": [
#             {
#                 "key_id": 1
#             }
#         ],
#         "update_calendar": true
#     }
```

## [Return Values](iosxr_ntp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  Returned: when changed  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  Sample: `["sample command 1", "sample command 2", "sample command 3"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  Returned: when *state* is `gathered`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  Returned: when *state* is `parsed`  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  Returned: when *state* is `rendered`  Sample: `["sample command 1", "sample command 2", "sample command 3"]` |

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
