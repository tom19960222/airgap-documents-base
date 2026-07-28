---
collection: ansible
version: "8"
title: "community.network.flowadm module – Manage bandwidth resource control and priority for protocols, services and zones on Solaris/illumos systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/flowadm_module.html
fetched_at: 2026-07-28T01:56:39+00:00
---
# community.network.flowadm module – Manage bandwidth resource control and priority for protocols, services and zones on Solaris/illumos systems

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
> To use it in a playbook, specify: `community.network.flowadm`.

- [Synopsis](flowadm_module.md#synopsis)
- [Parameters](flowadm_module.md#parameters)
- [Examples](flowadm_module.md#examples)
- [Return Values](flowadm_module.md#return-values)

## [Synopsis](flowadm_module.md#id1)

- Create/modify/remove networking bandwidth and associated resources for a type of traffic on a particular link.

Aliases: network.illumos.flowadm

## [Parameters](flowadm_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dsfield**  string | - Identifies the 8-bit differentiated services field (as defined in RFC 2474). The optional dsfield_mask is used to state the bits of interest in the differentiated services field when comparing with the dsfield value. Both values must be in hexadecimal. |
| **link**  string | Specifiies a link to configure flow on. |
| **local_ip**  string | Identifies a network flow by the local IP address. |
| **local_port**  string | Identifies a service specified by the local port. |
| **maxbw**  string | - Sets the full duplex bandwidth for the flow. The bandwidth is specified as an integer with one of the scale suffixes(K, M, or G for Kbps, Mbps, and Gbps). If no units are specified, the input value will be read as Mbps. |
| **name**  aliases: flow  string / required | - A flow is defined as a set of attributes based on Layer 3 and Layer 4 headers, which can be used to identify a protocol, service, or a zone. |
| **priority**  string | Sets the relative priority for the flow.  **Choices:**   - `"low"` - `"medium"` ← (default) - `"high"` |
| **remote_ip**  string | Identifies a network flow by the remote IP address. |
| **state**  string | Create/delete/enable/disable an IP address on the network interface.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"resetted"` |
| **temporary**  boolean | Specifies that the configured flow is temporary. Temporary flows do not persist across reboots.  **Choices:**   - `false` ← (default) - `true` |
| **transport**  string | - Specifies a Layer 4 protocol to be used. It is typically used in combination with *local_port* to identify the service that needs special attention. |

## [Examples](flowadm_module.md#id3)

```yaml+jinja
- name: Limit SSH traffic to 100M via vnic0 interface
  community.network.flowadm:
    link: vnic0
    flow: ssh_out
    transport: tcp
    local_port: 22
    maxbw: 100M
    state: present

- name: Reset flow properties
  community.network.flowadm:
    name: dns
    state: resetted

- name: Configure policy for EF PHB (DSCP value of 101110 from RFC 2598) with a bandwidth of 500 Mbps and a high priority
  community.network.flowadm:
    link: bge0
    dsfield: '0x2e:0xfc'
    maxbw: 500M
    priority: high
    flow: efphb-flow
    state: present
```

## [Return Values](flowadm_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dsfield**  string | flow’s differentiated services value  **Returned:** if dsfield is defined  **Sample:** `"0x2e:0xfc"` |
| **link**  string | flow’s link  **Returned:** if link is defined  **Sample:** `"vnic0"` |
| **local_Ip**  string | flow’s local IP address  **Returned:** if local_ip is defined  **Sample:** `"10.0.0.42"` |
| **local_port**  integer | flow’s local port  **Returned:** if local_port is defined  **Sample:** `1337` |
| **maxbw**  string | flow’s maximum bandwidth  **Returned:** if maxbw is defined  **Sample:** `"100M"` |
| **name**  string | flow name  **Returned:** always  **Sample:** `"http_drop"` |
| **priority**  string | flow’s priority  **Returned:** if priority is defined  **Sample:** `"low"` |
| **remote_Ip**  string | flow’s remote IP address  **Returned:** if remote_ip is defined  **Sample:** `"10.0.0.42"` |
| **state**  string | state of the target  **Returned:** always  **Sample:** `"present"` |
| **temporary**  boolean | flow’s persistence  **Returned:** always  **Sample:** `true` |
| **transport**  string | flow’s transport  **Returned:** if transport is defined  **Sample:** `"tcp"` |

### Authors

- Adam Števko (@xen0l)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
