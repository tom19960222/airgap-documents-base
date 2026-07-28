---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_prefix_lists module – Prefix-Lists resource module for VyOS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_prefix_lists_module.html
fetched_at: 2026-07-28T02:59:24+00:00
---
# vyos.vyos.vyos_prefix_lists module – Prefix-Lists resource module for VyOS

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_prefix_lists`.

New in vyos.vyos 2.4.0

- [Synopsis](vyos_prefix_lists_module.md#synopsis)
- [Parameters](vyos_prefix_lists_module.md#parameters)
- [Notes](vyos_prefix_lists_module.md#notes)
- [Examples](vyos_prefix_lists_module.md#examples)
- [Return Values](vyos_prefix_lists_module.md#return-values)

## [Synopsis](vyos_prefix_lists_module.md#id1)

- This module manages prefix-lists configuration on devices running VyOS

Aliases: prefix_lists

## [Parameters](vyos_prefix_lists_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of prefix-list options |
| **afi**  string / required | The Address Family Indicator (AFI) for the prefix-lists  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **prefix_lists**  list / elements=dictionary | A list of prefix-list configurations |
| **description**  string | A brief text description for the prefix-list |
| **entries**  list / elements=dictionary | Rule configurations for the prefix-list |
| **action**  string | The action to be taken for packets matching a prefix list rule  **Choices:**   - `"permit"` - `"deny"` |
| **description**  string | A brief text description for the prefix list rule |
| **ge**  integer | Minimum prefix length to be matched |
| **le**  integer | Maximum prefix list length to be matched |
| **prefix**  string | IPv4 or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format |
| **sequence**  integer / required | A numeric identifier for the rule |
| **name**  string / required | The name of a defined prefix-list |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep prefix-list**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](vyos_prefix_lists_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium)
> - This module works with connection `network_cli`

## [Examples](vyos_prefix_lists_module.md#id4)

```yaml+jinja
# # -------------------
# # 1. Using merged
# # -------------------

# # Before state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   vyos@vyos:~$

# # Task
# # -------------
#     - name: Merge the provided configuration with the existing running configuration
#         vyos.vyos.vyos_prefix_lists:
#             config:
#             - afi: "ipv4"
#                 prefix_lists:
#                 - name: "AnsibleIPv4PrefixList"
#                     description: "PL configured by ansible"
#                     entries:
#                     - sequence: 2
#                         description: "Rule 2 given by ansible"
#                         action: "permit"
#                         prefix: "92.168.10.0/26"
#                         le: 32

#                     - sequence: 3
#                         description: "Rule 3"
#                         action: "deny"
#                         prefix: "72.168.2.0/24"
#                         ge: 26

#             - afi: "ipv6"
#                 prefix_lists:
#                 - name: "AllowIPv6Prefix"
#                     description: "Configured by ansible for allowing IPv6 networks"
#                     entries:
#                     - sequence: 5
#                         description: "Permit rule"
#                         action: "permit"
#                         prefix: "2001:db8:8000::/35"
#                         le: 37

#                 - name: DenyIPv6Prefix
#                     description: "Configured by ansible for disallowing IPv6 networks"
#                     entries:
#                     - sequence: 8
#                         action: deny
#                         prefix: "2001:db8:2000::/35"
#                         le: 37
#             state: merged

# # Task output:
# # -------------
#     "after": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "before": [],
#     "changed": true,
#     "commands": [
#         "set policy prefix-list AnsibleIPv4PrefixList",
#         "set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'",
#         "set policy prefix-list6 AllowIPv6Prefix",
#         "set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'",
#         "set policy prefix-list6 DenyIPv6Prefix",
#         "set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'",
#         "set policy prefix-list6 DenyIPv6Prefix rule 8",
#         "set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'",
#         "set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'",
#         "set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'"
#     ]

# After state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
#   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
#   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
#   vyos@vyos:~$

# # -------------------
# # 2. Using replaced
# # -------------------

# # Before state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
#   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
#   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
#   vyos@vyos:~$

