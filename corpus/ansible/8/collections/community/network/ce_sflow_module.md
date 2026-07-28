---
collection: ansible
version: "8"
title: "community.network.ce_sflow module – Manages sFlow configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_sflow_module.html
fetched_at: 2026-07-28T01:55:49+00:00
---
# community.network.ce_sflow module – Manages sFlow configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_sflow`.

- [Synopsis](ce_sflow_module.md#synopsis)
- [Parameters](ce_sflow_module.md#parameters)
- [Notes](ce_sflow_module.md#notes)
- [Examples](ce_sflow_module.md#examples)
- [Return Values](ce_sflow_module.md#return-values)

## [Synopsis](ce_sflow_module.md#id1)

- Configure Sampled Flow (sFlow) to monitor traffic on an interface in real time, detect abnormal traffic, and locate the source of attack traffic, ensuring stable running of the network.

Aliases: network.cloudengine.ce_sflow

## [Parameters](ce_sflow_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **agent_ip**  string | Specifies the IPv4/IPv6 address of an sFlow agent. |
| **collector_datagram_size**  string | Specifies the maximum length of sFlow packets sent from an sFlow agent to an sFlow collector. The value is an integer, in bytes. It ranges from 1024 to 8100. The default value is 1400. |
| **collector_description**  string | Specifies the description of an sFlow collector. The value is a string of 1 to 255 case-sensitive characters without spaces. |
| **collector_id**  string | Specifies the ID of an sFlow collector. This ID is used when you specify the collector in subsequent sFlow configuration.  **Choices:**   - `"1"` - `"2"` |
| **collector_ip**  string | Specifies the IPv4/IPv6 address of the sFlow collector. |
| **collector_ip_vpn**  string | Specifies the name of a VPN instance. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value `_public_` is reserved and cannot be used as the VPN instance name. |
| **collector_meth**  string | Configures the device to send sFlow packets through service interfaces, enhancing the sFlow packet forwarding capability. The enhanced parameter is optional. No matter whether you configure the enhanced mode, the switch determines to send sFlow packets through service cards or management port based on the routing information on the collector. When the value is meth, the device forwards sFlow packets at the control plane. When the value is enhanced, the device forwards sFlow packets at the forwarding plane to enhance the sFlow packet forwarding capacity.  **Choices:**   - `"meth"` - `"enhanced"` |
| **collector_udp_port**  string | Specifies the UDP destination port number of sFlow packets. The value is an integer that ranges from 1 to 65535. The default value is 6343. |
| **counter_collector**  string | Indicates the ID list of the counter collector. |
| **counter_interval**  string | Indicates the counter sampling interval. The value is an integer that ranges from 10 to 4294967295, in seconds. The default value is 20. |
| **export_route**  string | Configures the sFlow packets sent by the switch not to carry routing information.  **Choices:**   - `"enable"` - `"disable"` |
| **sample_collector**  string | Indicates the ID list of the collector. |
| **sample_direction**  string | Enables flow sampling in the inbound or outbound direction.  **Choices:**   - `"inbound"` - `"outbound"` - `"both"` |
| **sample_length**  string | Specifies the maximum length of sampled packets. The value is an integer and ranges from 18 to 512, in bytes. The default value is 128. |
| **sample_rate**  string | Specifies the flow sampling rate in the format 1/rate. The value is an integer and ranges from 1 to 4294967295. The default value is 8192. |
| **sflow_interface**  string | Full name of interface for Flow Sampling or Counter. It must be a physical interface, Eth-Trunk, or Layer 2 subinterface. |
| **source_ip**  string | Specifies the source IPv4/IPv6 address of sFlow packets. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](ce_sflow_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_sflow_module.md#id4)

```yaml+jinja
---

- name: Sflow module test
  hosts: ce128
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
  - name: Configuring sFlow Agent
    community.network.ce_sflow:
      agent_ip: 6.6.6.6
      provider: '{{ cli }}'

  - name: Configuring sFlow Collector
    community.network.ce_sflow:
      collector_id: 1
      collector_ip: 7.7.7.7
      collector_ip_vpn: vpn1
      collector_description: Collector1
      provider: '{{ cli }}'

  - name: Configure flow sampling.
    community.network.ce_sflow:
      sflow_interface: 10GE2/0/2
      sample_collector: 1
      sample_direction: inbound
      provider: '{{ cli }}'

  - name: Configure counter sampling.
    community.network.ce_sflow:
      sflow_interface: 10GE2/0/2
      counter_collector: 1
      counter_interval: 1000
      provider: '{{ cli }}'
```

## [Return Values](ce_sflow_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  **Returned:** verbose mode  **Sample:** `{"agent": {"family": "ipv4", "ipv4Addr": "1.2.3.4", "ipv6Addr": null}}` |
| **existing**  dictionary | k/v pairs of existing configuration  **Returned:** verbose mode  **Sample:** `{"agent": {}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** verbose mode  **Sample:** `{"agent_ip": "6.6.6.6", "state": "present"}` |
| **updates**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["sflow agent ip 6.6.6.6"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
