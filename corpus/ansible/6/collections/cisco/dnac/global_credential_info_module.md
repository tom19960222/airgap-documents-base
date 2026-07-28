---
collection: ansible
version: "6"
title: "cisco.dnac.global_credential_info module – Information module for Global Credential"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/global_credential_info_module.html
fetched_at: 2026-07-27T16:52:12+00:00
---
# cisco.dnac.global_credential_info module – Information module for Global Credential

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
> see [Requirements](global_credential_info_module.md#ansible-collections-cisco-dnac-global-credential-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.global_credential_info`.

New in cisco.dnac 3.1.0

- [Synopsis](global_credential_info_module.md#synopsis)
- [Requirements](global_credential_info_module.md#requirements)
- [Parameters](global_credential_info_module.md#parameters)
- [Notes](global_credential_info_module.md#notes)
- [See Also](global_credential_info_module.md#see-also)
- [Examples](global_credential_info_module.md#examples)
- [Return Values](global_credential_info_module.md#return-values)

## [Synopsis](global_credential_info_module.md#id1)

- Get all Global Credential.
- Get Global Credential by id.
- Returns global credential for the given credential sub type.
- Returns the credential sub type for the given Id.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](global_credential_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](global_credential_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **credentialSubType**  string | CredentialSubType query parameter. Credential type as CLI / SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **headers**  dictionary | Additional headers. |
| **id**  string | Id path parameter. Global Credential ID. |
| **order**  string | Order query parameter. |
| **sortBy**  string | SortBy query parameter. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](global_credential_info_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.get_credential_sub_type_by_credential_id, discovery.Discovery.get_global_credentials,
> - Paths used are get /dna/intent/api/v1/global-credential, get /dna/intent/api/v1/global-credential/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](global_credential_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery GetCredentialSubTypeByCredentialId](https://developer.cisco.com/docs/dna-center/#!get-credential-sub-type-by-credential-id)
> :   Complete reference of the GetCredentialSubTypeByCredentialId API.
>
> [Cisco DNA Center documentation for Discovery GetGlobalCredentials](https://developer.cisco.com/docs/dna-center/#!get-global-credentials)
> :   Complete reference of the GetGlobalCredentials API.

## [Examples](global_credential_info_module.md#id6)

```yaml+jinja
- name: Get all Global Credential
  cisco.dnac.global_credential_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    credentialSubType: string
    sortBy: string
    order: string
  register: result

- name: Get Global Credential by id
  cisco.dnac.global_credential_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
```

## [Return Values](global_credential_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": "string", "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
