---
collection: ansible
version: "6"
title: "cisco.dnac.system_health_info module – Information module for System Health"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/system_health_info_module.html
fetched_at: 2026-07-27T16:54:28+00:00
---
# cisco.dnac.system_health_info module – Information module for System Health

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
> see [Requirements](system_health_info_module.md#ansible-collections-cisco-dnac-system-health-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.system_health_info`.

New in cisco.dnac 3.1.0

- [Synopsis](system_health_info_module.md#synopsis)
- [Requirements](system_health_info_module.md#requirements)
- [Parameters](system_health_info_module.md#parameters)
- [Notes](system_health_info_module.md#notes)
- [See Also](system_health_info_module.md#see-also)
- [Examples](system_health_info_module.md#examples)
- [Return Values](system_health_info_module.md#return-values)

## [Synopsis](system_health_info_module.md#id1)

- Get all System Health.
- This API retrieves the latest system events.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](system_health_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](system_health_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **domain**  string | Domain query parameter. Fetch system events with this domain. Possible values of domain are listed here /dna/platform/app/consumer-portal/developer-toolkit/events. |
| **headers**  dictionary | Additional headers. |
| **limit**  integer | Limit query parameter. |
| **offset**  integer | Offset query parameter. |
| **subdomain**  string | Subdomain query parameter. Fetch system events with this subdomain. Possible values of subdomain are listed here /dna/platform/app/consumer-portal/developer-toolkit/events. |
| **summary**  boolean | Summary query parameter. Fetch the latest high severity event.  Choices:   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](system_health_info_module.md#id4)

> **Note:**
>
> - SDK Method used are health_and_performance.HealthAndPerformance.system_health,
> - Paths used are get /dna/intent/api/v1/diagnostics/system/health,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](system_health_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Health and Performance SystemHealthAPI](https://developer.cisco.com/docs/dna-center/#!system-health-api)
> :   Complete reference of the SystemHealthAPI API.

## [Examples](system_health_info_module.md#id6)

```yaml+jinja
- name: Get all System Health
  cisco.dnac.system_health_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    summary: True
    domain: string
    subdomain: string
    limit: 0
    offset: 0
  register: result
```

## [Return Values](system_health_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"cimcaddress": ["string"], "healthEvents": [{"description": "string", "domain": "string", "hostname": "string", "instance": "string", "severity": "string", "state": "string", "status": "string", "subDomain": "string", "timestamp": "string"}], "hostName": "string", "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
