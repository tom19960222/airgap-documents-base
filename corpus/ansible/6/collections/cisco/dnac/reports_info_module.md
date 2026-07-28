---
collection: ansible
version: "6"
title: "cisco.dnac.reports_info module – Information module for Reports"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/reports_info_module.html
fetched_at: 2026-07-27T16:53:33+00:00
---
# cisco.dnac.reports_info module – Information module for Reports

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
> see [Requirements](reports_info_module.md#ansible-collections-cisco-dnac-reports-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.reports_info`.

New in cisco.dnac 3.1.0

- [Synopsis](reports_info_module.md#synopsis)
- [Requirements](reports_info_module.md#requirements)
- [Parameters](reports_info_module.md#parameters)
- [Notes](reports_info_module.md#notes)
- [See Also](reports_info_module.md#see-also)
- [Examples](reports_info_module.md#examples)
- [Return Values](reports_info_module.md#return-values)

## [Synopsis](reports_info_module.md#id1)

- Get all Reports.
- Get Reports by id.
- Get list of scheduled report configurations.
- Get scheduled report configuration by reportId.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](reports_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](reports_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **reportId**  string | ReportId path parameter. ReportId of report. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **viewGroupId**  string | ViewGroupId query parameter. ViewGroupId of viewgroup for report. |
| **viewId**  string | ViewId query parameter. ViewId of view for report. |

## [Notes](reports_info_module.md#id4)

> **Note:**
>
> - SDK Method used are reports.Reports.get_a_scheduled_report, reports.Reports.get_list_of_scheduled_reports,
> - Paths used are get /dna/intent/api/v1/data/reports, get /dna/intent/api/v1/data/reports/{reportId},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](reports_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Reports GetAScheduledReport](https://developer.cisco.com/docs/dna-center/#!get-a-scheduled-report)
> :   Complete reference of the GetAScheduledReport API.
>
> [Cisco DNA Center documentation for Reports GetListOfScheduledReports](https://developer.cisco.com/docs/dna-center/#!get-list-of-scheduled-reports)
> :   Complete reference of the GetListOfScheduledReports API.

## [Examples](reports_info_module.md#id6)

```yaml+jinja
- name: Get all Reports
  cisco.dnac.reports_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    viewGroupId: string
    viewId: string
  register: result

- name: Get Reports by id
  cisco.dnac.reports_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    reportId: string
  register: result
```

## [Return Values](reports_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"dataCategory": "string", "deliveries": [{}], "executionCount": 0, "executions": [{"endTime": 0, "errors": ["string"], "executionId": "string", "processStatus": "string", "requestStatus": "string", "startTime": 0, "warnings": ["string"]}], "name": "string", "reportId": "string", "reportWasExecuted": true, "schedule": {}, "tags": ["string"], "view": {"description": "string", "fieldGroups": [{"fieldGroupDisplayName": "string", "fieldGroupName": "string", "fields": [{"displayName": "string", "name": "string"}]}], "filters": [{"displayName": "string", "name": "string", "type": "string", "value": {}}], "format": {"default": true, "formatType": "string", "name": "string"}, "name": "string", "viewId": "string", "viewInfo": "string"}, "viewGroupId": "string", "viewGroupVersion": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
