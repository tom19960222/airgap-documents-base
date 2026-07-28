---
collection: ansible
version: "8"
title: "cisco.dnac.snmp_properties module – Resource module for Snmp Properties"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/snmp_properties_module.html
fetched_at: 2026-07-28T01:25:06+00:00
---
# cisco.dnac.snmp_properties module – Resource module for Snmp Properties

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
> see [Requirements](snmp_properties_module.md#ansible-collections-cisco-dnac-snmp-properties-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.snmp_properties`.

New in cisco.dnac 3.1.0

- [Synopsis](snmp_properties_module.md#synopsis)
- [Requirements](snmp_properties_module.md#requirements)
- [Parameters](snmp_properties_module.md#parameters)
- [Notes](snmp_properties_module.md#notes)
- [See Also](snmp_properties_module.md#see-also)
- [Examples](snmp_properties_module.md#examples)
- [Return Values](snmp_properties_module.md#return-values)

## [Synopsis](snmp_properties_module.md#id1)

- Manage operation create of the resource Snmp Properties.
- Adds SNMP properties.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](snmp_properties_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](snmp_properties_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **payload**  list / elements=dictionary | Snmp Properties’s payload. |
| **id**  string | Snmp Properties’s id. |
| **instanceTenantId**  string | Snmp Properties’s instanceTenantId. |
| **instanceUuid**  string | Snmp Properties’s instanceUuid. |
| **intValue**  integer | Snmp Properties’s intValue. |
| **systemPropertyName**  string | Snmp Properties’s systemPropertyName. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](snmp_properties_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.create_update_snmp_properties,
> - Paths used are post /dna/intent/api/v1/snmp-property,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](snmp_properties_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery CreateUpdateSNMPProperties](https://developer.cisco.com/docs/dna-center/#!create-update-snmp-properties)
> :   Complete reference of the CreateUpdateSNMPProperties API.

## [Examples](snmp_properties_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.snmp_properties:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - id: string
      instanceTenantId: string
      instanceUuid: string
      intValue: 0
      systemPropertyName: string
```

## [Return Values](snmp_properties_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
