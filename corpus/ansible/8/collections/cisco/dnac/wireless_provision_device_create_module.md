---
collection: ansible
version: "8"
title: "cisco.dnac.wireless_provision_device_create module – Resource module for Wireless Provision Device Create"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/wireless_provision_device_create_module.html
fetched_at: 2026-07-28T01:25:50+00:00
---
# cisco.dnac.wireless_provision_device_create module – Resource module for Wireless Provision Device Create

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
> see [Requirements](wireless_provision_device_create_module.md#ansible-collections-cisco-dnac-wireless-provision-device-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_provision_device_create`.

New in cisco.dnac 3.1.0

- [Synopsis](wireless_provision_device_create_module.md#synopsis)
- [Requirements](wireless_provision_device_create_module.md#requirements)
- [Parameters](wireless_provision_device_create_module.md#parameters)
- [Notes](wireless_provision_device_create_module.md#notes)
- [See Also](wireless_provision_device_create_module.md#see-also)
- [Examples](wireless_provision_device_create_module.md#examples)
- [Return Values](wireless_provision_device_create_module.md#return-values)

## [Synopsis](wireless_provision_device_create_module.md#id1)

- Manage operation create of the resource Wireless Provision Device Create.
- Provision wireless devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_provision_device_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_provision_device_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **payload**  list / elements=dictionary | Wireless Provision Device Create’s payload. |
| **deviceName**  string | Controller Name. |
| **dynamicInterfaces**  list / elements=dictionary | Wireless Provision Device Create’s dynamicInterfaces. |
| **interfaceGateway**  string | Interface Gateway. |
| **interfaceIPAddress**  string | Interface IP Address. |
| **interfaceName**  string | Interface Name. |
| **interfaceNetmaskInCIDR**  integer | Interface Netmask In CIDR. |
| **lagOrPortNumber**  integer | Lag Or Port Number. |
| **vlanId**  integer | VLAN ID. |
| **managedAPLocations**  list / elements=string | List of managed AP locations (Site Hierarchies). |
| **site**  string | Full Site Hierarchy where device has to be assigned. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](wireless_provision_device_create_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.provision,
> - Paths used are post /dna/intent/api/v1/wireless/provision,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_provision_device_create_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless Provision](https://developer.cisco.com/docs/dna-center/#!provision)
> :   Complete reference of the Provision API.

## [Examples](wireless_provision_device_create_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.wireless_provision_device_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
    - deviceName: string
      dynamicInterfaces:
      - interfaceGateway: string
        interfaceIPAddress: string
        interfaceName: string
        interfaceNetmaskInCIDR: 0
        lagOrPortNumber: 0
        vlanId: 0
      managedAPLocations:
      - string
      site: string
```

## [Return Values](wireless_provision_device_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionUrl": "string", "provisioningTasks": {"failed": ["string"], "success": ["string"]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
