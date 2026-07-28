---
collection: ansible
version: "6"
title: "community.network.ce_netstream_global module – Manages global parameters of NetStream on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_netstream_global_module.html
fetched_at: 2026-07-27T17:17:43+00:00
---
# community.network.ce_netstream_global module – Manages global parameters of NetStream on HUAWEI CloudEngine switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.ce_netstream_global`.

- [Synopsis](ce_netstream_global_module.md#synopsis)
- [Parameters](ce_netstream_global_module.md#parameters)
- [Notes](ce_netstream_global_module.md#notes)
- [Examples](ce_netstream_global_module.md#examples)
- [Return Values](ce_netstream_global_module.md#return-values)

## [Synopsis](ce_netstream_global_module.md#id1)

- Manages global parameters of NetStream on HUAWEI CloudEngine switches.

## [Parameters](ce_netstream_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **index_switch**  string | Specifies the netstream index-switch.  Choices:   - `"16"` ← (default) - `"32"` |
| **interface**  string / required | Netstream global interface. |
| **sampler_direction**  string | Specifies the netstream sampler direction.  Choices:   - `"inbound"` - `"outbound"` |
| **sampler_interval**  string | Specifies the netstream sampler interval, length is 1 - 65535. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **statistics_direction**  string | Specifies the netstream statistic direction.  Choices:   - `"inbound"` - `"outbound"` |
| **statistics_record**  string | Specifies the flexible netstream statistic record, length is 1 - 32. |
| **type**  string | Specifies the type of netstream global.  Choices:   - `"ip"` ← (default) - `"vxlan"` |

## [Notes](ce_netstream_global_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_netstream_global_module.md#id4)

```yaml+jinja
- name: Netstream global module test
  hosts: cloudengine
  connection: local
  gather_facts: no

  tasks:

  - name: Configure a netstream sampler at interface 10ge1/0/2, direction is outbound,interval is 30.
    community.network.ce_netstream_global:
      interface: 10ge1/0/2
      type: ip
      sampler_interval: 30
      sampler_direction: outbound
      state: present
  - name: Configure a netstream flexible statistic at interface 10ge1/0/2, record is test1, type is ip.
    community.network.ce_netstream_global:
      type: ip
      interface: 10ge1/0/2
      statistics_record: test1
  - name: Set the vxlan index-switch to 32.
    community.network.ce_netstream_global:
      type: vxlan
      interface: all
      index_switch: 32
```

## [Return Values](ce_netstream_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  Returned: verbose mode  Sample: `{"flexible_statistic": [{"interface": "10ge1/0/2", "statistics_record": [], "type": "ip"}, {"interface": "10ge1/0/2", "statistics_record": ["test"], "type": "vxlan"}], "index-switch": [{"index-switch": "16", "type": "ip"}, {"index-switch": "16", "type": "vxlan"}], "sampler": [{"interface": "all", "sampler_direction": "null", "sampler_interval": "null"}], "statistic": [{"interface": "10ge1/0/2", "statistics_direction": [], "type": "null"}]}` |
| **existing**  dictionary | k/v pairs of existing configuration  Returned: verbose mode  Sample: `{"flexible_statistic": [{"interface": "10ge1/0/2", "statistics_record": [], "type": "ip"}, {"interface": "10ge1/0/2", "statistics_record": [], "type": "vxlan"}], "index-switch": [{"index-switch": "16", "type": "ip"}, {"index-switch": "16", "type": "vxlan"}], "ip_record": ["test", "test1"], "sampler": [{"interface": "all", "sampler_direction": "null", "sampler_interval": "null"}], "statistic": [{"interface": "10ge1/0/2", "statistics_direction": [], "type": "null"}], "vxlan_record": ["test"]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: verbose mode  Sample: `{"index_switch": "16", "interface": "10ge1/0/2", "state": "present", "statistics_record": "test", "type": "vxlan"}` |
| **updates**  list / elements=string | commands sent to the device  Returned: always  Sample: `["interface 10ge1/0/2", "netstream record test vxlan inner-ip"]` |

### Authors

- YangYang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
