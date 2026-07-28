---
collection: ansible
version: "8"
title: "community.network.ce_dldp_interface module – Manages interface DLDP configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_dldp_interface_module.html
fetched_at: 2026-07-28T01:55:21+00:00
---
# community.network.ce_dldp_interface module – Manages interface DLDP configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_dldp_interface`.

- [Synopsis](ce_dldp_interface_module.md#synopsis)
- [Parameters](ce_dldp_interface_module.md#parameters)
- [Notes](ce_dldp_interface_module.md#notes)
- [Examples](ce_dldp_interface_module.md#examples)
- [Return Values](ce_dldp_interface_module.md#return-values)

## [Synopsis](ce_dldp_interface_module.md#id1)

- Manages interface DLDP configuration on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_dldp_interface

## [Parameters](ce_dldp_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **enable**  string | Set interface DLDP enable state.  **Choices:**   - `"enable"` - `"disable"` |
| **interface**  string / required | Must be fully qualified interface name, i.e. GE1/0/1, 10GE1/0/1, 40GE1/0/22, 100GE1/0/1. |
| **local_mac**  string | Set the source MAC address for DLDP packets sent in the DLDP-compatible mode. The value of MAC address is in H-H-H format. H contains 1 to 4 hexadecimal digits. |
| **mode_enable**  string | Set DLDP compatible-mode enable state.  **Choices:**   - `"enable"` - `"disable"` |
| **reset**  string | Specify whether reseting interface DLDP state.  **Choices:**   - `"enable"` - `"disable"` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_dldp_interface_module.md#id3)

> **Note:**
>
> - If `state=present, enable=disable`, interface DLDP enable will be turned off and related interface DLDP configuration will be cleared.
> - If `state=absent`, only local_mac is supported to configure.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_dldp_interface_module.md#id4)

```yaml+jinja
- name: DLDP interface test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: "Configure interface DLDP enable state and ensure global dldp enable is turned on"
    community.network.ce_dldp_interface:
      interface: 40GE2/0/1
      enable: enable
      provider: "{{ cli }}"

  - name: "Configuire interface DLDP compatible-mode enable state  and ensure interface DLDP state is already enabled"
    community.network.ce_dldp_interface:
      interface: 40GE2/0/1
      enable: enable
      mode_enable: enable
      provider: "{{ cli }}"

  - name: "Configuire the source MAC address for DLDP packets sent in the DLDP-compatible mode  and
           ensure interface DLDP state and compatible-mode enable state  is already enabled"
    community.network.ce_dldp_interface:
      interface: 40GE2/0/1
      enable: enable
      mode_enable: enable
      local_mac: aa-aa-aa
      provider: "{{ cli }}"

  - name: "Reset DLDP state of specified interface and ensure interface DLDP state is already enabled"
    community.network.ce_dldp_interface:
      interface: 40GE2/0/1
      enable: enable
      reset: enable
      provider: "{{ cli }}"

  - name: "Unconfigure interface DLDP local mac address when C(state=absent)"
    community.network.ce_dldp_interface:
      interface: 40GE2/0/1
      state: absent
      local_mac: aa-aa-aa
      provider: "{{ cli }}"
```

## [Return Values](ce_dldp_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of interface DLDP configuration after module execution  **Returned:** always  **Sample:** `{"enable": "enable", "interface": "40GE2/0/22", "local_mac": "00aa-00aa-00aa", "mode_enable": "enable", "reset": "enable"}` |
| **existing**  dictionary | k/v pairs of existing interface DLDP configuration  **Returned:** always  **Sample:** `{"enable": "disable", "interface": "40GE2/0/22", "local_mac": null, "mode_enable": null, "reset": "disable"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"enable": "enalbe", "interface": "40GE2/0/22", "local_mac": "aa-aa-aa", "mode_enable": "enable", "reset": "enable"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["dldp enable", "dldp compatible-mode enable", "dldp compatible-mode local-mac aa-aa-aa", "dldp reset"]` |

### Authors

- Zhou Zhijin (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
