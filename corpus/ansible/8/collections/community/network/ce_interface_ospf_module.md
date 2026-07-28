---
collection: ansible
version: "8"
title: "community.network.ce_interface_ospf module – Manages configuration of an OSPF interface instanceon HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_interface_ospf_module.html
fetched_at: 2026-07-28T01:55:31+00:00
---
# community.network.ce_interface_ospf module – Manages configuration of an OSPF interface instanceon HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_interface_ospf`.

- [Synopsis](ce_interface_ospf_module.md#synopsis)
- [Parameters](ce_interface_ospf_module.md#parameters)
- [Notes](ce_interface_ospf_module.md#notes)
- [Examples](ce_interface_ospf_module.md#examples)
- [Return Values](ce_interface_ospf_module.md#return-values)

## [Synopsis](ce_interface_ospf_module.md#id1)

- Manages configuration of an OSPF interface instanceon HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_interface_ospf

## [Parameters](ce_interface_ospf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **area**  string / required | Ospf area associated with this ospf process. Valid values are a string, formatted as an IP address (i.e. “0.0.0.0”) or as an integer between 1 and 4294967295. |
| **auth_key_id**  string | Authentication key id when `auth_mode` is ‘hmac-sha256’, ‘md5’ or ‘hmac-md5. Valid value is an integer is in the range from 1 to 255. |
| **auth_mode**  string | Specifies the authentication type.  **Choices:**   - `"none"` - `"null"` - `"hmac-sha256"` - `"md5"` - `"hmac-md5"` - `"simple"` |
| **auth_text_md5**  string | Specifies a password for MD5, HMAC-MD5, or HMAC-SHA256 authentication. The value is a string of 1 to 255 case-sensitive characters, spaces not supported. |
| **auth_text_simple**  string | Specifies a password for simple authentication. The value is a string of 1 to 8 characters. |
| **cost**  string | The cost associated with this interface. Valid values are an integer in the range from 1 to 65535. |
| **dead_interval**  string | Time interval an ospf neighbor waits for a hello packet before tearing down adjacencies. Valid values are an integer in the range from 1 to 235926000. |
| **hello_interval**  string | Time between sending successive hello packets. Valid values are an integer in the range from 1 to 65535. |
| **interface**  string / required | Full name of interface, i.e. 40GE1/0/10. |
| **process_id**  string / required | Specifies a process ID. The value is an integer ranging from 1 to 4294967295. |
| **silent_interface**  boolean | Setting to true will prevent this interface from receiving HELLO packets. Valid values are ‘true’ and ‘false’.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_interface_ospf_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_interface_ospf_module.md#id4)

```yaml+jinja
- name: Eth_trunk module test
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
  - name: Enables OSPF and sets the cost on an interface
    community.network.ce_interface_ospf:
      interface: 10GE1/0/30
      process_id: 1
      area: 100
      cost: 100
      provider: '{{ cli }}'

  - name: Sets the dead interval of the OSPF neighbor
    community.network.ce_interface_ospf:
      interface: 10GE1/0/30
      process_id: 1
      area: 100
      dead_interval: 100
      provider: '{{ cli }}'

  - name: Sets the interval for sending Hello packets on an interface
    community.network.ce_interface_ospf:
      interface: 10GE1/0/30
      process_id: 1
      area: 100
      hello_interval: 2
      provider: '{{ cli }}'

  - name: Disables an interface from receiving and sending OSPF packets
    community.network.ce_interface_ospf:
      interface: 10GE1/0/30
      process_id: 1
      area: 100
      silent_interface: true
      provider: '{{ cli }}'
```

## [Return Values](ce_interface_ospf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"area": "0.0.0.100", "auth_mode": "none", "cost": "100", "dead_interval": "40", "hello_interval": "10", "interface": "10GE1/0/30", "process_id": "1", "silent_interface": "false"}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"area": "0.0.0.100", "process_id": "1"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"area": "0.0.0.100", "cost": "100", "interface": "10GE1/0/30", "process_id": "1"}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["interface 10GE1/0/30", "ospf enable 1 area 0.0.0.100", "ospf cost 100"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
