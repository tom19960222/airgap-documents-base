---
collection: ansible
version: "8"
title: "cisco.ise.sxp_local_bindings module – Resource module for SXP Local Bindings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/sxp_local_bindings_module.html
fetched_at: 2026-07-28T01:31:16+00:00
---
# cisco.ise.sxp_local_bindings module – Resource module for SXP Local Bindings

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
> see [Requirements](sxp_local_bindings_module.md#ansible-collections-cisco-ise-sxp-local-bindings-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.sxp_local_bindings`.

New in cisco.ise 1.0.0

- [Synopsis](sxp_local_bindings_module.md#synopsis)
- [Requirements](sxp_local_bindings_module.md#requirements)
- [Parameters](sxp_local_bindings_module.md#parameters)
- [Notes](sxp_local_bindings_module.md#notes)
- [Examples](sxp_local_bindings_module.md#examples)
- [Return Values](sxp_local_bindings_module.md#return-values)

## [Synopsis](sxp_local_bindings_module.md#id1)

- Manage operations create, update and delete of the resource SXP Local Bindings.
- This API creates a SXP local binding.
- This API deletes a SXP local binding.
- This API allows the client to update a SXP local binding.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sxp_local_bindings_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](sxp_local_bindings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bindingName**  string | This field is depricated from Cisco ISE 3.0. |
| **description**  string | SXP Local Bindings’s description. |
| **id**  string | SXP Local Bindings’s id. |
| **ipAddressOrHost**  string | IP address for static mapping (hostname is not supported). |
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
| **sgt**  string | SGT name or ID. |
| **sxpVpn**  string | List of SXP Domains, separated with comma. At least one of sxpVpn or vns should be defined. |
| **vns**  string | List of Virtual Networks, separated with comma. At least one of sxpVpn or vns should be defined. |

## [Notes](sxp_local_bindings_module.md#id4)

> **Note:**
>
> - SDK Method used are sxp_local_bindings.SxpLocalBindings.create_sxp_local_bindings, sxp_local_bindings.SxpLocalBindings.delete_sxp_local_bindings_by_id, sxp_local_bindings.SxpLocalBindings.update_sxp_local_bindings_by_id,
> - Paths used are post /ers/config/sxplocalbindings, delete /ers/config/sxplocalbindings/{id}, put /ers/config/sxplocalbindings/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](sxp_local_bindings_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.sxp_local_bindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    bindingName: string
    description: string
    id: string
    ipAddressOrHost: string
    sgt: string
    sxpVpn: string
    vns: string

- name: Delete by id
  cisco.ise.sxp_local_bindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sxp_local_bindings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    bindingName: string
    description: string
    id: string
    ipAddressOrHost: string
    sgt: string
    sxpVpn: string
    vns: string
```

## [Return Values](sxp_local_bindings_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"bindingName": "string", "description": "string", "id": "string", "ipAddressOrHost": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "sgt": "string", "sxpVpn": "string", "vns": "string"}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
