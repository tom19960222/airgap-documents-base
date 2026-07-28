---
collection: ansible
version: "8"
title: "cisco.ise.egress_matrix_cell module – Resource module for Egress Matrix Cell"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/egress_matrix_cell_module.html
fetched_at: 2026-07-28T01:28:12+00:00
---
# cisco.ise.egress_matrix_cell module – Resource module for Egress Matrix Cell

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
> see [Requirements](egress_matrix_cell_module.md#ansible-collections-cisco-ise-egress-matrix-cell-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.egress_matrix_cell`.

New in cisco.ise 1.0.0

- [Synopsis](egress_matrix_cell_module.md#synopsis)
- [Requirements](egress_matrix_cell_module.md#requirements)
- [Parameters](egress_matrix_cell_module.md#parameters)
- [Notes](egress_matrix_cell_module.md#notes)
- [Examples](egress_matrix_cell_module.md#examples)
- [Return Values](egress_matrix_cell_module.md#return-values)

## [Synopsis](egress_matrix_cell_module.md#id1)

- Manage operations create, update and delete of the resource Egress Matrix Cell.
- This API creates an egress matrix cell.
- This API deletes an egress matrix cell.
- This API allows the client to update an egress matrix cell.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](egress_matrix_cell_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](egress_matrix_cell_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **defaultRule**  string | Allowed values - NONE, - DENY_IP, - PERMIT_IP. |
| **description**  string | Egress Matrix Cell’s description. |
| **destinationSGtId**  string | Egress Matrix Cell’s destinationSGtId. |
| **id**  string | Egress Matrix Cell’s id. |
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
| **matrixCellStatus**  string | Allowed values - DISABLED, - ENABLED, - MONITOR. |
| **name**  string | Egress Matrix Cell’s name. |
| **sgacls**  list / elements=string | Egress Matrix Cell’s sgacls. |
| **sourceSGtId**  string | Egress Matrix Cell’s sourceSGtId. |

## [Notes](egress_matrix_cell_module.md#id4)

> **Note:**
>
> - SDK Method used are egress_matrix_cell.EgressMatrixCell.create_egress_matrix_cell, egress_matrix_cell.EgressMatrixCell.delete_egress_matrix_cell_by_id, egress_matrix_cell.EgressMatrixCell.update_egress_matrix_cell_by_id,
> - Paths used are post /ers/config/egressmatrixcell, delete /ers/config/egressmatrixcell/{id}, put /ers/config/egressmatrixcell/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](egress_matrix_cell_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultRule: string
    description: string
    destinationSgtId: string
    id: string
    matrixCellStatus: string
    name: string
    sgacls:
    - string
    sourceSgtId: string

- name: Delete by id
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.egress_matrix_cell:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    defaultRule: string
    description: string
    destinationSgtId: string
    matrixCellStatus: string
    name: string
    sgacls:
    - string
    sourceSgtId: string
```

## [Return Values](egress_matrix_cell_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"defaultRule": "string", "description": "string", "destinationSgtId": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "matrixCellStatus": "string", "name": "string", "sgacls": ["string"], "sourceSgtId": "string"}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
