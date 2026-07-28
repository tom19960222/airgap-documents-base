---
collection: ansible
version: "6"
title: "cisco.ios.ios_lldp_interfaces module – Resource module to configure LLDP interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_lldp_interfaces_module.html
fetched_at: 2026-07-27T16:55:20+00:00
---
# cisco.ios.ios_lldp_interfaces module – Resource module to configure LLDP interfaces.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_lldp_interfaces`.

New in cisco.ios 1.0.0

- [Synopsis](ios_lldp_interfaces_module.md#synopsis)
- [Parameters](ios_lldp_interfaces_module.md#parameters)
- [Notes](ios_lldp_interfaces_module.md#notes)
- [Examples](ios_lldp_interfaces_module.md#examples)
- [Return Values](ios_lldp_interfaces_module.md#return-values)

## [Synopsis](ios_lldp_interfaces_module.md#id1)

- This module manages link layer discovery protocol (LLDP) attributes of interfaces on Cisco IOS devices.

## [Parameters](ios_lldp_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of LLDP options |
| **med_tlv_select**  dictionary | Selection of LLDP MED TLVs to send  NOTE, if med-tlv-select is configured idempotency won’t be maintained as Cisco device doesn’t record configured med-tlv-select options. As such, Ansible cannot verify if the respective med-tlv-select options is already configured or not from the device side. If you try to apply med-tlv-select option in every play run, Ansible will show changed as True. |
| **inventory_management**  boolean | LLDP MED Inventory Management TLV  Choices:   - `false` - `true` |
| **name**  string / required | Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1. |
| **receive**  boolean | Enable LLDP reception on interface.  Choices:   - `false` - `true` |
| **tlv_select**  dictionary | Selection of LLDP type-length-value i.e. TLVs to send  NOTE, if tlv-select is configured idempotency won’t be maintained as Cisco device doesn’t record configured tlv-select options. As such, Ansible cannot verify if the respective tlv-select options is already configured or not from the device side. If you try to apply tlv-select option in every play run, Ansible will show changed as True. |
| **power_management**  boolean | IEEE 802.3 DTE Power via MDI TLV  Choices:   - `false` - `true` |
| **transmit**  boolean | Enable LLDP transmission on interface.  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh lldp interface**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](ios_lldp_interfaces_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.2 on VIRL.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_lldp_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#

- name: Merge provided configuration with device configuration
  cisco.ios.ios_lldp_interfaces:
    config:
    - name: GigabitEthernet0/1
      receive: true
      transmit: true
    - name: GigabitEthernet0/2
      receive: true
    - name: GigabitEthernet0/3
      transmit: true
    state: merged

# After state:
# ------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: disabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: enabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#

# Using overridden
#
# Before state:
# -------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME

- name: Override device configuration of all lldp_interfaces with provided configuration
  cisco.ios.ios_lldp_interfaces:
    config:
    - name: GigabitEthernet0/2
      receive: true
      transmit: true
    state: overridden

# After state:
# ------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME

# Using replaced
#
# Before state:
# -------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#

- name: Replaces device configuration of listed lldp_interfaces with provided configuration
  cisco.ios.ios_lldp_interfaces:
    config:
    - name: GigabitEthernet0/2
      receive: true
      transmit: true
    - name: GigabitEthernet0/3
      receive: true
    state: replaced

# After state:
# ------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: disabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#

# Using Deleted
#
# Before state:
# -------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME

- name: "Delete LLDP attributes of given interfaces (Note: This won't delete the interface itself)"
  cisco.ios.ios_lldp_interfaces:
    config:
    - name: GigabitEthernet0/1
    state: deleted

# After state:
# -------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/2:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#

# Using Deleted without any config passed
# "(NOTE: This will delete all of configured LLDP module attributes)"
#
# Before state:
# -------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME

- name: "Delete LLDP attributes for all configured interfaces (Note: This won't delete the interface itself)"
  cisco.ios.ios_lldp_interfaces:
    state: deleted

# After state:
# -------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: INIT
#
# GigabitEthernet0/3:
#    Tx: disabled
#    Rx: disabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME

# Using Gathered

# Before state:
# -------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME

- name: Gather listed LLDP interfaces with provided configurations
  cisco.ios.ios_lldp_interfaces:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "name": "GigabitEthernet0/0",
#             "receive": true,
#             "transmit": true
#         },
#         {
#             "name": "GigabitEthernet0/1",
#             "receive": true,
#             "transmit": true
#         },
#         {
#             "name": "GigabitEthernet0/2",
#             "receive": true,
#             "transmit": true
#         }
#     ]

# After state:
# ------------
#
# vios#sh lldp interface
# GigabitEthernet0/0:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME

# GigabitEthernet0/2:
#    Tx: enabled
#    Rx: enabled
#    Tx state: IDLE
#    Rx state: WAIT FOR FRAME

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_lldp_interfaces:
    config:
    - name: GigabitEthernet0/0
      receive: true
      transmit: true
    - name: GigabitEthernet0/1
      receive: true
      transmit: true
    - name: GigabitEthernet0/2
      receive: true
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "interface GigabitEthernet0/0",
#         "lldp receive",
#         "lldp transmit",
#         "interface GigabitEthernet0/1",
#         "lldp receive",
#         "lldp transmit",
#         "interface GigabitEthernet0/2",
#         "lldp receive"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# GigabitEthernet0/0:
#   Tx: enabled
#   Rx: disabled
#   Tx state: IDLE
#   Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/1:
#   Tx: enabled
#   Rx: enabled
#   Tx state: IDLE
#   Rx state: WAIT FOR FRAME
#
# GigabitEthernet0/2:
#   Tx: disabled
#   Rx: enabled
#   Tx state: IDLE
#   Rx state: INIT

- name: Parse the commands for provided configuration
  cisco.ios.ios_lldp_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "name": "GigabitEthernet0/0",
#             "receive": false,
#             "transmit": true
#         },
#         {
#             "name": "GigabitEthernet0/1",
#             "receive": true,
#             "transmit": true
#         },
#         {
#             "name": "GigabitEthernet0/2",
#             "receive": true,
#             "transmit": false
#         }
#     ]
```

## [Return Values](ios_lldp_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["interface GigabitEthernet 0/1", "lldp transmit", "lldp receive"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
