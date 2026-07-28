---
collection: ansible
version: "8"
title: "cisco.dnac.interface_operation_create module – Resource module for Interface Operation Create"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/interface_operation_create_module.html
fetched_at: 2026-07-28T01:22:58+00:00
---
# cisco.dnac.interface_operation_create module – Resource module for Interface Operation Create

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
> see [Requirements](interface_operation_create_module.md#ansible-collections-cisco-dnac-interface-operation-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.interface_operation_create`.

New in cisco.dnac 6.0.0

- [Synopsis](interface_operation_create_module.md#synopsis)
- [Requirements](interface_operation_create_module.md#requirements)
- [Parameters](interface_operation_create_module.md#parameters)
- [Notes](interface_operation_create_module.md#notes)
- [See Also](interface_operation_create_module.md#see-also)
- [Examples](interface_operation_create_module.md#examples)
- [Return Values](interface_operation_create_module.md#return-values)

## [Synopsis](interface_operation_create_module.md#id1)

- Manage operation create of the resource Interface Operation Create.
- Clear mac-address on an individual port. In request body, operation needs to be specified as ‘ClearMacAddress’. In the future more possible operations will be added to this API.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](interface_operation_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](interface_operation_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deploymentMode**  string | DeploymentMode query parameter. Preview/Deploy ‘Preview’ means the configuration is not pushed to the device. ‘Deploy’ makes the configuration pushed to the device. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **interfaceUuid**  string | InterfaceUuid path parameter. Interface Id. |
| **operation**  string | Operation. |
| **payload**  dictionary | Payload. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](interface_operation_create_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.clear_mac_address_table,
> - Paths used are post /dna/intent/api/v1/interface/{interfaceUuid}/operation,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](interface_operation_create_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices ClearMacAddressTable](https://developer.cisco.com/docs/dna-center/#!clear-mac-address-table)
> :   Complete reference of the ClearMacAddressTable API.

## [Examples](interface_operation_create_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.interface_operation_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deploymentMode: string
    interfaceUuid: string
    operation: string
    payload: {}
```

## [Return Values](interface_operation_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
