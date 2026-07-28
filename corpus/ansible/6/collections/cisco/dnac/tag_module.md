---
collection: ansible
version: "6"
title: "cisco.dnac.tag module – Resource module for Tag"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/tag_module.html
fetched_at: 2026-07-27T16:54:30+00:00
---
# cisco.dnac.tag module – Resource module for Tag

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
> see [Requirements](tag_module.md#ansible-collections-cisco-dnac-tag-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.tag`.

New in cisco.dnac 3.1.0

- [Synopsis](tag_module.md#synopsis)
- [Requirements](tag_module.md#requirements)
- [Parameters](tag_module.md#parameters)
- [Notes](tag_module.md#notes)
- [See Also](tag_module.md#see-also)
- [Examples](tag_module.md#examples)
- [Return Values](tag_module.md#return-values)

## [Synopsis](tag_module.md#id1)

- Manage operations create, update and delete of the resource Tag.
- Creates tag with specified tag attributes.
- Deletes a tag specified by id.
- Updates a tag specified by id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](tag_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](tag_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Tag’s description. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **dynamicRules**  list / elements=dictionary | Tag’s dynamicRules. |
| **memberType**  string | Tag’s memberType. |
| **rules**  dictionary | Tag’s rules. |
| **items**  list / elements=dictionary | Tag’s items. |
| **name**  string | Tag’s name. |
| **operation**  string | Tag’s operation. |
| **value**  string | Tag’s value. |
| **values**  list / elements=string | Tag’s values. |
| **id**  string | Tag’s id. |
| **instanceTenantId**  string | Tag’s instanceTenantId. |
| **name**  string | Tag’s name. |
| **systemTag**  boolean | SystemTag flag.  Choices:   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](tag_module.md#id4)

> **Note:**
>
> - SDK Method used are tag.Tag.create_tag, tag.Tag.delete_tag, tag.Tag.update_tag,
> - Paths used are post /dna/intent/api/v1/tag, delete /dna/intent/api/v1/tag/{id}, put /dna/intent/api/v1/tag,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](tag_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Tag CreateTag](https://developer.cisco.com/docs/dna-center/#!create-tag)
> :   Complete reference of the CreateTag API.
>
> [Cisco DNA Center documentation for Tag DeleteTag](https://developer.cisco.com/docs/dna-center/#!delete-tag)
> :   Complete reference of the DeleteTag API.
>
> [Cisco DNA Center documentation for Tag UpdateTag](https://developer.cisco.com/docs/dna-center/#!update-tag)
> :   Complete reference of the UpdateTag API.

## [Examples](tag_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.tag:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    dynamicRules:
    - memberType: string
      rules:
        items:
        - {}
        name: string
        operation: string
        value: string
        values:
        - string
    id: string
    instanceTenantId: string
    name: string
    systemTag: true

- name: Create
  cisco.dnac.tag:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    description: string
    dynamicRules:
    - memberType: string
      rules:
        items:
        - {}
        name: string
        operation: string
        value: string
        values:
        - string
    id: string
    instanceTenantId: string
    name: string
    systemTag: true

- name: Delete by id
  cisco.dnac.tag:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
```

## [Return Values](tag_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
