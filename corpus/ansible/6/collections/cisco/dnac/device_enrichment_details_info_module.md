---
collection: ansible
version: "6"
title: "cisco.dnac.device_enrichment_details_info module – Information module for Device Enrichment Details"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/device_enrichment_details_info_module.html
fetched_at: 2026-07-27T16:51:30+00:00
---
# cisco.dnac.device_enrichment_details_info module – Information module for Device Enrichment Details

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](device_enrichment_details_info_module.md#ansible-collections-cisco-dnac-device-enrichment-details-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.device_enrichment_details_info`.

New in cisco.dnac 3.1.0

- [Synopsis](device_enrichment_details_info_module.md#synopsis)
- [Requirements](device_enrichment_details_info_module.md#requirements)
- [Parameters](device_enrichment_details_info_module.md#parameters)
- [Notes](device_enrichment_details_info_module.md#notes)
- [See Also](device_enrichment_details_info_module.md#see-also)
- [Examples](device_enrichment_details_info_module.md#examples)
- [Return Values](device_enrichment_details_info_module.md#return-values)

## [Synopsis](device_enrichment_details_info_module.md#id1)

- Get all Device Enrichment Details.
- Enriches a given network device context device id or device Mac Address or device management IP address with details about the device and neighbor topology.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_enrichment_details_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](device_enrichment_details_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](device_enrichment_details_info_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.get_device_enrichment_details,
> - Paths used are get /dna/intent/api/v1/device-enrichment-details,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](device_enrichment_details_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices GetDeviceEnrichmentDetails](https://developer.cisco.com/docs/dna-center/#!get-device-enrichment-details)
> :   Complete reference of the GetDeviceEnrichmentDetails API.

## [Examples](device_enrichment_details_info_module.md#id6)

```yaml+jinja
- name: Get all Device Enrichment Details
  cisco.dnac.device_enrichment_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
```

## [Return Values](device_enrichment_details_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"[\n  {\n    \"deviceDetails\": {\n      \"family\": \"string\",\n      \"type\": \"string\",\n      \"location\": {},\n      \"errorCode\": \"string\",\n      \"macAddress\": \"string\",\n      \"role\": \"string\",\n      \"apManagerInterfaceIp\": \"string\",\n      \"associatedWlcIp\": \"string\",\n      \"bootDateTime\": \"string\",\n      \"collectionStatus\": \"string\",\n      \"interfaceCount\": \"string\",\n      \"lineCardCount\": \"string\",\n      \"lineCardId\": \"string\",\n      \"managementIpAddress\": \"string\",\n      \"memorySize\": \"string\",\n      \"platformId\": \"string\",\n      \"reachabilityFailureReason\": \"string\",\n      \"reachabilityStatus\": \"string\",\n      \"snmpContact\": \"string\",\n      \"snmpLocation\": \"string\",\n      \"tunnelUdpPort\": {},\n      \"waasDeviceMode\": {},\n      \"series\": \"string\",\n      \"inventoryStatusDetail\": \"string\",\n      \"collectionInterval\": \"string\",\n      \"serialNumber\": \"string\",\n      \"softwareVersion\": \"string\",\n      \"roleSource\": \"string\",\n      \"hostname\": \"string\",\n      \"upTime\": \"string\",\n      \"lastUpdateTime\": 0,\n      \"errorDescription\": \"string\",\n      \"locationName\": {},\n      \"tagCount\": \"string\",\n      \"lastUpdated\": \"string\",\n      \"instanceUuid\": \"string\",\n      \"id\": \"string\",\n      \"neighborTopology\": [\n        {\n          \"nodes\": [\n            {\n              \"role\": \"string\",\n              \"name\": \"string\",\n              \"id\": \"string\",\n              \"description\": \"string\",\n              \"deviceType\": \"string\",\n              \"platformId\": \"string\",\n              \"family\": \"string\",\n              \"ip\": \"string\",\n              \"softwareVersion\": \"string\",\n              \"userId\": {},\n              \"nodeType\": \"string\",\n              \"radioFrequency\": {},\n              \"clients\": {},\n              \"count\": {},\n              \"healthScore\": 0,\n              \"level\": 0,\n              \"fabricGroup\": {},\n              \"connectedDevice\": {}\n            }\n          ],\n          \"links\": [\n            {\n              \"source\": \"string\",\n              \"linkStatus\": \"string\",\n              \"label\": [\n                {}\n              ],\n              \"target\": \"string\",\n              \"id\": {},\n              \"portUtilization\": {}\n            }\n          ]\n        }\n      ]\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
