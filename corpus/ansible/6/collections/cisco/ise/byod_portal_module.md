---
collection: ansible
version: "6"
title: "cisco.ise.byod_portal module – Resource module for BYOD Portal"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/byod_portal_module.html
fetched_at: 2026-07-27T16:56:24+00:00
---
# cisco.ise.byod_portal module – Resource module for BYOD Portal

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
> see [Requirements](byod_portal_module.md#ansible-collections-cisco-ise-byod-portal-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.byod_portal`.

New in cisco.ise 1.0.0

- [Synopsis](byod_portal_module.md#synopsis)
- [Requirements](byod_portal_module.md#requirements)
- [Parameters](byod_portal_module.md#parameters)
- [Notes](byod_portal_module.md#notes)
- [Examples](byod_portal_module.md#examples)
- [Return Values](byod_portal_module.md#return-values)

## [Synopsis](byod_portal_module.md#id1)

- Manage operations create, update and delete of the resource BYOD Portal.
- This API creates a BYOD portal.
- This API deletes a BYOD portal by ID.
- This API allows the client to update a BYOD portal by ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](byod_portal_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](byod_portal_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **customizations**  dictionary | Defines all of the Portal Customizations available for a BYOD. |
| **globalCustomizations**  dictionary | Represent the portal Global customizations. |
| **backgroundImage**  dictionary | BYOD Portal’s backgroundImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerImage**  dictionary | BYOD Portal’s bannerImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerTitle**  string | BYOD Portal’s bannerTitle. |
| **contactText**  string | BYOD Portal’s contactText. |
| **desktopLogoImage**  dictionary | BYOD Portal’s desktopLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **footerElement**  string | BYOD Portal’s footerElement. |
| **mobileLogoImage**  dictionary | BYOD Portal’s mobileLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **language**  dictionary | This property is supported only for Read operation and it allows to show the customizations in English. Other languages are not supported. |
| **viewLanguage**  string | BYOD Portal’s viewLanguage. |
| **pageCustomizations**  dictionary | Represent the entire page customization as a giant dictionary. |
| **data**  list / elements=dictionary | The Dictionary will be exposed here as key value pair. |
| **key**  string | BYOD Portal’s key. |
| **value**  string | BYOD Portal’s value. |
| **portalTheme**  dictionary | Defines the configuration for portal theme. |
| **id**  string | The unique internal identifier of the portal theme. |
| **name**  string | The system- or user-assigned name of the portal theme. |
| **themeData**  string | A CSS file, represented as a Base64-encoded byte array. |
| **portalTweakSettings**  dictionary | The Tweak Settings are a customization of the Portal Theme that has been selected for the portal. When the Portal Theme selection is changed, the Tweak Settings are overwritten to match the values in the theme. The Tweak Settings can subsequently be changed by the user. |
| **bannerColor**  string | Hex value of color. |
| **bannerTextColor**  string | BYOD Portal’s bannerTextColor. |
| **pageBackgroundColor**  string | BYOD Portal’s pageBackgroundColor. |
| **pageLabelAndTextColor**  string | BYOD Portal’s pageLabelAndTextColor. |
| **description**  string | BYOD Portal’s description. |
| **id**  string | Resource UUID, mandatory for update. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | Resource Name. |
| **portalTestUrl**  string | URL to bring up a test page for this portal. |
| **portalType**  string | Allowed values - BYOD, - HOTSPOTGUEST, - MYDEVICE, - SELFREGGUEST, - SPONSOR, - SPONSOREDGUEST. |
| **settings**  dictionary | Defines all of the settings groups available for a BYOD. |
| **byodSettings**  dictionary | Configuration of BYOD Device Welcome, Registration and Success steps. |
| **byodRegistrationSettings**  dictionary | BYOD Portal’s byodRegistrationSettings. |
| **endPointIdentityGroupId**  string | BYOD Portal’s endPointIdentityGroupId. |
| **showDeviceID**  boolean | ShowDeviceID flag.  Choices:   - `false` - `true` |
| **byodRegistrationSuccessSettings**  dictionary | BYOD Portal’s byodRegistrationSuccessSettings. |
| **redirectUrl**  string | Target URL for redirection, used when successRedirect = URL. |
| **successRedirect**  string | After an Authentication Success where should device be redirected. Allowed values. |
| **byodWelcomeSettings**  dictionary | Configuration of BYOD endpoint welcome step configuration. |
| **aupDisplay**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed values - ONPAGE, - ASLINK. |
| **enableBYOD**  boolean | EnableBYOD flag.  Choices:   - `false` - `true` |
| **enableGuestAccess**  boolean | EnableGuestAccess flag.  Choices:   - `false` - `true` |
| **includeAup**  boolean | IncludeAup flag.  Choices:   - `false` - `true` |
| **requireAupAcceptance**  boolean | RequireAupAcceptance flag.  Choices:   - `false` - `true` |
| **requireMDM**  boolean | RequireMDM flag.  Choices:   - `false` - `true` |
| **requireScrolling**  boolean | Require BYOD devices to scroll down to the bottom of the AUP, Only valid if includeAup = true.  Choices:   - `false` - `true` |
| **portalSettings**  dictionary | The port, interface, certificate, and other basic settings of a portal. |
| **allowedInterfaces**  list / elements=string | Interfaces that the portal will be reachable on. Allowed values - eth0, - eth1, - eth2, - eth3, - eth4, - eth5, - bond0, - bond1, - bond2. |
| **alwaysUsedLanguage**  string | Used when displayLang = ALWAYSUSE. |
| **certificateGroupTag**  string | Logical name of the x.509 server certificate that will be used for the portal. |
| **displayLang**  string | Allowed values - USEBROWSERLOCALE, - ALWAYSUSE. |
| **endpointIdentityGroup**  string | Unique Id of the endpoint identity group where user’s devices will be added. Used only in Hotspot Portal. |
| **fallbackLanguage**  string | Used when displayLang = USEBROWSERLOCALE. |
| **httpsPort**  integer | The port number that the allowed interfaces will listen on. Range from 8000 to 8999. |
| **supportInfoSettings**  dictionary | BYOD Portal’s supportInfoSettings. |
| **defaultEmptyFieldValue**  string | The default value displayed for an empty field. Only valid when emptyFieldDisplay = DISPLAYWITHDEFAULTVALUE. |
| **emptyFieldDisplay**  string | Specifies how empty fields are handled on the Support Information Page. Allowed values - HIDE, - DISPLAYWITHNOVALUE, - DISPLAYWITHDEFAULTVALUE. |
| **includeBrowserUserAgent**  boolean | IncludeBrowserUserAgent flag.  Choices:   - `false` - `true` |
| **includeFailureCode**  boolean | IncludeFailureCode flag.  Choices:   - `false` - `true` |
| **includeIpAddress**  boolean | IncludeIpAddress flag.  Choices:   - `false` - `true` |
| **includeMacAddr**  boolean | IncludeMacAddr flag.  Choices:   - `false` - `true` |
| **includePolicyServer**  boolean | IncludePolicyServer flag.  Choices:   - `false` - `true` |
| **includeSupportInfoPage**  boolean | IncludeSupportInfoPage flag.  Choices:   - `false` - `true` |

## [Notes](byod_portal_module.md#id4)

> **Note:**
>
> - SDK Method used are byod_portal.ByodPortal.create_byod_portal, byod_portal.ByodPortal.delete_byod_portal_by_id, byod_portal.ByodPortal.update_byod_portal_by_id,
> - Paths used are post /ers/config/byodportal, delete /ers/config/byodportal/{id}, put /ers/config/byodportal/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](byod_portal_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.byod_portal:
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
      byodSettings:
        byodRegistrationSettings:
          endPointIdentityGroupId: string
          showDeviceID: true
        byodRegistrationSuccessSettings:
          redirectUrl: string
          successRedirect: string
        byodWelcomeSettings:
          aupDisplay: string
          enableBYOD: true
          enableGuestAccess: true
          includeAup: true
          requireAupAcceptance: true
          requireMDM: true
          requireScrolling: true
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        certificateGroupTag: string
        displayLang: string
        endpointIdentityGroup: string
        fallbackLanguage: string
        httpsPort: 0
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
  cisco.ise.byod_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.byod_portal:
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
      byodSettings:
        byodRegistrationSettings:
          endPointIdentityGroupId: string
          showDeviceID: true
        byodRegistrationSuccessSettings:
          redirectUrl: string
          successRedirect: string
        byodWelcomeSettings:
          aupDisplay: string
          enableBYOD: true
          enableGuestAccess: true
          includeAup: true
          requireAupAcceptance: true
          requireMDM: true
          requireScrolling: true
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        certificateGroupTag: string
        displayLang: string
        endpointIdentityGroup: string
        fallbackLanguage: string
        httpsPort: 0
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

## [Return Values](byod_portal_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"customizations": {"globalCustomizations": {"backgroundImage": {"data": "string"}, "bannerImage": {"data": "string"}, "bannerTitle": "string", "contactText": "string", "desktopLogoImage": {"data": "string"}, "footerElement": "string", "mobileLogoImage": {"data": "string"}}, "language": {"viewLanguage": "string"}, "pageCustomizations": {"data": [{"key": "string", "value": "string"}]}, "portalTheme": {"id": "string", "name": "string", "themeData": "string"}, "portalTweakSettings": {"bannerColor": "string", "bannerTextColor": "string", "pageBackgroundColor": "string", "pageLabelAndTextColor": "string"}}, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalTestUrl": "string", "portalType": "string", "settings": {"byodSettings": {"byodRegistrationSettings": {"endPointIdentityGroupId": "string", "showDeviceID": true}, "byodRegistrationSuccessSettings": {"redirectUrl": "string", "successRedirect": "string"}, "byodWelcomeSettings": {"aupDisplay": "string", "enableBYOD": true, "enableGuestAccess": true, "includeAup": true, "requireAupAcceptance": true, "requireMDM": true, "requireScrolling": true}}, "portalSettings": {"allowedInterfaces": ["string"], "alwaysUsedLanguage": "string", "certificateGroupTag": "string", "displayLang": "string", "endpointIdentityGroup": "string", "fallbackLanguage": "string", "httpsPort": 0}, "supportInfoSettings": {"defaultEmptyFieldValue": "string", "emptyFieldDisplay": "string", "includeBrowserUserAgent": true, "includeFailureCode": true, "includeIpAddress": true, "includeMacAddr": true, "includePolicyServer": true, "includeSupportInfoPage": true}}}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
