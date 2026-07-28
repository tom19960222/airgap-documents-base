---
collection: ansible
version: "8"
title: "cisco.dnac.global_credential_v2 module – Resource module for Global Credential V2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/global_credential_v2_module.html
fetched_at: 2026-07-28T01:22:47+00:00
---
# cisco.dnac.global_credential_v2 module – Resource module for Global Credential V2

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
> see [Requirements](global_credential_v2_module.md#ansible-collections-cisco-dnac-global-credential-v2-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.global_credential_v2`.

New in cisco.dnac 6.7.0

- [Synopsis](global_credential_v2_module.md#synopsis)
- [Requirements](global_credential_v2_module.md#requirements)
- [Parameters](global_credential_v2_module.md#parameters)
- [Notes](global_credential_v2_module.md#notes)
- [See Also](global_credential_v2_module.md#see-also)
- [Examples](global_credential_v2_module.md#examples)
- [Return Values](global_credential_v2_module.md#return-values)

## [Synopsis](global_credential_v2_module.md#id1)

- Manage operations create, update and delete of the resource Global Credential V2.
- API to create new global credentials. Multiple credentials of various types can be passed at once. Please refer sample Request Body for more information.
- Delete a global credential. Only ‘id’ of the credential has to be passed.
- API to update device credentials. Multiple credentials can be passed at once, but only a single credential of a given type can be passed at once. Please refer sample Request Body for more information.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](global_credential_v2_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](global_credential_v2_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cliCredential**  dictionary | Global Credential V2’s cliCredential. |
| **description**  string | Description. |
| **enablePassword**  string | Enable Password. |
| **id**  string | Id. |
| **password**  string | Password. |
| **username**  string | Username. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **httpsRead**  dictionary | Global Credential V2’s httpsRead. |
| **id**  string | Id. |
| **name**  string | Name. |
| **password**  string | Password. |
| **port**  integer | Port. |
| **username**  string | Username. |
| **httpsWrite**  dictionary | Global Credential V2’s httpsWrite. |
| **id**  string | Id. |
| **name**  string | Name. |
| **password**  string | Password. |
| **port**  integer | Port. |
| **username**  string | Username. |
| **id**  string | Id path parameter. Global Credential id. |
| **snmpV2cRead**  dictionary | Global Credential V2’s snmpV2cRead. |
| **description**  string | Description. |
| **id**  string | Id. |
| **readCommunity**  string | Read Community. |
| **snmpV2cWrite**  dictionary | Global Credential V2’s snmpV2cWrite. |
| **description**  string | Description. |
| **id**  string | Id. |
| **writeCommunity**  string | Write Community. |
| **snmpV3**  dictionary | Global Credential V2’s snmpV3. |
| **authPassword**  string | Auth Password. |
| **authType**  string | Auth Type. |
| **description**  string | Description. |
| **id**  string | Id. |
| **privacyPassword**  string | Privacy Password. |
| **privacyType**  string | Privacy Type. |
| **snmpMode**  string | Snmp Mode. |
| **username**  string | Username. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](global_credential_v2_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.create_global_credentials_v2, discovery.Discovery.delete_global_credential_v2, discovery.Discovery.update_global_credentials_v2,
> - Paths used are post /dna/intent/api/v2/global-credential, delete /dna/intent/api/v2/global-credential/{id}, put /dna/intent/api/v2/global-credential,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](global_credential_v2_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery CreateGlobalCredentialsV2](https://developer.cisco.com/docs/dna-center/#!create-global-credentials-v-2)
> :   Complete reference of the CreateGlobalCredentialsV2 API.
>
> [Cisco DNA Center documentation for Discovery DeleteGlobalCredentialV2](https://developer.cisco.com/docs/dna-center/#!delete-global-credential-v-2)
> :   Complete reference of the DeleteGlobalCredentialV2 API.
>
> [Cisco DNA Center documentation for Discovery UpdateGlobalCredentialsV2](https://developer.cisco.com/docs/dna-center/#!update-global-credentials-v-2)
> :   Complete reference of the UpdateGlobalCredentialsV2 API.

## [Examples](global_credential_v2_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.global_credential_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cliCredential:
      description: string
      enablePassword: string
      id: string
      password: string
      username: string
    httpsRead:
      id: string
      name: string
      password: string
      port: 0
      username: string
    httpsWrite:
      id: string
      name: string
      password: string
      port: 0
      username: string
    snmpV2cRead:
      description: string
      id: string
      readCommunity: string
    snmpV2cWrite:
      description: string
      id: string
      writeCommunity: string
    snmpV3:
      authPassword: string
      authType: string
      description: string
      id: string
      privacyPassword: string
      privacyType: string
      snmpMode: string
      username: string

- name: Create
  cisco.dnac.global_credential_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    cliCredential:
    - description: string
      enablePassword: string
      password: string
      username: string
    httpsRead:
    - name: string
      password: string
      port: 0
      username: string
    httpsWrite:
    - name: string
      password: string
      port: 0
      username: string
    snmpV2cRead:
    - description: string
      readCommunity: string
    snmpV2cWrite:
    - description: string
      writeCommunity: string
    snmpV3:
    - authPassword: string
      authType: string
      description: string
      privacyPassword: string
      privacyType: string
      snmpMode: string
      username: string

- name: Delete by id
  cisco.dnac.global_credential_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string
```

## [Return Values](global_credential_v2_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
