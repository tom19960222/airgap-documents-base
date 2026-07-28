---
collection: ansible
version: "8"
title: "cisco.dnac.threat_detail module – Resource module for Threat Detail"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/threat_detail_module.html
fetched_at: 2026-07-28T01:25:30+00:00
---
# cisco.dnac.threat_detail module – Resource module for Threat Detail

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
> see [Requirements](threat_detail_module.md#ansible-collections-cisco-dnac-threat-detail-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.threat_detail`.

New in cisco.dnac 3.1.0

- [Synopsis](threat_detail_module.md#synopsis)
- [Requirements](threat_detail_module.md#requirements)
- [Parameters](threat_detail_module.md#parameters)
- [Notes](threat_detail_module.md#notes)
- [Examples](threat_detail_module.md#examples)
- [Return Values](threat_detail_module.md#return-values)

## [Synopsis](threat_detail_module.md#id1)

- Manage operation create of the resource Threat Detail.
- The details for the Rogue and aWIPS threats.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](threat_detail_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](threat_detail_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **endTime**  integer | End Time. |
| **isNewThreat**  boolean | Is New Threat.  **Choices:**   - `false` - `true` |
| **limit**  integer | Limit. |
| **offset**  integer | Offset. |
| **siteId**  list / elements=string | Site Id. |
| **startTime**  integer | Start Time. |
| **threatLevel**  list / elements=string | Threat Level. |
| **threatType**  list / elements=string | Threat Type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](threat_detail_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.threat_details,
> - Paths used are post /dna/intent/api/v1/security/threats/details,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](threat_detail_module.md#id5)

```yaml+jinja
- name: Create
  cisco.dnac.threat_detail:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    endTime: 0
    isNewThreat: true
    limit: 0
    offset: 0
    siteId:
    - string
    startTime: 0
    threatLevel:
    - string
    threatType:
    - string
```

## [Return Values](threat_detail_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": [{"apName": "string", "macAddress": "string", "siteNameHierarchy": "string", "ssid": "string", "threatLevel": "string", "threatType": "string", "updatedTime": 0, "vendor": "string"}], "totalCount": 0, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
