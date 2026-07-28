---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_bgp module – Manage global BGP and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_bgp_module.html
fetched_at: 2026-07-28T02:03:27+00:00
---
# dellemc.enterprise_sonic.sonic_bgp module – Manage global BGP and its parameters

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
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_bgp`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_bgp_module.md#synopsis)
- [Parameters](sonic_bgp_module.md#parameters)
- [Notes](sonic_bgp_module.md#notes)
- [Examples](sonic_bgp_module.md#examples)
- [Return Values](sonic_bgp_module.md#return-values)

## [Synopsis](sonic_bgp_module.md#id1)

- This module provides configuration management of global BGP parameters on devices running Enterprise SONiC Distribution by Dell Technologies.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_bgp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the BGP-related configuration. |
| **bestpath**  dictionary | Configures the BGP best-path. |
| **as_path**  dictionary | Configures the as-path values. |
| **confed**  boolean | Configures the confed values of as-path.  **Choices:**   - `false` - `true` |
| **ignore**  boolean | Configures the ignore values of as-path.  **Choices:**   - `false` - `true` |
| **multipath_relax**  boolean | Configures the multipath_relax values of as-path.  **Choices:**   - `false` - `true` |
| **multipath_relax_as_set**  boolean | Configures the multipath_relax_as_set values of as-path.  **Choices:**   - `false` - `true` |
| **compare_routerid**  boolean | Configures the compare_routerid.  **Choices:**   - `false` - `true` |
| **med**  dictionary | Configures the med values. |
| **always_compare_med**  boolean | Allows comparing meds from different neighbors if set to true  **Choices:**   - `false` - `true` |
| **confed**  boolean | Configures the confed values of med.  **Choices:**   - `false` - `true` |
| **missing_as_worst**  boolean | Configures the missing_as_worst values of as-path.  **Choices:**   - `false` - `true` |
| **bgp_as**  string / required | Specifies the BGP autonomous system (AS) number to configure on the device. |
| **log_neighbor_changes**  boolean | Enables/disables logging neighbor up/down and reset reason.  **Choices:**   - `false` - `true` |
| **max_med**  dictionary | Configure max med and its parameters |
| **on_startup**  dictionary | On startup time and max-med value |
| **med_val**  integer | on startup med value |
| **timer**  integer | Configures on startup time |
| **router_id**  string | Configures the BGP routing process router-id value. |
| **rt_delay**  integer | Time in seconds to wait before processing route-map changes.  Range is 0-600. 0 disables the timer and changes to route-map will not be updated. |
| **timers**  dictionary | Adjust routing timers |
| **holdtime**  integer | Configures hold-time |
| **keepalive_interval**  integer | Configures keepalive-interval |
| **vrf_name**  string | Specifies the VRF name.  **Default:** `"default"` |
| **state**  string | Specifies the operation to be performed on the BGP process that is configured on the device.  In case of merged, the input configuration is merged with the existing BGP configuration on the device.  In case of deleted, the existing BGP configuration is removed from the device.  In case of replaced, the existing configuration of the specified BGP AS will be replaced with provided configuration.  In case of overridden, the existing BGP configuration will be overridden with the provided configuration.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Notes](sonic_bgp_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_bgp_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
# !
# router bgp 10 vrf VrfCheck1
#  router-id 10.2.2.32
#  route-map delay-timer 20
#  log-neighbor-changes
# !
# router bgp 11 vrf VrfCheck2
#  log-neighbor-changes
#  bestpath as-path ignore
#  bestpath med missing-as-worst confed
#  bestpath compare-routerid
# !
# router bgp 4
#  router-id 10.2.2.4
#  route-map delay-timer 10
#  bestpath as-path ignore
#  bestpath as-path confed
#  bestpath med missing-as-worst confed
#  bestpath compare-routerid
# !
#
- name: Delete BGP Global attributes
  dellemc.enterprise_sonic.sonic_bgp:
    config:
       - bgp_as: 4
         router_id: 10.2.2.4
         rt_delay: 10
         log_neighbor_changes: False
         bestpath:
           as_path:
             confed: True
             ignore: True
             multipath_relax: False
             multipath_relax_as_set: True
           compare_routerid: True
           med:
             confed: True
             missing_as_worst: True
       - bgp_as: 10
         router_id: 10.2.2.32
         rt_delay: 20
         log_neighbor_changes: True
         vrf_name: 'VrfCheck1'
       - bgp_as: 11
         log_neighbor_changes: True
         vrf_name: 'VrfCheck2'
         bestpath:
           as_path:
             confed: False
             ignore: True
             multipath_relax_as_set: True
           compare_routerid: True
           med:
             confed: True
             missing_as_worst: True
    state: deleted

# After state:
# ------------
#
# !
# router bgp 10 vrf VrfCheck1
#  log-neighbor-changes
# !
# router bgp 11 vrf VrfCheck2
#  log-neighbor-changes
#  bestpath compare-routerid
# !
# router bgp 4
#  log-neighbor-changes
#  bestpath compare-routerid
# !

# Using deleted
#
# Before state:
# -------------
#
# !
# router bgp 10 vrf VrfCheck1
#  router-id 10.2.2.32
#  route-map delay-timer 20
#  log-neighbor-changes
# !
# router bgp 11 vrf VrfCheck2
#  log-neighbor-changes
#  bestpath as-path ignore
#  bestpath med missing-as-worst confed
#  bestpath compare-routerid
# !
# router bgp 4
#  router-id 10.2.2.4
#  route-map delay-timer 10
#  bestpath as-path ignore
#  bestpath as-path confed
#  bestpath med missing-as-worst confed
#  bestpath compare-routerid
# !

- name: Deletes all the bgp global configurations
  dellemc.enterprise_sonic.sonic_bgp:
     config:
     state: deleted

# After state:
# ------------
#
# !
# !

# Using merged
#
# Before state:
# -------------
#
# !
# router bgp 4
#  router-id 10.1.1.4
# !
#
- name: Merges provided configuration with device configuration
  dellemc.enterprise_sonic.sonic_bgp:
     config:
       - bgp_as: 4
         router_id: 10.2.2.4
         rt_delay: 10
         log_neighbor_changes: False
         timers:
           holdtime: 20
           keepalive_interval: 30
         bestpath:
           as_path:
             confed: True
             ignore: True
             multipath_relax: False
             multipath_relax_as_set: True
           compare_routerid: True
           med:
             confed: True
             missing_as_worst: True
             always_compare_med: True
         max_med:
           on_startup:
             timer: 667
             med_val: 7878
       - bgp_as: 10
         router_id: 10.2.2.32
         rt_delay: 20
         log_neighbor_changes: True
         vrf_name: 'VrfCheck1'
       - bgp_as: 11
         log_neighbor_changes: True
         vrf_name: 'VrfCheck2'
         bestpath:
           as_path:
             confed: False
             ignore: True
             multipath_relax_as_set: True
           compare_routerid: True
           med:
             confed: True
             missing_as_worst: True
     state: merged
#
# After state:
# ------------
#
# !
# router bgp 10 vrf VrfCheck1
#  router-id 10.2.2.32
#  route-map delay-timer 20
#  log-neighbor-changes
# !
# router bgp 11 vrf VrfCheck2
#  log-neighbor-changes
#  bestpath as-path ignore
#  bestpath med missing-as-worst confed
#  bestpath compare-routerid
# !
# router bgp 4
#  router-id 10.2.2.4
#  route-map delay-timer 10
#  bestpath as-path ignore
#  bestpath as-path confed
#  bestpath med missing-as-worst confed
#  bestpath compare-routerid
#  always-compare-med
#  max-med on-startup 667 7878
#  timers 20 30
#
# !

# Using replaced
#
# Before state:
# -------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
# timers 60 180
#!
#router bgp 4
# router-id 10.2.2.4
# max-med on-startup 667 7878
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
# timers 20 30
#!
#

- name: Replace device configuration of specified BGP AS with provided
  dellemc.enterprise_sonic.sonic_bgp:
    config:
      - bgp_as: 4
        router_id: 10.2.2.44
        log_neighbor_changes: True
        bestpath:
          as_path:
            confed: True
          compare_routerid: True
      - bgp_as: 11
        vrf_name: 'VrfCheck2'
        router_id: 10.2.2.33
        log_neighbor_changes: True
        bestpath:
          as_path:
            confed: True
            ignore: True
          compare_routerid: True
          med:
            confed: True
            missing_as_worst: True
    state: replaced

#
# After state:
# ------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
# timers 60 180
#!
#router bgp 11 vrf VrfCheck2
# router-id 10.2.2.33
# log-neighbor-changes
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
# timers 60 180
#!
#router bgp 4
# router-id 10.2.2.44
# log-neighbor-changes
# bestpath as-path confed
# bestpath compare-routerid
# timers 60 180
#!

# Using overridden
#
# Before state:
# -------------
#
#!
#router bgp 10 vrf VrfCheck1
# router-id 10.2.2.32
# log-neighbor-changes
# timers 60 180
#!
#router bgp 4
# router-id 10.2.2.4
# max-med on-startup 667 7878
# bestpath as-path ignore
# bestpath as-path confed
# bestpath med missing-as-worst confed
# bestpath compare-routerid
# timers 20 30
#!
#

- name: Override device configuration of global BGP with provided configuration
  dellemc.enterprise_sonic.sonic_bgp:
    config:
      - bgp_as: 4
        router_id: 10.2.2.44
        log_neighbor_changes: True
        bestpath:
          as_path:
            confed: True
          compare_routerid: True
      - bgp_as: 11
        vrf_name: 'VrfCheck2'
        router_id: 10.2.2.33
        log_neighbor_changes: True
        bestpath:
          as_path:
            confed: True
            ignore: True
          compare_routerid: True
        timers:
          holdtime: 90
          keepalive_interval: 30
    state: overridden

#
# After state:
# ------------
#
#!
#router bgp 11 vrf VrfCheck2
# router-id 10.2.2.33
# log-neighbor-changes
# bestpath as-path ignore
# bestpath as-path confed
# bestpath compare-routerid
# timers 30 90
#!
#router bgp 4
# router-id 10.2.2.44
# log-neighbor-changes
# bestpath as-path confed
# bestpath compare-routerid
# timers 60 180
#!
```

## [Return Values](sonic_bgp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Dhivya P (@dhivayp)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
