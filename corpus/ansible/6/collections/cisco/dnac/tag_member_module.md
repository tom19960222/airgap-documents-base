---
collection: ansible
version: "6"
title: "cisco.dnac.tag_member module – Resource module for Tag Member"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/tag_member_module.html
fetched_at: 2026-07-27T16:54:32+00:00
---
# cisco.dnac.tag_member module – Resource module for Tag Member

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
> see [Requirements](tag_member_module.md#ansible-collections-cisco-dnac-tag-member-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.tag_member`.

New in cisco.dnac 3.1.0

- [Synopsis](tag_member_module.md#synopsis)
- [Requirements](tag_member_module.md#requirements)
- [Parameters](tag_member_module.md#parameters)
- [Notes](tag_member_module.md#notes)
- [See Also](tag_member_module.md#see-also)
- [Examples](tag_member_module.md#examples)
- [Return Values](tag_member_module.md#return-values)

## [Synopsis](tag_member_module.md#id1)

- Manage operations create and delete of the resource Tag Member.
- Adds members to the tag specified by id.
- Removes Tag member from the tag specified by id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](tag_member_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](tag_member_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **id**  string | Id path parameter. Tag ID. |
| **memberId**  string | MemberId path parameter. TagMember id to be removed from tag. |
| **object**  string | Object. |
| **payload**  dictionary | Map of member type and member ids. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](tag_member_module.md#id4)

> **Note:**
>
> - SDK Method used are tag.Tag.add_members_to_the_tag, tag.Tag.remove_tag_member,
> - Paths used are post /dna/intent/api/v1/tag/{id}/member, delete /dna/intent/api/v1/tag/{id}/member/{memberId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](tag_member_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Tag AddMembersToTheTag](https://developer.cisco.com/docs/dna-center/#!add-members-to-the-tag)
> :   Complete reference of the AddMembersToTheTag API.
>
> [Cisco DNA Center documentation for Tag RemoveTagMember](https://developer.cisco.com/docs/dna-center/#!remove-tag-member)
> :   Complete reference of the RemoveTagMember API.

## [Examples](tag_member_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.tag_member:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    id: string
    object: string
    payload:
      networkinterface:
      - string

- name: Delete by id
  cisco.dnac.tag_member:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
    memberId: string
```

## [Return Values](tag_member_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
