---
collection: ansible
version: "8"
title: "cisco.dnac.authentication_policy_servers_info module – Information module for Authentication Policy Servers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/authentication_policy_servers_info_module.html
fetched_at: 2026-07-28T01:21:24+00:00
---
# cisco.dnac.authentication_policy_servers_info module – Information module for Authentication Policy Servers

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
> see [Requirements](authentication_policy_servers_info_module.md#ansible-collections-cisco-dnac-authentication-policy-servers-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.authentication_policy_servers_info`.

New in cisco.dnac 6.7.0

- [Synopsis](authentication_policy_servers_info_module.md#synopsis)
- [Requirements](authentication_policy_servers_info_module.md#requirements)
- [Parameters](authentication_policy_servers_info_module.md#parameters)
- [Notes](authentication_policy_servers_info_module.md#notes)
- [See Also](authentication_policy_servers_info_module.md#see-also)
- [Examples](authentication_policy_servers_info_module.md#examples)
- [Return Values](authentication_policy_servers_info_module.md#return-values)

## [Synopsis](authentication_policy_servers_info_module.md#id1)

- Get all Authentication Policy Servers.
- API to get Authentication and Policy Servers.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](authentication_policy_servers_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](authentication_policy_servers_info_module.md#id3)

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
| **isIseEnabled**  boolean | IsIseEnabled query parameter. Valid values are true, false.  **Choices:**   - `false` - `true` |
| **role**  string | Role query parameter. Authentication and Policy Server Role (Example primary, secondary). |
| **state_**  string | State query parameter. Valid values are INPROGRESS, ACTIVE, DELETED, RBAC-FAILURE, FAILED. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](authentication_policy_servers_info_module.md#id4)

> **Note:**
>
> - SDK Method used are system_settings.SystemSettings.get_authentication_and_policy_servers,
> - Paths used are get /dna/intent/api/v1/authentication-policy-servers,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](authentication_policy_servers_info_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for System Settings GetAuthenticationAndPolicyServers](https://developer.cisco.com/docs/dna-center/#!get-authentication-and-policy-servers)
> :   Complete reference of the GetAuthenticationAndPolicyServers API.

## [Examples](authentication_policy_servers_info_module.md#id6)

```yaml+jinja
- name: Get all Authentication Policy Servers
  cisco.dnac.authentication_policy_servers_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    isIseEnabled: True
    state_: string
    role: string
  register: result
```

## [Return Values](authentication_policy_servers_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"ipAddress\": \"string\",\n    \"sharedSecret\": \"string\",\n    \"protocol\": \"string\",\n    \"role\": \"string\",\n    \"port\": 0,\n    \"authenticationPort\": \"string\",\n    \"accountingPort\": \"string\",\n    \"retries\": 0,\n    \"timeoutSeconds\": 0,\n    \"isIseEnabled\": true,\n    \"instanceUuid\": \"string\",\n    \"state\": \"string\",\n    \"ciscoIseDtos\": [\n      {\n        \"subscriberName\": \"string\",\n        \"description\": \"string\",\n        \"password\": \"string\",\n        \"userName\": \"string\",\n        \"fqdn\": \"string\",\n        \"ipAddress\": \"string\",\n        \"trustState\": \"string\",\n        \"instanceUuid\": \"string\",\n        \"sshkey\": \"string\",\n        \"type\": \"string\",\n        \"failureReason\": \"string\",\n        \"role\": \"string\",\n        \"externalCiscoIseIpAddrDtos\": {\n          \"type\": \"string\",\n          \"externalCiscoIseIpAddresses\": [\n            {\n              \"externalIpAddress\": \"string\"\n            }\n          ]\n        }\n      }\n    ],\n    \"encryptionScheme\": \"string\",\n    \"messageKey\": \"string\",\n    \"encryptionKey\": \"string\",\n    \"useDnacCertForPxgrid\": true,\n    \"iseEnabled\": true,\n    \"pxgridEnabled\": true\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
