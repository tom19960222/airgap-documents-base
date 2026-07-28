---
collection: ansible
version: "8"
title: "cisco.dnac.wireless_provision_access_point module – Resource module for Wireless Provision Access Point"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/wireless_provision_access_point_module.html
fetched_at: 2026-07-28T01:25:49+00:00
---
# cisco.dnac.wireless_provision_access_point module – Resource module for Wireless Provision Access Point

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
> see [Requirements](wireless_provision_access_point_module.md#ansible-collections-cisco-dnac-wireless-provision-access-point-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_provision_access_point`.

New in cisco.dnac 3.1.0

- [Synopsis](wireless_provision_access_point_module.md#synopsis)
- [Requirements](wireless_provision_access_point_module.md#requirements)
- [Parameters](wireless_provision_access_point_module.md#parameters)
- [Notes](wireless_provision_access_point_module.md#notes)
- [See Also](wireless_provision_access_point_module.md#see-also)
- [Examples](wireless_provision_access_point_module.md#examples)
- [Return Values](wireless_provision_access_point_module.md#return-values)

## [Synopsis](wireless_provision_access_point_module.md#id1)

- Manage operation create of the resource Wireless Provision Access Point.
- Access Point Provision and ReProvision.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_provision_access_point_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_provision_access_point_module.md#id3)

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
| **payload**  list / elements=dictionary | Wireless Provision Access Point’s payload. |
| **customApGroupName**  string | Custom AP group name. |
| **customFlexGroupName**  list / elements=string | “Custom flex group name”. |
| **deviceName**  string | Device name. |
| **rfProfile**  string | Radio frequency profile name. |
| **siteId**  string | Site name hierarchy(ex Global/…). |
| **siteNameHierarchy**  string | Site name hierarchy(ex Global/…). |
| **type**  string | ApWirelessConfiguration. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](wireless_provision_access_point_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.ap_provision,
> - Paths used are post /dna/intent/api/v1/wireless/ap-provision,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_provision_access_point_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless APProvision](https://developer.cisco.com/docs/dna-center/#!a-p-provision)
> :   Complete reference of the APProvision API.

## [Examples](wireless_provision_access_point_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.wireless_provision_access_point:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: '{{my_headers | from_json}}'
    payload:
    - customApGroupName: string
      customFlexGroupName:
      - string
      deviceName: string
      rfProfile: string
      siteId: string
      siteNameHierarchy: string
      type: string
```

## [Return Values](wireless_provision_access_point_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
