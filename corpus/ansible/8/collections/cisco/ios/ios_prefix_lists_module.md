---
collection: ansible
version: "8"
title: "cisco.ios.ios_prefix_lists module – Resource module to configure prefix lists."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_prefix_lists_module.html
fetched_at: 2026-07-28T01:26:24+00:00
---
# cisco.ios.ios_prefix_lists module – Resource module to configure prefix lists.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_prefix_lists`.

New in cisco.ios 2.2.0

- [Synopsis](ios_prefix_lists_module.md#synopsis)
- [Parameters](ios_prefix_lists_module.md#parameters)
- [Notes](ios_prefix_lists_module.md#notes)
- [Examples](ios_prefix_lists_module.md#examples)
- [Return Values](ios_prefix_lists_module.md#return-values)

## [Synopsis](ios_prefix_lists_module.md#id1)

- This module configures and manages the attributes of prefix list on Cisco IOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: prefix_lists

## [Parameters](ios_prefix_lists_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of configurations for Prefix lists. |
| **afi**  string | The Address Family Indicator (AFI) for the prefix list.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **prefix_lists**  list / elements=dictionary | List of Prefix-lists. |
| **description**  string | Prefix-list specific description |
| **entries**  list / elements=dictionary | Prefix-lists supported params. |
| **action**  string | Specify packets to be rejected or forwarded  **Choices:**   - `"deny"` - `"permit"` |
| **description**  string | Prefix-list specific description  Description param at entries level is DEPRECATED  New Description is introduced at prefix_lists level, please use the Description param defined at prefix_lists level instead of Description param at entries level, as at this level description option will get removed in a future release. |
| **ge**  integer | Minimum prefix length to be matched |
| **le**  integer | Maximum prefix length to be matched |
| **prefix**  string | IPv4 prefix <network>/<length>, e.g., A.B.C.D/nn  IPv6 prefix <network>/<length>, e.g., X:X:X:X::X/<0-128> |
| **sequence**  integer | sequence number of an entry |
| **name**  string | Name of a prefix-list |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *merged* is the default state which merges the want and have config, but for Prefix-List module as the IOS platform doesn’t allow update of Prefix-List over an pre-existing Prefix-List, same way Prefix-Lists resource module will error out for respective scenario and only addition of new Prefix-List over new sequence will be allowed with merge state.  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *sh running-config | section ^ip prefix-list|^ipv6 prefix-list* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](ios_prefix_lists_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_prefix_lists_module.md#id4)

```yaml+jinja
# Using deleted by Name

# Before state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is test description
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Delete provided Prefix lists config by Prefix name
  cisco.ios.ios_prefix_lists:
    config:
      - afi: ipv4
        prefix_lists:
          - name: 10
          - name: test_prefix
    state: deleted

#  Commands Fired:
#  ---------------
#
#  "commands": [
#         "no ip prefix-list 10",
#         "no ip prefix-list test_prefix"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

# Using deleted by AFI

# Before state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is test description
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Delete provided Prefix lists config by AFI
  cisco.ios.ios_prefix_lists:
    config:
      - afi: ipv4
    state: deleted

#  Commands Fired:
#  ---------------
#
#  "commands": [
#         "no ip prefix-list test",
#         "no ip prefix-list 10",
#         "no ip prefix-list test_prefix"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

# Using deleted without any config passed (NOTE: This will delete all Prefix lists configuration from device)

# Before state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is test description
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Delete all Prefix lists config
  cisco.ios.ios_prefix_lists:
    state: deleted

# Commands Fired:
# ---------------
#
#  "commands": [
#         "no ip prefix-list test",
#         "no ip prefix-list 10",
#         "no ip prefix-list test_prefix",
#         "no ipv6 prefix-list test_ipv6"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# router-ios#

# Using merged

# Before state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ipv6 prefix-list test_ipv6 description this is ipv6
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Merge provided Prefix lists configuration
  cisco.ios.ios_prefix_lists:
    config:
      - afi: ipv6
        prefix_lists:
          - name: test_ipv6
            description: this is ipv6 merge test
            entries:
              - action: deny
                prefix: 2001:DB8:0:4::/64
                ge: 80
                le: 100
                sequence: 10
    state: merged

# After state:
# -------------
#
# Play Execution fails, with error:
# Cannot update existing sequence 10 of Prefix Lists test_ipv6 with state merged.
# Please use state replaced or overridden.

# Before state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ipv6 prefix-list test_ipv6 description this is ipv6
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Merge provided Prefix lists configuration
  cisco.ios.ios_prefix_lists:
    config:
      - afi: ipv4
        prefix_lists:
          - name: 10
            description: this is new merge test
            entries:
              - action: deny
                prefix: 1.0.0.0/8
                le: 15
                sequence: 5
              - action: deny
                prefix: 35.0.0.0/8
                ge: 10
                sequence: 10
              - action: deny
                prefix: 12.0.0.0/8
                ge: 15
                sequence: 15
              - action: deny
                prefix: 14.0.0.0/8
                ge: 20
                le: 21
                sequence: 20
          - name: test
            description: this is merge test
            entries:
              - action: deny
                prefix: 12.0.0.0/8
                ge: 15
                sequence: 50
          - name: test_prefix
            description: this is for prefix-list
            entries:
              - action: deny
                prefix: 35.0.0.0/8
                ge: 10
                le: 15
                sequence: 5
              - action: deny
                prefix: 35.0.0.0/8
                ge: 20
                sequence: 10
      - afi: ipv6
        prefix_lists:
          - name: test_ipv6
            description: this is ipv6 merge test
            entries:
              - action: deny
                prefix: 2001:DB8:0:4::/64
                ge: 80
                le: 100
                sequence: 20
    state: merged

#  Commands Fired:
#  ---------------
#
#   "commands": [
#         "ip prefix-list test description this is merge test",
#         "ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15",
#         "ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15",
#         "ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10",
#         "ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15",
#         "ip prefix-list 10 description this is new merge test",
#         "ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21",
#         "ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20",
#         "ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15",
#         "ip prefix-list test_prefix description this is for prefix-list",
#         "ipv6 prefix-list test_ipv6 seq 20 deny 2001:DB8:0:4::/64 ge 80 le 100",
#         "ipv6 prefix-list test_ipv6 description this is ipv6 merge test"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is new merge test
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is merge test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 merge test
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80 le 100

# Using overridden

# Before state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is test description
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Override provided Prefix lists configuration
  cisco.ios.ios_prefix_lists:
    config:
      - afi: ipv4
        prefix_lists:
          - name: 10
            description: this is override test
            entries:
              - action: deny
                prefix: 12.0.0.0/8
                ge: 15
                sequence: 15
              - action: deny
                prefix: 14.0.0.0/8
                ge: 20
                le: 21
                sequence: 20
          - name: test_override
            description: this is override test
            entries:
              - action: deny
                prefix: 35.0.0.0/8
                ge: 20
                sequence: 10
      - afi: ipv6
        prefix_lists:
          - name: test_ipv6
            description: this is ipv6 override test
            entries:
              - action: deny
                prefix: 2001:DB8:0:4::/64
                ge: 80
                le: 100
                sequence: 10
    state: overridden

# Commands Fired:
# ---------------
#
#  "commands": [
#         "no ip prefix-list test",
#         "no ip prefix-list test_prefix",
#         "ip prefix-list 10 description this is override test",
#         "no ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10",
#         "no ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15",
#         "ip prefix-list test_override seq 10 deny 35.0.0.0/8 ge 20",
#         "ip prefix-list test_override description this is override test",
#         "no ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80",
#         "ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80 le 100",
#         "ipv6 prefix-list test_ipv6 description this is ipv6 override test"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is override test
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test_override description this is override test
# ip prefix-list test_override seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 override test
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80 le 100

# Using replaced

# Before state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is test description
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Replaced provided Prefix lists configuration
  cisco.ios.ios_prefix_lists:
    config:
      - afi: ipv4
        prefix_lists:
          - name: 10
            description: this is replace test
            entries:
              - action: deny
                prefix: 12.0.0.0/8
                ge: 15
                sequence: 15
              - action: deny
                prefix: 14.0.0.0/8
                ge: 20
                le: 21
                sequence: 20
          - name: test_replace
            description: this is replace test
            entries:
              - action: deny
                prefix: 35.0.0.0/8
                ge: 20
                sequence: 10
      - afi: ipv6
        prefix_lists:
          - name: test_ipv6
            description: this is ipv6 replace test
            entries:
              - action: deny
                prefix: 2001:DB8:0:4::/64
                ge: 80
                le: 100
                sequence: 10
    state: replaced

# Commands Fired:
# ---------------
#  "commands": [
#         "ip prefix-list 10 description this is replace test",
#         "no ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10",
#         "no ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15",
#         "ip prefix-list test_replace seq 10 deny 35.0.0.0/8 ge 20",
#         "ip prefix-list test_replace description this is replace test",
#         "no ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80",
#         "ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80 le 100",
#         "ipv6 prefix-list test_ipv6 description this is ipv6 replace test"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is replace test
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ip prefix-list test_replace description this is replace test
# ip prefix-list test_replace seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 replace test
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80 le 100

# Using Gathered

# Before state:
# -------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is test description
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Gather Prefix lists provided configurations
  cisco.ios.ios_prefix_lists:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "this is test description"
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "le": 15,
#                             "prefix": "1.0.0.0/8",
#                             "sequence": 5
#                         },
#                         {
#                             "action": "deny",
#                             "ge": 10,
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 10
#                         },
#                         {
#                             "action": "deny",
#                             "ge": 15,
#                             "prefix": "12.0.0.0/8",
#                             "sequence": 15
#                         },
#                         {
#                             "action": "deny",
#                             "ge": 20,
#                             "le": 21,
#                             "prefix": "14.0.0.0/8",
#                             "sequence": 20
#                         }
#                     ],
#                     "name": "10"
#                 },
#                 {
#                     "description": "this is test"
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "ge": 15,
#                             "prefix": "12.0.0.0/8",
#                             "sequence": 50
#                         }
#                     ],
#                     "name": "test"
#                 },
#                 {
#                     "description": "this is for prefix-list"
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "ge": 10,
#                             "le": 15,
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 5
#                         },
#                         {
#                             "action": "deny",
#                             "ge": 20,
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 10
#                         }
#                     ],
#                     "name": "test_prefix"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "this is ipv6 prefix-list"
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "ge": 80,
#                             "prefix": "2001:DB8:0:4::/64",
#                             "sequence": 10
#                         }
#                     ],
#                     "name": "test_ipv6"
#                 }
#             ]
#         }
#     ]

# After state:
# ------------
#
# router-ios#sh running-config | section ^ip prefix-list|^ipv6 prefix-list
# ip prefix-list 10 description this is test description
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_prefix_lists:
    config:
      - afi: ipv4
        prefix_lists:
          - name: 10
            description: this is new merge test
            entries:
              - action: deny
                prefix: 1.0.0.0/8
                le: 15
                sequence: 5
              - action: deny
                prefix: 35.0.0.0/8
                ge: 10
                sequence: 10
              - action: deny
                prefix: 12.0.0.0/8
                ge: 15
                sequence: 15
              - action: deny
                prefix: 14.0.0.0/8
                ge: 20
                le: 21
                sequence: 20
          - name: test
            description: this is merge test
            entries:
              - action: deny
                prefix: 12.0.0.0/8
                ge: 15
                sequence: 50
          - name: test_prefix
            description: this is for prefix-list
            entries:
              - action: deny
                prefix: 35.0.0.0/8
                ge: 10
                le: 15
                sequence: 5
              - action: deny
                prefix: 35.0.0.0/8
                ge: 20
                sequence: 10
      - afi: ipv6
        prefix_lists:
          - name: test_ipv6
            description: this is ipv6 merge test
            entries:
              - action: deny
                prefix: 2001:DB8:0:4::/64
                ge: 80
                le: 100
                sequence: 10
    state: rendered

# Module Execution Result:
# ------------------------
#
#  "rendered": [
#         "ip prefix-list test description this is test",
#         "ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15",
#         "ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15",
#         "ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10",
#         "ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15",
#         "ip prefix-list 10 description this is test description",
#         "ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21",
#         "ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20",
#         "ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15",
#         "ip prefix-list test_prefix description this is for prefix-list",
#         "ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80 l2 100",
#         "ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# ip prefix-list 10 description this is test description
# ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15
# ip prefix-list 10 seq 10 deny 35.0.0.0/8 ge 10
# ip prefix-list 10 seq 15 deny 12.0.0.0/8 ge 15
# ip prefix-list 10 seq 20 deny 14.0.0.0/8 ge 20 le 21
# ip prefix-list test description this is test
# ip prefix-list test seq 50 deny 12.0.0.0/8 ge 15
# ip prefix-list test_prefix description this is for prefix-list
# ip prefix-list test_prefix seq 5 deny 35.0.0.0/8 ge 10 le 15
# ip prefix-list test_prefix seq 10 deny 35.0.0.0/8 ge 20
# ipv6 prefix-list test_ipv6 description this is ipv6 prefix-list
# ipv6 prefix-list test_ipv6 seq 10 deny 2001:DB8:0:4::/64 ge 80

- name: Parse the provided configuration with the existing running configuration
  cisco.ios.ios_prefix_lists:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "this is test description"
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "le": 15,
#                             "prefix": "1.0.0.0/8",
#                             "sequence": 5
#                         },
#                         {
#                             "action": "deny",
#                             "ge": 10,
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 10
#                         },
#                         {
#                             "action": "deny",
#                             "ge": 15,
#                             "prefix": "12.0.0.0/8",
#                             "sequence": 15
#                         },
#                         {
#                             "action": "deny",
#                             "ge": 20,
#                             "le": 21,
#                             "prefix": "14.0.0.0/8",
#                             "sequence": 20
#                         }
#                     ],
#                     "name": "10"
#                 },
#                 {
#                     "description": "this is test"
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "ge": 15,
#                             "prefix": "12.0.0.0/8",
#                             "sequence": 50
#                         }
#                     ],
#                     "name": "test"
#                 },
#                 {
#                     "description": "this is for prefix-list"
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "ge": 10,
#                             "le": 15,
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 5
#                         },
#                         {
#                             "action": "deny",
#                             "ge": 20,
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 10
#                         }
#                     ],
#                     "name": "test_prefix"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "this is ipv6 prefix-list"
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "ge": 80,
#                             "prefix": "2001:DB8:0:4::/64",
#                             "sequence": 10
#                         }
#                     ],
#                     "name": "test_ipv6"
#                 }
#             ]
#         }
#     ]
```

## [Return Values](ios_prefix_lists_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["ip prefix-list 10 description this is test description", "ip prefix-list 10 seq 5 deny 1.0.0.0/8 le 15"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
