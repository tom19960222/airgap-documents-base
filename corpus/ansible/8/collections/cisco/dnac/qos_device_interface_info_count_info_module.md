---
collection: ansible
version: "8"
title: "cisco.dnac.qos_device_interface_info_count_info module – Information module for Qos Device Interface Info Count"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/qos_device_interface_info_count_info_module.html
fetched_at: 2026-07-28T01:24:15+00:00
---
# cisco.dnac.qos_device_interface_info_count_info module – Information module for Qos Device Interface Info Count

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
> see [Requirements](qos_device_interface_info_count_info_module.md#ansible-collections-cisco-dnac-qos-device-interface-info-count-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.qos_device_interface_info_count_info`.

New in cisco.dnac 4.0.0

- [Synopsis](qos_device_interface_info_count_info_module.md#synopsis)
- [Requirements](qos_device_interface_info_count_info_module.md#requirements)
- [Parameters](qos_device_interface_info_count_info_module.md#parameters)
- [Notes](qos_device_interface_info_count_info_module.md#notes)
- [See Also](qos_device_interface_info_count_info_module.md#see-also)
- [Examples](qos_device_interface_info_count_info_module.md#examples)
- [Return Values](qos_device_interface_info_count_info_module.md#return-values)

## [Synopsis](qos_device_interface_info_count_info_module.md#id1)

- Get all Qos Device Interface Info Count.
- Get the number of all existing qos device interface infos group by network device id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](qos_device_interface_info_count_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](qos_device_interface_info_count_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](qos_device_interface_info_count_info_module.md#id4)

> **Note:**
>
> - SDK Method used are application_policy.ApplicationPolicy.get_qos_device_interface_info_count,
> - Paths used are get /dna/intent/api/v1/qos-device-interface-info-count,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](qos_device_interface_info_count_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Application Policy GetQosDeviceInterfaceInfoCount](https://developer.cisco.com/docs/dna-center/#!get-qos-device-interface-info-count)
> :   Complete reference of the GetQosDeviceInterfaceInfoCount API.

## [Examples](qos_device_interface_info_count_info_module.md#id6)

```yaml+jinja
- name: Get all Qos Device Interface Info Count
  cisco.dnac.qos_device_interface_info_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
```

## [Return Values](qos_device_interface_info_count_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": 0, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
