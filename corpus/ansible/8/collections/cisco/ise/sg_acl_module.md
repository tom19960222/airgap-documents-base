---
collection: ansible
version: "8"
title: "cisco.ise.sg_acl module – Resource module for SGACL"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/sg_acl_module.html
fetched_at: 2026-07-28T01:30:43+00:00
---
# cisco.ise.sg_acl module – Resource module for SGACL

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
> see [Requirements](sg_acl_module.md#ansible-collections-cisco-ise-sg-acl-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.sg_acl`.

New in cisco.ise 1.0.0

- [Synopsis](sg_acl_module.md#synopsis)
- [Requirements](sg_acl_module.md#requirements)
- [Parameters](sg_acl_module.md#parameters)
- [Notes](sg_acl_module.md#notes)
- [See Also](sg_acl_module.md#see-also)
- [Examples](sg_acl_module.md#examples)
- [Return Values](sg_acl_module.md#return-values)

## [Synopsis](sg_acl_module.md#id1)

- Manage operations create, update and delete of the resource SGACL.
- This API creates a security group ACL.
- This API deletes a security group ACL.
- This API allows the client to update a security group ACL.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sg_acl_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](sg_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aclcontent**  string | SGACL’s aclcontent. |
| **description**  string | SGACL’s description. |
| **generationId**  string | SGACL’s generationId. |
| **id**  string | SGACL’s id. |
| **ipVersion**  string | Allowed values - IPV4, - IPV6, - IP_AGNOSTIC. |
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
| **modelledContent**  dictionary | Modelled content of contract. |
| **name**  string | SGACL’s name. |

## [Notes](sg_acl_module.md#id4)

> **Note:**
>
> - SDK Method used are security_groups_acls.SecurityGroupsAcls.create_security_groups_acl, security_groups_acls.SecurityGroupsAcls.delete_security_groups_acl_by_id, security_groups_acls.SecurityGroupsAcls.update_security_groups_acl_by_id,
> - Paths used are post /ers/config/sgacl, delete /ers/config/sgacl/{id}, put /ers/config/sgacl/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](sg_acl_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for SecurityGroupsACLs](https://developer.cisco.com/docs/identity-services-engine/v1/#!sgacl)
> :   Complete reference of the SecurityGroupsACLs API.

## [Examples](sg_acl_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.ise.sg_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aclcontent: string
    description: string
    generationId: string
    id: string
    ipVersion: string
    isReadOnly: true
    modelledContent: {}
    name: string

- name: Delete by id
  cisco.ise.sg_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sg_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aclcontent: string
    description: string
    generationId: string
    ipVersion: string
    isReadOnly: true
    modelledContent: {}
    name: string
```

## [Return Values](sg_acl_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"aclcontent": "string", "description": "string", "generationId": "string", "id": "string", "ipVersion": "string", "isReadOnly": true, "link": {"href": "string", "rel": "string", "type": "string"}, "modelledContent": {}, "name": "string"}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
