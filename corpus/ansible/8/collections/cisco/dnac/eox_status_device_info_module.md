---
collection: ansible
version: "8"
title: "cisco.dnac.eox_status_device_info module – Information module for Eox Status Device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/eox_status_device_info_module.html
fetched_at: 2026-07-28T01:22:17+00:00
---
# cisco.dnac.eox_status_device_info module – Information module for Eox Status Device

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
> see [Requirements](eox_status_device_info_module.md#ansible-collections-cisco-dnac-eox-status-device-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.eox_status_device_info`.

New in cisco.dnac 6.7.0

- [Synopsis](eox_status_device_info_module.md#synopsis)
- [Requirements](eox_status_device_info_module.md#requirements)
- [Parameters](eox_status_device_info_module.md#parameters)
- [Notes](eox_status_device_info_module.md#notes)
- [See Also](eox_status_device_info_module.md#see-also)
- [Examples](eox_status_device_info_module.md#examples)
- [Return Values](eox_status_device_info_module.md#return-values)

## [Synopsis](eox_status_device_info_module.md#id1)

- Get all Eox Status Device.
- Get Eox Status Device by id.
- Retrieves EoX details for a device.
- Retrieves EoX status for all devices in the network.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](eox_status_device_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](eox_status_device_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceId**  string | DeviceId path parameter. Device instance UUID. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](eox_status_device_info_module.md#id4)

> **Note:**
>
> - SDK Method used are eo_x.EoX.get_eo_x_details_per_device, eo_x.EoX.get_eo_x_status_for_all_devices,
> - Paths used are get /dna/intent/api/v1/eox-status/device, get /dna/intent/api/v1/eox-status/device/{deviceId},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](eox_status_device_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for EoX GetEoXDetailsPerDevice](https://developer.cisco.com/docs/dna-center/#!get-eo-x-details-per-device)
> :   Complete reference of the GetEoXDetailsPerDevice API.
>
> [Cisco DNA Center documentation for EoX GetEoXStatusForAllDevices](https://developer.cisco.com/docs/dna-center/#!get-eo-x-status-for-all-devices)
> :   Complete reference of the GetEoXStatusForAllDevices API.

## [Examples](eox_status_device_info_module.md#id6)

```yaml+jinja
- name: Get all Eox Status Device
  cisco.dnac.eox_status_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

- name: Get Eox Status Device by id
  cisco.dnac.eox_status_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
  register: result
```

## [Return Values](eox_status_device_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"alertCount": 0, "comments": [{}], "deviceId": "string", "eoxDetails": [{"bulletinHeadline": "string", "bulletinNumber": "string", "bulletinURL": "string", "endOfHardwareNewServiceAttachmentDate": 0, "endOfHardwareServiceContractRenewalDate": 0, "endOfLastHardwareShipDate": 0, "endOfLifeDate": 0, "endOfLifeExternalAnnouncementDate": 0, "endOfSaleDate": 0, "endOfSignatureReleasesDate": 0, "endOfSoftwareMaintenanceReleasesDate": 0, "endOfSoftwareVulnerabilityOrSecuritySupportDate": 0, "endOfSoftwareVulnerabilityOrSecuritySupportDateHw": 0, "eoxAlertType": "string", "lastDateOfSupport": 0, "name": "string"}], "lastScanTime": 0, "scanStatus": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
