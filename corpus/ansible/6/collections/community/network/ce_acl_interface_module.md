---
collection: ansible
version: "6"
title: "community.network.ce_acl_interface module – Manages applying ACLs to interfaces on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_acl_interface_module.html
fetched_at: 2026-07-27T17:17:15+00:00
---
# community.network.ce_acl_interface module – Manages applying ACLs to interfaces on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_acl_interface`.

- [Synopsis](ce_acl_interface_module.md#synopsis)
- [Parameters](ce_acl_interface_module.md#parameters)
- [Notes](ce_acl_interface_module.md#notes)
- [Examples](ce_acl_interface_module.md#examples)
- [Return Values](ce_acl_interface_module.md#return-values)

## [Synopsis](ce_acl_interface_module.md#id1)

- Manages applying ACLs to interfaces on HUAWEI CloudEngine switches.

## [Parameters](ce_acl_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **acl_name**  string / required | ACL number or name. For a numbered rule group, the value ranging from 2000 to 4999. For a named rule group, the value is a string of 1 to 32 case-sensitive characters starting with a letter, spaces not supported. |
| **direction**  string / required | Direction ACL to be applied in on the interface.  Choices:   - `"inbound"` - `"outbound"` |
| **interface**  string / required | Interface name. Only support interface full name, such as “40GE2/0/1”. |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_acl_interface_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_acl_interface_module.md#id4)

```yaml+jinja
- name: CloudEngine acl interface test
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

  - name: "Apply acl to interface"
    community.network.ce_acl_interface:
      state: present
      acl_name: 2000
      interface: 40GE1/0/1
      direction: outbound
      provider: "{{ cli }}"

  - name: "Undo acl from interface"
    community.network.ce_acl_interface:
      state: absent
      acl_name: 2000
      interface: 40GE1/0/1
      direction: outbound
      provider: "{{ cli }}"
```

## [Return Values](ce_acl_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"acl interface": ["traffic-filter acl lb inbound", "traffic-filter acl 2000 outbound"]}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"acl interface": "traffic-filter acl lb inbound"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"acl_name": "2000", "direction": "outbound", "interface": "40GE2/0/1", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["interface 40ge2/0/1", "traffic-filter acl 2000 outbound"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
