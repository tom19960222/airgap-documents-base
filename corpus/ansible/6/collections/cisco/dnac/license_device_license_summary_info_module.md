---
collection: ansible
version: "6"
title: "cisco.dnac.license_device_license_summary_info module – Information module for License Device License Summary"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/license_device_license_summary_info_module.html
fetched_at: 2026-07-27T16:52:31+00:00
---
# cisco.dnac.license_device_license_summary_info module – Information module for License Device License Summary

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
> see [Requirements](license_device_license_summary_info_module.md#ansible-collections-cisco-dnac-license-device-license-summary-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.license_device_license_summary_info`.

New in cisco.dnac 3.1.0

- [Synopsis](license_device_license_summary_info_module.md#synopsis)
- [Requirements](license_device_license_summary_info_module.md#requirements)
- [Parameters](license_device_license_summary_info_module.md#parameters)
- [Notes](license_device_license_summary_info_module.md#notes)
- [See Also](license_device_license_summary_info_module.md#see-also)
- [Examples](license_device_license_summary_info_module.md#examples)
- [Return Values](license_device_license_summary_info_module.md#return-values)

## [Synopsis](license_device_license_summary_info_module.md#id1)

- Get all License Device License Summary.
- Show license summary of devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](license_device_license_summary_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](license_device_license_summary_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **device_type**  string | Device_type query parameter. Type of device. |
| **device_uuid**  string | Device_uuid query parameter. Id of device. |
| **dna_level**  string | Dna_level query parameter. Device Cisco DNA license level. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. |
| **order**  string | Order query parameter. Sorting order. |
| **page_number**  integer | Page_number query parameter. Page number of response. |
| **registration_status**  string | Registration_status query parameter. Smart license registration status of device. |
| **smart_account_id**  integer | Smart_account_id query parameter. Id of smart account. |
| **sort_by**  string | Sort_by query parameter. Sort result by field. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **virtual_account_name**  string | Virtual_account_name query parameter. Name of virtual account. |

## [Notes](license_device_license_summary_info_module.md#id4)

> **Note:**
>
> - SDK Method used are licenses.Licenses.device_license_summary,
> - Paths used are get /dna/intent/api/v1/licenses/device/summary,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](license_device_license_summary_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Licenses DeviceLicenseSummary](https://developer.cisco.com/docs/dna-center/#!device-license-summary)
> :   Complete reference of the DeviceLicenseSummary API.

## [Examples](license_device_license_summary_info_module.md#id6)

```yaml+jinja
- name: Get all License Device License Summary
  cisco.dnac.license_device_license_summary_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    page_number: 0
    order: string
    sort_by: string
    dna_level: string
    device_type: string
    limit: 0
    registration_status: string
    virtual_account_name: string
    smart_account_id: 0
    device_uuid: string
  register: result
```

## [Return Values](license_device_license_summary_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `"[\n  {\n    \"authorization_status\": \"string\",\n    \"last_updated_time\": \"string\",\n    \"is_performance_allowed\": true,\n    \"sle_auth_code\": \"string\",\n    \"throughput_level\": \"string\",\n    \"hsec_status\": \"string\",\n    \"device_uuid\": \"string\",\n    \"site\": \"string\",\n    \"total_access_point_count\": 0,\n    \"model\": \"string\",\n    \"is_wireless_capable\": true,\n    \"registration_status\": \"string\",\n    \"sle_state\": \"string\",\n    \"performance_license\": \"string\",\n    \"license_mode\": \"string\",\n    \"is_license_expired\": true,\n    \"software_version\": \"string\",\n    \"reservation_status\": \"string\",\n    \"is_wireless\": true,\n    \"network_license\": \"string\",\n    \"evaluation_license_expiry\": \"string\",\n    \"wireless_capable_network_license\": \"string\",\n    \"device_name\": \"string\",\n    \"device_type\": \"string\",\n    \"dna_level\": \"string\",\n    \"virtual_account_name\": \"string\",\n    \"last_successful_rum_usage_upload_time\": \"string\",\n    \"ip_address\": \"string\",\n    \"wireless_capable_dna_license\": \"string\",\n    \"mac_address\": \"string\",\n    \"customer_tag1\": \"string\",\n    \"customer_tag2\": \"string\",\n    \"customer_tag3\": \"string\",\n    \"customer_tag4\": \"string\",\n    \"smart_account_name\": \"string\"\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
