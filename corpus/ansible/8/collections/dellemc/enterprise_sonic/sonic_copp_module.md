---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_copp module – Manage CoPP configuration on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_copp_module.html
fetched_at: 2026-07-28T02:03:34+00:00
---
# dellemc.enterprise_sonic.sonic_copp module – Manage CoPP configuration on SONiC

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_copp`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_copp_module.md#synopsis)
- [Parameters](sonic_copp_module.md#parameters)
- [Examples](sonic_copp_module.md#examples)
- [Return Values](sonic_copp_module.md#return-values)

## [Synopsis](sonic_copp_module.md#id1)

- This module provides configuration management of CoPP for devices running SONiC

## [Parameters](sonic_copp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies CoPP configurations |
| **copp_groups**  list / elements=dictionary | List of CoPP entries that comprise a CoPP group |
| **cbs**  string | Committed bucket size in packets or bytes |
| **cir**  string | Committed information rate in bps or pps (packets per second) |
| **copp_name**  string / required | Name of CoPP classifier |
| **queue**  integer | CoPP queue ID |
| **trap_action**  string | CoPP trap action |
| **trap_priority**  integer | CoPP trap priority |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Examples](sonic_copp_module.md#id3)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# sonic# show copp actions
# (No "copp actions" configuration present)

  - name: Merge CoPP groups configuration
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      copp_groups:
        - copp_name: 'copp-1'
          trap_priority: 1
          trap_action: 'DROP'
          queue: 1
          cir: '45'
          cbs: '45'
        - copp_name: 'copp-2'
          trap_priority: 2
          trap_action: 'FORWARD'
          queue: 2
          cir: '90'
          cbs: '90'
    state: merged

# After state:
# ------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action drop
#    trap-priority 1
#    trap-queue 1
#    police cir 45 cbs 45
# CoPP action group copp-2
#    trap-action forward
#    trap-priority 2
#    trap-queue 2
#    police cir 90 cbs 90
#
#
# Using replaced
#
# Before state:
# -------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action drop
#    trap-priority 1
#    trap-queue 1
#    police cir 45 cbs 45

  - name: Replace CoPP groups configuration
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      copp_groups:
        - copp_name: 'copp-1'
          trap_priority: 2
          trap_action: 'FORWARD'
          queue: 2
        - copp_name: 'copp-3'
          trap_priority: 3
          trap_action: 'DROP'
          queue: 3
          cir: '1000'
          cbs: '1000'
    state: replaced

# After state:
# ------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action forward
#    trap-priority 2
#    trap-queue 2
# CoPP action group copp-3
#    trap-action drop
#    trap-priority 3
#    trap-queue 3
#    police cir 1000 cbs 1000
#
#
# Using overridden
#
# Before state:
# -------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action forward
#    trap-priority 2
#    trap-queue 2
# CoPP action group copp-3
#    trap-action drop
#    trap-priority 3
#    trap-queue 3
#    police cir 1000 cbs 1000

  - name: Override CoPP groups configuration
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      copp_groups:
        - copp_name: 'copp-4'
          trap_priority: 4
          trap_action: 'FORWARD'
          queue: 4
          cir: 200
          cbs: 200
    state: overridden

# After state:
# ------------
#
# sonic# show copp actions
# CoPP action group copp-4
#    trap-action forward
#    trap-priority 4
#    trap-queue 4
#    police cir 200 cbs 200
#
#
# Using deleted
#
# Before state:
# -------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action drop
#    trap-priority 1
#    trap-queue 1
#    police cir 45 cbs 45
# CoPP action group copp-2
#    trap-action forward
#    trap-priority 2
#    trap-queue 2
#    police cir 90 cbs 90

  - name: Delete CoPP groups configuration
    dellemc.enterprise_sonic.sonic_static_routes:
    config:
      copp_groups:
        - copp_name: 'copp-1'
          trap_action: 'DROP'
          cir: '45'
          cbs: '45'
        - copp_name: 'copp-2'
    state: deleted

# After state:
# ------------
#
# sonic# show copp actions
# CoPP action group copp-1
#    trap-action drop
#    police cir 45 cbs 45
```

## [Return Values](sonic_copp_module.md#id4)

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
