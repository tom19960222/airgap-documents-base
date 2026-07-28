---
collection: ansible
version: "8"
title: "cisco.dnac.dnac_packages_info module – Information module for Dnac Packages"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/dnac_packages_info_module.html
fetched_at: 2026-07-28T01:22:14+00:00
---
# cisco.dnac.dnac_packages_info module – Information module for Dnac Packages

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
> see [Requirements](dnac_packages_info_module.md#ansible-collections-cisco-dnac-dnac-packages-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.dnac_packages_info`.

New in cisco.dnac 6.7.0

- [Synopsis](dnac_packages_info_module.md#synopsis)
- [Requirements](dnac_packages_info_module.md#requirements)
- [Parameters](dnac_packages_info_module.md#parameters)
- [Notes](dnac_packages_info_module.md#notes)
- [See Also](dnac_packages_info_module.md#see-also)
- [Examples](dnac_packages_info_module.md#examples)
- [Return Values](dnac_packages_info_module.md#return-values)

## [Synopsis](dnac_packages_info_module.md#id1)

- Get all Dnac Packages.
- Provides information such as name, version of packages installed on the DNA center.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](dnac_packages_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](dnac_packages_info_module.md#id3)

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

## [Notes](dnac_packages_info_module.md#id4)

> **Note:**
>
> - SDK Method used are platform.Platform.cisco_dna_center_packages_summary,
> - Paths used are get /dna/intent/api/v1/dnac-packages,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](dnac_packages_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Platform CiscoDNACenterPackagesSummary](https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-packages-summary)
> :   Complete reference of the CiscoDNACenterPackagesSummary API.

## [Examples](dnac_packages_info_module.md#id6)

```yaml+jinja
- name: Get all Dnac Packages
  cisco.dnac.dnac_packages_info:
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

## [Return Values](dnac_packages_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": [{"name": "string", "version": "string"}], "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
