---
collection: ansible
version: "6"
title: "cisco.ise.active_directory module – Resource module for Active Directory"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/active_directory_module.html
fetched_at: 2026-07-27T16:56:03+00:00
---
# cisco.ise.active_directory module – Resource module for Active Directory

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
> see [Requirements](active_directory_module.md#ansible-collections-cisco-ise-active-directory-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.active_directory`.

New in cisco.ise 1.0.0

- [Synopsis](active_directory_module.md#synopsis)
- [Requirements](active_directory_module.md#requirements)
- [Parameters](active_directory_module.md#parameters)
- [Notes](active_directory_module.md#notes)
- [Examples](active_directory_module.md#examples)
- [Return Values](active_directory_module.md#return-values)

## [Synopsis](active_directory_module.md#id1)

- Manage operations create and delete of the resource Active Directory.
- This API creates an AD join point in Cisco ISE.
- This API deletes an AD join point from Cisco ISE.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](active_directory_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](active_directory_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **adAttributes**  dictionary | Holds list of AD Attributes. |
| **attributes**  list / elements=dictionary | List of Attributes. |
| **defaultValue**  string | Required for each attribute in the attribute list. Can contain an empty string. All characters are allowed except <%”. |
| **internalName**  string | Required for each attribute in the attribute list. All characters are allowed except <%”. |
| **name**  string | Required for each attribute in the attribute list with no duplication between attributes. All characters are allowed except <%”. |
| **type**  string | Required for each group in the group list. Allowed values STRING, IP, BOOLEAN, INT, OCTET_STRING. |
| **adgroups**  dictionary | Holds list of AD Groups. |
| **groups**  list / elements=dictionary | List of Groups. |
| **name**  string | Required for each group in the group list with no duplication between groups. All characters are allowed except %. |
| **sid**  string | Cisco ISE uses security identifiers (SIDs) for optimization of group membership evaluation. SIDs are useful for efficiency (speed) when the groups are evaluated. All characters are allowed except %. |
| **type**  string | No character restriction. |
| **adScopesNames**  string | String that contains the names of the scopes that the active directory belongs to. Names are separated by comma. Alphanumeric, underscore (_) characters are allowed. |
| **advancedSettings**  dictionary | Active Directory’s advancedSettings. |
| **agingTime**  integer | Range 1-8760 hours. |
| **authProtectionType**  string | Enable prevent AD account lockout. Allowed values - WIRELESS, - WIRED, - BOTH. |
| **country**  string | User info attribute. All characters are allowed except %. |
| **department**  string | User info attribute. All characters are allowed except %. |
| **email**  string | User info attribute. All characters are allowed except %. |
| **enableCallbackForDialinClient**  boolean | EnableCallbackForDialinClient flag.  Choices:   - `false` - `true` |
| **enableDialinPermissionCheck**  boolean | EnableDialinPermissionCheck flag.  Choices:   - `false` - `true` |
| **enableFailedAuthProtection**  boolean | Enable prevent AD account lockout due to too many bad password attempts.  Choices:   - `false` - `true` |
| **enableMachineAccess**  boolean | EnableMachineAccess flag.  Choices:   - `false` - `true` |
| **enableMachineAuth**  boolean | EnableMachineAuth flag.  Choices:   - `false` - `true` |
| **enablePassChange**  boolean | EnablePassChange flag.  Choices:   - `false` - `true` |
| **enableRewrites**  boolean | EnableRewrites flag.  Choices:   - `false` - `true` |
| **failedAuthThreshold**  integer | Number of bad password attempts. |
| **firstName**  string | User info attribute. All characters are allowed except %. |
| **identityNotInAdBehaviour**  string | Allowed values REJECT, SEARCH_JOINED_FOREST, SEARCH_ALL. |
| **jobTitle**  string | User info attribute. All characters are allowed except %. |
| **lastName**  string | User info attribute. All characters are allowed except %. |
| **locality**  string | User info attribute. All characters are allowed except %. |
| **organizationalUnit**  string | User info attribute. All characters are allowed except %. |
| **plaintextAuth**  boolean | PlaintextAuth flag.  Choices:   - `false` - `true` |
| **rewriteRules**  list / elements=dictionary | Identity rewrite is an advanced feature that directs Cisco ISE to manipulate the identity before it is passed to the external Active Directory system. You can create rules to change the identity to a desired format that includes or excludes a domain prefix and/or suffix or other additional markup of your choice. |
| **rewriteMatch**  string | Required for each rule in the list with no duplication between rules. All characters are allowed except %”. |
| **rewriteResult**  string | Required for each rule in the list. All characters are allowed except %”. |
| **rowId**  integer | Required for each rule in the list in serial order. |
| **schema**  string | Allowed values ACTIVE_DIRECTORY, CUSTOM. Choose ACTIVE_DIRECTORY schema when the AD attributes defined in AD can be copied to relevant attributes in Cisco ISE. If customization is needed, choose CUSTOM schema. All User info attributes are always set to default value if schema is ACTIVE_DIRECTORY. Values can be changed only for CUSTOM schema. |
| **stateOrProvince**  string | User info attribute. All characters are allowed except %. |
| **streetAddress**  string | User info attribute. All characters are allowed except %. |
| **telephone**  string | User info attribute. All characters are allowed except %. |
| **unreachableDomainsBehaviour**  string | Allowed values PROCEED, DROP. |
| **description**  string | No character restriction. |
| **domain**  string | The AD domain. Alphanumeric, hyphen (-) and dot (.) characters are allowed. |
| **enableDomainWhiteList**  boolean | EnableDomainWhiteList flag.  Choices:   - `false` - `true` |
| **id**  string | Id path parameter. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Resource Name. Maximum 32 characters allowed. Allowed characters are alphanumeric and .-_/\\ characters. |

## [Notes](active_directory_module.md#id4)

> **Note:**
>
> - SDK Method used are active_directory.ActiveDirectory.create_active_directory, active_directory.ActiveDirectory.delete_active_directory_by_id,
> - Paths used are post /ers/config/activedirectory, delete /ers/config/activedirectory/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](active_directory_module.md#id5)

```yaml+jinja
- name: Delete by id
  cisco.ise.active_directory:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.active_directory:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    adAttributes:
      attributes:
      - defaultValue: string
        internalName: string
        name: string
        type: string
    adScopesNames: string
    adgroups:
      groups:
      - name: string
        sid: string
        type: string
    advancedSettings:
      agingTime: 0
      authProtectionType: string
      country: string
      department: string
      email: string
      enableCallbackForDialinClient: true
      enableDialinPermissionCheck: true
      enableFailedAuthProtection: true
      enableMachineAccess: true
      enableMachineAuth: true
      enablePassChange: true
      enableRewrites: true
      failedAuthThreshold: 0
      firstName: string
      identityNotInAdBehaviour: string
      jobTitle: string
      lastName: string
      locality: string
      organizationalUnit: string
      plaintextAuth: true
      rewriteRules:
      - rewriteMatch: string
        rewriteResult: string
        rowId: 0
      schema: string
      stateOrProvince: string
      streetAddress: string
      telephone: string
      unreachableDomainsBehaviour: string
    description: string
    domain: string
    enableDomainWhiteList: true
    id: string
    name: string
```

## [Return Values](active_directory_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"adAttributes": {"attributes": [{"defaultValue": "string", "internalName": "string", "name": "string", "type": "string"}]}, "adScopesNames": "string", "adgroups": {"groups": [{"name": "string", "sid": "string", "type": "string"}]}, "advancedSettings": {"agingTime": 0, "authProtectionType": "string", "country": "string", "department": "string", "email": "string", "enableCallbackForDialinClient": true, "enableDialinPermissionCheck": true, "enableFailedAuthProtection": true, "enableMachineAccess": true, "enableMachineAuth": true, "enablePassChange": true, "enableRewrites": true, "failedAuthThreshold": 0, "firstName": "string", "identityNotInAdBehaviour": "string", "jobTitle": "string", "lastName": "string", "locality": "string", "organizationalUnit": "string", "plaintextAuth": true, "rewriteRules": [{"rewriteMatch": "string", "rewriteResult": "string", "rowId": 0}], "schema": "string", "stateOrProvince": "string", "streetAddress": "string", "telephone": "string", "unreachableDomainsBehaviour": "string"}, "description": "string", "domain": "string", "enableDomainAllowedList": true, "enableDomainWhiteList": true, "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
