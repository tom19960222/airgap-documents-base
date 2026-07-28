---
collection: ansible
version: "6"
title: "community.network.ce_bfd_session module – Manages BFD session configuration on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_bfd_session_module.html
fetched_at: 2026-07-27T17:17:16+00:00
---
# community.network.ce_bfd_session module – Manages BFD session configuration on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_bfd_session`.

- [Synopsis](ce_bfd_session_module.md#synopsis)
- [Parameters](ce_bfd_session_module.md#parameters)
- [Notes](ce_bfd_session_module.md#notes)
- [Examples](ce_bfd_session_module.md#examples)
- [Return Values](ce_bfd_session_module.md#return-values)

## [Synopsis](ce_bfd_session_module.md#id1)

- Manages BFD session configuration, creates a BFD session or deletes a specified BFD session on HUAWEI CloudEngine devices.

## [Parameters](ce_bfd_session_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **addr_type**  string | Specifies the peer IP address type.  Choices:   - `"ipv4"` |
| **create_type**  string | BFD session creation mode, the currently created BFD session only supports static or static auto-negotiation mode.  Choices:   - `"static"` ← (default) - `"auto"` |
| **dest_addr**  string | Specifies the peer IP address bound to the BFD session. |
| **local_discr**  string | The BFD session local identifier does not need to be configured when the mode is auto. |
| **out_if_name**  string | Specifies the type and number of the interface bound to the BFD session. |
| **remote_discr**  string | The BFD session remote identifier does not need to be configured when the mode is auto. |
| **session_name**  string / required | Specifies the name of a BFD session. The value is a string of 1 to 15 case-sensitive characters without spaces. |
| **src_addr**  string | Indicates the source IP address carried in BFD packets. |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_default_ip**  boolean | Indicates the default multicast IP address that is bound to a BFD session. By default, BFD uses the multicast IP address 224.0.0.184. You can set the multicast IP address by running the default-ip-address command. The value is a bool type.  Choices:   - `false` ← (default) - `true` |
| **vrf_name**  string | Specifies the name of a Virtual Private Network (VPN) instance that is bound to a BFD session. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value _public_ is reserved and cannot be used as the VPN instance name. |

## [Notes](ce_bfd_session_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_bfd_session_module.md#id4)

```yaml+jinja
- name: Bfd session module test
  hosts: cloudengine
  connection: local
  gather_facts: no

  tasks:
  - name: Configuring Single-hop BFD for Detecting Faults on a Layer 2 Link
    community.network.ce_bfd_session:
      session_name: bfd_l2link
      use_default_ip: true
      out_if_name: 10GE1/0/1
      local_discr: 163
      remote_discr: 163

  - name: Configuring Single-Hop BFD on a VLANIF Interface
    community.network.ce_bfd_session:
      session_name: bfd_vlanif
      dest_addr: 10.1.1.6
      out_if_name: Vlanif100
      local_discr: 163
      remote_discr: 163

  - name: Configuring Multi-Hop BFD
    community.network.ce_bfd_session:
      session_name: bfd_multi_hop
      dest_addr: 10.1.1.1
      local_discr: 163
      remote_discr: 163
```

## [Return Values](ce_bfd_session_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of configuration after module execution  Returned: always  Sample: `{"session": {"addrType": "IPV4", "createType": "SESS_STATIC", "destAddr": null, "outIfName": "10GE1/0/1", "sessName": "bfd_l2link", "srcAddr": null, "useDefaultIp": "true", "vrfName": null}}` |
| **existing**  dictionary | k/v pairs of existing configuration  Returned: always  Sample: `{"session": {}}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"addr_type": null, "create_type": null, "dest_addr": null, "out_if_name": "10GE1/0/1", "session_name": "bfd_l2link", "src_addr": null, "state": "present", "use_default_ip": true, "vrf_name": null}` |
| **updates**  list / elements=string | commands sent to the device  Returned: always  Sample: `["bfd bfd_l2link bind peer-ip default-ip interface 10ge1/0/1"]` |

### Authors

- QijunPan (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
