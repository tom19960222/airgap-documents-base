---
collection: ansible
version: "8"
title: "cisco.ios.ios_lldp_global module – Resource module to configure LLDP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_lldp_global_module.html
fetched_at: 2026-07-28T01:26:16+00:00
---
# cisco.ios.ios_lldp_global module – Resource module to configure LLDP.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_lldp_global`.

New in cisco.ios 1.0.0

- [Synopsis](ios_lldp_global_module.md#synopsis)
- [Parameters](ios_lldp_global_module.md#parameters)
- [Notes](ios_lldp_global_module.md#notes)
- [Examples](ios_lldp_global_module.md#examples)
- [Return Values](ios_lldp_global_module.md#return-values)

## [Synopsis](ios_lldp_global_module.md#id1)

- This module configures and manages the Link Layer Discovery Protocol(LLDP) attributes on IOS platforms.

Aliases: lldp_global

## [Parameters](ios_lldp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of LLDP options |
| **enabled**  boolean | Enable LLDP  **Choices:**   - `false` - `true` |
| **holdtime**  integer | LLDP holdtime (in sec) to be sent in packets.  Refer to vendor documentation for valid values. |
| **reinit**  integer | Specify the delay (in secs) for LLDP to initialize.  Refer to vendor documentation for valid values.  NOTE, if LLDP reinit is configured with a starting value, idempotency won’t be maintained as the Cisco device doesn’t record the starting reinit configured value. As such, Ansible cannot verify if the respective starting reinit value is already configured or not from the device side. If you try to apply starting reinit value in every play run, Ansible will show changed as True. For any other reinit value, idempotency will be maintained since any other reinit value is recorded in the Cisco device. |
| **timer**  integer | Specify the rate at which LLDP packets are sent (in sec).  Refer to vendor documentation for valid values. |
| **tlv_select**  dictionary | Selection of LLDP TLVs i.e. type-length-value to send  NOTE, if tlv-select is configured idempotency won’t be maintained as Cisco device doesn’t record configured tlv-select options. As such, Ansible cannot verify if the respective tlv-select options is already configured or not from the device side. If you try to apply tlv-select option in every play run, Ansible will show changed as True. |
| **four_wire_power_management**  boolean | Cisco 4-wire Power via MDI TLV  **Choices:**   - `false` - `true` |
| **mac_phy_cfg**  boolean | IEEE 802.3 MAC/Phy Configuration/status TLV  **Choices:**   - `false` - `true` |
| **management_address**  boolean | Management Address TLV  **Choices:**   - `false` - `true` |
| **port_description**  boolean | Port Description TLV  **Choices:**   - `false` - `true` |
| **port_vlan**  boolean | Port VLAN ID TLV  **Choices:**   - `false` - `true` |
| **power_management**  boolean | IEEE 802.3 DTE Power via MDI TLV  **Choices:**   - `false` - `true` |
| **system_capabilities**  boolean | System Capabilities TLV  **Choices:**   - `false` - `true` |
| **system_description**  boolean | System Description TLV  **Choices:**   - `false` - `true` |
| **system_name**  boolean | System Name TLV  **Choices:**   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | section ^lldp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](ios_lldp_global_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_lldp_global_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# vios#sh running-config | section ^lldp
# vios1#

- name: Merge provided configuration with device configuration
  cisco.ios.ios_lldp_global:
    config:
      holdtime: 10
      enabled: true
      reinit: 3
      timer: 10
    state: merged

# After state:
# ------------
# vios#sh running-config | section ^lldp
#  lldp timer 10
#  lldp holdtime 10
#  lldp reinit 3
#  lldp run

# Using replaced

# Before state:
# -------------
# vios#sh running-config | section ^lldp
#  lldp timer 10
#  lldp holdtime 10
#  lldp reinit 3
#  lldp run

- name: Replaces LLDP device configuration with provided configuration
  cisco.ios.ios_lldp_global:
    config:
      holdtime: 20
      reinit: 5
    state: replaced

# After state:
# -------------
# vios#sh running-config | section ^lldp
#  lldp holdtime 20
#  lldp reinit 5

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured LLDP module attributes)"

# Before state:
# -------------
# vios#sh running-config | section ^lldp
#  lldp timer 10
#  lldp holdtime 10
#  lldp reinit 3
#  lldp run

- name: Delete LLDP attributes
  cisco.ios.ios_lldp_global:
    state: deleted

# After state:
# -------------
# vios#sh running-config | section ^lldp
# vios1#

# Using Gathered

# Before state:
# -------------
#
# vios#sh running-config | section ^lldp
#  lldp timer 10
#  lldp holdtime 10
#  lldp reinit 3
#  lldp run

- name: Gather listed interfaces with provided configurations
  cisco.ios.ios_lldp_global:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": {
#         "enabled": true,
#         "holdtime": 10,
#         "reinit": 3,
#         "timer": 10
#     }

# After state:
# ------------
#
# vios#sh running-config | section ^lldp
#  lldp timer 10
#  lldp holdtime 10
#  lldp reinit 3
#  lldp run

# Using Rendered
- name: Render the commands for provided  configuration
  cisco.ios.ios_lldp_global:
    config:
      holdtime: 10
      enabled: true
      reinit: 3
      timer: 10
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "lldp holdtime 10",
#         "lldp run",
#         "lldp timer 10",
#         "lldp reinit 3"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# lldp timer 10
# lldp holdtime 10
# lldp reinit 3
# lldp run

- name: Parse the commands for provided configuration
  cisco.ios.ios_lldp_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": {
#         "enabled": true,
#         "holdtime": 10,
#         "reinit": 3,
#         "timer": 10
#     }
```

## [Return Values](ios_lldp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format of the parameters above."` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format of the parameters above."` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  **Returned:** always  **Sample:** `["lldp holdtime 10", "lldp run", "lldp timer 10"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
