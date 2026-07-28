---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_system module – Configure system parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_system_module.html
fetched_at: 2026-07-28T02:03:50+00:00
---
# dellemc.enterprise_sonic.sonic_system module – Configure system parameters

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_system`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_system_module.md#synopsis)
- [Parameters](sonic_system_module.md#parameters)
- [Notes](sonic_system_module.md#notes)
- [Examples](sonic_system_module.md#examples)
- [Return Values](sonic_system_module.md#return-values)

## [Synopsis](sonic_system_module.md#id1)

- This module is used for configuration management of global system parameters on devices running Enterprise SONiC.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_system_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies the system related configurations |
| **anycast_address**  dictionary | Specifies different types of anycast address that can be configured on the device |
| **ipv4**  boolean | Enable or disable ipv4 anycast-address  **Choices:**   - `false` - `true` |
| **ipv6**  boolean | Enable or disable ipv6 anycast-address  **Choices:**   - `false` - `true` |
| **mac_address**  string | Specifies the mac anycast-address |
| **hostname**  string | Specifies the hostname of the SONiC device |
| **interface_naming**  string | Specifies the type of interface-naming in device  **Choices:**   - `"standard"` - `"native"` |
| **state**  string | Specifies the operation to be performed on the system parameters configured on the device.  In case of merged, the input configuration will be merged with the existing system configuration on the device.  In case of deleted the existing system configuration will be removed from the device.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Notes](sonic_system_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_system_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#!
#SONIC(config)#do show running-configuration
#!
#ip anycast-mac-address aa:bb:cc:dd:ee:ff
#ip anycast-address enable
#ipv6 anycast-address enable
#interface-naming standard

- name: Merge provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_system:
    config:
      hostname: SONIC
      interface_naming: standard
      anycast_address:
        ipv6: true
    state: deleted

# After state:
# ------------
#!
#sonic(config)#do show running-configuration
#!
#ip anycast-mac-address aa:bb:cc:dd:ee:ff
#ip anycast-address enable

# Using deleted
#
# Before state:
# -------------
#!
#SONIC(config)#do show running-configuration
#!
#ip anycast-mac-address aa:bb:cc:dd:ee:ff
#ip anycast-address enable
#ipv6 anycast-address enable
#interface-naming standard

- name: Delete all system related configs in device configuration
  dellemc.enterprise_sonic.sonic_system:
    config:
    state: deleted

# After state:
# ------------
#!
#sonic(config)#do show running-configuration
#!

# Using merged
#
# Before state:
# -------------
#!
#sonic(config)#do show running-configuration
#!

- name: Merge provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_system:
    config:
      hostname: SONIC
      interface_naming: standard
      anycast_address:
        ipv6: true
        ipv4: true
        mac_address: aa:bb:cc:dd:ee:ff
    state: merged

# After state:
# ------------
#!
#SONIC(config)#do show running-configuration
#!
#ip anycast-mac-address aa:bb:cc:dd:ee:ff
#ip anycast-address enable
#ipv6 anycast-address enable
#interface-naming standard

# Using replaced
#
# Before state:
# -------------
#!
#sonic(config)#do show running-configuration
#!
#ip anycast-mac-address aa:bb:cc:dd:ee:ff
#ip anycast-address enable
#ipv6 anycast-address enable

- name: Replace system configuration.
  sonic_system:
    config:
      hostname: sonic
      interface_naming: standard
    state: replaced

# After state:
# ------------
#!
#SONIC(config)#do show running-configuration
#!
#interface-naming standard

# Using replaced
#
# Before state:
# -------------
#!
#sonic(config)#do show running-configuration
#!
#ip anycast-mac-address aa:bb:cc:dd:ee:ff
#interface-naming standard

- name: Replace system device configuration.
  sonic_system:
    config:
      hostname: sonic
      interface_naming: standard
      anycast_address:
        ipv6: true
        ipv4: true
    state: replaced

# After state:
# ------------
#!
#SONIC(config)#do show running-configuration
#!
#ip anycast-address enable
#ipv6 anycast-address enable
#interface-naming standard

# Using overridden
#
# Before state:
# -------------
#!
#sonic(config)#do show running-configuration
#!
#ip anycast-mac-address aa:bb:cc:dd:ee:ff
#ip anycast-address enable
#ipv6 anycast-address enable

- name: Override system configuration.
  sonic_system:
    config:
      hostname: sonic
      interface_naming: standard
      anycast_address:
        ipv4: true
        mac_address: bb:aa:cc:dd:ee:ff
    state: overridden

# After state:
# ------------
#!
#SONIC(config)#do show running-configuration
#!
#ip anycast-mac-address bb:aa:cc:dd:ee:ff
#ip anycast-address enable
#interface-naming standard
```

## [Return Values](sonic_system_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
