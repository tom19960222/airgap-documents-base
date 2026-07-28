---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_prefix_lists module – prefix list configuration handling for SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_prefix_lists_module.html
fetched_at: 2026-07-28T02:03:47+00:00
---
# dellemc.enterprise_sonic.sonic_prefix_lists module – prefix list configuration handling for SONiC

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_prefix_lists`.

New in dellemc.enterprise_sonic 2.0.0

- [Synopsis](sonic_prefix_lists_module.md#synopsis)
- [Parameters](sonic_prefix_lists_module.md#parameters)
- [Examples](sonic_prefix_lists_module.md#examples)
- [Return Values](sonic_prefix_lists_module.md#return-values)

## [Synopsis](sonic_prefix_lists_module.md#id1)

- This module provides configuration management for prefix list parameters on devices running SONiC.

## [Parameters](sonic_prefix_lists_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies a list of prefix set configuration dictionaries |
| **afi**  string | Specifies the Address Family for addresses in the prefix list entries  **Choices:**   - `"ipv4"` ← (default) - `"ipv6"` |
| **name**  string / required | Name of a prefix set (a list of prefix entries) |
| **prefixes**  list / elements=dictionary | A list of prefix entries |
| **action**  string / required | Action to be taken for addresses matching this prefix entry  **Choices:**   - `"permit"` - `"deny"` |
| **ge**  integer | Minimum prefix length to be matched |
| **le**  integer | Maximum prefix length to be matched |
| **prefix**  string / required | IPv4 or IPv6 prefix in A.B.C.D/LEN or A:B::C:D/LEN format |
| **sequence**  integer / required | Precedence for this prefix entry (unique within the prefix list) |
| **state**  string | Specifies the type of configuration update to be performed on the device.  For “merged”, merge specified attributes with existing configured attributes.  For “deleted”, delete the specified attributes from existing configuration.  For “replaced”, replace the specified existing configuration with the provided configuration.  For “overridden”, override the existing configuration with the provided configuration.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Examples](sonic_prefix_lists_module.md#id3)

```yaml+jinja
# Using "merged" state to create initial configuration
#
# Before state:
# -------------
#
# sonic# show running-configuration ip prefix-list
# sonic#
# (No configuration present)
#
# -------------
#
- name: Merge initial prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx1
         afi: "ipv4"
         prefixes:
           - sequence: 10
             prefix: "1.2.3.4/24"
             action: "permit"
             ge: 26
             le: 30
     state: merged

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
# ------------
#
# ***************************************************************
# Using "merged" state to update and add configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# (no IPv6 prefix-list configuration present)
#
# ------------
#
- name: Merge additional prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx1
         afi: "ipv4"
         prefixes:
           - sequence: 20
             action: "deny"
             prefix: "1.2.3.12/26"
           - sequence: 30
             action: "permit"
             prefix: "7.8.9.0/24"
       - name: pfx6
         afi: "ipv6"
         prefixes:
           - sequence: 25
             action: "permit"
             prefix: "40::300/124"
     state: merged

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
# ip prefix-list pfx1 seq 20 deny 1.2.3.12/26
# ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
#
# sonic# show running-configuration ipv6 prefix-list
# !
# ipv6 prefix-list pfx6 seq 25 permit 40::300/124
#
# ***************************************************************
# Using "deleted" state to remove configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
# ip prefix-list pfx1 seq 20 deny 1.2.3.12/26
# ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
#
# sonic# show running-configuration ipv6 prefix-list
# !
# ipv6 prefix-list pfx6 seq 25 permit 40::300/124
#
# ------------
#
- name: Delete selected prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx1
         afi: "ipv4"
         prefixes:
           - sequence: 10
             prefix: "1.2.3.4/24"
             action: "permit"
             ge: 26
             le: 30
           - sequence: 20
             action: "deny"
             prefix: "1.2.3.12/26"
       - name: pfx6
         afi: "ipv6"
         prefixes:
           - sequence: 25
             action: "permit"
             prefix: "40::300/124"
     state: deleted

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 30 permit 7.8.9.0/24
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# (no IPv6 prefix-list configuration present)
#
# ***************************************************************
# Using "overriden" state to override configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx1 seq 10 permit 1.2.3.4/24 ge 26 le 30
# ip prefix-list pfx3 seq 20 deny 1.2.3.12/26
# ip prefix-list pfx4 seq 30 permit 7.8.9.0/24
#
# sonic# show running-configuration ipv6 prefix-list
# !
# ipv6 prefix-list pfx6 seq 25 permit 40::300/124
#
# ------------
#
- name: Override prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx2
         afi: "ipv4"
         prefixes:
           - sequence: 10
             prefix: "10.20.30.128/24"
             action: "deny"
             ge: 25
             le: 30
     state: overridden

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx2 seq 10 deny 10.20.30.128/24 ge 25 le 30
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# (no IPv6 prefix-list configuration present)
#
# ***************************************************************
# Using "replaced" state to replace configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx2 seq 10 deny 10.20.30.128/24 ge 25 le 30
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# (no IPv6 prefix-list configuration present)
#
# ------------
#
- name: Replace prefix-list configuration
  dellemc.enterprise_sonic.sonic_prefix_lists:
     config:
       - name: pfx2
         afi: "ipv4"
         prefixes:
           - sequence: 10
             prefix: "10.20.30.128/24"
             action: "permit"
             ge: 25
             le: 30
       - name: pfx3
         afi: "ipv6"
         prefixes:
           - sequence: 20
             action: "deny"
             prefix: "60::70/124"
     state: replaced

# After state:
# ------------
#
# sonic# show running-configuration ip prefix-list
# !
# ip prefix-list pfx2 seq 10 permit 10.20.30.128/24 ge 25 le 30
#
# sonic# show running-configuration ipv6 prefix-list
# sonic#
# !
# ipv6 prefix-list pfx3 seq 20 deny 60::70/124
#
```

## [Return Values](sonic_prefix_lists_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `[""]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `[""]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always |

### Authors

- Kerry Meyer (@kerry-meyer)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
