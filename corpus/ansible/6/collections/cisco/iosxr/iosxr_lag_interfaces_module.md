---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_lag_interfaces module – Resource module to configure LAG interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_lag_interfaces_module.html
fetched_at: 2026-07-27T16:55:47+00:00
---
# cisco.iosxr.iosxr_lag_interfaces module – Resource module to configure LAG interfaces.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_lag_interfaces`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_lag_interfaces_module.md#synopsis)
- [Parameters](iosxr_lag_interfaces_module.md#parameters)
- [Notes](iosxr_lag_interfaces_module.md#notes)
- [Examples](iosxr_lag_interfaces_module.md#examples)
- [Return Values](iosxr_lag_interfaces_module.md#return-values)

## [Synopsis](iosxr_lag_interfaces_module.md#id1)

- This module manages the attributes of LAG/Ether-Bundle interfaces on IOS-XR devices.

## [Parameters](iosxr_lag_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A provided Link Aggregation Group (LAG) configuration. |
| **links**  dictionary | This dict contains configurable options related to LAG/Ether-Bundle links. |
| **max_active**  integer | Specifies the limit on the number of links that can be active in the LAG/Ether-Bundle.  Refer to vendor documentation for valid values. |
| **min_active**  integer | Specifies the minimum number of active links needed to bring up the LAG/Ether-Bundle.  Refer to vendor documentation for valid values. |
| **load_balancing_hash**  string | Specifies the hash function used for traffic forwarded over the LAG/Ether-Bundle.  Option ‘dst-ip’ uses the destination IP as the hash function.  Option ‘src-ip’ uses the source IP as the hash function.  Choices:   - `"dst-ip"` - `"src-ip"` |
| **members**  list / elements=dictionary | List of member interfaces for the LAG/Ether-Bundle. |
| **member**  string | Name of the member interface. |
| **mode**  string | Specifies the mode of the operation for the member interface.  Mode ‘active’ runs LACP in active mode.  Mode ‘on’ does not run LACP over the port.  Mode ‘passive’ runs LACP in passive mode over the port.  Mode ‘inherit’ runs LACP as configured in the bundle.  Choices:   - `"on"` - `"active"` - `"passive"` - `"inherit"` |
| **mode**  string | LAG mode.  Mode ‘active’ runs LACP in active mode over the port.  Mode ‘on’ does not run LACP over the port.  Mode ‘passive’ runs LACP in passive mode over the port.  Choices:   - `"on"` - `"active"` - `"passive"` |
| **name**  string / required | Name/Identifier of the LAG/Ether-Bundle to configure. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config int**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](iosxr_lag_interfaces_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_lag_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
#
# ------------
# Before state
# ------------
#
# RP/0/0/CPU0:iosxr01#show run int
# Sun Jul  7 19:42:59.416 UTC
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description "GigabitEthernet - 1"
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#
- name: Merge provided configuration with device configuration
  cisco.iosxr.iosxr_lag_interfaces:
    config:
    - name: Bundle-Ether10
      members:
      - member: GigabitEthernet0/0/0/1
        mode: inherit
      - member: GigabitEthernet0/0/0/3
        mode: inherit
      mode: active
      links:
        max_active: 5
        min_active: 2
      load_balancing_hash: src-ip

    - name: Bundle-Ether12
      members:
      - member: GigabitEthernet0/0/0/2
        mode: passive
      - member: GigabitEthernet0/0/0/4
        mode: passive
      load_balancing_hash: dst-ip
    state: merged
#
#
# -----------
# After state
# -----------
#
# RP/0/0/CPU0:iosxr01#show run int
# Sun Jul  7 20:51:17.685 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether12
#  bundle load-balancing hash dst-ip
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#   bundle id 12 mode passive
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 12 mode passive
# !
#

# Using replaced
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/0/CPU0:iosxr01#sho run int
# Sun Jul  7 20:58:06.527 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether12
#  bundle load-balancing hash dst-ip
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 12 mode passive
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 12 mode passive
# !
#
#
- name: Replace device configuration of listed Bundles with provided configurations
  cisco.iosxr.iosxr_lag_interfaces:
    config:
    - name: Bundle-Ether12
      members:
      - name: GigabitEthernet0/0/0/2
      mode: passive

    - name: Bundle-Ether11
      members:
      - name: GigabitEthernet0/0/0/4
      load_balancing_hash: src-ip
    state: replaced
#
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:22:27.397 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether11
#  bundle load-balancing hash src-ip
# !
# interface Bundle-Ether12
#  lacp mode passive
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 12 mode on
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 11 mode on
# !
#
#

# Using overridden
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:22:27.397 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether11
#  bundle load-balancing hash src-ip
# !
# interface Bundle-Ether12
#  lacp mode passive
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 12 mode on
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 11 mode on
# !
#
#

- name: Overrides all device configuration with provided configuration
  cisco.iosxr.iosxr_lag_interfaces:
    config:
    - name: Bundle-Ether10
      members:
      - member: GigabitEthernet0/0/0/1
        mode: inherit
      - member: GigabitEthernet0/0/0/2
        mode: inherit
      mode: active
      load_balancing_hash: dst-ip
    state: overridden
#
#
# ------------
# After state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:43:04.802 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash dst-ip
# !
# interface Bundle-Ether11
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#

# Using deleted
#
#
# ------------
# Before state
# ------------
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:22:27.397 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether11
#  bundle load-balancing hash src-ip
# !
# interface Bundle-Ether12
#  lacp mode passive
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#  bundle id 12 mode on
# !n
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 11 mode on
# !
#
#

- name: Delete attributes of given bundles and removes member interfaces from them
    (Note - This won't delete the bundles themselves)
  cisco.iosxr.iosxr_lag_interfaces:
    config:
    - name: Bundle-Ether10
    - name: Bundle-Ether11
    - name: Bundle-Ether12
    state: deleted

#
#
# ------------
# After state
# ------------
#
# RP/0/0/CPU0:iosxr01#sh run int
# Sun Jul  7 21:49:50.004 UTC
# interface Bundle-Ether10
# !
# interface Bundle-Ether11
# !
# interface Bundle-Ether12
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
# !
#
#

# Using deleted (without config)
#
#
# ------------
# Before state
# ------------
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Aug 18 19:49:51.908 UTC
# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 10
#  bundle minimum-active links 2
# !
# interface Bundle-Ether11
#  bundle load-balancing hash dst-ip
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
# !
# interface GigabitEthernet0/0/0/1
#  bundle id 10 mode inherit
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  bundle id 10 mode passive
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  bundle id 11 mode passive
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  bundle id 11 mode passive
#  shutdown
# !
#

- name: Delete attributes of all bundles and removes member interfaces from them (Note
    - This won't delete the bundles themselves)
  cisco.iosxr.iosxr_lag_interfaces:
    state: deleted

#
#
# ------------
# After state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run int
# Sun Aug 18 19:54:22.389 UTC
# interface Bundle-Ether10
# !
# interface Bundle-Ether11
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 10.8.38.69 255.255.255.0
# !
# interface GigabitEthernet0/0/0/0
#  shutdown
# !
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !

# Using parsed:

# parsed.cfg

# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether12
#  bundle load-balancing hash dst-ip
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#   bundle id 12 mode passive
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 12 mode passive
# !
#
- name: Convert lag interfaces config to argspec without connecting to the appliance
  cisco.iosxr.iosxr_lag_interfaces:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# --------------
# Output
# --------------
#   parsed:
#     - name: Bundle-Ether10
#       members:
#         - member: GigabitEthernet0/0/0/1
#           mode: inherit
#         - member: GigabitEthernet0/0/0/3
#           mode: inherit
#       mode: active
#       links:
#         max_active: 5
#         min_active: 2
#       load_balancing_hash: src-ip

#     - name: Bundle-Ether12
#       members:
#         - member: GigabitEthernet0/0/0/2
#           mode: passive
#         - member: GigabitEthernet0/0/0/4
#           mode: passive
#       load_balancing_hash: dst-ip

# using gathered

# Device Config:
# -------------

# interface Bundle-Ether10
#  lacp mode active
#  bundle load-balancing hash src-ip
#  bundle maximum-active links 5
#  bundle minimum-active links 2
# !
# interface Bundle-Ether12
#  bundle load-balancing hash dst-ip
# !
# interface Loopback888
#  description test for ansible
#  shutdown
# !
# interface MgmtEth0/0/CPU0/0
#  ipv4 address 192.0.2.11 255.255.255.0
# !
# interface GigabitEthernet0/0/0/1
#  description 'GigabitEthernet - 1"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/2
#  description "GigabitEthernet - 2"
#   bundle id 12 mode passive
# !
# interface GigabitEthernet0/0/0/3
#  description "GigabitEthernet - 3"
#  bundle id 10 mode inherit
# !
# interface GigabitEthernet0/0/0/4
#  description "GigabitEthernet - 4"
#  bundle id 12 mode passive
# !
#

- name: Gather IOSXR lag interfaces configuration
  cisco.iosxr.iosxr_lag_interfaces:
    config:
    state: gathered

# --------------
# Output
# --------------
#   gathered:
#     - name: Bundle-Ether10
#       members:
#         - member: GigabitEthernet0/0/0/1
#           mode: inherit
#         - member: GigabitEthernet0/0/0/3
#           mode: inherit
#       mode: active
#       links:
#         max_active: 5
#         min_active: 2
#       load_balancing_hash: src-ip

#     - name: Bundle-Ether12
#       members:
#         - member: GigabitEthernet0/0/0/2
#           mode: passive
#         - member: GigabitEthernet0/0/0/4
#           mode: passive
#       load_balancing_hash: dst-ip

# Using rendered:
- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_lag_interfaces:
    config:
    - name: Bundle-Ether10
      members:
      - member: GigabitEthernet0/0/0/1
        mode: inherit
      - member: GigabitEthernet0/0/0/3
        mode: inherit
      mode: active
      links:
        max_active: 5
        min_active: 2
      load_balancing_hash: src-ip

    - name: Bundle-Ether12
      members:
      - member: GigabitEthernet0/0/0/2
        mode: passive
      - member: GigabitEthernet0/0/0/4
        mode: passive
      load_balancing_hash: dst-ip
    state: rendered

# Output:

# rendered:
#    [
#         - "interface Bundle-Ether10"
#         - " lacp mode active"
#         - " bundle load-balancing hash src-ip"
#         - " bundle maximum-active links 5"
#         - " bundle minimum-active links 2"
#         - "interface Bundle-Ether12"
#         - " bundle load-balancing hash dst-ip"
#         - "interface Loopback888"
#         - " description test for ansible"
#         - " shutdown"
#         - "interface MgmtEth0/0/CPU0/0"
#         - " ipv4 address 192.0.2.11 255.255.255.0"
#         - "interface GigabitEthernet0/0/0/1"
#         - " description 'GigabitEthernet - 1""
#         - " bundle id 10 mode inherit"
#         - "interface GigabitEthernet0/0/0/2"
#         - " description "GigabitEthernet - 2""
#         - "  bundle id 12 mode passive"
#         - "interface GigabitEthernet0/0/0/3"
#         - " description "GigabitEthernet - 3""
#         - " bundle id 10 mode inherit"
#         - "interface GigabitEthernet0/0/0/4"
#         - " description "GigabitEthernet - 4""
#         - " bundle id 12 mode passive"
#    ]
#
#
```

## [Return Values](iosxr_lag_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface Bundle-Ether10", "bundle minimum-active links 2", "bundle load-balancing hash src-ip"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
