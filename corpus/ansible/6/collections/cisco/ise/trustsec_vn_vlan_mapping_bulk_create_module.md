---
collection: ansible
version: "6"
title: "cisco.ise.trustsec_vn_vlan_mapping_bulk_create module – Resource module for Trustsec VN VLAN Mapping Bulk Create"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/trustsec_vn_vlan_mapping_bulk_create_module.html
fetched_at: 2026-07-27T17:00:14+00:00
---
# cisco.ise.trustsec_vn_vlan_mapping_bulk_create module – Resource module for Trustsec VN VLAN Mapping Bulk Create

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
> see [Requirements](trustsec_vn_vlan_mapping_bulk_create_module.md#ansible-collections-cisco-ise-trustsec-vn-vlan-mapping-bulk-create-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.trustsec_vn_vlan_mapping_bulk_create`.

New in cisco.ise 2.0.0

- [Synopsis](trustsec_vn_vlan_mapping_bulk_create_module.md#synopsis)
- [Requirements](trustsec_vn_vlan_mapping_bulk_create_module.md#requirements)
- [Parameters](trustsec_vn_vlan_mapping_bulk_create_module.md#parameters)
- [Notes](trustsec_vn_vlan_mapping_bulk_create_module.md#notes)
- [See Also](trustsec_vn_vlan_mapping_bulk_create_module.md#see-also)
- [Examples](trustsec_vn_vlan_mapping_bulk_create_module.md#examples)
- [Return Values](trustsec_vn_vlan_mapping_bulk_create_module.md#return-values)

## [Synopsis](trustsec_vn_vlan_mapping_bulk_create_module.md#id1)

- Manage operation create of the resource Trustsec VN VLAN Mapping Bulk Create.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](trustsec_vn_vlan_mapping_bulk_create_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](trustsec_vn_vlan_mapping_bulk_create_module.md#id3)

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
| **payload**  list / elements=dictionary | Trustsec VN VLAN Mapping Bulk Create’s payload. |
| **id**  string | Identifier of the VN-VLAN Mapping. |
| **isData**  boolean | Flag which indicates whether the VLAN is data or voice type.  Choices:   - `false` - `true` |
| **isDefaultVLAN**  boolean | Flag which indicates if the VLAN is default.  Choices:   - `false` - `true` |
| **lastUpdate**  string | Timestamp for the last update of the VN-VLAN Mapping. |
| **maxValue**  integer | Max value. |
| **name**  string | Name of the VLAN. |
| **vnId**  string | Identifier for the associated Virtual Network which is required unless its name is provided. |
| **vnName**  string | Name of the associated Virtual Network to be used for identity if id is not provided. |

## [Notes](trustsec_vn_vlan_mapping_bulk_create_module.md#id4)

> **Note:**
>
> - SDK Method used are vn_vlan_mapping.VnVlanMapping.bulk_create_vn_vlan_mappings,
> - Paths used are post /api/v1/trustsec/vnvlanmapping/bulk/create,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](trustsec_vn_vlan_mapping_bulk_create_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for vnVlanMapping](https://developer.cisco.com/docs/identity-services-engine/v1/#!trustsec-openapi)
> :   Complete reference of the vnVlanMapping API.

## [Examples](trustsec_vn_vlan_mapping_bulk_create_module.md#id6)

```yaml+jinja
- name: Create
  cisco.ise.trustsec_vn_vlan_mapping_bulk_create:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    payload:
    - id: string
      isData: true
      isDefaultVlan: true
      lastUpdate: string
      maxValue: 0
      name: string
      vnId: string
      vnName: string
```

## [Return Values](trustsec_vn_vlan_mapping_bulk_create_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"id": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
