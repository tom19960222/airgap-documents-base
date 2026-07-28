---
collection: ansible
version: "8"
title: "cisco.dnac.golden_tag_image_delete module – Resource module for Golden Tag Image Delete"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/golden_tag_image_delete_module.html
fetched_at: 2026-07-28T01:22:51+00:00
---
# cisco.dnac.golden_tag_image_delete module – Resource module for Golden Tag Image Delete

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
> see [Requirements](golden_tag_image_delete_module.md#ansible-collections-cisco-dnac-golden-tag-image-delete-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.golden_tag_image_delete`.

New in cisco.dnac 4.0.0

- [Synopsis](golden_tag_image_delete_module.md#synopsis)
- [Requirements](golden_tag_image_delete_module.md#requirements)
- [Parameters](golden_tag_image_delete_module.md#parameters)
- [Notes](golden_tag_image_delete_module.md#notes)
- [See Also](golden_tag_image_delete_module.md#see-also)
- [Examples](golden_tag_image_delete_module.md#examples)
- [Return Values](golden_tag_image_delete_module.md#return-values)

## [Synopsis](golden_tag_image_delete_module.md#id1)

- Manage operation delete of the resource Golden Tag Image Delete.
- Remove golden tag. Set siteId as -1 for Global site.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](golden_tag_image_delete_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](golden_tag_image_delete_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceFamilyIdentifier**  string | DeviceFamilyIdentifier path parameter. Device family identifier e.g. 277696480-283933147, e.g. 277696480. |
| **deviceRole**  string | DeviceRole path parameter. Device Role. Permissible Values ALL, UNKNOWN, ACCESS, BORDER ROUTER, DISTRIBUTION and CORE. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **imageId**  string | ImageId path parameter. Image Id in uuid format. |
| **siteId**  string | SiteId path parameter. Site Id in uuid format. Set siteId as -1 for Global site. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](golden_tag_image_delete_module.md#id4)

> **Note:**
>
> - SDK Method used are software_image_management_swim.SoftwareImageManagementSwim.remove_golden_tag_for_image,
> - Paths used are delete /dna/intent/api/v1/image/importation/golden/site/{siteId}/family/{deviceFamilyIdentifier}/role/{deviceRole}/image/{imageId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](golden_tag_image_delete_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Software Image Management (SWIM) RemoveGoldenTagForImage](https://developer.cisco.com/docs/dna-center/#!remove-golden-tag-for-image)
> :   Complete reference of the RemoveGoldenTagForImage API.

## [Examples](golden_tag_image_delete_module.md#id6)

```yaml+jinja
- name: Delete by id
  cisco.dnac.golden_tag_image_delete:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceFamilyIdentifier: string
    deviceRole: string
    imageId: string
    siteId: string
```

## [Return Values](golden_tag_image_delete_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
