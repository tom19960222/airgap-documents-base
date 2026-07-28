---
collection: ansible
version: "8"
title: "cisco.dnac.topology_site_info module – Information module for Topology Site"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/topology_site_info_module.html
fetched_at: 2026-07-28T01:25:36+00:00
---
# cisco.dnac.topology_site_info module – Information module for Topology Site

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
> see [Requirements](topology_site_info_module.md#ansible-collections-cisco-dnac-topology-site-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.topology_site_info`.

New in cisco.dnac 3.1.0

- [Synopsis](topology_site_info_module.md#synopsis)
- [Requirements](topology_site_info_module.md#requirements)
- [Parameters](topology_site_info_module.md#parameters)
- [Notes](topology_site_info_module.md#notes)
- [See Also](topology_site_info_module.md#see-also)
- [Examples](topology_site_info_module.md#examples)
- [Return Values](topology_site_info_module.md#return-values)

## [Synopsis](topology_site_info_module.md#id1)

- Get all Topology Site.
- Returns site topology.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](topology_site_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](topology_site_info_module.md#id3)

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

## [Notes](topology_site_info_module.md#id4)

> **Note:**
>
> - SDK Method used are topology.Topology.get_site_topology,
> - Paths used are get /dna/intent/api/v1/topology/site-topology,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](topology_site_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Topology GetSiteTopology](https://developer.cisco.com/docs/dna-center/#!get-site-topology)
> :   Complete reference of the GetSiteTopology API.

## [Examples](topology_site_info_module.md#id6)

```yaml+jinja
- name: Get all Topology Site
  cisco.dnac.topology_site_info:
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

## [Return Values](topology_site_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"sites": [{"displayName": "string", "groupNameHierarchy": "string", "id": "string", "latitude": "string", "locationAddress": "string", "locationCountry": "string", "locationType": "string", "longitude": "string", "name": "string", "parentId": "string"}]}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
