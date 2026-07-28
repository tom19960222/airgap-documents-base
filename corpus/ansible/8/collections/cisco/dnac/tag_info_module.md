---
collection: ansible
version: "8"
title: "cisco.dnac.tag_info module – Information module for Tag"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/tag_info_module.html
fetched_at: 2026-07-28T01:25:21+00:00
---
# cisco.dnac.tag_info module – Information module for Tag

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
> see [Requirements](tag_info_module.md#ansible-collections-cisco-dnac-tag-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.tag_info`.

New in cisco.dnac 3.1.0

- [Synopsis](tag_info_module.md#synopsis)
- [Requirements](tag_info_module.md#requirements)
- [Parameters](tag_info_module.md#parameters)
- [Notes](tag_info_module.md#notes)
- [See Also](tag_info_module.md#see-also)
- [Examples](tag_info_module.md#examples)
- [Return Values](tag_info_module.md#return-values)

## [Synopsis](tag_info_module.md#id1)

- Get all Tag.
- Get Tag by id.
- Returns tag specified by Id.
- Returns the tags for given filter criteria.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](tag_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](tag_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **additionalInfo_attributes**  string | AdditionalInfo.attributes query parameter. |
| **additionalInfo_nameSpace**  string | AdditionalInfo.nameSpace query parameter. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **field**  string | Field query parameter. Available field names are ‘name,id,parentId,type,additionalInfo.nameSpace,additionalInfo.attributes’. |
| **headers**  dictionary | Additional headers. |
| **id**  string | Id path parameter. Tag ID. |
| **level**  string | Level query parameter. |
| **limit**  integer | Limit query parameter. |
| **name**  string | Name query parameter. Tag name is mandatory when filter operation is used. |
| **offset**  integer | Offset query parameter. |
| **order**  string | Order query parameter. Available values are asc and des. |
| **size**  string | Size query parameter. Size in kilobytes(KB). |
| **sortBy**  string | SortBy query parameter. Only supported attribute is name. SortyBy is mandatory when order is used. |
| **systemTag**  string | SystemTag query parameter. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](tag_info_module.md#id4)

> **Note:**
>
> - SDK Method used are tag.Tag.get_tag, tag.Tag.get_tag_by_id,
> - Paths used are get /dna/intent/api/v1/tag, get /dna/intent/api/v1/tag/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](tag_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Tag GetTag](https://developer.cisco.com/docs/dna-center/#!get-tag)
> :   Complete reference of the GetTag API.
>
> [Cisco DNA Center documentation for Tag GetTagById](https://developer.cisco.com/docs/dna-center/#!get-tag-by-id)
> :   Complete reference of the GetTagById API.

## [Examples](tag_info_module.md#id6)

```yaml+jinja
- name: Get all Tag
  cisco.dnac.tag_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    additionalInfo_nameSpace: string
    additionalInfo_attributes: string
    level: string
    offset: 0
    limit: 0
    size: string
    field: string
    sortBy: string
    order: string
    systemTag: string
  register: result

- name: Get Tag by id
  cisco.dnac.tag_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
```

## [Return Values](tag_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"description": "string", "dynamicRules": [{"memberType": "string", "rules": {"items": "string", "name": "string", "operation": "string", "value": "string", "values": ["string"]}}], "id": "string", "instanceTenantId": "string", "name": "string", "systemTag": true}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
