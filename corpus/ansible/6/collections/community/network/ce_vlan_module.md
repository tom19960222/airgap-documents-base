---
collection: ansible
version: "6"
title: "community.network.ce_vlan module – Manages VLAN resources and attributes on Huawei CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_vlan_module.html
fetched_at: 2026-07-27T17:17:56+00:00
---
# community.network.ce_vlan module – Manages VLAN resources and attributes on Huawei CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_vlan`.

- [Synopsis](ce_vlan_module.md#synopsis)
- [Parameters](ce_vlan_module.md#parameters)
- [Notes](ce_vlan_module.md#notes)
- [Examples](ce_vlan_module.md#examples)
- [Return Values](ce_vlan_module.md#return-values)

## [Synopsis](ce_vlan_module.md#id1)

- Manages VLAN configurations on Huawei CloudEngine switches.

## [Parameters](ce_vlan_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Specify VLAN description, minimum of 1 character, maximum of 80 characters. |
| **name**  string | Name of VLAN, minimum of 1 character, maximum of 31 characters. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vlan_id**  string | Single VLAN ID, in the range from 1 to 4094. |
| **vlan_range**  string | Range of VLANs such as `2-10` or `2,5,10-15`, etc. |

## [Notes](ce_vlan_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_vlan_module.md#id4)

```yaml+jinja
- name: Vlan module test
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

  - name: Ensure a range of VLANs are not present on the switch
    community.network.ce_vlan:
      vlan_range: "2-10,20,50,55-60,100-150"
      state: absent
      provider: "{{ cli }}"

  - name: Ensure VLAN 50 exists with the name WEB
    community.network.ce_vlan:
      vlan_id: 50
      name: WEB
      state: absent
      provider: "{{ cli }}"

  - name: Ensure VLAN is NOT on the device
    community.network.ce_vlan:
      vlan_id: 50
      state: absent
      provider: "{{ cli }}"
```

## [Return Values](ce_vlan_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of the VLAN after executing module or null when using vlan_range  Returned: always  Sample: `{"description": "vlan for app", "name": "VLAN_APP", "vlan_id": "20"}` |
| **end_state_vlans_list**  list / elements=string | list of VLANs after the module is executed  Returned: always  Sample: `["1", "2", "3", "4", "5", "20", "100"]` |
| **existing**  dictionary | k/v pairs of existing vlan or null when using vlan_range  Returned: always  Sample: `{"description": "", "name": "VLAN_APP", "vlan_id": "20"}` |
| **existing_vlans_list**  list / elements=string | list of existing VLANs on the switch prior to making changes  Returned: always  Sample: `["1", "2", "3", "4", "5", "20"]` |
| **proposed**  dictionary | k/v pairs of parameters passed into module (does not include vlan_id or vlan_range)  Returned: always  Sample: `{"description": "vlan for app", "name": "VLAN_APP", "vlan_id": "20"}` |
| **proposed_vlans_list**  list / elements=string | list of VLANs being proposed  Returned: always  Sample: `["100"]` |
| **updates**  list / elements=string | command string sent to the device  Returned: always  Sample: `["vlan 20", "name VLAN20"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
