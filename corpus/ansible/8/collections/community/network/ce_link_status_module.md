---
collection: ansible
version: "8"
title: "community.network.ce_link_status module – Get interface link status on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_link_status_module.html
fetched_at: 2026-07-28T01:55:35+00:00
---
# community.network.ce_link_status module – Get interface link status on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_link_status`.

- [Synopsis](ce_link_status_module.md#synopsis)
- [Parameters](ce_link_status_module.md#parameters)
- [Notes](ce_link_status_module.md#notes)
- [Examples](ce_link_status_module.md#examples)
- [Return Values](ce_link_status_module.md#return-values)

## [Synopsis](ce_link_status_module.md#id1)

- Get interface link status on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_link_status

## [Parameters](ce_link_status_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **interface**  string / required | For the interface parameter, you can enter `all` to display information about all interfaces, an interface type such as `40GE` to display information about interfaces of the specified type, or full name of an interface such as `40GE1/0/22` or `vlanif10` to display information about the specific interface. |

## [Notes](ce_link_status_module.md#id3)

> **Note:**
>
> - Current physical state shows an interface’s physical status.
> - Current link state shows an interface’s link layer protocol status.
> - Current IPv4 state shows an interface’s IPv4 protocol status.
> - Current IPv6 state shows an interface’s IPv6 protocol status.
> - Inbound octets(bytes) shows the number of bytes that an interface received.
> - Inbound unicast(pkts) shows the number of unicast packets that an interface received.
> - Inbound multicast(pkts) shows the number of multicast packets that an interface received.
> - Inbound broadcast(pkts) shows the number of broadcast packets that an interface received.
> - Inbound error(pkts) shows the number of error packets that an interface received.
> - Inbound drop(pkts) shows the total number of packets that were sent to the interface but dropped by an interface.
> - Inbound rate(byte/sec) shows the rate at which an interface receives bytes within an interval.
> - Inbound rate(pkts/sec) shows the rate at which an interface receives packets within an interval.
> - Outbound octets(bytes) shows the number of the bytes that an interface sent.
> - Outbound unicast(pkts) shows the number of unicast packets that an interface sent.
> - Outbound multicast(pkts) shows the number of multicast packets that an interface sent.
> - Outbound broadcast(pkts) shows the number of broadcast packets that an interface sent.
> - Outbound error(pkts) shows the total number of packets that an interface sent but dropped by the remote interface.
> - Outbound drop(pkts) shows the number of dropped packets that an interface sent.
> - Outbound rate(byte/sec) shows the rate at which an interface sends bytes within an interval.
> - Outbound rate(pkts/sec) shows the rate at which an interface sends packets within an interval.
> - Speed shows the rate for an Ethernet interface.
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_link_status_module.md#id4)

```yaml+jinja
- name: Link status test
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

  - name: Get specified interface link status information
    community.network.ce_link_status:
      interface: 40GE1/0/1
      provider: "{{ cli }}"

  - name: Get specified interface type link status information
    community.network.ce_link_status:
      interface: 40GE
      provider: "{{ cli }}"

  - name: Get all interfaces link status information
    community.network.ce_link_status:
      interface: all
      provider: "{{ cli }}"
```

## [Return Values](ce_link_status_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | Interface link status information  **Returned:** always  **Sample:** `{"40ge2/0/8": {"Current IPv4 state": "down", "Current IPv6 state": "down", "Current link state": "up", "Current physical state": "up", "Inbound broadcast(pkts)": "0", "Inbound drop(pkts)": "0", "Inbound error(pkts)": "0", "Inbound multicast(pkts)": "20151", "Inbound octets(bytes)": "7314813", "Inbound rate(byte/sec)": "11", "Inbound rate(pkts/sec)": "0", "Inbound unicast(pkts)": "0", "Outbound broadcast(pkts)": "1", "Outbound drop(pkts)": "0", "Outbound error(pkts)": "0", "Outbound multicast(pkts)": "20152", "Outbound octets(bytes)": "7235021", "Outbound rate(byte/sec)": "11", "Outbound rate(pkts/sec)": "0", "Outbound unicast(pkts)": "0", "Speed": "40GE"}}` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
