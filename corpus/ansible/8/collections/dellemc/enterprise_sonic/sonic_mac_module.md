---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_mac module – Manage MAC configuration on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_mac_module.html
fetched_at: 2026-07-28T02:03:43+00:00
---
# dellemc.enterprise_sonic.sonic_mac module – Manage MAC configuration on SONiC

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_mac`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_mac_module.md#synopsis)
- [Parameters](sonic_mac_module.md#parameters)
- [Examples](sonic_mac_module.md#examples)
- [Return Values](sonic_mac_module.md#return-values)

## [Synopsis](sonic_mac_module.md#id1)

- This module provides configuration management of MAC for devices running SONiC

## [Parameters](sonic_mac_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of MAC configurations. |
| **mac**  dictionary | Configuration attributes for MAC. |
| **aging_time**  integer | Time in seconds of inactivity before the MAC entry is timed out.  **Default:** `600` |
| **dampening_interval**  integer | Interval for which mac movements are observed before disabling MAC learning on a port.  **Default:** `5` |
| **dampening_threshold**  integer | Number of MAC movements allowed per second before disabling MAC learning on a port.  **Default:** `5` |
| **mac_table_entries**  list / elements=dictionary | Configuration attributes for MAC table entries. |
| **interface**  string | Specifies the interface for the MAC table entry. |
| **mac_address**  string / required | MAC address for the dynamic or static MAC table entry. |
| **vlan_id**  integer / required | ID number of VLAN on which the MAC address is present. |
| **vrf_name**  string | Specifies the VRF name.  **Default:** `"default"` |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Examples](sonic_mac_module.md#id3)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# sonic# show mac dampening
# MAC Move Dampening Threshold : 5
# MAC Move Dampening Interval  : 5
# sonic# show running-configuration | grep mac
# (No mac configuration pressent)

  - name: Merge MAC configurations
    input:
      - vrf_name: 'default'
        mac:
          aging_time: 50
          dampening_interval: 20
          dampening_threshold: 30
          mac_table_entries:
            - mac_address: '00:00:5e:00:53:af'
              vlan_id: 1
              interface: 'Ethernet20'
            - mac_address: '00:33:33:33:33:33'
              vlan_id: 2
              interface: 'Ethernet24'
            - mac_address: '00:00:4e:00:24:af'
              vlan_id: 3
              interface: 'Ethernet28'
    state: merged

# After state:
# ------------
#
# sonic# show mac dampening
# MAC Move Dampening Threshold : 30
# MAC Move Dampening Interval  : 20
# sonic# show running-configuration | grep mac
# mac address-table 00:00:5e:00:53:af Vlan1 Ethernet20
# mac address-table 00:33:33:33:33:33 Vlan2 Ethernet24
# mac address-table 00:00:4e:00:24:af Vlan3 Ethernet28
# mac address-table aging-time 50
#
#
# Using replaced
#
# Before state:
# -------------
#
# sonic# show mac dampening
# MAC Move Dampening Threshold : 30
# MAC Move Dampening Interval  : 20
# sonic# show running-configuration | grep mac
# mac address-table 00:00:5e:00:53:af Vlan1 Ethernet20
# mac address-table 00:33:33:33:33:33 Vlan2 Ethernet24
# mac address-table 00:00:4e:00:24:af Vlan3 Ethernet28
# mac address-table aging-time 50

  - name: Replace MAC configurations
    input:
      - vrf_name: 'default'
        mac:
          aging_time: 45
          dampening_interval: 30
          dampening_threshold: 60
          mac_table_entries:
            - mac_address: '00:00:5e:00:53:af'
              vlan_id: 3
              interface: 'Ethernet24'
            - mac_address: '00:44:44:44:44:44'
              vlan_id: 2
              interface: 'Ethernet20'
    state: replaced

# sonic# show mac dampening
# MAC Move Dampening Threshold : 60
# MAC Move Dampening Interval  : 30
# sonic# show running-configuration | grep mac
# mac address-table 00:00:5e:00:53:af Vlan3 Ethernet24
# mac address-table 00:33:33:33:33:33 Vlan2 Ethernet24
# mac address-table 00:00:4e:00:24:af Vlan3 Ethernet28
# mac address-table 00:44:44:44:44:44 Vlan2 Ethernet20
# mac address-table aging-time 45
#
#
# Using overridden
#
# Before state:
# -------------
#
# sonic# show mac dampening
# MAC Move Dampening Threshold : 60
# MAC Move Dampening Interval  : 30
# sonic# show running-configuration | grep mac
# mac address-table 00:00:5e:00:53:af Vlan3 Ethernet24
# mac address-table 00:33:33:33:33:33 Vlan2 Ethernet24
# mac address-table 00:00:4e:00:24:af Vlan3 Ethernet28
# mac address-table 00:44:44:44:44:44 Vlan2 Ethernet20
# mac address-table aging-time 45

  - name: Override MAC cofigurations
    input:
      - vrf_name: 'default'
        mac:
          aging_time: 10
          dampening_interval: 20
          dampening_threshold: 30
          mac_table_entries:
            - mac_address: '00:11:11:11:11:11'
              vlan_id: 1
              interface: 'Ethernet20'
            - mac_address: '00:22:22:22:22:22'
              vlan_id: 2
              interface: 'Ethernet24'
    state: overridden

# After state:
# ------------
#
# sonic# show mac dampening
# MAC Move Dampening Threshold : 30
# MAC Move Dampening Interval  : 20
# sonic# show running-configuration | grep mac
# mac address-table 00:11:11:11:11:11 Vlan1 Ethernet20
# mac address-table 00:22:22:22:22:22 Vlan2 Ethernet24
# mac address-table aging-time 10
#
#
# Using deleted
#
# Before state:
# -------------
#
# sonic# show mac dampening
# MAC Move Dampening Threshold : 30
# MAC Move Dampening Interval  : 20
# sonic# show running-configuration | grep mac
# mac address-table 00:11:11:11:11:11 Vlan1 Ethernet20
# mac address-table 00:22:22:22:22:22 Vlan2 Ethernet24
# mac address-table aging-time 10

  - name: Delete MAC cofigurations
    input:
      - vrf_name: 'default'
        mac:
          aging_time: 10
          dampening_interval: 20
          dampening_threshold: 30
          mac_table_entries:
            - mac_address: '00:11:11:11:11:11'
              vlan_id: 1
              interface: 'Ethernet20'
            - mac_address: '00:22:22:22:22:22'
              vlan_id: 2
              interface: 'Ethernet24'
    state: deleted

# After state:
# ------------
#
# sonic# show mac dampening
# MAC Move Dampening Threshold : 5
# MAC Move Dampening Interval  : 5
# sonic# show running-configuration | grep mac
# (No mac configuration pressent)
```

## [Return Values](sonic_mac_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Shade Talabi (@stalabi1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