# # Task:
# # -------------
#     - name: Replace prefix-lists configurations of listed prefix-lists with provided configurations
#       vyos.vyos.vyos_prefix_lists:
#         config:
#           - afi: "ipv4"
#             prefix_lists:
#               - name: "AnsibleIPv4PrefixList"
#                 description: "Configuration replaced by ansible"
#                 entries:
#                   - sequence: 3
#                     description: "Rule 3 replaced by ansible"
#                     action: "permit"
#                     prefix: "82.168.2.0/24"
#                     ge: 26
#         state: replaced

# # Task output:
# # -------------
#     "after": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "Configuration replaced by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 3 replaced by ansible",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "82.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "before": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "set policy prefix-list AnsibleIPv4PrefixList description 'Configuration replaced by ansible'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'permit'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3 replaced by ansible'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '82.168.2.0/24'",
#         "delete policy prefix-list AnsibleIPv4PrefixList rule 2"
#     ]

# # After state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'Configuration replaced by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'permit'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3 replaced by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '82.168.2.0/24'
#   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
#   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
#   vyos@vyos:~$

# # -------------------
# # 3. Using overridden
# # -------------------

# # Before state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
#   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
#   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
#   vyos@vyos:~$

# # Task:
# # -------------
#     - name: Override all prefix-lists configuration with provided configuration
#       vyos.vyos.vyos_prefix_lists:
#         config:
#           - afi: "ipv4"
#             prefix_lists:
#               - name: "AnsibleIPv4PrefixList"
#                 description: Rule 2 overridden by ansible
#                 entries:
#                   - sequence: 2
#                     action: "deny"
#                     ge: 26
#                     prefix: "82.168.2.0/24"

#               - name: "OverriddenPrefixList"
#                 description: Configuration overridden by ansible
#                 entries:
#                   - sequence: 10
#                     action: permit
#                     prefix: "203.0.113.96/27"
#                     le: 32
#         state: overridden

# # Task output:
# # -------------
#     "after": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "Rule 2 overridden by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "ge": 26,
#                             "sequence": 2,
#                             "prefix": "82.168.2.0/24"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configuration overridden by ansible",
#                     "name": "OverriddenPrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "sequence": 10,
#                             "le": 32,
#                             "prefix": "203.0.113.96/27"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "before": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete policy prefix-list6 AllowIPv6Prefix",
#         "delete policy prefix-list6 DenyIPv6Prefix",
#         "set policy prefix-list AnsibleIPv4PrefixList description 'Rule 2 overridden by ansible'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'deny'",
#         "delete policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 ge '26'",
#         "delete policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '82.168.2.0/24'",
#         "delete policy prefix-list AnsibleIPv4PrefixList rule 3",
#         "set policy prefix-list OverriddenPrefixList",
#         "set policy prefix-list OverriddenPrefixList description 'Configuration overridden by ansible'",
#         "set policy prefix-list OverriddenPrefixList rule 10",
#         "set policy prefix-list OverriddenPrefixList rule 10 action 'permit'",
#         "set policy prefix-list OverriddenPrefixList rule 10 le '32'",
#         "set policy prefix-list OverriddenPrefixList rule 10 prefix '203.0.113.96/27'"
#     ]

# # After state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'Rule 2 overridden by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'deny'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '82.168.2.0/24'
#   set policy prefix-list OverriddenPrefixList description 'Configuration overridden by ansible'
#   set policy prefix-list OverriddenPrefixList rule 10 action 'permit'
#   set policy prefix-list OverriddenPrefixList rule 10 le '32'
#   set policy prefix-list OverriddenPrefixList rule 10 prefix '203.0.113.96/27'
#   vyos@vyos:~$

# # -------------------
# # 4(i). Using deleted (to delete all prefix lists from the device)
# # -------------------

# # Before state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
#   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
#   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
#   vyos@vyos:~$

# # Task:
# # -------------
#     - name: Delete all prefix-lists
#       vyos.vyos.vyos_prefix_lists:
#         config:
#         state: deleted

