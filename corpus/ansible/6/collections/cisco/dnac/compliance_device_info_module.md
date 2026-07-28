---
collection: ansible
version: "6"
title: "cisco.dnac.compliance_device_info module – Information module for Compliance Device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/compliance_device_info_module.html
fetched_at: 2026-07-27T16:51:13+00:00
---
# cisco.dnac.compliance_device_info module – Information module for Compliance Device

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
> see [Requirements](compliance_device_info_module.md#ansible-collections-cisco-dnac-compliance-device-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.compliance_device_info`.

New in cisco.dnac 3.1.0

- [Synopsis](compliance_device_info_module.md#synopsis)
- [Requirements](compliance_device_info_module.md#requirements)
- [Parameters](compliance_device_info_module.md#parameters)
- [Notes](compliance_device_info_module.md#notes)
- [See Also](compliance_device_info_module.md#see-also)
- [Examples](compliance_device_info_module.md#examples)
- [Return Values](compliance_device_info_module.md#return-values)

## [Synopsis](compliance_device_info_module.md#id1)

- Get all Compliance Device.
- Get Compliance Device by id.
- Return compliance status of a device.
- Return compliance status of devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](compliance_device_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](compliance_device_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **complianceStatus**  string | ComplianceStatus query parameter. Compliance status can be have value among ‘COMPLIANT’,’NON_COMPLIANT’,’IN_PROGRESS’, ‘ERROR’. |
| **deviceUuid**  string | DeviceUuid query parameter. Comma separated deviceUuids. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. Number of records to be retrieved. |
| **offset**  integer | Offset query parameter. Offset/starting row. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](compliance_device_info_module.md#id4)

> **Note:**
>
> - SDK Method used are compliance.Compliance.device_compliance_status, compliance.Compliance.get_compliance_status,
> - Paths used are get /dna/intent/api/v1/compliance, get /dna/intent/api/v1/compliance/{deviceUuid},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](compliance_device_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Compliance DeviceComplianceStatus](https://developer.cisco.com/docs/dna-center/#!device-compliance-status)
> :   Complete reference of the DeviceComplianceStatus API.
>
> [Cisco DNA Center documentation for Compliance GetComplianceStatus](https://developer.cisco.com/docs/dna-center/#!get-compliance-status)
> :   Complete reference of the GetComplianceStatus API.

## [Examples](compliance_device_info_module.md#id6)

```yaml+jinja
- name: Get all Compliance Device
  cisco.dnac.compliance_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    complianceStatus: string
    deviceUuid: string
    offset: 0
    limit: 0
  register: result

- name: Get Compliance Device by id
  cisco.dnac.compliance_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceUuid: string
  register: result
```

## [Return Values](compliance_device_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"complianceStatus": "string", "deviceUuid": "string", "lastUpdateTime": 0, "message": "string", "scheduleTime": 0}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
