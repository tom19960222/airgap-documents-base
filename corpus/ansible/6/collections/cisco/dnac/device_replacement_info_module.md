---
collection: ansible
version: "6"
title: "cisco.dnac.device_replacement_info module – Information module for Device Replacement"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/device_replacement_info_module.html
fetched_at: 2026-07-27T16:51:37+00:00
---
# cisco.dnac.device_replacement_info module – Information module for Device Replacement

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
> see [Requirements](device_replacement_info_module.md#ansible-collections-cisco-dnac-device-replacement-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.device_replacement_info`.

New in cisco.dnac 3.1.0

- [Synopsis](device_replacement_info_module.md#synopsis)
- [Requirements](device_replacement_info_module.md#requirements)
- [Parameters](device_replacement_info_module.md#parameters)
- [Notes](device_replacement_info_module.md#notes)
- [See Also](device_replacement_info_module.md#see-also)
- [Examples](device_replacement_info_module.md#examples)
- [Return Values](device_replacement_info_module.md#return-values)

## [Synopsis](device_replacement_info_module.md#id1)

- Get all Device Replacement.
- Get list of replacement devices with replacement details and it can filter replacement devices based on Faulty Device Name,Faulty Device Platform, Replacement Device Platform, Faulty Device Serial Number,Replacement Device Serial Number, Device Replacement status, Product Family.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_replacement_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](device_replacement_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **family**  list / elements=string | Family query parameter. List of familiesRouters, Switches and Hubs, AP. |
| **faultyDeviceName**  string | FaultyDeviceName query parameter. Faulty Device Name. |
| **faultyDevicePlatform**  string | FaultyDevicePlatform query parameter. Faulty Device Platform. |
| **faultyDeviceSerialNumber**  string | FaultyDeviceSerialNumber query parameter. Faulty Device Serial Number. |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. |
| **offset**  integer | Offset query parameter. |
| **replacementDevicePlatform**  string | ReplacementDevicePlatform query parameter. Replacement Device Platform. |
| **replacementDeviceSerialNumber**  string | ReplacementDeviceSerialNumber query parameter. Replacement Device Serial Number. |
| **replacementStatus**  list / elements=string | ReplacementStatus query parameter. Device Replacement status READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR, NETWORK_READINESS_REQUESTED, NETWORK_READINESS_FAILED. |
| **sortBy**  string | SortBy query parameter. SortBy this field. SortBy is mandatory when order is used. |
| **sortOrder**  string | SortOrder query parameter. Order on displayNameASC,DESC. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](device_replacement_info_module.md#id4)

> **Note:**
>
> - SDK Method used are device_replacement.DeviceReplacement.return_replacement_devices_with_details,
> - Paths used are get /dna/intent/api/v1/device-replacement,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](device_replacement_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Replacement ReturnListOfReplacementDevicesWithReplacementDetails](https://developer.cisco.com/docs/dna-center/#!return-list-of-replacement-devices-with-replacement-details)
> :   Complete reference of the ReturnListOfReplacementDevicesWithReplacementDetails API.

## [Examples](device_replacement_info_module.md#id6)

```yaml+jinja
- name: Get all Device Replacement
  cisco.dnac.device_replacement_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    faultyDeviceName: string
    faultyDevicePlatform: string
    replacementDevicePlatform: string
    faultyDeviceSerialNumber: string
    replacementDeviceSerialNumber: string
    replacementStatus: []
    family: []
    sortBy: string
    sortOrder: string
    offset: 0
    limit: 0
  register: result
```

## [Return Values](device_replacement_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"creationTime": 0, "family": "string", "faultyDeviceId": "string", "faultyDeviceName": "string", "faultyDevicePlatform": "string", "faultyDeviceSerialNumber": "string", "id": "string", "neighbourDeviceId": "string", "networkReadinessTaskId": "string", "replacementDevicePlatform": "string", "replacementDeviceSerialNumber": "string", "replacementStatus": "string", "replacementTime": 0, "workflowId": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
