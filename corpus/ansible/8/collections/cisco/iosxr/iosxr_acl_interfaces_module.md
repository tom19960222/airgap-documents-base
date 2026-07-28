---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_acl_interfaces module – Resource module to configure ACL interfaces."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_acl_interfaces_module.html
fetched_at: 2026-07-28T01:26:33+00:00
---
# cisco.iosxr.iosxr_acl_interfaces module – Resource module to configure ACL interfaces.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_acl_interfaces`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_acl_interfaces_module.md#synopsis)
- [Parameters](iosxr_acl_interfaces_module.md#parameters)
- [Examples](iosxr_acl_interfaces_module.md#examples)
- [Return Values](iosxr_acl_interfaces_module.md#return-values)

## [Synopsis](iosxr_acl_interfaces_module.md#id1)

- This module manages adding and removing Access Control Lists (ACLs) from interfaces on devices running IOS-XR software.

Aliases: acl_interfaces

## [Parameters](iosxr_acl_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of ACL options for interfaces. |
| **access_groups**  list / elements=dictionary | Specifies ACLs attached to the interfaces. |
| **acls**  list / elements=dictionary | Specifies the ACLs for the provided AFI. |
| **direction**  string / required | Specifies the direction of packets that the ACL will be applied on.  **Choices:**   - `"in"` - `"out"` |
| **name**  string / required | Specifies the name of the IPv4/IPv6 ACL for the interface. |
| **afi**  string / required | Specifies the AFI for the ACL(s) to be configured on this interface.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **name**  string / required | Name/Identifier for the interface |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Examples](iosxr_acl_interfaces_module.md#id3)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:22:32.911 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
# !

- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_1
          direction: in
        - name: acl_2
          direction: out
      - afi: ipv6
        acls:
        - name: acl6_1
          direction: in
        - name: acl6_2
          direction: out

    - name: GigabitEthernet0/0/0/1
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_1
          direction: out
    state: merged

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:27:49.378 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !

# Using merged to update interface ACL configuration

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:27:49.378 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

- name: Update acl_interfaces configuration using merged
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_2
          direction: out
        - name: acl_1
          direction: in
    state: merged

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:27:49.378 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
# !
#

# Using replaced

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !

- name: Replace device configurations of listed interface with provided configurations
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/0
      access_groups:
      - afi: ipv6
        acls:
        - name: acl6_3
          direction: in
    state: replaced

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv6 access-group acl6_3 ingress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

# Using overridden

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

- name: Overridde all interface ACL configuration with provided configuration
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_2
          direction: in
      - afi: ipv6
        acls:
        - name: acl6_3
          direction: out
    state: overridden

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_2 ingress
#  ipv6 access-group acl6_3 egress
# !
#

# Using 'deleted' to delete all ACL attributes of a single interface

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

- name: Delete all ACL attributes of GigabitEthernet0/0/0/1
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/1
    state: deleted

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
#

# Using 'deleted' to remove all ACLs attached to all the interfaces in the device

# Before state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !
#

- name: Delete all ACL interfaces configuration from the device
  cisco.iosxr.iosxr_acl_interfaces:
    state: deleted

# After state:
# -------------
#
# RP/0/RP0/CPU0:ios#sh running-config interface
# Wed Jan 15 12:34:56.689 UTC
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
#

# Using parsed

# parsed.cfg
# ------------
#
# interface MgmtEth0/RP0/CPU0/0
#  ipv4 address dhcp
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
#  ipv4 access-group acl_1 ingress
#  ipv4 access-group acl_2 egress
#  ipv6 access-group acl6_1 ingress
#  ipv6 access-group acl6_2 egress
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
#  ipv4 access-group acl_1 egress
# !

# - name: Convert ACL interfaces config to argspec without connecting to the appliance
#   cisco.iosxr.iosxr_acl_interfaces:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed

# Task Output (redacted)
# -----------------------

# "parsed": [
#        {
#            "name": "MgmtEth0/RP0/CPU0/0"
#        },
#        {
#            "access_groups": [
#                {
#                    "acls": [
#                        {
#                            "direction": "in",
#                            "name": "acl_1"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "acl_2"
#                        }
#                    ],
#                    "afi": "ipv4"
#                },
#                {
#                    "acls": [
#                        {
#                            "direction": "in",
#                            "name": "acl6_1"
#                        },
#                        {
#                            "direction": "out",
#                            "name": "acl6_2"
#                        }
#                    ],
#                    "afi": "ipv6"
#                }
#            ],
#            "name": "GigabitEthernet0/0/0/0"
#        },
#        {
#            "access_groups": [
#                {
#                    "acls": [
#                        {
#                            "direction": "out",
#                            "name": "acl_1"
#                        }
#                    ],
#                    "afi": "ipv4"
#                }
#            ],
#            "name": "GigabitEthernet0/0/0/1"
#        }
#    ]
# }

# Using gathered

- name: Gather ACL interfaces facts using gathered state
  cisco.iosxr.iosxr_acl_interfaces:
    state: gathered

# Task Output (redacted)
# -----------------------
#
# "gathered": [
#   {
#      "name": "MgmtEth0/RP0/CPU0/0"
#   },
#   {
#      "access_groups": [
#          {
#              "acls": [
#                  {
#                      "direction": "in",
#                      "name": "acl_1"
#                  },
#                  {
#                      "direction": "out",
#                      "name": "acl_2"
#                  }
#              ],
#              "afi": "ipv4"
#          }
#      "name": "GigabitEthernet0/0/0/0"
#  },
#  {
#      "access_groups": [
#          {
#              "acls": [
#                  {
#                      "direction": "in",
#                      "name": "acl6_1"
#                  }
#              ],
#              "afi": "ipv6"
#          }
#       "name": "GigabitEthernet0/0/0/1"
#   }
# ]

# Using rendered

- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_acl_interfaces:
    config:
    - name: GigabitEthernet0/0/0/0
      access_groups:
      - afi: ipv4
        acls:
        - name: acl_1
          direction: in
        - name: acl_2
          direction: out
    state: rendered

# Task Output (redacted)
# -----------------------

# "rendered": [
#     "interface GigabitEthernet0/0/0/0",
#     "ipv4 access-group acl_1 ingress",
#     "ipv4 access-group acl_2 egress"
# ]
```

## [Return Values](iosxr_acl_interfaces_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["interface GigabitEthernet0/0/0/1", "ipv4 access-group acl_1 ingress", "ipv4 access-group acl_2 egress", "ipv6 access-group acl6_1 ingress", "interface GigabitEthernet0/0/0/2", "no ipv4 access-group acl_3 ingress", "ipv4 access-group acl_4 egress"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
