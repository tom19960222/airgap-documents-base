---
collection: ansible
version: "8"
title: "community.network.ce_ip_interface module – Manages L3 attributes for IPv4 and IPv6 interfaces on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_ip_interface_module.html
fetched_at: 2026-07-28T01:55:31+00:00
---
# community.network.ce_ip_interface module – Manages L3 attributes for IPv4 and IPv6 interfaces on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_ip_interface`.

- [Synopsis](ce_ip_interface_module.md#synopsis)
- [Parameters](ce_ip_interface_module.md#parameters)
- [Notes](ce_ip_interface_module.md#notes)
- [Examples](ce_ip_interface_module.md#examples)
- [Return Values](ce_ip_interface_module.md#return-values)

## [Synopsis](ce_ip_interface_module.md#id1)

- Manages Layer 3 attributes for IPv4 and IPv6 interfaces on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_ip_interface

## [Parameters](ce_ip_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **addr**  string | IPv4 or IPv6 Address. |
| **interface**  string / required | Full name of interface, i.e. 40GE1/0/22, vlanif10. |
| **ipv4_type**  string | Specifies an address type. The value is an enumerated type. main, primary IP address. sub, secondary IP address.  **Choices:**   - `"main"` ← (default) - `"sub"` |
| **mask**  string | Subnet mask for IPv4 or IPv6 Address in decimal format. |
| **state**  string | Specify desired state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **version**  string | IP address version.  **Choices:**   - `"v4"` ← (default) - `"v6"` |

## [Notes](ce_ip_interface_module.md#id3)

> **Note:**
>
> - Interface must already be a L3 port when using this module.
> - Logical interfaces (loopback, vlanif) must be created first.
> - `mask` must be inserted in decimal format (i.e. 24) for both IPv6 and IPv4.
> - A single interface can have multiple IPv6 configured.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_ip_interface_module.md#id4)

```yaml+jinja
- name: Ip_interface module test
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
  - name: Ensure ipv4 address is configured on 10GE1/0/22
    community.network.ce_ip_interface:
      interface: 10GE1/0/22
      version: v4
      state: present
      addr: 20.20.20.20
      mask: 24
      provider: '{{ cli }}'

  - name: Ensure ipv4 secondary address is configured on 10GE1/0/22
    community.network.ce_ip_interface:
      interface: 10GE1/0/22
      version: v4
      state: present
      addr: 30.30.30.30
      mask: 24
      ipv4_type: sub
      provider: '{{ cli }}'

  - name: Ensure ipv6 is enabled on 10GE1/0/22
    community.network.ce_ip_interface:
      interface: 10GE1/0/22
      version: v6
      state: present
      provider: '{{ cli }}'

  - name: Ensure ipv6 address is configured on 10GE1/0/22
    community.network.ce_ip_interface:
      interface: 10GE1/0/22
      version: v6
      state: present
      addr: 2001::db8:800:200c:cccb
      mask: 64
      provider: '{{ cli }}'
```

## [Return Values](ce_ip_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of IP attributes after module execution  **Returned:** always  **Sample:** `{"interface": "10GE1/0/22", "ipv4": [{"addrType": "main", "ifIpAddr": "20.20.20.20", "subnetMask": "255.255.255.0"}]}` |
| **existing**  dictionary | k/v pairs of existing IP attributes on the interface  **Returned:** always  **Sample:** `{"interface": "10GE1/0/22", "ipv4": [{"addrType": "main", "ifIpAddr": "11.11.11.11", "subnetMask": "255.255.0.0"}]}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"addr": "20.20.20.20", "interface": "10GE1/0/22", "mask": "24"}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["interface 10GE1/0/22", "ip address 20.20.20.20 24"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
