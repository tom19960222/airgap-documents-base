---
collection: ansible
version: "6"
title: "cisco.dnac.interface_update module – Resource module for Interface Update"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/interface_update_module.html
fetched_at: 2026-07-27T16:52:22+00:00
---
# cisco.dnac.interface_update module – Resource module for Interface Update

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
> see [Requirements](interface_update_module.md#ansible-collections-cisco-dnac-interface-update-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.interface_update`.

New in cisco.dnac 6.0.0

- [Synopsis](interface_update_module.md#synopsis)
- [Requirements](interface_update_module.md#requirements)
- [Parameters](interface_update_module.md#parameters)
- [Notes](interface_update_module.md#notes)
- [See Also](interface_update_module.md#see-also)
- [Examples](interface_update_module.md#examples)
- [Return Values](interface_update_module.md#return-values)

## [Synopsis](interface_update_module.md#id1)

- Manage operation update of the resource Interface Update.
- Add/Update Interface description, VLAN membership, Voice VLAN and change Interface admin status ‘UP’/’DOWN’ from Request body.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](interface_update_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](interface_update_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **adminStatus**  string | Admin Status. |
| **deploymentMode**  string | DeploymentMode query parameter. Preview/Deploy ‘Preview’ means the configuration is not pushed to the device. ‘Deploy’ makes the configuration pushed to the device. |
| **description**  string | Description. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **interfaceUuid**  string | InterfaceUuid path parameter. Interface ID. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **vlanId**  integer | Vlan Id. |
| **voiceVlanId**  integer | Voice Vlan Id. |

## [Notes](interface_update_module.md#id4)

> **Note:**
>
> - SDK Method used are devices.Devices.update_interface_details,
> - Paths used are put /dna/intent/api/v1/interface/{interfaceUuid},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](interface_update_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Devices UpdateInterfaceDetails](https://developer.cisco.com/docs/dna-center/#!update-interface-details)
> :   Complete reference of the UpdateInterfaceDetails API.

## [Examples](interface_update_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.dnac.interface_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    adminStatus: string
    deploymentMode: string
    description: string
    interfaceUuid: string
    vlanId: 0
    voiceVlanId: 0
```

## [Return Values](interface_update_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"properties": {"taskId": {"type": "string"}, "url": {"type": "string"}}, "required": ["string"], "type": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
