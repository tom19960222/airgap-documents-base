---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_radius_server module – Manage RADIUS server and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_radius_server_module.html
fetched_at: 2026-07-28T02:03:47+00:00
---
# dellemc.enterprise_sonic.sonic_radius_server module – Manage RADIUS server and its parameters

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_radius_server`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_radius_server_module.md#synopsis)
- [Parameters](sonic_radius_server_module.md#parameters)
- [Notes](sonic_radius_server_module.md#notes)
- [Examples](sonic_radius_server_module.md#examples)
- [Return Values](sonic_radius_server_module.md#return-values)

## [Synopsis](sonic_radius_server_module.md#id1)

- This module provides configuration management of radius server parameters on devices running Enterprise SONiC.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_radius_server_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies the radius server related configuration. |
| **auth_type**  string | Specifies the authentication type of the radius server.  **Choices:**   - `"pap"` ← (default) - `"chap"` - `"mschapv2"` |
| **key**  string | Specifies the key of the radius server. |
| **nas_ip**  string | Specifies the network access server of the radius server. |
| **retransmit**  integer | Specifies the re-transmit value of the radius server. |
| **servers**  dictionary | Specifies the servers list of the radius server. |
| **host**  list / elements=dictionary | Specifies the host details of the radius servers list. |
| **auth_type**  string | Specifies the authentication type of the radius server host.  **Choices:**   - `"pap"` - `"chap"` - `"mschapv2"` |
| **key**  string | Specifies the key of the radius server host. |
| **name**  string | Specifies the name of the radius server host. |
| **port**  integer | Specifies the port of the radius server host.  **Default:** `1812` |
| **priority**  integer | Specifies the priority of the radius server host. |
| **retransmit**  integer | Specifies the retransmit of the radius server host. |
| **source_interface**  string | Specifies the source interface of the radius server host. |
| **timeout**  integer | Specifies the timeout of the radius server host. |
| **vrf**  string | Specifies the vrf of the radius server host. |
| **statistics**  boolean | Specifies the statistics flag of the radius server.  **Choices:**   - `false` - `true` |
| **timeout**  integer | Specifies the timeout of the radius server.  **Default:** `5` |
| **state**  string | Specifies the operation to be performed on the radius server configured on the device.  In case of merged, the input mode configuration will be merged with the existing radius server configuration on the device.  In case of deleted the existing radius server mode configuration will be removed from the device.  In case of replaced, the existing radius server configuration will be replaced with provided configuration.  In case of overridden, the existing radius server configuration will be overridden with the provided configuration.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Notes](sonic_radius_server_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_radius_server_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#nas-ip-addr: 1.2.3.4
#statistics : True
#timeout    : 10
#auth-type  : chap
#key        : chap
#retransmit : 3
#--------------------------------------------------------------------------------
#HOST            AUTH-TYPE KEY       AUTH-PORT PRIORITY TIMEOUT RTSMT VRF   SI
#--------------------------------------------------------------------------------
#localhost       mschapv2  local     52        2        20      2     mgmt  Ethernet12
#myhost          chap      local     53        3        23      3     mgmt  Ethernet24
#---------------------------------------------------------
#RADIUS Statistics
#---------------------------------------------------------
#

- name: Merge radius configurations
  dellemc.enterprise_sonic.sonic_radius_server:
    config:
      auth_type: chap
      nas_ip: 1.2.3.4
      statistics: true
      timeout: 10
      servers:
        host:
          - name: localhost
    state: deleted

# After state:
# ------------
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#timeout    : 5
#auth-type  : pap
#key        : chap
#retransmit : 3
#--------------------------------------------------------------------------------
#HOST            AUTH-TYPE KEY       AUTH-PORT PRIORITY TIMEOUT RTSMT VRF   SI
#--------------------------------------------------------------------------------
#myhost          chap      local     53        3        23      3     mgmt  Ethernet24

# Using deleted
#
# Before state:
# -------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#nas-ip-addr: 1.2.3.4
#statistics : True
#timeout    : 10
#auth-type  : chap
#key        : chap
#retransmit : 3
#--------------------------------------------------------------------------------
#HOST            AUTH-TYPE KEY       AUTH-PORT PRIORITY TIMEOUT RTSMT VRF   SI
#--------------------------------------------------------------------------------
#localhost       mschapv2  local     52        2        20      2     mgmt  Ethernet12
#myhost          chap      local     53        3        23      3     mgmt  Ethernet24
#---------------------------------------------------------
#RADIUS Statistics
#---------------------------------------------------------
#
- name: Merge radius configurations
  dellemc.enterprise_sonic.sonic_radius_server:
    config:
    state: deleted

# After state:
# ------------
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#timeout    : 5
#auth-type  : pap

# Using merged
#
# Before state:
# -------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#
- name: Merge radius configurations
  dellemc.enterprise_sonic.sonic_radius_server:
    config:
      auth_type: chap
      key: chap
      nas_ip: 1.2.3.4
      statistics: true
      timeout: 10
      retransmit: 3
      servers:
        host:
          - name: localhost
            auth_type: mschapv2
            key: local
            priority: 2
            port: 52
            retransmit: 2
            timeout: 20
            source_interface: Eth 12
            vrf: mgmt
    state: merged

# After state:
# ------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#nas-ip-addr: 1.2.3.4
#statistics : True
#timeout    : 10
#auth-type  : chap
#key        : chap
#retransmit : 3
#--------------------------------------------------------------------------------
#HOST            AUTH-TYPE KEY       AUTH-PORT PRIORITY TIMEOUT RTSMT VRF   SI
#--------------------------------------------------------------------------------
#localhost       mschapv2  local     52        2        20      2     mgmt  Ethernet12
#---------------------------------------------------------
#RADIUS Statistics
#---------------------------------------------------------
#
# Using replaced
#
# Before state:
# -------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#timeout           : 10
#auth-type         : pap
#key configured    : Yes
#--------------------------------------------------------------------------------------
#HOST        AUTH-TYPE KEY-CONFIG AUTH-PORT PRIORITY TIMEOUT RTSMT VRF     SI
#--------------------------------------------------------------------------------------
#1.2.3.4     pap       No         49        1         5      -     -       Ethernet0
#
- name: Replace radius configurations
  sonic_radius_server:
    config:
      auth_type: mschapv2
      timeout: 20
      servers:
        - host:
            name: 1.2.3.4
            auth_type: mschapv2
            key: mschapv2
            source_interface: Ethernet12
    state: replaced
#
# After state:
# ------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#timeout           : 20
#auth-type         : mschapv2
#key configured    : No
#--------------------------------------------------------------------------------------
#HOST        AUTH-TYPE KEY-CONFIG AUTH-PORT PRIORITY TIMEOUT RTSMT VRF     SI
#--------------------------------------------------------------------------------------
#1.2.3.4      mschapv2 Yes        1812       -          -    -     -       Ethernet12
#
# Using overridden
#
# Before state:
# -------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#timeout           : 10
#auth-type         : pap
#key configured    : Yes
#--------------------------------------------------------------------------------------
#HOST        AUTH-TYPE KEY-CONFIG AUTH-PORT PRIORITY TIMEOUT RTSMT VRF     SI
#--------------------------------------------------------------------------------------
#1.2.3.4     pap       No         49        1         5      -     -       Ethernet0
#11.12.13.14 chap      Yes        49        10        5      3     -       -
#
- name: Override radius configurations
  sonic_radius_server:
    config:
      auth_type: mschapv2
      key: mschapv2
      timeout: 20
      servers:
        - host:
            name: 1.2.3.4
            auth_type: mschapv2
            key: mschapv2
            source_interface: Ethernet12
        - host:
            name: 10.10.11.12
            auth_type: chap
            timeout: 30
            priority: 2
            port: 49
    state: overridden
#
# After state:
# ------------
#
#sonic(config)# do show radius-server
#---------------------------------------------------------
#RADIUS Global Configuration
#---------------------------------------------------------
#timeout           : 20
#auth-type         : mschapv2
#key configured    : Yes
#--------------------------------------------------------------------------------------
#HOST        AUTH-TYPE KEY-CONFIG AUTH-PORT PRIORITY TIMEOUT RTSMT VRF     SI
#--------------------------------------------------------------------------------------
#1.2.3.4      mschapv2 Yes        1812       -          -    -     -       Ethernet12
#10.10.11.12  chap     No         49         2          30   -     -       -
#
```

## [Return Values](sonic_radius_server_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M (@niraimadaiselvamm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
