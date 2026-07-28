---
collection: ansible
version: "6"
title: "community.network.ce_interface module – Manages physical attributes of interfaces on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_interface_module.html
fetched_at: 2026-07-27T17:17:30+00:00
---
# community.network.ce_interface module – Manages physical attributes of interfaces on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_interface`.

- [Synopsis](ce_interface_module.md#synopsis)
- [Parameters](ce_interface_module.md#parameters)
- [Notes](ce_interface_module.md#notes)
- [Examples](ce_interface_module.md#examples)
- [Return Values](ce_interface_module.md#return-values)

## [Synopsis](ce_interface_module.md#id1)

- Manages physical attributes of interfaces on HUAWEI CloudEngine switches.

## [Parameters](ce_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string | Specifies the interface management status. The value is an enumerated type. up, An interface is in the administrative Up state. down, An interface is in the administrative Down state.  Choices:   - `"up"` - `"down"` |
| **description**  string | Specifies an interface description. The value is a string of 1 to 242 case-sensitive characters, spaces supported but question marks (?) not supported. |
| **interface**  string | Full name of interface, i.e. 40GE1/0/10, Tunnel1. |
| **interface_type**  string | Interface type to be configured from the device.  Choices:   - `"ge"` - `"10ge"` - `"25ge"` - `"4x10ge"` - `"40ge"` - `"100ge"` - `"vlanif"` - `"loopback"` - `"meth"` - `"eth-trunk"` - `"nve"` - `"tunnel"` - `"ethernet"` - `"fcoe-port"` - `"fabric-port"` - `"stack-port"` - `"null"` |
| **l2sub**  boolean | Specifies whether the interface is a Layer 2 sub-interface.  Choices:   - `false` ← (default) - `true` |
| **mode**  string | Manage Layer 2 or Layer 3 state of the interface.  Choices:   - `"layer2"` - `"layer3"` |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` - `"default"` |

## [Notes](ce_interface_module.md#id3)

> **Note:**
>
> - This module is also used to create logical interfaces such as vlanif and loopbacks.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_interface_module.md#id4)

```yaml+jinja
- name: Interface module test
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
  - name: Ensure an interface is a Layer 3 port and that it has the proper description
    community.network.ce_interface:
      interface: 10GE1/0/22
      description: 'Configured by Ansible'
      mode: layer3
      provider: '{{ cli }}'

  - name: Admin down an interface
    community.network.ce_interface:
      interface: 10GE1/0/22
      admin_state: down
      provider: '{{ cli }}'

  - name: Remove all tunnel interfaces
    community.network.ce_interface:
      interface_type: tunnel
      state: absent
      provider: '{{ cli }}'

  - name: Remove all logical interfaces
    community.network.ce_interface:
      interface_type: '{{ item }}'
      state: absent
      provider: '{{ cli }}'
    with_items:
      - loopback
      - eth-trunk
      - nve

  - name: Admin up all 10GE interfaces
    community.network.ce_interface:
      interface_type: 10GE
      admin_state: up
      provider: '{{ cli }}'
```

## [Return Values](ce_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of switchport after module execution  Returned: always  Sample: `{"admin_state": "down", "description": "None", "interface": "10GE1/0/10", "mode": "layer2"}` |
| **existing**  dictionary | k/v pairs of existing switchport  Returned: always  Sample: `{"admin_state": "up", "description": "None", "interface": "10GE1/0/10", "mode": "layer2"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"admin_state": "down", "interface": "10GE1/0/10"}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["interface 10GE1/0/10", "shutdown"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
