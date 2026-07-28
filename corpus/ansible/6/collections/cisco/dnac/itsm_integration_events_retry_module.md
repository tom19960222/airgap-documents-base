---
collection: ansible
version: "6"
title: "cisco.dnac.itsm_integration_events_retry module – Resource module for Itsm Integration Events Retry"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/itsm_integration_events_retry_module.html
fetched_at: 2026-07-27T16:52:25+00:00
---
# cisco.dnac.itsm_integration_events_retry module – Resource module for Itsm Integration Events Retry

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
> see [Requirements](itsm_integration_events_retry_module.md#ansible-collections-cisco-dnac-itsm-integration-events-retry-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.itsm_integration_events_retry`.

New in cisco.dnac 3.1.0

- [Synopsis](itsm_integration_events_retry_module.md#synopsis)
- [Requirements](itsm_integration_events_retry_module.md#requirements)
- [Parameters](itsm_integration_events_retry_module.md#parameters)
- [Notes](itsm_integration_events_retry_module.md#notes)
- [See Also](itsm_integration_events_retry_module.md#see-also)
- [Examples](itsm_integration_events_retry_module.md#examples)
- [Return Values](itsm_integration_events_retry_module.md#return-values)

## [Synopsis](itsm_integration_events_retry_module.md#id1)

- Manage operation create of the resource Itsm Integration Events Retry.
- Allows retry of multiple failed ITSM event instances. The retry request payload can be given as a list of strings “instance1”,”instance2”,”instance3”,.. A minimum of one instance Id is mandatory. The list of failed event instance Ids can be retrieved using the ‘Get Failed ITSM Events’ API in the ‘instanceId’ attribute.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](itsm_integration_events_retry_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](itsm_integration_events_retry_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **payload**  list / elements=string | Itsm Integration Events Retry’s payload. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](itsm_integration_events_retry_module.md#id4)

> **Note:**
>
> - SDK Method used are itsm.Itsm.retry_integration_events,
> - Paths used are post /dna/intent/api/v1/integration/events,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](itsm_integration_events_retry_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for ITSM RetryIntegrationEvents](https://developer.cisco.com/docs/dna-center/#!retry-integration-events)
> :   Complete reference of the RetryIntegrationEvents API.

## [Examples](itsm_integration_events_retry_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.itsm_integration_events_retry:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
    - string
```

## [Return Values](itsm_integration_events_retry_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
