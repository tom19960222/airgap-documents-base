---
collection: ansible
version: "8"
title: "cisco.dnac.security_advisories_devices_info module – Information module for Security Advisories Devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/security_advisories_devices_info_module.html
fetched_at: 2026-07-28T01:24:46+00:00
---
# cisco.dnac.security_advisories_devices_info module – Information module for Security Advisories Devices

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
> see [Requirements](security_advisories_devices_info_module.md#ansible-collections-cisco-dnac-security-advisories-devices-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.security_advisories_devices_info`.

New in cisco.dnac 3.1.0

- [Synopsis](security_advisories_devices_info_module.md#synopsis)
- [Requirements](security_advisories_devices_info_module.md#requirements)
- [Parameters](security_advisories_devices_info_module.md#parameters)
- [Notes](security_advisories_devices_info_module.md#notes)
- [See Also](security_advisories_devices_info_module.md#see-also)
- [Examples](security_advisories_devices_info_module.md#examples)
- [Return Values](security_advisories_devices_info_module.md#return-values)

## [Synopsis](security_advisories_devices_info_module.md#id1)

- Get all Security Advisories Devices.
- Retrieves list of devices for an advisory.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](security_advisories_devices_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](security_advisories_devices_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **advisoryId**  string | AdvisoryId path parameter. Advisory ID. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **headers**  dictionary | Additional headers. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](security_advisories_devices_info_module.md#id4)

> **Note:**
>
> - SDK Method used are security_advisories.SecurityAdvisories.get_devices_per_advisory,
> - Paths used are get /dna/intent/api/v1/security-advisory/advisory/{advisoryId}/device,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](security_advisories_devices_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Security Advisories GetDevicesPerAdvisory](https://developer.cisco.com/docs/dna-center/#!get-devices-per-advisory)
> :   Complete reference of the GetDevicesPerAdvisory API.

## [Examples](security_advisories_devices_info_module.md#id6)

```yaml+jinja
- name: Get all Security Advisories Devices
  cisco.dnac.security_advisories_devices_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    advisoryId: string
  register: result
```

## [Return Values](security_advisories_devices_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": ["string"], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