# # Task output:
# # -------------
#     "after": [],
#     "before": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete policy prefix-list AnsibleIPv4PrefixList",
#         "delete policy prefix-list6 AllowIPv6Prefix",
#         "delete policy prefix-list6 DenyIPv6Prefix"
#     ]

# # After state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   vyos@vyos:~$

# # -------------------
# # 4(ii). Using deleted (to delete all prefix lists for an AFI)
# # -------------------

# # Before state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
#   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
#   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
#   vyos@vyos:~$

# # Task:
# # -------------
#     - name: Delete all prefix-lists for IPv6 AFI
#       vyos.vyos.vyos_prefix_lists:
#         config:
#           - afi: "ipv6"
#         state: deleted

# # Task output:
# # -------------
#     "after": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "before": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete policy prefix-list6 AllowIPv6Prefix",
#         "delete policy prefix-list6 DenyIPv6Prefix"
#     ]

# # After state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
#   vyos@vyos:~$

# # -------------------
# # 4(iii). Using deleted (to delete single prefix list by name in different AFIs)
# # -------------------

# # Before state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
#   set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
#   set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
#   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
#   set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
#   set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'
#   vyos@vyos:~$

# # Task:
# # -------------
#     - name: Delete a single prefix-list from different AFIs
#       vyos.vyos.vyos_prefix_lists:
#         config:
#           - afi: "ipv4"
#             prefix_lists:
#               - name: "AnsibleIPv4PrefixList"
#           - afi: "ipv6"
#             prefix_lists:
#               - name: "DenyIPv6Prefix"
#         state: deleted

# # Task output:
# # -------------
#     "after": [
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "before": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete policy prefix-list AnsibleIPv4PrefixList",
#         "delete policy prefix-list6 DenyIPv6Prefix"
#     ]

# # After state:
# # -------------
#   vyos@vyos:~$ show configuration commands | grep prefix-list
#   set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
#   set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
#   vyos@vyos:~$

# # -------------------
# # 5. Using gathered
# # -------------------

# # Task:
# # -------------
#     - name: Gather prefix-lists configurations
#       vyos.vyos.vyos_prefix_lists:
#         config:
#         state: gathered

# # Task output:
# # -------------
#     "gathered": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ]

# # -------------------
# # 6. Using rendered
# # -------------------

# # Task:
# # -------------
#     - name: Render commands externally for the described prefix-list configurations
#       vyos.vyos.vyos_prefix_lists:
#         config:
#           - afi: "ipv4"
#             prefix_lists:
#               - name: "AnsibleIPv4PrefixList"
#                 description: "PL configured by ansible"
#                 entries:
#                   - sequence: 2
#                     description: "Rule 2 given by ansible"
#                     action: "permit"
#                     prefix: "92.168.10.0/26"
#                     le: 32

#                   - sequence: 3
#                     description: "Rule 3"
#                     action: "deny"
#                     prefix: "72.168.2.0/24"
#                     ge: 26

#           - afi: "ipv6"
#             prefix_lists:
#               - name: "AllowIPv6Prefix"
#                 description: "Configured by ansible for allowing IPv6 networks"
#                 entries:
#                   - sequence: 5
#                     description: "Permit rule"
#                     action: "permit"
#                     prefix: "2001:db8:8000::/35"
#                     le: 37

#               - name: DenyIPv6Prefix
#                 description: "Configured by ansible for disallowing IPv6 networks"
#                 entries:
#                   - sequence: 8
#                     action: deny
#                     prefix: "2001:db8:2000::/35"
#                     le: 37
#         state: rendered

# # Task output:
# # -------------
#     "rendered": [
#         "set policy prefix-list AnsibleIPv4PrefixList",
#         "set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'",
#         "set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'",
#         "set policy prefix-list6 AllowIPv6Prefix",
#         "set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'",
#         "set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'",
#         "set policy prefix-list6 DenyIPv6Prefix",
#         "set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'",
#         "set policy prefix-list6 DenyIPv6Prefix rule 8",
#         "set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'",
#         "set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'",
#         "set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'"
#     ]

