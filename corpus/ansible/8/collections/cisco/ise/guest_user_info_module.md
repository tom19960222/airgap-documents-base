---
collection: ansible
version: "8"
title: "cisco.ise.guest_user_info module – Information module for Guest User"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/guest_user_info_module.html
fetched_at: 2026-07-28T01:28:39+00:00
---
# cisco.ise.guest_user_info module – Information module for Guest User

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
> see [Requirements](guest_user_info_module.md#ansible-collections-cisco-ise-guest-user-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.guest_user_info`.

New in cisco.ise 1.0.0

- [Synopsis](guest_user_info_module.md#synopsis)
- [Requirements](guest_user_info_module.md#requirements)
- [Parameters](guest_user_info_module.md#parameters)
- [Notes](guest_user_info_module.md#notes)
- [Examples](guest_user_info_module.md#examples)
- [Return Values](guest_user_info_module.md#return-values)

## [Synopsis](guest_user_info_module.md#id1)

- Get all Guest User.
- Get Guest User by id.
- Get Guest User by name.
- This API allows the client to get a guest user by ID.
- This API allows the client to get a guest user by name.
- This API allows the client to get all the guest users.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](guest_user_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](guest_user_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **filter**  list / elements=string | Filter query parameter. \*\*Simple filtering\*\* should be available through the filter query string parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the “filterType=or” query string parameter.  Each resource Data model description should specify if an attribute is a filtered field.  The ‘EQ’ operator describes ‘Equals’.  The ‘NEQ’ operator describes ‘Not Equals’.  The ‘GT’ operator describes ‘Greater Than’.  The ‘LT’ operator describes ‘Less Than’.  The ‘STARTSW’ operator describes ‘Starts With’.  The ‘NSTARTSW’ operator describes ‘Not Starts With’.  The ‘ENDSW’ operator describes ‘Ends With’.  The ‘NENDSW’ operator describes ‘Not Ends With’.  The ‘CONTAINS’ operator describes ‘Contains’.  The ‘NCONTAINS’ operator describes ‘Not Contains’. |
| **filterType**  string | FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the parameter. |
| **id**  string | Id path parameter. |
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
| **name**  string | Name path parameter. |
| **page**  integer | Page query parameter. Page number. |
| **size**  integer | Size query parameter. Number of objects returned per page. |
| **sortasc**  string | Sortasc query parameter. Sort asc. |
| **sortdsc**  string | Sortdsc query parameter. Sort desc. |

## [Notes](guest_user_info_module.md#id4)

> **Note:**
>
> - SDK Method used are guest_user.GuestUser.get_guest_user_by_id, guest_user.GuestUser.get_guest_user_by_name, guest_user.GuestUser.get_guest_users_generator,
> - Paths used are get /ers/config/guestuser, get /ers/config/guestuser/name/{name}, get /ers/config/guestuser/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](guest_user_info_module.md#id5)

```yaml+jinja
- name: Get all Guest User
  cisco.ise.guest_user_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
    sortasc: string
    sortdsc: string
    filter: []
    filterType: AND
  register: result

- name: Get Guest User by id
  cisco.ise.guest_user_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get Guest User by name
  cisco.ise.guest_user_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result
```

## [Return Values](guest_user_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"customFields": {}, "description": "string", "guestAccessInfo": {"fromDate": "string", "groupTag": "string", "location": "string", "ssid": "string", "toDate": "string", "validDays": 0}, "guestInfo": {"company": "string", "creationTime": "string", "emailAddress": "string", "enabled": true, "firstName": "string", "lastName": "string", "notificationLanguage": "string", "password": "string", "phoneNumber": "string", "smsServiceProvider": "string", "userName": "string"}, "guestType": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalId": "string", "reasonForVisit": "string", "sponsorUserId": "string", "sponsorUserName": "string", "status": "string", "statusReason": "string"}` |
| **ise_responses**  list / elements=dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"id\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"guestType\": \"string\",\n    \"status\": \"string\",\n    \"statusReason\": \"string\",\n    \"reasonForVisit\": \"string\",\n    \"sponsorUserId\": \"string\",\n    \"sponsorUserName\": \"string\",\n    \"guestInfo\": {\n      \"firstName\": \"string\",\n      \"lastName\": \"string\",\n      \"company\": \"string\",\n      \"creationTime\": \"string\",\n      \"notificationLanguage\": \"string\",\n      \"userName\": \"string\",\n      \"emailAddress\": \"string\",\n      \"phoneNumber\": \"string\",\n      \"password\": \"string\",\n      \"enabled\": true,\n      \"smsServiceProvider\": \"string\"\n    },\n    \"guestAccessInfo\": {\n      \"validDays\": 0,\n      \"fromDate\": \"string\",\n      \"toDate\": \"string\",\n      \"location\": \"string\",\n      \"ssid\": \"string\",\n      \"groupTag\": \"string\"\n    },\n    \"portalId\": \"string\",\n    \"customFields\": {},\n    \"link\": {\n      \"rel\": \"string\",\n      \"href\": \"string\",\n      \"type\": \"string\"\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
