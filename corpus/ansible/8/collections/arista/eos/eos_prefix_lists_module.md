---
collection: ansible
version: "8"
title: "arista.eos.eos_prefix_lists module – Manages Prefix lists resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_prefix_lists_module.html
fetched_at: 2026-07-28T01:11:13+00:00
---
# arista.eos.eos_prefix_lists module – Manages Prefix lists resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_prefix_lists`.

New in arista.eos 2.2.0

- [Synopsis](eos_prefix_lists_module.md#synopsis)
- [Parameters](eos_prefix_lists_module.md#parameters)
- [Notes](eos_prefix_lists_module.md#notes)
- [Examples](eos_prefix_lists_module.md#examples)
- [Return Values](eos_prefix_lists_module.md#return-values)

## [Synopsis](eos_prefix_lists_module.md#id1)

- This module configures and manages the attributes of Prefix lists on Arista EOS platforms.

Aliases: prefix_lists

## [Parameters](eos_prefix_lists_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of dictionary of prefix-list options |
| **afi**  string / required | The Address Family Indicator (AFI) for the prefix list.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **prefix_lists**  list / elements=dictionary | A list of prefix-lists. |
| **entries**  list / elements=dictionary | List of prefix-lists |
| **action**  string | action to be performed on the specified path  **Choices:**   - `"deny"` - `"permit"` |
| **address**  string | ipv4/v6 address in prefix-mask or address-masklen format |
| **match**  dictionary | match masklen |
| **masklen**  integer | Mask Length. |
| **operator**  string | equalto/greater than/lesser than  **Choices:**   - `"eq"` - `"le"` - `"ge"` |
| **resequence**  dictionary | Resequence the list. |
| **default**  boolean | Resequence with default values (10).  **Choices:**   - `false` - `true` |
| **start_seq**  integer | Starting sequence number. |
| **step**  integer | Step to increment the sequence number. |
| **sequence**  integer | sequence number |
| **name**  string / required | Name of the prefix-list |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section access-list**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_prefix_lists_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](eos_platform_options.md).

## [Examples](eos_prefix_lists_module.md#id4)

```yaml+jinja
# Using merged

# Before state
# veos#show running-config | section prefix-lists
# veos#

- name: Merge provided configuration with device configuration
  arista.eos.eos_prefix_lists:
    config:
      - afi: "ipv4"
        prefix_lists:
          - name: "v401"
            entries:
              - sequence: 25
                action: "deny"
                address: "45.55.4.0/24"
              - sequence: 100
                action: "permit"
                address: "11.11.2.0/24"
                match:
                  masklen: 32
                  operator: "ge"
          - name: "v402"
            entries:
              - action: "deny"
                address: "10.1.1.0/24"
                sequence: 10
                match:
                  masklen: 32
                  operator: "ge"
      - afi: "ipv6"
        prefix_lists:
          - name: "v601"
            entries:
              - sequence: 125
                action: "deny"
                address: "5000:1::/64"

# Task Output
# -------------
# before: {}
# commands:
# - ipv6 prefix-list v601
# - seq 125 deny 5000:1::/64
# - ip prefix-list v401
# - seq 25 deny 45.55.4.0/24
# - seq 100 permit 11.11.2.0/24 ge 32
# - ip prefix-list v402
# - seq 10 deny 10.1.1.0/24 ge 32
# after:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       sequence: 25
#     - action: permit
#       address: 11.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 100
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 10
#     name: v402
# - afi: ipv6
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 5000:1::/64
#       sequence: 125
#     name: v601

# After state:
# ------------
# veos#
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24
#    seq 100 permit 11.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24 ge 32
# !
# ipv6 prefix-list v601
#    seq 125 deny 5000:1::/64
# veos#

# Using merged:
# Failure scenario : 'merged' should not be used when an existing prefix-list (sequence number)
# is to be modified.

# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24
#    seq 100 permit 11.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24 ge 32
# !
# ipv6 prefix-list v601
#    seq 125 deny 5000:1::/64
# veos#

- name: Merge provided configuration with device configuration
  arista.eos.eos_prefix_lists:
    config:
      - afi: "ipv4"
        prefix_lists:
          - name: "v401"
            entries:
              - sequence: 25
                action: "deny"
                address: "45.55.4.0/24"
                match:
                  masklen: 32
                  operator: "ge"
              - sequence: 100
                action: "permit"
                address: "11.11.2.0/24"
                match:
                  masklen: 32
                  operator: "ge"
          - name: "v402"
            entries:
              - action: "deny"
                address: "10.1.1.0/24"
                sequence: 10
                match:
                  masklen: 32
                  operator: "ge"
      - afi: "ipv6"
        prefix_lists:
          - name: "v601"
            entries:
              - sequence: 125
                action: "deny"
                address: "5000:1::/64"
    state: merged

# Task Output
# -------------
# changed: false
# invocation:
#   module_args:
#     config:
#     - afi: ipv4
#       prefix_lists:
#       - entries:
#         - action: deny
#           address: 45.55.4.0/24
#           match:
#             masklen: 32
#             operator: ge
#           resequence:
#           sequence: 25
#         - action: permit
#           address: 11.11.2.0/24
#           match:
#             masklen: 32
#             operator: ge
#           resequence:
#           sequence: 100
#         name: v401
#       - entries:
#         - action: deny
#           address: 10.1.1.0/24
#           match:
#             masklen: 32
#             operator: ge
#           resequence:
#           sequence: 10
#         name: v402
#     - afi: ipv6
#       prefix_lists:
#       - entries:
#         - action: deny
#           address: 5000:1::/64
#           match:
#           resequence:
#           sequence: 125
#         name: v601
#     running_config:
#     state: merged
# msg: Sequence number 25 is already present. Use replaced/overridden operation to change
#   the configuration

# Using Replaced:

# Before state:
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24
#    seq 100 permit 11.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24 ge 32
# !
# ipv6 prefix-list v601
#    seq 125 deny 5000:1::/64
# veos#

- name: Replace Provided configuration with given configuration
  arista.eos.eos_prefix_lists:
    config:
      - afi: "ipv4"
        prefix_lists:
          - name: "v401"
            entries:
              - sequence: 25
                action: "deny"
                address: "45.55.4.0/24"
                match:
                  masklen: 32
                  operator: "ge"
              - sequence: 200
                action: "permit"
                address: "200.11.2.0/24"
                match:
                  masklen: 32
                  operator: "ge"
    state: replaced

# Task Output
# -------------
# before:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       sequence: 25
#     - action: permit
#       address: 11.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 100
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 10
#     name: v402
# - afi: ipv6
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 5000:1::/64
#       sequence: 125
#     name: v601
# commands:
# - ip prefix-list v401
# - no seq 25
# - seq 25 deny 45.55.4.0/24 ge 32
# - seq 200 permit 200.11.2.0/24 ge 32
# - no seq 100
# - no ip prefix-list v402
# after:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 25
#     - action: permit
#       address: 200.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 200
#     name: v401
# - afi: ipv6
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 5000:1::/64
#       sequence: 125
#     name: v601

# After State:
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24 ge 32
#    seq 200 permit 200.11.2.0/24 ge 32
# !
# ipv6 prefix-list v601
#    seq 125 deny 5000:1::/64
# veos#
#
#

# Using overridden:

# Before State:
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24 ge 32
#    seq 100 permit 11.11.2.0/24 ge 32
#    seq 200 permit 200.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24 ge 32
# !
# ipv6 prefix-list v601
#    seq 125 deny 5000:1::/64
# veos#

- name: Override
  arista.eos.eos_prefix_lists:
    config:
      - afi: "ipv4"
        prefix_lists:
          - name: "v401"
            entries:
              - sequence: 25
                action: "deny"
                address: "45.55.4.0/24"
              - sequence: 300
                action: "permit"
                address: "30.11.2.0/24"
                match:
                  masklen: 32
                  operator: "ge"
          - name: "v403"
            entries:
              - action: "deny"
                address: "10.1.1.0/24"
                sequence: 10
    state: overridden

# Task Output
# -------------
# before:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 25
#     - action: permit
#       address: 11.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 100
#     - action: permit
#       address: 200.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 200
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 10
#     name: v402
# - afi: ipv6
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 5000:1::/64
#       sequence: 125
#     name: v601
# commands:
# - no ipv6 prefix-list v601
# - ip prefix-list v401
# - seq 25 deny 45.55.4.0/24
# - seq 300 permit 30.11.2.0/24 ge 32
# - no seq 100
# - no seq 200
# - ip prefix-list v403
# - seq 10 deny 10.1.1.0/24
# - no ip prefix-list v402
# after:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 25
#     - action: permit
#       address: 30.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 300
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       sequence: 10
#     name: v403

# After State
# veos#
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24 ge 32
#    seq 300 permit 30.11.2.0/24 ge 32
# !
# ip prefix-list v403
#    seq 10 deny 10.1.1.0/24
# veos#

# Using deleted:

# Before State:
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24 ge 32
#    seq 100 permit 11.11.2.0/24 ge 32
#    seq 300 permit 30.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24 ge 32
# !
# ip prefix-list v403
#    seq 10 deny 10.1.1.0/24
# !
# ipv6 prefix-list v601
#    seq 125 deny 5000:1::/64
# veos#

- name: Delete device configuration
  arista.eos.eos_prefix_lists:
    config:
      - afi: "ipv6"
    state: deleted

# Task Output
# -------------
# before:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 25
#     - action: permit
#       address: 11.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 100
#     - action: permit
#       address: 30.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 300
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 10
#     name: v402
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       sequence: 10
#     name: v403
# - afi: ipv6
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 5000:1::/64
#       sequence: 125
#     name: v601
# commands:
# - no ipv6 prefix-list v601
# after:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 25
#     - action: permit
#       address: 11.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 100
#     - action: permit
#       address: 30.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 300
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 10
#     name: v402
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       sequence: 10
#     name: v403

# after State:
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24 ge 32
#    seq 100 permit 11.11.2.0/24 ge 32
#    seq 300 permit 30.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24 ge 32
# !
# ip prefix-list v403
#    seq 10 deny 10.1.1.0/24
#

# Using deleted

# Before state:
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24 ge 32
#    seq 100 permit 11.11.2.0/24 ge 32
#    seq 300 permit 30.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24 ge 32
# !
# ip prefix-list v403
#    seq 10 deny 10.1.1.0/24
# veos#

- name: Delete device configuration
  arista.eos.eos_prefix_lists:
    state: deleted

# Task Output
# -------------
# before:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 25
#     - action: permit
#       address: 11.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 100
#     - action: permit
#       address: 30.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 300
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 10
#     name: v402
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       sequence: 10
#     name: v403
# commands:
# - no ip prefix-list v401
# - no ip prefix-list v402
# - no ip prefix-list v403
# after: {}

# After State:
# veos#show running-config | section prefix-list
# veos#

# Using parsed:

# parse_prefix_lists.cfg
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24
#    seq 100 permit 11.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24
# !
# ipv6 prefix-list v601
#    seq 125 deny 5000:1::/64
#

- name: parse configs
  arista.eos.eos_prefix_lists:
    running_config: "{{ lookup('file', './parsed_prefix_lists.cfg') }}"
    state: parsed

# Task Output
# -------------
# parsed:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       sequence: 25
#     - action: permit
#       address: 11.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 100
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       sequence: 10
#     name: v402
# - afi: ipv6
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 5000:1::/64
#       sequence: 125
#     name: v601

# Using rendered:

- name: Render provided configuration
  arista.eos.eos_prefix_lists:
    config:
      - afi: "ipv4"
        prefix_lists:
          - name: "v401"
            entries:
              - sequence: 25
                action: "deny"
                address: "45.55.4.0/24"
              - sequence: 200
                action: "permit"
                address: "200.11.2.0/24"
                match:
                  masklen: 32
                  operator: "ge"
          - name: "v403"
            entries:
              - action: "deny"
                address: "10.1.1.0/24"
                sequence: 10
    state: rendered

# Task Output
# -------------
# rendered:
# - ip prefix-list v401
# - seq 25 deny 45.55.4.0/24
# - seq 200 permit 200.11.2.0/24 ge 32
# - ip prefix-list v403
# - seq 10 deny 10.1.1.0/24

# using gathered:

# Device config:
# veos#show running-config | section prefix-list
# ip prefix-list v401
#    seq 25 deny 45.55.4.0/24
#    seq 100 permit 11.11.2.0/24 ge 32
# !
# ip prefix-list v402
#    seq 10 deny 10.1.1.0/24 ge 32
# !
# ipv6 prefix-list v601
#    seq 125 deny 5000:1::/64
# veos#

- name: gather configs
  arista.eos.eos_prefix_lists:
    state: gathered

# Task Output
# -------------
# gathered:
# - afi: ipv4
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 45.55.4.0/24
#       sequence: 25
#     - action: permit
#       address: 11.11.2.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 100
#     name: v401
#   - entries:
#     - action: deny
#       address: 10.1.1.0/24
#       match:
#         masklen: 32
#         operator: ge
#       sequence: 10
#     name: v402
# - afi: ipv6
#   prefix_lists:
#   - entries:
#     - action: deny
#       address: 5000:1::/64
#       sequence: 125
#     name: v601
```

## [Return Values](eos_prefix_lists_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["ip prefix-list v401", "seq 25 deny 45.55.4.0/24", "seq 200 permit 200.11.2.0/24 ge 32", "ip prefix-list v403", "seq 10 deny 10.1.1.0/24"]` |
| **gathered**  list / elements=string | The configuration as structured data transformed for the running configuration fetched from remote host  **Returned:** When `state` is *gathered*  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **parsed**  list / elements=string | The configuration as structured data transformed for the value of `running_config` option  **Returned:** When `state` is *parsed*  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **rendered**  list / elements=string | The set of CLI commands generated from the value in `config` option  **Returned:** When `state` is *rendered*  **Sample:** `["- ip prefix-list v401 - seq 25 deny 45.55.4.0/24 - seq 200 permit 200.11.2.0/24 ge 32 - ip prefix-list v403 - seq 10 deny 10.1.1.0/24\n"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
