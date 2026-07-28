---
collection: ansible
version: "8"
title: "cisco.ise.external_radius_server module – Resource module for External RADIUS Server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/external_radius_server_module.html
fetched_at: 2026-07-28T01:28:25+00:00
---
# cisco.ise.external_radius_server module – Resource module for External RADIUS Server

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](external_radius_server_module.md#ansible-collections-cisco-ise-external-radius-server-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.external_radius_server`.

New in cisco.ise 1.0.0

- [Synopsis](external_radius_server_module.md#synopsis)
- [Requirements](external_radius_server_module.md#requirements)
- [Parameters](external_radius_server_module.md#parameters)
- [Notes](external_radius_server_module.md#notes)
- [Examples](external_radius_server_module.md#examples)
- [Return Values](external_radius_server_module.md#return-values)

## [Synopsis](external_radius_server_module.md#id1)

- Manage operations create, update and delete of the resource External RADIUS Server.
- This API creates an external RADIUS server.
- This API deletes an external RADIUS server.
- This API allows the client to update an external RADIUS server.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](external_radius_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](external_radius_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accountingPort**  integer | Valid Range 1 to 65535. |
| **authenticationPort**  integer | Valid Range 1 to 65535. |
| **authenticatorKey**  string | The authenticatorKey is required only if enableKeyWrap is true, otherwise it must be ignored or empty. The maximum length is 20 ASCII characters or 40 HEXADECIMAL characters (depend on selection in field ‘keyInputFormat’). |
| **description**  string | External RADIUS Server’s description. |
| **enableKeyWrap**  boolean | KeyWrap may only be enabled if it is supported on the device. When running in FIPS mode this option should be enabled for such devices.  **Choices:**   - `false` - `true` |
| **encryptionKey**  string | The encryptionKey is required only if enableKeyWrap is true, otherwise it must be ignored or empty. The maximum length is 16 ASCII characters or 32 HEXADECIMAL characters (depend on selection in field ‘keyInputFormat’). |
| **hostIP**  string | The IP of the host - must be a valid IPV4 address. |
| **id**  string | External RADIUS Server’s id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_single_request_timeout**  integer  *added in cisco.ise 3.0.0* | Timeout (in seconds) for RESTful HTTP requests.  **Default:** `60` |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  *added in cisco.ise 1.1.0* | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  **Choices:**   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  *added in cisco.ise 3.0.0* | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  **Choices:**   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  **Default:** `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  **Choices:**   - `false` - `true` ← (default) |
| **keyInputFormat**  string | Specifies the format of the input for fields ‘encryptionKey’ and ‘authenticatorKey’. Allowed Values - ASCII - HEXADECIMAL. |
| **name**  string | Resource Name. Allowed charactera are alphanumeric and _ (underscore). |
| **proxyTimeout**  integer | Valid Range 1 to 600. |
| **retries**  integer | Valid Range 1 to 9. |
| **sharedSecret**  string | Shared secret maximum length is 128 characters. |
| **timeout**  integer | Valid Range 1 to 120. |

## [Notes](external_radius_server_module.md#id4)

> **Note:**
>
> - SDK Method used are external_radius_server.ExternalRadiusServer.create_external_radius_server, external_radius_server.ExternalRadiusServer.delete_external_radius_server_by_id, external_radius_server.ExternalRadiusServer.update_external_radius_server_by_id,
> - Paths used are post /ers/config/externalradiusserver, delete /ers/config/externalradiusserver/{id}, put /ers/config/externalradiusserver/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](external_radius_server_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.external_radius_server:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accountingPort: 0
    authenticationPort: 0
    authenticatorKey: string
    description: string
    enableKeyWrap: true
    encryptionKey: string
    hostIP: string
    id: string
    keyInputFormat: string
    name: string
    proxyTimeout: 0
    retries: 0
    sharedSecret: string
    timeout: 0

- name: Delete by id
  cisco.ise.external_radius_server:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.external_radius_server:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accountingPort: 0
    authenticationPort: 0
    authenticatorKey: string
    description: string
    enableKeyWrap: true
    encryptionKey: string
    hostIP: string
    keyInputFormat: string
    name: string
    proxyTimeout: 0
    retries: 0
    sharedSecret: string
    timeout: 0
```

## [Return Values](external_radius_server_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"accountingPort": 0, "authenticationPort": 0, "authenticatorKey": "string", "description": "string", "enableKeyWrap": true, "encryptionKey": "string", "hostIP": "string", "id": "string", "keyInputFormat": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "proxyTimeout": 0, "retries": 0, "sharedSecret": "string", "timeout": 0}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
