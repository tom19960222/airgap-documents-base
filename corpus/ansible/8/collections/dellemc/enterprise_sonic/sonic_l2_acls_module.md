---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_l2_acls module – Manage Layer 2 access control lists (ACL) configurations on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_l2_acls_module.html
fetched_at: 2026-07-28T02:03:38+00:00
---
# dellemc.enterprise_sonic.sonic_l2_acls module – Manage Layer 2 access control lists (ACL) configurations on SONiC

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_l2_acls`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_l2_acls_module.md#synopsis)
- [Parameters](sonic_l2_acls_module.md#parameters)
- [Examples](sonic_l2_acls_module.md#examples)
- [Return Values](sonic_l2_acls_module.md#return-values)

## [Synopsis](sonic_l2_acls_module.md#id1)

- This module provides configuration management of Layer 2 access control lists (ACL) in devices running SONiC.

## [Parameters](sonic_l2_acls_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies Layer 2 ACL configurations. |
| **name**  string / required | Specifies the ACL name. |
| **remark**  string | Specifies remark for the ACL. |
| **rules**  list / elements=dictionary | List of rules with the ACL.  *sequence_num*, *action*, *source* & *destination* are required for adding a new rule.  If *state=deleted*, options other than *sequence_num* are not considered.  *ethertype* and *vlan_tag_format* are mutually exclusive. |
| **action**  string | Specifies the action taken on the matched Ethernet frame.  **Choices:**   - `"deny"` - `"discard"` - `"do-not-nat"` - `"permit"` - `"transit"` |
| **dei**  integer | Match Ethernet frame with the given Drop Eligible Indicator (DEI) value.  **Choices:**   - `0` - `1` |
| **destination**  dictionary | Specifies the destination of the Ethernet frame.  *address* and *address_mask* are required together.  *any*, *host* and *address* are mutually exclusive. |
| **address**  string | Destination MAC address. |
| **address_mask**  string | Destination MAC address mask. |
| **any**  boolean | Match any destination MAC address.  **Choices:**   - `false` - `true` |
| **host**  string | MAC address of a single destination host. |
| **ethertype**  dictionary | Specifies the EtherType of the Ethernet frame.  Only one suboption can be specified for ethertype in a rule. |
| **arp**  boolean | Match Ethernet frame with ARP EtherType (0x806).  **Choices:**   - `false` - `true` |
| **ipv4**  boolean | Match Ethernet frame with IPv4 EtherType (0x800).  **Choices:**   - `false` - `true` |
| **ipv6**  boolean | Match Ethernet frame with IPv6 EtherType (0x86DD).  **Choices:**   - `false` - `true` |
| **value**  string | Specifies the EtherType value to match as a hexadecimal string.  The range is from 0x600 to 0xffff. |
| **pcp**  dictionary | Match Ethernet frames using Priority Code Point (PCP) value.  *mask* is valid only when *value* is specified.  *value* and *traffic_type* are mutually exclusive. |
| **mask**  integer | Match Ethernet frame with given PCP value and mask.  The range is from 0 to 7. |
| **traffic_type**  string | Match Ethernet frame with PCP value for the given traffic type.  `be` - Match Ethernet frame with Best effort PCP (0).  `bk` - Match Ethernet frame with Background PCP (1).  `ee` - Match Ethernet frame with Excellent effort PCP (2).  `ca` - Match Ethernet frame with Critical applications PCP (3).  `vi` - Match Ethernet frame with Video, < 100 ms latency and jitter PCP (4).  `vo` - Match Ethernet frame with Voice, < 10 ms latency and jitter PCP (5).  `ic` - Match Ethernet frame with Internetwork control PCP (6).  `nc` - Match Ethernet frame with Network control PCP (7).  **Choices:**   - `"be"` - `"bk"` - `"ee"` - `"ca"` - `"vi"` - `"vo"` - `"ic"` - `"nc"` |
| **value**  integer | Match Ethernet frame with the given PCP value.  The range is from 0 to 7 |
| **remark**  string | Specifies remark for the ACL rule. |
| **sequence_num**  integer / required | Specifies the sequence number of the rule.  The range is from 1 to 65535. |
| **source**  dictionary | Specifies the source of the Ethernet frame.  *address* and *address_mask* are required together.  *any*, *host* and *address* are mutually exclusive. |
| **address**  string | Source MAC address. |
| **address_mask**  string | Source MAC address mask. |
| **any**  boolean | Match any source MAC address.  **Choices:**   - `false` - `true` |
| **host**  string | MAC address of a single source host. |
| **vlan_id**  integer | Match Ethernet frame with the given VLAN ID. |
| **vlan_tag_format**  dictionary | Match Ethernet frame with the given VLAN tag format. |
| **multi_tagged**  boolean | Match three of more VLAN tagged Ethernet frame.  **Choices:**   - `false` - `true` |
| **state**  string | The state of the configuration after module completion.  `merged` - Merges provided L2 ACL configuration with on-device configuration.  `replaced` - Replaces on-device configuration of the specified L2 ACLs with provided configuration.  `overridden` - Overrides all on-device L2 ACL configurations with the provided configuration.  `deleted` - Deletes on-device L2 ACL configuration.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Examples](sonic_l2_acls_module.md#id3)

```yaml+jinja
# Using merged
#
# Before State:
# -------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test
#  seq 1 permit host 22:22:22:22:22:22 any vlan 20
# sonic#

  - name: Merge provided Layer 2 ACL configurations
    dellemc.enterprise_sonic.sonic_l2_acls:
      config:
        - name: 'test'
          rules:
            - sequence_num: 2
              action: 'permit'
              source:
                any: true
              destination:
                any: true
              ethertype:
                value: '0x88cc'
              remark: 'LLDP'
            - sequence_num: 3
              action: 'permit'
              source:
                any: true
              destination:
                address: '00:00:10:00:00:00'
                address_mask: '00:00:ff:ff:00:00'
              pcp:
                value: 4
                mask: 6
            - sequence_num: 4
              action: 'deny'
              source:
                any: true
              destination:
                any: true
              vlan_tag_format:
                multi_tagged: true
        - name: 'test1'
          remark: 'test_mac_acl'
          rules:
            - sequence_num: 1
              action: 'permit'
              source:
                host: '11:11:11:11:11:11'
              destination:
                any: true
            - sequence_num: 2
              action: 'permit'
              source:
                any: true
              destination:
                any: true
              ethertype:
                arp: true
              vlan_id: 100
            - sequence_num: 3
              action: 'deny'
              source:
                any: true
              destination:
                any: true
              dei: 0
      state: merged

