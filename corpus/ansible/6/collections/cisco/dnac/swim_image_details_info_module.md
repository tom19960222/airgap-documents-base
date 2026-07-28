---
collection: ansible
version: "6"
title: "cisco.dnac.swim_image_details_info module – Information module for Swim Image Details"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/swim_image_details_info_module.html
fetched_at: 2026-07-27T16:54:21+00:00
---
# cisco.dnac.swim_image_details_info module – Information module for Swim Image Details

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
> see [Requirements](swim_image_details_info_module.md#ansible-collections-cisco-dnac-swim-image-details-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.swim_image_details_info`.

New in cisco.dnac 3.1.0

- [Synopsis](swim_image_details_info_module.md#synopsis)
- [Requirements](swim_image_details_info_module.md#requirements)
- [Parameters](swim_image_details_info_module.md#parameters)
- [Notes](swim_image_details_info_module.md#notes)
- [See Also](swim_image_details_info_module.md#see-also)
- [Examples](swim_image_details_info_module.md#examples)
- [Return Values](swim_image_details_info_module.md#return-values)

## [Synopsis](swim_image_details_info_module.md#id1)

- Get all Swim Image Details.
- Returns software image list based on a filter criteria. For example “filterbyName = cat3k%”.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](swim_image_details_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](swim_image_details_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **applicationType**  string | ApplicationType query parameter. |
| **createdTime**  integer | CreatedTime query parameter. Time in milliseconds (epoch format). |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **family**  string | Family query parameter. |
| **headers**  dictionary | Additional headers. |
| **imageIntegrityStatus**  string | ImageIntegrityStatus query parameter. ImageIntegrityStatus - FAILURE, UNKNOWN, VERIFIED. |
| **imageName**  string | ImageName query parameter. Image Name. |
| **imageSeries**  string | ImageSeries query parameter. Image Series. |
| **imageSizeGreaterThan**  integer | ImageSizeGreaterThan query parameter. Size in bytes. |
| **imageSizeLesserThan**  integer | ImageSizeLesserThan query parameter. Size in bytes. |
| **imageUuid**  string | ImageUuid query parameter. |
| **isCCOLatest**  boolean | IsCCOLatest query parameter. Is latest from cisco.com.  Choices:   - `false` - `true` |
| **isCCORecommended**  boolean | IsCCORecommended query parameter. Is recommended from cisco.com.  Choices:   - `false` - `true` |
| **isTaggedGolden**  boolean | IsTaggedGolden query parameter. Is Tagged Golden.  Choices:   - `false` - `true` |
| **limit**  integer | Limit query parameter. |
| **name**  string | Name query parameter. |
| **offset**  integer | Offset query parameter. |
| **sortBy**  string | SortBy query parameter. Sort results by this field. |
| **sortOrder**  string | SortOrder query parameter. Sort order - ‘asc’ or ‘des’. Default is asc. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **version**  string | Version query parameter. Software Image Version. |

## [Notes](swim_image_details_info_module.md#id4)

> **Note:**
>
> - SDK Method used are software_image_management_swim.SoftwareImageManagementSwim.get_software_image_details,
> - Paths used are get /dna/intent/api/v1/image/importation,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](swim_image_details_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Software Image Management (SWIM) GetSoftwareImageDetails](https://developer.cisco.com/docs/dna-center/#!get-software-image-details)
> :   Complete reference of the GetSoftwareImageDetails API.

## [Examples](swim_image_details_info_module.md#id6)

```yaml+jinja
- name: Get all Swim Image Details
  cisco.dnac.swim_image_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    imageUuid: string
    name: string
    family: string
    applicationType: string
    imageIntegrityStatus: string
    version: string
    imageSeries: string
    imageName: string
    isTaggedGolden: True
    isCCORecommended: True
    isCCOLatest: True
    createdTime: 0
    imageSizeGreaterThan: 0
    imageSizeLesserThan: 0
    sortBy: string
    sortOrder: string
    limit: 0
    offset: 0
  register: result
```

## [Return Values](swim_image_details_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": [{"applicableDevicesForImage": [{"mdfId": "string", "productId": ["string"], "productName": "string"}], "applicationType": "string", "createdTime": "string", "extendedAttributes": {}, "family": "string", "feature": "string", "fileServiceId": "string", "fileSize": "string", "imageIntegrityStatus": "string", "imageName": "string", "imageSeries": ["string"], "imageSource": "string", "imageType": "string", "imageUuid": "string", "importSourceType": "string", "isTaggedGolden": true, "md5Checksum": "string", "name": "string", "profileInfo": [{"description": "string", "extendedAttributes": {}, "memory": 0, "productType": "string", "profileName": "string", "shares": 0, "vCpu": 0}], "shaCheckSum": "string", "vendor": "string", "version": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
