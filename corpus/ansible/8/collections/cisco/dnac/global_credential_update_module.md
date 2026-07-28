---
collection: ansible
version: "8"
title: "cisco.dnac.global_credential_update module – Resource module for Global Credential Update"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/global_credential_update_module.html
fetched_at: 2026-07-28T01:22:47+00:00
---
# cisco.dnac.global_credential_update module – Resource module for Global Credential Update

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
> see [Requirements](global_credential_update_module.md#ansible-collections-cisco-dnac-global-credential-update-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.global_credential_update`.

New in cisco.dnac 3.1.0

- [Synopsis](global_credential_update_module.md#synopsis)
- [Requirements](global_credential_update_module.md#requirements)
- [Parameters](global_credential_update_module.md#parameters)
- [Notes](global_credential_update_module.md#notes)
- [See Also](global_credential_update_module.md#see-also)
- [Examples](global_credential_update_module.md#examples)
- [Return Values](global_credential_update_module.md#return-values)

## [Synopsis](global_credential_update_module.md#id1)

- Manage operation update of the resource Global Credential Update.
- Update global credential for network devices in sites.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](global_credential_update_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](global_credential_update_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **globalCredentialId**  string | GlobalCredentialId path parameter. Global credential Uuid. |
| **siteUuids**  list / elements=string | Global Credential Update’s siteUuids. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](global_credential_update_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.update_global_credentials,
> - Paths used are put /dna/intent/api/v1/global-credential/{globalCredentialId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](global_credential_update_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery UpdateGlobalCredentials](https://developer.cisco.com/docs/dna-center/#!update-global-credentials)
> :   Complete reference of the UpdateGlobalCredentials API.

## [Examples](global_credential_update_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.dnac.global_credential_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    globalCredentialId: string
    siteUuids:
    - string
```

## [Return Values](global_credential_update_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
