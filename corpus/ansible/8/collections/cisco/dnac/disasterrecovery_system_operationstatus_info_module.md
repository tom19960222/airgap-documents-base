---
collection: ansible
version: "8"
title: "cisco.dnac.disasterrecovery_system_operationstatus_info module – Information module for Disasterrecovery System Operationstatus"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/disasterrecovery_system_operationstatus_info_module.html
fetched_at: 2026-07-28T01:22:05+00:00
---
# cisco.dnac.disasterrecovery_system_operationstatus_info module – Information module for Disasterrecovery System Operationstatus

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
> see [Requirements](disasterrecovery_system_operationstatus_info_module.md#ansible-collections-cisco-dnac-disasterrecovery-system-operationstatus-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.disasterrecovery_system_operationstatus_info`.

New in cisco.dnac 4.0.0

- [Synopsis](disasterrecovery_system_operationstatus_info_module.md#synopsis)
- [Requirements](disasterrecovery_system_operationstatus_info_module.md#requirements)
- [Parameters](disasterrecovery_system_operationstatus_info_module.md#parameters)
- [Notes](disasterrecovery_system_operationstatus_info_module.md#notes)
- [Examples](disasterrecovery_system_operationstatus_info_module.md#examples)
- [Return Values](disasterrecovery_system_operationstatus_info_module.md#return-values)

## [Synopsis](disasterrecovery_system_operationstatus_info_module.md#id1)

- Get all Disasterrecovery System Operationstatus.
- Returns the status of Disaster Recovery operation performed on the system.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](disasterrecovery_system_operationstatus_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](disasterrecovery_system_operationstatus_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](disasterrecovery_system_operationstatus_info_module.md#id4)

> **Note:**
>
> - SDK Method used are disaster_recovery.DisasterRecovery.disaster_recovery_operational_status,
> - Paths used are get /dna/intent/api/v1/disasterrecovery/system/operationstatus,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](disasterrecovery_system_operationstatus_info_module.md#id5)

```yaml+jinja
- name: Get all Disasterrecovery System Operationstatus
  cisco.dnac.disasterrecovery_system_operationstatus_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
  register: result
```

## [Return Values](disasterrecovery_system_operationstatus_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"endTimestamp": "string", "initiated_by": "string", "ipconfig": [{"interface": "string", "ip": "string", "vip": "string"}], "message": "string", "severity": "string", "site": "string", "startTimestamp": "string", "status": "string", "tasks": [{"endTimestamp": "string", "ipconfig": [{"interface": "string", "ip": "string", "vip": "string"}], "message": "string", "site": "string", "startTimestamp": "string", "status": "string", "title": "string"}], "title": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
