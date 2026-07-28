---
collection: ansible
version: "6"
title: "cisco.dnac.device_replacement module – Resource module for Device Replacement"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/device_replacement_module.html
fetched_at: 2026-07-27T16:51:35+00:00
---
# cisco.dnac.device_replacement module – Resource module for Device Replacement

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
> see [Requirements](device_replacement_module.md#ansible-collections-cisco-dnac-device-replacement-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.device_replacement`.

New in cisco.dnac 3.1.0

- [Synopsis](device_replacement_module.md#synopsis)
- [Requirements](device_replacement_module.md#requirements)
- [Parameters](device_replacement_module.md#parameters)
- [Notes](device_replacement_module.md#notes)
- [See Also](device_replacement_module.md#see-also)
- [Examples](device_replacement_module.md#examples)
- [Return Values](device_replacement_module.md#return-values)

## [Synopsis](device_replacement_module.md#id1)

- Manage operations create and update of the resource Device Replacement.
- Marks device for replacement.
- UnMarks device for replacement.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_replacement_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](device_replacement_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **payload**  list / elements=dictionary | Device Replacement’s payload. |
| **creationTime**  integer | Device Replacement’s creationTime. |
| **family**  string | Device Replacement’s family. |
| **faultyDeviceId**  string | Device Replacement’s faultyDeviceId. |
| **faultyDeviceName**  string | Device Replacement’s faultyDeviceName. |
| **faultyDevicePlatform**  string | Device Replacement’s faultyDevicePlatform. |
| **faultyDeviceSerialNumber**  string | Device Replacement’s faultyDeviceSerialNumber. |
| **id**  string | Device Replacement’s id. |
| **neighbourDeviceId**  string | Device Replacement’s neighbourDeviceId. |
| **networkReadinessTaskId**  string | Device Replacement’s networkReadinessTaskId. |
| **replacementDevicePlatform**  string | Device Replacement’s replacementDevicePlatform. |
| **replacementDeviceSerialNumber**  string | Device Replacement’s replacementDeviceSerialNumber. |
| **replacementStatus**  string | Device Replacement’s replacementStatus. |
| **replacementTime**  integer | Device Replacement’s replacementTime. |
| **workflowId**  string | Device Replacement’s workflowId. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](device_replacement_module.md#id4)

> **Note:**
>
> - SDK Method used are device_replacement.DeviceReplacement.mark_device_for_replacement, device_replacement.DeviceReplacement.unmark_device_for_replacement,
> - Paths used are post /dna/intent/api/v1/device-replacement, put /dna/intent/api/v1/device-replacement,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](device_replacement_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Replacement MarkDeviceForReplacement](https://developer.cisco.com/docs/dna-center/#!mark-device-for-replacement)
> :   Complete reference of the MarkDeviceForReplacement API.
>
> [Cisco DNA Center documentation for Device Replacement UnMarkDeviceForReplacement](https://developer.cisco.com/docs/dna-center/#!un-mark-device-for-replacement)
> :   Complete reference of the UnMarkDeviceForReplacement API.

## [Examples](device_replacement_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.device_replacement:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - creationTime: 0
      family: string
      faultyDeviceId: string
      faultyDeviceName: string
      faultyDevicePlatform: string
      faultyDeviceSerialNumber: string
      id: string
      neighbourDeviceId: string
      networkReadinessTaskId: string
      replacementDevicePlatform: string
      replacementDeviceSerialNumber: string
      replacementStatus: string
      replacementTime: 0
      workflowId: string

- name: Create
  cisco.dnac.device_replacement:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - creationTime: 0
      family: string
      faultyDeviceId: string
      faultyDeviceName: string
      faultyDevicePlatform: string
      faultyDeviceSerialNumber: string
      id: string
      neighbourDeviceId: string
      networkReadinessTaskId: string
      replacementDevicePlatform: string
      replacementDeviceSerialNumber: string
      replacementStatus: string
      replacementTime: 0
      workflowId: string
```

## [Return Values](device_replacement_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
