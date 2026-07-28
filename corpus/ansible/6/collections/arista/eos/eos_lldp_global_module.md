---
collection: ansible
version: "6"
title: "arista.eos.eos_lldp_global module – LLDP resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_lldp_global_module.html
fetched_at: 2026-07-27T16:45:13+00:00
---
# arista.eos.eos_lldp_global module – LLDP resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_lldp_global`.

New in arista.eos 1.0.0

- [Synopsis](eos_lldp_global_module.md#synopsis)
- [Parameters](eos_lldp_global_module.md#parameters)
- [Notes](eos_lldp_global_module.md#notes)
- [Examples](eos_lldp_global_module.md#examples)
- [Return Values](eos_lldp_global_module.md#return-values)

## [Synopsis](eos_lldp_global_module.md#id1)

- This module manages Global Link Layer Discovery Protocol (LLDP) settings on Arista EOS devices.

## [Parameters](eos_lldp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The provided global LLDP configuration. |
| **holdtime**  integer | Specifies the holdtime (in sec) to be sent in packets. |
| **reinit**  integer | Specifies the delay (in sec) for LLDP initialization on any interface. |
| **timer**  integer | Specifies the rate at which LLDP packets are sent (in sec). |
| **tlv_select**  dictionary | Specifies the LLDP TLVs to enable or disable. |
| **link_aggregation**  boolean | Enable or disable link aggregation TLV.  Choices:   - `false` - `true` |
| **management_address**  boolean | Enable or disable management address TLV.  Choices:   - `false` - `true` |
| **max_frame_size**  boolean | Enable or disable maximum frame size TLV.  Choices:   - `false` - `true` |
| **port_description**  boolean | Enable or disable port description TLV.  Choices:   - `false` - `true` |
| **system_capabilities**  boolean | Enable or disable system capabilities TLV.  Choices:   - `false` - `true` |
| **system_description**  boolean | Enable or disable system description TLV.  Choices:   - `false` - `true` |
| **system_name**  boolean | Enable or disable system name TLV.  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section lldp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](eos_lldp_global_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_lldp_global_module.md#id4)

```yaml+jinja
# Using merged
#
# ------------
# Before State
# ------------
#
# veos# show run | section lldp
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Merge provided LLDP configuration with the existing configuration
  arista.eos.eos_lldp_global:
    config:
      holdtime: 100
      tlv_select:
        management_address: false
        port_description: false
        system_description: true
    state: merged

# -----------
# After state
# -----------
#
# veos# show run | section lldp
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select port-description

# Using replaced
#
# ------------
# Before State
# ------------
#
# veos# show run | section lldp
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Replace existing LLDP device configuration with provided configuration
  arista.eos.eos_lldp_global:
    config:
      holdtime: 100
      tlv_select:
        management_address: false
        port_description: false
        system_description: true
    state: replaced

# -----------
# After state
# -----------
#
# veos# show run | section lldp
# lldp holdtime 100
# no lldp tlv-select management-address
# no lldp tlv-select port-description

# Using deleted
#
# ------------
# Before State
# ------------
#
# veos# show run | section lldp
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Delete existing LLDP configurations from the device
  arista.eos.eos_lldp_global:
    state: deleted

# -----------
# After state
# -----------
#
# veos# show run | section ^lldp

# Using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_lldp_global:
    config:
      holdtime: 100
      tlv_select:
        management_address: false
        port_description: false
        system_description: true
    state: rendered

# -----------
# Output
# -----------
#
# rendered:
#   - "lldp holdtime 100"
#   - "no lldp tlv-select management-address"
#   - "no lldp tlv-select port-description"

# Using parsed

# parsed.cfg

# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Use parsed to convert native configs to structured data
  arista.eos.lldp_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# -----------
# Output
# -----------

#    parsed:
#      holdtime: 100
#      timer 3000
#      reinit 5
#      tlv_select:
#        management_address: False
#        port_description: False
#        system_description: True

# Using gathered:
# native config:
# lldp timer 3000
# lldp holdtime 100
# lldp reinit 5
# no lldp tlv-select management-address
# no lldp tlv-select system-description

- name: Gather lldp_global facts from the device
  arista.eos.lldp_global:
    state: gathered

# -----------
# Output
# -----------

#    gathered:
#      holdtime: 100
#      timer 3000
#      reinit 5
#      tlv_select:
#        management_address: False
#        port_description: False
#        system_description: True
```

## [Return Values](eos_lldp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["lldp holdtime 100", "no lldp timer", "lldp tlv-select system-description"]` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
