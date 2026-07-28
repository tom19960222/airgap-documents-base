---
collection: ansible
version: "8"
title: "cisco.dnac.golden_tag_image_details_info module – Information module for Golden Tag Image Details"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/golden_tag_image_details_info_module.html
fetched_at: 2026-07-28T01:22:52+00:00
---
# cisco.dnac.golden_tag_image_details_info module – Information module for Golden Tag Image Details

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
> see [Requirements](golden_tag_image_details_info_module.md#ansible-collections-cisco-dnac-golden-tag-image-details-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.golden_tag_image_details_info`.

New in cisco.dnac 4.0.0

- [Synopsis](golden_tag_image_details_info_module.md#synopsis)
- [Requirements](golden_tag_image_details_info_module.md#requirements)
- [Parameters](golden_tag_image_details_info_module.md#parameters)
- [Notes](golden_tag_image_details_info_module.md#notes)
- [See Also](golden_tag_image_details_info_module.md#see-also)
- [Examples](golden_tag_image_details_info_module.md#examples)
- [Return Values](golden_tag_image_details_info_module.md#return-values)

## [Synopsis](golden_tag_image_details_info_module.md#id1)

- Get Golden Tag Image Details by id.
- Get golden tag status of an image. Set siteId as -1 for Global site.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](golden_tag_image_details_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](golden_tag_image_details_info_module.md#id3)

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
| **headers**  dictionary | Additional headers. |
| **imageId**  string | ImageId path parameter. Image Id in uuid format. |
| **siteId**  string | SiteId path parameter. Site Id in uuid format. Set siteId as -1 for Global site. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](golden_tag_image_details_info_module.md#id4)

> **Note:**
>
> - SDK Method used are software_image_management_swim.SoftwareImageManagementSwim.get_golden_tag_status_of_an_image,
> - Paths used are get /dna/intent/api/v1/image/importation/golden/site/{siteId}/family/{deviceFamilyIdentifier}/role/{deviceRole}/image/{imageId},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](golden_tag_image_details_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Software Image Management (SWIM) GetGoldenTagStatusOfAnImage](https://developer.cisco.com/docs/dna-center/#!get-golden-tag-status-of-an-image)
> :   Complete reference of the GetGoldenTagStatusOfAnImage API.

## [Examples](golden_tag_image_details_info_module.md#id6)

```yaml+jinja
- name: Get Golden Tag Image Details by id
  cisco.dnac.golden_tag_image_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    deviceFamilyIdentifier: string
    deviceRole: string
    imageId: string
  register: result
```

## [Return Values](golden_tag_image_details_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"deviceRole": "string", "inheritedSiteId": "string", "inheritedSiteName": "string", "taggedGolden": true}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