# # -------------------
# # 7. Using parsed
# # -------------------

# # sample_config.cfg:
# # -------------
# set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'
# set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'
# set policy prefix-list AnsibleIPv4PrefixList rule 2 description 'Rule 2 given by ansible'
# set policy prefix-list AnsibleIPv4PrefixList rule 2 le '32'
# set policy prefix-list AnsibleIPv4PrefixList rule 2 prefix '92.168.10.0/26'
# set policy prefix-list AnsibleIPv4PrefixList rule 3 action 'deny'
# set policy prefix-list AnsibleIPv4PrefixList rule 3 description 'Rule 3'
# set policy prefix-list AnsibleIPv4PrefixList rule 3 ge '26'
# set policy prefix-list AnsibleIPv4PrefixList rule 3 prefix '72.168.2.0/24'
# set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'
# set policy prefix-list6 AllowIPv6Prefix rule 5 action 'permit'
# set policy prefix-list6 AllowIPv6Prefix rule 5 description 'Permit rule'
# set policy prefix-list6 AllowIPv6Prefix rule 5 le '37'
# set policy prefix-list6 AllowIPv6Prefix rule 5 prefix '2001:db8:8000::/35'
# set policy prefix-list6 DenyIPv6Prefix description 'Configured by ansible for disallowing IPv6 networks'
# set policy prefix-list6 DenyIPv6Prefix rule 8 action 'deny'
# set policy prefix-list6 DenyIPv6Prefix rule 8 le '37'
# set policy prefix-list6 DenyIPv6Prefix rule 8 prefix '2001:db8:2000::/35'

# # Task:
# # -------------
#     - name: Parse externally provided prefix-lists configuration
#       vyos.vyos.vyos_prefix_lists:
#         running_config: "{{ lookup('file', './sample_config.cfg') }}"
#         state: parsed

# # Task output:
# # -------------
#     "parsed": [
#         {
#             "afi": "ipv4",
#             "prefix_lists": [
#                 {
#                     "description": "PL configured by ansible",
#                     "name": "AnsibleIPv4PrefixList",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Rule 2 given by ansible",
#                             "sequence": 2,
#                             "le": 32,
#                             "prefix": "92.168.10.0/26"
#                         },
#                         {
#                             "action": "deny",
#                             "description": "Rule 3",
#                             "ge": 26,
#                             "sequence": 3,
#                             "prefix": "72.168.2.0/24"
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             "afi": "ipv6",
#             "prefix_lists": [
#                 {
#                     "description": "Configured by ansible for allowing IPv6 networks",
#                     "name": "AllowIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "permit",
#                             "description": "Permit rule",
#                             "sequence": 5,
#                             "le": 37,
#                             "prefix": "2001:db8:8000::/35"
#                         }
#                     ]
#                 },
#                 {
#                     "description": "Configured by ansible for disallowing IPv6 networks",
#                     "name": "DenyIPv6Prefix",
#                     "entries": [
#                         {
#                             "action": "deny",
#                             "sequence": 8,
#                             "le": 37,
#                             "prefix": "2001:db8:2000::/35"
#                         }
#                     ]
#                 }
#             ]
#         }
#     ]
```

## [Return Values](vyos_prefix_lists_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration after the module invocation.  **Returned:** when changed  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **before**  list / elements=string | The configuration prior to the module invocation.  **Returned:** when state is *merged*, *replaced*, *overridden* or *deleted*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device for the required configurations to take place.  **Returned:** when state is *merged*, *replaced*, *overridden* or *deleted*  **Sample:** `["set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'", "set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'", "set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when state is *parsed*  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when state is *rendered*  **Sample:** `["set policy prefix-list AnsibleIPv4PrefixList description 'PL configured by ansible'", "set policy prefix-list AnsibleIPv4PrefixList rule 2 action 'permit'", "set policy prefix-list6 AllowIPv6Prefix description 'Configured by ansible for allowing IPv6 networks'"]` |

### Authors

- Priyam Sahoo (@priyamsahoo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
