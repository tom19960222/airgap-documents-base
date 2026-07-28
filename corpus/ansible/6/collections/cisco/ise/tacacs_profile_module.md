---
collection: ansible
version: "6"
title: "cisco.ise.tacacs_profile module – Resource module for TACACS Profile"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/tacacs_profile_module.html
fetched_at: 2026-07-27T16:59:56+00:00
---
# cisco.ise.tacacs_profile module – Resource module for TACACS Profile

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
> see [Requirements](tacacs_profile_module.md#ansible-collections-cisco-ise-tacacs-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.tacacs_profile`.

New in cisco.ise 1.0.0

- [Synopsis](tacacs_profile_module.md#synopsis)
- [Requirements](tacacs_profile_module.md#requirements)
- [Parameters](tacacs_profile_module.md#parameters)
- [Notes](tacacs_profile_module.md#notes)
- [Examples](tacacs_profile_module.md#examples)
- [Return Values](tacacs_profile_module.md#return-values)

## [Synopsis](tacacs_profile_module.md#id1)

- Manage operations create, update and delete of the resource TACACS Profile.
- This API creates a TACACS profile.
- This API deletes a TACACS profile.
- This API allows the client to update a TACACS profile.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](tacacs_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](tacacs_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | TACACS Profile’s description. |
| **id**  string | TACACS Profile’s id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | TACACS Profile’s name. |
| **sessionAttributes**  dictionary | Holds list of session attributes. View type for GUI is Shell by default. |
| **sessionAttributeList**  list / elements=dictionary | TACACS Profile’s sessionAttributeList. |
| **name**  string | TACACS Profile’s name. |
| **type**  string | Allowed values MANDATORY, OPTIONAL. |
| **value**  string | TACACS Profile’s value. |

## [Notes](tacacs_profile_module.md#id4)

> **Note:**
>
> - SDK Method used are tacacs_profile.TacacsProfile.create_tacacs_profile, tacacs_profile.TacacsProfile.delete_tacacs_profile_by_id, tacacs_profile.TacacsProfile.update_tacacs_profile_by_id,
> - Paths used are post /ers/config/tacacsprofile, delete /ers/config/tacacsprofile/{id}, put /ers/config/tacacsprofile/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](tacacs_profile_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.tacacs_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    id: string
    name: string
    sessionAttributes:
      sessionAttributeList:
      - name: string
        type: string
        value: string

- name: Delete by id
  cisco.ise.tacacs_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.tacacs_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    name: string
    sessionAttributes:
      sessionAttributeList:
      - name: string
        type: string
        value: string
```

## [Return Values](tacacs_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "sessionAttributes": {"sessionAttributeList": [{"name": "string", "type": "string", "value": "string"}]}}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
