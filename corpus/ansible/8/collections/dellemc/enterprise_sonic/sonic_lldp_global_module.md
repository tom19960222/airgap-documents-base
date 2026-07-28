---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_lldp_global module – Manage Global LLDP configurations on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_lldp_global_module.html
fetched_at: 2026-07-28T02:03:42+00:00
---
# dellemc.enterprise_sonic.sonic_lldp_global module – Manage Global LLDP configurations on SONiC

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_lldp_global`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_lldp_global_module.md#synopsis)
- [Parameters](sonic_lldp_global_module.md#parameters)
- [Examples](sonic_lldp_global_module.md#examples)
- [Return Values](sonic_lldp_global_module.md#return-values)

## [Synopsis](sonic_lldp_global_module.md#id1)

- This module provides configuration management of global LLDP parameters for use on LLDP enabled Layer 2 interfaces of devices running SONiC.
- It is intended for use in conjunction with LLDP Layer 2 interface configuration applied on participating interfaces.

## [Parameters](sonic_lldp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The set of link layer discovery protocol global attribute configurations |
| **enable**  boolean | This argument is a boolean value to enable or disable LLDP.  **Choices:**   - `false` - `true` |
| **hello_time**  integer | Frequency at which LLDP advertisements are sent (in seconds).  The range is from 5 to 254 sec |
| **mode**  string | By default both transmit and receive of LLDP frames is enabled.  This command can be used to configure either in receive only or transmit only mode.  **Choices:**   - `"receive"` - `"transmit"` |
| **multiplier**  integer | Multiplier value is used to determine the timeout interval (i.e. hello-time x multiplier value)  The range is from 1 to 10 |
| **system_description**  string | Description of this system to be sent in LLDP advertisements.  When configured, this value is used in the advertisements instead of the default system description. |
| **system_name**  string | Specifying a descriptive system name using this command, user may find it easier to distinguish the device with LLDP.  By default, the host name is used. |
| **tlv_select**  dictionary | By default, management address and system capabilities TLV are advertised in LLDP frames.  This configuration option can be used to selectively suppress sending of these TLVs to the Peer. |
| **management_address**  boolean | Enable or disable management address TLV.  **Choices:**   - `false` - `true` |
| **system_capabilities**  boolean | Enable or disable system capabilities TLV.  **Choices:**   - `false` - `true` |
| **state**  string | The state specifies the type of configuration update to be performed on the device.  If the state is “merged”, merge specified attributes with existing configured attributes.  For “deleted”, delete the specified attributes from existing configuration.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |

## [Examples](sonic_lldp_global_module.md#id3)

```yaml+jinja
# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration
# !
# lldp receive
# lldp timer 200
# lldp multiplier 1
# lldp system-name 8999_System
# lldp system-description sonic_system
# !

  - name: Delete LLDP configurations
    dellemc.enterprise_sonic.sonic_lldp_global:
      config:
        hello_time: 200
        system_description : sonic_system
        mode: receive
        multiplier: 1
      state: deleted

# After State:
# ------------
# sonic# show running-configuration | grep lldp
# !
# lldp system-name 8999_System
# !
# sonic#

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep lldp
# sonic#

  - name: Delete default LLDP configurations
    dellemc.enterprise_sonic.sonic_lldp_global:
      config:
        tlv_select:
          system_capabilities: true
      state: deleted

# After State:
# ------------
# sonic# show running-configuration
# !
# no lldp tlv-select system-capabilities
# !

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep lldp
# !
# lldp receive
# lldp timer 200
# lldp multiplier 1
# lldp system-name 8999_System
# lldp system-description sonic_system
# !

  - name: Delete all LLDP configuration
    dellemc.enterprise_sonic.sonic_lldp_global:
      config:
      state: deleted

# After State:  (No LLDP global configuration present.)
# ------------
# sonic# show running-configuration | grep lldp
# sonic#

# Using Merged
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep lldp
# sonic#

  - name: Modify LLDP configurations
    dellemc.enterprise_sonic.sonic_lldp_global:
      config:
        enable: false
        multiplier: 9
        system_name : CR_sonic
        hello_time: 18
        mode: receive
        system_description: Sonic_System
        tlv_select:
          management_address: true
          system_capabilities: false
      state: merged

# After State:
# ------------
# sonic# show running-configuration | grep lldp
# !
# no lldp enable
# no lldp tlv-select system_capabilities
# lldp receive
# lldp timer 18
# lldp multiplier 9
# lldp system-name CR_sonic
# lldp system-description Sonic_System
# !

# Using Merged
#
# Before State:
# -------------
#
# sonic# show running-configuration | grep lldp
# !
# lldp receive
# lldp timer 200
# lldp multiplier 1
# lldp system-name 8999_System
# lldp system-description sonic_system
# !

  - name: Modify LLDP configurations
    dellemc.enterprise_sonic.sonic_lldp_global:
      config:
         multiplier: 9
         system_name : CR_sonic
      state: merged

# After State:
# ------------
# sonic# show running-configuration | grep lldp
# !
# lldp receive
# lldp timer 200
# lldp multiplier 9
# lldp system-name CR_sonic
# lldp system-description sonic_system
# !
```

## [Return Values](sonic_lldp_global_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Divya Balasubramanian(@divya-balasubramania)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
