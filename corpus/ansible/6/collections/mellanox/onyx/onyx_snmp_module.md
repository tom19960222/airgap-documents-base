---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_snmp module – Manages SNMP general configurations on Mellanox ONYX network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_snmp_module.html
fetched_at: 2026-07-27T17:55:40+00:00
---
# mellanox.onyx.onyx_snmp module – Manages SNMP general configurations on Mellanox ONYX network devices

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_snmp`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_snmp_module.md#synopsis)
- [Parameters](onyx_snmp_module.md#parameters)
- [Examples](onyx_snmp_module.md#examples)
- [Return Values](onyx_snmp_module.md#return-values)

## [Synopsis](onyx_snmp_module.md#id1)

- This module provides declarative management of SNMP on Mellanox ONYX network devices.

## [Parameters](onyx_snmp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **communities_enabled**  boolean | Enables/Disables community-based authentication on the system.  Choices:   - `false` - `true` |
| **contact_name**  string | Sets the SNMP contact name. |
| **engine_id_reset**  boolean | Sets SNMPv3 engineID to node unique value.  Choices:   - `false` - `true` |
| **location**  string | Sets the SNMP location. |
| **multi_communities_enabled**  boolean | Enables/Disables multiple communities to be configured.  Choices:   - `false` - `true` |
| **notify_community**  string | Sets the default community for SNMP v1 and v2c notifications sent to hosts which do not have a community override set. |
| **notify_enabled**  boolean | Enables/Disables sending of SNMP notifications (traps and informs) from thee system.  Choices:   - `false` - `true` |
| **notify_event**  string | Specifys which events will be sent as SNMP notifications.  Choices:   - `"asic-chip-down"` - `"dcbx-pfc-port-oper-state-trap"` - `"insufficient-power"` - `"mstp-new-bridge-root"` - `"ospf-lsdb-approaching-overflow"` - `"sm-stop"` - `"user-logout"` - `"cli-line-executed"` - `"dcbx-pfc-port-peer-state-trap"` - `"interface-down"` - `"mstp-new-root-port"` - `"ospf-lsdb-overflow"` - `"snmp-authtrap"` - `"xstp-new-root-bridge"` - `"cpu-util-high"` - `"disk-io-high"` - `"interface-up"` - `"mstp-topology-change"` - `"ospf-nbr-state-change"` - `"temperature-too-high"` - `"xstp-root-port-change"` - `"dcbx-ets-module-state-change"` - `"disk-space-low"` - `"internal-bus-error"` - `"netusage-high"` - `"paging-high"` - `"topology_change"` - `"xstp-topology-change"` - `"dcbx-ets-port-admin-state-trap"` - `"entity-state-change"` - `"internal-link-speed-mismatch"` - `"new_root"` - `"power-redundancy-mismatch"` - `"unexpected-cluster-join"` - `"dcbx-ets-port-oper-state-trap"` - `"expected-shutdown"` - `"liveness-failure"` - `"ospf-auth-fail"` - `"process-crash"` - `"unexpected-cluster-leave"` - `"dcbx-ets-port-peer-state-trap"` - `"health-module-status"` - `"low-power"` - `"ospf-config-error"` - `"process-exit"` - `"unexpected-cluster-size"` - `"dcbx-pfc-module-state-change"` - `"insufficient-fans"` - `"low-power-recover"` - `"ospf-if-rx-bad-packet"` - `"sm-restart"` - `"unexpected-shutdown"` - `"dcbx-pfc-port-admin-state-trap"` - `"insufficient-fans-recover"` - `"memusage-high"` - `"ospf-if-state-change"` - `"sm-start"` - `"user-login"` |
| **notify_port**  string | Sets the default port to which notifications are sent. |
| **notify_send_test**  string | Sends a test notification.  Choices:   - `"yes"` - `"no"` |
| **snmp_communities**  list / elements=string | List of snmp communities |
| **community_name**  string / required | Configures snmp community name. |
| **community_type**  string | Add this community as either a read-only or read-write community.  Choices:   - `"read-only"` - `"read-write"` |
| **state**  string | Used to decide if you want to delete the given snmp community or not  Choices:   - `"present"` - `"absent"` |
| **snmp_permissions**  list / elements=string | Allow SNMPSET requests for items in a MIB. |
| **permission_type**  string | Configures the request type.  Choices:   - `"MELLANOX-CONFIG-DB-MIB"` - `"MELLANOX-EFM-MIB"` - `"MELLANOX-POWER-CYCLE"` - `"MELLANOX-SW-UPDATE"` - `"RFC1213-MIB"` |
| **state_enabled**  boolean / required | Enables/Disables the request.  Choices:   - `false` - `true` |
| **state_enabled**  boolean | Enables/Disables the state of the SNMP configuration.  Choices:   - `false` - `true` |

## [Examples](onyx_snmp_module.md#id3)

```yaml+jinja
- name: Configure SNMP
  onyx_snmp:
    state_enabled: yes
    contact_name: sara
    location: Nablus
    communities_enabled: no
    multi_communities_enabled: no
    notify_enabled: yes
    notify_port: 1
    notify_community: community_1
    notify_send_test: yes
    notify_event: temperature-too-high
    snmp_communities:
        - community_name: public
          community_type: read-only
          state: absent
    snmp_permissions:
        - state_enabled: yes
          permission_type: MELLANOX-CONFIG-DB-MIB
```

## [Return Values](onyx_snmp_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always.  Sample: `["snmp-server enable", "no snmp-server enable", "snmp-server location <location_name>", "snmp-server contact <contact_name>", "snmp-server enable communities", "no snmp-server enable communities", "snmp-server enable mult-communities", "no snmp-server enable mult-communities", "snmp-server enable notify", "snmp-server notify port <port_number>", "snmp-server notify community <community_name>", "snmp-server notify send-test", "snmp-server notify event <event_name>", "snmp-server enable set-permission <permission_type>", "no snmp-server enable set-permission <permission_type>", "snmp-server community <community_name> <community_type>", "no snmp-server community <community_name>.", "snmp-server engineID reset."]` |

### Authors

- Sara-Touqan (@sarato)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
