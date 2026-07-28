---
collection: ansible
version: "6"
title: "cisco.dnac.sda_multicast module – Resource module for Sda Multicast"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/sda_multicast_module.html
fetched_at: 2026-07-27T16:53:51+00:00
---
# cisco.dnac.sda_multicast module – Resource module for Sda Multicast

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
> see [Requirements](sda_multicast_module.md#ansible-collections-cisco-dnac-sda-multicast-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sda_multicast`.

New in cisco.dnac 3.1.0

- [Synopsis](sda_multicast_module.md#synopsis)
- [Requirements](sda_multicast_module.md#requirements)
- [Parameters](sda_multicast_module.md#parameters)
- [Notes](sda_multicast_module.md#notes)
- [See Also](sda_multicast_module.md#see-also)
- [Examples](sda_multicast_module.md#examples)
- [Return Values](sda_multicast_module.md#return-values)

## [Synopsis](sda_multicast_module.md#id1)

- Manage operations create and delete of the resource Sda Multicast.
- Add multicast in SDA fabric.
- Delete multicast from SDA fabric.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sda_multicast_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](sda_multicast_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **multicastMethod**  string | Multicast Method. |
| **multicastType**  string | Multicast Type. |
| **multicastVnInfo**  list / elements=dictionary | Sda Multicast’s multicastVnInfo. |
| **externalRpIpAddress**  string | ExternalRpIpAddress, required if multicastType is asm_with_external_rp. |
| **internalRpIpAddress**  list / elements=string | InternalRpIpAddress, required if multicastType is asm_with_internal_rp. |
| **ipPoolName**  string | Ip Pool Name, that is reserved to Fabric Site. |
| **ssmInfo**  dictionary | Sda Multicast’s ssmInfo. |
| **ssmGroupRange**  string | Valid SSM group range ip address(e.g., 230.0.0.0). |
| **ssmWildcardMask**  string | Valid SSM Wildcard Mask ip address(e.g.,0.255.255.255). |
| **virtualNetworkName**  string | Virtual Network Name, that is associated to Fabric Site. |
| **siteNameHierarchy**  string | Full path of sda Fabric Site. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](sda_multicast_module.md#id4)

> **Note:**
>
> - SDK Method used are sda.Sda.add_multicast_in_sda_fabric, sda.Sda.delete_multicast_from_sda_fabric,
> - Paths used are post /dna/intent/api/v1/business/sda/multicast, delete /dna/intent/api/v1/business/sda/multicast,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](sda_multicast_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for SDA AddMulticastInSDAFabric](https://developer.cisco.com/docs/dna-center/#!add-multicast-in-sda-fabric)
> :   Complete reference of the AddMulticastInSDAFabric API.
>
> [Cisco DNA Center documentation for SDA DeleteMulticastFromSDAFabric](https://developer.cisco.com/docs/dna-center/#!delete-multicast-from-sda-fabric)
> :   Complete reference of the DeleteMulticastFromSDAFabric API.

## [Examples](sda_multicast_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.sda_multicast:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    multicastMethod: string
    multicastType: string
    multicastVnInfo:
    - externalRpIpAddress: string
      internalRpIpAddress:
      - string
      ipPoolName: string
      ssmInfo:
        ssmGroupRange: string
        ssmWildcardMask: string
      virtualNetworkName: string
    siteNameHierarchy: string

- name: Delete all
  cisco.dnac.sda_multicast:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    siteNameHierarchy: string
```

## [Return Values](sda_multicast_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"description": "string", "executionId": "string", "executionStatusUrl": "string", "status": "string", "taskId": "string", "taskStatusUrl": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
