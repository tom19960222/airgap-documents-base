---
collection: ansible
version: "8"
title: "cisco.ise.guest_user module – Resource module for Guest User"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/guest_user_module.html
fetched_at: 2026-07-28T01:28:34+00:00
---
# cisco.ise.guest_user module – Resource module for Guest User

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
> see [Requirements](guest_user_module.md#ansible-collections-cisco-ise-guest-user-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.guest_user`.

New in cisco.ise 1.0.0

- [Synopsis](guest_user_module.md#synopsis)
- [Requirements](guest_user_module.md#requirements)
- [Parameters](guest_user_module.md#parameters)
- [Notes](guest_user_module.md#notes)
- [Examples](guest_user_module.md#examples)
- [Return Values](guest_user_module.md#return-values)

## [Synopsis](guest_user_module.md#id1)

- Manage operations create, update and delete of the resource Guest User.
- This API creates a guest user.
- This API deletes a guest user by ID.
- This API deletes a guest user.
- This API allows the client to update a guest user by ID.
- This API allows the client to update a guest user by name.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](guest_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](guest_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **customFields**  dictionary | Key value map. |
| **description**  string | Guest User’s description. |
| **guestAccessInfo**  dictionary | Guest User’s guestAccessInfo. |
| **fromDate**  string | Guest User’s fromDate. |
| **groupTag**  string | Guest User’s groupTag. |
| **location**  string | Guest User’s location. |
| **ssid**  string | Guest User’s ssid. |
| **toDate**  string | Guest User’s toDate. |
| **validDays**  integer | Guest User’s validDays. |
| **guestInfo**  dictionary | Guest User’s guestInfo. |
| **company**  string | Guest User’s company. |
| **creationTime**  string | Guest User’s creationTime. |
| **emailAddress**  string | Guest User’s emailAddress. |
| **enabled**  boolean | This field is only for Get operation not applicable for Create, Update operations.  **Choices:**   - `false` - `true` |
| **firstName**  string | Guest User’s firstName. |
| **lastName**  string | Guest User’s lastName. |
| **notificationLanguage**  string | Guest User’s notificationLanguage. |
| **password**  string | Guest User’s password. |
| **phoneNumber**  string | Phone number should be E.164 format. |
| **smsServiceProvider**  string | Guest User’s smsServiceProvider. |
| **userName**  string | If account needs be created with mobile number, please provide mobile number here. |
| **guestType**  string | Guest User’s guestType. |
| **id**  string | Guest User’s id. |
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
| **name**  string | Guest User’s name. |
| **portalId**  string | Guest User’s portalId. |
| **reasonForVisit**  string | Guest User’s reasonForVisit. |
| **sponsorUserId**  string | Guest User’s sponsorUserId. |
| **sponsorUserName**  string | Guest User’s sponsorUserName. |
| **status**  string | Guest User’s status. |
| **statusReason**  string | Guest User’s statusReason. |

## [Notes](guest_user_module.md#id4)

> **Note:**
>
> - SDK Method used are guest_user.GuestUser.create_guest_user, guest_user.GuestUser.delete_guest_user_by_id, guest_user.GuestUser.delete_guest_user_by_name, guest_user.GuestUser.update_guest_user_by_id, guest_user.GuestUser.update_guest_user_by_name,
> - Paths used are post /ers/config/guestuser, delete /ers/config/guestuser/name/{name}, delete /ers/config/guestuser/{id}, put /ers/config/guestuser/name/{name}, put /ers/config/guestuser/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](guest_user_module.md#id5)

```yaml+jinja
- name: Update by name
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customFields: {}
    description: string
    guestAccessInfo:
      fromDate: string
      groupTag: string
      location: string
      ssid: string
      toDate: string
      validDays: 0
    guestInfo:
      company: string
      creationTime: string
      emailAddress: string
      enabled: true
      firstName: string
      lastName: string
      notificationLanguage: string
      password: string
      phoneNumber: string
      smsServiceProvider: string
      userName: string
    guestType: string
    id: string
    name: string
    portalId: string
    reasonForVisit: string
    sponsorUserId: string
    sponsorUserName: string
    status: string
    statusReason: string

- name: Delete by name
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string

- name: Update by id
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customFields: {}
    description: string
    guestAccessInfo:
      fromDate: string
      groupTag: string
      location: string
      ssid: string
      toDate: string
      validDays: 0
    guestInfo:
      company: string
      creationTime: string
      emailAddress: string
      enabled: true
      firstName: string
      lastName: string
      notificationLanguage: string
      password: string
      phoneNumber: string
      smsServiceProvider: string
      userName: string
    guestType: string
    id: string
    name: string
    portalId: string
    reasonForVisit: string
    sponsorUserId: string
    sponsorUserName: string
    status: string
    statusReason: string

- name: Delete by id
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.guest_user:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customFields: {}
    description: string
    guestAccessInfo:
      fromDate: string
      groupTag: string
      location: string
      ssid: string
      toDate: string
      validDays: 0
    guestInfo:
      company: string
      creationTime: string
      emailAddress: string
      enabled: true
      firstName: string
      lastName: string
      notificationLanguage: string
      password: string
      phoneNumber: string
      smsServiceProvider: string
      userName: string
    guestType: string
    name: string
    portalId: string
    reasonForVisit: string
    sponsorUserId: string
    sponsorUserName: string
    status: string
    statusReason: string
```

## [Return Values](guest_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"customFields": {}, "description": "string", "guestAccessInfo": {"fromDate": "string", "groupTag": "string", "location": "string", "ssid": "string", "toDate": "string", "validDays": 0}, "guestInfo": {"company": "string", "creationTime": "string", "emailAddress": "string", "enabled": true, "firstName": "string", "lastName": "string", "notificationLanguage": "string", "password": "string", "phoneNumber": "string", "smsServiceProvider": "string", "userName": "string"}, "guestType": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalId": "string", "reasonForVisit": "string", "sponsorUserId": "string", "sponsorUserName": "string", "status": "string", "statusReason": "string"}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
