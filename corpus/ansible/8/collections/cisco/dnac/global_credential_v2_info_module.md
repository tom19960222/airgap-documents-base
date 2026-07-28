---
collection: ansible
version: "8"
title: "cisco.dnac.global_credential_v2_info module – Information module for Global Credential V2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/global_credential_v2_info_module.html
fetched_at: 2026-07-28T01:22:48+00:00
---
# cisco.dnac.global_credential_v2_info module – Information module for Global Credential V2

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
> see [Requirements](global_credential_v2_info_module.md#ansible-collections-cisco-dnac-global-credential-v2-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.global_credential_v2_info`.

New in cisco.dnac 6.7.0

- [Synopsis](global_credential_v2_info_module.md#synopsis)
- [Requirements](global_credential_v2_info_module.md#requirements)
- [Parameters](global_credential_v2_info_module.md#parameters)
- [Notes](global_credential_v2_info_module.md#notes)
- [See Also](global_credential_v2_info_module.md#see-also)
- [Examples](global_credential_v2_info_module.md#examples)
- [Return Values](global_credential_v2_info_module.md#return-values)

## [Synopsis](global_credential_v2_info_module.md#id1)

- Get all Global Credential V2.
- API to get device credentials’ details. It fetches all global credentials of all types at once, without the need to pass any input parameters.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](global_credential_v2_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](global_credential_v2_info_module.md#id3)

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

## [Notes](global_credential_v2_info_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.get_all_global_credentials_v2,
> - Paths used are get /dna/intent/api/v2/global-credential,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](global_credential_v2_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery GetAllGlobalCredentialsV2](https://developer.cisco.com/docs/dna-center/#!get-all-global-credentials-v-2)
> :   Complete reference of the GetAllGlobalCredentialsV2 API.

## [Examples](global_credential_v2_info_module.md#id6)

```yaml+jinja
- name: Get all Global Credential V2
  cisco.dnac.global_credential_v2_info:
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

## [Return Values](global_credential_v2_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"cliCredential": [{"comments": "string", "credentialType": "string", "description": "string", "enablePassword": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "username": "string"}], "httpsRead": [{"comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": 0, "secure": true, "username": "string"}], "httpsWrite": [{"comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "password": "string", "port": 0, "secure": true, "username": "string"}], "snmpV2cRead": [{"comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "readCommunity": "string"}], "snmpV2cWrite": [{"comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "writeCommunity": "string"}], "snmpV3": [{"authPassword": "string", "authType": "string", "comments": "string", "credentialType": "string", "description": "string", "id": "string", "instanceTenantId": "string", "instanceUuid": "string", "privacyPassword": "string", "privacyType": "string", "snmpMode": "string", "username": "string"}]}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
