---
collection: ansible
version: "6"
title: "cisco.ise.sg_mapping_bulk_monitor_status_info module – Information module for SG Mapping Bulk Monitor Status"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/sg_mapping_bulk_monitor_status_info_module.html
fetched_at: 2026-07-27T16:59:20+00:00
---
# cisco.ise.sg_mapping_bulk_monitor_status_info module – Information module for SG Mapping Bulk Monitor Status

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/cisco/ise) (version 2.5.9).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](sg_mapping_bulk_monitor_status_info_module.md#ansible-collections-cisco-ise-sg-mapping-bulk-monitor-status-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.sg_mapping_bulk_monitor_status_info`.

New in cisco.ise 1.0.0

- [Synopsis](sg_mapping_bulk_monitor_status_info_module.md#synopsis)
- [Requirements](sg_mapping_bulk_monitor_status_info_module.md#requirements)
- [Parameters](sg_mapping_bulk_monitor_status_info_module.md#parameters)
- [Notes](sg_mapping_bulk_monitor_status_info_module.md#notes)
- [See Also](sg_mapping_bulk_monitor_status_info_module.md#see-also)
- [Examples](sg_mapping_bulk_monitor_status_info_module.md#examples)
- [Return Values](sg_mapping_bulk_monitor_status_info_module.md#return-values)

## [Synopsis](sg_mapping_bulk_monitor_status_info_module.md#id1)

- Get SG Mapping Bulk Monitor Status by id.
- This API allows the client to monitor the bulk request.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sg_mapping_bulk_monitor_status_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](sg_mapping_bulk_monitor_status_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bulkid**  string | Bulkid path parameter. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |

## [Notes](sg_mapping_bulk_monitor_status_info_module.md#id4)

> **Note:**
>
> - SDK Method used are ip_to_sgt_mapping.IpToSgtMapping.monitor_bulk_status_ip_to_sgt_mapping,
> - Paths used are get /ers/config/sgmapping/bulk/{bulkid},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](sg_mapping_bulk_monitor_status_info_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for IPToSGTMapping](https://developer.cisco.com/docs/identity-services-engine/v1/#!sgmapping)
> :   Complete reference of the IPToSGTMapping API.

## [Examples](sg_mapping_bulk_monitor_status_info_module.md#id6)

```yaml+jinja
- name: Get SG Mapping Bulk Monitor Status by id
  cisco.ise.sg_mapping_bulk_monitor_status_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    bulkid: string
  register: result
```

## [Return Values](sg_mapping_bulk_monitor_status_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"bulkId": "string", "executionStatus": "string", "failCount": 0, "mediaType": "string", "operationType": "string", "resourcesCount": 0, "resourcesStatus": [{"description": "string", "id": "string", "name": "string", "resourceExecutionStatus": "string", "status": "string"}], "startTime": "string", "successCount": 0}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
