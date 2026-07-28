---
collection: ansible
version: "6"
title: "cisco.dnac.cli_credential module – Resource module for Cli Credential"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/cli_credential_module.html
fetched_at: 2026-07-27T16:51:06+00:00
---
# cisco.dnac.cli_credential module – Resource module for Cli Credential

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
> see [Requirements](cli_credential_module.md#ansible-collections-cisco-dnac-cli-credential-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.cli_credential`.

New in cisco.dnac 3.1.0

- [Synopsis](cli_credential_module.md#synopsis)
- [Requirements](cli_credential_module.md#requirements)
- [Parameters](cli_credential_module.md#parameters)
- [Notes](cli_credential_module.md#notes)
- [See Also](cli_credential_module.md#see-also)
- [Examples](cli_credential_module.md#examples)
- [Return Values](cli_credential_module.md#return-values)

## [Synopsis](cli_credential_module.md#id1)

- Manage operations create and update of the resource Cli Credential.
- Adds global CLI credential.
- Updates global CLI credentials.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](cli_credential_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](cli_credential_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **comments**  string | Cli Credential’s comments. |
| **credentialType**  string | Cli Credential’s credentialType. |
| **description**  string | Cli Credential’s description. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **enablePassword**  string | Cli Credential’s enablePassword. |
| **id**  string | Cli Credential’s id. |
| **instanceTenantId**  string | Cli Credential’s instanceTenantId. |
| **instanceUuid**  string | Cli Credential’s instanceUuid. |
| **password**  string | Cli Credential’s password. |
| **username**  string | Cli Credential’s username. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](cli_credential_module.md#id4)

> **Note:**
>
> - SDK Method used are discovery.Discovery.create_cli_credentials, discovery.Discovery.update_cli_credentials,
> - Paths used are post /dna/intent/api/v1/global-credential/cli, put /dna/intent/api/v1/global-credential/cli,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](cli_credential_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Discovery CreateCLICredentials](https://developer.cisco.com/docs/dna-center/#!create-cli-credentials)
> :   Complete reference of the CreateCLICredentials API.
>
> [Cisco DNA Center documentation for Discovery UpdateCLICredentials](https://developer.cisco.com/docs/dna-center/#!update-cli-credentials)
> :   Complete reference of the UpdateCLICredentials API.

## [Examples](cli_credential_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.dnac.cli_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    enablePassword: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    password: string
    username: string

- name: Create
  cisco.dnac.cli_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    enablePassword: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    password: string
    username: string
```

## [Return Values](cli_credential_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
