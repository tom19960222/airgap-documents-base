---
collection: ansible
version: "6"
title: "cisco.dnac.issues_info module – Information module for Issues"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/issues_info_module.html
fetched_at: 2026-07-27T16:52:23+00:00
---
# cisco.dnac.issues_info module – Information module for Issues

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
> see [Requirements](issues_info_module.md#ansible-collections-cisco-dnac-issues-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.issues_info`.

New in cisco.dnac 3.1.0

- [Synopsis](issues_info_module.md#synopsis)
- [Requirements](issues_info_module.md#requirements)
- [Parameters](issues_info_module.md#parameters)
- [Notes](issues_info_module.md#notes)
- [See Also](issues_info_module.md#see-also)
- [Examples](issues_info_module.md#examples)
- [Return Values](issues_info_module.md#return-values)

## [Synopsis](issues_info_module.md#id1)

- Get all Issues.
- Intent API to get a list of global issues, issues for a specific device, or issue for a specific client device’s MAC address.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](issues_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](issues_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aiDriven**  string | AiDriven query parameter. The issue’s AI driven value (Yes or No)(Use only when macAddress and deviceId are not provided). |
| **deviceId**  string | DeviceId query parameter. Assurance UUID value of the device in the issue content. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **endTime**  integer | EndTime query parameter. Ending epoch time in milliseconds of query time window. |
| **headers**  dictionary | Additional headers. |
| **issueStatus**  string | IssueStatus query parameter. The issue’s status value (One of ACTIVE, IGNORED, RESOLVED). |
| **macAddress**  string | MacAddress query parameter. Client’s device MAC address of the issue (format xx xx xx xx xx xx). |
| **priority**  string | Priority query parameter. The issue’s priority value (One of P1, P2, P3, or P4)(Use only when macAddress and deviceId are not provided). |
| **siteId**  string | SiteId query parameter. Assurance UUID value of the site in the issue content. |
| **startTime**  integer | StartTime query parameter. Starting epoch time in milliseconds of query time window. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](issues_info_module.md#id4)

> **Note:**
>
> - SDK Method used are issues.Issues.issues,
> - Paths used are get /dna/intent/api/v1/issues,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](issues_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Issues Issues](https://developer.cisco.com/docs/dna-center/#!issues-issues)
> :   Complete reference of the Issues API.

## [Examples](issues_info_module.md#id6)

```yaml+jinja
- name: Get all Issues
  cisco.dnac.issues_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    siteId: string
    deviceId: string
    macAddress: string
    priority: string
    aiDriven: string
    issueStatus: string
  register: result
```

## [Return Values](issues_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"aiDriven": true, "category": "string", "clientMac": "string", "deviceId": "string", "deviceRole": "string", "issueId": "string", "issue_occurence_count": 0, "last_occurence_time": 0, "name": "string", "priority": "string", "siteId": "string", "status": "string"}], "totalCount": 0, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
