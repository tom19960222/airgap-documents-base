---
collection: ansible
version: "8"
title: "cisco.dnac.pnp_intent module – Resource module for Site and PnP related functions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/pnp_intent_module.html
fetched_at: 2026-07-28T01:24:03+00:00
---
# cisco.dnac.pnp_intent module – Resource module for Site and PnP related functions

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
> see [Requirements](pnp_intent_module.md#ansible-collections-cisco-dnac-pnp-intent-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_intent`.

New in cisco.dnac 6.6.0

- [Synopsis](pnp_intent_module.md#synopsis)
- [Requirements](pnp_intent_module.md#requirements)
- [Parameters](pnp_intent_module.md#parameters)
- [Notes](pnp_intent_module.md#notes)
- [Examples](pnp_intent_module.md#examples)
- [Return Values](pnp_intent_module.md#return-values)

## [Synopsis](pnp_intent_module.md#id1)

- Manage operations add device, claim device and unclaim device of Onboarding Configuration(PnP) resource
- API to add device to pnp inventory and claim it to a site.
- API to delete device from the pnp inventory.

## [Requirements](pnp_intent_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk == 2.6.5
- python >= 3.5

## [Parameters](pnp_intent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary / required | List of details of device being managed. |
| **deviceInfo**  dictionary / required | Pnp Device’s deviceInfo. |
| **add_device_method**  string | Pnp Device’s device addition method (Single/Bulk/Smart Account). |
| **hostname**  string | Pnp Device’s hostname. |
| **isSudiRequired**  boolean | Sudi Authentication requiremnet’s flag.  **Choices:**   - `false` - `true` |
| **pid**  string | Pnp Device’s pid. |
| **serialNumber**  string | Pnp Device’s serialNumber. |
| **state**  string | Pnp Device’s onbording state (Unclaimed/Claimed/Provisioned). |
| **gateway**  string | Gateway IP address of the Wireless Controller for getting pinged |
| **golden_image**  boolean | Is the image to be condifgured tagged as golden image  **Choices:**   - `false` - `true` |
| **image_name**  string | Name of image to be configured on the device |
| **ipInterfaceName**  string | Name of the Interface used for Pnp by the Wireless Controller |
| **pnp_type**  string | Device type of the Pnp device (Default/CatalystWLC/AccessPoint)  **Default:** `"Default"` |
| **projectName**  string | Name of the project under which the template is present  **Default:** `"Onboarding Configuration"` |
| **rfProfile**  string | rfprofile of the AP being claimed (HIGH/LOW/TYPICAL) |
| **site_name**  string | Name of the site for which device will be claimed. |
| **staticIP**  string | Management IP address of the Wireless Controller |
| **subnetMask**  string | Subnet Mask of the Management IP address of the Wireless Controller |
| **template_name**  string | Name of template to be configured on the device. |
| **vlanId**  string | Vlan Id allocated for claimimg of Wireless Controller |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_log**  boolean | Flag for logging playbook execution details. If set to true the log file will be created at the location of the execution with the name dnac.log  **Choices:**   - `false` ← (default) - `true` |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  string | The Cisco DNA Center port.  **Default:** `"443"` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.2.3.3"` |
| **state**  string | The state of DNAC after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](pnp_intent_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.add_device, device_onboarding_pnp.DeviceOnboardingPnp.get_device_list, device_onboarding_pnp.DeviceOnboardingPnp.claim_a_device_to_a_site, device_onboarding_pnp.DeviceOnboardingPnp.delete_device_by_id_from_pnp, device_onboarding_pnp.DeviceOnboardingPnp.get_device_count, sites.Sites.get_site, software_image_management_swim.SoftwareImageManagementSwim.get_software_image_details, configuration_templates.ConfigurationTemplates.gets_the_templates_available
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-device post /dna/intent/api/v1/onboarding/pnp-device/site-claim post /dna/intent/api/v1/onboarding/pnp-device/{id} get /dna/intent/api/v1/onboarding/pnp-device/count get /dna/intent/api/v1/onboarding/pnp-device get /dna/intent/api/v1/site get /dna/intent/api/v1/image/importation get /dna/intent/api/v1/template-programmer/template
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](pnp_intent_module.md#id5)

```yaml+jinja
- name: Add a new device and claim the device
  cisco.dnac.pnp_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
        - template_name: string
          image_name: string
          golden_image: bool
          site_name: string
          projectName: string
          pnp_type: string
          staticIP: string
          subnetMask: string
          gateway: string
          vlanId: string
          ipInterfaceName: string
          rfProfile: string
          deviceInfo:
            hostname: string
            state: string
            pid: string
            serialNumber: string
            add_device_method: string
            isSudiRequired: string
```

## [Return Values](pnp_intent_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response_1**  dictionary | A dictionary with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"{\n  \"response\":\n    {\n      \"response\": String,\n      \"version\": String\n    },\n  \"msg\": String\n}\n"` |
| **response_2**  list / elements=string | A list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `["{\n  \"response\": []", "\n  \"msg\": String\n}\n"]` |
| **response_3**  dictionary | A string with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"{\n  \"response\": String,\n  \"msg\": String\n}\n"` |

### Authors

- Madhan Sankaranarayanan (@madhansansel) Rishita Chowdhary (@rishitachowdhary) Abinash Mishra (@abimishr)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
