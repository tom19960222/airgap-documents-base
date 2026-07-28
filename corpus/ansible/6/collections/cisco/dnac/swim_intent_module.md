---
collection: ansible
version: "6"
title: "cisco.dnac.swim_intent module – Intent module for SWIM related functions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/swim_intent_module.html
fetched_at: 2026-07-27T16:54:23+00:00
---
# cisco.dnac.swim_intent module – Intent module for SWIM related functions

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
> see [Requirements](swim_intent_module.md#ansible-collections-cisco-dnac-swim-intent-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.swim_intent`.

New in cisco.dnac 6.6.0

- [Synopsis](swim_intent_module.md#synopsis)
- [Requirements](swim_intent_module.md#requirements)
- [Parameters](swim_intent_module.md#parameters)
- [Notes](swim_intent_module.md#notes)
- [Examples](swim_intent_module.md#examples)
- [Return Values](swim_intent_module.md#return-values)

## [Synopsis](swim_intent_module.md#id1)

- Manage operation related to image importation, distribution, activation and tagging image as golden
- API to fetch a software image from remote file system using URL for HTTP/FTP and uploads to DNA Center. Supported image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2.
- API to tag/untag image as golen for a given family of devices
- API to distribute a software image on a given device. Software image must be imported successfully into DNA Center before it can be distributed.
- API to activate a software image on a given device. Software image must be present in the device flash.

## [Requirements](swim_intent_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk == 2.4.5
- python >= 3.5

## [Parameters](swim_intent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary / required | List of details of SWIM image being managed |
| **imageActivationDetails**  dictionary | Details for SWIM image activation. Device on which the image needs to activated can be speciifed using any of the following parameters - deviceSerialNumber, deviceIPAddress, deviceHostname or deviceMacAddress. |
| **activateLowerImageVersion**  boolean | ActivateLowerImageVersion flag.  Choices:   - `false` - `true` |
| **deviceHostname**  string | Device hostname where the image needs to be activated |
| **deviceIPAddress**  string | Device IP address where the image needs to be activated |
| **deviceMacAddress**  string | Device MAC address where the image needs to be activated |
| **deviceSerialNumber**  string | Device serial number where the image needs to be activated |
| **deviceUpgradeMode**  string | Swim Trigger Activation’s deviceUpgradeMode. |
| **distributeIfNeeded**  boolean | DistributeIfNeeded flag.  Choices:   - `false` - `true` |
| **imageName**  string | SWIM image’s name |
| **scheduleValidate**  boolean | ScheduleValidate query parameter. ScheduleValidate, validates data before schedule (Optional).  Choices:   - `false` - `true` |
| **imageDistributionDetails**  dictionary | Details for SWIM image distribution. Device on which the image needs to distributed can be speciifed using any of the following parameters - deviceSerialNumber, deviceIPAddress, deviceHostname or deviceMacAddress. |
| **deviceHostname**  string | Device hostname where the image needs to be distributed |
| **deviceIPAddress**  string | Device IP address where the image needs to be distributed |
| **deviceMacAddress**  string | Device MAC address where the image needs to be distributed |
| **deviceSerialNumber**  string | Device serial number where the image needs to be distributed |
| **imageName**  string | SWIM image’s name |
| **importImageDetails**  dictionary | Details of image being imported |
| **type**  string | The source of import (Currently support vis URL). |
| **urlDetails**  dictionary | URL details for SWIM import |
| **payload**  list / elements=dictionary | Swim Import Via Url’s payload. |
| **applicationType**  string | Swim Import Via Url’s applicationType. |
| **imageFamily**  string | Swim Import Via Url’s imageFamily. |
| **sourceURL**  string | Swim Import Via Url’s sourceURL. |
| **thirdParty**  boolean | ThirdParty flag.  Choices:   - `false` - `true` |
| **vendor**  string | Swim Import Via Url’s vendor. |
| **scheduleAt**  string | ScheduleAt query parameter. Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the distribution should be scheduled (Optional). |
| **scheduleDesc**  string | ScheduleDesc query parameter. Custom Description (Optional). |
| **scheduleOrigin**  string | ScheduleOrigin query parameter. Originator of this call (Optional). |
| **taggingDetails**  dictionary | Details for tagging or untagging an image as golden |
| **deviceFamilyName**  string | Device family name |
| **deviceRole**  string | Device Role. Permissible Values ALL, UNKNOWN, ACCESS, BORDER ROUTER, DISTRIBUTION and CORE. |
| **imageName**  string | SWIM image name which will be tagged or untagged as golden. |
| **siteName**  string | Site name for which SWIM image will be tagged/untagged as golden. If not provided, SWIM image will be mapped to global site. |
| **tagging**  boolean | Booelan value to tag/untag SWIM image as golden If True then the given image will be tagged as golden. If False then the given image will be un-tagged as golden.  Choices:   - `false` - `true` |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_log**  boolean | Flag for logging playbook execution details. If set to true the log file will be created at the location of the execution with the name dnac.log  Choices:   - `false` ← (default) - `true` |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  string | The Cisco DNA Center port.  Default: `"443"` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.2.3.3"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](swim_intent_module.md#id4)

> **Note:**
>
> - SDK Method used are software_image_management_swim.SoftwareImageManagementSwim.import_software_image_via_url, software_image_management_swim.SoftwareImageManagementSwim.tag_as_golden_image, software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_distribution, software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_activation,
> - Paths used are post /dna/intent/api/v1/image/importation/source/url, post /dna/intent/api/v1/image/importation/golden, post /dna/intent/api/v1/image/distribution, post /dna/intent/api/v1/image/activation/device,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](swim_intent_module.md#id5)

```yaml+jinja
- name: Import an image, tag it as golden and load it on device
  cisco.dnac.swim_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    config:
    - importImageDetails:
        type: string
        urlDetails:
          payload:
          - sourceURL: string
            isThirdParty: bool
            imageFamily: string
            vendor: string
            applicationType: string
          scheduleAt: string
          scheduleDesc: string
          scheduleOrigin: string
      taggingDetails:
        imageName: string
        deviceRole: string
        deviceFamilyName: string
        siteName: string
        tagging: bool
      imageDistributionDetails:
        imageName: string
        deviceSerialNumber: string
      imageActivationDetails:
        scheduleValidate: bool
        activateLowerImageVersion: bool
        distributeIfNeeded: bool
        deviceSerialNumber: string
        imageName: string
```

## [Return Values](swim_intent_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response**  dictionary | A dictionary with activation details as returned by the DNAC Python SDK  Returned: always  Sample: `"{\n  \"response\": {\n                    \"additionalStatusURL\": String,\n                    \"data\": String,\n                    \"endTime\": 0,\n                    \"id\": String,\n                    \"instanceTenantId\": String,\n                    \"isError\": bool,\n                    \"lastUpdate\": 0,\n                    \"progress\": String,\n                    \"rootId\": String,\n                    \"serviceType\": String,\n                    \"startTime\": 0,\n                    \"version\": 0\n              },\n  \"msg\": String\n}\n"` |

### Authors

- Madhan Sankaranarayanan (@madhansansel) Rishita Chowdhary (@rishitachowdhary)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
