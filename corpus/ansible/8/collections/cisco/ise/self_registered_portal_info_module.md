---
collection: ansible
version: "8"
title: "cisco.ise.self_registered_portal_info module – Information module for Self Registered Portal"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/self_registered_portal_info_module.html
fetched_at: 2026-07-28T01:30:41+00:00
---
# cisco.ise.self_registered_portal_info module – Information module for Self Registered Portal

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
> see [Requirements](self_registered_portal_info_module.md#ansible-collections-cisco-ise-self-registered-portal-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.self_registered_portal_info`.

New in cisco.ise 1.0.0

- [Synopsis](self_registered_portal_info_module.md#synopsis)
- [Requirements](self_registered_portal_info_module.md#requirements)
- [Parameters](self_registered_portal_info_module.md#parameters)
- [Notes](self_registered_portal_info_module.md#notes)
- [See Also](self_registered_portal_info_module.md#see-also)
- [Examples](self_registered_portal_info_module.md#examples)
- [Return Values](self_registered_portal_info_module.md#return-values)

## [Synopsis](self_registered_portal_info_module.md#id1)

- Get all Self Registered Portal.
- Get Self Registered Portal by id.
- This API allows the client to get a self registered portal by ID.
- This API allows the client to get all the self registered portals.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](self_registered_portal_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](self_registered_portal_info_module.md#id3)

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
| **page**  integer | Page query parameter. Page number. |
| **size**  integer | Size query parameter. Number of objects returned per page. |
| **sortasc**  string | Sortasc query parameter. Sort asc. |
| **sortdsc**  string | Sortdsc query parameter. Sort desc. |

## [Notes](self_registered_portal_info_module.md#id4)

> **Note:**
>
> - SDK Method used are self_registered_portal.SelfRegisteredPortal.get_self_registered_portal_by_id, self_registered_portal.SelfRegisteredPortal.get_self_registered_portals_generator,
> - Paths used are get /ers/config/selfregportal, get /ers/config/selfregportal/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](self_registered_portal_info_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for SelfRegisteredPortal](https://developer.cisco.com/docs/identity-services-engine/v1/#!selfregportal)
> :   Complete reference of the SelfRegisteredPortal API.

## [Examples](self_registered_portal_info_module.md#id6)

```yaml+jinja
- name: Get all Self Registered Portal
  cisco.ise.self_registered_portal_info:
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

- name: Get Self Registered Portal by id
  cisco.ise.self_registered_portal_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result
```

## [Return Values](self_registered_portal_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"customizations": {"globalCustomizations": {"backgroundImage": {"data": "string"}, "bannerImage": {"data": "string"}, "bannerTitle": "string", "contactText": "string", "desktopLogoImage": {"data": "string"}, "footerElement": "string", "mobileLogoImage": {"data": "string"}}, "language": {"viewLanguage": "string"}, "pageCustomizations": {"data": [{"key": "string", "value": "string"}]}, "portalTheme": {"id": "string", "name": "string", "themeData": "string"}, "portalTweakSettings": {"bannerColor": "string", "bannerTextColor": "string", "pageBackgroundColor": "string", "pageLabelAndTextColor": "string"}}, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalTestUrl": "string", "portalType": "string", "settings": {"aupSettings": {"displayFrequency": "string", "displayFrequencyIntervalDays": 0, "includeAup": true, "requireAupScrolling": true, "requireScrolling": true, "skipAupForEmployees": true, "useDiffAupForEmployees": true}, "authSuccessSettings": {"redirectUrl": "string", "successRedirect": "string"}, "byodSettings": {"byodRegistrationSettings": {"endPointIdentityGroupId": "string", "showDeviceID": true}, "byodRegistrationSuccessSettings": {"redirectUrl": "string", "successRedirect": "string"}, "byodWelcomeSettings": {"aupDisplay": "string", "enableBYOD": true, "enableGuestAccess": true, "includeAup": true, "requireAupAcceptance": true, "requireMDM": true, "requireScrolling": true}}, "guestChangePasswordSettings": {"allowChangePasswdAtFirstLogin": true}, "guestDeviceRegistrationSettings": {"allowGuestsToRegisterDevices": true, "autoRegisterGuestDevices": true}, "loginPageSettings": {"accessCode": "string", "allowAlternateGuestPortal": true, "allowForgotPassword": true, "allowGuestToChangePassword": true, "allowGuestToCreateAccounts": true, "allowGuestToUseSocialAccounts": true, "allowShowGuestForm": true, "alternateGuestPortal": "string", "aupDisplay": "string", "includeAup": true, "maxFailedAttemptsBeforeRateLimit": 0, "requireAccessCode": true, "requireAupAcceptance": true, "socialConfigs": [{"socialMediaType": "string", "socialMediaValue": "string"}], "timeBetweenLoginsDuringRateLimit": 0}, "portalSettings": {"allowedInterfaces": ["string"], "alwaysUsedLanguage": "string", "assignedGuestTypeForEmployee": "string", "authenticationMethod": "string", "certificateGroupTag": "string", "displayLang": "string", "fallbackLanguage": "string", "httpsPort": 0}, "postAccessBannerSettings": {"includePostAccessBanner": true}, "postLoginBannerSettings": {"includePostAccessBanner": true}, "selfRegPageSettings": {"accountValidityDuration": 0, "accountValidityTimeUnits": "string", "allowGraceAccess": true, "approvalEmailAddresses": "string", "approveDenyLinksTimeUnits": "string", "approveDenyLinksValidFor": 0, "assignGuestsToGuestType": "string", "aupDisplay": "string", "authenticateSponsorsUsingPortalList": true, "autoLoginSelfWait": true, "autoLoginTimePeriod": 0, "credentialNotificationUsingEmail": true, "credentialNotificationUsingSms": true, "enableGuestEmailBlacklist": true, "enableGuestEmailWhitelist": true, "fieldCompany": {"include": true, "require": true}, "fieldEmailAddr": {"include": true, "require": true}, "fieldFirstName": {"include": true, "require": true}, "fieldLastName": {"include": true, "require": true}, "fieldLocation": {"include": true, "require": true}, "fieldPersonBeingVisited": {"include": true, "require": true}, "fieldPhoneNo": {"include": true, "require": true}, "fieldReasonForVisit": {"include": true, "require": true}, "fieldSmsProvider": {"include": true, "require": true}, "fieldUserName": {"include": true, "require": true}, "graceAccessExpireInterval": 0, "graceAccessSendAccountExpiration": true, "guestEmailBlacklistDomains": ["string"], "guestEmailWhitelistDomains": ["string"], "includeAup": true, "postRegistrationRedirect": "string", "postRegistrationRedirectUrl": "string", "registrationCode": "string", "requireApproverToAuthenticate": true, "requireAupAcceptance": true, "requireGuestApproval": true, "requireRegistrationCode": true, "selectableLocations": ["string"], "selectableSmsProviders": ["string"], "sendApprovalRequestTo": "string", "sponsorPortalList": ["string"]}, "selfRegSuccessSettings": {"allowGuestLoginFromSelfregSuccessPage": true, "allowGuestSendSelfUsingEmail": true, "allowGuestSendSelfUsingPrint": true, "allowGuestSendSelfUsingSms": true, "aupOnPage": true, "includeAup": true, "includeCompany": true, "includeEmailAddr": true, "includeFirstName": true, "includeLastName": true, "includeLocation": true, "includePassword": true, "includePersonBeingVisited": true, "includePhoneNo": true, "includeReasonForVisit": true, "includeSmsProvider": true, "includeUserName": true, "requireAupAcceptance": true, "requireAupScrolling": true}, "supportInfoSettings": {"defaultEmptyFieldValue": "string", "emptyFieldDisplay": "string", "includeBrowserUserAgent": true, "includeFailureCode": true, "includeIpAddress": true, "includeMacAddr": true, "includePolicyServer": true, "includeSupportInfoPage": true}}}` |
| **ise_responses**  list / elements=dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"id\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"portalType\": \"string\",\n    \"portalTestUrl\": \"string\",\n    \"settings\": {\n      \"portalSettings\": {\n        \"httpsPort\": 0,\n        \"allowedInterfaces\": [\n          \"string\"\n        ],\n        \"certificateGroupTag\": \"string\",\n        \"authenticationMethod\": \"string\",\n        \"assignedGuestTypeForEmployee\": \"string\",\n        \"displayLang\": \"string\",\n        \"fallbackLanguage\": \"string\",\n        \"alwaysUsedLanguage\": \"string\"\n      },\n      \"loginPageSettings\": {\n        \"requireAccessCode\": true,\n        \"maxFailedAttemptsBeforeRateLimit\": 0,\n        \"timeBetweenLoginsDuringRateLimit\": 0,\n        \"includeAup\": true,\n        \"aupDisplay\": \"string\",\n        \"requireAupAcceptance\": true,\n        \"accessCode\": \"string\",\n        \"allowGuestToCreateAccounts\": true,\n        \"allowForgotPassword\": true,\n        \"allowGuestToChangePassword\": true,\n        \"allowAlternateGuestPortal\": true,\n        \"alternateGuestPortal\": \"string\",\n        \"allowGuestToUseSocialAccounts\": true,\n        \"allowShowGuestForm\": true,\n        \"socialConfigs\": [\n          {\n            \"socialMediaType\": \"string\",\n            \"socialMediaValue\": \"string\"\n          }\n        ]\n      },\n      \"selfRegPageSettings\": {\n        \"assignGuestsToGuestType\": \"string\",\n        \"accountValidityDuration\": 0,\n        \"accountValidityTimeUnits\": \"string\",\n        \"requireRegistrationCode\": true,\n        \"registrationCode\": \"string\",\n        \"fieldUserName\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"fieldFirstName\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"fieldLastName\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"fieldEmailAddr\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"fieldPhoneNo\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"fieldCompany\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"fieldLocation\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"selectableLocations\": [\n          \"string\"\n        ],\n        \"fieldSmsProvider\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"selectableSmsProviders\": [\n          \"string\"\n        ],\n        \"fieldPersonBeingVisited\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"fieldReasonForVisit\": {\n          \"include\": true,\n          \"require\": true\n        },\n        \"includeAup\": true,\n        \"aupDisplay\": \"string\",\n        \"requireAupAcceptance\": true,\n        \"enableGuestEmailWhitelist\": true,\n        \"guestEmailWhitelistDomains\": [\n          \"string\"\n        ],\n        \"enableGuestEmailBlacklist\": true,\n        \"guestEmailBlacklistDomains\": [\n          \"string\"\n        ],\n        \"requireGuestApproval\": true,\n        \"autoLoginSelfWait\": true,\n        \"autoLoginTimePeriod\": 0,\n        \"allowGraceAccess\": true,\n        \"graceAccessExpireInterval\": 0,\n        \"graceAccessSendAccountExpiration\": true,\n        \"sendApprovalRequestTo\": \"string\",\n        \"approvalEmailAddresses\": \"string\",\n        \"postRegistrationRedirect\": \"string\",\n        \"postRegistrationRedirectUrl\": \"string\",\n        \"credentialNotificationUsingEmail\": true,\n        \"credentialNotificationUsingSms\": true,\n        \"approveDenyLinksValidFor\": 0,\n        \"approveDenyLinksTimeUnits\": \"string\",\n        \"requireApproverToAuthenticate\": true,\n        \"authenticateSponsorsUsingPortalList\": true,\n        \"sponsorPortalList\": [\n          \"string\"\n        ]\n      },\n      \"selfRegSuccessSettings\": {\n        \"includeUserName\": true,\n        \"includePassword\": true,\n        \"includeFirstName\": true,\n        \"includeLastName\": true,\n        \"includeEmailAddr\": true,\n        \"includePhoneNo\": true,\n        \"includeCompany\": true,\n        \"includeLocation\": true,\n        \"includeSmsProvider\": true,\n        \"includePersonBeingVisited\": true,\n        \"includeReasonForVisit\": true,\n        \"allowGuestSendSelfUsingPrint\": true,\n        \"allowGuestSendSelfUsingEmail\": true,\n        \"allowGuestSendSelfUsingSms\": true,\n        \"includeAup\": true,\n        \"aupOnPage\": true,\n        \"requireAupAcceptance\": true,\n        \"requireAupScrolling\": true,\n        \"allowGuestLoginFromSelfregSuccessPage\": true\n      },\n      \"aupSettings\": {\n        \"includeAup\": true,\n        \"useDiffAupForEmployees\": true,\n        \"skipAupForEmployees\": true,\n        \"requireScrolling\": true,\n        \"requireAupScrolling\": true,\n        \"displayFrequency\": \"string\",\n        \"displayFrequencyIntervalDays\": 0\n      },\n      \"guestChangePasswordSettings\": {\n        \"allowChangePasswdAtFirstLogin\": true\n      },\n      \"guestDeviceRegistrationSettings\": {\n        \"autoRegisterGuestDevices\": true,\n        \"allowGuestsToRegisterDevices\": true\n      },\n      \"byodSettings\": {\n        \"byodWelcomeSettings\": {\n          \"enableBYOD\": true,\n          \"enableGuestAccess\": true,\n          \"requireMDM\": true,\n          \"includeAup\": true,\n          \"aupDisplay\": \"string\",\n          \"requireAupAcceptance\": true,\n          \"requireScrolling\": true\n        },\n        \"byodRegistrationSettings\": {\n          \"showDeviceID\": true,\n          \"endPointIdentityGroupId\": \"string\"\n        },\n        \"byodRegistrationSuccessSettings\": {\n          \"successRedirect\": \"string\",\n          \"redirectUrl\": \"string\"\n        }\n      },\n      \"postLoginBannerSettings\": {\n        \"includePostAccessBanner\": true\n      },\n      \"postAccessBannerSettings\": {\n        \"includePostAccessBanner\": true\n      },\n      \"authSuccessSettings\": {\n        \"successRedirect\": \"string\",\n        \"redirectUrl\": \"string\"\n      },\n      \"supportInfoSettings\": {\n        \"includeSupportInfoPage\": true,\n        \"includeMacAddr\": true,\n        \"includeIpAddress\": true,\n        \"includeBrowserUserAgent\": true,\n        \"includePolicyServer\": true,\n        \"includeFailureCode\": true,\n        \"emptyFieldDisplay\": \"string\",\n        \"defaultEmptyFieldValue\": \"string\"\n      }\n    },\n    \"customizations\": {\n      \"portalTheme\": {\n        \"id\": \"string\",\n        \"name\": \"string\",\n        \"themeData\": \"string\"\n      },\n      \"portalTweakSettings\": {\n        \"bannerColor\": \"string\",\n        \"bannerTextColor\": \"string\",\n        \"pageBackgroundColor\": \"string\",\n        \"pageLabelAndTextColor\": \"string\"\n      },\n      \"language\": {\n        \"viewLanguage\": \"string\"\n      },\n      \"globalCustomizations\": {\n        \"mobileLogoImage\": {\n          \"data\": \"string\"\n        },\n        \"desktopLogoImage\": {\n          \"data\": \"string\"\n        },\n        \"bannerImage\": {\n          \"data\": \"string\"\n        },\n        \"backgroundImage\": {\n          \"data\": \"string\"\n        },\n        \"bannerTitle\": \"string\",\n        \"contactText\": \"string\",\n        \"footerElement\": \"string\"\n      },\n      \"pageCustomizations\": {\n        \"data\": [\n          {\n            \"key\": \"string\",\n            \"value\": \"string\"\n          }\n        ]\n      }\n    },\n    \"link\": {\n      \"rel\": \"string\",\n      \"href\": \"string\",\n      \"type\": \"string\"\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
