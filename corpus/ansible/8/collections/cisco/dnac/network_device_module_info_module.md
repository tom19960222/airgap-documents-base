---
collection: ansible
version: "8"
title: "cisco.dnac.network_device_module_info module – Information module for Network Device Module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/network_device_module_info_module.html
fetched_at: 2026-07-28T01:23:32+00:00
---
# cisco.dnac.network_device_module_info module – Information module for Network Device Module

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
> see [Requirements](network_device_module_info_module.md#ansible-collections-cisco-dnac-network-device-module-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.network_device_module_info`.

New in cisco.dnac 3.1.0

- [Synopsis](network_device_module_info_module.md#synopsis)
- [Requirements](network_device_module_info_module.md#requirements)
- [Parameters](network_device_module_info_module.md#parameters)
- [Notes](network_device_module_info_module.md#notes)
- [See Also](network_device_module_info_module.md#see-also)
- [Examples](network_device_module_info_module.md#examples)
- [Return Values](network_device_module_info_module.md#return-values)

## [Synopsis](network_device_module_info_module.md#id1)

- Get all Network Device Module.
- Get Network Device Module by id.
- Returns Module info by ‘module id’.
- Returns modules by specified device id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](network_device_module_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](network_device_module_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceId**  string | DeviceId query parameter. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **id**  string | Id path parameter. Module id. |
| **limit**  integer | Limit query parameter. |
| **nameList**  list / elements=string | NameList query parameter. |
| **offset**  integer | Offset query parameter. |
| **operationalStateCodeList**  list / elements=string | OperationalStateCodeList query parameter. |
| **partNumberList**  list / elements=string | PartNumberList query parameter. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **vendorEquipmentTypeList**  list / elements=string | VendorEquipmentTypeList query parameter. |

## [Notes](network_device_module_info_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.get_module_info_by_id, devices.Devices.get_modules,
> - Paths used are get /dna/intent/api/v1/network-device/module, get /dna/intent/api/v1/network-device/module/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](network_device_module_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices GetModuleInfoById](https://developer.cisco.com/docs/dna-center/#!get-module-info-by-id)
> :   Complete reference of the GetModuleInfoById API.
>
> [Cisco DNA Center documentation for Devices GetModules](https://developer.cisco.com/docs/dna-center/#!get-modules)
> :   Complete reference of the GetModules API.

## [Examples](network_device_module_info_module.md#id6)

```yaml+jinja
- name: Get all Network Device Module
  cisco.dnac.network_device_module_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
    limit: 0
    offset: 0
    nameList: []
    vendorEquipmentTypeList: []
    partNumberList: []
    operationalStateCodeList: []
  register: result

- name: Get Network Device Module by id
  cisco.dnac.network_device_module_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
```

## [Return Values](network_device_module_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"assemblyNumber": "string", "assemblyRevision": "string", "attributeInfo": {}, "containmentEntity": "string", "description": "string", "entityPhysicalIndex": "string", "id": "string", "isFieldReplaceable": "string", "isReportingAlarmsAllowed": "string", "manufacturer": "string", "moduleIndex": 0, "name": "string", "operationalStateCode": "string", "partNumber": "string", "serialNumber": "string", "vendorEquipmentType": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
