---
collection: ansible
version: "8"
title: "cisco.dnac.transit_peer_network module – Resource module for Transit Peer Network"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/transit_peer_network_module.html
fetched_at: 2026-07-28T01:25:38+00:00
---
# cisco.dnac.transit_peer_network module – Resource module for Transit Peer Network

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
> see [Requirements](transit_peer_network_module.md#ansible-collections-cisco-dnac-transit-peer-network-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.transit_peer_network`.

New in cisco.dnac 6.5.0

- [Synopsis](transit_peer_network_module.md#synopsis)
- [Requirements](transit_peer_network_module.md#requirements)
- [Parameters](transit_peer_network_module.md#parameters)
- [Notes](transit_peer_network_module.md#notes)
- [See Also](transit_peer_network_module.md#see-also)
- [Examples](transit_peer_network_module.md#examples)
- [Return Values](transit_peer_network_module.md#return-values)

## [Synopsis](transit_peer_network_module.md#id1)

- Manage operations create and delete of the resource Transit Peer Network.
- Add Transit Peer Network in SD-Access.
- Delete Transit Peer Network from SD-Access.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](transit_peer_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](transit_peer_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **ipTransitSettings**  dictionary | Transit Peer Network’s ipTransitSettings. |
| **autonomousSystemNumber**  string | Autonomous System Number (e.g.,1-65535). |
| **routingProtocolName**  string | Routing Protocol Name. |
| **sdaTransitSettings**  dictionary | Transit Peer Network’s sdaTransitSettings. |
| **transitControlPlaneSettings**  list / elements=dictionary | Transit Peer Network’s transitControlPlaneSettings. |
| **deviceManagementIpAddress**  string | Device Management Ip Address of provisioned device. |
| **siteNameHierarchy**  string | Site Name Hierarchy where device is provisioned. |
| **transitPeerNetworkName**  string | TransitPeerNetworkName query parameter. Transit Peer Network Name. |
| **transitPeerNetworkType**  string | Transit Peer Network Type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](transit_peer_network_module.md#id4)

> **Note:**
>
> - SDK Method used are ..add_transit_peer_network, ..delete_transit_peer_network,
> - Paths used are post /dna/intent/api/v1/business/sda/transit-peer-network, delete /dna/intent/api/v1/business/sda/transit-peer-network,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](transit_peer_network_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for AddTransitPeerNetwork](https://developer.cisco.com/docs/dna-center/#!add-transit-peer-network)
> :   Complete reference of the AddTransitPeerNetwork API.
>
> [Cisco DNA Center documentation for DeleteTransitPeerNetwork](https://developer.cisco.com/docs/dna-center/#!delete-transit-peer-network)
> :   Complete reference of the DeleteTransitPeerNetwork API.

## [Examples](transit_peer_network_module.md#id6)

```yaml+jinja
- name: Delete all
  cisco.dnac.transit_peer_network:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    transitPeerNetworkName: string

- name: Create
  cisco.dnac.transit_peer_network:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    ipTransitSettings:
      autonomousSystemNumber: string
      routingProtocolName: string
    sdaTransitSettings:
      transitControlPlaneSettings:
      - deviceManagementIpAddress: string
        siteNameHierarchy: string
    transitPeerNetworkName: string
    transitPeerNetworkType: string
```

## [Return Values](transit_peer_network_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"description": "string", "executionId": "string", "executionStatusUrl": "string", "status": "string", "taskId": "string", "taskStatusUrl": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
