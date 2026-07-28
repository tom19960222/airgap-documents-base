---
collection: ansible
version: "6"
title: "cisco.ise.external_radius_server_info module – Information module for External RADIUS Server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/external_radius_server_info_module.html
fetched_at: 2026-07-27T16:57:06+00:00
---
# cisco.ise.external_radius_server_info module – Information module for External RADIUS Server

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
> see [Requirements](external_radius_server_info_module.md#ansible-collections-cisco-ise-external-radius-server-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.external_radius_server_info`.

New in cisco.ise 1.0.0

- [Synopsis](external_radius_server_info_module.md#synopsis)
- [Requirements](external_radius_server_info_module.md#requirements)
- [Parameters](external_radius_server_info_module.md#parameters)
- [Notes](external_radius_server_info_module.md#notes)
- [Examples](external_radius_server_info_module.md#examples)
- [Return Values](external_radius_server_info_module.md#return-values)

## [Synopsis](external_radius_server_info_module.md#id1)

- Get all External RADIUS Server.
- Get External RADIUS Server by id.
- Get External RADIUS Server by name.
- This API allows the client to get all the external RADIUS servers.
- This API allows the client to get an external RADIUS server by ID.
- This API allows the client to get an external RADIUS server by name.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](external_radius_server_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](external_radius_server_info_module.md#id3)

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

## [Notes](external_radius_server_info_module.md#id4)

> **Note:**
>
> - SDK Method used are external_radius_server.ExternalRadiusServer.get_external_radius_server_by_id, external_radius_server.ExternalRadiusServer.get_external_radius_server_by_name, external_radius_server.ExternalRadiusServer.get_external_radius_server_generator,
> - Paths used are get /ers/config/externalradiusserver, get /ers/config/externalradiusserver/name/{name}, get /ers/config/externalradiusserver/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](external_radius_server_info_module.md#id5)

```yaml+jinja
- name: Get all External RADIUS Server
  cisco.ise.external_radius_server_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
  register: result

- name: Get External RADIUS Server by id
  cisco.ise.external_radius_server_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get External RADIUS Server by name
  cisco.ise.external_radius_server_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result
```

## [Return Values](external_radius_server_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"accountingPort": 0, "authenticationPort": 0, "authenticatorKey": "string", "description": "string", "enableKeyWrap": true, "encryptionKey": "string", "hostIP": "string", "id": "string", "keyInputFormat": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "proxyTimeout": 0, "retries": 0, "sharedSecret": "string", "timeout": 0}` |
| **ise_responses**  list / elements=dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `"[\n  {\n    \"id\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"hostIP\": \"string\",\n    \"sharedSecret\": \"string\",\n    \"enableKeyWrap\": true,\n    \"encryptionKey\": \"string\",\n    \"authenticatorKey\": \"string\",\n    \"keyInputFormat\": \"string\",\n    \"authenticationPort\": 0,\n    \"accountingPort\": 0,\n    \"timeout\": 0,\n    \"retries\": 0,\n    \"proxyTimeout\": 0,\n    \"link\": {\n      \"rel\": \"string\",\n      \"href\": \"string\",\n      \"type\": \"string\"\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
