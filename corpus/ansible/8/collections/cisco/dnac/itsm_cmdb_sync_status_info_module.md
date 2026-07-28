---
collection: ansible
version: "8"
title: "cisco.dnac.itsm_cmdb_sync_status_info module – Information module for Itsm Cmdb Sync Status"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/itsm_cmdb_sync_status_info_module.html
fetched_at: 2026-07-28T01:23:01+00:00
---
# cisco.dnac.itsm_cmdb_sync_status_info module – Information module for Itsm Cmdb Sync Status

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
> see [Requirements](itsm_cmdb_sync_status_info_module.md#ansible-collections-cisco-dnac-itsm-cmdb-sync-status-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.itsm_cmdb_sync_status_info`.

New in cisco.dnac 3.1.0

- [Synopsis](itsm_cmdb_sync_status_info_module.md#synopsis)
- [Requirements](itsm_cmdb_sync_status_info_module.md#requirements)
- [Parameters](itsm_cmdb_sync_status_info_module.md#parameters)
- [Notes](itsm_cmdb_sync_status_info_module.md#notes)
- [See Also](itsm_cmdb_sync_status_info_module.md#see-also)
- [Examples](itsm_cmdb_sync_status_info_module.md#examples)
- [Return Values](itsm_cmdb_sync_status_info_module.md#return-values)

## [Synopsis](itsm_cmdb_sync_status_info_module.md#id1)

- Get all Itsm Cmdb Sync Status.
- This API allows to retrieve the detail of CMDB sync status.It accepts two query parameter “status”,”date”.The supported values for status field are “Success”,”Failed”,”Unknown” and date field should be in “YYYY-MM-DD” format. By default all the cmdb sync status will be send as response and based on the query parameter filtered detail will be send as response.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](itsm_cmdb_sync_status_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](itsm_cmdb_sync_status_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **date**  string | Date query parameter. Provide date in “YYYY-MM-DD” format. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **status**  string | Status query parameter. Supported values are “Success”,”Failed” and “Unknown”. Providing other values will result in all the available sync job status. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](itsm_cmdb_sync_status_info_module.md#id4)

> **Note:**
>
> - SDK Method used are itsm.Itsm.get_cmdb_sync_status,
> - Paths used are get /dna/intent/api/v1/cmdb-sync/detail,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](itsm_cmdb_sync_status_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for ITSM GetCMDBSyncStatus](https://developer.cisco.com/docs/dna-center/#!get-cmdb-sync-status)
> :   Complete reference of the GetCMDBSyncStatus API.

## [Examples](itsm_cmdb_sync_status_info_module.md#id6)

```yaml+jinja
- name: Get all Itsm Cmdb Sync Status
  cisco.dnac.itsm_cmdb_sync_status_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    status: string
    date: string
  register: result
```

## [Return Values](itsm_cmdb_sync_status_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"successCount\": \"string\",\n    \"failureCount\": \"string\",\n    \"devices\": [\n      {\n        \"deviceId\": \"string\",\n        \"status\": \"string\"\n      }\n    ],\n    \"unknownErrorCount\": \"string\",\n    \"message\": \"string\",\n    \"syncTime\": \"string\"\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
