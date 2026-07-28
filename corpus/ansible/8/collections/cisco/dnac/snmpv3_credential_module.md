---
collection: ansible
version: "8"
title: "cisco.dnac.snmpv3_credential module – Resource module for Snmpv3 Credential"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/snmpv3_credential_module.html
fetched_at: 2026-07-28T01:25:09+00:00
---
# cisco.dnac.snmpv3_credential module – Resource module for Snmpv3 Credential

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
> see [Requirements](snmpv3_credential_module.md#ansible-collections-cisco-dnac-snmpv3-credential-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.snmpv3_credential`.

New in cisco.dnac 3.1.0

- [Synopsis](snmpv3_credential_module.md#synopsis)
- [Requirements](snmpv3_credential_module.md#requirements)
- [Parameters](snmpv3_credential_module.md#parameters)
- [Notes](snmpv3_credential_module.md#notes)
- [See Also](snmpv3_credential_module.md#see-also)
- [Examples](snmpv3_credential_module.md#examples)
- [Return Values](snmpv3_credential_module.md#return-values)

## [Synopsis](snmpv3_credential_module.md#id1)

- Manage operations create and update of the resource Snmpv3 Credential.
- Adds global SNMPv3 credentials.
- Updates global SNMPv3 credential.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](snmpv3_credential_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](snmpv3_credential_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authPassword**  string | Snmpv3 Credential’s authPassword. |
| **authType**  string | Snmpv3 Credential’s authType. |
| **comments**  string | Snmpv3 Credential’s comments. |
| **credentialType**  string | Snmpv3 Credential’s credentialType. |
| **description**  string | Snmpv3 Credential’s description. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **id**  string | Snmpv3 Credential’s id. |
| **instanceTenantId**  string | Snmpv3 Credential’s instanceTenantId. |
| **instanceUuid**  string | Snmpv3 Credential’s instanceUuid. |
| **privacyPassword**  string | Snmpv3 Credential’s privacyPassword. |
| **privacyType**  string | Snmpv3 Credential’s privacyType. |
| **snmpMode**  string | Snmpv3 Credential’s snmpMode. |
| **username**  string | Snmpv3 Credential’s username. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](snmpv3_credential_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.create_snmpv3_credentials, discovery.Discovery.update_snmpv3_credentials,
> - Paths used are post /dna/intent/api/v1/global-credential/snmpv3, put /dna/intent/api/v1/global-credential/snmpv3,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](snmpv3_credential_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery CreateSNMPv3Credentials](https://developer.cisco.com/docs/dna-center/#!create-snm-pv-3-credentials)
> :   Complete reference of the CreateSNMPv3Credentials API.
>
> [Cisco DNA Center documentation for Discovery UpdateSNMPv3Credentials](https://developer.cisco.com/docs/dna-center/#!update-snm-pv-3-credentials)
> :   Complete reference of the UpdateSNMPv3Credentials API.

## [Examples](snmpv3_credential_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.snmpv3_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    authPassword: string
    authType: string
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    privacyPassword: string
    privacyType: string
    snmpMode: string
    username: string

- name: Create
  cisco.dnac.snmpv3_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    authPassword: string
    authType: string
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    privacyPassword: string
    privacyType: string
    snmpMode: string
    username: string
```

## [Return Values](snmpv3_credential_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
