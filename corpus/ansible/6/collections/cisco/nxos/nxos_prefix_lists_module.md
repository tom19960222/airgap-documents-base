---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_prefix_lists module – Prefix-Lists resource module."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_prefix_lists_module.html
fetched_at: 2026-07-27T17:02:16+00:00
---
# cisco.nxos.nxos_prefix_lists module – Prefix-Lists resource module.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_prefix_lists`.

New in cisco.nxos 2.4.0

- [Synopsis](nxos_prefix_lists_module.md#synopsis)
- [Parameters](nxos_prefix_lists_module.md#parameters)
- [Notes](nxos_prefix_lists_module.md#notes)
- [Examples](nxos_prefix_lists_module.md#examples)

## [Synopsis](nxos_prefix_lists_module.md#id1)

- This module manages prefix-lists configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_prefix_lists_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of prefix-list configuration. |
| **afi**  string | The Address Family Identifier (AFI) for the prefix-lists.  Choices:   - `"ipv4"` - `"ipv6"` |
| **prefix_lists**  list / elements=dictionary | List of prefix-list configurations. |
| **description**  string | Description of the prefix list |
| **entries**  list / elements=dictionary | List of configurations for the specified prefix-list |
| **action**  string | Prefix-List permit or deny.  Choices:   - `"permit"` - `"deny"` |
| **eq**  integer | Exact prefix length to be matched. |
| **ge**  integer | Minimum prefix length to be matched. |
| **le**  integer | Maximum prefix length to be matched. |
| **mask**  string | Explicit match mask. |
| **prefix**  string | IP or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format. |
| **sequence**  integer | Sequence Number. |
| **name**  string | Name of the prefix-list. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^ip(.\*** prefix-list’).  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Refer to examples for more details.  With state *replaced*, for the listed prefix-lists, sequences that are in running-config but not in the task are negated.  With state *overridden*, all prefix-lists that are in running-config but not in the task are negated.  Please refer to examples for more details.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_prefix_lists_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6.
> - Unsupported for Cisco MDS
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](nxos_prefix_lists_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# nxos-9k-rdo#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_prefix_lists:
    config:
      - afi: ipv4
        prefix_lists:
          - name: AllowPrefix
            description: allows engineering IPv4 networks
            entries:
              - sequence: 10
                action: permit
                prefix: 192.0.2.0/23
                eq: 24
              - sequence: 20
                action: permit
                prefix: 198.51.100.128/26
          - name: DenyPrefix
            description: denies lab IPv4 networks
            entries:
              - sequence: 20
                action: deny
                prefix: 203.0.113.0/24
                le: 25

      - afi: ipv6
        prefix_lists:
          - name: AllowIPv6Prefix
            description: allows engineering IPv6 networks
            entries:
              - sequence: 8
                action: permit
                prefix: "2001:db8:400::/38"
              - sequence: 20
                action: permit
                prefix: "2001:db8:8000::/35"
                le: 37

# Task output
# -------------
# before: []
#
# commands:
#   - "ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks"
#   - "ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38"
#   - "ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37"
#   - "ip prefix-list AllowPrefix description allows engineering IPv4 networks"
#   - "ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24"
#   - "ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26"
#   - "ip prefix-list DenyPrefix description denies lab IPv4 networks"
#   - "ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25"
#
# after:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 192.0.2.0/23
#             eq: 24
#           - sequence: 20
#             action: permit
#             prefix: 198.51.100.128/26
#         name: AllowPrefix
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix

# After state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24
# ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

# Using replaced

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24
# ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

- name: Replace prefix-lists configurations of listed prefix-lists with provided configurations
  cisco.nxos.nxos_prefix_lists:
    config:
      - afi: ipv4
        prefix_lists:
          - name: AllowPrefix
            description: allows engineering IPv4 networks
            entries:
              - sequence: 10
                action: permit
                prefix: 203.0.113.64/27

              - sequence: 30
                action: permit
                prefix: 203.0.113.96/27
          - name: AllowPrefix2Stub
            description: allow other engineering IPv4 network
    state: replaced

# Task output
# -------------
# before:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 192.0.2.0/23
#             eq: 24
#           - sequence: 20
#             action: permit
#             prefix: 198.51.100.128/26
#         name: AllowPrefix
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
#
# commands:
#   - "no ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24"
#   - "ip prefix-list AllowPrefix seq 10 permit 203.0.113.64/27"
#   - "ip prefix-list AllowPrefix seq 30 permit 203.0.113.96/27"
#   - "no ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26"
#   - "ip prefix-list AllowPrefix2Stub description allow other engineering IPv4 network"
#
# after:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 203.0.113.64/27
#           - sequence: 30
#             action: permit
#             prefix: 203.0.113.96/27
#          name: AllowPrefix
#       - description: allow other engineering IPv4 network
#         name: AllowPrefix2Stub
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
#
# After state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 203.0.113.64/27
# ip prefix-list AllowPrefix seq 30 permit 203.0.113.96/27
# ip prefix-list AllowPrefix2Stub description allow other engineering IPv4 network
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

# Using overridden

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24
# ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

- name: Override all prefix-lists configuration with provided configuration
  cisco.nxos.nxos_prefix_lists: &id003
    config:
      - afi: ipv4
        prefix_lists:
          - name: AllowPrefix
            description: allows engineering IPv4 networks
            entries:
              - sequence: 10
                action: permit
                prefix: 203.0.113.64/27

              - sequence: 30
                action: permit
                prefix: 203.0.113.96/27
          - name: AllowPrefix2Stub
            description: allow other engineering IPv4 network
    state: overridden

# Task output
# -------------
# before:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 192.0.2.0/23
#             eq: 24
#           - sequence: 20
#             action: permit
#             prefix: 198.51.100.128/26
#         name: AllowPrefix
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
#
# commands:
#   - "no ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24"
#   - "ip prefix-list AllowPrefix seq 10 permit 203.0.113.64/27"
#   - "ip prefix-list AllowPrefix seq 30 permit 203.0.113.96/27"
#   - "no ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26"
#   - "ip prefix-list AllowPrefix2Stub description allow other engineering IPv4 network"
#   - "no ip prefix-list DenyPrefix"
#   - "no ipv6 prefix-list AllowIPv6Prefix"
#
# after:
#   - afi: ipv4
#     prefix_lists:
#       - name: AllowPrefix
#         description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 203.0.113.64/27
#
#           - sequence: 30
#             action: permit
#             prefix: 203.0.113.96/27
#       - name: AllowPrefix2Stub
#         description: allow other engineering IPv4 network
#
# After state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 203.0.113.64/27
# ip prefix-list AllowPrefix seq 30 permit 203.0.113.96/27
# ip prefix-list AllowPrefix2Stub description allow other engineering IPv4 network

# Using deleted to delete a all prefix lists for an AFI

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24
# ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

- name: Delete all prefix-lists for an AFI
  cisco.nxos.nxos_prefix_lists:
    config:
      - afi: ipv4
    state: deleted
  register: result

# Task output
# -------------
# before:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 192.0.2.0/23
#             eq: 24
#           - sequence: 20
#             action: permit
#             prefix: 198.51.100.128/26
#         name: AllowPrefix
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
#
# commands:
#   - "no ip prefix-list AllowPrefix"
#   - "no ip prefix-list DenyPrefix"
#
# after:
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
#
# After state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

# Using deleted to delete a single prefix-list

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24
# ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

- name: Delete a single prefix-list
  cisco.nxos.nxos_prefix_lists:
    config:
      - afi: ipv4
        prefix_lists:
          - name: AllowPrefix
    state: deleted

# Task output
# -------------
# before:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 192.0.2.0/23
#             eq: 24
#           - sequence: 20
#             action: permit
#             prefix: 198.51.100.128/26
#         name: AllowPrefix
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
#
# commands:
#   - "no ip prefix-list AllowPrefix"
#
# after:
#   - afi: ipv4
#     prefix_lists:
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
#
# After state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

# Using deleted to delete all prefix-lists from the device

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24
# ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

- name: Delete all prefix-lists
  cisco.nxos.nxos_prefix_lists:
    state: deleted

# Task output
# -------------
# before:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 192.0.2.0/23
#             eq: 24
#           - sequence: 20
#             action: permit
#             prefix: 198.51.100.128/26
#         name: AllowPrefix
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
#
# commands:
#   - "no ip prefix-list AllowPrefix"
#   - "no ip prefix-list DenyPrefix"
#   - "no ipv6 prefix-list AllowIPv6Prefix"
#
# after: []
#
# After state:
# ------------
# nxos-9k-rdo# show running-config | section 'ip(.*) prefix-list'
# nxos-9k-rdo#

# Using rendered

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_prefix_lists: &id001
    config:
      - afi: ipv4
        prefix_lists:
          - name: AllowPrefix
            description: allows engineering IPv4 networks
            entries:
              - sequence: 10
                action: permit
                prefix: 192.0.2.0/23
                eq: 24
              - sequence: 20
                action: permit
                prefix: 198.51.100.128/26
          - name: DenyPrefix
            description: denies lab IPv4 networks
            entries:
              - sequence: 20
                action: deny
                prefix: 203.0.113.0/24
                le: 25

      - afi: ipv6
        prefix_lists:
          - name: AllowIPv6Prefix
            description: allows engineering IPv6 networks
            entries:
              - sequence: 8
                action: permit
                prefix: "2001:db8:400::/38"
              - sequence: 20
                action: permit
                prefix: "2001:db8:8000::/35"
                le: 37
    state: rendered

# Task Output (redacted)
# -----------------------
# rendered:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 192.0.2.0/23
#             eq: 24
#           - sequence: 20
#             action: permit
#             prefix: 198.51.100.128/26
#         name: AllowPrefix
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix

# Using parsed

# parsed.cfg
# ------------
# ip prefix-list AllowPrefix description allows engineering IPv4 networks
# ip prefix-list AllowPrefix seq 10 permit 192.0.2.0/23 eq 24
# ip prefix-list AllowPrefix seq 20 permit 198.51.100.128/26
# ip prefix-list DenyPrefix description denies lab IPv4 networks
# ip prefix-list DenyPrefix seq 20 deny 203.0.113.0/24 le 25
# ipv6 prefix-list AllowIPv6Prefix description allows engineering IPv6 networks
# ipv6 prefix-list AllowIPv6Prefix seq 8 permit 2001:db8:400::/38
# ipv6 prefix-list AllowIPv6Prefix seq 20 permit 2001:db8:8000::/35 le 37

- name: Parse externally provided prefix-lists configuration
  register: result
  cisco.nxos.nxos_prefix_lists:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#   - afi: ipv4
#     prefix_lists:
#       - description: allows engineering IPv4 networks
#         entries:
#           - sequence: 10
#             action: permit
#             prefix: 192.0.2.0/23
#             eq: 24
#           - sequence: 20
#             action: permit
#             prefix: 198.51.100.128/26
#         name: AllowPrefix
#       - description: denies lab IPv4 networks
#         entries:
#           - sequence: 20
#             action: deny
#             prefix: 203.0.113.0/24
#             le: 25
#         name: DenyPrefix
#
#   - afi: ipv6
#     prefix_lists:
#       - description: allows engineering IPv6 networks
#         entries:
#           - sequence: 8
#             action: permit
#             prefix: "2001:db8:400::/38"
#           - sequence: 20
#             action: permit
#             prefix: "2001:db8:8000::/35"
#             le: 37
#         name: AllowIPv6Prefix
```

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
