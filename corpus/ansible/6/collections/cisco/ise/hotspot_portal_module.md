---
collection: ansible
version: "6"
title: "cisco.ise.hotspot_portal module – Resource module for Hotspot Portal"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/hotspot_portal_module.html
fetched_at: 2026-07-27T16:57:24+00:00
---
# cisco.ise.hotspot_portal module – Resource module for Hotspot Portal

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
> see [Requirements](hotspot_portal_module.md#ansible-collections-cisco-ise-hotspot-portal-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.hotspot_portal`.

New in cisco.ise 1.0.0

- [Synopsis](hotspot_portal_module.md#synopsis)
- [Requirements](hotspot_portal_module.md#requirements)
- [Parameters](hotspot_portal_module.md#parameters)
- [Notes](hotspot_portal_module.md#notes)
- [Examples](hotspot_portal_module.md#examples)
- [Return Values](hotspot_portal_module.md#return-values)

## [Synopsis](hotspot_portal_module.md#id1)

- Manage operations create, update and delete of the resource Hotspot Portal.
- This API creates a hotspot portal.
- This API deletes a hotspot portal by ID.
- This API allows the client to update a hotspot portal by ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](hotspot_portal_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](hotspot_portal_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **customizations**  dictionary | Defines all of the Portal Customizations available. |
| **globalCustomizations**  dictionary | Hotspot Portal’s globalCustomizations. |
| **backgroundImage**  dictionary | Hotspot Portal’s backgroundImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerImage**  dictionary | Hotspot Portal’s bannerImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerTitle**  string | Hotspot Portal’s bannerTitle. |
| **contactText**  string | Hotspot Portal’s contactText. |
| **desktopLogoImage**  dictionary | Hotspot Portal’s desktopLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **footerElement**  string | Hotspot Portal’s footerElement. |
| **mobileLogoImage**  dictionary | Hotspot Portal’s mobileLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **language**  dictionary | This property is supported only for Read operation and it allows to show the customizations in English. Other languages are not supported. |
| **viewLanguage**  string | Hotspot Portal’s viewLanguage. |
| **pageCustomizations**  dictionary | Hotspot Portal’s pageCustomizations. |
| **data**  list / elements=dictionary | Hotspot Portal’s data. |
| **key**  string | Hotspot Portal’s key. |
| **value**  string | Hotspot Portal’s value. |
| **portalTheme**  dictionary | Defines the configuration for portal theme. |
| **id**  string | The unique internal identifier of the portal theme. |
| **name**  string | The system- or user-assigned name of the portal theme. |
| **themeData**  string | A CSS file, represented as a Base64-encoded byte array. |
| **portalTweakSettings**  dictionary | The Tweak Settings are a customization of the Portal Theme that has been selected for the portal. When the Portal Theme selection is changed, the Tweak Settings are overwritten to match the values in the theme. The Tweak Settings can subsequently be changed by the user. |
| **bannerColor**  string | Hex value of color. |
| **bannerTextColor**  string | Hotspot Portal’s bannerTextColor. |
| **pageBackgroundColor**  string | Hotspot Portal’s pageBackgroundColor. |
| **pageLabelAndTextColor**  string | Hotspot Portal’s pageLabelAndTextColor. |
| **description**  string | Hotspot Portal’s description. |
| **id**  string | Hotspot Portal’s id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Hotspot Portal’s name. |
| **portalTestUrl**  string | URL to bring up a test page for this portal. |
| **portalType**  string | Allowed values - BYOD, - HOTSPOTGUEST, - MYDEVICE, - SELFREGGUEST, - SPONSOR, - SPONSOREDGUEST. |
| **settings**  dictionary | Defines all of the settings groups available for a BYOD. |
| **aupSettings**  dictionary | Configuration of the Acceptable Use Policy (AUP) for a portal. |
| **accessCode**  string | Access code that must be entered by the portal user (only valid if requireAccessCode = true). |
| **includeAup**  boolean | Require the portal user to read and accept an AUP.  Choices:   - `false` - `true` |
| **requireAccessCode**  boolean | Require the portal user to enter an access code. Only used in Hotspot portal.  Choices:   - `false` - `true` |
| **requireScrolling**  boolean | Require the portal user to scroll to the end of the AUP. Only valid if requireAupAcceptance = true.  Choices:   - `false` - `true` |
| **authSuccessSettings**  dictionary | Hotspot Portal’s authSuccessSettings. |
| **redirectUrl**  string | Target URL for redirection, used when successRedirect = URL. |
| **successRedirect**  string | After an Authentication Success where should device be redirected. Allowed values - AUTHSUCCESSPAGE, - ORIGINATINGURL, - URL. |
| **portalSettings**  dictionary | The port, interface, certificate, and other basic settings of a portal. |
| **allowedInterfaces**  list / elements=string | Interfaces that the portal will be reachable on. Allowed values - eth0 - eth1 - eth2 - eth3 - eth4 - eth5 - bond0 - bond1 - bond2. |
| **alwaysUsedLanguage**  string | Used when displayLang = ALWAYSUSE. |
| **certificateGroupTag**  string | Logical name of the x.509 server certificate that will be used for the portal. |
| **coaType**  string | Allowed Values - COAREAUTHENTICATE, - COATERMINATE. |
| **displayLang**  string | Allowed values - USEBROWSERLOCALE, - ALWAYSUSE. |
| **endpointIdentityGroup**  string | Unique Id of the endpoint identity group where user’s devices will be added. Used only in Hotspot Portal. |
| **fallbackLanguage**  string | Used when displayLang = USEBROWSERLOCALE. |
| **httpsPort**  integer | The port number that the allowed interfaces will listen on. Range from 8000 to 8999. |
| **postAccessBannerSettings**  dictionary | Hotspot Portal’s postAccessBannerSettings. |
| **includePostAccessBanner**  boolean | IncludePostAccessBanner flag.  Choices:   - `false` - `true` |
| **postLoginBannerSettings**  dictionary | Hotspot Portal’s postLoginBannerSettings. |
| **includePostAccessBanner**  boolean | Include a Post-Login Banner page.  Choices:   - `false` - `true` |
| **supportInfoSettings**  dictionary | Portal Support Information Settings. |
| **defaultEmptyFieldValue**  string | The default value displayed for an empty field. Only valid when emptyFieldDisplay = DISPLAYWITHDEFAULTVALUE. |
| **emptyFieldDisplay**  string | Specifies how empty fields are handled on the Support Information Page. Allowed values - HIDE, - DISPLAYWITHNOVALUE, - DISPLAYWITHDEFAULTVALUE. |
| **includeBrowserUserAgent**  boolean | IncludeBrowserUserAgent flag.  Choices:   - `false` - `true` |
| **includeFailureCode**  boolean | IncludeFailureCode flag.  Choices:   - `false` - `true` |
| **includeIpAddress**  boolean | IncludeIpAddress flag.  Choices:   - `false` - `true` |
| **includeMacAddr**  boolean | IncludeMacAddr flag.  Choices:   - `false` - `true` |
| **includePolicyServer**  boolean | IncludePolicyServer flag.  Choices:   - `false` - `true` |
| **includeSupportInfoPage**  boolean | IncludeSupportInfoPage flag.  Choices:   - `false` - `true` |

## [Notes](hotspot_portal_module.md#id4)

> **Note:**
>
> - SDK Method used are hotspot_portal.HotspotPortal.create_hotspot_portal, hotspot_portal.HotspotPortal.delete_hotspot_portal_by_id, hotspot_portal.HotspotPortal.update_hotspot_portal_by_id,
> - Paths used are post /ers/config/hotspotportal, delete /ers/config/hotspotportal/{id}, put /ers/config/hotspotportal/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](hotspot_portal_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.hotspot_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        backgroundImage:
          data: string
        bannerImage:
          data: string
        bannerTitle: string
        contactText: string
        desktopLogoImage:
          data: string
        footerElement: string
        mobileLogoImage:
          data: string
      language:
        viewLanguage: string
      pageCustomizations:
        data:
        - key: string
          value: string
      portalTheme:
        id: string
        name: string
        themeData: string
      portalTweakSettings:
        bannerColor: string
        bannerTextColor: string
        pageBackgroundColor: string
        pageLabelAndTextColor: string
    description: string
    id: string
    name: string
    portalTestUrl: string
    portalType: string
    settings:
      aupSettings:
        accessCode: string
        includeAup: true
        requireAccessCode: true
        requireScrolling: true
      authSuccessSettings:
        redirectUrl: string
        successRedirect: string
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        certificateGroupTag: string
        coaType: string
        displayLang: string
        endpointIdentityGroup: string
        fallbackLanguage: string
        httpsPort: 0
      postAccessBannerSettings:
        includePostAccessBanner: true
      postLoginBannerSettings:
        includePostAccessBanner: true
      supportInfoSettings:
        defaultEmptyFieldValue: string
        emptyFieldDisplay: string
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: true

- name: Delete by id
  cisco.ise.hotspot_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.hotspot_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    customizations:
      globalCustomizations:
        backgroundImage:
          data: string
        bannerImage:
          data: string
        bannerTitle: string
        contactText: string
        desktopLogoImage:
          data: string
        footerElement: string
        mobileLogoImage:
          data: string
      language:
        viewLanguage: string
      pageCustomizations:
        data:
        - key: string
          value: string
      portalTheme:
        id: string
        name: string
        themeData: string
      portalTweakSettings:
        bannerColor: string
        bannerTextColor: string
        pageBackgroundColor: string
        pageLabelAndTextColor: string
    description: string
    name: string
    portalTestUrl: string
    portalType: string
    settings:
      aupSettings:
        accessCode: string
        includeAup: true
        requireAccessCode: true
        requireScrolling: true
      authSuccessSettings:
        redirectUrl: string
        successRedirect: string
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        certificateGroupTag: string
        coaType: string
        displayLang: string
        endpointIdentityGroup: string
        fallbackLanguage: string
        httpsPort: 0
      postAccessBannerSettings:
        includePostAccessBanner: true
      postLoginBannerSettings:
        includePostAccessBanner: true
      supportInfoSettings:
        defaultEmptyFieldValue: string
        emptyFieldDisplay: string
        includeBrowserUserAgent: true
        includeFailureCode: true
        includeIpAddress: true
        includeMacAddr: true
        includePolicyServer: true
        includeSupportInfoPage: true
```

## [Return Values](hotspot_portal_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"customizations": {"globalCustomizations": {"backgroundImage": {"data": "string"}, "bannerImage": {"data": "string"}, "bannerTitle": "string", "contactText": "string", "desktopLogoImage": {"data": "string"}, "footerElement": "string", "mobileLogoImage": {"data": "string"}}, "language": {"viewLanguage": "string"}, "pageCustomizations": {"data": [{"key": "string", "value": "string"}]}, "portalTheme": {"id": "string", "name": "string", "themeData": "string"}, "portalTweakSettings": {"bannerColor": "string", "bannerTextColor": "string", "pageBackgroundColor": "string", "pageLabelAndTextColor": "string"}}, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalTestUrl": "string", "portalType": "string", "settings": {"aupSettings": {"accessCode": "string", "includeAup": true, "requireAccessCode": true, "requireScrolling": true}, "authSuccessSettings": {"redirectUrl": "string", "successRedirect": "string"}, "portalSettings": {"allowedInterfaces": ["string"], "alwaysUsedLanguage": "string", "certificateGroupTag": "string", "coaType": "string", "displayLang": "string", "endpointIdentityGroup": "string", "fallbackLanguage": "string", "httpsPort": 0}, "postAccessBannerSettings": {"includePostAccessBanner": true}, "postLoginBannerSettings": {"includePostAccessBanner": true}, "supportInfoSettings": {"defaultEmptyFieldValue": "string", "emptyFieldDisplay": "string", "includeBrowserUserAgent": true, "includeFailureCode": true, "includeIpAddress": true, "includeMacAddr": true, "includePolicyServer": true, "includeSupportInfoPage": true}}}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
