---
collection: ansible
version: "6"
title: "cisco.ise.my_device_portal_info module – Information module for My Device Portal"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/my_device_portal_info_module.html
fetched_at: 2026-07-27T16:57:50+00:00
---
# cisco.ise.my_device_portal_info module – Information module for My Device Portal

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
> see [Requirements](my_device_portal_info_module.md#ansible-collections-cisco-ise-my-device-portal-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.my_device_portal_info`.

New in cisco.ise 1.0.0

- [Synopsis](my_device_portal_info_module.md#synopsis)
- [Requirements](my_device_portal_info_module.md#requirements)
- [Parameters](my_device_portal_info_module.md#parameters)
- [Notes](my_device_portal_info_module.md#notes)
- [Examples](my_device_portal_info_module.md#examples)
- [Return Values](my_device_portal_info_module.md#return-values)

## [Synopsis](my_device_portal_info_module.md#id1)

- Get all My Device Portal.
- Get My Device Portal by id.
- This API allows the client to get a my device portal by ID.
- This API allows the client to get all the my device portals.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](my_device_portal_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](my_device_portal_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **filter**  list / elements=string | Filter query parameter. \*\*Simple filtering\*\* should be available through the filter query string parameter. The structure of a filter is a triplet of field operator and value separated with dots. More than one filter can be sent. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the “filterType=or” query string parameter.  Each resource Data model description should specify if an attribute is a filtered field.  The ‘EQ’ operator describes ‘Equals’.  The ‘NEQ’ operator describes ‘Not Equals’.  The ‘GT’ operator describes ‘Greater Than’.  The ‘LT’ operator describes ‘Less Than’.  The ‘STARTSW’ operator describes ‘Starts With’.  The ‘NSTARTSW’ operator describes ‘Not Starts With’.  The ‘ENDSW’ operator describes ‘Ends With’.  The ‘NENDSW’ operator describes ‘Not Ends With’.  The ‘CONTAINS’ operator describes ‘Contains’.  The ‘NCONTAINS’ operator describes ‘Not Contains’. |
| **filterType**  string | FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and can be changed by using the parameter. |
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
| **page**  integer | Page query parameter. Page number. |
| **size**  integer | Size query parameter. Number of objects returned per page. |
| **sortasc**  string | Sortasc query parameter. Sort asc. |
| **sortdsc**  string | Sortdsc query parameter. Sort desc. |

## [Notes](my_device_portal_info_module.md#id4)

> **Note:**
>
> - SDK Method used are my_device_portal.MyDevicePortal.get_my_device_portal_by_id, my_device_portal.MyDevicePortal.get_my_device_portal_generator,
> - Paths used are get /ers/config/mydeviceportal, get /ers/config/mydeviceportal/{id},
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](my_device_portal_info_module.md#id5)

```yaml+jinja
- name: Get all My Device Portal
  cisco.ise.my_device_portal_info:
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

- name: Get My Device Portal by id
  cisco.ise.my_device_portal_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result
```

## [Return Values](my_device_portal_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"customizations": {"globalCustomizations": {"backgroundImage": {"data": "string"}, "bannerImage": {"data": "string"}, "bannerTitle": "string", "contactText": "string", "desktopLogoImage": {"data": "string"}, "footerElement": "string", "mobileLogoImage": {"data": "string"}}, "language": {"viewLanguage": "string"}, "pageCustomizations": {"data": [{"key": "string", "value": "string"}]}, "portalTheme": {"id": "string", "name": "string", "themeData": "string"}, "portalTweakSettings": {"bannerColor": "string", "bannerTextColor": "string", "pageBackgroundColor": "string", "pageLabelAndTextColor": "string"}}, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalTestUrl": "string", "portalType": "string", "settings": {"aupSettings": {"displayFrequency": "string", "displayFrequencyIntervalDays": 0, "includeAup": true, "requireScrolling": true}, "employeeChangePasswordSettings": {"allowEmployeeToChangePwd": true}, "loginPageSettings": {"aupDisplay": "string", "includeAup": true, "maxFailedAttemptsBeforeRateLimit": 0, "requireAupAcceptance": true, "requireScrolling": true, "socialConfigs": [{}], "timeBetweenLoginsDuringRateLimit": 0}, "portalSettings": {"allowedInterfaces": ["string"], "alwaysUsedLanguage": "string", "certificateGroupTag": "string", "displayLang": "string", "endpointIdentityGroup": "string", "fallbackLanguage": "string", "httpsPort": 0}, "postAccessBannerSettings": {"includePostAccessBanner": true}, "postLoginBannerSettings": {"includePostAccessBanner": true}, "supportInfoSettings": {"defaultEmptyFieldValue": "string", "emptyFieldDisplay": "string", "includeBrowserUserAgent": true, "includeFailureCode": true, "includeIpAddress": true, "includeMacAddr": true, "includePolicyServer": true, "includeSupportInfoPage": true}}}` |
| **ise_responses**  list / elements=dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `"[\n  {\n    \"id\": \"string\",\n    \"name\": \"string\",\n    \"description\": \"string\",\n    \"portalType\": \"string\",\n    \"portalTestUrl\": \"string\",\n    \"settings\": {\n      \"portalSettings\": {\n        \"httpsPort\": 0,\n        \"allowedInterfaces\": [\n          \"string\"\n        ],\n        \"certificateGroupTag\": \"string\",\n        \"endpointIdentityGroup\": \"string\",\n        \"displayLang\": \"string\",\n        \"fallbackLanguage\": \"string\",\n        \"alwaysUsedLanguage\": \"string\"\n      },\n      \"loginPageSettings\": {\n        \"maxFailedAttemptsBeforeRateLimit\": 0,\n        \"timeBetweenLoginsDuringRateLimit\": 0,\n        \"includeAup\": true,\n        \"aupDisplay\": \"string\",\n        \"requireAupAcceptance\": true,\n        \"requireScrolling\": true,\n        \"socialConfigs\": [\n          {}\n        ]\n      },\n      \"aupSettings\": {\n        \"displayFrequencyIntervalDays\": 0,\n        \"displayFrequency\": \"string\",\n        \"includeAup\": true,\n        \"requireScrolling\": true\n      },\n      \"employeeChangePasswordSettings\": {\n        \"allowEmployeeToChangePwd\": true\n      },\n      \"postLoginBannerSettings\": {\n        \"includePostAccessBanner\": true\n      },\n      \"postAccessBannerSettings\": {\n        \"includePostAccessBanner\": true\n      },\n      \"supportInfoSettings\": {\n        \"includeSupportInfoPage\": true,\n        \"includeMacAddr\": true,\n        \"includeIpAddress\": true,\n        \"includeBrowserUserAgent\": true,\n        \"includePolicyServer\": true,\n        \"includeFailureCode\": true,\n        \"emptyFieldDisplay\": \"string\",\n        \"defaultEmptyFieldValue\": \"string\"\n      }\n    },\n    \"customizations\": {\n      \"portalTheme\": {\n        \"id\": \"string\",\n        \"name\": \"string\",\n        \"themeData\": \"string\"\n      },\n      \"portalTweakSettings\": {\n        \"bannerColor\": \"string\",\n        \"bannerTextColor\": \"string\",\n        \"pageBackgroundColor\": \"string\",\n        \"pageLabelAndTextColor\": \"string\"\n      },\n      \"language\": {\n        \"viewLanguage\": \"string\"\n      },\n      \"globalCustomizations\": {\n        \"mobileLogoImage\": {\n          \"data\": \"string\"\n        },\n        \"desktopLogoImage\": {\n          \"data\": \"string\"\n        },\n        \"bannerImage\": {\n          \"data\": \"string\"\n        },\n        \"backgroundImage\": {\n          \"data\": \"string\"\n        },\n        \"bannerTitle\": \"string\",\n        \"contactText\": \"string\",\n        \"footerElement\": \"string\"\n      },\n      \"pageCustomizations\": {\n        \"data\": [\n          {\n            \"key\": \"string\",\n            \"value\": \"string\"\n          }\n        ]\n      }\n    },\n    \"link\": {\n      \"rel\": \"string\",\n      \"href\": \"string\",\n      \"type\": \"string\"\n    }\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
