---
collection: ansible
version: "6"
title: "cisco.dnac.reports_executions_info module – Information module for Reports Executions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/reports_executions_info_module.html
fetched_at: 2026-07-27T16:53:32+00:00
---
# cisco.dnac.reports_executions_info module – Information module for Reports Executions

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
> see [Requirements](reports_executions_info_module.md#ansible-collections-cisco-dnac-reports-executions-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.reports_executions_info`.

New in cisco.dnac 3.1.0

- [Synopsis](reports_executions_info_module.md#synopsis)
- [Requirements](reports_executions_info_module.md#requirements)
- [Parameters](reports_executions_info_module.md#parameters)
- [Notes](reports_executions_info_module.md#notes)
- [See Also](reports_executions_info_module.md#see-also)
- [Examples](reports_executions_info_module.md#examples)
- [Return Values](reports_executions_info_module.md#return-values)

## [Synopsis](reports_executions_info_module.md#id1)

- Get all Reports Executions.
- Get Reports Executions by id.
- Get details of all executions for a given report.
- Returns report content. Save the response to a file by converting the response data as a blob and setting the file format available from content-disposition response header.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](reports_executions_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](reports_executions_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dirPath**  string | Directory absolute path. Defaults to the current working directory. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **executionId**  string | ExecutionId path parameter. ExecutionId of report execution. |
| **filename**  string | The filename used to save the download file. |
| **headers**  dictionary | Additional headers. |
| **reportId**  string | ReportId path parameter. ReportId of report. |
| **saveFile**  boolean | Enable or disable automatic file creation of raw response.  Choices:   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](reports_executions_info_module.md#id4)

> **Note:**
>
> - SDK Method used are reports.Reports.download_report_content, reports.Reports.get_all_execution_details_for_a_given_report,
> - Paths used are get /dna/intent/api/v1/data/reports/{reportId}/executions, get /dna/intent/api/v1/data/reports/{reportId}/executions/{executionId},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](reports_executions_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Reports DownloadReportContent](https://developer.cisco.com/docs/dna-center/#!download-report-content)
> :   Complete reference of the DownloadReportContent API.
>
> [Cisco DNA Center documentation for Reports GetAllExecutionDetailsForAGivenReport](https://developer.cisco.com/docs/dna-center/#!get-all-execution-details-for-a-given-report)
> :   Complete reference of the GetAllExecutionDetailsForAGivenReport API.

## [Examples](reports_executions_info_module.md#id6)

```yaml+jinja
- name: Get all Reports Executions
  cisco.dnac.reports_executions_info:
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

- name: Get Reports Executions by id
  cisco.dnac.reports_executions_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    reportId: string
    executionId: string
  register: result
```

## [Return Values](reports_executions_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"data": "filecontent", "dirpath": "download/directory", "filename": "filename", "path": "download/directory/filename"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
