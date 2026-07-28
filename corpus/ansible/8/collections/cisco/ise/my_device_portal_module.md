---
collection: ansible
version: "8"
title: "cisco.ise.my_device_portal module – Resource module for My Device Portal"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/my_device_portal_module.html
fetched_at: 2026-07-28T01:29:10+00:00
---
# cisco.ise.my_device_portal module – Resource module for My Device Portal

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
> see [Requirements](my_device_portal_module.md#ansible-collections-cisco-ise-my-device-portal-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.my_device_portal`.

New in cisco.ise 1.0.0

- [Synopsis](my_device_portal_module.md#synopsis)
- [Requirements](my_device_portal_module.md#requirements)
- [Parameters](my_device_portal_module.md#parameters)
- [Notes](my_device_portal_module.md#notes)
- [Examples](my_device_portal_module.md#examples)
- [Return Values](my_device_portal_module.md#return-values)

## [Synopsis](my_device_portal_module.md#id1)

- Manage operations create, update and delete of the resource My Device Portal.
- This API creates a my device portal.
- This API deletes a my device portal by ID.
- This API allows the client to update a my device portal by ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](my_device_portal_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](my_device_portal_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **customizations**  dictionary | Defines all of the Portal Customizations available. |
| **globalCustomizations**  dictionary | My Device Portal’s globalCustomizations. |
| **backgroundImage**  dictionary | My Device Portal’s backgroundImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerImage**  dictionary | My Device Portal’s bannerImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerTitle**  string | My Device Portal’s bannerTitle. |
| **contactText**  string | My Device Portal’s contactText. |
| **desktopLogoImage**  dictionary | My Device Portal’s desktopLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **footerElement**  string | My Device Portal’s footerElement. |
| **mobileLogoImage**  dictionary | My Device Portal’s mobileLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **language**  dictionary | This property is supported only for Read operation and it allows to show the customizations in English. Other languages are not supported. |
| **viewLanguage**  string | My Device Portal’s viewLanguage. |
| **pageCustomizations**  dictionary | Represent the entire page customization as a giant dictionary. |
| **data**  list / elements=dictionary | The Dictionary will be exposed here as key value pair. |
| **key**  string | My Device Portal’s key. |
| **value**  string | My Device Portal’s value. |
| **portalTheme**  dictionary | My Device Portal’s portalTheme. |
| **id**  string | My Device Portal’s id. |
| **name**  string | The system- or user-assigned name of the portal theme. |
| **themeData**  string | A CSS file, represented as a Base64-encoded byte array. |
| **portalTweakSettings**  dictionary | The Tweak Settings are a customization of the Portal Theme that has been selected for the portal. When the Portal Theme selection is changed, the Tweak Settings are overwritten to match the values in the theme. The Tweak Settings can subsequently be changed by the user. |
| **bannerColor**  string | Hex value of color. |
| **bannerTextColor**  string | My Device Portal’s bannerTextColor. |
| **pageBackgroundColor**  string | My Device Portal’s pageBackgroundColor. |
| **pageLabelAndTextColor**  string | My Device Portal’s pageLabelAndTextColor. |
| **description**  string | My Device Portal’s description. |
| **id**  string | My Device Portal’s id. |
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
| **name**  string | My Device Portal’s name. |
| **portalTestUrl**  string | URL to bring up a test page for this portal. |
| **portalType**  string | Allowed values - BYOD, - HOTSPOTGUEST, - MYDEVICE, - SELFREGGUEST, - SPONSOR, - SPONSOREDGUEST. |
| **settings**  dictionary | Defines all of the settings groups available for a Mydevice portal. |
| **aupSettings**  dictionary | Configuration of the Acceptable Use Policy (AUP) for a portal. |
| **displayFrequency**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed Values - FIRSTLOGIN, - EVERYLOGIN, - RECURRING. |
| **displayFrequencyIntervalDays**  integer | Number of days between AUP confirmations (when displayFrequency = recurring). |
| **includeAup**  boolean | Require the portal user to read and accept an AUP.  **Choices:**   - `false` - `true` |
| **requireScrolling**  boolean | Require the portal user to scroll to the end of the AUP. Only valid if requireAupAcceptance = true.  **Choices:**   - `false` - `true` |
| **employeeChangePasswordSettings**  dictionary | My Device Portal’s employeeChangePasswordSettings. |
| **allowEmployeeToChangePwd**  boolean | AllowEmployeeToChangePwd flag.  **Choices:**   - `false` - `true` |
| **loginPageSettings**  dictionary | My Device Portal’s loginPageSettings. |
| **aupDisplay**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed values - ONPAGE, - ASLINK. |
| **includeAup**  boolean | Include an Acceptable Use Policy (AUP) that should be displayed during login.  **Choices:**   - `false` - `true` |
| **maxFailedAttemptsBeforeRateLimit**  integer | Maximum failed login attempts before rate limiting. |
| **requireAupAcceptance**  boolean | Require the portal user to accept the AUP. Only valid if includeAup = true.  **Choices:**   - `false` - `true` |
| **requireScrolling**  boolean | Require the portal user to scroll to the end of the AUP. Only valid if requireAupAcceptance = true.  **Choices:**   - `false` - `true` |
| **socialConfigs**  list / elements=dictionary | My Device Portal’s socialConfigs. |
| **timeBetweenLoginsDuringRateLimit**  integer | Time between login attempts when rate limiting. |
| **portalSettings**  dictionary | The port, interface, certificate, and other basic settings of a portal. |
| **allowedInterfaces**  list / elements=string | Interfaces that the portal will be reachable on. Allowed values - eth0, - eth1, - eth2, - eth3, - eth4, - eth5, - bond0, - bond1, - bond2. |
| **alwaysUsedLanguage**  string | My Device Portal’s alwaysUsedLanguage. |
| **certificateGroupTag**  string | Logical name of the x.509 server certificate that will be used for the portal. |
| **displayLang**  string | Allowed values - USEBROWSERLOCALE, - ALWAYSUSE. |
| **endpointIdentityGroup**  string | Unique Id of the endpoint identity group where user’s devices will be added. Used only in Hotspot Portal. |
| **fallbackLanguage**  string | Used when displayLang = USEBROWSERLOCALE. |
| **httpsPort**  integer | The port number that the allowed interfaces will listen on. Range from 8000 to 8999. |
| **postAccessBannerSettings**  dictionary | My Device Portal’s postAccessBannerSettings. |
| **includePostAccessBanner**  boolean | IncludePostAccessBanner flag.  **Choices:**   - `false` - `true` |
| **postLoginBannerSettings**  dictionary | My Device Portal’s postLoginBannerSettings. |
| **includePostAccessBanner**  boolean | Include a Post-Login Banner page.  **Choices:**   - `false` - `true` |
| **supportInfoSettings**  dictionary | My Device Portal’s supportInfoSettings. |
| **defaultEmptyFieldValue**  string | The default value displayed for an empty field. Only valid when emptyFieldDisplay = DISPLAYWITHDEFAULTVALUE. |
| **emptyFieldDisplay**  string | Specifies how empty fields are handled on the Support Information Page. Allowed values - HIDE, - DISPLAYWITHNOVALUE, - DISPLAYWITHDEFAULTVALUE. |
| **includeBrowserUserAgent**  boolean | IncludeBrowserUserAgent flag.  **Choices:**   - `false` - `true` |
| **includeFailureCode**  boolean | IncludeFailureCode flag.  **Choices:**   - `false` - `true` |
| **includeIpAddress**  boolean | IncludeIpAddress flag.  **Choices:**   - `false` - `true` |
| **includeMacAddr**  boolean | IncludeMacAddr flag.  **Choices:**   - `false` - `true` |
| **includePolicyServer**  boolean | IncludePolicyServer flag.  **Choices:**   - `false` - `true` |
| **includeSupportInfoPage**  boolean | IncludeSupportInfoPage flag.  **Choices:**   - `false` - `true` |

## [Notes](my_device_portal_module.md#id4)

> **Note:**
>
> - SDK Method used are my_device_portal.MyDevicePortal.create_my_device_portal, my_device_portal.MyDevicePortal.delete_my_device_portal_by_id, my_device_portal.MyDevicePortal.update_my_device_portal_by_id,
> - Paths used are post /ers/config/mydeviceportal, delete /ers/config/mydeviceportal/{id}, put /ers/config/mydeviceportal/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](my_device_portal_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.my_device_portal:
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
        requireScrolling: true
      employeeChangePasswordSettings:
        allowEmployeeToChangePwd: true
      loginPageSettings:
        aupDisplay: string
        includeAup: true
        maxFailedAttemptsBeforeRateLimit: 0
        requireAupAcceptance: true
        requireScrolling: true
        socialConfigs:
        - {}
        timeBetweenLoginsDuringRateLimit: 0
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        certificateGroupTag: string
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
  cisco.ise.my_device_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.my_device_portal:
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
        requireScrolling: true
      employeeChangePasswordSettings:
        allowEmployeeToChangePwd: true
      loginPageSettings:
        aupDisplay: string
        includeAup: true
        maxFailedAttemptsBeforeRateLimit: 0
        requireAupAcceptance: true
        requireScrolling: true
        socialConfigs:
        - {}
        timeBetweenLoginsDuringRateLimit: 0
      portalSettings:
        allowedInterfaces:
        - string
        alwaysUsedLanguage: string
        certificateGroupTag: string
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

## [Return Values](my_device_portal_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"customizations": {"globalCustomizations": {"backgroundImage": {"data": "string"}, "bannerImage": {"data": "string"}, "bannerTitle": "string", "contactText": "string", "desktopLogoImage": {"data": "string"}, "footerElement": "string", "mobileLogoImage": {"data": "string"}}, "language": {"viewLanguage": "string"}, "pageCustomizations": {"data": [{"key": "string", "value": "string"}]}, "portalTheme": {"id": "string", "name": "string", "themeData": "string"}, "portalTweakSettings": {"bannerColor": "string", "bannerTextColor": "string", "pageBackgroundColor": "string", "pageLabelAndTextColor": "string"}}, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalTestUrl": "string", "portalType": "string", "settings": {"aupSettings": {"displayFrequency": "string", "displayFrequencyIntervalDays": 0, "includeAup": true, "requireScrolling": true}, "employeeChangePasswordSettings": {"allowEmployeeToChangePwd": true}, "loginPageSettings": {"aupDisplay": "string", "includeAup": true, "maxFailedAttemptsBeforeRateLimit": 0, "requireAupAcceptance": true, "requireScrolling": true, "socialConfigs": [{}], "timeBetweenLoginsDuringRateLimit": 0}, "portalSettings": {"allowedInterfaces": ["string"], "alwaysUsedLanguage": "string", "certificateGroupTag": "string", "displayLang": "string", "endpointIdentityGroup": "string", "fallbackLanguage": "string", "httpsPort": 0}, "postAccessBannerSettings": {"includePostAccessBanner": true}, "postLoginBannerSettings": {"includePostAccessBanner": true}, "supportInfoSettings": {"defaultEmptyFieldValue": "string", "emptyFieldDisplay": "string", "includeBrowserUserAgent": true, "includeFailureCode": true, "includeIpAddress": true, "includeMacAddr": true, "includePolicyServer": true, "includeSupportInfoPage": true}}}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
