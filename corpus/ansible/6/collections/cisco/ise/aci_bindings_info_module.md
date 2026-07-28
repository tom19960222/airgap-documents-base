---
collection: ansible
version: "6"
title: "cisco.ise.aci_bindings_info module – Information module for ACI Bindings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/aci_bindings_info_module.html
fetched_at: 2026-07-27T16:56:00+00:00
---
# cisco.ise.aci_bindings_info module – Information module for ACI Bindings

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
> see [Requirements](aci_bindings_info_module.md#ansible-collections-cisco-ise-aci-bindings-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.aci_bindings_info`.

New in cisco.ise 1.0.0

- [Synopsis](aci_bindings_info_module.md#synopsis)
- [Requirements](aci_bindings_info_module.md#requirements)
- [Parameters](aci_bindings_info_module.md#parameters)
- [Notes](aci_bindings_info_module.md#notes)
- [Examples](aci_bindings_info_module.md#examples)
- [Return Values](aci_bindings_info_module.md#return-values)

## [Synopsis](aci_bindings_info_module.md#id1)

- Get all ACI Bindings.
- This API allows clients to retrieve all the bindings that were sent to Cisco.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](aci_bindings_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](aci_bindings_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **filterBy**  list / elements=string | FilterBy query parameter. |
| **filterValue**  list / elements=string | FilterValue query parameter. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **page**  integer | Page query parameter. Page number. |
| **size**  integer | Size query parameter. Number of objects returned per page. |
| **sort**  string | Sort query parameter. Sort type - asc or desc. |
| **sortBy**  string | SortBy query parameter. Sort column by which objects needs to be sorted. |

## [Notes](aci_bindings_info_module.md#id4)

> **Note:**
>
> - SDK Method used are aci_bindings.AciBindings.get_aci_bindings_generator,
> - Paths used are get /ers/config/acibindings/getall,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](aci_bindings_info_module.md#id5)

```yaml+jinja
- name: Get all ACI Bindings
  cisco.ise.aci_bindings_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
    sort: asc
    sortBy: string
    filterBy: []
    filterValue: []
  register: result
```

## [Return Values](aci_bindings_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"description": "string", "id": "string", "ip": "string", "learnedBy": "string", "learnedFrom": "string", "name": "string", "psn": "string", "sgtValue": "string", "vn": "string"}` |
| **ise_responses**  list / elements=dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `"[\n  {\n    \"id\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"ip\": \"string\",\n    \"sgtValue\": \"string\",\n    \"vn\": \"string\",\n    \"psn\": \"string\",\n    \"learnedFrom\": \"string\",\n    \"learnedBy\": \"string\"\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
