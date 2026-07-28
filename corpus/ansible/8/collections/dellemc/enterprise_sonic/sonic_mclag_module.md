---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_mclag module – Manage multi chassis link aggregation groups domain (MCLAG) and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_mclag_module.html
fetched_at: 2026-07-28T02:03:44+00:00
---
# dellemc.enterprise_sonic.sonic_mclag module – Manage multi chassis link aggregation groups domain (MCLAG) and its parameters

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_mclag`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_mclag_module.md#synopsis)
- [Parameters](sonic_mclag_module.md#parameters)
- [Notes](sonic_mclag_module.md#notes)
- [Examples](sonic_mclag_module.md#examples)
- [Return Values](sonic_mclag_module.md#return-values)

## [Synopsis](sonic_mclag_module.md#id1)

- Manage multi chassis link aggregation groups domain (MCLAG) and its parameters.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_mclag_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Dict of mclag domain configurations. |
| **delay_restore**  integer | MCLAG delay restore time in secs. |
| **domain_id**  integer / required | ID of the mclag domain (MCLAG domain). |
| **gateway_mac**  string | Gateway MAC address for router ports over MCLAG. |
| **keepalive**  integer | MCLAG session keepalive-interval in secs. |
| **members**  dictionary | Holds portchannels dictionary for an MCLAG domain. |
| **portchannels**  list / elements=dictionary | Holds a list of portchannels for configuring as an MCLAG interface. |
| **lag**  string | Holds a PortChannel ID. |
| **peer_address**  string | The IPV4 peer-ip for corresponding MCLAG. |
| **peer_gateway**  dictionary | Holds Vlan dictionary for MCLAG peer gateway. |
| **vlans**  list / elements=dictionary | Holds a list of VLANs for which MCLAG peer gateway functionality is enabled. |
| **vlan**  string | Holds a VLAN ID. |
| **peer_link**  string | Peer-link for corresponding MCLAG. |
| **session_timeout**  integer | MCLAG session timeout value in secs. |
| **source_address**  string | The IPV4 source-ip for corresponding MCLAG. |
| **system_mac**  string | MAC address of MCLAG. |
| **unique_ip**  dictionary | Holds Vlan dictionary for MCLAG unique IP. |
| **vlans**  list / elements=dictionary | Holds a list of VLANs for which a separate IP address is enabled for Layer 3 protocol support over MCLAG. |
| **vlan**  string | Holds a VLAN ID. |
| **state**  string | The state that the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_mclag_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_mclag_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# sonic# show mclag brief
# MCLAG Not Configured

- name: Merge provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      peer_address: 1.1.1.1
      source_address: 2.2.2.2
      peer_link: 'Portchannel1'
      keepalive: 1
      session_timeout: 3
      delay_restore: 240
      system_mac: '00:00:00:11:11:11'
      gateway_mac: '00:00:00:12:12:12'
      unique_ip:
        vlans:
          - vlan: Vlan4
      peer_gateway:
        vlans:
          - vlan: Vlan4
      members:
        portchannels:
          - lag: PortChannel10
    state: merged

# After state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 2.2.2.2
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 1 secs
# Session Timeout      : 3 secs
# Delay Restore        : 240 secs
# System Mac           : 20:04:0f:37:bd:c9
# Mclag System Mac     : 00:00:00:11:11:11
# Gateway Mac          : 00:00:00:12:12:12
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# sonic# show mclag separate-ip-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#
# sonic# show mclag peer-gateway-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#

# Using merged
#
# Before state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 2.2.2.2
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 1 secs
# Session Timeout      : 3 secs
# Delay Restore        : 240 secs
# System Mac           : 20:04:0f:37:bd:c9
# Mclag System Mac     : 00:00:00:11:11:11
# Gateway Mac          : 00:00:00:12:12:12
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# sonic# show mclag separate-ip-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#
# sonic# show mclag peer-gateway-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#

- name: Merge device configuration with the provided configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      source_address: 3.3.3.3
      keepalive: 10
      session_timeout: 30
      delay_restore: 360
      unique_ip:
        vlans:
          - vlan: Vlan5
      peer_gateway:
        vlans:
          - vlan: Vlan5
      members:
        portchannels:
          - lag: PortChannel12
    state: merged

# After state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 3.3.3.3
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 10 secs
# Session Timeout      : 30 secs
# Delay Restore        : 360 secs
# System Mac           : 20:04:0f:37:bd:c9
# Mclag System Mac     : 00:00:00:11:11:11
# Gateway Mac          : 00:00:00:12:12:12
#
#
# Number of MLAG Interfaces:2
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
# PortChannel12            down/down
#
# sonic# show mclag separate-ip-interfaces
# Interface Name
# ==============
# Vlan4
# Vlan5
# ==============
# Total count :    2
# ==============
# sonic# show mclag peer-gateway-interfaces
# Interface Name
# ==============
# Vlan4
# Vlan5
# ==============
# Total count :    2
# ==============
# sonic#

# Using deleted
#
# Before state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 3.3.3.3
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 10 secs
# Session Timeout      : 30 secs
# Delay Restore        : 360 secs
# System Mac           : 20:04:0f:37:bd:c9
# Mclag System Mac     : 00:00:00:11:11:11
# Gateway Mac          : 00:00:00:12:12:12
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# sonic# show mclag separate-ip-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#
# sonic# show mclag peer-gateway-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#

- name: Delete device configuration based on the provided configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      source_address: 3.3.3.3
      keepalive: 10
      members:
        portchannels:
          - lag: PortChannel10
    state: deleted

# After state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       :
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 1 secs
# Session Timeout      : 30 secs
# Delay Restore        : 360 secs
# System Mac           : 20:04:0f:37:bd:c9
# Mclag System Mac     : 00:00:00:11:11:11
# Gateway Mac          : 00:00:00:12:12:12
#
#
# Number of MLAG Interfaces:0
#
# sonic# show mclag separate-ip-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#
# sonic# show mclag peer-gateway-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#

# Using deleted
#
# Before state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 3.3.3.3
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 10 secs
# Session Timeout      : 30 secs
# Delay Restore        : 360 secs
# System Mac           : 20:04:0f:37:bd:c9
# Mclag System Mac     : 00:00:00:11:11:11
# Gateway Mac          : 00:00:00:12:12:12
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# sonic# show mclag separate-ip-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#
# sonic# show mclag peer-gateway-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#

- name: Delete all device configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
    state: deleted

# After state:
# ------------
#
# sonic# show mclag brief
# MCLAG Not Configured
# sonic# show mclag separate-ip-interfaces
# MCLAG separate IP interface not configured
# sonic# show mclag peer-gateway-interfaces
# MCLAG Peer Gateway interface not configured
# sonic#

# Using deleted
#
# Before state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       : 3.3.3.3
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 10 secs
# Session Timeout      : 30 secs
# Delay Restore        : 360 secs
# System Mac           : 20:04:0f:37:bd:c9
# Mclag System Mac     : 00:00:00:11:11:11
# Gateway Mac          : 00:00:00:12:12:12
#
#
# Number of MLAG Interfaces:2
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
# PortChannel12            down/down
#
# sonic# show mclag separate-ip-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#
# sonic# show mclag peer-gateway-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#

- name: Delete device configuration based on the provided configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      source_address: 3.3.3.3
      keepalive: 10
      peer_gateway:
        vlans:
      members:
        portchannels:
    state: deleted

# After state:
# ------------
#
# sonic# show mclag brief
#
# Domain ID            : 1
# Role                 : standby
# Session Status       : down
# Peer Link Status     : down
# Source Address       :
# Peer Address         : 1.1.1.1
# Peer Link            : PortChannel1
# Keepalive Interval   : 1 secs
# Session Timeout      : 30 secs
# Delay Restore        : 360 secs
# System Mac           : 20:04:0f:37:bd:c9
# Mclag System Mac     : 00:00:00:11:11:11
# Gateway Mac          : 00:00:00:12:12:12
#
#
# Number of MLAG Interfaces:0
#
# sonic# show mclag separate-ip-interfaces
# Interface Name
# ==============
# Vlan4
# ==============
# Total count :    1
# ==============
# sonic#
# sonic# show mclag peer-gateway-interfaces
# MCLAG Peer Gateway interface not configured
# sonic#
```

## [Return Values](sonic_mclag_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned always in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned always in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
