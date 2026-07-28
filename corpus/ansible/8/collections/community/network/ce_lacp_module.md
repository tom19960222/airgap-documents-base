---
collection: ansible
version: "8"
title: "community.network.ce_lacp module – Manages Eth-Trunk interfaces on HUAWEI CloudEngine switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_lacp_module.html
fetched_at: 2026-07-28T01:55:34+00:00
---
# community.network.ce_lacp module – Manages Eth-Trunk interfaces on HUAWEI CloudEngine switches

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
> To use it in a playbook, specify: `community.network.ce_lacp`.

New in community.network 0.2.0

- [Synopsis](ce_lacp_module.md#synopsis)
- [Parameters](ce_lacp_module.md#parameters)
- [Notes](ce_lacp_module.md#notes)
- [Examples](ce_lacp_module.md#examples)
- [Return Values](ce_lacp_module.md#return-values)

## [Synopsis](ce_lacp_module.md#id1)

- Manages Eth-Trunk specific configuration parameters on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_lacp

## [Parameters](ce_lacp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **collector_delay**  integer | Value of delay time in units of 10 microseconds. |
| **fast_timeout**  integer | When lacp timeout type is ‘Fast’, user-defined time can be a number(3~90). |
| **global_priority**  integer | Configure lacp priority on system-view. |
| **max_active_linknumber**  integer | Max active linknumber in link aggregation group. |
| **mixed_rate_link_enable**  boolean | Value of max active linknumber.  **Choices:**   - `false` - `true` |
| **mode**  string | Specifies the working mode of an Eth-Trunk interface.  **Choices:**   - `"Manual"` - `"Dynamic"` - `"Static"` |
| **port_id_extension_enable**  boolean | Enable the function of extending the LACP negotiation port number.  **Choices:**   - `false` - `true` |
| **preempt_delay**  integer | Value of preemption delay time. |
| **preempt_enable**  boolean | Specifies lacp preempt enable of Eth-Trunk lacp. The value is an boolean ‘true’ or ‘false’.  **Choices:**   - `false` - `true` |
| **priority**  integer | The priority of eth-trunk member interface. |
| **select**  string | Select priority or speed to preempt.  **Choices:**   - `"Speed"` - `"Prority"` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **state_flapping**  boolean | Lacp dampening state-flapping.  **Choices:**   - `false` - `true` |
| **system_id**  string | Link Aggregation Control Protocol System ID,interface Eth-Trunk View.  Formate ‘X-X-X’,X is hex(a,aa,aaa, or aaaa) |
| **timeout_type**  string | Lacp timeout type,that may be ‘Fast’ or ‘Slow’.  **Choices:**   - `"Slow"` - `"Fast"` |
| **trunk_id**  integer | Eth-Trunk interface number. The value is an integer. The value range depends on the assign forward eth-trunk mode command. When 256 is specified, the value ranges from 0 to 255. When 512 is specified, the value ranges from 0 to 511. When 1024 is specified, the value ranges from 0 to 1023. |
| **unexpected_mac_disable**  boolean | Lacp dampening unexpected-mac disable.  **Choices:**   - `false` - `true` |

## [Notes](ce_lacp_module.md#id3)

> **Note:**
>
> - `state=absent` removes the Eth-Trunk config and interface if it already exists. If members to be removed are not explicitly passed, all existing members (if any), are removed, and Eth-Trunk removed.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_lacp_module.md#id4)

```yaml+jinja
- name: Ensure Eth-Trunk100 is created, and set to mode lacp-static
  community.network.ce_lacp:
    trunk_id: 100
    mode: 'lacp-static'
    state: present
- name: Ensure Eth-Trunk100 is created, add two members, and set global priority to 1231
  community.network.ce_lacp:
    trunk_id: 100
    global_priority: 1231
    state: present
- name: Ensure Eth-Trunk100 is created, and set mode to Dynamic and configure other options
  community.network.ce_lacp:
    trunk_id: 100
    mode: Dynamic
    preempt_enable: True,
    state_flapping: True,
    port_id_extension_enable: True,
    unexpected_mac_disable: True,
    timeout_type: Fast,
    fast_timeout: 123,
    mixed_rate_link_enable: True,
    preempt_delay: 23,
    collector_delay: 33,
    state: present
```

## [Return Values](ce_lacp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | k/v pairs of Eth-Trunk info after module execution  **Returned:** always  **Sample:** `{"hash_type": "mac", "members_detail": [{"memberIfName": "10GE1/0/24", "memberIfState": "Down"}, {"memberIfName": "10GE1/0/25", "memberIfState": "Down"}], "min_links": "1", "mode": "lacp-static", "trunk_id": "100"}` |
| **existing**  dictionary | k/v pairs of existing Eth-Trunk  **Returned:** always  **Sample:** `{"hash_type": "mac", "members_detail": [{"memberIfName": "10GE1/0/25", "memberIfState": "Down"}], "min_links": "1", "mode": "manual", "trunk_id": "100"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"members": ["10GE1/0/24", "10GE1/0/25"], "mode": "lacp-static", "trunk_id": "100"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["interface Eth-Trunk 100", "mode lacp-static", "interface 10GE1/0/25", "eth-trunk 100"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
