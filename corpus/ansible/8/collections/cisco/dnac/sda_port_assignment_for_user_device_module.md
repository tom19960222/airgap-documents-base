---
collection: ansible
version: "8"
title: "cisco.dnac.sda_port_assignment_for_user_device module – Resource module for Sda Port Assignment For User Device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/sda_port_assignment_for_user_device_module.html
fetched_at: 2026-07-28T01:24:38+00:00
---
# cisco.dnac.sda_port_assignment_for_user_device module – Resource module for Sda Port Assignment For User Device

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
> see [Requirements](sda_port_assignment_for_user_device_module.md#ansible-collections-cisco-dnac-sda-port-assignment-for-user-device-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sda_port_assignment_for_user_device`.

New in cisco.dnac 3.1.0

- [Synopsis](sda_port_assignment_for_user_device_module.md#synopsis)
- [Requirements](sda_port_assignment_for_user_device_module.md#requirements)
- [Parameters](sda_port_assignment_for_user_device_module.md#parameters)
- [Notes](sda_port_assignment_for_user_device_module.md#notes)
- [See Also](sda_port_assignment_for_user_device_module.md#see-also)
- [Examples](sda_port_assignment_for_user_device_module.md#examples)
- [Return Values](sda_port_assignment_for_user_device_module.md#return-values)

## [Synopsis](sda_port_assignment_for_user_device_module.md#id1)

- Manage operations create and delete of the resource Sda Port Assignment For User Device.
- Add Port assignment for user device in SDA Fabric.
- Delete Port assignment for user device in SDA Fabric.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sda_port_assignment_for_user_device_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sda_port_assignment_for_user_device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authenticateTemplateName**  string  *added in cisco.dnac 4.0.0* | Authenticate TemplateName associated with siteNameHierarchy. |
| **dataIpAddressPoolName**  string  *added in cisco.dnac 4.0.0* | Ip Pool Name, that is assigned to virtual network with traffic type as DATA(can’t be empty if voiceIpAddressPoolName is empty). |
| **deviceManagementIpAddress**  string | DeviceManagementIpAddress query parameter. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **interfaceDescription**  string  *added in cisco.dnac 4.0.0* | User defined text message for port assignment. |
| **interfaceName**  string | InterfaceName query parameter. |
| **interfaceNames**  list / elements=string | List of Interface Names on the Edge Node Device. E.g.”GigabitEthernet1/0/3”,”GigabitEthernet1/0/4”. |
| **scalableGroupName**  string  *added in cisco.dnac 4.0.0* | Scalable Group name associated with VN. |
| **siteNameHierarchy**  string  *added in cisco.dnac 4.0.0* | Complete Path of SD-Access Fabric Site. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **voiceIpAddressPoolName**  string  *added in cisco.dnac 4.0.0* | Ip Pool Name, that is assigned to virtual network with traffic type as VOICE(can’t be empty if dataIpAddressPoolName is empty). |

## [Notes](sda_port_assignment_for_user_device_module.md#id4)

> **Note:**
>
> - SDK Method used are sda.Sda.add_port_assignment_for_user_device, sda.Sda.delete_port_assignment_for_user_device,
> - Paths used are post /dna/intent/api/v1/business/sda/hostonboarding/user-device, delete /dna/intent/api/v1/business/sda/hostonboarding/user-device,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sda_port_assignment_for_user_device_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for SDA AddPortAssignmentForUserDeviceInSDAFabric](https://developer.cisco.com/docs/dna-center/#!add-port-assignment-for-user-device-in-sda-fabric)
> :   Complete reference of the AddPortAssignmentForUserDeviceInSDAFabric API.
>
> [Cisco DNA Center documentation for SDA DeletePortAssignmentForUserDeviceInSDAFabric](https://developer.cisco.com/docs/dna-center/#!delete-port-assignment-for-user-device-in-sda-fabric)
> :   Complete reference of the DeletePortAssignmentForUserDeviceInSDAFabric API.

## [Examples](sda_port_assignment_for_user_device_module.md#id6)

```yaml+jinja
- name: Delete all
  cisco.dnac.sda_port_assignment_for_user_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceManagementIpAddress: string
    interfaceName: string

- name: Create
  cisco.dnac.sda_port_assignment_for_user_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    authenticateTemplateName: string
    dataIpAddressPoolName: string
    deviceManagementIpAddress: string
    interfaceDescription: string
    interfaceName: string
    interfaceNames:
    - string
    scalableGroupName: string
    siteNameHierarchy: string
    voiceIpAddressPoolName: string
```

## [Return Values](sda_port_assignment_for_user_device_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"description": "string", "executionId": "string", "executionStatusUrl": "string", "status": "string", "taskId": "string", "taskStatusUrl": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
