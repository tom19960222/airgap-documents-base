---
collection: ansible
version: "8"
title: "cisco.dnac.license_device_registration module – Resource module for License Device Registration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/license_device_registration_module.html
fetched_at: 2026-07-28T01:23:11+00:00
---
# cisco.dnac.license_device_registration module – Resource module for License Device Registration

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
> see [Requirements](license_device_registration_module.md#ansible-collections-cisco-dnac-license-device-registration-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.license_device_registration`.

New in cisco.dnac 3.1.0

- [Synopsis](license_device_registration_module.md#synopsis)
- [Requirements](license_device_registration_module.md#requirements)
- [Parameters](license_device_registration_module.md#parameters)
- [Notes](license_device_registration_module.md#notes)
- [See Also](license_device_registration_module.md#see-also)
- [Examples](license_device_registration_module.md#examples)
- [Return Values](license_device_registration_module.md#return-values)

## [Synopsis](license_device_registration_module.md#id1)

- Manage operation update of the resource License Device Registration.
- Register devices in CSSM Cisco Smart Software Manager .

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](license_device_registration_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](license_device_registration_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **device_uuids**  list / elements=string | Comma separated device ids. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **virtual_account_name**  string | Virtual_account_name path parameter. Name of virtual account. |

## [Notes](license_device_registration_module.md#id4)

> **Note:**
>
> - SDK Method used are licenses.Licenses.device_registration2,
> - Paths used are put /dna/intent/api/v1/licenses/smartAccount/virtualAccount/{virtual_account_name}/register,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](license_device_registration_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Licenses DeviceRegistration2](https://developer.cisco.com/docs/dna-center/#!device-registration-2)
> :   Complete reference of the DeviceRegistration2 API.

## [Examples](license_device_registration_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.license_device_registration:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    device_uuids:
    - string
    virtual_account_name: string
```

## [Return Values](license_device_registration_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
