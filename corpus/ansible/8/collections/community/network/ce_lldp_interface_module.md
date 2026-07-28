---
collection: ansible
version: "8"
title: "community.network.ce_lldp_interface module – Manages INTERFACE LLDP configuration on HUAWEI CloudEngine switches."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_lldp_interface_module.html
fetched_at: 2026-07-28T01:55:36+00:00
---
# community.network.ce_lldp_interface module – Manages INTERFACE LLDP configuration on HUAWEI CloudEngine switches.

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
> To use it in a playbook, specify: `community.network.ce_lldp_interface`.

New in community.network 0.2.0

- [Synopsis](ce_lldp_interface_module.md#synopsis)
- [Parameters](ce_lldp_interface_module.md#parameters)
- [Notes](ce_lldp_interface_module.md#notes)
- [Examples](ce_lldp_interface_module.md#examples)
- [Return Values](ce_lldp_interface_module.md#return-values)

## [Synopsis](ce_lldp_interface_module.md#id1)

- Manages INTERFACE LLDP configuration on HUAWEI CloudEngine switches.

Aliases: network.cloudengine.ce_lldp_interface

## [Parameters](ce_lldp_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **dcbx**  boolean | Enable the ability to send DCBX TLV.  **Choices:**   - `false` - `true` |
| **eee**  boolean | Enable the ability to send EEE TLV.  **Choices:**   - `false` - `true` |
| **function_lldp_interface_flag**  string | Used to distinguish between command line functions.  **Choices:**   - `"disableINTERFACE"` - `"tlvdisableINTERFACE"` - `"tlvenableINTERFACE"` - `"intervalINTERFACE"` |
| **ifname**  string | Interface name. |
| **linkaggretxenable**  boolean | Enable the ability to send link aggregation TLV.  **Choices:**   - `false` - `true` |
| **lldpadminstatus**  string | Set interface lldp enable state.  **Choices:**   - `"txOnly"` - `"rxOnly"` - `"txAndRx"` - `"disabled"` |
| **lldpenable**  string | Set global LLDP enable state.  **Choices:**   - `"enabled"` - `"disabled"` |
| **macphytxenable**  boolean | Enable MAC/PHY configuration and state TLV to be sent.  **Choices:**   - `false` - `true` |
| **manaddrtxenable**  boolean | Make it able to send management address TLV.  **Choices:**   - `false` - `true` |
| **maxframetxenable**  boolean | Enable the ability to send maximum frame length TLV.  **Choices:**   - `false` - `true` |
| **portdesctxenable**  boolean | Enabling the ability to send a description of TLV.  **Choices:**   - `false` - `true` |
| **portvlantxenable**  boolean | Enable port vlan tx.  **Choices:**   - `false` - `true` |
| **protoidtxenable**  boolean | Enable the ability to send protocol identity TLV.  **Choices:**   - `false` - `true` |
| **protovlantxenable**  boolean | Enable protocol vlan tx.  **Choices:**   - `false` - `true` |
| **state**  string | Manage the state of the resource.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **syscaptxenable**  boolean | Enable the ability to send system capabilities TLV.  **Choices:**   - `false` - `true` |
| **sysdesctxenable**  boolean | Enable the ability to send system description TLV.  **Choices:**   - `false` - `true` |
| **sysnametxenable**  boolean | Enable the ability to send system name TLV.  **Choices:**   - `false` - `true` |
| **txinterval**  integer | LLDP send message interval. |
| **txprotocolvlanid**  integer | Set tx protocol vlan id. |
| **txvlannameid**  integer | Set tx vlan name id. |
| **type_tlv_disable**  string | Used to distinguish between command line functions.  **Choices:**   - `"basic_tlv"` - `"dot3_tlv"` |
| **type_tlv_enable**  string | Used to distinguish between command line functions.  **Choices:**   - `"dot1_tlv"` - `"dcbx"` |
| **vlannametxenable**  boolean | Set vlan name tx enable or not.  **Choices:**   - `false` - `true` |

## [Notes](ce_lldp_interface_module.md#id3)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Recommended connection is `netconf`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_lldp_interface_module.md#id4)

```yaml+jinja
- name: "Configure global LLDP enable state"
  ce_lldp_interface_interface:
    lldpenable: enabled

- name: "Configure interface lldp enable state"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: disableINTERFACE
    ifname: 10GE1/0/1
    lldpadminstatus: rxOnly
- name: "Configure LLDP transmit interval and ensure global LLDP state is already enabled"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: intervalINTERFACE
    ifname: 10GE1/0/1
    txinterval: 4

- name: "Configure basic-tlv: management-address TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: basic_tlv
    ifname: 10GE1/0/1
    manaddrtxenable: true

- name: "Configure basic-tlv: prot description TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: basic_tlv
    ifname: 10GE1/0/1
    portdesctxenable: true

- name: "Configure basic-tlv: system capabilities TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: basic_tlv
    ifname: 10GE1/0/1
    syscaptxenable: true

- name: "Configure basic-tlv: system description TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: basic_tlv
    ifname: 10GE1/0/1
    sysdesctxenable: true

- name: "Configure basic-tlv: system name TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: basic_tlv
    ifname: 10GE1/0/1
    sysnametxenable: true

- name: "TLV types that are forbidden to be published on the configuration interface, link aggregation TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: dot3_tlv
    ifname: 10GE1/0/1
    linkAggreTxEnable: true

- name: "TLV types that are forbidden to be published on the configuration interface, MAC/PHY configuration/status TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: dot3_tlv
    ifname: 10GE1/0/1
    macPhyTxEnable: true

- name: "TLV types that are forbidden to be published on the configuration interface, maximum frame size TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: dot3_tlv
    ifname: 10GE1/0/1
    maxFrameTxEnable: true

- name: "TLV types that are forbidden to be published on the configuration interface, EEE TLV"
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvdisableINTERFACE
    type_tlv_disable: dot3_tlv
    ifname: 10GE1/0/1
    eee: true

- name: "Configure the interface to publish an optional DCBX TLV type "
  community.network.ce_lldp_interface:
    function_lldp_interface_flag: tlvenableINTERFACE
    ifname: 10GE1/0/1
    type_tlv_enable: dcbx
```

## [Return Values](ce_lldp_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | check to see if a change was made on the device  **Returned:** always  **Sample:** `true` |
| **end_state**  dictionary | k/v pairs of global DLDP configration after module execution  **Returned:** always  **Sample:** `{"function_lldp_interface_flag": "tlvenableINTERFACE", "ifname": "10GE1/0/1", "lldpadminstatus": "rxOnly", "lldpenable": "enabled", "type_tlv_enable": "dot1_tlv"}` |
| **existing**  dictionary | k/v pairs of existing global LLDP configration  **Returned:** always  **Sample:** `{"ifname": "10GE1/0/1", "lldpadminstatus": "txAndRx", "lldpenable": "disabled"}` |
| **proposed**  dictionary | k/v pairs of parameters passed into module  **Returned:** always  **Sample:** `{"function_lldp_interface_flag": "tlvenableINTERFACE", "ifname": "10GE1/0/1", "lldpadminstatus": "rxOnly", "lldpenable": "enabled", "state": "present", "type_tlv_enable": "dot1_tlv"}` |
| **updates**  list / elements=string | command sent to the device  **Returned:** always  **Sample:** `["lldp enable", "interface 10ge 1/0/1", "undo lldp disable", "lldp tlv-enable dot1-tlv vlan-name 4"]` |

### Authors

- xuxiaowei0512 (@CloudEngine-Ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