# After State:
# ------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test
#  seq 1 permit host 22:22:22:22:22:22 any vlan 20
#  seq 2 permit any any 0x88cc remark LLDP
#  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
#  seq 4 deny any any vlan-tag-format multi-tagged
# !
# mac access-list test1
#  remark test_mac_acl
#  seq 1 permit host 11:11:11:11:11:11 any
#  seq 2 permit any any arp vlan 100
#  seq 3 deny any any dei 0
# sonic#

# Using replaced
#
# Before State:
# -------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test
#  seq 1 permit host 22:22:22:22:22:22 any vlan 20
#  seq 2 permit any any 0x88cc remark LLDP
#  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
# !
# mac access-list test1
#  remark test_mac_acl
#  seq 1 permit host 11:11:11:11:11:11 any
#  seq 2 permit any any arp vlan 100
#  seq 3 deny any any dei 0
# sonic#

  - name: Replace device configuration of specified Layer 2 ACLs with provided configuration
    dellemc.enterprise_sonic.sonic_l2_acls:
      config:
        - name: 'test1'
          rules:
            - sequence_num: 1
              action: 'permit'
              source:
                any: true
              destination:
                any: true
              ethertype:
                arp: true
              vlan_id: 200
            - sequence_num: 2
              action: 'discard'
              source:
                any: true
              destination:
                any: true
        - name: 'test2'
          rules:
            - sequence_num: 1
              action: 'permit'
              source:
                host: '33:33:33:33:33:33'
              destination:
                host: '44:44:44:44:44:44'
      state: replaced

