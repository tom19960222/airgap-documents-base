---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_lacp module – Resource module to configure LACP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_lacp_module.html
fetched_at: 2026-07-28T01:26:44+00:00
---
# cisco.iosxr.iosxr_lacp module – Resource module to configure LACP.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_lacp`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_lacp_module.md#synopsis)
- [Parameters](iosxr_lacp_module.md#parameters)
- [Notes](iosxr_lacp_module.md#notes)
- [Examples](iosxr_lacp_module.md#examples)
- [Return Values](iosxr_lacp_module.md#return-values)

## [Synopsis](iosxr_lacp_module.md#id1)

- This module manages Global Link Aggregation Control Protocol (LACP) on IOS-XR devices.

Aliases: lacp

## [Parameters](iosxr_lacp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The provided configurations. |
| **system**  dictionary | This option sets the default system parameters for LACP bundles. |
| **mac**  dictionary | The system MAC related configuration for LACP. |
| **address**  string | The system ID to use in LACP negotiations. |
| **priority**  integer | The system priority to use in LACP negotiations.  Lower value is higher priority.  Refer to vendor documentation for valid values. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config lacp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"parsed"` - `"rendered"` - `"gathered"` |

## [Notes](iosxr_lacp_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).

## [Examples](iosxr_lacp_module.md#id4)

```yaml+jinja
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#show running-config lacp
# Tue Jul 16 17:46:08.147 UTC
# % No such configuration item(s)
#
#

- name: Merge provided configuration with device configuration
  cisco.iosxr.iosxr_lacp:
    config:
      system:
        priority: 10
        mac:
          address: 00c1.4c00.bd15
    state: merged

#
#
# -----------------------
# Module Execution Result
# -----------------------
#
# "before": {}
#
#
# "commands": [
#    "lacp system priority 10",
#    "lacp system mac 00c1.4c00.bd15"
#  ]
#
#
# "after": {
#    "system": {
#       "mac": {
#          "address": "00c1.4c00.bd15"
#       },
#       "priority": 10
#     }
#  }
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 17:51:29.365 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 10
#
#

# Using replaced
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 17:53:59.904 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 10
#

- name: Replace device global lacp configuration with the given configuration
  cisco.iosxr.iosxr_lacp:
    config:
      system:
        priority: 11
    state: replaced
#
#
# -----------------------
# Module Execution Result
# -----------------------
# "before": {
#    "system": {
#       "mac": {
#         "address": "00c1.4c00.bd15"
#       },
#       "priority": 10
#    }
#  }
#
#
# "commands": [
#    "no lacp system mac",
#    "lacp system priority 11"
#  ]
#
#
# "after": {
#    "system": {
#       "priority": 11
#    }
# }
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:02:40.379 UTC
# lacp system priority 11
#
#

# Using deleted
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:37:09.727 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 11
#
#

- name: Delete global LACP configurations from the device
  cisco.iosxr.iosxr_lacp:
    state: deleted

#
#
# -----------------------
# Module Execution Result
# -----------------------
# "before": {
#    "system": {
#       "mac": {
#         "address": "00c1.4c00.bd15"
#       },
#       "priority": 11
#    }
# }
#
#
# "commands": [
#     "no lacp system mac",
#     "no lacp system priority"
# ]
#
#
# "after": {}
#
# ------------
# After state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:39:44.116 UTC
# % No such configuration item(s)
#
#

# Using parsed
# parsed.cfg
# ------------
#
# lacp system mac 00c1.4c00.bd15
# lacp system priority 11
# - name: Convert LACP config to argspec without connecting to the appliance
#   cisco.iosxr.iosxr_lacp:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": {
#         "system": {
#             "mac": {
#                 "address": "00c1.4c00.bd15"
#             },
#             "priority": 11
#         }
#     }

# Using rendered
- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_lacp:
    config:
      system:
        priority: 11
        mac:
          address: 00c1.4c00.bd15
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": [
#         "lacp system priority 11",
#         "lacp system mac 00c1.4c00.bd15"
#     ]

# Using gathered
# Before state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config lacp
# lacp system mac 00c1.4c00.bd15
# lacp system priority 11
- name: Gather IOSXR LACP configuration
  cisco.iosxr.iosxr_lacp:
    config:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": {
#         "system": {
#             "mac": {
#                 "address": "00c1.4c00.bd15"
#             },
#             "priority": 11
#         }
#     }
# After state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config lacp
# lacp system mac 00c1.4c00.bd15
# lacp system priority
```

## [Return Values](iosxr_lacp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["lacp system priority 10", "lacp system mac 00c1.4c00.bd15"]` |

### Authors

- Nilashish Chakraborty (@nilashishc)
- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
