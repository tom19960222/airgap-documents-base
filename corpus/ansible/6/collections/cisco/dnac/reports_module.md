---
collection: ansible
version: "6"
title: "cisco.dnac.reports module – Resource module for Reports"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/reports_module.html
fetched_at: 2026-07-27T16:53:31+00:00
---
# cisco.dnac.reports module – Resource module for Reports

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
> see [Requirements](reports_module.md#ansible-collections-cisco-dnac-reports-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.reports`.

New in cisco.dnac 3.1.0

- [Synopsis](reports_module.md#synopsis)
- [Requirements](reports_module.md#requirements)
- [Parameters](reports_module.md#parameters)
- [Notes](reports_module.md#notes)
- [See Also](reports_module.md#see-also)
- [Examples](reports_module.md#examples)
- [Return Values](reports_module.md#return-values)

## [Synopsis](reports_module.md#id1)

- Manage operations create and delete of the resource Reports.
- Create/Schedule a report configuration. Use “Get view details for a given view group & view” API to get the metadata required to configure a report.
- Delete a scheduled report configuration. Deletes the report executions also.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](reports_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](reports_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deliveries**  list / elements=dictionary | Array of available delivery channels. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **name**  string | Report name. |
| **reportId**  string | ReportId path parameter. ReportId of report. |
| **schedule**  dictionary | Reports’s schedule. |
| **tags**  list / elements=string | Array of tags for report. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **view**  dictionary | Reports’s view. |
| **fieldGroups**  list / elements=dictionary | Reports’s fieldGroups. |
| **fieldGroupDisplayName**  string | Field group label/displayname for user. |
| **fieldGroupName**  string | Field group name. |
| **fields**  list / elements=dictionary | Reports’s fields. |
| **displayName**  string | Field label/displayname. |
| **name**  string | Field name. |
| **filters**  list / elements=dictionary | Reports’s filters. |
| **displayName**  string | Filter label/displayname. |
| **name**  string | Filter name. |
| **type**  string | Filter type. |
| **value**  dictionary | Value of filter. Data type is based on the filter type. Use the filter definitions from the view to fetch the options for a filter. |
| **format**  dictionary | Reports’s format. |
| **formatType**  string | Format type of report. |
| **name**  string | Format name of report. |
| **name**  string | View name. |
| **viewId**  string | View Id. |
| **viewGroupId**  string | ViewGroupId of the viewgroup for the report. |
| **viewGroupVersion**  string | Version of viewgroup for the report. |

## [Notes](reports_module.md#id4)

> **Note:**
>
> - SDK Method used are reports.Reports.create_or_schedule_a_report, reports.Reports.delete_a_scheduled_report,
> - Paths used are post /dna/intent/api/v1/data/reports, delete /dna/intent/api/v1/data/reports/{reportId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](reports_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Reports CreateOrScheduleAReport](https://developer.cisco.com/docs/dna-center/#!create-or-schedule-a-report)
> :   Complete reference of the CreateOrScheduleAReport API.
>
> [Cisco DNA Center documentation for Reports DeleteAScheduledReport](https://developer.cisco.com/docs/dna-center/#!delete-a-scheduled-report)
> :   Complete reference of the DeleteAScheduledReport API.

## [Examples](reports_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.reports:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    deliveries:
    - {}
    name: string
    schedule: {}
    tags:
    - string
    view:
      fieldGroups:
      - fieldGroupDisplayName: string
        fieldGroupName: string
        fields:
        - displayName: string
          name: string
      filters:
      - displayName: string
        name: string
        type: string
        value: {}
      format:
        formatType: string
        name: string
      name: string
      viewId: string
    viewGroupId: string
    viewGroupVersion: string

- name: Delete by id
  cisco.dnac.reports:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    reportId: string
```

## [Return Values](reports_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"dataCategory": "string", "deliveries": [{}], "executionCount": 0, "executions": [{"endTime": 0, "errors": ["string"], "executionId": "string", "processStatus": "string", "requestStatus": "string", "startTime": 0, "warnings": ["string"]}], "name": "string", "reportId": "string", "reportWasExecuted": true, "schedule": {}, "tags": ["string"], "view": {"description": "string", "fieldGroups": [{"fieldGroupDisplayName": "string", "fieldGroupName": "string", "fields": [{"displayName": "string", "name": "string"}]}], "filters": [{"displayName": "string", "name": "string", "type": "string", "value": {}}], "format": {"formatType": "string", "name": "string"}, "name": "string", "viewId": "string", "viewInfo": "string"}, "viewGroupId": "string", "viewGroupVersion": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
