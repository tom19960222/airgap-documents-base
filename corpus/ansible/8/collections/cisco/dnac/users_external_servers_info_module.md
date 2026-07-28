---
collection: ansible
version: "8"
title: "cisco.dnac.users_external_servers_info module – Information module for Users External Servers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/users_external_servers_info_module.html
fetched_at: 2026-07-28T01:25:41+00:00
---
# cisco.dnac.users_external_servers_info module – Information module for Users External Servers

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
> see [Requirements](users_external_servers_info_module.md#ansible-collections-cisco-dnac-users-external-servers-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.users_external_servers_info`.

New in cisco.dnac 6.7.0

- [Synopsis](users_external_servers_info_module.md#synopsis)
- [Requirements](users_external_servers_info_module.md#requirements)
- [Parameters](users_external_servers_info_module.md#parameters)
- [Notes](users_external_servers_info_module.md#notes)
- [See Also](users_external_servers_info_module.md#see-also)
- [Examples](users_external_servers_info_module.md#examples)
- [Return Values](users_external_servers_info_module.md#return-values)

## [Synopsis](users_external_servers_info_module.md#id1)

- Get all Users External Servers.
- Get external users authentication servers.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](users_external_servers_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](users_external_servers_info_module.md#id3)

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
| **invokeSource**  string | InvokeSource query parameter. The source that invokes this API. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](users_external_servers_info_module.md#id4)

> **Note:**
>
> - SDK Method used are user_and_roles.UserandRoles.get_external_authentication_servers_ap_i,
> - Paths used are get /dna/system/api/v1/users/external-servers,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](users_external_servers_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for User and Roles GetExternalAuthenticationServersAPI](https://developer.cisco.com/docs/dna-center/#!get-external-authentication-servers-api)
> :   Complete reference of the GetExternalAuthenticationServersAPI API.

## [Examples](users_external_servers_info_module.md#id6)

```yaml+jinja
- name: Get all Users External Servers
  cisco.dnac.users_external_servers_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    invokeSource: string
  register: result
```

## [Return Values](users_external_servers_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"aaa-servers": [{"aaaAttribute": "string", "accountingPort": 0, "authenticationPort": 0, "protocol": "string", "retries": 0, "role": "string", "serverId": "string", "serverIp": "string", "sharedSecret": "string", "socketTimeout": 0}]}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
