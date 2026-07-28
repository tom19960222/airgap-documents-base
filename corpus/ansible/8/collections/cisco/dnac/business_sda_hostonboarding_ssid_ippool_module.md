---
collection: ansible
version: "8"
title: "cisco.dnac.business_sda_hostonboarding_ssid_ippool module – Resource module for Business Sda Hostonboarding Ssid Ippool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/business_sda_hostonboarding_ssid_ippool_module.html
fetched_at: 2026-07-28T01:21:25+00:00
---
# cisco.dnac.business_sda_hostonboarding_ssid_ippool module – Resource module for Business Sda Hostonboarding Ssid Ippool

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
> see [Requirements](business_sda_hostonboarding_ssid_ippool_module.md#ansible-collections-cisco-dnac-business-sda-hostonboarding-ssid-ippool-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.business_sda_hostonboarding_ssid_ippool`.

New in cisco.dnac 4.0.0

- [Synopsis](business_sda_hostonboarding_ssid_ippool_module.md#synopsis)
- [Requirements](business_sda_hostonboarding_ssid_ippool_module.md#requirements)
- [Parameters](business_sda_hostonboarding_ssid_ippool_module.md#parameters)
- [Notes](business_sda_hostonboarding_ssid_ippool_module.md#notes)
- [See Also](business_sda_hostonboarding_ssid_ippool_module.md#see-also)
- [Examples](business_sda_hostonboarding_ssid_ippool_module.md#examples)
- [Return Values](business_sda_hostonboarding_ssid_ippool_module.md#return-values)

## [Synopsis](business_sda_hostonboarding_ssid_ippool_module.md#id1)

- Manage operations create and update of the resource Business Sda Hostonboarding Ssid Ippool.
- Add SSID to IP Pool Mapping.
- Update SSID to IP Pool Mapping.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](business_sda_hostonboarding_ssid_ippool_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](business_sda_hostonboarding_ssid_ippool_module.md#id3)

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
| **scalableGroupName**  string | Scalable Group Name. |
| **siteNameHierarchy**  string | Site Name Hierarchy. |
| **ssidNames**  list / elements=string | List of SSIDs. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |
| **vlanName**  string | VLAN Name. |

## [Notes](business_sda_hostonboarding_ssid_ippool_module.md#id4)

> **Note:**
>
> - SDK Method used are fabric_wireless.FabricWireless.add_ssid_to_ip_pool_mapping, fabric_wireless.FabricWireless.update_ssid_to_ip_pool_mapping,
> - Paths used are post /dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool, put /dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](business_sda_hostonboarding_ssid_ippool_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Fabric Wireless AddSSIDToIPPoolMapping](https://developer.cisco.com/docs/dna-center/#!add-ssid-to-ip-pool-mapping)
> :   Complete reference of the AddSSIDToIPPoolMapping API.
>
> [Cisco DNA Center documentation for Fabric Wireless UpdateSSIDToIPPoolMapping](https://developer.cisco.com/docs/dna-center/#!update-ssid-to-ip-pool-mapping)
> :   Complete reference of the UpdateSSIDToIPPoolMapping API.

## [Examples](business_sda_hostonboarding_ssid_ippool_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.business_sda_hostonboarding_ssid_ippool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    headers: '{{my_headers | from_json}}'
    scalableGroupName: string
    siteNameHierarchy: string
    ssidNames:
    - string
    vlanName: string

- name: Update all
  cisco.dnac.business_sda_hostonboarding_ssid_ippool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    scalableGroupName: string
    siteNameHierarchy: string
    ssidNames:
    - string
    vlanName: string
```

## [Return Values](business_sda_hostonboarding_ssid_ippool_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=string | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `["[\n  {\n    \"executionId\": \"string\"", "\n    \"executionStatusURL\": \"string\"", "\n    \"message\": \"string\"\n  }\n]\n"]` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
