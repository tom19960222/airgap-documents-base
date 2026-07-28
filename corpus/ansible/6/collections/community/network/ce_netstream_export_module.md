---
collection: ansible
version: "6"
title: "community.network.ce_netstream_export module – Manages netstream export on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_netstream_export_module.html
fetched_at: 2026-07-27T17:17:42+00:00
---
# community.network.ce_netstream_export module – Manages netstream export on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_netstream_export`.

- [Synopsis](ce_netstream_export_module.md#synopsis)
- [Parameters](ce_netstream_export_module.md#parameters)
- [Notes](ce_netstream_export_module.md#notes)
- [Examples](ce_netstream_export_module.md#examples)
- [Return Values](ce_netstream_export_module.md#return-values)

## [Synopsis](ce_netstream_export_module.md#id1)

- Configure NetStream flow statistics exporting and versions for exported packets on HUAWEI CloudEngine switches.

## [Parameters](ce_netstream_export_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **as_option**  string | Specifies the AS number recorded in the statistics as the original or the peer AS number.  Choices:   - `"origin"` - `"peer"` |
| **bgp_nexthop**  string | Configures the statistics to carry BGP next hop information. Currently, only V9 supports the exported packets carrying BGP next hop information.  Choices:   - `"enable"` - `"disable"` ← (default) |
| **host_ip**  string | Specifies destination address which can be IPv6 or IPv4 of the exported NetStream packet. |
| **host_port**  string | Specifies the destination UDP port number of the exported packets. The value is an integer that ranges from 1 to 65535. |
| **host_vpn**  string | Specifies the VPN instance of the exported packets carrying flow statistics. Ensure the VPN instance has been created on the device. |
| **source_ip**  string | Specifies source address which can be IPv6 or IPv4 of the exported NetStream packet. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | Specifies NetStream feature.  Choices:   - `"ip"` - `"vxlan"` |
| **version**  string | Sets the version of exported packets.  Choices:   - `"5"` - `"9"` |

## [Notes](ce_netstream_export_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_netstream_export_module.md#id4)

```yaml+jinja
- name: Netstream export module test
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

  - name: Configures the source address for the exported packets carrying IPv4 flow statistics.
    community.network.ce_netstream_export:
      type: ip
      source_ip: 192.8.2.2
      provider: "{{ cli }}"

  - name: Configures the source IP address for the exported packets carrying VXLAN flexible flow statistics.
    community.network.ce_netstream_export:
      type: vxlan
      source_ip: 192.8.2.3
      provider: "{{ cli }}"

  - name: Configures the destination IP address and destination UDP port number for the exported packets carrying IPv4 flow statistics.
    community.network.ce_netstream_export:
      type: ip
      host_ip: 192.8.2.4
      host_port: 25
      host_vpn: test
      provider: "{{ cli }}"

  - name: Configures the destination IP address and destination UDP port number for the exported packets carrying VXLAN flexible flow statistics.
    community.network.ce_netstream_export:
      type: vxlan
      host_ip: 192.8.2.5
      host_port: 26
      host_vpn: test
      provider: "{{ cli }}"

  - name: Configures the version number of the exported packets carrying IPv4 flow statistics.
    community.network.ce_netstream_export:
      type: ip
      version: 9
      as_option: origin
      bgp_nexthop: enable
      provider: "{{ cli }}"

  - name: Configures the version for the exported packets carrying VXLAN flexible flow statistics.
    community.network.ce_netstream_export:
      type: vxlan
      version: 9
      provider: "{{ cli }}"
```

## [Return Values](ce_netstream_export_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of end attributes on the device  Returned: always  Sample: `{"as_option": "origin", "bgp_nexthop": "enable", "host_ip": "192.8.5.6", "host_port": "26", "host_vpn": "test", "source_ip": "192.8.2.5", "type": "ip", "version": "9"}` |
| **existing**  dictionary | k/v pairs of existing attributes on the device  Returned: always  Sample: `{"as_option": null, "bgp_nexthop": "disable", "host_ip": null, "host_port": null, "host_vpn": null, "source_ip": null, "type": "ip", "version": null}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"as_option": "origin", "bgp_nexthop": "enable", "host_ip": "192.8.5.6", "host_port": "26", "host_vpn": "test", "source_ip": "192.8.2.5", "state": "present", "type": "ip", "version": "9"}` |
| **updates**  list / elements=string | command list sent to the device  Returned: always  Sample: `["netstream export ip source 192.8.2.5", "netstream export ip host 192.8.5.6 26 vpn-instance test", "netstream export ip version 9 origin-as bgp-nexthop"]` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
