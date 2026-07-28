---
collection: ansible
version: "8"
title: "cisco.ios.ios_vlans module – Resource module to configure VLANs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_vlans_module.html
fetched_at: 2026-07-28T01:26:30+00:00
---
# cisco.ios.ios_vlans module – Resource module to configure VLANs.

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
> To use it in a playbook, specify: `cisco.ios.ios_vlans`.

New in cisco.ios 1.0.0

- [Synopsis](ios_vlans_module.md#synopsis)
- [Parameters](ios_vlans_module.md#parameters)
- [Notes](ios_vlans_module.md#notes)
- [Examples](ios_vlans_module.md#examples)
- [Return Values](ios_vlans_module.md#return-values)

## [Synopsis](ios_vlans_module.md#id1)

- This module provides declarative management of VLANs on Cisco IOS network devices.

Aliases: vlans

## [Parameters](ios_vlans_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of VLANs options |
| **mtu**  integer | VLAN Maximum Transmission Unit.  Refer to vendor documentation for valid values. |
| **name**  string | Ascii name of the VLAN.  NOTE, *name* should not be named/appended with *default* as it is reserved for device default vlans. |
| **private_vlan**  dictionary | Options for private vlan configuration. |
| **associated**  list / elements=integer | List of private VLANs associated with the primary . Only works with `type: primary`. |
| **type**  string | Private VLAN type  **Choices:**   - `"primary"` - `"isolated"` - `"community"` |
| **remote_span**  boolean | Configure as Remote SPAN VLAN  **Choices:**   - `false` - `true` |
| **shutdown**  string | Shutdown VLAN switching.  **Choices:**   - `"enabled"` - `"disabled"` |
| **state**  string | Operational state of the VLAN  **Choices:**   - `"active"` - `"suspend"` |
| **vlan_id**  integer / required | ID of the VLAN. Range 1-4094 |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show vlan**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](ios_vlans_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSl2 device with Version 15.2 on VIRL.
> - Starting from v2.5.0, this module will fail when run against Cisco IOS devices that do not support VLANs. The offline states (`rendered` and `parsed`) will work as expected.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_vlans_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

- name: Merge provided configuration with device configuration
  cisco.ios.ios_vlans:
    config:
      - name: Vlan_10
        vlan_id: 10
        state: active
        shutdown: disabled
        remote_span: true
      - name: Vlan_20
        vlan_id: 20
        mtu: 610
        state: active
        shutdown: enabled
      - name: Vlan_30
        vlan_id: 30
        state: suspend
        shutdown: enabled
    state: merged

# After state:
# ------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

# Using overridden

# Before state:
# -------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Override device configuration of all VLANs with provided configuration
  cisco.ios.ios_vlans:
    config:
      - name: Vlan_10
        vlan_id: 10
        mtu: 1000
    state: overridden

# After state:
# ------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   Vlan_10                          active
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1000  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

# Using replaced

# Before state:
# -------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Replaces device configuration of listed VLANs with provided configuration
  cisco.ios.ios_vlans:
    config:
      - vlan_id: 20
        name: Test_VLAN20
        mtu: 700
        shutdown: disabled
      - vlan_id: 50
        name: pvlan-isolated
        private_vlan:
          type: isolated
      - vlan_id: 60
        name: pvlan-community
        private_vlan:
          type: community
      - vlan_id: 70
        name: pvlan-primary
        private_vlan:
          type: primary
          associated:
            - 50
            - 60

    state: replaced

# After state:
# ------------
#
# vios_l2#sh vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/0, Gi0/1, Gi0/2, Gi0/3
# 10   Vlan_10                          active
# 20   Test_VLAN20                      active
# 50   pvlan-isolated                   active
# 60   pvlan-community                  active
# 70   pvlan-primary                    active
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1000  -      -      -        -    -        0      0
# 20   enet  100020     700   -      -      -        -    -        0      0
# 50   enet  100050     1500  -      -      -        -    -        0      0
# 60   enet  100051     1500  -      -      -        -    -        0      0
# 70   enet  100059     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
#
#
# Primary Secondary Type              Ports
# ------- --------- ----------------- ------------------------------------------
# 70      50        isolated
# 70      60        community

# Using deleted

# Before state:
# -------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Delete attributes of given VLANs
  cisco.ios.ios_vlans:
    config:
      - vlan_id: 10
      - vlan_id: 20
    state: deleted

# After state:
# -------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured vlans attributes)"

# Before state:
# -------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Delete attributes of ALL VLANs
  cisco.ios.ios_vlans:
    state: deleted

# After state:
# -------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

# Using Gathered

# Before state:
# -------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

- name: Gather listed vlans with provided configurations
  cisco.ios.ios_vlans:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "mtu": 1500,
#             "name": "default",
#             "shutdown": "disabled",
#             "state": "active",
#             "vlan_id": 1
#         },
#         {
#             "mtu": 1500,
#             "name": "VLAN0010",
#             "shutdown": "disabled",
#             "state": "active",
#             "vlan_id": 10
#         },
#         {
#             "mtu": 1500,
#             "name": "VLAN0020",
#             "shutdown": "disabled",
#             "state": "active",
#             "vlan_id": 20
#         },
#         {
#             "mtu": 1500,
#             "name": "VLAN0030",
#             "shutdown": "disabled",
#             "state": "active",
#             "vlan_id": 30
#         },
#         {
#             "mtu": 1500,
#             "name": "fddi-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1002
#         },
#         {
#             "mtu": 1500,
#             "name": "token-ring-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1003
#         },
#         {
#             "mtu": 1500,
#             "name": "fddinet-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1004
#         },
#         {
#             "mtu": 1500,
#             "name": "trnet-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1005
#         }
#     ]

# After state:
# ------------
#
# vios_l2#show vlan
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     610   -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0
#
# Remote SPAN VLANs
# ------------------------------------------------------------------------------
# 10

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_vlans:
    config:
      - name: Vlan_10
        vlan_id: 10
        state: active
        shutdown: disabled
        remote_span: true
      - name: Vlan_20
        vlan_id: 20
        mtu: 610
        state: active
        shutdown: enabled
      - name: Vlan_30
        vlan_id: 30
        state: suspend
        shutdown: enabled
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "vlan 10",
#         "name Vlan_10",
#         "state active",
#         "remote-span",
#         "no shutdown",
#         "vlan 20",
#         "name Vlan_20",
#         "state active",
#         "mtu 610",
#         "shutdown",
#         "vlan 30",
#         "name Vlan_30",
#         "state suspend",
#         "shutdown"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     1500  -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

- name: Parse the commands for provided configuration
  cisco.ios.ios_vlans:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "mtu": 1500,
#             "name": "default",
#             "shutdown": "disabled",
#             "state": "active",
#             "vlan_id": 1
#         },
#         {
#             "mtu": 1500,
#             "name": "vlan_10",
#             "shutdown": "disabled",
#             "state": "active",
#             "vlan_id": 10
#         },
#         {
#             "mtu": 1500,
#             "name": "vlan_20",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 20
#         },
#         {
#             "mtu": 1500,
#             "name": "vlan_30",
#             "shutdown": "enabled",
#             "state": "suspend",
#             "vlan_id": 30
#         },
#         {
#             "mtu": 1500,
#             "name": "fddi-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1002
#         },
#         {
#             "mtu": 1500,
#             "name": "token-ring-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1003
#         },
#         {
#             "mtu": 1500,
#             "name": "fddinet-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1004
#         },
#         {
#             "mtu": 1500,
#             "name": "trnet-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1005
#         }
#     ]
```

## [Return Values](ios_vlans_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["vlan 20", "name vlan_20", "mtu 600", "remote-span"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
