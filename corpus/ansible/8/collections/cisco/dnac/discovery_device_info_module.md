---
collection: ansible
version: "8"
title: "cisco.dnac.discovery_device_info module – Information module for Discovery Device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/discovery_device_info_module.html
fetched_at: 2026-07-28T01:22:09+00:00
---
# cisco.dnac.discovery_device_info module – Information module for Discovery Device

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
> see [Requirements](discovery_device_info_module.md#ansible-collections-cisco-dnac-discovery-device-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.discovery_device_info`.

New in cisco.dnac 3.1.0

- [Synopsis](discovery_device_info_module.md#synopsis)
- [Requirements](discovery_device_info_module.md#requirements)
- [Parameters](discovery_device_info_module.md#parameters)
- [Notes](discovery_device_info_module.md#notes)
- [See Also](discovery_device_info_module.md#see-also)
- [Examples](discovery_device_info_module.md#examples)
- [Return Values](discovery_device_info_module.md#return-values)

## [Synopsis](discovery_device_info_module.md#id1)

- Get all Discovery Device.
- Returns the network devices discovered for the given Discovery ID. Discovery ID can be obtained using the “Get Discoveries by range” API.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](discovery_device_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](discovery_device_info_module.md#id3)

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
| **id**  string | Id path parameter. Discovery ID. |
| **taskId**  string | TaskId query parameter. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](discovery_device_info_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.get_discovered_network_devices_by_discovery_id,
> - Paths used are get /dna/intent/api/v1/discovery/{id}/network-device,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](discovery_device_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery GetDiscoveredNetworkDevicesByDiscoveryId](https://developer.cisco.com/docs/dna-center/#!get-discovered-network-devices-by-discovery-id)
> :   Complete reference of the GetDiscoveredNetworkDevicesByDiscoveryId API.

## [Examples](discovery_device_info_module.md#id6)

```yaml+jinja
- name: Get all Discovery Device
  cisco.dnac.discovery_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    taskId: string
    id: string
  register: result
```

## [Return Values](discovery_device_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": [{"anchorWlcForAp": "string", "authModelId": "string", "avgUpdateFrequency": 0, "bootDateTime": "string", "cliStatus": "string", "duplicateDeviceId": "string", "errorCode": "string", "errorDescription": "string", "family": "string", "hostname": "string", "httpStatus": "string", "id": "string", "imageName": "string", "ingressQueueConfig": "string", "interfaceCount": "string", "inventoryCollectionStatus": "string", "inventoryReachabilityStatus": "string", "lastUpdated": "string", "lineCardCount": "string", "lineCardId": "string", "location": "string", "locationName": "string", "macAddress": "string", "managementIpAddress": "string", "memorySize": "string", "netconfStatus": "string", "numUpdates": 0, "pingStatus": "string", "platformId": "string", "portRange": "string", "qosStatus": "string", "reachabilityFailureReason": "string", "reachabilityStatus": "string", "role": "string", "roleSource": "string", "serialNumber": "string", "snmpContact": "string", "snmpLocation": "string", "snmpStatus": "string", "softwareVersion": "string", "tag": "string", "tagCount": 0, "type": "string", "upTime": "string", "vendor": "string", "wlcApDeviceStatus": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
