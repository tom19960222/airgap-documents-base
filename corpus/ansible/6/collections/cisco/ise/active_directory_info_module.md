---
collection: ansible
version: "6"
title: "cisco.ise.active_directory_info module – Information module for Active Directory"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/active_directory_info_module.html
fetched_at: 2026-07-27T16:56:05+00:00
---
# cisco.ise.active_directory_info module – Information module for Active Directory

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/cisco/ise) (version 2.5.9).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](active_directory_info_module.md#ansible-collections-cisco-ise-active-directory-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.active_directory_info`.

New in cisco.ise 1.0.0

- [Synopsis](active_directory_info_module.md#synopsis)
- [Requirements](active_directory_info_module.md#requirements)
- [Parameters](active_directory_info_module.md#parameters)
- [Notes](active_directory_info_module.md#notes)
- [Examples](active_directory_info_module.md#examples)
- [Return Values](active_directory_info_module.md#return-values)

## [Synopsis](active_directory_info_module.md#id1)

- Get all Active Directory.
- Get Active Directory by id.
- Get Active Directory by name.
- This API allows the client to get Active Directory by name.
- This API fetchs the join point details by ID. The ID can be retrieved with the.
- This API lists all the join points for Active Directory domains in Cisco ISE.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](active_directory_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](active_directory_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **id**  string | Id path parameter. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Name path parameter. |
| **page**  integer | Page query parameter. Page number. |
| **size**  integer | Size query parameter. Number of objects returned per page. |

## [Notes](active_directory_info_module.md#id4)

> **Note:**
>
> - SDK Method used are active_directory.ActiveDirectory.get_active_directory_by_id, active_directory.ActiveDirectory.get_active_directory_by_name, active_directory.ActiveDirectory.get_active_directory_generator,
> - Paths used are get /ers/config/activedirectory, get /ers/config/activedirectory/name/{name}, get /ers/config/activedirectory/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](active_directory_info_module.md#id5)

```yaml+jinja
- name: Get all Active Directory
  cisco.ise.active_directory_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get Active Directory by id
  cisco.ise.active_directory_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get Active Directory by name
  cisco.ise.active_directory_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result
```

## [Return Values](active_directory_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"adAttributes": {"attributes": [{"defaultValue": "string", "internalName": "string", "name": "string", "type": "string"}]}, "adScopesNames": "string", "adgroups": {"groups": [{"name": "string", "sid": "string", "type": "string"}]}, "advancedSettings": {"agingTime": 0, "authProtectionType": "string", "country": "string", "department": "string", "email": "string", "enableCallbackForDialinClient": true, "enableDialinPermissionCheck": true, "enableFailedAuthProtection": true, "enableMachineAccess": true, "enableMachineAuth": true, "enablePassChange": true, "enableRewrites": true, "failedAuthThreshold": 0, "firstName": "string", "identityNotInAdBehaviour": "string", "jobTitle": "string", "lastName": "string", "locality": "string", "organizationalUnit": "string", "plaintextAuth": true, "rewriteRules": [{"rewriteMatch": "string", "rewriteResult": "string", "rowId": 0}], "schema": "string", "stateOrProvince": "string", "streetAddress": "string", "telephone": "string", "unreachableDomainsBehaviour": "string"}, "description": "string", "domain": "string", "enableDomainAllowedList": true, "enableDomainWhiteList": true, "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string"}` |
| **ise_responses**  list / elements=dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `"[\n  {\n    \"id\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"domain\": \"string\",\n    \"enableDomainWhiteList\": true,\n    \"enableDomainAllowedList\": true,\n    \"adgroups\": {\n      \"groups\": [\n        {\n          \"name\": \"string\",\n          \"sid\": \"string\",\n          \"type\": \"string\"\n        }\n      ]\n    },\n    \"advancedSettings\": {\n      \"enablePassChange\": true,\n      \"enableMachineAuth\": true,\n      \"enableMachineAccess\": true,\n      \"agingTime\": 0,\n      \"enableDialinPermissionCheck\": true,\n      \"enableCallbackForDialinClient\": true,\n      \"plaintextAuth\": true,\n      \"enableFailedAuthProtection\": true,\n      \"authProtectionType\": \"string\",\n      \"failedAuthThreshold\": 0,\n      \"identityNotInAdBehaviour\": \"string\",\n      \"unreachableDomainsBehaviour\": \"string\",\n      \"enableRewrites\": true,\n      \"rewriteRules\": [\n        {\n          \"rowId\": 0,\n          \"rewriteMatch\": \"string\",\n          \"rewriteResult\": \"string\"\n        }\n      ],\n      \"firstName\": \"string\",\n      \"department\": \"string\",\n      \"lastName\": \"string\",\n      \"organizationalUnit\": \"string\",\n      \"jobTitle\": \"string\",\n      \"locality\": \"string\",\n      \"email\": \"string\",\n      \"stateOrProvince\": \"string\",\n      \"telephone\": \"string\",\n      \"country\": \"string\",\n      \"streetAddress\": \"string\",\n      \"schema\": \"string\"\n    },\n    \"adAttributes\": {\n      \"attributes\": [\n        {\n          \"name\": \"string\",\n          \"type\": \"string\",\n          \"internalName\": \"string\",\n          \"defaultValue\": \"string\"\n        }\n      ]\n    },\n    \"adScopesNames\": \"string\",\n    \"link\": {\n      \"rel\": \"string\",\n      \"href\": \"string\",\n      \"type\": \"string\"\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
