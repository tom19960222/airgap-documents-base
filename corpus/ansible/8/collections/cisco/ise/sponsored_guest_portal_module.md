---
collection: ansible
version: "8"
title: "cisco.ise.sponsored_guest_portal module – Resource module for Sponsored Guest Portal"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/sponsored_guest_portal_module.html
fetched_at: 2026-07-28T01:31:07+00:00
---
# cisco.ise.sponsored_guest_portal module – Resource module for Sponsored Guest Portal

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
> see [Requirements](sponsored_guest_portal_module.md#ansible-collections-cisco-ise-sponsored-guest-portal-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.sponsored_guest_portal`.

New in cisco.ise 1.0.0

- [Synopsis](sponsored_guest_portal_module.md#synopsis)
- [Requirements](sponsored_guest_portal_module.md#requirements)
- [Parameters](sponsored_guest_portal_module.md#parameters)
- [Notes](sponsored_guest_portal_module.md#notes)
- [Examples](sponsored_guest_portal_module.md#examples)
- [Return Values](sponsored_guest_portal_module.md#return-values)

## [Synopsis](sponsored_guest_portal_module.md#id1)

- Manage operations create, update and delete of the resource Sponsored Guest Portal.
- This API creates a sponsored guest portal.
- This API deletes a sponsored guest portal by ID.
- This API allows the client to update a sponsored guest portal by ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](sponsored_guest_portal_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](sponsored_guest_portal_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **customizations**  dictionary | Defines all of the Portal Customizations available. |
| **globalCustomizations**  dictionary | Sponsored Guest Portal’s globalCustomizations. |
| **backgroundImage**  dictionary | Sponsored Guest Portal’s backgroundImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerImage**  dictionary | Sponsored Guest Portal’s bannerImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerTitle**  string | Sponsored Guest Portal’s bannerTitle. |
| **contactText**  string | Sponsored Guest Portal’s contactText. |
| **desktopLogoImage**  dictionary | Sponsored Guest Portal’s desktopLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **footerElement**  string | Sponsored Guest Portal’s footerElement. |
| **mobileLogoImage**  dictionary | Sponsored Guest Portal’s mobileLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **language**  dictionary | This property is supported only for Read operation and it allows to show the customizations in English. Other languages are not supported. |
| **viewLanguage**  string | Sponsored Guest Portal’s viewLanguage. |
| **pageCustomizations**  dictionary | Represent the entire page customization as a giant dictionary. |
| **data**  list / elements=dictionary | The Dictionary will be exposed here as key value pair. |
| **key**  string | Sponsored Guest Portal’s key. |
| **value**  string | Sponsored Guest Portal’s value. |
| **portalTheme**  dictionary | Sponsored Guest Portal’s portalTheme. |
| **id**  string | Sponsored Guest Portal’s id. |
| **name**  string | The system- or user-assigned name of the portal theme. |
| **themeData**  string | A CSS file, represented as a Base64-encoded byte array. |
| **portalTweakSettings**  dictionary | The Tweak Settings are a customization of the Portal Theme that has been selected for the portal. When the Portal Theme selection is changed, the Tweak Settings are overwritten to match the values in the theme. The Tweak Settings can subsequently be changed by the user. |
| **bannerColor**  string | Hex value of color. |
| **bannerTextColor**  string | Sponsored Guest Portal’s bannerTextColor. |
| **pageBackgroundColor**  string | Sponsored Guest Portal’s pageBackgroundColor. |
| **pageLabelAndTextColor**  string | Sponsored Guest Portal’s pageLabelAndTextColor. |
| **description**  string | Sponsored Guest Portal’s description. |
| **id**  string | Sponsored Guest Portal’s id. |
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
| **name**  string | Sponsored Guest Portal’s name. |
| **portalTestUrl**  string | URL to bring up a test page for this portal. |
| **portalType**  string | Allowed values - BYOD, - HOTSPOTGUEST, - MYDEVICE, - SELFREGGUEST, - SPONSOR, - SPONSOREDGUEST. |
| **settings**  dictionary | Defines all of the settings groups available for a portal. |
| **aupSettings**  dictionary | Sponsored Guest Portal’s aupSettings. |
| **displayFrequency**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed Values - FIRSTLOGIN, - EVERYLOGIN, - RECURRING. |
| **displayFrequencyIntervalDays**  integer | Number of days between AUP confirmations (when displayFrequency = recurring). |
| **includeAup**  boolean | IncludeAup flag.  **Choices:**   - `false` - `true` |
| **requireAupScrolling**  boolean | Require the portal user to scroll to the end of the AUP. Only valid if requireAupAcceptance = true.  **Choices:**   - `false` - `true` |
| **requireScrolling**  boolean | RequireScrolling flag.  **Choices:**   - `false` - `true` |
| **skipAupForEmployees**  boolean | Only valid if requireAupAcceptance = true.  **Choices:**   - `false` - `true` |
| **useDiffAupForEmployees**  boolean | Only valid if requireAupAcceptance = true.  **Choices:**   - `false` - `true` |
| **authSuccessSettings**  dictionary | Sponsored Guest Portal’s authSuccessSettings. |
| **redirectUrl**  string | Target URL for redirection, used when successRedirect = URL. |
| **successRedirect**  string | After an Authentication Success where should device be redirected. Allowed values - AUTHSUCCESSPAGE, - ORIGINATINGURL, - URL. |
| **byodSettings**  dictionary | Sponsored Guest Portal’s byodSettings. |
| **byodRegistrationSettings**  dictionary | Configuration of BYOD endpoint Registration step configuration. |
| **endPointIdentityGroupId**  string | Identity group id for which endpoint belongs. |
| **showDeviceID**  boolean | Display Device ID field during registration.  **Choices:**   - `false` - `true` |
| **byodRegistrationSuccessSettings**  dictionary | Sponsored Guest Portal’s byodRegistrationSuccessSettings. |
| **redirectUrl**  string | Target URL for redirection, used when successRedirect = URL. |
| **successRedirect**  string | After an Authentication Success where should device be redirected. Allowed values - AUTHSUCCESSPAGE, - ORIGINATINGURL, - URL. |
| **byodWelcomeSettings**  dictionary | Sponsored Guest Portal’s byodWelcomeSettings. |
| **aupDisplay**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed values - ONPAGE, - ASLINK. |
| **enableBYOD**  boolean | EnableBYOD flag.  **Choices:**   - `false` - `true` |
| **enableGuestAccess**  boolean | EnableGuestAccess flag.  **Choices:**   - `false` - `true` |
| **includeAup**  boolean | IncludeAup flag.  **Choices:**   - `false` - `true` |
| **requireAupAcceptance**  boolean | RequireAupAcceptance flag.  **Choices:**   - `false` - `true` |
| **requireMDM**  boolean | RequireMDM flag.  **Choices:**   - `false` - `true` |
| **requireScrolling**  boolean | Require BYOD devices to scroll down to the bottom of the AUP. Only valid if includeAup = true.  **Choices:**   - `false` - `true` |
| **guestChangePasswordSettings**  dictionary | Sponsored Guest Portal’s guestChangePasswordSettings. |
| **allowChangePasswdAtFirstLogin**  boolean | Allow guest to change their own passwords.  **Choices:**   - `false` - `true` |
| **guestDeviceRegistrationSettings**  dictionary | Sponsored Guest Portal’s guestDeviceRegistrationSettings. |
| **allowGuestsToRegisterDevices**  boolean | Allow guests to register devices.  **Choices:**   - `false` - `true` |
| **autoRegisterGuestDevices**  boolean | Automatically register guest devices.  **Choices:**   - `false` - `true` |
| **loginPageSettings**  dictionary | Portal Login Page settings groups follow. |
| **accessCode**  string | Access code that must be entered by the portal user (only valid if requireAccessCode = true). |
| **allowAlternateGuestPortal**  boolean | AllowAlternateGuestPortal flag.  **Choices:**   - `false` - `true` |
| **allowForgotPassword**  boolean | AllowForgotPassword flag.  **Choices:**   - `false` - `true` |
| **allowGuestToChangePassword**  boolean | Require the portal user to enter an access code.  **Choices:**   - `false` - `true` |
| **allowGuestToCreateAccounts**  boolean | AllowGuestToCreateAccounts flag.  **Choices:**   - `false` - `true` |
| **aupDisplay**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed values - ONPAGE, - ASLINK. |
| **includeAup**  boolean | Include an Acceptable Use Policy (AUP) that should be displayed during login.  **Choices:**   - `false` - `true` |
| **maxFailedAttemptsBeforeRateLimit**  integer | Maximum failed login attempts before rate limiting. |
| **requireAccessCode**  boolean | RequireAccessCode flag.  **Choices:**   - `false` - `true` |
| **requireAupAcceptance**  boolean | Require the portal user to accept the AUP. Only valid if includeAup = true.  **Choices:**   - `false` - `true` |
| **socialConfigs**  list / elements=dictionary | Sponsored Guest Portal’s socialConfigs. |
| **socialMediaType**  string | Sponsored Guest Portal’s socialMediaType. |
| **socialMediaValue**  string | Sponsored Guest Portal’s socialMediaValue. |
| **timeBetweenLoginsDuringRateLimit**  integer | Time between login attempts when rate limiting. |
| **portalSettings**  dictionary | The port, interface, certificate, and other basic settings of a portal. |
| **allowedInterfaces**  list / elements=string | Interfaces that the portal will be reachable on. Allowed values - eth0, - eth1, - eth2, - eth3, - eth4, - eth5, - bond0, - bond1, - bond2. |
| **alwaysUsedLanguage**  string | Sponsored Guest Portal’s alwaysUsedLanguage. |
| **assignedGuestTypeForEmployee**  string | Unique Id of a guest type. Employees using this portal as a guest inherit login options from the guest type. |
| **authenticationMethod**  string | Unique Id of the identity source sequence. |
| **certificateGroupTag**  string | Logical name of the x.509 server certificate that will be used for the portal. |
| **displayLang**  string | Allowed values - USEBROWSERLOCALE, - ALWAYSUSE. |
| **fallbackLanguage**  string | Used when displayLang = USEBROWSERLOCALE. |
| **httpsPort**  integer | The port number that the allowed interfaces will listen on. Range from 8000 to 8999. |
| **postAccessBannerSettings**  dictionary | Sponsored Guest Portal’s postAccessBannerSettings. |
| **includePostAccessBanner**  boolean | IncludePostAccessBanner flag.  **Choices:**   - `false` - `true` |
| **postLoginBannerSettings**  dictionary | Sponsored Guest Portal’s postLoginBannerSettings. |
| **includePostAccessBanner**  boolean | Include a Post-Login Banner page.  **Choices:**   - `false` - `true` |
| **supportInfoSettings**  dictionary | Sponsored Guest Portal’s supportInfoSettings. |
| **defaultEmptyFieldValue**  string | The default value displayed for an empty field. Only valid when emptyFieldDisplay = DISPLAYWITHDEFAULTVALUE. |
| **emptyFieldDisplay**  string | Specifies how empty fields are handled on the Support Information Page. Allowed values - HIDE, - DISPLAYWITHNOVALUE, - DISPLAYWITHDEFAULTVALUE. |
| **includeBrowserUserAgent**  boolean | IncludeBrowserUserAgent flag.  **Choices:**   - `false` - `true` |
| **includeFailureCode**  boolean | IncludeFailureCode flag.  **Choices:**   - `false` - `true` |
| **includeIpAddress**  boolean | IncludeIpAddress flag.  **Choices:**   - `false` - `true` |
| **includeMacAddr**  boolean | IncludeMacAddr flag.  **Choices:**   - `false` - `true` |
| **includePolicyServer**  boolean | IncludePolicyServer flag.  **Choices:**   - `false` - `true` |
| **includeSupportInfoPage**  boolean | IncludeSupportInfoPage flag.  **Choices:**   - `false` - `true` |

## [Notes](sponsored_guest_portal_module.md#id4)

> **Note:**
>
> - SDK Method used are sponsored_guest_portal.SponsoredGuestPortal.create_sponsored_guest_portal, sponsored_guest_portal.SponsoredGuestPortal.delete_sponsored_guest_portal_by_id, sponsored_guest_portal.SponsoredGuestPortal.update_sponsored_guest_portal_by_id,
> - Paths used are post /ers/config/sponsoredguestportal, delete /ers/config/sponsoredguestportal/{id}, put /ers/config/sponsoredguestportal/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](sponsored_guest_portal_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.sponsored_guest_portal:
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
        displayFrequency: string
        displayFrequencyIntervalDays: 0
        includeAup: true
        requireAupScrolling: true
        requireScrolling: true
        skipAupForEmployees: true
        useDiffAupForEmployees: true
      authSuccessSettings:
        redirectUrl: string
        successRedirect: string
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
      guestChangePasswordSettings:
        allowChangePasswdAtFirstLogin: true
      guestDeviceRegistrationSettings:
        allowGuestsToRegisterDevices: true
        autoRegisterGuestDevices: true
      loginPageSettings:
        accessCode: string
        allowAlternateGuestPortal: true
        allowForgotPassword: true
        allowGuestToChangePassword: true
        allowGuestToCreateAccounts: true
        aupDisplay: string
        includeAup: true
        maxFailedAttemptsBeforeRateLimit: 0
        requireAccessCode: true
        requireAupAcceptance: true
        socialConfigs:
        - socialMediaType: string
          socialMediaValue: string
        timeBetweenLoginsDuringRateLimit: 0
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        assignedGuestTypeForEmployee: string
        authenticationMethod: string
        certificateGroupTag: string
        displayLang: string
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
  cisco.ise.sponsored_guest_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.sponsored_guest_portal:
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
        displayFrequency: string
        displayFrequencyIntervalDays: 0
        includeAup: true
        requireAupScrolling: true
        requireScrolling: true
        skipAupForEmployees: true
        useDiffAupForEmployees: true
      authSuccessSettings:
        redirectUrl: string
        successRedirect: string
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
      guestChangePasswordSettings:
        allowChangePasswdAtFirstLogin: true
      guestDeviceRegistrationSettings:
        allowGuestsToRegisterDevices: true
        autoRegisterGuestDevices: true
      loginPageSettings:
        accessCode: string
        allowAlternateGuestPortal: true
        allowForgotPassword: true
        allowGuestToChangePassword: true
        allowGuestToCreateAccounts: true
        aupDisplay: string
        includeAup: true
        maxFailedAttemptsBeforeRateLimit: 0
        requireAccessCode: true
        requireAupAcceptance: true
        socialConfigs:
        - socialMediaType: string
          socialMediaValue: string
        timeBetweenLoginsDuringRateLimit: 0
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        assignedGuestTypeForEmployee: string
        authenticationMethod: string
        certificateGroupTag: string
        displayLang: string
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

## [Return Values](sponsored_guest_portal_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"customizations": {"globalCustomizations": {"backgroundImage": {"data": "string"}, "bannerImage": {"data": "string"}, "bannerTitle": "string", "contactText": "string", "desktopLogoImage": {"data": "string"}, "footerElement": "string", "mobileLogoImage": {"data": "string"}}, "language": {"viewLanguage": "string"}, "pageCustomizations": {"data": [{"key": "string", "value": "string"}]}, "portalTheme": {"id": "string", "name": "string", "themeData": "string"}, "portalTweakSettings": {"bannerColor": "string", "bannerTextColor": "string", "pageBackgroundColor": "string", "pageLabelAndTextColor": "string"}}, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalTestUrl": "string", "portalType": "string", "settings": {"aupSettings": {"displayFrequency": "string", "displayFrequencyIntervalDays": 0, "includeAup": true, "requireAupScrolling": true, "requireScrolling": true, "skipAupForEmployees": true, "useDiffAupForEmployees": true}, "authSuccessSettings": {"redirectUrl": "string", "successRedirect": "string"}, "byodSettings": {"byodRegistrationSettings": {"endPointIdentityGroupId": "string", "showDeviceID": true}, "byodRegistrationSuccessSettings": {"redirectUrl": "string", "successRedirect": "string"}, "byodWelcomeSettings": {"aupDisplay": "string", "enableBYOD": true, "enableGuestAccess": true, "includeAup": true, "requireAupAcceptance": true, "requireMDM": true, "requireScrolling": true}}, "guestChangePasswordSettings": {"allowChangePasswdAtFirstLogin": true}, "guestDeviceRegistrationSettings": {"allowGuestsToRegisterDevices": true, "autoRegisterGuestDevices": true}, "loginPageSettings": {"accessCode": "string", "allowAlternateGuestPortal": true, "allowForgotPassword": true, "allowGuestToChangePassword": true, "allowGuestToCreateAccounts": true, "aupDisplay": "string", "includeAup": true, "maxFailedAttemptsBeforeRateLimit": 0, "requireAccessCode": true, "requireAupAcceptance": true, "socialConfigs": [{"socialMediaType": "string", "socialMediaValue": "string"}], "timeBetweenLoginsDuringRateLimit": 0}, "portalSettings": {"allowedInterfaces": ["string"], "alwaysUsedLanguage": "string", "assignedGuestTypeForEmployee": "string", "authenticationMethod": "string", "certificateGroupTag": "string", "displayLang": "string", "fallbackLanguage": "string", "httpsPort": 0}, "postAccessBannerSettings": {"includePostAccessBanner": true}, "postLoginBannerSettings": {"includePostAccessBanner": true}, "supportInfoSettings": {"defaultEmptyFieldValue": "string", "emptyFieldDisplay": "string", "includeBrowserUserAgent": true, "includeFailureCode": true, "includeIpAddress": true, "includeMacAddr": true, "includePolicyServer": true, "includeSupportInfoPage": true}}}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
