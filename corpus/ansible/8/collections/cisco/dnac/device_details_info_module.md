---
collection: ansible
version: "8"
title: "cisco.dnac.device_details_info module – Information module for Device Details"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/device_details_info_module.html
fetched_at: 2026-07-28T01:21:54+00:00
---
# cisco.dnac.device_details_info module – Information module for Device Details

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
> see [Requirements](device_details_info_module.md#ansible-collections-cisco-dnac-device-details-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.device_details_info`.

New in cisco.dnac 3.1.0

- [Synopsis](device_details_info_module.md#synopsis)
- [Requirements](device_details_info_module.md#requirements)
- [Parameters](device_details_info_module.md#parameters)
- [Notes](device_details_info_module.md#notes)
- [See Also](device_details_info_module.md#see-also)
- [Examples](device_details_info_module.md#examples)
- [Return Values](device_details_info_module.md#return-values)

## [Synopsis](device_details_info_module.md#id1)

- Get all Device Details.
- Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of time.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_details_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](device_details_info_module.md#id3)

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
| **identifier**  string | Identifier query parameter. One of keywords macAddress or uuid or nwDeviceName. |
| **searchBy**  string | SearchBy query parameter. MAC Address or Device Name value or UUID of the network device. |
| **timestamp**  string | Timestamp query parameter. Epoch time(in milliseconds) when the device data is required. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](device_details_info_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.get_device_detail,
> - Paths used are get /dna/intent/api/v1/device-detail,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](device_details_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices GetDeviceDetail](https://developer.cisco.com/docs/dna-center/#!get-device-detail)
> :   Complete reference of the GetDeviceDetail API.

## [Examples](device_details_info_module.md#id6)

```yaml+jinja
- name: Get all Device Details
  cisco.dnac.device_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    timestamp: string
    searchBy: string
    identifier: string
  register: result
```

## [Return Values](device_details_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"HALastResetReason": "string", "HAPrimaryPowerStatus": "string", "HASecondaryPowerStatus": "string", "airQuality": "string", "airQualityScore": 0, "clientCount": "string", "collectionStatus": "string", "communicationState": "string", "cpu": "string", "cpuScore": 0, "deviceSeries": "string", "freeMbuf": "string", "freeMbufScore": 0, "freeTimer": "string", "freeTimerScore": 0, "interference": "string", "interferenceScore": 0, "location": "string", "macAddress": "string", "managementIpAddr": "string", "memory": "string", "memoryScore": 0, "noise": "string", "noiseScore": 0, "nwDeviceFamily": "string", "nwDeviceId": "string", "nwDeviceName": "string", "nwDeviceRole": "string", "nwDeviceType": "string", "osType": "string", "overallHealth": 0, "packetPool": "string", "packetPoolScore": 0, "platformId": "string", "redundancyMode": "string", "redundancyPeerState": "string", "redundancyState": "string", "redundancyUnit": "string", "softwareVersion": "string", "timestamp": "string", "utilization": "string", "utilizationScore": 0, "wqe": "string", "wqeScore": 0}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
