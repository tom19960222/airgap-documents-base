---
collection: ansible
version: "6"
title: "cisco.ise.native_supplicant_profile module – Resource module for Native Supplicant Profile"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/native_supplicant_profile_module.html
fetched_at: 2026-07-27T16:57:50+00:00
---
# cisco.ise.native_supplicant_profile module – Resource module for Native Supplicant Profile

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
> see [Requirements](native_supplicant_profile_module.md#ansible-collections-cisco-ise-native-supplicant-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.native_supplicant_profile`.

New in cisco.ise 1.0.0

- [Synopsis](native_supplicant_profile_module.md#synopsis)
- [Requirements](native_supplicant_profile_module.md#requirements)
- [Parameters](native_supplicant_profile_module.md#parameters)
- [Notes](native_supplicant_profile_module.md#notes)
- [See Also](native_supplicant_profile_module.md#see-also)
- [Examples](native_supplicant_profile_module.md#examples)
- [Return Values](native_supplicant_profile_module.md#return-values)

## [Synopsis](native_supplicant_profile_module.md#id1)

- Manage operations update and delete of the resource Native Supplicant Profile.
- This API deletes a native supplicant profile.
- This API allows the client to update a native supplicant profile.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](native_supplicant_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](native_supplicant_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Native Supplicant Profile’s description. |
| **id**  string | Native Supplicant Profile’s id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Native Supplicant Profile’s name. |
| **wirelessProfiles**  list / elements=dictionary | Native Supplicant Profile’s wirelessProfiles. |
| **actionType**  string | Action type for WifiProfile. Allowed values - ADD, - UPDATE, - DELETE (required for updating existing WirelessProfile). |
| **allowedProtocol**  string | Native Supplicant Profile’s allowedProtocol. |
| **certificateTemplateId**  string | Native Supplicant Profile’s certificateTemplateId. |
| **previousSSID**  string | Previous ssid for WifiProfile (required for updating existing WirelessProfile). |
| **ssid**  string | Native Supplicant Profile’s ssid. |

## [Notes](native_supplicant_profile_module.md#id4)

> **Note:**
>
> - SDK Method used are native_supplicant_profile.NativeSupplicantProfile.delete_native_supplicant_profile_by_id, native_supplicant_profile.NativeSupplicantProfile.update_native_supplicant_profile_by_id,
> - Paths used are delete /ers/config/nspprofile/{id}, put /ers/config/nspprofile/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](native_supplicant_profile_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for NativeSupplicantProfile](https://developer.cisco.com/docs/identity-services-engine/v1/#!nspprofile)
> :   Complete reference of the NativeSupplicantProfile API.

## [Examples](native_supplicant_profile_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.ise.native_supplicant_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    description: string
    id: string
    name: string
    wirelessProfiles:
    - actionType: string
      allowedProtocol: string
      certificateTemplateId: string
      previousSsid: string
      ssid: string

- name: Delete by id
  cisco.ise.native_supplicant_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
```

## [Return Values](native_supplicant_profile_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "wirelessProfiles": [{"actionType": "string", "allowedProtocol": "string", "certificateTemplateId": "string", "previousSsid": "string", "ssid": "string"}]}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
