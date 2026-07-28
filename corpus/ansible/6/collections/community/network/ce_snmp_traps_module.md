---
collection: ansible
version: "6"
title: "community.network.ce_snmp_traps module – Manages SNMP traps configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ce_snmp_traps_module.html
fetched_at: 2026-07-27T17:17:51+00:00
---
# community.network.ce_snmp_traps module – Manages SNMP traps configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_snmp_traps`.

- [Synopsis](ce_snmp_traps_module.md#synopsis)
- [Parameters](ce_snmp_traps_module.md#parameters)
- [Notes](ce_snmp_traps_module.md#notes)
- [Examples](ce_snmp_traps_module.md#examples)
- [Return Values](ce_snmp_traps_module.md#return-values)

## [Synopsis](ce_snmp_traps_module.md#id1)

- Manages SNMP traps configurations on HUAWEI CloudEngine switches.

## [Parameters](ce_snmp_traps_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **feature_name**  string | Alarm feature name.  Choices:   - `"aaa"` - `"arp"` - `"bfd"` - `"bgp"` - `"cfg"` - `"configuration"` - `"dad"` - `"devm"` - `"dhcpsnp"` - `"dldp"` - `"driver"` - `"efm"` - `"erps"` - `"error-down"` - `"fcoe"` - `"fei"` - `"fei_comm"` - `"fm"` - `"ifnet"` - `"info"` - `"ipsg"` - `"ipv6"` - `"isis"` - `"l3vpn"` - `"lacp"` - `"lcs"` - `"ldm"` - `"ldp"` - `"ldt"` - `"lldp"` - `"mpls_lspm"` - `"msdp"` - `"mstp"` - `"nd"` - `"netconf"` - `"nqa"` - `"nvo3"` - `"openflow"` - `"ospf"` - `"ospfv3"` - `"pim"` - `"pim-std"` - `"qos"` - `"radius"` - `"rm"` - `"rmon"` - `"securitytrap"` - `"smlktrap"` - `"snmp"` - `"ssh"` - `"stackmng"` - `"sysclock"` - `"sysom"` - `"system"` - `"tcp"` - `"telnet"` - `"trill"` - `"trunk"` - `"tty"` - `"vbst"` - `"vfs"` - `"virtual-perception"` - `"vrrp"` - `"vstm"` - `"all"` |
| **interface_number**  string | Interface number. |
| **interface_type**  string | Interface type.  Choices:   - `"Ethernet"` - `"Eth-Trunk"` - `"Tunnel"` - `"NULL"` - `"LoopBack"` - `"Vlanif"` - `"100GE"` - `"40GE"` - `"MTunnel"` - `"10GE"` - `"GE"` - `"MEth"` - `"Vbdif"` - `"Nve"` |
| **port_number**  string | Source port number. |
| **trap_name**  string | Alarm trap name. |

## [Notes](ce_snmp_traps_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_snmp_traps_module.md#id4)

```yaml+jinja
- name: CloudEngine snmp traps test
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

  - name: "Config SNMP trap all enable"
    community.network.ce_snmp_traps:
      state: present
      feature_name: all
      provider: "{{ cli }}"

  - name: "Config SNMP trap interface"
    community.network.ce_snmp_traps:
      state: present
      interface_type: 40GE
      interface_number: 2/0/1
      provider: "{{ cli }}"

  - name: "Config SNMP trap port"
    community.network.ce_snmp_traps:
      state: present
      port_number: 2222
      provider: "{{ cli }}"
```

## [Return Values](ce_snmp_traps_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  Returned: always  Sample: `true` |
| **end_state**  dictionary | k/v pairs of aaa params after module execution  Returned: always  Sample: `{"snmp-agent trap": ["enable"], "undo snmp-agent trap": []}` |
| **existing**  dictionary | k/v pairs of existing aaa server  Returned: always  Sample: `{"snmp-agent trap": [], "undo snmp-agent trap": []}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  Returned: always  Sample: `{"feature_name": "all", "state": "present"}` |
| **updates**  list / elements=string | command sent to the device  Returned: always  Sample: `["snmp-agent trap enable"]` |

### Authors

- wangdezhuang (@QijunPan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
