---
collection: ansible
version: "8"
title: "cisco.dnac.assign_device_to_site module – Resource module for Assign Device To Site"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/assign_device_to_site_module.html
fetched_at: 2026-07-28T01:21:21+00:00
---
# cisco.dnac.assign_device_to_site module – Resource module for Assign Device To Site

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
> see [Requirements](assign_device_to_site_module.md#ansible-collections-cisco-dnac-assign-device-to-site-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.assign_device_to_site`.

New in cisco.dnac 6.5.0

- [Synopsis](assign_device_to_site_module.md#synopsis)
- [Requirements](assign_device_to_site_module.md#requirements)
- [Parameters](assign_device_to_site_module.md#parameters)
- [Notes](assign_device_to_site_module.md#notes)
- [See Also](assign_device_to_site_module.md#see-also)
- [Examples](assign_device_to_site_module.md#examples)
- [Return Values](assign_device_to_site_module.md#return-values)

## [Synopsis](assign_device_to_site_module.md#id1)

- Manage operation create of the resource Assign Device To Site.
- Assigns unassigned devices to a site. This API does not move assigned devices to other sites.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](assign_device_to_site_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](assign_device_to_site_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **device**  list / elements=dictionary | Assign Device To Site’s device. |
| **ip**  string | Device ip (eg 10.104.240.64). |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **siteId**  string | SiteId path parameter. Site id to which site the device to assign. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](assign_device_to_site_module.md#id4)

> **Note:**
>
> - SDK Method used are ..assign_devices_to_site,
> - Paths used are post /dna/intent/api/v1/assign-device-to-site/{siteId}/device,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](assign_device_to_site_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for AssignDevicesToSite](https://developer.cisco.com/docs/dna-center/#!assign-devices-to-site)
> :   Complete reference of the AssignDevicesToSite API.

## [Examples](assign_device_to_site_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.assign_device_to_site:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    device:
    - ip: string
    headers: '{{my_headers | from_json}}'
    siteId: string
```

## [Return Values](assign_device_to_site_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
