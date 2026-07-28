---
collection: ansible
version: "6"
title: "cisco.dnac.license_device_license_details_info module – Information module for License Device License Details"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/license_device_license_details_info_module.html
fetched_at: 2026-07-27T16:52:31+00:00
---
# cisco.dnac.license_device_license_details_info module – Information module for License Device License Details

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
> see [Requirements](license_device_license_details_info_module.md#ansible-collections-cisco-dnac-license-device-license-details-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.license_device_license_details_info`.

New in cisco.dnac 3.1.0

- [Synopsis](license_device_license_details_info_module.md#synopsis)
- [Requirements](license_device_license_details_info_module.md#requirements)
- [Parameters](license_device_license_details_info_module.md#parameters)
- [Notes](license_device_license_details_info_module.md#notes)
- [See Also](license_device_license_details_info_module.md#see-also)
- [Examples](license_device_license_details_info_module.md#examples)
- [Return Values](license_device_license_details_info_module.md#return-values)

## [Synopsis](license_device_license_details_info_module.md#id1)

- Get all License Device License Details.
- Get detailed license information of a device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](license_device_license_details_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](license_device_license_details_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **device_uuid**  string | Device_uuid path parameter. Id of device. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](license_device_license_details_info_module.md#id4)

> **Note:**
>
> - SDK Method used are licenses.Licenses.device_license_details,
> - Paths used are get /dna/intent/api/v1/licenses/device/{device_uuid}/details,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](license_device_license_details_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Licenses DeviceLicenseDetails](https://developer.cisco.com/docs/dna-center/#!device-license-details)
> :   Complete reference of the DeviceLicenseDetails API.

## [Examples](license_device_license_details_info_module.md#id6)

```yaml+jinja
- name: Get all License Device License Details
  cisco.dnac.license_device_license_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    device_uuid: string
  register: result
```

## [Return Values](license_device_license_details_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"[\n  {\n    \"device_uuid\": \"string\",\n    \"site\": \"string\",\n    \"model\": \"string\",\n    \"license_mode\": \"string\",\n    \"is_license_expired\": true,\n    \"software_version\": \"string\",\n    \"network_license\": \"string\",\n    \"evaluation_license_expiry\": \"string\",\n    \"device_name\": \"string\",\n    \"device_type\": \"string\",\n    \"dna_level\": \"string\",\n    \"virtual_account_name\": \"string\",\n    \"ip_address\": \"string\",\n    \"mac_address\": \"string\",\n    \"sntc_status\": \"string\",\n    \"feature_license\": [\n      \"string\"\n    ],\n    \"has_sup_cards\": true,\n    \"udi\": \"string\",\n    \"stacked_devices\": [\n      {\n        \"mac_address\": \"string\",\n        \"id\": \"string\",\n        \"role\": \"string\",\n        \"serial_number\": \"string\"\n      }\n    ],\n    \"is_stacked_device\": true,\n    \"access_points\": [\n      {\n        \"ap_type\": \"string\",\n        \"count\": \"string\"\n      }\n    ],\n    \"chassis_details\": {\n      \"board_serial_number\": \"string\",\n      \"modules\": [\n        {\n          \"module_type\": \"string\",\n          \"module_name\": \"string\",\n          \"serial_number\": \"string\",\n          \"id\": \"string\"\n        }\n      ],\n      \"supervisor_cards\": [\n        {\n          \"serial_number\": \"string\",\n          \"supervisor_card_type\": \"string\",\n          \"status\": \"string\"\n        }\n      ],\n      \"port\": 0\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
