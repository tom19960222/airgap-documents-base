---
collection: ansible
version: "6"
title: "cisco.ise.trustsec_sg_vn_mapping_bulk_delete module – Resource module for Trustsec SG VN Mapping Bulk Delete"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/trustsec_sg_vn_mapping_bulk_delete_module.html
fetched_at: 2026-07-27T17:00:08+00:00
---
# cisco.ise.trustsec_sg_vn_mapping_bulk_delete module – Resource module for Trustsec SG VN Mapping Bulk Delete

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
> see [Requirements](trustsec_sg_vn_mapping_bulk_delete_module.md#ansible-collections-cisco-ise-trustsec-sg-vn-mapping-bulk-delete-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.trustsec_sg_vn_mapping_bulk_delete`.

New in cisco.ise 2.0.0

- [Synopsis](trustsec_sg_vn_mapping_bulk_delete_module.md#synopsis)
- [Requirements](trustsec_sg_vn_mapping_bulk_delete_module.md#requirements)
- [Parameters](trustsec_sg_vn_mapping_bulk_delete_module.md#parameters)
- [Notes](trustsec_sg_vn_mapping_bulk_delete_module.md#notes)
- [See Also](trustsec_sg_vn_mapping_bulk_delete_module.md#see-also)
- [Examples](trustsec_sg_vn_mapping_bulk_delete_module.md#examples)
- [Return Values](trustsec_sg_vn_mapping_bulk_delete_module.md#return-values)

## [Synopsis](trustsec_sg_vn_mapping_bulk_delete_module.md#id1)

- Manage operation create of the resource Trustsec SG VN Mapping Bulk Delete.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](trustsec_sg_vn_mapping_bulk_delete_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](trustsec_sg_vn_mapping_bulk_delete_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **payload**  list / elements=string | Trustsec SG VN Mapping Bulk Delete’s payload. |

## [Notes](trustsec_sg_vn_mapping_bulk_delete_module.md#id4)

> **Note:**
>
> - SDK Method used are sg_vn_mapping.SgVnMapping.bulk_delete_sg_vn_mappings,
> - Paths used are post /api/v1/trustsec/sgvnmapping/bulk/delete,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](trustsec_sg_vn_mapping_bulk_delete_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for sgVnMapping](https://developer.cisco.com/docs/identity-services-engine/v1/#!trustsec-openapi)
> :   Complete reference of the sgVnMapping API.

## [Examples](trustsec_sg_vn_mapping_bulk_delete_module.md#id6)

```yaml+jinja
- name: Create
  cisco.ise.trustsec_sg_vn_mapping_bulk_delete:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    payload:
    - string
```

## [Return Values](trustsec_sg_vn_mapping_bulk_delete_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"id": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
