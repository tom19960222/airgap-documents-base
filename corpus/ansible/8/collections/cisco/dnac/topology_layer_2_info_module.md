---
collection: ansible
version: "8"
title: "cisco.dnac.topology_layer_2_info module – Information module for Topology Layer 2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/topology_layer_2_info_module.html
fetched_at: 2026-07-28T01:25:33+00:00
---
# cisco.dnac.topology_layer_2_info module – Information module for Topology Layer 2

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
> see [Requirements](topology_layer_2_info_module.md#ansible-collections-cisco-dnac-topology-layer-2-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.topology_layer_2_info`.

New in cisco.dnac 3.1.0

- [Synopsis](topology_layer_2_info_module.md#synopsis)
- [Requirements](topology_layer_2_info_module.md#requirements)
- [Parameters](topology_layer_2_info_module.md#parameters)
- [Notes](topology_layer_2_info_module.md#notes)
- [See Also](topology_layer_2_info_module.md#see-also)
- [Examples](topology_layer_2_info_module.md#examples)
- [Return Values](topology_layer_2_info_module.md#return-values)

## [Synopsis](topology_layer_2_info_module.md#id1)

- Get Topology Layer 2 by id.
- Returns Layer 2 network topology by specified VLAN ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](topology_layer_2_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](topology_layer_2_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **vlanID**  string | VlanID path parameter. Vlan Name for e.g Vlan1, Vlan23 etc. |

## [Notes](topology_layer_2_info_module.md#id4)

> **Note:**
>
> - SDK Method used are topology.Topology.get_topology_details,
> - Paths used are get /dna/intent/api/v1/topology/l2/{vlanID},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](topology_layer_2_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Topology GetTopologyDetails](https://developer.cisco.com/docs/dna-center/#!get-topology-details)
> :   Complete reference of the GetTopologyDetails API.

## [Examples](topology_layer_2_info_module.md#id6)

```yaml+jinja
- name: Get Topology Layer 2 by id
  cisco.dnac.topology_layer_2_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    vlanID: string
  register: result
```

## [Return Values](topology_layer_2_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"id": "string", "links": [{"additionalInfo": {}, "endPortID": "string", "endPortIpv4Address": "string", "endPortIpv4Mask": "string", "endPortName": "string", "endPortSpeed": "string", "greyOut": true, "id": "string", "linkStatus": "string", "source": "string", "startPortID": "string", "startPortIpv4Address": "string", "startPortIpv4Mask": "string", "startPortName": "string", "startPortSpeed": "string", "tag": "string", "target": "string"}], "nodes": [{"aclApplied": true, "additionalInfo": {}, "customParam": {"id": "string", "label": "string", "parentNodeId": "string", "x": 0, "y": 0}, "dataPathId": "string", "deviceType": "string", "family": "string", "fixed": true, "greyOut": true, "id": "string", "ip": "string", "label": "string", "networkType": "string", "nodeType": "string", "order": 0, "osType": "string", "platformId": "string", "role": "string", "roleSource": "string", "softwareVersion": "string", "tags": ["string"], "upperNode": "string", "userId": "string", "vlanId": "string", "x": 0, "y": 0}]}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
