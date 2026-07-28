---
collection: ansible
version: "6"
title: "community.network.pn_vrouter_packet_relay module – CLI command to add/remove vrouter-packet-relay"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/pn_vrouter_packet_relay_module.html
fetched_at: 2026-07-27T17:19:39+00:00
---
# community.network.pn_vrouter_packet_relay module – CLI command to add/remove vrouter-packet-relay

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
> To use it in a playbook, specify: `community.network.pn_vrouter_packet_relay`.

- [Synopsis](pn_vrouter_packet_relay_module.md#synopsis)
- [Parameters](pn_vrouter_packet_relay_module.md#parameters)
- [Examples](pn_vrouter_packet_relay_module.md#examples)
- [Return Values](pn_vrouter_packet_relay_module.md#return-values)

## [Synopsis](pn_vrouter_packet_relay_module.md#id1)

- This module can be used to add packet relay configuration for DHCP on vrouter and remove packet relay configuration for DHCP on vrouter.

## [Parameters](pn_vrouter_packet_relay_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **pn_cliswitch**  string | Target switch to run the CLI on. |
| **pn_forward_ip**  string / required | forwarding IP address. |
| **pn_forward_proto**  string | protocol type to forward packets.  Choices:   - `"dhcp"` ← (default) |
| **pn_nic**  string / required | NIC. |
| **pn_vrouter_name**  string / required | name of service config. |
| **state**  string | vrouter-packet-relay configuration command.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Examples](pn_vrouter_packet_relay_module.md#id3)

```yaml+jinja
- name: VRouter packet relay add
  community.network.pn_vrouter_packet_relay:
    pn_cliswitch: "sw01"
    pn_forward_ip: "192.168.10.1"
    pn_nic: "eth0.4092"
    pn_vrouter_name: "sw01-vrouter"

- name: VRouter packet relay remove
  community.network.pn_vrouter_packet_relay:
    pn_cliswitch: "sw01"
    state: "absent"
    pn_forward_ip: "192.168.10.1"
    pn_nic: "eth0.4092"
    pn_vrouter_name: "sw01-vrouter"
```

## [Return Values](pn_vrouter_packet_relay_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | indicates whether the CLI caused changes on the target.  Returned: always |
| **command**  string | the CLI command run on the target node.  Returned: always |
| **stderr**  list / elements=string | set of error responses from the vrouter-packet-relay command.  Returned: on error |
| **stdout**  list / elements=string | set of responses from the vrouter-packet-relay command.  Returned: always |

### Authors

- Pluribus Networks (@rajaspachipulusu17)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
