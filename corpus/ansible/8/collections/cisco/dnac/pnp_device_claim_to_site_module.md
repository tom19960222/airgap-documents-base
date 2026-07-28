---
collection: ansible
version: "8"
title: "cisco.dnac.pnp_device_claim_to_site module – Resource module for Pnp Device Claim To Site"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/pnp_device_claim_to_site_module.html
fetched_at: 2026-07-28T01:23:56+00:00
---
# cisco.dnac.pnp_device_claim_to_site module – Resource module for Pnp Device Claim To Site

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
> see [Requirements](pnp_device_claim_to_site_module.md#ansible-collections-cisco-dnac-pnp-device-claim-to-site-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_device_claim_to_site`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_device_claim_to_site_module.md#synopsis)
- [Requirements](pnp_device_claim_to_site_module.md#requirements)
- [Parameters](pnp_device_claim_to_site_module.md#parameters)
- [Notes](pnp_device_claim_to_site_module.md#notes)
- [See Also](pnp_device_claim_to_site_module.md#see-also)
- [Examples](pnp_device_claim_to_site_module.md#examples)
- [Return Values](pnp_device_claim_to_site_module.md#return-values)

## [Synopsis](pnp_device_claim_to_site_module.md#id1)

- Manage operation create of the resource Pnp Device Claim To Site.
- Claim a device based on DNA-C Site-based design process. Some required parameters differ based on device platform.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_device_claim_to_site_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_device_claim_to_site_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **configInfo**  list / elements=dictionary  *added in cisco.dnac 4.2.0* | Pnp Device Claim To Site’s configInfo. |
| **configId**  string | Config Id. |
| **configParameters**  dictionary | Pnp Device Claim To Site’s configParameters. |
| **key**  string | Key. |
| **value**  string | Value. |
| **deviceId**  string | Device Id. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **gateway**  string  *added in cisco.dnac 6.4.0* | For CatalystWLC/MobilityExpress. |
| **imageInfo**  dictionary  *added in cisco.dnac 4.2.0* | Pnp Device Claim To Site’s imageInfo. |
| **imageId**  string | Image Id. |
| **skip**  boolean | Skip.  **Choices:**   - `false` - `true` |
| **interfaceName**  string | For Catalyst 9800 WLC. |
| **rfProfile**  string  *added in cisco.dnac 6.1.0* | For Access Points. |
| **sensorProfile**  string | For Sensors. |
| **siteId**  string | Site Id. |
| **staticIP**  string  *added in cisco.dnac 6.4.0* | For CatalystWLC/MobilityExpress. |
| **subnetMask**  string | For CatalystWLC/MobilityExpress. |
| **type**  string | Type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **vlanID**  string | For Catalyst 9800 WLC. |

## [Notes](pnp_device_claim_to_site_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.claim_a_device_to_a_site,
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-device/site-claim,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_device_claim_to_site_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) ClaimADeviceToASite](https://developer.cisco.com/docs/dna-center/#!claim-a-device-to-a-site)
> :   Complete reference of the ClaimADeviceToASite API.

## [Examples](pnp_device_claim_to_site_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.pnp_device_claim_to_site:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    configInfo:
    - configId: string
      configParameters:
        key: string
        value: string
    deviceId: string
    gateway: string
    imageInfo:
      imageId: string
      skip: true
    interfaceName: string
    rfProfile: string
    sensorProfile: string
    siteId: string
    staticIP: string
    subnetMask: string
    type: string
    vlanID: string
```

## [Return Values](pnp_device_claim_to_site_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": "string", "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
