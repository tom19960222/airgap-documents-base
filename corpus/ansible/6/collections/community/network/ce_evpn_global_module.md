---
collection: ansible
version: "6"
title: "community.network.ce_evpn_global module – Manages global configuration of EVPN on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_evpn_global_module.html
fetched_at: 2026-07-27T17:17:25+00:00
---
# community.network.ce_evpn_global module – Manages global configuration of EVPN on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_evpn_global`.

- [Synopsis](ce_evpn_global_module.md#synopsis)
- [Parameters](ce_evpn_global_module.md#parameters)
- [Notes](ce_evpn_global_module.md#notes)
- [Examples](ce_evpn_global_module.md#examples)
- [Return Values](ce_evpn_global_module.md#return-values)

## [Synopsis](ce_evpn_global_module.md#id1)

- Manages global configuration of EVPN on HUAWEI CloudEngine switches.

## [Parameters](ce_evpn_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **evpn_overlay_enable**  string / required | Configure EVPN as the VXLAN control plane.  Choices:   - `"enable"` - `"disable"` |

## [Notes](ce_evpn_global_module.md#id3)

> **Note:**
>
> - Before configuring evpn_overlay_enable=disable, delete other EVPN configurations.
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_evpn_global_module.md#id4)

```yaml+jinja
- name: Evpn global module test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: Configure EVPN as the VXLAN control plan
    community.network.ce_evpn_global:
      evpn_overlay_enable: enable
      provider: "{{ cli }}"

  - name: Undo EVPN as the VXLAN control plan
    community.network.ce_evpn_global:
      evpn_overlay_enable: disable
      provider: "{{ cli }}"
```

## [Return Values](ce_evpn_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of end attributes on the interface  Returned: always  Sample: `{"evpn_overlay_enable": "enable"}` |
| **existing**  dictionary | k/v pairs of existing attributes on the device  Returned: always  Sample: `{"evpn_overlay_enable": "disable"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"evpn_overlay_enable": "enable"}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["evpn-overlay enable"]` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
