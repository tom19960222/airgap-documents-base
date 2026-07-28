---
collection: ansible
version: "6"
title: "cisco.ise.guest_type module – Resource module for Guest Type"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/guest_type_module.html
fetched_at: 2026-07-27T16:57:12+00:00
---
# cisco.ise.guest_type module – Resource module for Guest Type

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
> see [Requirements](guest_type_module.md#ansible-collections-cisco-ise-guest-type-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.guest_type`.

New in cisco.ise 1.0.0

- [Synopsis](guest_type_module.md#synopsis)
- [Requirements](guest_type_module.md#requirements)
- [Parameters](guest_type_module.md#parameters)
- [Notes](guest_type_module.md#notes)
- [Examples](guest_type_module.md#examples)
- [Return Values](guest_type_module.md#return-values)

## [Synopsis](guest_type_module.md#id1)

- Manage operations create, update and delete of the resource Guest Type.
- This API creates a guest type.
- This API deletes a guest type.
- This API allows the client to update a guest type.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](guest_type_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](guest_type_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accessTime**  dictionary | Guest Type’s accessTime. |
| **allowAccessOnSpecificDaysTimes**  boolean | AllowAccessOnSpecificDaysTimes flag.  Choices:   - `false` - `true` |
| **dayTimeLimits**  list / elements=dictionary | List of Time Ranges for account access. |
| **days**  list / elements=string | List of Days Values should be one of Week day. Allowed values are - Sunday, - Monday, - Tuesday, - Wednesday, - Thursday, - Friday, - Saturday. |
| **endTime**  string | End time in HH mm format. |
| **startTime**  string | Start time in HH mm format. |
| **defaultDuration**  integer | Guest Type’s defaultDuration. |
| **durationTimeUnit**  string | Allowed values are - DAYS, - HOURS, - MINUTES. |
| **fromFirstLogin**  boolean | When Account Duration starts from first login or specified date.  Choices:   - `false` - `true` |
| **maxAccountDuration**  integer | Maximum value of Account Duration. |
| **description**  string | Guest Type’s description. |
| **expirationNotification**  dictionary | Expiration Notification Settings. |
| **advanceNotificationDuration**  integer | Send Account Expiration Notification Duration before ( Days, Hours, Minutes ). |
| **advanceNotificationUnits**  string | Allowed values are - DAYS, - HOURS, - MINUTES. |
| **emailText**  string | Guest Type’s emailText. |
| **enableNotification**  boolean | Enable Notification settings.  Choices:   - `false` - `true` |
| **sendEmailNotification**  boolean | Enable Email Notification.  Choices:   - `false` - `true` |
| **sendSMSNotification**  boolean | Maximum devices guests can register.  Choices:   - `false` - `true` |
| **smsText**  string | Guest Type’s smsText. |
| **id**  string | Guest Type’s id. |
| **isDefaultType**  boolean | IsDefaultType flag.  Choices:   - `false` - `true` |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **loginOptions**  dictionary | Guest Type’s loginOptions. |
| **allowGuestPortalBypass**  boolean | AllowGuestPortalBypass flag.  Choices:   - `false` - `true` |
| **failureAction**  string | When Guest Exceeds limit this action will be invoked. Allowed values are - Disconnect_Oldest_Connection, - Disconnect_Newest_Connection. |
| **identityGroupId**  string | Guest Type’s identityGroupId. |
| **limitSimultaneousLogins**  boolean | Enable Simultaneous Logins.  Choices:   - `false` - `true` |
| **maxRegisteredDevices**  integer | Maximum devices guests can register. |
| **maxSimultaneousLogins**  integer | Number of Simultaneous Logins. |
| **name**  string | Guest Type’s name. |
| **sponsorGroups**  list / elements=string | Guest Type’s sponsorGroups. |

## [Notes](guest_type_module.md#id4)

> **Note:**
>
> - SDK Method used are guest_type.GuestType.create_guest_type, guest_type.GuestType.delete_guest_type_by_id, guest_type.GuestType.update_guest_type_by_id,
> - Paths used are post /ers/config/guesttype, delete /ers/config/guesttype/{id}, put /ers/config/guesttype/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](guest_type_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.guest_type:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accessTime:
      allowAccessOnSpecificDaysTimes: true
      dayTimeLimits:
      - days:
        - string
        endTime: string
        startTime: string
      defaultDuration: 0
      durationTimeUnit: string
      fromFirstLogin: true
      maxAccountDuration: 0
    description: string
    expirationNotification:
      advanceNotificationDuration: 0
      advanceNotificationUnits: string
      emailText: string
      enableNotification: true
      sendEmailNotification: true
      sendSmsNotification: true
      smsText: string
    id: string
    isDefaultType: true
    loginOptions:
      allowGuestPortalBypass: true
      failureAction: string
      identityGroupId: string
      limitSimultaneousLogins: true
      maxRegisteredDevices: 0
      maxSimultaneousLogins: 0
    name: string
    sponsorGroups:
    - string

- name: Delete by id
  cisco.ise.guest_type:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.guest_type:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accessTime:
      allowAccessOnSpecificDaysTimes: true
      dayTimeLimits:
      - days:
        - string
        endTime: string
        startTime: string
      defaultDuration: 0
      durationTimeUnit: string
      fromFirstLogin: true
      maxAccountDuration: 0
    description: string
    expirationNotification:
      advanceNotificationDuration: 0
      advanceNotificationUnits: string
      emailText: string
      enableNotification: true
      sendEmailNotification: true
      sendSmsNotification: true
      smsText: string
    isDefaultType: true
    loginOptions:
      allowGuestPortalBypass: true
      failureAction: string
      identityGroupId: string
      limitSimultaneousLogins: true
      maxRegisteredDevices: 0
      maxSimultaneousLogins: 0
    name: string
    sponsorGroups:
    - string
```

## [Return Values](guest_type_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"accessTime": {"allowAccessOnSpecificDaysTimes": true, "dayTimeLimits": [{"days": ["string"], "endTime": "string", "startTime": "string"}], "defaultDuration": 0, "durationTimeUnit": "string", "fromFirstLogin": true, "maxAccountDuration": 0}, "description": "string", "expirationNotification": {"advanceNotificationDuration": 0, "advanceNotificationUnits": "string", "emailText": "string", "enableNotification": true, "sendEmailNotification": true, "sendSmsNotification": true, "smsText": "string"}, "id": "string", "isDefaultType": true, "link": {"href": "string", "rel": "string", "type": "string"}, "loginOptions": {"allowGuestPortalBypass": true, "failureAction": "string", "identityGroupId": "string", "limitSimultaneousLogins": true, "maxRegisteredDevices": 0, "maxSimultaneousLogins": 0}, "name": "string", "sponsorGroups": ["string"]}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
