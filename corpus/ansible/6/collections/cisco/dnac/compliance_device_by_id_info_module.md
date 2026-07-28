---
collection: ansible
version: "6"
title: "cisco.dnac.compliance_device_by_id_info module – Information module for Compliance Device By Id"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/compliance_device_by_id_info_module.html
fetched_at: 2026-07-27T16:51:11+00:00
---
# cisco.dnac.compliance_device_by_id_info module – Information module for Compliance Device By Id

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
> see [Requirements](compliance_device_by_id_info_module.md#ansible-collections-cisco-dnac-compliance-device-by-id-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.compliance_device_by_id_info`.

New in cisco.dnac 3.1.0

- [Synopsis](compliance_device_by_id_info_module.md#synopsis)
- [Requirements](compliance_device_by_id_info_module.md#requirements)
- [Parameters](compliance_device_by_id_info_module.md#parameters)
- [Notes](compliance_device_by_id_info_module.md#notes)
- [See Also](compliance_device_by_id_info_module.md#see-also)
- [Examples](compliance_device_by_id_info_module.md#examples)
- [Return Values](compliance_device_by_id_info_module.md#return-values)

## [Synopsis](compliance_device_by_id_info_module.md#id1)

- Get all Compliance Device By Id.
- Return compliance detailed report for a device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](compliance_device_by_id_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](compliance_device_by_id_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **category**  string | Category query parameter. ComplianceCategory can have any value among ‘INTENT’, ‘RUNNING_CONFIG’. |
| **complianceType**  string | ComplianceType query parameter. ComplianceType can have any value among ‘NETWORK_DESIGN’, ‘NETWORK_PROFILE’, ‘FABRIC’, ‘POLICY’, ‘RUNNING_CONFIG’. |
| **deviceUuid**  string | DeviceUuid path parameter. |
| **diffList**  boolean | DiffList query parameter. Diff list pass true to fetch the diff list.  Choices:   - `false` - `true` |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **key**  string | Key query parameter. Extended attribute key. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **value**  string | Value query parameter. Extended attribute value. |

## [Notes](compliance_device_by_id_info_module.md#id4)

> **Note:**
>
> - SDK Method used are compliance.Compliance.compliance_details_of_device,
> - Paths used are get /dna/intent/api/v1/compliance/{deviceUuid}/detail,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](compliance_device_by_id_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Compliance ComplianceDetailsOfDevice](https://developer.cisco.com/docs/dna-center/#!compliance-details-of-device)
> :   Complete reference of the ComplianceDetailsOfDevice API.

## [Examples](compliance_device_by_id_info_module.md#id6)

```yaml+jinja
- name: Get all Compliance Device By Id
  cisco.dnac.compliance_device_by_id_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    category: string
    complianceType: string
    diffList: True
    key: string
    value: string
    deviceUuid: string
  register: result
```

## [Return Values](compliance_device_by_id_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"deviceUuid": "string", "response": [{"additionalDataURL": "string", "category": "string", "complianceType": "string", "deviceUuid": "string", "displayName": "string", "lastSyncTime": "string", "lastUpdateTime": 0, "message": "string", "sourceInfoList": [{"appName": "string", "businessKey": {"businessKeyAttributes": "string", "otherAttributes": {"cfsAttributes": "string", "name": "string"}, "resourceName": "string"}, "count": 0, "diffList": [{"businessKey": "string", "configuredValue": "string", "displayName": "string", "extendedAttributes": "string", "intendedValue": "string", "moveFromPath": "string", "op": "string", "path": "string"}], "displayName": "string", "licenseAppName": "string", "name": "string", "nameWithBusinessKey": "string", "networkProfileName": "string", "provisioningArea": "string", "sourceEnum": "string", "type": "string"}], "state": "string", "status": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
