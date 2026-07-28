---
collection: ansible
version: "6"
title: "cisco.dnac.swim_trigger_activation module – Resource module for Swim Trigger Activation"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/swim_trigger_activation_module.html
fetched_at: 2026-07-27T16:54:24+00:00
---
# cisco.dnac.swim_trigger_activation module – Resource module for Swim Trigger Activation

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
> see [Requirements](swim_trigger_activation_module.md#ansible-collections-cisco-dnac-swim-trigger-activation-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.swim_trigger_activation`.

New in cisco.dnac 3.1.0

- [Synopsis](swim_trigger_activation_module.md#synopsis)
- [Requirements](swim_trigger_activation_module.md#requirements)
- [Parameters](swim_trigger_activation_module.md#parameters)
- [Notes](swim_trigger_activation_module.md#notes)
- [See Also](swim_trigger_activation_module.md#see-also)
- [Examples](swim_trigger_activation_module.md#examples)
- [Return Values](swim_trigger_activation_module.md#return-values)

## [Synopsis](swim_trigger_activation_module.md#id1)

- Manage operation create of the resource Swim Trigger Activation.
- Activates a software image on a given device. Software image must be present in the device flash.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](swim_trigger_activation_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](swim_trigger_activation_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **payload**  list / elements=dictionary | Swim Trigger Activation’s payload. |
| **activateLowerImageVersion**  boolean | ActivateLowerImageVersion flag.  Choices:   - `false` - `true` |
| **deviceUpgradeMode**  string | Swim Trigger Activation’s deviceUpgradeMode. |
| **deviceUuid**  string | Swim Trigger Activation’s deviceUuid. |
| **distributeIfNeeded**  boolean | DistributeIfNeeded flag.  Choices:   - `false` - `true` |
| **imageUuidList**  list / elements=string | Swim Trigger Activation’s imageUuidList. |
| **smuImageUuidList**  list / elements=string | Swim Trigger Activation’s smuImageUuidList. |
| **scheduleValidate**  boolean | ScheduleValidate query parameter. ScheduleValidate, validates data before schedule (Optional).  Choices:   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](swim_trigger_activation_module.md#id4)

> **Note:**
>
> - SDK Method used are software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_activation,
> - Paths used are post /dna/intent/api/v1/image/activation/device,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](swim_trigger_activation_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Software Image Management (SWIM) TriggerSoftwareImageActivation](https://developer.cisco.com/docs/dna-center/#!trigger-software-image-activation)
> :   Complete reference of the TriggerSoftwareImageActivation API.

## [Examples](swim_trigger_activation_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.swim_trigger_activation:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: '{{my_headers | from_json}}'
    payload:
    - activateLowerImageVersion: true
      deviceUpgradeMode: string
      deviceUuid: string
      distributeIfNeeded: true
      imageUuidList:
      - string
      smuImageUuidList:
      - string
    scheduleValidate: true
```

## [Return Values](swim_trigger_activation_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
