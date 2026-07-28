---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_lldp_global module – Resource module to configure LLDP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_lldp_global_module.html
fetched_at: 2026-07-28T01:26:48+00:00
---
# cisco.iosxr.iosxr_lldp_global module – Resource module to configure LLDP.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_lldp_global`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_lldp_global_module.md#synopsis)
- [Parameters](iosxr_lldp_global_module.md#parameters)
- [Notes](iosxr_lldp_global_module.md#notes)
- [Examples](iosxr_lldp_global_module.md#examples)
- [Return Values](iosxr_lldp_global_module.md#return-values)

## [Synopsis](iosxr_lldp_global_module.md#id1)

- This module manages Global Link Layer Discovery Protocol (LLDP) settings on IOS-XR devices.

Aliases: lldp_global

## [Parameters](iosxr_lldp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The provided global LLDP configuration. |
| **holdtime**  integer | Specifies the holdtime (in sec) to be sent in packets. |
| **reinit**  integer | Specifies the delay (in sec) for LLDP initialization on any interface. |
| **subinterfaces**  boolean | Enable or disable LLDP over sub-interfaces.  **Choices:**   - `false` - `true` |
| **timer**  integer | Specifies the rate at which LLDP packets are sent (in sec). |
| **tlv_select**  dictionary | Specifies the LLDP TLVs to enable or disable. |
| **management_address**  boolean | Enable or disable management address TLV.  **Choices:**   - `false` - `true` |
| **port_description**  boolean | Enable or disable port description TLV.  **Choices:**   - `false` - `true` |
| **system_capabilities**  boolean | Enable or disable system capabilities TLV.  **Choices:**   - `false` - `true` |
| **system_description**  boolean | Enable or disable system description TLV.  **Choices:**   - `false` - `true` |
| **system_name**  boolean | Enable or disable system name TLV.  **Choices:**   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config lldp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](iosxr_lldp_global_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_lldp_global_module.md#id4)

```yaml+jinja
# Using merged
#
#
# -------------
# Before State
# -------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run lldp
# Tue Aug  6 19:27:54.933 UTC
# % No such configuration item(s)
#
#

- name: Merge provided LLDP configuration with the existing configuration
  cisco.iosxr.iosxr_lldp_global:
    config:
      holdtime: 100
      reinit: 2
      timer: 3000
      subinterfaces: true
      tlv_select:
        management_address: false
        system_description: false
    state: merged

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {}
#
#  "commands": [
#        "lldp subinterfaces enable",
#        "lldp holdtime 100",
#        "lldp reinit 2",
#        "lldp tlv-select system-description disable",
#        "lldp tlv-select management-address disable",
#        "lldp timer 3000"
#  ]
#
#  "after": {
#        "holdtime": 100,
#        "reinit": 2,
#        "subinterfaces": true,
#        "timer": 3000,
#        "tlv_select": {
#            "management_address": false,
#            "system_description": false
#        }
#  }
#
#
# ------------
# After state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run lldp
# Tue Aug  6 21:31:10.587 UTC
# lldp
#  timer 3000
#  reinit 2
#  subinterfaces enable
#  holdtime 100
#  tlv-select
#   management-address disable
#   system-description disable
#  !
# !
#
#

# Using replaced
#
#
# -------------
# Before State
# -------------
#
# RP/0/0/CPU0:an-iosxr#sh run lldp
# Tue Aug  6 21:31:10.587 UTC
# lldp
#  timer 3000
#  reinit 2
#  subinterfaces enable
#  holdtime 100
#  tlv-select
#   management-address disable
#   system-description disable
#  !
# !
#
#

- name: Replace existing LLDP device configuration with provided configuration
  cisco.iosxr.iosxr_lldp_global:
    config:
      holdtime: 100
      tlv_select:
        port_description: false
        system_description: true
        management_description: true
    state: replaced

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {
#        "holdtime": 100,
#        "reinit": 2,
#        "subinterfaces": true,
#        "timer": 3000,
#        "tlv_select": {
#            "management_address": false,
#            "system_description": false
#        }
#  }
#
#  "commands": [
#        "no lldp reinit 2",
#        "no lldp subinterfaces enable",
#        "no lldp timer 3000",
#        "no lldp tlv-select management-address disable",
#        "no lldp tlv-select system-description disable",
#        "lldp tlv-select port-description disable"
#  ]
#
#  "after": {
#        "holdtime": 100,
#        "tlv_select": {
#            "port_description": false
#        }
#  }
#
#
# ------------
# After state
# ------------
#
# RP/0/0/CPU0:an-iosxr#sh run lldp
# Tue Aug  6 21:53:08.407 UTC
# lldp
#  holdtime 100
#  tlv-select
#   port-description disable
#  !
# !
#
#

# Using deleted
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:an-iosxr#sh run lldp
# Tue Aug  6 21:31:10.587 UTC
# lldp
#  timer 3000
#  reinit 2
#  subinterfaces enable
#  holdtime 100
#  tlv-select
#   management-address disable
#   system-description disable
#  !
# !
#
#

- name: Deleted existing LLDP configurations from the device
  cisco.iosxr.iosxr_lldp_global:
    state: deleted

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {
#        "holdtime": 100,
#        "reinit": 2,
#        "subinterfaces": true,
#        "timer": 3000,
#        "tlv_select": {
#            "management_address": false,
#            "system_description": false
#        }
#  },
#
#  "commands": [
#        "no lldp holdtime 100",
#        "no lldp reinit 2",
#        "no lldp subinterfaces enable",
#        "no lldp timer 3000",
#        "no lldp tlv-select management-address disable",
#        "no lldp tlv-select system-description disable"
#  ]
#
#  "after": {}
#
#
# -----------
# After state
# -----------
#
# RP/0/0/CPU0:an-iosxr#sh run lldp
# Tue Aug  6 21:38:31.187 UTC
# lldp
# !
#
# Using parsed:

# parsed.cfg
# lldp
#  timer 3000
#  reinit 2
#  subinterfaces enable
#  holdtime 100
#  tlv-select
#   management-address disable
#   system-description disable
#  !
# !

- name: Convert lldp global config to argspec without connecting to the appliance
  cisco.iosxr.iosxr_lldp_global:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# ------------------------
# Module Execution Result
# ------------------------
# parsed:
#     holdtime: 100
#     reinit: 2
#     timer: 3000
#     subinterfaces: True
#     tlv_select:
#       management_address: False
#       system_description: False

# using gathered:

# Device config:
# lldp
#  timer 3000
#  reinit 2
#  subinterfaces enable
#  holdtime 100
#  tlv-select
#   management-address disable
#   system-description disable
#  !
# !

- name: Gather IOSXR lldp global configuration
  cisco.iosxr.iosxr_lldp_global:
    config:
    state: gathered

# ------------------------
# Module Execution Result
# ------------------------
# gathered:
#     holdtime: 100
#     reinit: 2
#     timer: 3000
#     subinterfaces: True
#     tlv_select:
#       management_address: False
#       system_description: False

# using rendered:

- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_lldp_global:
    config:
      holdtime: 100
      reinit: 2
      timer: 3000
      subinterfaces: true
      tlv_select:
        management_address: false
        system_description: false
    state: rendered

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "rendered": [
#        "lldp subinterfaces enable",
#        "lldp holdtime 100",
#        "lldp reinit 2",
#        "lldp tlv-select system-description disable",
#        "lldp tlv-select management-address disable",
#        "lldp timer 3000"
#  ]
```

## [Return Values](iosxr_lldp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["lldp subinterfaces enable", "lldp holdtime 100", "no lldp tlv-select management-address disable"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
