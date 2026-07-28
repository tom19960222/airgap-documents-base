---
collection: ansible
version: "6"
title: "cisco.dnac.pnp_device_claim module – Resource module for Pnp Device Claim"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/pnp_device_claim_module.html
fetched_at: 2026-07-27T16:53:11+00:00
---
# cisco.dnac.pnp_device_claim module – Resource module for Pnp Device Claim

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
> see [Requirements](pnp_device_claim_module.md#ansible-collections-cisco-dnac-pnp-device-claim-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_device_claim`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_device_claim_module.md#synopsis)
- [Requirements](pnp_device_claim_module.md#requirements)
- [Parameters](pnp_device_claim_module.md#parameters)
- [Notes](pnp_device_claim_module.md#notes)
- [See Also](pnp_device_claim_module.md#see-also)
- [Examples](pnp_device_claim_module.md#examples)
- [Return Values](pnp_device_claim_module.md#return-values)

## [Synopsis](pnp_device_claim_module.md#id1)

- Manage operation create of the resource Pnp Device Claim.
- Claims one of more devices with specified workflow.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_device_claim_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_device_claim_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **configFileUrl**  string | Pnp Device Claim’s configFileUrl. |
| **configId**  string | Pnp Device Claim’s configId. |
| **deviceClaimList**  list / elements=dictionary | Pnp Device Claim’s deviceClaimList. |
| **configList**  list / elements=dictionary | Pnp Device Claim’s configList. |
| **configId**  string | Pnp Device Claim’s configId. |
| **configParameters**  list / elements=dictionary | Pnp Device Claim’s configParameters. |
| **key**  string | Pnp Device Claim’s key. |
| **value**  string | Pnp Device Claim’s value. |
| **deviceId**  string | Pnp Device Claim’s deviceId. |
| **licenseLevel**  string | Pnp Device Claim’s licenseLevel. |
| **licenseType**  string | Pnp Device Claim’s licenseType. |
| **topOfStackSerialNumber**  string | Pnp Device Claim’s topOfStackSerialNumber. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **fileServiceId**  string | Pnp Device Claim’s fileServiceId. |
| **imageId**  string | Pnp Device Claim’s imageId. |
| **imageUrl**  string | Pnp Device Claim’s imageUrl. |
| **populateInventory**  boolean | PopulateInventory flag.  Choices:   - `false` - `true` |
| **projectId**  string | Pnp Device Claim’s projectId. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **workflowId**  string | Pnp Device Claim’s workflowId. |

## [Notes](pnp_device_claim_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.claim_device,
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-device/claim,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_device_claim_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) ClaimDevice](https://developer.cisco.com/docs/dna-center/#!claim-device)
> :   Complete reference of the ClaimDevice API.

## [Examples](pnp_device_claim_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.pnp_device_claim:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    configFileUrl: string
    configId: string
    deviceClaimList:
    - configList:
      - configId: string
        configParameters:
        - key: string
          value: string
      deviceId: string
      licenseLevel: string
      licenseType: string
      topOfStackSerialNumber: string
    fileServiceId: string
    imageId: string
    imageUrl: string
    populateInventory: true
    projectId: string
    workflowId: string
```

## [Return Values](pnp_device_claim_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"jsonArrayResponse": [{}], "jsonResponse": {}, "message": "string", "statusCode": 0}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
