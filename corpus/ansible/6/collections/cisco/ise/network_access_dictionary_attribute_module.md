---
collection: ansible
version: "6"
title: "cisco.ise.network_access_dictionary_attribute module – Resource module for Network Access Dictionary Attribute"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/network_access_dictionary_attribute_module.html
fetched_at: 2026-07-27T16:58:00+00:00
---
# cisco.ise.network_access_dictionary_attribute module – Resource module for Network Access Dictionary Attribute

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
> see [Requirements](network_access_dictionary_attribute_module.md#ansible-collections-cisco-ise-network-access-dictionary-attribute-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.network_access_dictionary_attribute`.

New in cisco.ise 1.0.0

- [Synopsis](network_access_dictionary_attribute_module.md#synopsis)
- [Requirements](network_access_dictionary_attribute_module.md#requirements)
- [Parameters](network_access_dictionary_attribute_module.md#parameters)
- [Notes](network_access_dictionary_attribute_module.md#notes)
- [See Also](network_access_dictionary_attribute_module.md#see-also)
- [Examples](network_access_dictionary_attribute_module.md#examples)
- [Return Values](network_access_dictionary_attribute_module.md#return-values)

## [Synopsis](network_access_dictionary_attribute_module.md#id1)

- Manage operations create, update and delete of the resource Network Access Dictionary Attribute.
- Create a new Dictionary Attribute for an existing Dictionary.
- Delete a Dictionary Attribute.
- Update a Dictionary Attribute.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](network_access_dictionary_attribute_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](network_access_dictionary_attribute_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allowedValues**  list / elements=dictionary | All of the allowed values for the dictionary attribute. |
| **isDefault**  boolean | True if this key value is the default between the allowed values of the dictionary attribute.  Choices:   - `false` - `true` |
| **key**  string | Network Access Dictionary Attribute’s key. |
| **value**  string | Network Access Dictionary Attribute’s value. |
| **dataType**  string | The data type for the dictionary attribute. |
| **description**  string | The description of the Dictionary attribute. |
| **dictionaryName**  string | The name of the dictionary which the dictionary attribute belongs to. |
| **directionType**  string | The direction for the useage of the dictionary attribute. |
| **id**  string | Identifier for the dictionary attribute. |
| **internalName**  string | The internal name of the dictionary attribute. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | The dictionary attribute’s name. |

## [Notes](network_access_dictionary_attribute_module.md#id4)

> **Note:**
>
> - SDK Method used are network_access_dictionary_attribute.NetworkAccessDictionaryAttribute.create_network_access_dictionary_attribute, network_access_dictionary_attribute.NetworkAccessDictionaryAttribute.delete_network_access_dictionary_attribute_by_name, network_access_dictionary_attribute.NetworkAccessDictionaryAttribute.update_network_access_dictionary_attribute_by_name,
> - Paths used are post /network-access/dictionaries/{dictionaryName}/attribute, delete /network-access/dictionaries/{dictionaryName}/attribute/{name}, put /network-access/dictionaries/{dictionaryName}/attribute/{name},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](network_access_dictionary_attribute_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Network Access - Dictionary Attribute](https://developer.cisco.com/docs/identity-services-engine/v1/#!policy-openapi)
> :   Complete reference of the Network Access - Dictionary Attribute API.

## [Examples](network_access_dictionary_attribute_module.md#id6)

```yaml+jinja
- name: Create
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedValues:
    - isDefault: true
      key: string
      value: string
    dataType: string
    description: string
    dictionaryName: string
    directionType: string
    id: string
    internalName: string
    name: string

- name: Update by name
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    allowedValues:
    - isDefault: true
      key: string
      value: string
    dataType: string
    description: string
    dictionaryName: string
    directionType: string
    id: string
    internalName: string
    name: string

- name: Delete by name
  cisco.ise.network_access_dictionary_attribute:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    dictionaryName: string
    name: string
```

## [Return Values](network_access_dictionary_attribute_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"allowedValues": [{"isDefault": true, "key": "string", "value": "string"}], "dataType": "string", "description": "string", "dictionaryName": "string", "directionType": "string", "id": "string", "internalName": "string", "name": "string"}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"response": {"allowedValues": [{"isDefault": true, "key": "string", "value": "string"}], "dataType": "string", "description": "string", "dictionaryName": "string", "directionType": "string", "id": "string", "internalName": "string", "name": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
