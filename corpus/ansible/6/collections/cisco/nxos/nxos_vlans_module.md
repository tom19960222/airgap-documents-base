---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_vlans module – VLANs resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_vlans_module.html
fetched_at: 2026-07-27T17:02:32+00:00
---
# cisco.nxos.nxos_vlans module – VLANs resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vlans`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vlans_module.md#synopsis)
- [Parameters](nxos_vlans_module.md#parameters)
- [Notes](nxos_vlans_module.md#notes)
- [Examples](nxos_vlans_module.md#examples)
- [Return Values](nxos_vlans_module.md#return-values)

## [Synopsis](nxos_vlans_module.md#id1)

- This module creates and manages VLAN configurations on Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_vlans_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of Vlan options |
| **enabled**  boolean | Manage administrative state of the vlan.  Choices:   - `false` - `true` |
| **mapped_vni**  integer | The Virtual Network Identifier (VNI) ID that is mapped to the VLAN. |
| **mode**  string | Set vlan mode to classical ethernet or fabricpath. This is a valid option for Nexus 5000, 6000 and 7000 series.  Choices:   - `"ce"` - `"fabricpath"` |
| **name**  string | Name of VLAN. |
| **state**  string | Manage operational state of the vlan.  Choices:   - `"active"` - `"suspend"` |
| **vlan_id**  integer / required | Vlan ID. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the commands **show vlans | json-pretty** and **show running-config | section ^vlan** in order and delimited by a line.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  The state *overridden* would override the configuration of all the VLANs on the device (including VLAN 1) with the provided configuration in the task. Use caution with this state.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_vlans_module.md#id3)

> **Note:**
>
> - Tested against NXOS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS

## [Examples](nxos_vlans_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# vlan 1

- name: Merge provided configuration with device configuration.
  cisco.nxos.nxos_vlans:
    config:
    - vlan_id: 5
      name: test-vlan5
    - vlan_id: 10
      enabled: false
    state: merged

# After state:
# ------------
# vlan 5
#   name test-vlan5
#   state active
#   no shutdown
# vlan 10
#   state active
#   shutdown

# Using replaced

# Before state:
# -------------
# vlan 1
# vlan 5
#   name test-vlan5
# vlan 10
#   shutdown

- name: Replace device configuration of specified vlan with provided configuration.
  cisco.nxos.nxos_vlans:
    config:
    - vlan_id: 5
      name: test-vlan
      enabled: false
    - vlan_id: 10
      enabled: false
    state: replaced

# After state:
# ------------
# vlan 1
# vlan 5
#   name test-vlan
#   state active
#   shutdown
# vlan 10
#   state active
#   shutdown

# Using overridden

# Before state:
# -------------
# vlan 1
# vlan 3
#   name testing
# vlan 5
#   name test-vlan5
#   shutdown
# vlan 10
#   shutdown

- name: Override device configuration of all vlans with provided configuration.
  cisco.nxos.nxos_vlans:
    config:
    - vlan_id: 5
      name: test-vlan
    - vlan_id: 10
      state: active
    state: overridden

# After state:
# ------------
# vlan 5
#   name test-vlan
#   state active
#   no shutdown
# vlan 10
#   state active
#   no shutdown

# Using deleted

# Before state:
# -------------
# vlan 1
# vlan 5
# vlan 10

- name: Delete vlans.
  cisco.nxos.nxos_vlans:
    config:
    - vlan_id: 5
    - vlan_id: 10
    state: deleted

# After state:
# ------------
#

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_vlans:
    config:
    - vlan_id: 5
      name: vlan5
      mapped_vni: 100

    - vlan_id: 6
      name: vlan6
      state: suspend
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#   - vlan 5
#   - name vlan5
#   - vn-segment 100
#   - vlan 6
#   - name vlan6
#   - state suspend

# Using parsed

# parsed.cfg
# ------------
# {
#     "TABLE_vlanbrief": {
#        "ROW_vlanbrief": [
#            {
#                "vlanshowbr-vlanid": "1",
#                "vlanshowbr-vlanid-utf": "1",
#                "vlanshowbr-vlanname": "default",
#                "vlanshowbr-vlanstate": "active",
#                "vlanshowbr-shutstate": "noshutdown"
#            },
#            {
#                "vlanshowbr-vlanid": "5",
#                "vlanshowbr-vlanid-utf": "5",
#                "vlanshowbr-vlanname": "vlan5",
#                "vlanshowbr-vlanstate": "suspend",
#                "vlanshowbr-shutstate": "noshutdown"
#            },
#            {
#                "vlanshowbr-vlanid": "6",
#                "vlanshowbr-vlanid-utf": "6",
#                "vlanshowbr-vlanname": "VLAN0006",
#                "vlanshowbr-vlanstate": "active",
#                "vlanshowbr-shutstate": "noshutdown"
#            },
#            {
#                "vlanshowbr-vlanid": "7",
#                "vlanshowbr-vlanid-utf": "7",
#                "vlanshowbr-vlanname": "vlan7",
#                "vlanshowbr-vlanstate": "active",
#                "vlanshowbr-shutstate": "noshutdown"
#            }
#        ]
#    },
#    "TABLE_mtuinfo": {
#        "ROW_mtuinfo": [
#            {
#                "vlanshowinfo-vlanid": "1",
#                "vlanshowinfo-media-type": "enet",
#                "vlanshowinfo-vlanmode": "ce-vlan"
#            },
#            {
#                "vlanshowinfo-vlanid": "5",
#                "vlanshowinfo-media-type": "enet",
#                "vlanshowinfo-vlanmode": "ce-vlan"
#            },
#            {
#                "vlanshowinfo-vlanid": "6",
#                "vlanshowinfo-media-type": "enet",
#                "vlanshowinfo-vlanmode": "ce-vlan"
#            },
#            {
#                "vlanshowinfo-vlanid": "7",
#                "vlanshowinfo-media-type": "enet",
#                "vlanshowinfo-vlanmode": "ce-vlan"
#             }
#        ]
#    }
# }
#
# vlan 1,5-7
# vlan 5
#   state suspend
#   name vlan5
# vlan 7
#   name vlan7
#   vn-segment 100

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_vlans:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------

# parsed:
#   - vlan_id: 5
#     enabled: True
#     mode: "ce"
#     name: "vlan5"
#     state: suspend
#
#   - vlan_id: 6
#     enabled: True
#     mode: "ce"
#     state: active
#
#   - vlan_id: 7
#     enabled: True
#     mode: "ce"
#     name: "vlan7"
#     state: active
#     mapped_vni: 100

# Using gathered

# Existing device config state
# -------------------------------
# nxos-9k# show vlan | json
# {"TABLE_vlanbrief": {"ROW_vlanbrief": [{"vlanshowbr-vlanid": "1", "vlanshowbr-vlanid-utf": "1", "vlanshowbr-vlanname": "default", "vlanshowbr-vlanstate
# ": "active", "vlanshowbr-shutstate": "noshutdown"}, {"vlanshowbr-vlanid": "5", "vlanshowbr-vlanid-utf": "5", "vlanshowbr-vlanname": "vlan5", "vlanshowb
# r-vlanstate": "suspend", "vlanshowbr-shutstate": "noshutdown"}, {"vlanshowbr-vlanid": "6", "vlanshowbr-vlanid-utf": "6", "vlanshowbr-vlanname": "VLAN00
# 06", "vlanshowbr-vlanstate": "active", "vlanshowbr-shutstate": "noshutdown"}, {"vlanshowbr-vlanid": "7", "vlanshowbr-vlanid-utf": "7", "vlanshowbr-vlan
# name": "vlan7", "vlanshowbr-vlanstate": "active", "vlanshowbr-shutstate": "shutdown"}]}, "TABLE_mtuinfo": {"ROW_mtuinfo": [{"vlanshowinfo-vlanid": "1",
# "vlanshowinfo-media-type": "enet", "vlanshowinfo-vlanmode": "ce-vlan"}, {"vlanshowinfo-vlanid": "5", "vlanshowinfo-media-type": "enet", "vlanshowinfo-
# vlanmode": "ce-vlan"}, {"vlanshowinfo-vlanid": "6", "vlanshowinfo-media-type": "enet", "vlanshowinfo-vlanmode": "ce-vlan"}, {"vlanshowinfo-vlanid": "7"
# , "vlanshowinfo-media-type": "enet", "vlanshowinfo-vlanmode": "ce-vlan"}]}}
#
# nxos-9k#  show running-config | section ^vlan
# vlan 1,5-7
# vlan 5
#   state suspend
#   name vlan5
# vlan 7
#   shutdown
#   name vlan7
#   vn-segment 190

- name: Gather vlans facts from the device using nxos_vlans
  cisco.nxos.nxos_vlans:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
#   - vlan_id: 5
#     enabled: True
#     mode: "ce"
#     name: "vlan5"
#     state: suspend
#
#   - vlan_id: 6
#     enabled: True
#     mode: "ce"
#     state: active
#
#   - vlan_id: 7
#     enabled: False
#     mode: "ce"
#     name: "vlan7"
#     state: active
#     mapped_vni: 190
```

## [Return Values](nxos_vlans_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["vlan 5", "name test-vlan5", "state suspend"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
