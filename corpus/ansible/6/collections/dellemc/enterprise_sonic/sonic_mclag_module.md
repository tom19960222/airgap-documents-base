---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_mclag module – Manage multi chassis link aggregation groups domain (MCLAG) and its parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_mclag_module.html
fetched_at: 2026-07-27T17:24:56+00:00
---
# dellemc.enterprise_sonic.sonic_mclag module – Manage multi chassis link aggregation groups domain (MCLAG) and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
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

- Manage multi chassis link aggregation groups domain (MCLAG) and its parameters

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_mclag_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Dict of mclag domain configurations. |
| **domain_id**  integer / required | ID of the mclag domain (MCLAG domain). |
| **keepalive**  integer | MCLAG session keepalive-interval in secs. |
| **members**  dictionary | Holds portchannels dictionary for an MCLAG domain. |
| **portchannels**  list / elements=dictionary | Holds a list of portchannels for configuring as an MCLAG interface. |
| **lag**  string | Holds a PortChannel ID. |
| **peer_address**  string | The IPV4 peer-ip for corresponding MCLAG. |
| **peer_link**  string | Peer-link for corresponding MCLAG. |
| **session_timeout**  integer | MCLAG session timeout value in secs. |
| **source_address**  string | The IPV4 source-ip for corresponding MCLAG. |
| **system_mac**  string | Mac address of MCLAG. |
| **unique_ip**  dictionary | Holds Vlan dictionary for mclag unique ip. |
| **vlans**  list / elements=dictionary | Holds list of VLANs for which a separate IP addresses is enabled for Layer 3 protocol support over MCLAG. |
| **vlan**  string | Holds a VLAN ID. |
| **state**  string | The state that the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"deleted"` |

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
#
- name: Merge provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      peer_address: 1.1.1.1
      source_address: 2.2.2.2
      peer_link: 'Portchannel1'
      keepalive: 1
      session_timeout: 3
      unique_ip:
          vlans:
            - vlan: Vlan4
      members:
          portchannles:
            - lag: PortChannel10
    state: merged
#
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
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
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
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
- name: Merge device configuration with the provided configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
      domain_id: 1
      source_address: 3.3.3.3
      keepalive: 10
      session_timeout: 30
      unique_ip:
        vlans:
          - vlan: Vlan5
      members:
        portchannels:
          - lag: PortChannel12
    state: merged
#
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
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:2
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
# PortChannel12            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        },
#         "Vlan5": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
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
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
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
#
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
# Session Timeout      : 15 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:0
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
#
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
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:1
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
- name: Delete all device configuration
  dellemc.enterprise_sonic.sonic_mclag:
    config:
    state: deleted
#
# After state:
# ------------
#
# sonic# show mclag brief
# MCLAG Not Configured
#
# admin@sonic:~$ show runningconfiguration all | grep MCLAG_UNIQUE_IP
# admin@sonic:~$
#
#
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
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:2
#-----------------------------------------------------------
# MLAG Interface       Local/Remote Status
#-----------------------------------------------------------
# PortChannel10            down/down
# PortChannel12            down/sown
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
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
#
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
# Session Timeout      : 15 secs
# System Mac           : 20:04:0f:37:bd:c9
#
#
# Number of MLAG Interfaces:0
#
# admin@sonic:~$ show runningconfiguration all
# {
# ...
# "MCLAG_UNIQUE_IP": {
#        "Vlan4": {
#            "unique_ip": "enable"
#        }
#    },
# ...
# }
#
#
```

## [Return Values](sonic_mclag_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned always in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned always in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
