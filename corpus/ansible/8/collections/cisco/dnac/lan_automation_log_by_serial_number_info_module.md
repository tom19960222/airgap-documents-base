---
collection: ansible
version: "8"
title: "cisco.dnac.lan_automation_log_by_serial_number_info module – Information module for Lan Automation Log By Serial Number"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/lan_automation_log_by_serial_number_info_module.html
fetched_at: 2026-07-28T01:23:06+00:00
---
# cisco.dnac.lan_automation_log_by_serial_number_info module – Information module for Lan Automation Log By Serial Number

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
> see [Requirements](lan_automation_log_by_serial_number_info_module.md#ansible-collections-cisco-dnac-lan-automation-log-by-serial-number-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.lan_automation_log_by_serial_number_info`.

New in cisco.dnac 6.7.0

- [Synopsis](lan_automation_log_by_serial_number_info_module.md#synopsis)
- [Requirements](lan_automation_log_by_serial_number_info_module.md#requirements)
- [Parameters](lan_automation_log_by_serial_number_info_module.md#parameters)
- [Notes](lan_automation_log_by_serial_number_info_module.md#notes)
- [See Also](lan_automation_log_by_serial_number_info_module.md#see-also)
- [Examples](lan_automation_log_by_serial_number_info_module.md#examples)
- [Return Values](lan_automation_log_by_serial_number_info_module.md#return-values)

## [Synopsis](lan_automation_log_by_serial_number_info_module.md#id1)

- Get Lan Automation Log By Serial Number by id.
- Invoke this API to get the LAN Automation session logs for individual devices based on the given LAN Automation session id and device serial number.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](lan_automation_log_by_serial_number_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](lan_automation_log_by_serial_number_info_module.md#id3)

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
| **id**  string | Id path parameter. LAN Automation session identifier. |
| **logLevel**  string | LogLevel query parameter. Supported levels are ERROR, INFO, WARNING, TRACE, CONFIG and ALL. Specifying ALL will display device specific logs with the exception of CONFIG logs. In order to view CONFIG logs along with the remaining logs, please leave the query parameter blank. |
| **serialNumber**  string | SerialNumber path parameter. Device serial number. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](lan_automation_log_by_serial_number_info_module.md#id4)

> **Note:**
>
> - SDK Method used are lan_automation.LanAutomation.lan_automation_logs_for_individual_devices,
> - Paths used are get /dna/intent/api/v1/lan-automation/log/{id}/{serialNumber},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](lan_automation_log_by_serial_number_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for LAN Automation LANAutomationLogsForIndividualDevices](https://developer.cisco.com/docs/dna-center/#!l-an-automation-logs-for-individual-devices)
> :   Complete reference of the LANAutomationLogsForIndividualDevices API.

## [Examples](lan_automation_log_by_serial_number_info_module.md#id6)

```yaml+jinja
- name: Get Lan Automation Log By Serial Number by id
  cisco.dnac.lan_automation_log_by_serial_number_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    logLevel: string
    id: string
    serialNumber: string
  register: result
```

## [Return Values](lan_automation_log_by_serial_number_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": [{"logs": [{"logLevel": "string", "record": "string", "timeStamp": "string"}], "nwOrchId": "string", "serialNumber": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
