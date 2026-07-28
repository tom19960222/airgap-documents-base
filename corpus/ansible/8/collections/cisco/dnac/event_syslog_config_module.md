---
collection: ansible
version: "8"
title: "cisco.dnac.event_syslog_config module – Resource module for Event Syslog Config"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/event_syslog_config_module.html
fetched_at: 2026-07-28T01:22:39+00:00
---
# cisco.dnac.event_syslog_config module – Resource module for Event Syslog Config

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
> see [Requirements](event_syslog_config_module.md#ansible-collections-cisco-dnac-event-syslog-config-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.event_syslog_config`.

New in cisco.dnac 6.7.0

- [Synopsis](event_syslog_config_module.md#synopsis)
- [Requirements](event_syslog_config_module.md#requirements)
- [Parameters](event_syslog_config_module.md#parameters)
- [Notes](event_syslog_config_module.md#notes)
- [See Also](event_syslog_config_module.md#see-also)
- [Examples](event_syslog_config_module.md#examples)
- [Return Values](event_syslog_config_module.md#return-values)

## [Synopsis](event_syslog_config_module.md#id1)

- Manage operations create and update of the resource Event Syslog Config.
- Create Syslog Destination.
- Update Syslog Destination.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](event_syslog_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](event_syslog_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **configId**  string | Required only for update syslog configuration. |
| **description**  string | Description. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **host**  string | Host. |
| **name**  string | Name. |
| **port**  string | Port. |
| **protocol**  string | Protocol. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](event_syslog_config_module.md#id4)

> **Note:**
>
> - SDK Method used are event_management.EventManagement.create_syslog_destination, event_management.EventManagement.update_syslog_destination,
> - Paths used are post /dna/intent/api/v1/event/syslog-config, put /dna/intent/api/v1/event/syslog-config,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](event_syslog_config_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Event Management CreateSyslogDestination](https://developer.cisco.com/docs/dna-center/#!create-syslog-destination)
> :   Complete reference of the CreateSyslogDestination API.
>
> [Cisco DNA Center documentation for Event Management UpdateSyslogDestination](https://developer.cisco.com/docs/dna-center/#!update-syslog-destination)
> :   Complete reference of the UpdateSyslogDestination API.

## [Examples](event_syslog_config_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.event_syslog_config:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    configId: string
    description: string
    host: string
    name: string
    port: string
    protocol: string

- name: Create
  cisco.dnac.event_syslog_config:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    configId: string
    description: string
    host: string
    name: string
    port: string
    protocol: string
```

## [Return Values](event_syslog_config_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"apiStatus": "string", "errorMessage": {"errors": ["string"]}, "statusMessage": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