# After State:
# ------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test
#  seq 1 permit host 22:22:22:22:22:22 any vlan 20
#  seq 2 permit any any 0x88cc remark LLDP
#  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
# !
# mac access-list test1
#  seq 1 permit any any arp vlan 200
#  seq 2 discard any any
# !
# mac access-list test2
#  seq 1 permit host 33:33:33:33:33:33 host 44:44:44:44:44:44
# sonic#

# Using overridden
#
# Before State:
# -------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test
#  seq 1 permit host 22:22:22:22:22:22 any vlan 20
#  seq 2 permit any any 0x88cc remark LLDP
#  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
# !
# mac access-list test1
#  seq 1 permit any any arp vlan 200
#  seq 2 discard any any
# !
# mac access-list test2
#  seq 1 permit host 33:33:33:33:33:33 host 44:44:44:44:44:44
# sonic#

  - name: Override device configuration of all Layer 2 ACLs with provided configuration
    dellemc.enterprise_sonic.sonic_l2_acls:
      config:
        - name: 'test1'
          remark: 'test_mac_acl'
          rules:
            - sequence_num: 1
              action: 'permit'
              source:
                host: '11:11:11:11:11:11'
              destination:
                any: true
              vlan_id: 100
            - sequence_num: 2
              action: 'permit'
              source:
                any: true
              destination:
                any: true
              pcp:
                traffic_type: 'ca'
            - sequence_num: 3
              action: 'deny'
              source:
                any: true
              destination:
                any: true
              ethertype:
                ipv4: true
      state: overridden

# After State:
# ------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test1
#  remark test_mac_acl
#  seq 1 permit host 11:11:11:11:11:11 any vlan 100
#  seq 2 permit any any pcp ca
#  seq 3 deny any any ip
# sonic#

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test
#  seq 1 permit host 22:22:22:22:22:22 any vlan 20
#  seq 2 permit any any 0x88cc remark LLDP
#  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
# !
# mac access-list test1
#  remark test_mac_acl
#  seq 1 permit host 11:11:11:11:11:11 any vlan 100
#  seq 2 deny any any ip
# !
# mac access-list test2
#  seq 1 permit host 33:33:33:33:33:33 host 44:44:44:44:44:44
# sonic#

  - name: Delete specified Layer 2 ACLs, ACL remark and ACL rule entries
    dellemc.enterprise_sonic.sonic_l2_acls:
      config:
        - name: 'test'
          rules:
            - sequence_num: 3
        - name: 'test1'
          remark: 'test_mac_acl'
        - name: 'test2'
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test
#  seq 1 permit host 22:22:22:22:22:22 any vlan 20
#  seq 2 permit any any 0x88cc remark LLDP
# !
# mac access-list test1
#  seq 1 permit host 11:11:11:11:11:11 any vlan 100
#  seq 2 deny any any ip
# sonic#

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration mac access-list
# !
# mac access-list test
#  seq 1 permit host 22:22:22:22:22:22 any vlan 20
#  seq 2 permit any any 0x88cc remark LLDP
#  seq 3 permit any 00:00:10:00:00:00 00:00:ff:ff:00:00 pcp vi pcp-mask 6
# !
# mac access-list test1
#  remark test_mac_acl
#  seq 1 permit host 11:11:11:11:11:11 any vlan 100
#  seq 2 deny any any ip
# !
# mac access-list test2
#  seq 1 permit host 33:33:33:33:33:33 host 44:44:44:44:44:44
# sonic#

  - name: Delete all Layer 2 ACL configurations
    dellemc.enterprise_sonic.sonic_l2_acls:
      config:
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration mac access-list
# sonic#
```

## [Return Values](sonic_l2_acls_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
