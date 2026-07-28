---
collection: ansible
version: "8"
title: "cisco.ise.px_grid_settings_auto_approve module – Resource module for Px Grid Settings Auto Approve"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/px_grid_settings_auto_approve_module.html
fetched_at: 2026-07-28T01:30:11+00:00
---
# cisco.ise.px_grid_settings_auto_approve module – Resource module for Px Grid Settings Auto Approve

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
> see [Requirements](px_grid_settings_auto_approve_module.md#ansible-collections-cisco-ise-px-grid-settings-auto-approve-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.px_grid_settings_auto_approve`.

New in cisco.ise 1.0.0

- [Synopsis](px_grid_settings_auto_approve_module.md#synopsis)
- [Requirements](px_grid_settings_auto_approve_module.md#requirements)
- [Parameters](px_grid_settings_auto_approve_module.md#parameters)
- [Notes](px_grid_settings_auto_approve_module.md#notes)
- [Examples](px_grid_settings_auto_approve_module.md#examples)
- [Return Values](px_grid_settings_auto_approve_module.md#return-values)

## [Synopsis](px_grid_settings_auto_approve_module.md#id1)

- Manage operation update of the resource Px Grid Settings Auto Approve.
- This API allows the client to auto approve the pxGrid settings.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](px_grid_settings_auto_approve_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](px_grid_settings_auto_approve_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowPasswordBasedAccounts**  boolean | Allow password based accounts when true.  **Choices:**   - `false` - `true` |
| **autoApproveCertBasedAccounts**  boolean | Auto approve certificate based accounts when true.  **Choices:**   - `false` - `true` |
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

## [Notes](px_grid_settings_auto_approve_module.md#id4)

> **Note:**
>
> - SDK Method used are px_grid_settings.PxGridSettings.autoapprove_px_grid_settings,
> - Paths used are put /ers/config/pxgridsettings/autoapprove,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](px_grid_settings_auto_approve_module.md#id5)

```yaml+jinja
- name: Update all
  cisco.ise.px_grid_settings_auto_approve:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    allowPasswordBasedAccounts: true
    autoApproveCertBasedAccounts: true
```

## [Return Values](px_grid_settings_auto_approve_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
