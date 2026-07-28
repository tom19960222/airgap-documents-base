---
collection: ansible
version: "6"
title: "cisco.dnac.site_create module – Resource module for Site Create"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/site_create_module.html
fetched_at: 2026-07-27T16:54:12+00:00
---
# cisco.dnac.site_create module – Resource module for Site Create

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
> see [Requirements](site_create_module.md#ansible-collections-cisco-dnac-site-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.site_create`.

New in cisco.dnac 3.1.0

- [Synopsis](site_create_module.md#synopsis)
- [Requirements](site_create_module.md#requirements)
- [Parameters](site_create_module.md#parameters)
- [Notes](site_create_module.md#notes)
- [See Also](site_create_module.md#see-also)
- [Examples](site_create_module.md#examples)
- [Return Values](site_create_module.md#return-values)

## [Synopsis](site_create_module.md#id1)

- Manage operation create of the resource Site Create.
- Creates site with area/building/floor with specified hierarchy.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](site_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](site_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **site**  dictionary | Site Create’s site. |
| **area**  dictionary | Site Create’s area. |
| **name**  string | Name of the area (eg Area1). |
| **parentName**  string | Parent name of the area to be created. |
| **building**  dictionary | Site Create’s building. |
| **address**  string | Address of the building to be created. |
| **country**  string | Country (eg United States). |
| **latitude**  integer | Latitude coordinate of the building (eg 37.338). |
| **longitude**  integer | Longitude coordinate of the building (eg -121.832). |
| **name**  string | Name of the building (eg building1). |
| **parentName**  string | Parent name of building to be created. |
| **floor**  dictionary | Site Create’s floor. |
| **floorNumber**  integer | Floor number. (eg 5). |
| **height**  integer | Height of the floor. Unit of measure is ft. (eg 15). |
| **length**  integer | Length of the floor. Unit of measure is ft. (eg 100). |
| **name**  string | Name of the floor (eg floor-1). |
| **parentName**  string | Parent name of the floor to be created. |
| **rfModel**  string | Type of floor (eg Cubes And Walled Offices0. |
| **width**  integer | Width of the floor. Unit of measure is ft. (eg 100). |
| **type**  string | Type of site to create (eg area, building, floor). |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](site_create_module.md#id4)

> **Note:**
>
> - SDK Method used are sites.Sites.create_site,
> - Paths used are post /dna/intent/api/v1/site,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](site_create_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Sites CreateSite](https://developer.cisco.com/docs/dna-center/#!create-site)
> :   Complete reference of the CreateSite API.

## [Examples](site_create_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.site_create:
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
        country: string
        latitude: 0
        longitude: 0
        name: string
        parentName: string
      floor:
        floorNumber: 0
        height: 0
        length: 0
        name: string
        parentName: string
        rfModel: string
        width: 0
    type: string
```

## [Return Values](site_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
