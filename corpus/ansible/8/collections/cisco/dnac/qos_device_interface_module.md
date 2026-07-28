---
collection: ansible
version: "8"
title: "cisco.dnac.qos_device_interface module – Resource module for Qos Device Interface"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/qos_device_interface_module.html
fetched_at: 2026-07-28T01:24:14+00:00
---
# cisco.dnac.qos_device_interface module – Resource module for Qos Device Interface

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
> see [Requirements](qos_device_interface_module.md#ansible-collections-cisco-dnac-qos-device-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.qos_device_interface`.

New in cisco.dnac 4.0.0

- [Synopsis](qos_device_interface_module.md#synopsis)
- [Requirements](qos_device_interface_module.md#requirements)
- [Parameters](qos_device_interface_module.md#parameters)
- [Notes](qos_device_interface_module.md#notes)
- [See Also](qos_device_interface_module.md#see-also)
- [Examples](qos_device_interface_module.md#examples)
- [Return Values](qos_device_interface_module.md#return-values)

## [Synopsis](qos_device_interface_module.md#id1)

- Manage operations create, update and delete of the resource Qos Device Interface.
- Create qos device interface infos associate with network device id to allow the user to mark specific interfaces as WAN, to associate WAN interfaces with specific SP Profile and to be able to define a shaper on WAN interfaces.
- Delete all qos device interface infos associate with network device id.
- Update existing qos device interface infos associate with network device id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](qos_device_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](qos_device_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **id**  string | Id path parameter. Id of the qos device info, this object holds all qos device interface infos associate with network device id. |
| **payload**  list / elements=dictionary | Qos Device Interface’s payload. |
| **excludedInterfaces**  list / elements=string | Excluded interfaces ids. |
| **id**  string | Id of Qos device info. |
| **name**  string | Device name. |
| **networkDeviceId**  string | Network device id. |
| **qosDeviceInterfaceInfo**  list / elements=dictionary | Qos Device Interface’s qosDeviceInterfaceInfo. |
| **dmvpnRemoteSitesBw**  list / elements=integer | Dmvpn remote sites bandwidth. |
| **instanceId**  integer | Instance id. |
| **interfaceId**  string | Interface id. |
| **interfaceName**  string | Interface name. |
| **label**  string | SP Profile name. |
| **role**  string | Interface role. |
| **uploadBW**  integer | Upload bandwidth. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](qos_device_interface_module.md#id4)

> **Note:**
>
> - SDK Method used are application_policy.ApplicationPolicy.create_qos_device_interface_info, application_policy.ApplicationPolicy.delete_qos_device_interface_info, application_policy.ApplicationPolicy.update_qos_device_interface_info,
> - Paths used are post /dna/intent/api/v1/qos-device-interface-info, delete /dna/intent/api/v1/qos-device-interface-info/{id}, put /dna/intent/api/v1/qos-device-interface-info,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](qos_device_interface_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Application Policy CreateQosDeviceInterfaceInfo](https://developer.cisco.com/docs/dna-center/#!create-qos-device-interface-info)
> :   Complete reference of the CreateQosDeviceInterfaceInfo API.
>
> [Cisco DNA Center documentation for Application Policy DeleteQosDeviceInterfaceInfo](https://developer.cisco.com/docs/dna-center/#!delete-qos-device-interface-info)
> :   Complete reference of the DeleteQosDeviceInterfaceInfo API.
>
> [Cisco DNA Center documentation for Application Policy UpdateQosDeviceInterfaceInfo](https://developer.cisco.com/docs/dna-center/#!update-qos-device-interface-info)
> :   Complete reference of the UpdateQosDeviceInterfaceInfo API.

## [Examples](qos_device_interface_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.qos_device_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - excludedInterfaces:
      - string
      id: string
      name: string
      networkDeviceId: string
      qosDeviceInterfaceInfo:
      - dmvpnRemoteSitesBw:
        - 0
        instanceId: 0
        interfaceId: string
        interfaceName: string
        label: string
        role: string
        uploadBW: 0

- name: Create
  cisco.dnac.qos_device_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - excludedInterfaces:
      - string
      name: string
      networkDeviceId: string
      qosDeviceInterfaceInfo:
      - dmvpnRemoteSitesBw:
        - 0
        interfaceId: string
        interfaceName: string
        label: string
        role: string
        uploadBW: 0

- name: Delete by id
  cisco.dnac.qos_device_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
```

## [Return Values](qos_device_interface_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
