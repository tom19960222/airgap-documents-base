---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_prefix_lists module – Resource module to configure prefix lists."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_prefix_lists_module.html
fetched_at: 2026-07-28T01:26:57+00:00
---
# cisco.iosxr.iosxr_prefix_lists module – Resource module to configure prefix lists.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_prefix_lists`.

New in cisco.iosxr 2.3.0

- [Synopsis](iosxr_prefix_lists_module.md#synopsis)
- [Parameters](iosxr_prefix_lists_module.md#parameters)
- [Notes](iosxr_prefix_lists_module.md#notes)
- [Examples](iosxr_prefix_lists_module.md#examples)
- [Return Values](iosxr_prefix_lists_module.md#return-values)

## [Synopsis](iosxr_prefix_lists_module.md#id1)

- This module manages prefix-lists configuration on devices running Cisco IOSXR.

Aliases: prefix_lists

## [Parameters](iosxr_prefix_lists_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of prefix-lists configuration. |
| **afi**  string | The Address Family Identifier (AFI) for the prefix-lists.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **prefix_lists**  list / elements=dictionary | List of prefix-list configurations. |
| **entries**  list / elements=dictionary | List of configurations for the specified prefix-list |
| **action**  string | Prefix-List permit or deny.  **Choices:**   - `"permit"` - `"deny"` - `"remark"` |
| **description**  string | Description of the prefix list. only applicable for action “remark”. |
| **eq**  integer | Exact prefix length to be matched. |
| **ge**  integer | Minimum prefix length to be matched. |
| **le**  integer | Maximum prefix length to be matched. |
| **prefix**  string | IP or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format. only applicable for action “permit” and “deny” |
| **sequence**  integer | Sequence Number. |
| **name**  string | Name of the prefix-list. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Iosxr device by executing the command **show running-config prefix-list**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Refer to examples for more details.  With state *replaced*, for the listed prefix-lists, sequences that are in running-config but not in the task are negated.  With state *overridden*, all prefix-lists that are in running-config but not in the task are negated.  Please refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](iosxr_prefix_lists_module.md#id3)

> **Note:**
>
> - Tested against IOSXR 7.0.2.
> - This module works with connection `network_cli`.

## [Examples](iosxr_prefix_lists_module.md#id4)

```yaml+jinja
# Using merged
# Before state
#RP/0/0/CPU0:10#show running-config
#Thu Feb  4 09:38:36.245 UTC
#% No such configuration item(s)
#RP/0/0/CPU0:10#
#
- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_prefix_lists:
         state: merged
         config:
           - afi: ipv6
             prefix_lists:
               - name: pl_1
                 entries:
                   - prefix: 2001:db8:1234::/48
                     action: deny
                     sequence: 1
               - name: pl_2
                 entries:
                   - sequence: 2
                     action: remark
                     description: TEST_PL_2_REMARK
           - afi: ipv4
             prefix_lists:
               - name: pl1
                 entries:
                   - sequence: 3
                     action: remark
                     description: TEST_PL1_2_REMARK
                   - sequence: 4
                     action: permit
                     prefix: 10.0.0.0/24
               - name: pl2
                 entries:
                   - sequence: 5
                     action: remark
                     description: TEST_PL2_REMARK
               - name: pl3
                 entries:
                   - sequence: 6
                     action: permit
                     prefix: 35.0.0.0/8
                     eq: 0

#
# After state:
#
#RP/0/0/CPU0:10#show running-config
# ipv6 prefix-list pl_1
#  1 deny 2001:db8:1234::/48
# !
# ipv6 prefix-list pl_2
#  2 remark TEST_PL_2_REMARK
# !
# ipv4 prefix-list pl1
#  3 remark TEST_PL1_2_REMARK
#  4 permit 10.0.0.0/24
# !
# ipv4 prefix-list pl2
#  5 remark TEST_PL2_REMARK
# !
# ipv4 prefix-list pl3
#  6 permit 35.0.0.0/8 eq 0
# !

#Module execution
#
# "after": [
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "prefix": "2001:db8:1234::/48",
#                             "sequence": 1
#                         }
#                     ],
#                     "name": "pl_1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL_2_REMARK",
#                             "sequence": 2
#                         }
#                     ],
#                     "name": "pl_2"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL1_2_REMARK",
#                             "sequence": 3
#                         },
#                         {
#                             "action": "permit",
#                             "prefix": "10.0.0.0/24",
#                             "sequence": 4
#                         }
#                     ],
#                     "name": "pl1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL2_REMARK",
#                             "sequence": 5
#                         }
#                     ],
#                     "name": "pl2"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 6,
#                             "eq": 0
#                         }
#                     ],
#                     "name": "pl3"
#                 },
#             ]
#         }
#     ],
#     "before": [],
#     "changed": true,
#     "commands": [
#         "ipv6 prefix-list pl_1 1 deny 2001:db8:1234::/48",
#         "ipv6 prefix-list pl_2 2 remark TEST_PL_2_REMARK",
#         "ipv4 prefix-list pl1 3 remark TEST_PL1_2_REMARK",
#         "ipv4 prefix-list pl1 4 permit 10.0.0.0/24",
#         "ipv4 prefix-list pl2 5 remark TEST_PL2_REMARK"
#         "ipv4 prefix-list pl3 6 permit 35.0.0.0/8 eq 0"
#     ]
#-----------------------------------------------------------------------
# Using replaced:
# --------------
# Before state
#RP/0/0/CPU0:10#show running-config
#
# ipv6 prefix-list pl_1
#  1 deny 2001:db8:1234::/48
# !
# ipv6 prefix-list pl_2
#  2 remark TEST_PL_2_REMARK
# !
# ipv4 prefix-list pl1
#  3 remark TEST_PL1_2_REMARK
#  4 permit 10.0.0.0/24
# !
# ipv4 prefix-list pl2
#  5 remark TEST_PL2_REMARK
# !
#
#
- name: Replace device configurations of listed prefix lists with provided configurations
  register: result
  cisco.iosxr.iosxr_prefix_lists: &id001
    config:
           - afi: ipv4
             prefix_lists:
               - name: pl1
                 entries:
                   - sequence: 3
                     action: permit
                     prefix: 10.0.0.0/24
           - afi: ipv6
             prefix_lists:
               - name: pl_1
                 entries:
                   - prefix: 2001:db8:1234::/48
                     action: permit
                     sequence: 1
               - name: pl_2
                 entries:
                   - sequence: 2
                     action: remark
                     description: TEST_PL1_2
    state: replaced
# After state:
#RP/0/0/CPU0:10#show running-config
#
# ipv6 prefix-list pl_1
#  1 deny 2001:db8:1234::/48
# !
# ipv6 prefix-list pl_2
#  2 remark TEST_PL1_2
# !
# ipv4 prefix-list pl1
#  3 permit 10.0.0.0/24
# !
# ipv4 prefix-list pl2
#  5 remark TEST_PL2_REMARK
#
# Module Execution:
#
# "after": [
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "prefix": "2001:db8:1234::/48",
#                             "sequence": 1
#                         }
#                     ],
#                     "name": "pl_1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL1_2",
#                             "sequence": 2
#                         }
#                     ],
#                     "name": "pl_2"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "prefix": "10.0.0.0/24",
#                             "sequence": 3
#                         }
#                     ],
#                     "name": "pl1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL2_REMARK",
#                             "sequence": 5
#                         }
#                     ],
#                     "name": "pl2"
#                 }
#             ]
#         }
#     ],
#     "before": [
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "prefix": "2001:db8:1234::/48",
#                             "sequence": 1
#                         }
#                     ],
#                     "name": "pl_1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL_2_REMARK",
#                             "sequence": 2
#                         }
#                     ],
#                     "name": "pl_2"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL1_2_REMARK",
#                             "sequence": 3
#                         },
#                         {
#                             "action": "permit",
#                             "prefix": "10.0.0.0/24",
#                             "sequence": 4
#                         }
#                     ],
#                     "name": "pl1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL2_REMARK",
#                             "sequence": 5
#                         }
#                     ],
#                     "name": "pl2"
#                 }
#             ]
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "no ipv4 prefix-list pl1 3 remark TEST_PL1_2_REMARK",
#         "no ipv4 prefix-list pl1 4 permit 10.0.0.0/24",
#         "ipv4 prefix-list pl1 3 permit 10.0.0.0/24",
#         "ipv6 prefix-list pl_2 2 remark TEST_PL1_2"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": [
#                 {
#                     "afi": "ipv4",
#                     "prefix_lists": [
#                         {
#                             "entries": [
#                                 {
#                                     "action": "permit",
#                                     "description": null,
#                                     "prefix": "10.0.0.0/24",
#                                     "sequence": 3
#                                 }
#                             ],
#                             "name": "pl1"
#                         }
#                     ]
#                 },
#                 {
#                     "afi": "ipv6",
#                     "prefix_lists": [
#                         {
#                             "entries": [
#                                 {
#                                     "action": "permit",
#                                     "description": null,
#                                     "prefix": "2001:db8:1234::/48",
#                                     "sequence": 1
#                                 }
#                             ],
#                             "name": "pl_1"
#                         },
#                         {
#                             "entries": [
#                                 {
#                                     "action": "remark",
#                                     "description": "TEST_PL1_2",
#                                     "prefix": null,
#                                     "sequence": 2
#                                 }
#                             ],
#                             "name": "pl_2"
#                         }
#                     ]
#                 }
#             ],
#             "running_config": null,
#             "state": "replaced"
#         }
#     }
# }
#------------------------------------------------------------------
# Using deleted:
# -------------
# Before state:
#RP/0/0/CPU0:10#show running-config
#
# ipv6 prefix-list pl_1
#  1 deny 2001:db8:1234::/48
# !
# ipv6 prefix-list pl_2
#  2 remark TEST_PL_2_REMARK
# !
# ipv4 prefix-list pl1
#  3 remark TEST_PL1_2_REMARK
#  4 permit 10.0.0.0/24
# !
# ipv4 prefix-list pl2
#  5 remark TEST_PL2_REMARK
# ipv4 prefix-list pl3
#  6 permit 35.0.0.0/8 eq 0

- name: Delete all prefix-lists from the device
  cisco.iosxr.iosxr_prefix_lists:
    state: deleted

# After state:
#RP/0/0/CPU0:10#show running-config
#
#
# Module Execution:
#
# "after": [],
#     "before": [
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "prefix": "2001:db8:1234::/48",
#                             "sequence": 1
#                         }
#                     ],
#                     "name": "pl_1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL1_2",
#                             "sequence": 2
#                         }
#                     ],
#                     "name": "pl_2"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "prefix": "10.0.0.0/24",
#                             "sequence": 3
#                         }
#                     ],
#                     "name": "pl1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL2_REMARK",
#                             "sequence": 5
#                         }
#                     ],
#                     "name": "pl2"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "prefix": " 35.0.0.0/8",
#                             "sequence": 6,
#                             "eq": 0
#                         }
#                     ],
#                     "name": "pl3"
#                 },
#             ]
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "no ipv6 prefix-list pl_1",
#         "no ipv6 prefix-list pl_2",
#         "no ipv4 prefix-list pl1",
#         "no ipv4 prefix-list pl2"
#         "no ipv4 prefix-list pl3"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": null,
#             "running_config": null,
#             "state": "deleted"
#         }
#     }
# }
#---------------------------------------------------------------------------------
#
# using gathered:
# --------------
# Before state:
#RP/0/0/CPU0:10#show running-config
#
# ipv6 prefix-list pl_1
#  1 deny 2001:db8:1234::/48
# !
# ipv6 prefix-list pl_2
#  2 remark TEST_PL_2_REMARK
# !
# ipv4 prefix-list pl1
#  3 remark TEST_PL1_2_REMARK
#  4 permit 10.0.0.0/24
# !
# ipv4 prefix-list pl2
#  5 remark TEST_PL2_REMARK
#!
# ipv4 prefix-list pl3
#  6 permit 35.0.0.0/8 eq 0
#!
- name: Gather ACL interfaces facts using gathered state
  cisco.iosxr.iosxr_prefix_lists:
     state: gathered
#
# Module Execution:
#
# "gathered": [
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "prefix": "2001:db8:1234::/48",
#                             "sequence": 1
#                         }
#                     ],
#                     "name": "pl_1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL_2_REMARK",
#                             "sequence": 2
#                         }
#                     ],
#                     "name": "pl_2"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL1_2_REMARK",
#                             "sequence": 3
#                         },
#                         {
#                             "action": "permit",
#                             "prefix": "10.0.0.0/24",
#                             "sequence": 4
#                         }
#                     ],
#                     "name": "pl1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL2_REMARK",
#                             "sequence": 5
#                         }
#                     ],
#                     "name": "pl2"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 6,
#                             "eq": 0
#                         }
#                     ],
#                     "name": "pl3"
#                 },
#             ]
#         }
#     ],
#     "changed": false,
#--------------------------------------------------------------------------
# Using parsed:
# --------------
#
# parsed.cfg
#------------------------------
# ipv6 prefix-list pl_1
#  1 deny 2001:db8:1234::/48
# !
# ipv6 prefix-list pl_2
#  2 remark TEST_PL_2_REMARK
# !
# ipv4 prefix-list pl1
#  3 remark TEST_PL1_2_REMARK
#  4 permit 10.0.0.0/24
# !
# ipv4 prefix-list pl2
#  5 remark TEST_PL2_REMARK
#!
# ipv4 prefix-list pl3
#  6 permit 35.0.0.0/8 eq 0
#
#
- name: Parse externally provided Prefix_lists config to agnostic model
  cisco.iosxr.iosxr_prefix_lists:
     running_config: "{{ lookup('file', './fixtures/parsed.cfg') }}"
     state: parsed
#
# Module execution:
#"parsed": [
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "prefix": "2001:db8:1234::/48",
#                             "sequence": 1
#                         }
#                     ],
#                     "name": "pl_1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL_2_REMARK",
#                             "sequence": 2
#                         }
#                     ],
#                     "name": "pl_2"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL1_2_REMARK",
#                             "sequence": 3
#                         },
#                         {
#                             "action": "permit",
#                             "prefix": "10.0.0.0/24",
#                             "sequence": 4
#                         }
#                     ],
#                     "name": "pl1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL2_REMARK",
#                             "sequence": 5
#                         }
#                     ],
#                     "name": "pl2"
#                 },
#                  {
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 6,
#                             "eq": 0
#                         }
#                     ],
#                     "name": "pl3"
#                 },
#             ]
#         }
#     ]
#
#----------------------------------------------------------------------------
# Using rendered:
# --------------
#
- name: Render platform specific commands from task input using rendered state
  register: result
  cisco.iosxr.iosxr_prefix_lists:
     config:
       - afi: ipv6
         prefix_lists:
           - name: pl_1
             entries:
               - prefix: 2001:db8:1234::/48
                 action: deny
                 sequence: 1
           - name: pl_2
             entries:
               - sequence: 2
                 action: remark
                 description: TEST_PL_2_REMARK
       - afi: ipv4
         prefix_lists:
           - name: pl1
             entries:
               - sequence: 3
                 action: remark
                 description: TEST_PL1_2_REMARK
               - sequence: 4
                 action: permit
                 prefix: 10.0.0.0/24
           - name: pl2
             entries:
               - sequence: 5
                 action: remark
                 description: TEST_PL2_REMARK
               - sequence: 6
                 action: permit
                 prefix: 35.0.0.0/8
                 eq: 0

     state: rendered
# After state:
# Module Execution:
# "rendered": [
#         "ipv6 prefix-list pl_1 1 deny 2001:db8:1234::/48",
#         "ipv6 prefix-list pl_2 2 remark TEST_PL_2_REMARK",
#         "ipv4 prefix-list pl1 3 remark TEST_PL1_2_REMARK",
#         "ipv4 prefix-list pl1 4 permit 10.0.0.0/24",
#         "ipv4 prefix-list pl2 5 remark TEST_PL2_REMARK",
#         "ipv4 prefix-list pl2 6 permit 35.0.0.0/8 eq 0"
#     ]
#
#---------------------------------------------------------------------------------
# Using overridden:
# --------------
# Before state:
#RP/0/0/CPU0:10#show running-config
#
# ipv6 prefix-list pl_1
#  1 deny 2001:db8:1234::/48
# !
# ipv6 prefix-list pl_2
#  2 remark TEST_PL_2_REMARK
# !
# ipv4 prefix-list pl1
#  3 remark TEST_PL1_2_REMARK
#  4 permit 10.0.0.0/24
# !
# ipv4 prefix-list pl2
#  5 remark TEST_PL2_REMARK
#
- name: Overridde all Prefix_lists configuration with provided configuration
  cisco.iosxr.iosxr_prefix_lists:
        config:
           - afi: ipv4
             prefix_lists:
               - name: pl3
                 entries:
                   - sequence: 3
                     action: remark
                     description: TEST_PL1_3_REMARK
                   - sequence: 4
                     action: permit
                     prefix: 10.0.0.0/24
                   - sequence: 6
                     action: permit
                     prefix: 35.0.0.0/8
                     eq: 0
        state: overridden

# After state:
#RP/0/0/CPU0:10#show running-config
#
#ipv4 prefix-list pl3
# 3 remark TEST_PL1_3_REMARK
# 4 permit 10.0.0.0/24
# 6 permit 35.0.0.0/8 eq 0
# !
#!
# # Module Execution:
# "after": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL1_3_REMARK",
#                             "sequence": 3
#                         },
#                         {
#                             "action": "permit",
#                             "prefix": "10.0.0.0/24",
#                             "sequence": 4
#                         },
#                         {
#                             "action": "permit",
#                             "prefix": "35.0.0.0/8",
#                             "sequence": 6,
#                             "eq": 0
#                         }
#                     ],
#                     "name": "pl3"
#                 }
#             ]
#         }
#     ],
#     "before": [
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "prefix": "2001:db8:1234::/48",
#                             "sequence": 1
#                         }
#                     ],
#                     "name": "pl_1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL_2_REMARK",
#                             "sequence": 2
#                         }
#                     ],
#                     "name": "pl_2"
#                 }
#             ]
#         },
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL1_2_REMARK",
#                             "sequence": 3
#                         },
#                         {
#                             "action": "permit",
#                             "prefix": "10.0.0.0/24",
#                             "sequence": 4
#                         }
#                     ],
#                     "name": "pl1"
#                 },
#                 {
#                     "entries": [
#                         {
#                             "action": "remark",
#                             "description": "TEST_PL2_REMARK",
#                             "sequence": 5
#                         }
#                     ],
#                     "name": "pl2"
#                 }
#             ]
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "no ipv6 prefix-list pl_1",
#         "no ipv6 prefix-list pl_2",
#         "no ipv4 prefix-list pl1",
#         "no ipv4 prefix-list pl2",
#         "ipv4 prefix-list pl3 3 remark TEST_PL1_3_REMARK",
#         "ipv4 prefix-list pl3 4 permit 10.0.0.0/24",
#         "ipv4 prefix-list pl3 6 permit 35.0.0.0/8 eq 0"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": [
#                 {
#                     "afi": "ipv4",
#                     "prefix_lists": [
#                         {
#                             "entries": [
#                                 {
#                                     "action": "remark",
#                                     "description": "TEST_PL1_3_REMARK",
#                                     "prefix": null,
#                                     "sequence": 3,
#                                     "ge": null,
#                                     "le": null,
#                                     "eq": null
#                                 },
#                                 {
#                                     "action": "permit",
#                                     "description": null,
#                                     "prefix": "10.0.0.0/24",
#                                     "sequence": 4,
#                                     "ge": null,
#                                     "le": null,
#                                     "eq": null
#                                 },
#                                 {
#                                     "action": "permit",
#                                     "description": null,
#                                     "prefix": "35.0.0.0/8",
#                                     "sequence": 6,
#                                     "ge": null,
#                                     "le": null,
#                                     "eq": 0
#                                 }
#                             ],
#                             "name": "pl3"
#                         }
#                     ]
#                 }
#             ],
#             "running_config": null,
#             "state": "overridden"
#         }
#     }
# }
#
```

## [Return Values](iosxr_prefix_lists_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["ipv6 prefix-list pl_1 1 deny 2001:db8:1234::/48", "ipv6 prefix-list pl_2 2 remark TEST_PL_2_REMARK", "ipv4 prefix-list pl1 3 remark TEST_PL1_2_REMARK", "ipv4 prefix-list pl1 4 permit 10.0.0.0/24", "ipv4 prefix-list pl2 5 remark TEST_PL2_REMARK"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["ipv6 prefix-list pl_1 1 deny 2001:db8:1234::/48", "ipv6 prefix-list pl_2 2 remark TEST_PL_2_REMARK", "ipv4 prefix-list pl1 3 remark TEST_PL1_2_REMARK", "ipv4 prefix-list pl1 4 permit 10.0.0.0/24", "ipv4 prefix-list pl2 5 remark TEST_PL2_REMARK"]` |

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
