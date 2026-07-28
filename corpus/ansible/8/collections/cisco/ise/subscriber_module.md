---
collection: ansible
version: "8"
title: "cisco.ise.subscriber module – Resource module for Subscriber"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/subscriber_module.html
fetched_at: 2026-07-28T01:31:08+00:00
---
# cisco.ise.subscriber module – Resource module for Subscriber

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
> see [Requirements](subscriber_module.md#ansible-collections-cisco-ise-subscriber-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.subscriber`.

New in cisco.ise 3.2_beta

- [Synopsis](subscriber_module.md#synopsis)
- [Requirements](subscriber_module.md#requirements)
- [Parameters](subscriber_module.md#parameters)
- [Notes](subscriber_module.md#notes)
- [Examples](subscriber_module.md#examples)
- [Return Values](subscriber_module.md#return-values)

## [Synopsis](subscriber_module.md#id1)

- Manage operations create, update and delete of the resource Subscriber.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](subscriber_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.1
- python >= 3.5

## [Parameters](subscriber_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Subscriber is enabled or not.  **Choices:**   - `false` - `true` |
| **friendlyName**  string | Friendly name for the subscriber. |
| **identityGroups**  string | Identity Group(s). With more than one idGroups it needs to be comma seperated. |
| **imeis**  string | IMEI to be attached to the subscriber. |
| **imsi**  string | IMSI for Subscriber. |
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
| **ki**  string | KI. |
| **opc**  string | OPC. |
| **subscriberId**  string | SubscriberId path parameter. Unique id for a subscriber object. |

## [Notes](subscriber_module.md#id4)

> **Note:**
>
> - SDK Method used are subscriber.Subscriber.create_subscriber, subscriber.Subscriber.delete_subscriber, subscriber.Subscriber.update_subscriber,
> - Paths used are post /api/v1/fiveg/subscriber, delete /api/v1/fiveg/subscriber/{subscriberId}, put /api/v1/fiveg/subscriber/{subscriberId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](subscriber_module.md#id5)

```yaml+jinja
- name: Create
  cisco.ise.subscriber:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    enabled: true
    friendlyName: string
    identityGroups: string
    imeis: string
    imsi: string
    ki: string
    opc: string

- name: Update by id
  cisco.ise.subscriber:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    enabled: true
    friendlyName: string
    identityGroups: string
    imeis: string
    ki: string
    opc: string
    subscriberId: string

- name: Delete by id
  cisco.ise.subscriber:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    subscriberId: string
```

## [Return Values](subscriber_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"createTime": "string", "enabled": true, "friendlyName": "string", "id": "string", "identityGroups": "string", "imeis": "string", "imsi": "string", "ki": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "opc": "string", "updateTime": "string"}` |
| **ise_update_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"response": {"createTime": "string", "enabled": true, "friendlyName": "string", "id": "string", "identityGroups": "string", "imeis": "string", "imsi": "string", "ki": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "opc": "string", "updateTime": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
