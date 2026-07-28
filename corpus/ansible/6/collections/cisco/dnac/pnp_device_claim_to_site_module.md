---
collection: ansible
version: "6"
title: "cisco.dnac.pnp_device_claim_to_site module – Resource module for Pnp Device Claim To Site"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/pnp_device_claim_to_site_module.html
fetched_at: 2026-07-27T16:53:11+00:00
---
# cisco.dnac.pnp_device_claim_to_site module – Resource module for Pnp Device Claim To Site

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
- Claim a device based on DNA-C Site based design process. Different parameters are required for different device platforms.

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
| **configInfo**  dictionary  added in cisco.dnac 4.2.0 | Pnp Device Claim To Site’s configInfo. |
| **configId**  string | Pnp Device Claim To Site’s configId. |
| **configParameters**  list / elements=dictionary | Pnp Device Claim To Site’s configParameters. |
| **key**  string | Pnp Device Claim To Site’s key. |
| **value**  string | Pnp Device Claim To Site’s value. |
| **deviceId**  string | Pnp Device Claim To Site’s deviceId. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **gateway**  string  added in cisco.dnac 6.4.0 | Pnp Device Claim To Site’s gateway. |
| **hostname**  string  added in cisco.dnac 4.2.0 | Pnp Device Claim To Site’s hostname. |
| **imageId**  string | Pnp Device Claim To Site’s imageId. |
| **imageInfo**  dictionary  added in cisco.dnac 4.2.0 | Pnp Device Claim To Site’s imageInfo. |
| **imageId**  string | Pnp Device Claim To Site’s imageId. |
| **skip**  boolean | Skip flag.  Choices:   - `false` - `true` |
| **ipInterfaceName**  string  added in cisco.dnac 6.4.0 | Pnp Device Claim To Site’s ipInterfaceName. |
| **removeInactive**  boolean  added in cisco.dnac 6.4.0 | RemoveInactive flag.  Choices:   - `false` - `true` |
| **rfProfile**  string  added in cisco.dnac 6.1.0 | Pnp Device Claim To Site’s rfProfile. |
| **siteId**  string | Pnp Device Claim To Site’s siteId. |
| **staticIP**  string  added in cisco.dnac 6.4.0 | Pnp Device Claim To Site’s staticIP. |
| **subnetMask**  string | Pnp Device Claim To Site’s subnetMask. |
| **type**  string | Pnp Device Claim To Site’s type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **vlanId**  string  added in cisco.dnac 6.4.0 | Pnp Device Claim To Site’s vlanId. |

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
      configId: string
      configParameters:
      - key: string
        value: string
    deviceId: string
    gateway: string
    hostname: string
    imageId: string
    imageInfo:
      imageId: string
      skip: true
    ipInterfaceName: string
    removeInactive: true
    rfProfile: string
    siteId: string
    staticIP: string
    subnetMask: string
    type: string
    vlanId: string
```

## [Return Values](pnp_device_claim_to_site_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": "string", "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
