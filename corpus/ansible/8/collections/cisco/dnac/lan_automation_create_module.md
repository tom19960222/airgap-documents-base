---
collection: ansible
version: "8"
title: "cisco.dnac.lan_automation_create module – Resource module for Lan Automation Create"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/lan_automation_create_module.html
fetched_at: 2026-07-28T01:23:04+00:00
---
# cisco.dnac.lan_automation_create module – Resource module for Lan Automation Create

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
> see [Requirements](lan_automation_create_module.md#ansible-collections-cisco-dnac-lan-automation-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.lan_automation_create`.

New in cisco.dnac 6.0.0

- [Synopsis](lan_automation_create_module.md#synopsis)
- [Requirements](lan_automation_create_module.md#requirements)
- [Parameters](lan_automation_create_module.md#parameters)
- [Notes](lan_automation_create_module.md#notes)
- [See Also](lan_automation_create_module.md#see-also)
- [Examples](lan_automation_create_module.md#examples)
- [Return Values](lan_automation_create_module.md#return-values)

## [Synopsis](lan_automation_create_module.md#id1)

- Manage operation create of the resource Lan Automation Create.
- Invoke this API to start LAN Automation for the given site.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](lan_automation_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](lan_automation_create_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **payload**  list / elements=dictionary | Lan Automation Create’s payload. |
| **discoveredDeviceSiteNameHierarchy**  string | Discovered device site name. |
| **hostNameFileId**  string | Use /dna/intent/api/v1/file/namespace/nw_orch api to get the file id for the already uploaded file in nw_orch namespace. |
| **hostNamePrefix**  string | Host name prefix which shall be assigned to the discovered device. |
| **ipPools**  list / elements=dictionary | Lan Automation Create’s ipPools. |
| **ipPoolName**  string | Name of the IP pool. |
| **ipPoolRole**  string | Role of the IP pool. Supported roles are MAIN_POOL and PHYSICAL_LINK_POOL. |
| **isisDomainPwd**  string | IS-IS domain password in plain text. |
| **mulitcastEnabled**  boolean | To enable underlay native multicast.  **Choices:**   - `false` - `true` |
| **peerDeviceManagmentIPAddress**  string | Peer seed management IP address. |
| **primaryDeviceInterfaceNames**  list / elements=string | The list of interfaces on primary seed via which the discovered devices are connected. |
| **primaryDeviceManagmentIPAddress**  string | Primary seed management IP address. |
| **redistributeIsisToBgp**  boolean | Advertise LAN Automation summary route into BGP.  **Choices:**   - `false` - `true` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](lan_automation_create_module.md#id4)

> **Note:**
>
> - SDK Method used are lan_automation.LanAutomation.lan_automation_start,
> - Paths used are post /dna/intent/api/v1/lan-automation,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](lan_automation_create_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for LAN Automation LANAutomationStart](https://developer.cisco.com/docs/dna-center/#!l-an-automation-start)
> :   Complete reference of the LANAutomationStart API.

## [Examples](lan_automation_create_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.lan_automation_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
    - discoveredDeviceSiteNameHierarchy: string
      hostNameFileId: string
      hostNamePrefix: string
      ipPools:
      - ipPoolName: string
        ipPoolRole: string
      isisDomainPwd: string
      mulitcastEnabled: true
      peerDeviceManagmentIPAddress: string
      primaryDeviceInterfaceNames:
      - string
      primaryDeviceManagmentIPAddress: string
      redistributeIsisToBgp: true
```

## [Return Values](lan_automation_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"id": "string", "message": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
