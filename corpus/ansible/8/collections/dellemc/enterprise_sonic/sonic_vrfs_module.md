---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_vrfs module – Manage VRFs and associate VRFs to interfaces such as, Eth, LAG, VLAN, and loopback"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_vrfs_module.html
fetched_at: 2026-07-28T02:03:54+00:00
---
# dellemc.enterprise_sonic.sonic_vrfs module – Manage VRFs and associate VRFs to interfaces such as, Eth, LAG, VLAN, and loopback

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_vrfs`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_vrfs_module.md#synopsis)
- [Parameters](sonic_vrfs_module.md#parameters)
- [Notes](sonic_vrfs_module.md#notes)
- [Examples](sonic_vrfs_module.md#examples)
- [Return Values](sonic_vrfs_module.md#return-values)

## [Synopsis](sonic_vrfs_module.md#id1)

- Manages VRF and VRF interface attributes in Enterprise SONiC Distribution by Dell Technologies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_vrfs_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of VRF configurations. |
| **members**  dictionary | Holds a dictionary mapping of list of interfaces linked to a VRF interface. |
| **interfaces**  list / elements=dictionary | List of interface names that are linked to a specific VRF interface. |
| **name**  string | The name of the physical interface. |
| **name**  string / required | The name of the VRF interface. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` |

## [Notes](sonic_vrfs_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_vrfs_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/3
#                    Eth1/14
#                    Eth1/16
#                    Eth1/17
#Vrfcheck4           Eth1/5
#                    Eth1/6
#
- name: Configuring vrf deleted state
  dellemc.enterprise_sonic.sonic_vrfs:
    config:
     - name: Vrfcheck4
       members:
         interfaces:
           - name: Eth1/6
     - name: Vrfcheck3
       members:
         interfaces:
           - name: Eth1/3
           - name: Eth1/14
    state: deleted
#
# After state:
# ------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/16
#                    Eth1/17
#Vrfcheck4           Eth1/5
#
#
# Using merged
#
# Before state:
# -------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/16
#                    Eth1/17
#Vrfcheck4
#
- name: Configuring vrf merged state
  dellemc.enterprise_sonic.sonic_vrfs:
    config:
     - name: Vrfcheck4
       members:
         interfaces:
           - name: Eth1/5
           - name: Eth1/6
     - name: Vrfcheck3
       members:
         interfaces:
           - name: Eth1/3
           - name: Eth1/14
    state: merged
#
# After state:
# ------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/3
#                    Eth1/14
#                    Eth1/16
#                    Eth1/17
#Vrfcheck4           Eth1/5
#                    Eth1/6
#
# Using overridden
#
# Before state:
# -------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/7
#                    Eth1/8
#
- name: Overridden VRF configuration
  dellemc.enterprise_sonic.sonic_vrfs:
  sonic_vrfs:
    config:
      - name: Vrfcheck1
        members:
          interfaces:
            - name: Eth1/3
            - name: Eth1/14
      - name: Vrfcheck3
        members:
          interfaces:
            - name: Eth1/5
            - name: Eth1/6
    state: overridden
#
# After state:
# ------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1           Eth1/3
#                    Eth1/14
#Vrfcheck2
#Vrfcheck3           Eth1/5
#                    Eth1/6
#
# Using replaced
#
# Before state:
# -------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1           Eth1/3
#Vrfcheck2
#Vrfcheck3           Eth1/5
#                    Eth1/6
#
- name: Replace VRF configuration
  dellemc.enterprise_sonic.sonic_vrfs:
  sonic_vrfs:
    config:
      - name: Vrfcheck1
        members:
          interfaces:
            - name: Eth1/3
            - name: Eth1/14
      - name: Vrfcheck3
        members:
          interfaces:
            - name: Eth1/5
            - name: Eth1/6
    state: replaced
#
# After state:
# ------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1           Eth1/3
#                    Eth1/14
#Vrfcheck2
#Vrfcheck3           Eth1/5
#                    Eth1/6
#
```

## [Return Values](sonic_vrfs_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Abirami N (@abirami-n)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
