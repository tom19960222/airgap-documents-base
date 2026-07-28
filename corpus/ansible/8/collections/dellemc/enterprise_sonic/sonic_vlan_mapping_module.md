---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_vlan_mapping module – Configure vlan mappings on SONiC."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_vlan_mapping_module.html
fetched_at: 2026-07-28T02:03:52+00:00
---
# dellemc.enterprise_sonic.sonic_vlan_mapping module – Configure vlan mappings on SONiC.

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_vlan_mapping`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_vlan_mapping_module.md#synopsis)
- [Parameters](sonic_vlan_mapping_module.md#parameters)
- [Examples](sonic_vlan_mapping_module.md#examples)
- [Return Values](sonic_vlan_mapping_module.md#return-values)

## [Synopsis](sonic_vlan_mapping_module.md#id1)

- This module provides configuration management for vlan mappings on devices running SONiC.
- Vlan mappings only available on TD3 and TD4 devices.
- For TD4 devices must enable vlan mapping first (can enable in config-switch-resource).

## [Parameters](sonic_vlan_mapping_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the vlan mapping related configurations. |
| **mapping**  list / elements=dictionary | Defining a single vlan mapping. |
| **dot1q_tunnel**  boolean | Specify whether it is a vlan stacking or translation (false means translation; true means stacking).  **Choices:**   - `false` ← (default) - `true` |
| **inner_vlan**  integer | Configure inner customer VLAN ID.  VLAN IDs range is 1-4094.  Only available for double tagged translations. |
| **priority**  integer | Set priority level of the vlan mapping.  Priority range is 0-7. |
| **service_vlan**  integer / required | Configure service provider VLAN ID.  VLAN ID range is 1-4094. |
| **vlan_ids**  list / elements=string | Configure customer VLAN IDs.  If mode is double tagged translation then this VLAN ID represents the outer VLAN ID.  If mode is set to stacking can pass ranges and/or multiple list entries.  Individual VLAN ID or (-) separated range of VLAN IDs. |
| **name**  string / required | Full name of the interface, i.e. Ethernet8, PortChannel2, Eth1/2. |
| **state**  string | Specifies the operation to be performed on the vlan mappings configured on the device.  In case of merged, the input configuration will be merged with the existing vlan mappings on the device.  In case of deleted, the existing vlan mapping configuration will be removed from the device.  In case of overridden, all existing vlan mappings will be deleted and the specified input configuration will be add.  In case of replaced, the existing vlan mappings on the device will be replaced by the configuration for each vlan mapping.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Examples](sonic_vlan_mapping_module.md#id3)

```yaml+jinja
# Using deleted
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-432 dot1q-tunnel 2436 priority 3
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!

  - name: Delete vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
          mapping:
            - service_vlan: 2755
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
              priority: 3
            - service_vlan: 2436
              vlan_ids:
                - 404
                - 401
                - 412
                - 430-431
              priority: 3
      state: deleted

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400,402,406,408,410,420,422,432 dot1q-tunnel 2436
# switchport vlan-mapping 300 dot1q-tunnel 2567
#!

# Using deleted
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!

  - name: Delete vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
      state: deleted

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdo#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,406,408,410,420,422,431 dot1q-tunnel 2436
#!

# Using merged
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
#!
#interface PortChannel 2
# switchport vlan-mapping 345 2999 priority 0
# switchport vlan-mapping 500,540 dot1q-tunnel 3000
# no shutdown
#!

  - name: Add vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
          mapping:
            - service_vlan: 2755
              vlan_ids:
                - 392
              dot1q_tunnel: false
              inner_vlan: 590
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
              vlan_ids:
                - 300
              dot1q_tunnel: true
              priority: 3
            - service_vlan: 2436
              vlan_ids:
                - 400-402
                - 404
                - 406
                - 408
                - 410
                - 412
                - 420
                - 422
                - 430-431
              dot1q_tunnel: true
        - name: Portchannel 2
          mapping:
            - service_vlan: 2999
              priority: 4
            - service_vlan: 3000
              vlan_ids:
                - 506-512
                - 561
              priority: 5
      state: merged

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!
#interface PortChannel 2
# switchport vlan-mapping 345 2999 priority 4
# switchport vlan-mapping 500,506-512,540,561 dot1q-tunnel 3000 priority 5
# no shutdown
#!

# Using replaced
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!
#interface PortChannel 2
# switchport vlan-mapping 345 2999 priority 0
# no shutdown
#!

  - name: Replace vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
          mapping:
            - service_vlan: 2755
              vlan_ids:
                - 390
              dot1q_tunnel: false
              inner_vlan: 593
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
              vlan_ids:
                - 310
                - 330-340
              priority: 5
        - name: Portchannel 2
          mapping:
            - service_vlan: 2999
              vlan_ids:
                - 345
              dot1q_tunnel: true
              priority: 1
      state: replaced

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
# switchport vlan-mapping 390 inner 593 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
# switchport vlan-mapping 310,330-340 dot1q-tunnel 2567 priority 5
#!
#interface PortChannel 2
# switchport vlan-mapping 345 dot1q_tunnel 2999 priority 1
# no shutdown
#!

# Using overridden
#
# Before State:
# -------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 623 2411
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 400-402,404,406,408,410,412,420,422,430-431 dot1q-tunnel 2436
#!

  - name: Override the vlan mapping configurations
    sonic_vlan_mapping:
      config:
        - name: Ethernet8
          mapping:
            - service_vlan: 2755
              vlan_ids:
                - 392
              dot1q_tunnel: false
              inner_vlan: 590
        - name: Ethernet16
          mapping:
            - service_vlan: 2567
              vlan_ids:
                - 300
              dot1q_tunnel: true
              priority: 3
        - name: Portchannel 2
          mapping:
            - service_vlan: 2999
              vlan_ids:
                - 345
              priority: 0
      state: overridden

# After State:
# ------------
#
#sonic# show running-configuration interface
#!
#interface Ethernet8
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 392 inner 590 2755
#!
#interface Ethernet16
# mtu 9100
# speed 400000
# fec RS
# unreliable-los auto
# shutdown
# switchport vlan-mapping 300 dot1q-tunnel 2567 priority 3
#!
#interface PortChannel 2
# switchport vlan-mapping 345 2999 priority 0
# no shutdown
#!
```

## [Return Values](sonic_vlan_mapping_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Cypher Miller (@Cypher-Miller)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
