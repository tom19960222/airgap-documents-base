---
collection: ansible
version: "8"
title: "cisco.dnac.sda_virtual_network_v2 module – Resource module for Sda Virtual Network V2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/sda_virtual_network_v2_module.html
fetched_at: 2026-07-28T01:24:44+00:00
---
# cisco.dnac.sda_virtual_network_v2 module – Resource module for Sda Virtual Network V2

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/) (version 6.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](sda_virtual_network_v2_module.md#ansible-collections-cisco-dnac-sda-virtual-network-v2-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sda_virtual_network_v2`.

New in cisco.dnac 3.1.0

- [Synopsis](sda_virtual_network_v2_module.md#synopsis)
- [Requirements](sda_virtual_network_v2_module.md#requirements)
- [Parameters](sda_virtual_network_v2_module.md#parameters)
- [Notes](sda_virtual_network_v2_module.md#notes)
- [See Also](sda_virtual_network_v2_module.md#see-also)
- [Examples](sda_virtual_network_v2_module.md#examples)
- [Return Values](sda_virtual_network_v2_module.md#return-values)

## [Synopsis](sda_virtual_network_v2_module.md#id1)

- Manage operations create, update and delete of the resource Sda Virtual Network V2.
- Add virtual network with scalable groups at global level.
- Delete virtual network with scalable groups.
- Update virtual network with scalable groups.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sda_virtual_network_v2_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sda_virtual_network_v2_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **isGuestVirtualNetwork**  boolean | Guest Virtual Network enablement flag, default value is False.  **Choices:**   - `false` - `true` |
| **scalableGroupNames**  list / elements=string | Scalable Group to be associated to virtual network. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **virtualNetworkName**  string | Virtual Network Name to be assigned at global level. |
| **vManageVpnId**  string | VManage vpn id for SD-WAN. |

## [Notes](sda_virtual_network_v2_module.md#id4)

> **Note:**
>
> - SDK Method used are sda.Sda.add_virtual_network_with_scalable_groups, sda.Sda.delete_virtual_network_with_scalable_groups, sda.Sda.update_virtual_network_with_scalable_groups,
> - Paths used are post /dna/intent/api/v1/virtual-network, delete /dna/intent/api/v1/virtual-network, put /dna/intent/api/v1/virtual-network,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sda_virtual_network_v2_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for SDA AddVirtualNetworkWithScalableGroups](https://developer.cisco.com/docs/dna-center/#!add-virtual-network-with-scalable-groups)
> :   Complete reference of the AddVirtualNetworkWithScalableGroups API.
>
> [Cisco DNA Center documentation for SDA DeleteVirtualNetworkWithScalableGroups](https://developer.cisco.com/docs/dna-center/#!delete-virtual-network-with-scalable-groups)
> :   Complete reference of the DeleteVirtualNetworkWithScalableGroups API.
>
> [Cisco DNA Center documentation for SDA UpdateVirtualNetworkWithScalableGroups](https://developer.cisco.com/docs/dna-center/#!update-virtual-network-with-scalable-groups)
> :   Complete reference of the UpdateVirtualNetworkWithScalableGroups API.

## [Examples](sda_virtual_network_v2_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.sda_virtual_network_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    isGuestVirtualNetwork: true
    scalableGroupNames:
    - string
    vManageVpnId: string
    virtualNetworkName: string

- name: Delete all
  cisco.dnac.sda_virtual_network_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    virtualNetworkName: string

- name: Update all
  cisco.dnac.sda_virtual_network_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    isGuestVirtualNetwork: true
    scalableGroupNames:
    - string
    vManageVpnId: string
    virtualNetworkName: string
```

## [Return Values](sda_virtual_network_v2_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"description": "string", "executionId": "string", "executionStatusUrl": "string", "status": "string", "taskId": "string", "taskStatusUrl": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
