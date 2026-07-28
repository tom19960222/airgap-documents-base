---
collection: ansible
version: "8"
title: "cisco.ise.radius_server_sequence module – Resource module for RADIUS Server Sequence"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/radius_server_sequence_module.html
fetched_at: 2026-07-28T01:30:34+00:00
---
# cisco.ise.radius_server_sequence module – Resource module for RADIUS Server Sequence

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
> see [Requirements](radius_server_sequence_module.md#ansible-collections-cisco-ise-radius-server-sequence-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.radius_server_sequence`.

New in cisco.ise 1.0.0

- [Synopsis](radius_server_sequence_module.md#synopsis)
- [Requirements](radius_server_sequence_module.md#requirements)
- [Parameters](radius_server_sequence_module.md#parameters)
- [Notes](radius_server_sequence_module.md#notes)
- [Examples](radius_server_sequence_module.md#examples)
- [Return Values](radius_server_sequence_module.md#return-values)

## [Synopsis](radius_server_sequence_module.md#id1)

- Manage operations create, update and delete of the resource RADIUS Server Sequence.
- This API creates a RADIUS server sequence.
- This API deletes a RADIUS server sequence.
- This API allows the client to update a RADIUS server sequence.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](radius_server_sequence_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](radius_server_sequence_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **BeforeAcceptAttrManipulatorsList**  list / elements=dictionary | The beforeAcceptAttrManipulators is required only if useAttrSetBeforeAcc is true. |
| **action**  string | Allowed Values - ADD, - UPDATE, - REMOVE, - REMOVEANY. |
| **attributeName**  string | RADIUS Server Sequence’s attributeName. |
| **changedVal**  string | The changedVal is required only if the action equals to ‘UPDATE’. |
| **dictionaryName**  string | RADIUS Server Sequence’s dictionaryName. |
| **value**  string | RADIUS Server Sequence’s value. |
| **continueAuthorzPolicy**  boolean | ContinueAuthorzPolicy flag.  **Choices:**   - `false` - `true` |
| **description**  string | RADIUS Server Sequence’s description. |
| **id**  string | RADIUS Server Sequence’s id. |
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
| **localAccounting**  boolean | LocalAccounting flag.  **Choices:**   - `false` - `true` |
| **name**  string | RADIUS Server Sequence’s name. |
| **OnRequestAttrManipulatorList**  list / elements=dictionary | The onRequestAttrManipulators is required only if useAttrSetOnRequest is true. |
| **action**  string | Allowed Values - ADD, - UPDATE, - REMOVE, - REMOVEANY. |
| **attributeName**  string | RADIUS Server Sequence’s attributeName. |
| **changedVal**  string | The changedVal is required only if the action equals to ‘UPDATE’. |
| **dictionaryName**  string | RADIUS Server Sequence’s dictionaryName. |
| **value**  string | RADIUS Server Sequence’s value. |
| **prefixSeparator**  string | The prefixSeparator is required only if stripPrefix is true. The maximum length is 1 character. |
| **RADIUSServerList**  list / elements=string | RADIUS Server Sequence’s RADIUSServerList. |
| **remoteAccounting**  boolean | RemoteAccounting flag.  **Choices:**   - `false` - `true` |
| **stripPrefix**  boolean | StripPrefix flag.  **Choices:**   - `false` - `true` |
| **stripSuffix**  boolean | StripSuffix flag.  **Choices:**   - `false` - `true` |
| **suffixSeparator**  string | The suffixSeparator is required only if stripSuffix is true. The maximum length is 1 character. |
| **useAttrSetBeforeAcc**  boolean | UseAttrSetBeforeAcc flag.  **Choices:**   - `false` - `true` |
| **useAttrSetOnRequest**  boolean | UseAttrSetOnRequest flag.  **Choices:**   - `false` - `true` |

## [Notes](radius_server_sequence_module.md#id4)

> **Note:**
>
> - SDK Method used are radius_server_sequence.RadiusServerSequence.create_radius_server_sequence, radius_server_sequence.RadiusServerSequence.delete_radius_server_sequence_by_id, radius_server_sequence.RadiusServerSequence.update_radius_server_sequence_by_id,
> - Paths used are post /ers/config/radiusserversequence, delete /ers/config/radiusserversequence/{id}, put /ers/config/radiusserversequence/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](radius_server_sequence_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.radius_server_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    BeforeAcceptAttrManipulatorsList:
    - action: string
      attributeName: string
      changedVal: string
      dictionaryName: string
      value: string
    OnRequestAttrManipulatorList:
    - action: string
      attributeName: string
      changedVal: string
      dictionaryName: string
      value: string
    RadiusServerList:
    - string
    continueAuthorzPolicy: true
    description: string
    id: string
    localAccounting: true
    name: string
    prefixSeparator: string
    remoteAccounting: true
    stripPrefix: true
    stripSuffix: true
    suffixSeparator: string
    useAttrSetBeforeAcc: true
    useAttrSetOnRequest: true

- name: Delete by id
  cisco.ise.radius_server_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.radius_server_sequence:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    BeforeAcceptAttrManipulatorsList:
    - action: string
      attributeName: string
      changedVal: string
      dictionaryName: string
      value: string
    OnRequestAttrManipulatorList:
    - action: string
      attributeName: string
      changedVal: string
      dictionaryName: string
      value: string
    RadiusServerList:
    - string
    continueAuthorzPolicy: true
    description: string
    localAccounting: true
    name: string
    prefixSeparator: string
    remoteAccounting: true
    stripPrefix: true
    stripSuffix: true
    suffixSeparator: string
    useAttrSetBeforeAcc: true
    useAttrSetOnRequest: true
```

## [Return Values](radius_server_sequence_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"BeforeAcceptAttrManipulatorsList": [{"action": "string", "attributeName": "string", "changedVal": "string", "dictionaryName": "string", "value": "string"}], "OnRequestAttrManipulatorList": [{"action": "string", "attributeName": "string", "changedVal": "string", "dictionaryName": "string", "value": "string"}], "RadiusServerList": ["string"], "continueAuthorzPolicy": true, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "localAccounting": true, "name": "string", "prefixSeparator": "string", "remoteAccounting": true, "stripPrefix": true, "stripSuffix": true, "suffixSeparator": "string", "useAttrSetBeforeAcc": true, "useAttrSetOnRequest": true}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
