---
collection: ansible
version: "8"
title: "arista.eos.eos_vlans module – VLANs resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_vlans_module.html
fetched_at: 2026-07-28T01:11:18+00:00
---
# arista.eos.eos_vlans module – VLANs resource module

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
> To use it in a playbook, specify: `arista.eos.eos_vlans`.

New in arista.eos 1.0.0

- [Synopsis](eos_vlans_module.md#synopsis)
- [Parameters](eos_vlans_module.md#parameters)
- [Notes](eos_vlans_module.md#notes)
- [Examples](eos_vlans_module.md#examples)
- [Return Values](eos_vlans_module.md#return-values)

## [Synopsis](eos_vlans_module.md#id1)

- This module provides declarative management of VLANs on Arista EOS network devices.

Aliases: vlans

## [Parameters](eos_vlans_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of VLANs options |
| **name**  string | Name of the VLAN. |
| **state**  string | Operational state of the VLAN  **Choices:**   - `"active"` - `"suspend"` |
| **vlan_id**  integer / required | ID of the VLAN. Range 1-4094 |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section vlan**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](eos_vlans_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_vlans_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# veos(config-vlan-20)#show running-config | section vlan
# vlan 10
#    name ten
# !
# vlan 20
#    name twenty

- name: Delete attributes of the given VLANs.
  arista.eos.eos_vlans:
    config:
      - vlan_id: 20
    state: deleted

# After state:
# ------------
#
# veos(config-vlan-20)#show running-config | section vlan
# vlan 10
#    name ten

# Using merged

# Before state:
# -------------
#
# veos(config-vlan-20)#show running-config | section vlan
# vlan 10
#    name ten
# !
# vlan 20
#    name twenty

- name: Merge given VLAN attributes with device configuration
  arista.eos.eos_vlans:
    config:
      - vlan_id: 20
        state: suspend
    state: merged

# After state:
# ------------
#
# veos(config-vlan-20)#show running-config | section vlan
# vlan 10
#    name ten
# !
# vlan 20
#    name twenty
#    state suspend

# Using overridden

# Before state:
# -------------
#
# veos(config-vlan-20)#show running-config | section vlan
# vlan 10
#    name ten
# !
# vlan 20
#    name twenty

- name: Override device configuration of all VLANs with provided configuration
  arista.eos.eos_vlans:
    config:
      - vlan_id: 20
        state: suspend
    state: overridden

# After state:
# ------------
#
# veos(config-vlan-20)#show running-config | section vlan
# vlan 20
#    state suspend

# Using replaced

# Before state:
# -------------
#
# veos(config-vlan-20)#show running-config | section vlan
# vlan 10
#    name ten
# !
# vlan 20
#    name twenty

- name: Replace all attributes of specified VLANs with provided configuration
  arista.eos.eos_vlans:
    config:
      - vlan_id: 20
        state: suspend
    state: replaced

# After state:
# ------------
#
# veos(config-vlan-20)#show running-config | section vlan
# vlan 10
#    name ten
# !
# vlan 20
#    state suspend

# using parsed

# parsed.cfg
# vlan 10
#    name ten
# !
# vlan 20
#    name twenty
#    state suspend

- name: Use parsed to convert native configs to structured data
  arista.eos.eos_vlans:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Output:
# -------
#   parsed:
#     - vlan_id: 10
#       name: ten
#     - vlan_id: 20
#       state: suspend

# Using rendered:

- name: Use Rendered to convert the structured data to native config
  arista.eos.eos_vlans:
    config:
      - vlan_id: 10
        name: ten
      - vlan_id: 20
        state: suspend
    state: rendered

# Output:
# ------
# rendered:
#   - "vlan 10"
#   - "name ten"
#   - "vlan 20"
#   - "state suspend"

# Using gathered:
# native_config:
# vlan 10
#    name ten
# !
# vlan 20
#    name twenty
#    state suspend

- name: Gather vlans facts from the device
  arista.eos.eos_vlans:
    state: gathered

# Output:
# ------

# gathered:
#   - vlan_id: 10
#     name: ten
#   - vlan_id: 20
#     state: suspend
```

## [Return Values](eos_vlans_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["vlan 10", "no name", "vlan 11", "name Eleven"]` |

### Authors

- Nathaniel Case (@qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
