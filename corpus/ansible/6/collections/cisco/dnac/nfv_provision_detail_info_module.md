---
collection: ansible
version: "6"
title: "cisco.dnac.nfv_provision_detail_info module – Information module for Nfv Provision Detail"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/nfv_provision_detail_info_module.html
fetched_at: 2026-07-27T16:53:05+00:00
---
# cisco.dnac.nfv_provision_detail_info module – Information module for Nfv Provision Detail

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
> see [Requirements](nfv_provision_detail_info_module.md#ansible-collections-cisco-dnac-nfv-provision-detail-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.nfv_provision_detail_info`.

New in cisco.dnac 3.1.0

- [Synopsis](nfv_provision_detail_info_module.md#synopsis)
- [Requirements](nfv_provision_detail_info_module.md#requirements)
- [Parameters](nfv_provision_detail_info_module.md#parameters)
- [Notes](nfv_provision_detail_info_module.md#notes)
- [See Also](nfv_provision_detail_info_module.md#see-also)
- [Examples](nfv_provision_detail_info_module.md#examples)
- [Return Values](nfv_provision_detail_info_module.md#return-values)

## [Synopsis](nfv_provision_detail_info_module.md#id1)

- Get all Nfv Provision Detail.
- Returns provisioning device information for the specified IP address.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](nfv_provision_detail_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](nfv_provision_detail_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceIp**  string | DeviceIp query parameter. Device to which the provisioning detail has to be retrieved. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](nfv_provision_detail_info_module.md#id4)

> **Note:**
>
> - SDK Method used are site_design.SiteDesign.get_device_details_by_ip,
> - Paths used are get /dna/intent/api/v1/business/nfv/provisioningDetail,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](nfv_provision_detail_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Site Design GetDeviceDetailsByIP](https://developer.cisco.com/docs/dna-center/#!get-device-details-by-ip)
> :   Complete reference of the GetDeviceDetailsByIP API.

## [Examples](nfv_provision_detail_info_module.md#id6)

```yaml+jinja
- name: Get all Nfv Provision Detail
  cisco.dnac.nfv_provision_detail_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceIp: string
  register: result
```

## [Return Values](nfv_provision_detail_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"beginStep": "string", "duration": "string", "endTime": "string", "startTime": "string", "status": "string", "statusMessage": "string", "taskNodes": [{"cliTemplateUserMessageDTO": {}, "duration": "string", "endTime": "string", "errorPayload": {}, "name": "string", "nextTask": "string", "parentTask": {}, "payload": "string", "provisionedNames": {}, "startTime": "string", "status": "string", "statusMessage": "string", "stepRan": "string", "target": "string"}], "topology": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
