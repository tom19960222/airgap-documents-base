---
collection: ansible
version: "8"
title: "community.network.ce_snmp_location module – Manages SNMP location configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_snmp_location_module.html
fetched_at: 2026-07-28T01:55:51+00:00
---
# community.network.ce_snmp_location module – Manages SNMP location configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_snmp_location`.

- [Synopsis](ce_snmp_location_module.md#synopsis)
- [Parameters](ce_snmp_location_module.md#parameters)
- [Notes](ce_snmp_location_module.md#notes)
- [Examples](ce_snmp_location_module.md#examples)
- [Return Values](ce_snmp_location_module.md#return-values)

## [Synopsis](ce_snmp_location_module.md#id1)

- Manages SNMP location configurations on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_snmp_location

## [Parameters](ce_snmp_location_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **location**  string / required | Location information. |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_snmp_location_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_snmp_location_module.md#id4)

```yaml+jinja
- name: CloudEngine snmp location test
  hosts: cloudengine
  connection: local
  gather_facts: false

  tasks:

  - name: "Config SNMP location"
    community.network.ce_snmp_location:
      state: present
      location: nanjing China

  - name: "Remove SNMP location"
    community.network.ce_snmp_location:
      state: absent
      location: nanjing China
```

## [Return Values](ce_snmp_location_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  **Returned:** always  **Sample:** `{"location": "nanjing China"}` |
| **existing**  dictionary | k/v pairs of existing aaa server  **Returned:** always  **Sample:** `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"location": "nanjing China", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["snmp-agent sys-info location nanjing China"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
