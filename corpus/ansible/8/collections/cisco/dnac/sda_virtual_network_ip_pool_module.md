---
collection: ansible
version: "8"
title: "cisco.dnac.sda_virtual_network_ip_pool module – Resource module for Sda Virtual Network Ip Pool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/sda_virtual_network_ip_pool_module.html
fetched_at: 2026-07-28T01:24:43+00:00
---
# cisco.dnac.sda_virtual_network_ip_pool module – Resource module for Sda Virtual Network Ip Pool

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
> see [Requirements](sda_virtual_network_ip_pool_module.md#ansible-collections-cisco-dnac-sda-virtual-network-ip-pool-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sda_virtual_network_ip_pool`.

New in cisco.dnac 3.1.0

- [Synopsis](sda_virtual_network_ip_pool_module.md#synopsis)
- [Requirements](sda_virtual_network_ip_pool_module.md#requirements)
- [Parameters](sda_virtual_network_ip_pool_module.md#parameters)
- [Notes](sda_virtual_network_ip_pool_module.md#notes)
- [See Also](sda_virtual_network_ip_pool_module.md#see-also)
- [Examples](sda_virtual_network_ip_pool_module.md#examples)
- [Return Values](sda_virtual_network_ip_pool_module.md#return-values)

## [Synopsis](sda_virtual_network_ip_pool_module.md#id1)

- Manage operations create and delete of the resource Sda Virtual Network Ip Pool.
- Add IP Pool in SDA Virtual Network.
- Delete IP Pool from SDA Virtual Network.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sda_virtual_network_ip_pool_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sda_virtual_network_ip_pool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autoGenerateVlanName**  boolean | It will auto generate vlanName, if vlanName is empty(applicable for L3 and INFRA_VN).  **Choices:**   - `false` - `true` |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **ipPoolName**  string  *added in cisco.dnac 4.0.0* | IpPoolName query parameter. |
| **isBridgeModeVm**  boolean | Bridge Mode Vm enablement flag (applicable for L3 and L2 and default value is False ).  **Choices:**   - `false` - `true` |
| **isCommonPool**  boolean | Common Pool enablement flag(applicable for L3 and L2 and default value is False ).  **Choices:**   - `false` - `true` |
| **isIpDirectedBroadcast**  boolean | Ip Directed Broadcast enablement flag(applicable for L3 and default value is False ).  **Choices:**   - `false` - `true` |
| **isL2FloodingEnabled**  boolean  *added in cisco.dnac 4.0.0* | Layer2 flooding enablement flag(applicable for L3 , L2 and always true for L2 and default value is False ).  **Choices:**   - `false` - `true` |
| **isLayer2Only**  boolean | Layer2 Only enablement flag and default value is False.  **Choices:**   - `false` - `true` |
| **isThisCriticalPool**  boolean  *added in cisco.dnac 4.0.0* | Critical pool enablement flag(applicable for L3 and default value is False ).  **Choices:**   - `false` - `true` |
| **isWirelessPool**  boolean  *added in cisco.dnac 4.0.0* | Wireless Pool enablement flag(applicable for L3 and L2 and default value is False ).  **Choices:**   - `false` - `true` |
| **poolType**  string  *added in cisco.dnac 4.0.0* | Pool Type (applicable for INFRA_VN). |
| **scalableGroupName**  string  *added in cisco.dnac 4.0.0* | Scalable Group Name(applicable for L3). |
| **siteNameHierarchy**  string  *added in cisco.dnac 4.0.0* | SiteNameHierarchy query parameter. |
| **trafficType**  string  *added in cisco.dnac 4.0.0* | Traffic type(applicable for L3 and L2). |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **virtualNetworkName**  string | VirtualNetworkName query parameter. |
| **vlanId**  string | Vlan Id(applicable for L3 , L2 and INFRA_VN). |
| **vlanName**  string  *added in cisco.dnac 4.0.0* | Vlan name represent the segment name, if empty, vlanName would be auto generated by API. |

## [Notes](sda_virtual_network_ip_pool_module.md#id4)

> **Note:**
>
> - SDK Method used are sda.Sda.add_ip_pool_in_sda_virtual_network, sda.Sda.delete_ip_pool_from_sda_virtual_network,
> - Paths used are post /dna/intent/api/v1/business/sda/virtualnetwork/ippool, delete /dna/intent/api/v1/business/sda/virtualnetwork/ippool,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sda_virtual_network_ip_pool_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for SDA AddIPPoolInSDAVirtualNetwork](https://developer.cisco.com/docs/dna-center/#!add-ip-pool-in-sda-virtual-network)
> :   Complete reference of the AddIPPoolInSDAVirtualNetwork API.
>
> [Cisco DNA Center documentation for SDA DeleteIPPoolFromSDAVirtualNetwork](https://developer.cisco.com/docs/dna-center/#!delete-ip-pool-from-sda-virtual-network)
> :   Complete reference of the DeleteIPPoolFromSDAVirtualNetwork API.

## [Examples](sda_virtual_network_ip_pool_module.md#id6)

```yaml+jinja
- name: Delete all
  cisco.dnac.sda_virtual_network_ip_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    ipPoolName: string
    siteNameHierarchy: string
    virtualNetworkName: string

- name: Create
  cisco.dnac.sda_virtual_network_ip_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    autoGenerateVlanName: true
    ipPoolName: string
    isBridgeModeVm: true
    isCommonPool: true
    isIpDirectedBroadcast: true
    isL2FloodingEnabled: true
    isLayer2Only: true
    isThisCriticalPool: true
    isWirelessPool: true
    poolType: string
    scalableGroupName: string
    siteNameHierarchy: string
    trafficType: string
    virtualNetworkName: string
    vlanId: string
    vlanName: string
```

## [Return Values](sda_virtual_network_ip_pool_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"description": "string", "executionId": "string", "executionStatusUrl": "string", "status": "string", "taskId": "string", "taskStatusUrl": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
