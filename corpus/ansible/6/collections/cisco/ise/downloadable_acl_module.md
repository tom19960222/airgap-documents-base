---
collection: ansible
version: "6"
title: "cisco.ise.downloadable_acl module – Resource module for Downloadable ACL"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/downloadable_acl_module.html
fetched_at: 2026-07-27T16:56:52+00:00
---
# cisco.ise.downloadable_acl module – Resource module for Downloadable ACL

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
> see [Requirements](downloadable_acl_module.md#ansible-collections-cisco-ise-downloadable-acl-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.downloadable_acl`.

New in cisco.ise 1.0.0

- [Synopsis](downloadable_acl_module.md#synopsis)
- [Requirements](downloadable_acl_module.md#requirements)
- [Parameters](downloadable_acl_module.md#parameters)
- [Notes](downloadable_acl_module.md#notes)
- [Examples](downloadable_acl_module.md#examples)
- [Return Values](downloadable_acl_module.md#return-values)

## [Synopsis](downloadable_acl_module.md#id1)

- Manage operations create, update and delete of the resource Downloadable ACL.
- This API creates a downloadable ACL.
- This API deletes a downloadable ACL.
- This API allows the client to update a downloadable ACL.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](downloadable_acl_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](downloadable_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dacl**  string | The DACL Content. Use the string \\n for a newline. |
| **daclType**  string | Allowed values - IPV4, - IPV6, - IP_AGNOSTIC. |
| **description**  string | Use the string \\n for a newline. |
| **id**  string | Downloadable ACL’s id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Resource Name. Name may contain alphanumeric or any of the following characters _.-. |

## [Notes](downloadable_acl_module.md#id4)

> **Note:**
>
> - SDK Method used are downloadable_acl.DownloadableAcl.create_downloadable_acl, downloadable_acl.DownloadableAcl.delete_downloadable_acl_by_id, downloadable_acl.DownloadableAcl.update_downloadable_acl_by_id,
> - Paths used are post /ers/config/downloadableacl, delete /ers/config/downloadableacl/{id}, put /ers/config/downloadableacl/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](downloadable_acl_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.downloadable_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    dacl: string
    daclType: string
    description: string
    id: string
    name: string

- name: Update by id with multiline ACL
  cisco.ise.downloadable_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    dacl: "permit udp any eq bootpc any eq bootps\n permit tcp any host {{ise-ip}} eq www"
    daclType: string
    description: "this is my\n multiline\n ACL."
    id: string
    name: string

- name: Delete by id
  cisco.ise.downloadable_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.downloadable_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    dacl: string
    daclType: string
    description: string
    name: string

- name: Create with multiline ACL
  cisco.ise.downloadable_acl:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    dacl: "permit udp any eq bootpc any eq bootps\n permit tcp any host {{ise-ip}} eq www"
    daclType: string
    description: "this is my\n multiline\n ACL."
    name: string
```

## [Return Values](downloadable_acl_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"dacl": "string", "daclType": "string", "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string"}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
