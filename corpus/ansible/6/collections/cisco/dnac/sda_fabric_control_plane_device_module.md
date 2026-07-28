---
collection: ansible
version: "6"
title: "cisco.dnac.sda_fabric_control_plane_device module – Resource module for Sda Fabric Control Plane Device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/sda_fabric_control_plane_device_module.html
fetched_at: 2026-07-27T16:53:47+00:00
---
# cisco.dnac.sda_fabric_control_plane_device module – Resource module for Sda Fabric Control Plane Device

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
> see [Requirements](sda_fabric_control_plane_device_module.md#ansible-collections-cisco-dnac-sda-fabric-control-plane-device-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sda_fabric_control_plane_device`.

New in cisco.dnac 3.1.0

- [Synopsis](sda_fabric_control_plane_device_module.md#synopsis)
- [Requirements](sda_fabric_control_plane_device_module.md#requirements)
- [Parameters](sda_fabric_control_plane_device_module.md#parameters)
- [Notes](sda_fabric_control_plane_device_module.md#notes)
- [See Also](sda_fabric_control_plane_device_module.md#see-also)
- [Examples](sda_fabric_control_plane_device_module.md#examples)
- [Return Values](sda_fabric_control_plane_device_module.md#return-values)

## [Synopsis](sda_fabric_control_plane_device_module.md#id1)

- Manage operations create and delete of the resource Sda Fabric Control Plane Device.
- Add control plane device in SDA Fabric.
- Delete control plane device in SDA Fabric.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sda_fabric_control_plane_device_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sda_fabric_control_plane_device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deviceManagementIpAddress**  string  added in cisco.dnac 4.0.0 | DeviceManagementIpAddress query parameter. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **payload**  list / elements=dictionary | Sda Fabric Control Plane Device’s payload. |
| **deviceManagementIpAddress**  string  added in cisco.dnac 4.0.0 | Management Ip Address of the Device which is provisioned successfully. |
| **siteNameHierarchy**  string  added in cisco.dnac 4.0.0 | SiteNameHierarchy of the Provisioned Device(site should be part of Fabric Site(site should be part of Fabric Site). |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](sda_fabric_control_plane_device_module.md#id4)

> **Note:**
>
> - SDK Method used are sda.Sda.add_control_plane_device, sda.Sda.delete_control_plane_device,
> - Paths used are post /dna/intent/api/v1/business/sda/control-plane-device, delete /dna/intent/api/v1/business/sda/control-plane-device,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sda_fabric_control_plane_device_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for SDA AddControlPlaneDeviceInSDAFabric](https://developer.cisco.com/docs/dna-center/#!add-control-plane-device-in-sda-fabric)
> :   Complete reference of the AddControlPlaneDeviceInSDAFabric API.
>
> [Cisco DNA Center documentation for SDA DeleteControlPlaneDeviceInSDAFabric](https://developer.cisco.com/docs/dna-center/#!delete-control-plane-device-in-sda-fabric)
> :   Complete reference of the DeleteControlPlaneDeviceInSDAFabric API.

## [Examples](sda_fabric_control_plane_device_module.md#id6)

```yaml+jinja
- name: Delete all
  cisco.dnac.sda_fabric_control_plane_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceManagementIpAddress: string

- name: Create
  cisco.dnac.sda_fabric_control_plane_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - deviceManagementIpAddress: string
      siteNameHierarchy: string
```

## [Return Values](sda_fabric_control_plane_device_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"description": "string", "executionId": "string", "executionStatusUrl": "string", "status": "string", "taskId": "string", "taskStatusUrl": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
