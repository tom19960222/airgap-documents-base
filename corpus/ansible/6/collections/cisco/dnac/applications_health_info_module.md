---
collection: ansible
version: "6"
title: "cisco.dnac.applications_health_info module – Information module for Applications Health"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/applications_health_info_module.html
fetched_at: 2026-07-27T16:50:58+00:00
---
# cisco.dnac.applications_health_info module – Information module for Applications Health

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
> see [Requirements](applications_health_info_module.md#ansible-collections-cisco-dnac-applications-health-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.applications_health_info`.

New in cisco.dnac 3.1.0

- [Synopsis](applications_health_info_module.md#synopsis)
- [Requirements](applications_health_info_module.md#requirements)
- [Parameters](applications_health_info_module.md#parameters)
- [Notes](applications_health_info_module.md#notes)
- [See Also](applications_health_info_module.md#see-also)
- [Examples](applications_health_info_module.md#examples)
- [Return Values](applications_health_info_module.md#return-values)

## [Synopsis](applications_health_info_module.md#id1)

- Get all Applications Health.
- Intent API to get a list of applications for a specific site, a device, or a client device’s MAC address. For a combination of a specific application with site and/or device the API gets list of issues/devices/endpoints.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](applications_health_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](applications_health_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **applicationHealth**  string | ApplicationHealth query parameter. Application health category (POOR, FAIR, or GOOD. Optionally use with siteId only). |
| **applicationName**  string | ApplicationName query parameter. The name of the application to get information on. |
| **deviceId**  string | DeviceId query parameter. Assurance device UUID value (Cannot be submitted together with siteId and clientMac). |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **endTime**  integer | EndTime query parameter. Ending epoch time in milliseconds of time window. |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. The max number of application entries in returned data 1, 1000 (optionally used with siteId only). |
| **macAddress**  string | MacAddress query parameter. Client device’s MAC address (Cannot be submitted together with siteId and deviceId). |
| **offset**  integer | Offset query parameter. The offset of the first application in the returned data (optionally used with siteId only). |
| **siteId**  string | SiteId query parameter. Assurance site UUID value (Cannot be submitted together with deviceId and clientMac). |
| **startTime**  integer | StartTime query parameter. Starting epoch time in milliseconds of time window. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](applications_health_info_module.md#id4)

> **Note:**
>
> - SDK Method used are applications.Applications.applications,
> - Paths used are get /dna/intent/api/v1/application-health,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](applications_health_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Applications Applications](https://developer.cisco.com/docs/dna-center/#!applications-applications)
> :   Complete reference of the Applications API.

## [Examples](applications_health_info_module.md#id6)

```yaml+jinja
- name: Get all Applications Health
  cisco.dnac.applications_health_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    deviceId: string
    macAddress: string
    startTime: 0
    endTime: 0
    applicationHealth: string
    offset: 0
    limit: 0
    applicationName: string
  register: result
```

## [Return Values](applications_health_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"application": "string", "applicationServerLatency": {}, "averageThroughput": 0, "businessRelevance": "string", "clientIp": "string", "clientMacAddress": "string", "clientName": "string", "clientNetworkLatency": {}, "deviceType": "string", "exporterFamily": "string", "exporterIpAddress": "string", "exporterName": "string", "exporterUUID": "string", "health": 0, "issueId": "string", "issueName": "string", "jitter": {}, "location": "string", "name": "string", "networkLatency": {}, "occurrences": 0, "operatingSystem": "string", "packetLossPercent": {}, "priority": "string", "rootCause": "string", "serverNetworkLatency": {}, "severity": "string", "summary": "string", "timestamp": 0, "trafficClass": "string", "usageBytes": 0}], "totalCount": 0, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
