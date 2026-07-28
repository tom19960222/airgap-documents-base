---
collection: ansible
version: "8"
title: "cisco.ise.sgt module – Resource module for SGt"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/sgt_module.html
fetched_at: 2026-07-28T01:30:59+00:00
---
# cisco.ise.sgt module – Resource module for SGt

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
> see [Requirements](sgt_module.md#ansible-collections-cisco-ise-sgt-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.sgt`.

New in cisco.ise 1.0.0

- [Synopsis](sgt_module.md#synopsis)
- [Requirements](sgt_module.md#requirements)
- [Parameters](sgt_module.md#parameters)
- [Notes](sgt_module.md#notes)
- [See Also](sgt_module.md#see-also)
- [Examples](sgt_module.md#examples)
- [Return Values](sgt_module.md#return-values)

## [Synopsis](sgt_module.md#id1)

- Manage operations create, update and delete of the resource SGt.
- This API creates a security group.
- This API deletes a security group.
- This API allows the client to update a security group.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sgt_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](sgt_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **defaultSGACLs**  list / elements=dictionary | SGt’s defaultSGACLs. |
| **description**  string | SGt’s description. |
| **generationId**  string | SGt’s generationId. |
| **id**  string | SGt’s id. |
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
| **isReadOnly**  boolean | IsReadOnly flag.  **Choices:**   - `false` - `true` |
| **name**  string / required | SGt’s name. |
| **propogateToApic**  boolean | PropogateToApic flag.  **Choices:**   - `false` - `true` |
| **value**  integer / required | Value range 2 ot 65519 or -1 to auto-generate. |

## [Notes](sgt_module.md#id4)

> **Note:**
>
> - SDK Method used are security_groups.SecurityGroups.create_security_group, security_groups.SecurityGroups.delete_security_group_by_id, security_groups.SecurityGroups.update_security_group_by_id,
> - Paths used are post /ers/config/sgt, delete /ers/config/sgt/{id}, put /ers/config/sgt/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](sgt_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for SecurityGroups](https://developer.cisco.com/docs/identity-services-engine/v1/#!sgt)
> :   Complete reference of the SecurityGroups API.

## [Examples](sgt_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultSGACLs:
    - {}
    description: string
    generationId: string
    id: string
    isReadOnly: true
    name: string
    propogateToApic: true
    value: 0

- name: Delete by id
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sgt:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultSGACLs:
    - {}
    description: string
    generationId: string
    isReadOnly: true
    name: string
    propogateToApic: true
    value: 0
```

## [Return Values](sgt_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"defaultSGACLs": [{}], "description": "string", "generationId": "string", "id": "string", "isReadOnly": true, "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "propogateToApic": true, "value": 0}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
