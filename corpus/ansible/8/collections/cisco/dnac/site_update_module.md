---
collection: ansible
version: "8"
title: "cisco.dnac.site_update module – Resource module for Site Update"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/site_update_module.html
fetched_at: 2026-07-28T01:25:05+00:00
---
# cisco.dnac.site_update module – Resource module for Site Update

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
> see [Requirements](site_update_module.md#ansible-collections-cisco-dnac-site-update-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.site_update`.

New in cisco.dnac 3.1.0

- [Synopsis](site_update_module.md#synopsis)
- [Requirements](site_update_module.md#requirements)
- [Parameters](site_update_module.md#parameters)
- [Notes](site_update_module.md#notes)
- [See Also](site_update_module.md#see-also)
- [Examples](site_update_module.md#examples)
- [Return Values](site_update_module.md#return-values)

## [Synopsis](site_update_module.md#id1)

- Manage operation update of the resource Site Update.
- Update site area/building/floor with specified hierarchy and new values.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](site_update_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](site_update_module.md#id3)

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
| **site**  dictionary | Site Update’s site. |
| **area**  dictionary | Site Update’s area. |
| **name**  string | Name. |
| **parentName**  string | Parent Name. |
| **building**  dictionary | Site Update’s building. |
| **address**  string | Address. |
| **latitude**  integer | Latitude. |
| **longitude**  integer | Longitude. |
| **name**  string | Name. |
| **parentName**  string | Parent Name. |
| **floor**  dictionary | Site Update’s floor. |
| **height**  integer | Height. |
| **length**  integer | Length. |
| **name**  string | Name. |
| **rfModel**  string | Rf Model. |
| **width**  integer | Width. |
| **siteId**  string | SiteId path parameter. Site id to which site details to be updated. |
| **type**  string | Type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](site_update_module.md#id4)

> **Note:**
>
> - SDK Method used are sites.Sites.update_site,
> - Paths used are put /dna/intent/api/v1/site/{siteId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](site_update_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Sites UpdateSite](https://developer.cisco.com/docs/dna-center/#!update-site)
> :   Complete reference of the UpdateSite API.

## [Examples](site_update_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.dnac.site_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: '{{my_headers | from_json}}'
    site:
      area:
        name: string
        parentName: string
      building:
        address: string
        latitude: 0
        longitude: 0
        name: string
        parentName: string
      floor:
        height: 0
        length: 0
        name: string
        rfModel: string
        width: 0
    siteId: string
    type: string
```

## [Return Values](site_update_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"data": "string", "endTime": "string", "id": "string", "instanceTenantId": "string", "isError": "string", "operationIdList": ["string"], "progress": "string", "rootId": "string", "serviceType": "string", "startTime": "string", "version": "string"}, "result": "string", "status": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
