---
collection: ansible
version: "6"
title: "community.network.ce_snmp_contact module – Manages SNMP contact configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_snmp_contact_module.html
fetched_at: 2026-07-27T17:17:49+00:00
---
# community.network.ce_snmp_contact module – Manages SNMP contact configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_snmp_contact`.

- [Synopsis](ce_snmp_contact_module.md#synopsis)
- [Parameters](ce_snmp_contact_module.md#parameters)
- [Notes](ce_snmp_contact_module.md#notes)
- [Examples](ce_snmp_contact_module.md#examples)
- [Return Values](ce_snmp_contact_module.md#return-values)

## [Synopsis](ce_snmp_contact_module.md#id1)

- Manages SNMP contact configurations on HUAWEI CloudEngine switches.

## [Parameters](ce_snmp_contact_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **contact**  string / required | Contact information. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_snmp_contact_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_snmp_contact_module.md#id4)

```yaml+jinja
- name: CloudEngine snmp contact test
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

  - name: "Config SNMP contact"
    community.network.ce_snmp_contact:
      state: present
      contact: call Operator at 010-99999999
      provider: "{{ cli }}"

  - name: "Undo SNMP contact"
    community.network.ce_snmp_contact:
      state: absent
      contact: call Operator at 010-99999999
      provider: "{{ cli }}"
```

## [Return Values](ce_snmp_contact_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"contact": "call Operator at 010-99999999"}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"contact": "call Operator at 010-99999999", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["snmp-agent sys-info contact call Operator at 010-99999999"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
