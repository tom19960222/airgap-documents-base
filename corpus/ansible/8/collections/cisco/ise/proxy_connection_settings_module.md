---
collection: ansible
version: "8"
title: "cisco.ise.proxy_connection_settings module – Resource module for Proxy Connection Settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/proxy_connection_settings_module.html
fetched_at: 2026-07-28T01:30:07+00:00
---
# cisco.ise.proxy_connection_settings module – Resource module for Proxy Connection Settings

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
> see [Requirements](proxy_connection_settings_module.md#ansible-collections-cisco-ise-proxy-connection-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.proxy_connection_settings`.

New in cisco.ise 2.1.0

- [Synopsis](proxy_connection_settings_module.md#synopsis)
- [Requirements](proxy_connection_settings_module.md#requirements)
- [Parameters](proxy_connection_settings_module.md#parameters)
- [Notes](proxy_connection_settings_module.md#notes)
- [See Also](proxy_connection_settings_module.md#see-also)
- [Examples](proxy_connection_settings_module.md#examples)
- [Return Values](proxy_connection_settings_module.md#return-values)

## [Synopsis](proxy_connection_settings_module.md#id1)

- Manage operation update of the resource Proxy Connection Settings.
- The following functionalities are impacted by the proxy settings.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](proxy_connection_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](proxy_connection_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bypassHosts**  string | Bypass hosts for the proxy connection. |
| **fqdn**  string | Proxy IP address or DNS-resolvable host name. |
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
| **password**  string | Password for the proxy connection. |
| **passwordRequired**  boolean | Indicates whether password configuration is required for Proxy.  **Choices:**   - `false` - `true` |
| **port**  integer | Port for proxy connection. Should be between 1 and 65535. |
| **userName**  string | User name for the proxy connection. |

## [Notes](proxy_connection_settings_module.md#id4)

> **Note:**
>
> - SDK Method used are proxy.Proxy.update_proxy_connection,
> - Paths used are put /api/v1/system-settings/proxy,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](proxy_connection_settings_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for proxy](https://developer.cisco.com/docs/identity-services-engine/v1/#!system-settings-openapi)
> :   Complete reference of the proxy API.

## [Examples](proxy_connection_settings_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.ise.proxy_connection_settings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    bypassHosts: string
    fqdn: string
    password: string
    passwordRequired: true
    port: 0
    userName: string
```

## [Return Values](proxy_connection_settings_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"bypassHosts": "string", "fqdn": "string", "password": "string", "passwordRequired": true, "port": 0, "userName": "string"}` |
| **ise_update_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"response": {"bypassHosts": "string", "fqdn": "string", "password": "string", "passwordRequired": true, "port": 0, "userName": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
