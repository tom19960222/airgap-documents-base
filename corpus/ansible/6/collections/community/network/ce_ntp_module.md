---
collection: ansible
version: "6"
title: "community.network.ce_ntp module – Manages core NTP configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_ntp_module.html
fetched_at: 2026-07-27T17:17:44+00:00
---
# community.network.ce_ntp module – Manages core NTP configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_ntp`.

- [Synopsis](ce_ntp_module.md#synopsis)
- [Parameters](ce_ntp_module.md#parameters)
- [Notes](ce_ntp_module.md#notes)
- [Examples](ce_ntp_module.md#examples)
- [Return Values](ce_ntp_module.md#return-values)

## [Synopsis](ce_ntp_module.md#id1)

- Manages core NTP configuration on HUAWEI CloudEngine switches.

## [Parameters](ce_ntp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **is_preferred**  string | Makes given NTP server or peer the preferred NTP server or peer for the device.  Choices:   - `"enable"` - `"disable"` |
| **key_id**  string | Authentication key identifier to use with given NTP server or peer. |
| **peer**  string | Network address of NTP peer. |
| **server**  string | Network address of NTP server. |
| **source_int**  string | Local source interface from which NTP messages are sent. Must be fully qualified interface name, i.e. `40GE1/0/22`, `vlanif10`. Interface types, such as `10GE`, `40GE`, `100GE`, `Eth-Trunk`, `LoopBack`, `MEth`, `NULL`, `Tunnel`, `Vlanif`. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vpn_name**  string | Makes the device communicate with the given NTP server or peer over a specific vpn.  Default: `"_public_"` |

## [Notes](ce_ntp_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_ntp_module.md#id4)

```yaml+jinja
- name: NTP test
  hosts: cloudengine
  connection: local
  gather_facts: no

  tasks:

  - name: "Set NTP Server with parameters"
    community.network.ce_ntp:
      server: 192.8.2.6
      vpn_name: js
      source_int: vlanif4001
      is_preferred: enable
      key_id: 32

  - name: "Set NTP Peer with parameters"
    community.network.ce_ntp:
      peer: 192.8.2.6
      vpn_name: js
      source_int: vlanif4001
      is_preferred: enable
      key_id: 32
```

## [Return Values](ce_ntp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of ntp info after module execution  Returned: always  Sample: `{"is_preferred": "enable", "key_id": "48", "server": "2.2.2.2", "source_int": "vlanif4002", "vpn_name": "js"}` |
| **existing**  dictionary | k/v pairs of existing ntp server/peer  Returned: always  Sample: `{"is_preferred": "disable", "key_id": "32", "server": "2.2.2.2", "source_int": "vlanif4002", "vpn_name": "js"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"is_preferred": "enable", "key_id": "48", "server": "2.2.2.2", "source_int": "vlanif4002", "state": "present", "vpn_name": "js"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["ntp server 2.2.2.2 authentication-keyid 48 source-interface vlanif4002 vpn-instance js preferred"]` |

### Authors

- Zhijin Zhou (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
