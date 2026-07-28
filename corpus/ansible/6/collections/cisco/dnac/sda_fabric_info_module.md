---
collection: ansible
version: "6"
title: "cisco.dnac.sda_fabric_info module – Information module for Sda Fabric"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/sda_fabric_info_module.html
fetched_at: 2026-07-27T16:53:49+00:00
---
# cisco.dnac.sda_fabric_info module – Information module for Sda Fabric

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
> see [Requirements](sda_fabric_info_module.md#ansible-collections-cisco-dnac-sda-fabric-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.sda_fabric_info`.

New in cisco.dnac 3.1.0

- [Synopsis](sda_fabric_info_module.md#synopsis)
- [Requirements](sda_fabric_info_module.md#requirements)
- [Parameters](sda_fabric_info_module.md#parameters)
- [Notes](sda_fabric_info_module.md#notes)
- [Examples](sda_fabric_info_module.md#examples)
- [Return Values](sda_fabric_info_module.md#return-values)

## [Synopsis](sda_fabric_info_module.md#id1)

- Get all Sda Fabric.
- Get SDA Fabric Info.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sda_fabric_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.4.9
- python >= 3.5

## [Parameters](sda_fabric_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **fabricName**  string | FabricName query parameter. Fabric Name. |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](sda_fabric_info_module.md#id4)

> **Note:**
>
> - SDK Method used are sda.Sda.get_sda_fabric_info,
> - Paths used are get /dna/intent/api/v1/business/sda/fabric,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](sda_fabric_info_module.md#id5)

```yaml+jinja
- name: Get all Sda Fabric
  cisco.dnac.sda_fabric_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    fabricName: string
  register: result
```

## [Return Values](sda_fabric_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"description": "string", "executionId": "string", "fabricDomainType": "string", "fabricName": "string", "fabricType": "string", "status": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
