---
collection: ansible
version: "6"
title: "community.network.ce_snmp_target_host module – Manages SNMP target host configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_snmp_target_host_module.html
fetched_at: 2026-07-27T17:17:51+00:00
---
# community.network.ce_snmp_target_host module – Manages SNMP target host configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_snmp_target_host`.

- [Synopsis](ce_snmp_target_host_module.md#synopsis)
- [Parameters](ce_snmp_target_host_module.md#parameters)
- [Notes](ce_snmp_target_host_module.md#notes)
- [Examples](ce_snmp_target_host_module.md#examples)
- [Return Values](ce_snmp_target_host_module.md#return-values)

## [Synopsis](ce_snmp_target_host_module.md#id1)

- Manages SNMP target host configurations on HUAWEI CloudEngine switches.

## [Parameters](ce_snmp_target_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | Network Address. |
| **connect_port**  string | Udp port used by SNMP agent to connect the Network management. |
| **host_name**  string | Unique name to identify target host entry. |
| **interface_name**  string | Name of the interface to send the trap message. |
| **is_public_net**  string | To enable or disable Public Net-manager for target Host.  Choices:   - `"no_use"` ← (default) - `"true"` - `"false"` |
| **notify_type**  string | To configure notify type as trap or inform.  Choices:   - `"trap"` - `"inform"` |
| **recv_port**  string | UDP Port number used by network management to receive alarm messages. |
| **security_level**  string | Security level indicating whether to use authentication and encryption.  Choices:   - `"noAuthNoPriv"` - `"authentication"` - `"privacy"` |
| **security_model**  string | Security Model.  Choices:   - `"v1"` - `"v2c"` - `"v3"` |
| **security_name**  string | Security Name. |
| **security_name_v3**  string | Security Name V3. |
| **version**  string | Version(s) Supported by SNMP Engine.  Choices:   - `"none"` - `"v1"` - `"v2c"` - `"v3"` - `"v1v2c"` - `"v1v3"` - `"v2cv3"` - `"all"` |
| **vpn_name**  string | VPN instance Name. |

## [Notes](ce_snmp_target_host_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_snmp_target_host_module.md#id4)

```yaml+jinja
- name: CloudEngine snmp target host test
  hosts: cloudengine
  connection: local
  gather_facts: no

  tasks:

  - name: "Config SNMP version"
    community.network.ce_snmp_target_host:
      state: present
      version: v2cv3

  - name: "Config SNMP target host"
    community.network.ce_snmp_target_host:
      state: present
      host_name: test1
      address: 1.1.1.1
      notify_type: trap
      vpn_name: js
      security_model: v2c
      security_name: wdz
```

## [Return Values](ce_snmp_target_host_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"target host info": [{"address": "10.135.182.158", "domain": "snmpUDPDomain", "nmsName": "test2", "notifyType": "trap", "securityLevel": "authentication", "securityModel": "v3", "securityNameV3": "wdz", "vpnInstanceName": "js"}]}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"address": "10.135.182.158", "host_name": "test2", "notify_type": "trap", "security_level": "authentication", "security_model": "v3", "security_name_v3": "wdz", "state": "present", "vpn_name": "js"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["snmp-agent target-host host-name test2 trap address udp-domain 10.135.182.158 vpn-instance js params securityname wdz v3 authentication"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
