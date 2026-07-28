---
collection: ansible
version: "8"
title: "cisco.dnac.credential_to_site_by_siteid_create_v2 module – Resource module for Credential To Site By Siteid Create V2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/credential_to_site_by_siteid_create_v2_module.html
fetched_at: 2026-07-28T01:21:48+00:00
---
# cisco.dnac.credential_to_site_by_siteid_create_v2 module – Resource module for Credential To Site By Siteid Create V2

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
> see [Requirements](credential_to_site_by_siteid_create_v2_module.md#ansible-collections-cisco-dnac-credential-to-site-by-siteid-create-v2-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.credential_to_site_by_siteid_create_v2`.

New in cisco.dnac 6.7.0

- [Synopsis](credential_to_site_by_siteid_create_v2_module.md#synopsis)
- [Requirements](credential_to_site_by_siteid_create_v2_module.md#requirements)
- [Parameters](credential_to_site_by_siteid_create_v2_module.md#parameters)
- [Notes](credential_to_site_by_siteid_create_v2_module.md#notes)
- [See Also](credential_to_site_by_siteid_create_v2_module.md#see-also)
- [Examples](credential_to_site_by_siteid_create_v2_module.md#examples)
- [Return Values](credential_to_site_by_siteid_create_v2_module.md#return-values)

## [Synopsis](credential_to_site_by_siteid_create_v2_module.md#id1)

- Manage operation create of the resource Credential To Site By Siteid Create V2.
- API to assign Device Credential to a site.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](credential_to_site_by_siteid_create_v2_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](credential_to_site_by_siteid_create_v2_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cliId**  string | CLI Credential Id. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **httpRead**  string | HTTP(S) Read Credential Id. |
| **httpWrite**  string | HTTP(S) Write Credential Id. |
| **siteId**  string | SiteId path parameter. Site Id to assign credential. |
| **snmpV2ReadId**  string | SNMPv2c Read Credential Id. |
| **snmpV2WriteId**  string | SNMPv2c Write Credential Id. |
| **snmpV3Id**  string | SNMPv3 Credential Id. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](credential_to_site_by_siteid_create_v2_module.md#id4)

> **Note:**
>
> - SDK Method used are network_settings.NetworkSettings.assign_device_credential_to_site_v2,
> - Paths used are post /dna/intent/api/v2/credential-to-site/{siteId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](credential_to_site_by_siteid_create_v2_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Network Settings AssignDeviceCredentialToSiteV2](https://developer.cisco.com/docs/dna-center/#!assign-device-credential-to-site-v-2)
> :   Complete reference of the AssignDeviceCredentialToSiteV2 API.

## [Examples](credential_to_site_by_siteid_create_v2_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.credential_to_site_by_siteid_create_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    cliId: string
    httpRead: string
    httpWrite: string
    siteId: string
    snmpV2ReadId: string
    snmpV2WriteId: string
    snmpV3Id: string
```

## [Return Values](credential_to_site_by_siteid_create_v2_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
