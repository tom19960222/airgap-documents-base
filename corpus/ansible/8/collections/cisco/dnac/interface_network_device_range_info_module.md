---
collection: ansible
version: "8"
title: "cisco.dnac.interface_network_device_range_info module – Information module for Interface Network Device Range"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/interface_network_device_range_info_module.html
fetched_at: 2026-07-28T01:22:57+00:00
---
# cisco.dnac.interface_network_device_range_info module – Information module for Interface Network Device Range

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
> see [Requirements](interface_network_device_range_info_module.md#ansible-collections-cisco-dnac-interface-network-device-range-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.interface_network_device_range_info`.

New in cisco.dnac 3.1.0

- [Synopsis](interface_network_device_range_info_module.md#synopsis)
- [Requirements](interface_network_device_range_info_module.md#requirements)
- [Parameters](interface_network_device_range_info_module.md#parameters)
- [Notes](interface_network_device_range_info_module.md#notes)
- [See Also](interface_network_device_range_info_module.md#see-also)
- [Examples](interface_network_device_range_info_module.md#examples)
- [Return Values](interface_network_device_range_info_module.md#return-values)

## [Synopsis](interface_network_device_range_info_module.md#id1)

- Get all Interface Network Device Range.
- Returns the list of interfaces for the device for the specified range.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](interface_network_device_range_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](interface_network_device_range_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceId**  string | DeviceId path parameter. Device ID. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **recordsToReturn**  integer | RecordsToReturn path parameter. Number of records to return. |
| **startIndex**  integer | StartIndex path parameter. Start index. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](interface_network_device_range_info_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.get_device_interfaces_by_specified_range,
> - Paths used are get /dna/intent/api/v1/interface/network-device/{deviceId}/{startIndex}/{recordsToReturn},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](interface_network_device_range_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices GetDeviceInterfacesBySpecifiedRange](https://developer.cisco.com/docs/dna-center/#!get-device-interfaces-by-specified-range)
> :   Complete reference of the GetDeviceInterfacesBySpecifiedRange API.

## [Examples](interface_network_device_range_info_module.md#id6)

```yaml+jinja
- name: Get all Interface Network Device Range
  cisco.dnac.interface_network_device_range_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
    startIndex: 0
    recordsToReturn: 0
  register: result
```

## [Return Values](interface_network_device_range_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": [{"adminStatus": "string", "className": "string", "description": "string", "deviceId": "string", "duplex": "string", "id": "string", "ifIndex": "string", "instanceTenantId": "string", "instanceUuid": "string", "interfaceType": "string", "ipv4Address": "string", "ipv4Mask": "string", "isisSupport": "string", "lastUpdated": "string", "macAddress": "string", "mappedPhysicalInterfaceId": "string", "mappedPhysicalInterfaceName": "string", "mediaType": "string", "nativeVlanId": "string", "ospfSupport": "string", "pid": "string", "portMode": "string", "portName": "string", "portType": "string", "serialNo": "string", "series": "string", "speed": "string", "status": "string", "vlanId": "string", "voiceVlan": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
