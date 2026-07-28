---
collection: ansible
version: "8"
title: "cisco.dnac.pnp_device_config_preview module – Resource module for Pnp Device Config Preview"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/pnp_device_config_preview_module.html
fetched_at: 2026-07-28T01:23:56+00:00
---
# cisco.dnac.pnp_device_config_preview module – Resource module for Pnp Device Config Preview

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
> see [Requirements](pnp_device_config_preview_module.md#ansible-collections-cisco-dnac-pnp-device-config-preview-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_device_config_preview`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_device_config_preview_module.md#synopsis)
- [Requirements](pnp_device_config_preview_module.md#requirements)
- [Parameters](pnp_device_config_preview_module.md#parameters)
- [Notes](pnp_device_config_preview_module.md#notes)
- [See Also](pnp_device_config_preview_module.md#see-also)
- [Examples](pnp_device_config_preview_module.md#examples)
- [Return Values](pnp_device_config_preview_module.md#return-values)

## [Synopsis](pnp_device_config_preview_module.md#id1)

- Manage operation create of the resource Pnp Device Config Preview.
- Triggers a preview for site-based Day 0 Configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_device_config_preview_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_device_config_preview_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceId**  string | Pnp Device Config Preview’s deviceId. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **siteId**  string | Pnp Device Config Preview’s siteId. |
| **type**  string | Pnp Device Config Preview’s type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](pnp_device_config_preview_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.preview_config,
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-device/site-config-preview,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_device_config_preview_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) PreviewConfig](https://developer.cisco.com/docs/dna-center/#!preview-config)
> :   Complete reference of the PreviewConfig API.

## [Examples](pnp_device_config_preview_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.pnp_device_config_preview:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
    siteId: string
    type: string
```

## [Return Values](pnp_device_config_preview_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"complete": true, "config": "string", "error": true, "errorMessage": "string", "expiredTime": 0, "rfProfile": "string", "sensorProfile": "string", "siteId": "string", "startTime": 0, "taskId": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
