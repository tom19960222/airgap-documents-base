---
collection: ansible
version: "8"
title: "cisco.ise.sponsor_group module – Resource module for Sponsor Group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/sponsor_group_module.html
fetched_at: 2026-07-28T01:31:03+00:00
---
# cisco.ise.sponsor_group module – Resource module for Sponsor Group

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
> see [Requirements](sponsor_group_module.md#ansible-collections-cisco-ise-sponsor-group-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.sponsor_group`.

New in cisco.ise 1.0.0

- [Synopsis](sponsor_group_module.md#synopsis)
- [Requirements](sponsor_group_module.md#requirements)
- [Parameters](sponsor_group_module.md#parameters)
- [Notes](sponsor_group_module.md#notes)
- [Examples](sponsor_group_module.md#examples)
- [Return Values](sponsor_group_module.md#return-values)

## [Synopsis](sponsor_group_module.md#id1)

- Manage operations create, update and delete of the resource Sponsor Group.
- This API creates a sponsor group.
- This API deletes a sponsor group by ID.
- This API allows the client to update a sponsor group by ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sponsor_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](sponsor_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autoNotification**  boolean | AutoNotification flag.  **Choices:**   - `false` - `true` |
| **createPermissions**  dictionary | Sponsor Group’s createPermissions. |
| **canCreateRandomAccounts**  boolean | CanCreateRandomAccounts flag.  **Choices:**   - `false` - `true` |
| **canImportMultipleAccounts**  boolean | CanImportMultipleAccounts flag.  **Choices:**   - `false` - `true` |
| **canSetFutureStartDate**  boolean | CanSetFutureStartDate flag.  **Choices:**   - `false` - `true` |
| **canSpecifyUsernamePrefix**  boolean | CanSpecifyUsernamePrefix flag.  **Choices:**   - `false` - `true` |
| **defaultUsernamePrefix**  string | Sponsor Group’s defaultUsernamePrefix. |
| **importBatchSizeLimit**  integer | Sponsor Group’s importBatchSizeLimit. |
| **randomBatchSizeLimit**  integer | Sponsor Group’s randomBatchSizeLimit. |
| **startDateFutureLimitDays**  integer | Sponsor Group’s startDateFutureLimitDays. |
| **description**  string | Sponsor Group’s description. |
| **guestTypes**  list / elements=string | Sponsor Group’s guestTypes. |
| **id**  string | Sponsor Group’s id. |
| **isDefaultGroup**  boolean | IsDefaultGroup flag.  **Choices:**   - `false` - `true` |
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
| **isEnabled**  boolean | IsEnabled flag.  **Choices:**   - `false` - `true` |
| **locations**  list / elements=string | Sponsor Group’s locations. |
| **managePermission**  string | Sponsor Group’s managePermission. |
| **memberGroups**  list / elements=string | Sponsor Group’s memberGroups. |
| **name**  string | Sponsor Group’s name. |
| **otherPermissions**  dictionary | Sponsor Group’s otherPermissions. |
| **canAccessViaREST**  boolean | CanAccessViaREST flag.  **Choices:**   - `false` - `true` |
| **canApproveSelfregGuests**  boolean | CanApproveSelfregGuests flag.  **Choices:**   - `false` - `true` |
| **canDeleteGuestAccounts**  boolean | CanDeleteGuestAccounts flag.  **Choices:**   - `false` - `true` |
| **canExtendGuestAccounts**  boolean | CanExtendGuestAccounts flag.  **Choices:**   - `false` - `true` |
| **canReinstateSuspendedAccounts**  boolean | CanReinstateSuspendedAccounts flag.  **Choices:**   - `false` - `true` |
| **canResetGuestPasswords**  boolean | CanResetGuestPasswords flag.  **Choices:**   - `false` - `true` |
| **canSendSMSNotifications**  boolean | CanSendSMSNotifications flag.  **Choices:**   - `false` - `true` |
| **canSuspendGuestAccounts**  boolean | CanSuspendGuestAccounts flag.  **Choices:**   - `false` - `true` |
| **canUpdateGuestContactInfo**  boolean | CanUpdateGuestContactInfo flag.  **Choices:**   - `false` - `true` |
| **canViewGuestPasswords**  boolean | CanViewGuestPasswords flag.  **Choices:**   - `false` - `true` |
| **limitApprovalToSponsorsGuests**  boolean | LimitApprovalToSponsorsGuests flag.  **Choices:**   - `false` - `true` |
| **requireSuspensionReason**  boolean | RequireSuspensionReason flag.  **Choices:**   - `false` - `true` |

## [Notes](sponsor_group_module.md#id4)

> **Note:**
>
> - SDK Method used are sponsor_group.SponsorGroup.create_sponsor_group, sponsor_group.SponsorGroup.delete_sponsor_group_by_id, sponsor_group.SponsorGroup.update_sponsor_group_by_id,
> - Paths used are post /ers/config/sponsorgroup, delete /ers/config/sponsorgroup/{id}, put /ers/config/sponsorgroup/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](sponsor_group_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.sponsor_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    autoNotification: true
    createPermissions:
      canCreateRandomAccounts: true
      canImportMultipleAccounts: true
      canSetFutureStartDate: true
      canSpecifyUsernamePrefix: true
      defaultUsernamePrefix: string
      importBatchSizeLimit: 0
      randomBatchSizeLimit: 0
      startDateFutureLimitDays: 0
    description: string
    guestTypes:
    - string
    id: string
    isDefaultGroup: true
    isEnabled: true
    locations:
    - string
    managePermission: string
    memberGroups:
    - string
    name: string
    otherPermissions:
      canAccessViaRest: true
      canApproveSelfregGuests: true
      canDeleteGuestAccounts: true
      canExtendGuestAccounts: true
      canReinstateSuspendedAccounts: true
      canResetGuestPasswords: true
      canSendSmsNotifications: true
      canSuspendGuestAccounts: true
      canUpdateGuestContactInfo: true
      canViewGuestPasswords: true
      limitApprovalToSponsorsGuests: true
      requireSuspensionReason: true

- name: Delete by id
  cisco.ise.sponsor_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sponsor_group:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    autoNotification: true
    createPermissions:
      canCreateRandomAccounts: true
      canImportMultipleAccounts: true
      canSetFutureStartDate: true
      canSpecifyUsernamePrefix: true
      defaultUsernamePrefix: string
      importBatchSizeLimit: 0
      randomBatchSizeLimit: 0
      startDateFutureLimitDays: 0
    description: string
    guestTypes:
    - string
    isDefaultGroup: true
    isEnabled: true
    locations:
    - string
    managePermission: string
    memberGroups:
    - string
    name: string
    otherPermissions:
      canAccessViaRest: true
      canApproveSelfregGuests: true
      canDeleteGuestAccounts: true
      canExtendGuestAccounts: true
      canReinstateSuspendedAccounts: true
      canResetGuestPasswords: true
      canSendSmsNotifications: true
      canSuspendGuestAccounts: true
      canUpdateGuestContactInfo: true
      canViewGuestPasswords: true
      limitApprovalToSponsorsGuests: true
      requireSuspensionReason: true
```

## [Return Values](sponsor_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"autoNotification": true, "createPermissions": {"canCreateRandomAccounts": true, "canImportMultipleAccounts": true, "canSetFutureStartDate": true, "canSpecifyUsernamePrefix": true, "defaultUsernamePrefix": "string", "importBatchSizeLimit": 0, "randomBatchSizeLimit": 0, "startDateFutureLimitDays": 0}, "description": "string", "guestTypes": ["string"], "id": "string", "isDefaultGroup": true, "isEnabled": true, "link": {"href": "string", "rel": "string", "type": "string"}, "locations": ["string"], "managePermission": "string", "memberGroups": ["string"], "name": "string", "otherPermissions": {"canAccessViaRest": true, "canApproveSelfregGuests": true, "canDeleteGuestAccounts": true, "canExtendGuestAccounts": true, "canReinstateSuspendedAccounts": true, "canResetGuestPasswords": true, "canSendSmsNotifications": true, "canSuspendGuestAccounts": true, "canUpdateGuestContactInfo": true, "canViewGuestPasswords": true, "limitApprovalToSponsorsGuests": true, "requireSuspensionReason": true}}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
