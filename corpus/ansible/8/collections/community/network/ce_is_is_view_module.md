---
collection: ansible
version: "8"
title: "community.network.ce_is_is_view module – Manages isis view configuration on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_is_is_view_module.html
fetched_at: 2026-07-28T01:55:34+00:00
---
# community.network.ce_is_is_view module – Manages isis view configuration on HUAWEI CloudEngine devices.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_is_is_view`.

New in community.network 0.2.0

- [Synopsis](ce_is_is_view_module.md#synopsis)
- [Parameters](ce_is_is_view_module.md#parameters)
- [Notes](ce_is_is_view_module.md#notes)
- [Examples](ce_is_is_view_module.md#examples)
- [Return Values](ce_is_is_view_module.md#return-values)

## [Synopsis](ce_is_is_view_module.md#id1)

- Manages isis process id, creates a isis instance id or deletes a process id on HUAWEI CloudEngine devices.

Aliases: network.cloudengine.ce_is_is_view

## [Parameters](ce_is_is_view_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aclnum_or_name**  string | Specifies the acl number or name for isis. |
| **allow_filter**  boolean | Specifies the alow filter or not.  **Choices:**   - `false` - `true` |
| **allow_up_down**  boolean | Specifies the alow up or down.  **Choices:**   - `false` - `true` |
| **autocostenable**  boolean | Specifies the alow auto cost enable.  **Choices:**   - `false` - `true` |
| **autocostenablecompatible**  boolean | Specifies the alow auto cost enable compatible.  **Choices:**   - `false` - `true` |
| **avoid_learning**  boolean | Specifies the alow avoid learning.  **Choices:**   - `false` - `true` |
| **bfd_min_rx**  integer | Specifies the bfd min received package. |
| **bfd_min_tx**  integer | Specifies the bfd min sent package. |
| **bfd_multiplier_num**  integer | Specifies the bfd multiplier number. |
| **cost**  integer | Specifies the bfd cost. |
| **cost_type**  string | Specifies the cost type.  **Choices:**   - `"external"` - `"internal"` |
| **coststyle**  string | Specifies the cost style.  **Choices:**   - `"narrow"` - `"wide"` - `"transition"` - `"ntransition"` - `"wtransition"` |
| **defaultmode**  string | Specifies the default mode.  **Choices:**   - `"always"` - `"matchDefault"` - `"matchAny"` |
| **description**  string | Specifies description of isis. |
| **enablelevel1tolevel2**  boolean | Enable level1 to level2.  **Choices:**   - `false` - `true` |
| **export_aclnumorname**  string | Specifies export acl number or name. |
| **export_ipprefix**  string | Specifies export ip prefix. |
| **export_policytype**  string | Specifies the default mode.  **Choices:**   - `"aclNumOrName"` - `"ipPrefix"` - `"routePolicy"` |
| **export_processid**  integer | Specifies export process id. |
| **export_protocol**  string | Specifies the export router protocol.  **Choices:**   - `"direct"` - `"ospf"` - `"isis"` - `"static"` - `"rip"` - `"bgp"` - `"ospfv3"` - `"all"` |
| **export_routepolicyname**  string | Specifies export route policy name. |
| **import_aclnumorname**  string | Specifies import acl number or name. |
| **import_cost**  integer | Specifies import cost. |
| **import_ipprefix**  string | Specifies import ip prefix. |
| **import_route_policy**  string | Specifies import route policy. |
| **import_routepolicy_name**  string | Specifies import route policy name. |
| **import_routepolicyname**  string | Specifies import route policy name. |
| **import_tag**  integer | Specifies import tag. |
| **impotr_leveltype**  string | Specifies the export router protocol.  **Choices:**   - `"level_1"` - `"level_2"` - `"level_1_2"` |
| **inheritcost**  boolean | Enable inherit cost.  **Choices:**   - `false` - `true` |
| **instance_id**  integer | Specifies instance id. |
| **ip_address**  string | Specifies ip address. |
| **ip_prefix_name**  string | Specifies ip prefix name. |
| **islevel**  string | Specifies the isis level.  **Choices:**   - `"level_1"` - `"level_2"` - `"level_1_2"` |
| **level_type**  string | Specifies the isis level type.  **Choices:**   - `"level_1"` - `"level_2"` - `"level_1_2"` |
| **max_load**  integer | Specifies route max load. |
| **mode_routepolicyname**  string | Specifies the mode of route polic yname. |
| **mode_tag**  integer | Specifies the tag of mode. |
| **netentity**  string | Specifies the netentity. |
| **penetration_direct**  string | Specifies the penetration direct.  **Choices:**   - `"level2-level1"` - `"level1-level2"` |
| **permitibgp**  boolean | Specifies the permitibgp.  **Choices:**   - `false` - `true` |
| **preference_value**  integer | Specifies the preference value. |
| **processid**  integer | Specifies the process id. |
| **protocol**  string | Specifies the protocol.  **Choices:**   - `"direct"` - `"ospf"` - `"isis"` - `"static"` - `"rip"` - `"bgp"` - `"ospfv3"` - `"all"` |
| **relaxspfLimit**  boolean | Specifies enable the relax spf limit.  **Choices:**   - `false` - `true` |
| **route_policy_name**  string | Specifies the route policy name. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **stdbandwidth**  integer | Specifies the std band width. |
| **stdlevel1cost**  integer | Specifies the std level1 cost. |
| **stdlevel2cost**  integer | Specifies the std level2 cost. |
| **tag**  integer | Specifies the isis tag. |
| **weight**  integer | Specifies the isis weight. |

## [Notes](ce_is_is_view_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - This module works with connection `netconf`.

## [Examples](ce_is_is_view_module.md#id4)

```yaml+jinja
- name: Set isis description
  community.network.ce_is_is_view:
    instance_id: 3
    description: abcdeggfs
    state: present

- name: Set isis islevel
  community.network.ce_is_is_view:
    instance_id: 3
    islevel: level_1
    state: present
- name: Set isis coststyle
  community.network.ce_is_is_view:
    instance_id: 3
    coststyle: narrow
    state: present

- name: Set isis stdlevel1cost
  community.network.ce_is_is_view:
    instance_id: 3
    stdlevel1cost: 63
    state: present

- name: Set isis stdlevel2cost
  community.network.ce_is_is_view:
    instance_id: 3
    stdlevel2cost: 63
    state: present

- name: Set isis stdbandwidth
  community.network.ce_is_is_view:
    instance_id: 3
    stdbandwidth: 1
    state: present
```

## [Return Values](ce_is_is_view_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** always  **Sample:** `{"session": {"addrType": "IPV4", "createType": "SESS_STATIC", "destAddr": null, "outIfName": "10GE1/0/1", "sessName": "bfd_l2link", "srcAddr": null, "useDefaultIp": "true", "vrfName": null}}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** always  **Sample:** `{"session": {}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"state": "present"}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["bfd bfd_l2link bind peer-ip default-ip interface 10ge1/0/1"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
