---
collection: ansible
version: "6"
title: "cisco.dnac.device_credential_delete module – Resource module for Device Credential Delete"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/device_credential_delete_module.html
fetched_at: 2026-07-27T16:51:27+00:00
---
# cisco.dnac.device_credential_delete module – Resource module for Device Credential Delete

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
> see [Requirements](device_credential_delete_module.md#ansible-collections-cisco-dnac-device-credential-delete-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.device_credential_delete`.

New in cisco.dnac 3.1.0

- [Synopsis](device_credential_delete_module.md#synopsis)
- [Requirements](device_credential_delete_module.md#requirements)
- [Parameters](device_credential_delete_module.md#parameters)
- [Notes](device_credential_delete_module.md#notes)
- [See Also](device_credential_delete_module.md#see-also)
- [Examples](device_credential_delete_module.md#examples)
- [Return Values](device_credential_delete_module.md#return-values)

## [Synopsis](device_credential_delete_module.md#id1)

- Manage operation delete of the resource Device Credential Delete.
- Delete device credential.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_credential_delete_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](device_credential_delete_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **id**  string | Id path parameter. Global credential id. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](device_credential_delete_module.md#id4)

> **Note:**
>
> - SDK Method used are network_settings.NetworkSettings.delete_device_credential,
> - Paths used are delete /dna/intent/api/v1/device-credential/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](device_credential_delete_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Network Settings DeleteDeviceCredential](https://developer.cisco.com/docs/dna-center/#!delete-device-credential)
> :   Complete reference of the DeleteDeviceCredential API.

## [Examples](device_credential_delete_module.md#id6)

```yaml+jinja
- name: Delete by id
  cisco.dnac.device_credential_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    id: string
```

## [Return Values](device_credential_delete_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
