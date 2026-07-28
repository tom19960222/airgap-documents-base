---
collection: ansible
version: "8"
title: "cisco.ise.self_registered_portal module – Resource module for Self Registered Portal"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/self_registered_portal_module.html
fetched_at: 2026-07-28T01:30:40+00:00
---
# cisco.ise.self_registered_portal module – Resource module for Self Registered Portal

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
> see [Requirements](self_registered_portal_module.md#ansible-collections-cisco-ise-self-registered-portal-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.self_registered_portal`.

New in cisco.ise 1.0.0

- [Synopsis](self_registered_portal_module.md#synopsis)
- [Requirements](self_registered_portal_module.md#requirements)
- [Parameters](self_registered_portal_module.md#parameters)
- [Notes](self_registered_portal_module.md#notes)
- [See Also](self_registered_portal_module.md#see-also)
- [Examples](self_registered_portal_module.md#examples)
- [Return Values](self_registered_portal_module.md#return-values)

## [Synopsis](self_registered_portal_module.md#id1)

- Manage operations create, update and delete of the resource Self Registered Portal.
- This API creates a self registered portal.
- This API deletes a self registered portal by ID.
- This API allows the client to update a self registered portal by ID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](self_registered_portal_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](self_registered_portal_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **customizations**  dictionary | Defines all of the Portal Customizations available. |
| **globalCustomizations**  dictionary | Self Registered Portal’s globalCustomizations. |
| **backgroundImage**  dictionary | Self Registered Portal’s backgroundImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerImage**  dictionary | Self Registered Portal’s bannerImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **bannerTitle**  string | Self Registered Portal’s bannerTitle. |
| **contactText**  string | Self Registered Portal’s contactText. |
| **desktopLogoImage**  dictionary | Self Registered Portal’s desktopLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **footerElement**  string | Self Registered Portal’s footerElement. |
| **mobileLogoImage**  dictionary | Self Registered Portal’s mobileLogoImage. |
| **data**  string | Represented as base 64 encoded string of the image byte array. |
| **language**  dictionary | This property is supported only for Read operation and it allows to show the customizations in English. Other languages are not supported. |
| **viewLanguage**  string | Self Registered Portal’s viewLanguage. |
| **pageCustomizations**  dictionary | Represent the entire page customization as a giant dictionary. |
| **data**  list / elements=dictionary | The Dictionary will be exposed here as key value pair. |
| **key**  string | Self Registered Portal’s key. |
| **value**  string | Self Registered Portal’s value. |
| **portalTheme**  dictionary | Self Registered Portal’s portalTheme. |
| **id**  string | Self Registered Portal’s id. |
| **name**  string | The system- or user-assigned name of the portal theme. |
| **themeData**  string | A CSS file, represented as a Base64-encoded byte array. |
| **portalTweakSettings**  dictionary | The Tweak Settings are a customization of the Portal Theme that has been selected for the portal. When the Portal Theme selection is changed, the Tweak Settings are overwritten to match the values in the theme. The Tweak Settings can subsequently be changed by the user. |
| **bannerColor**  string | Hex value of color. |
| **bannerTextColor**  string | Self Registered Portal’s bannerTextColor. |
| **pageBackgroundColor**  string | Self Registered Portal’s pageBackgroundColor. |
| **pageLabelAndTextColor**  string | Self Registered Portal’s pageLabelAndTextColor. |
| **description**  string | Self Registered Portal’s description. |
| **id**  string | Self Registered Portal’s id. |
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
| **name**  string | Self Registered Portal’s name. |
| **portalTestUrl**  string | URL to bring up a test page for this portal. |
| **portalType**  string | Allowed values - BYOD, - HOTSPOTGUEST, - MYDEVICE, - SELFREGGUEST, - SPONSOR, - SPONSOREDGUEST. |
| **settings**  dictionary | Defines all of the settings groups available for a portal. |
| **aupSettings**  dictionary | Self Registered Portal’s aupSettings. |
| **displayFrequency**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed Values - FIRSTLOGIN, - EVERYLOGIN, - RECURRING. |
| **displayFrequencyIntervalDays**  integer | Number of days between AUP confirmations (when displayFrequency = recurring). |
| **includeAup**  boolean | Require the portal user to read and accept an AUP.  **Choices:**   - `false` - `true` |
| **requireAupScrolling**  boolean | Require the portal user to scroll to the end of the AUP. Only valid if requireAupAcceptance = true.  **Choices:**   - `false` - `true` |
| **requireScrolling**  boolean | RequireScrolling flag.  **Choices:**   - `false` - `true` |
| **skipAupForEmployees**  boolean | Only valid if requireAupAcceptance = trueG.  **Choices:**   - `false` - `true` |
| **useDiffAupForEmployees**  boolean | Only valid if requireAupAcceptance = trueG.  **Choices:**   - `false` - `true` |
| **authSuccessSettings**  dictionary | Self Registered Portal’s authSuccessSettings. |
| **redirectUrl**  string | Self Registered Portal’s redirectUrl. |
| **successRedirect**  string | Self Registered Portal’s successRedirect. |
| **byodSettings**  dictionary | Configuration of BYOD Device Welcome, Registration and Success steps. |
| **byodRegistrationSettings**  dictionary | Configuration of BYOD endpoint Registration step configuration. |
| **endPointIdentityGroupId**  string | Identity group id for which endpoint belongs. |
| **showDeviceID**  boolean | Display Device ID field during registration.  **Choices:**   - `false` - `true` |
| **byodRegistrationSuccessSettings**  dictionary | Configuration of BYOD endpoint Registration Success step configuration. |
| **redirectUrl**  string | Target URL for redirection, used when successRedirect = URL. |
| **successRedirect**  string | After an Authentication Success where should device be redirected. Allowed values - AUTHSUCCESSPAGE, - ORIGINATINGURL, - URL. |
| **byodWelcomeSettings**  dictionary | Configuration of BYOD endpoint welcome step configuration. |
| **aupDisplay**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed values - ONPAGE, - ASLINK. |
| **enableBYOD**  boolean | EnableBYOD flag.  **Choices:**   - `false` - `true` |
| **enableGuestAccess**  boolean | EnableGuestAccess flag.  **Choices:**   - `false` - `true` |
| **includeAup**  boolean | IncludeAup flag.  **Choices:**   - `false` - `true` |
| **requireAupAcceptance**  boolean | RequireAupAcceptance flag.  **Choices:**   - `false` - `true` |
| **requireMDM**  boolean | RequireMDM flag.  **Choices:**   - `false` - `true` |
| **requireScrolling**  boolean | Require BYOD devices to scroll down to the bottom of the AUP, Only valid if includeAup = true.  **Choices:**   - `false` - `true` |
| **guestChangePasswordSettings**  dictionary | Self Registered Portal’s guestChangePasswordSettings. |
| **allowChangePasswdAtFirstLogin**  boolean | Allow guest to change their own passwords.  **Choices:**   - `false` - `true` |
| **guestDeviceRegistrationSettings**  dictionary | Self Registered Portal’s guestDeviceRegistrationSettings. |
| **allowGuestsToRegisterDevices**  boolean | Allow guests to register devices.  **Choices:**   - `false` - `true` |
| **autoRegisterGuestDevices**  boolean | Automatically register guest devices.  **Choices:**   - `false` - `true` |
| **loginPageSettings**  dictionary | Portal Login Page settings groups follow. |
| **accessCode**  string | Access code that must be entered by the portal user (only valid if requireAccessCode = true). |
| **allowAlternateGuestPortal**  boolean | AllowAlternateGuestPortal flag.  **Choices:**   - `false` - `true` |
| **allowForgotPassword**  boolean | AllowForgotPassword flag.  **Choices:**   - `false` - `true` |
| **allowGuestToChangePassword**  boolean | Require the portal user to enter an access code.  **Choices:**   - `false` - `true` |
| **allowGuestToCreateAccounts**  boolean | AllowGuestToCreateAccounts flag.  **Choices:**   - `false` - `true` |
| **allowGuestToUseSocialAccounts**  boolean | AllowGuestToUseSocialAccounts flag.  **Choices:**   - `false` - `true` |
| **allowShowGuestForm**  boolean | AllowShowGuestForm flag.  **Choices:**   - `false` - `true` |
| **alternateGuestPortal**  string | Self Registered Portal’s alternateGuestPortal. |
| **aupDisplay**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed values - ONPAGE, - ASLINK. |
| **includeAup**  boolean | Include an Acceptable Use Policy (AUP) that should be displayed during login.  **Choices:**   - `false` - `true` |
| **maxFailedAttemptsBeforeRateLimit**  integer | Maximum failed login attempts before rate limiting. |
| **requireAccessCode**  boolean | Require the portal user to enter an access code.  **Choices:**   - `false` - `true` |
| **requireAupAcceptance**  boolean | Require the portal user to accept the AUP. Only valid if includeAup = true.  **Choices:**   - `false` - `true` |
| **socialConfigs**  list / elements=dictionary | Self Registered Portal’s socialConfigs. |
| **socialMediaType**  string | Self Registered Portal’s socialMediaType. |
| **socialMediaValue**  string | Self Registered Portal’s socialMediaValue. |
| **timeBetweenLoginsDuringRateLimit**  integer | Time between login attempts when rate limiting. |
| **portalSettings**  dictionary | The port, interface, certificate, and other basic settings of a portal. |
| **allowedInterfaces**  list / elements=string | Interfaces that the portal will be reachable on. Allowed values - eth0, - eth1, - eth2, - eth3, - eth4, - eth5, - bond0, - bond1, - bond2. |
| **alwaysUsedLanguage**  string | Self Registered Portal’s alwaysUsedLanguage. |
| **assignedGuestTypeForEmployee**  string | Unique Id of a guest type. Employees using this portal as a guest inherit login options from the guest type. |
| **authenticationMethod**  string | Unique Id of the identity source sequence. |
| **certificateGroupTag**  string | Logical name of the x.509 server certificate that will be used for the portal. |
| **displayLang**  string | Allowed values - USEBROWSERLOCALE, - ALWAYSUSE. |
| **fallbackLanguage**  string | Used when displayLang = USEBROWSERLOCALE. |
| **httpsPort**  integer | The port number that the allowed interfaces will listen on. Range from 8000 to 8999. |
| **postAccessBannerSettings**  dictionary | Self Registered Portal’s postAccessBannerSettings. |
| **includePostAccessBanner**  boolean | IncludePostAccessBanner flag.  **Choices:**   - `false` - `true` |
| **postLoginBannerSettings**  dictionary | Self Registered Portal’s postLoginBannerSettings. |
| **includePostAccessBanner**  boolean | Include a Post-Login Banner page.  **Choices:**   - `false` - `true` |
| **selfRegPageSettings**  dictionary | Self Registered Portal’s selfRegPageSettings. |
| **accountValidityDuration**  integer | Self-registered guest account is valid for this many account_validity_time_units. |
| **accountValidityTimeUnits**  string | Time units for account_validity_duration. Allowed Values - DAYS, - HOURS, - MINUTES. |
| **allowGraceAccess**  boolean | AllowGraceAccess flag.  **Choices:**   - `false` - `true` |
| **approvalEmailAddresses**  string | Only valid if requireGuestApproval = true and sendApprovalRequestTo = SELECTEDEMAILADDRESSES. |
| **approveDenyLinksTimeUnits**  string | This attribute, along with approveDenyLinksValidFor, specifies how long the link can be used. Only valid if requireGuestApproval = true. Allowed Values - DAYS, - HOURS, - MINUTES. |
| **approveDenyLinksValidFor**  integer | This attribute, along with approveDenyLinksTimeUnits, specifies how long the link can be used. Only valid if requireGuestApproval = true. |
| **assignGuestsToGuestType**  string | Guests are assigned to this guest type. |
| **aupDisplay**  string | How the AUP should be displayed, either on page or as a link. Only valid if includeAup = true. Allowed values - ONPAGE, - ASLINK. |
| **authenticateSponsorsUsingPortalList**  boolean | AuthenticateSponsorsUsingPortalList flag.  **Choices:**   - `false` - `true` |
| **autoLoginSelfWait**  boolean | Allow guests to login automatically from self-registration after sponsor’s approval. No need to provide the credentials by guest to login.  **Choices:**   - `false` - `true` |
| **autoLoginTimePeriod**  integer | Waiting period for auto login until sponsor’s approval. If time exceeds, guest has to login manually by providing the credentials. Default value is 5 minutes. |
| **credentialNotificationUsingEmail**  boolean | If true, send credential notification upon approval using email. Only valid if requireGuestApproval = true.  **Choices:**   - `false` - `true` |
| **credentialNotificationUsingSMS**  boolean | If true, send credential notification upon approval using SMS. Only valid if requireGuestApproval = true.  **Choices:**   - `false` - `true` |
| **enableGuestEmailBlacklist**  boolean | Disallow guests with an e-mail address from selected domains.  **Choices:**   - `false` - `true` |
| **enableGuestEmailWhitelist**  boolean | Allow guests with an e-mail address from selected domains.  **Choices:**   - `false` - `true` |
| **fieldCompany**  dictionary | Self Registered Portal’s fieldCompany. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldEmailAddr**  dictionary | Self Registered Portal’s fieldEmailAddr. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldFirstName**  dictionary | Self Registered Portal’s fieldFirstName. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldLastName**  dictionary | Self Registered Portal’s fieldLastName. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldLocation**  dictionary | Self Registered Portal’s fieldLocation. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldPersonBeingVisited**  dictionary | Self Registered Portal’s fieldPersonBeingVisited. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldPhoneNo**  dictionary | Self Registered Portal’s fieldPhoneNo. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldReasonForVisit**  dictionary | Self Registered Portal’s fieldReasonForVisit. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldSMSProvider**  dictionary | Self Registered Portal’s fieldSMSProvider. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **fieldUserName**  dictionary | Self Registered Portal’s fieldUserName. |
| **include**  boolean | Include flag.  **Choices:**   - `false` - `true` |
| **require**  boolean | Only applicable if include = true.  **Choices:**   - `false` - `true` |
| **graceAccessExpireInterval**  integer | Self Registered Portal’s graceAccessExpireInterval. |
| **graceAccessSendAccountExpiration**  boolean | GraceAccessSendAccountExpiration flag.  **Choices:**   - `false` - `true` |
| **guestEmailBlacklistDomains**  list / elements=string | Disallow guests with an e-mail address from selected domains. |
| **guestEmailWhitelistDomains**  list / elements=string | Self-registered guests whose e-mail address is in one of these domains will be allowed. Only valid if enableGuestEmailWhitelist = true. |
| **includeAup**  boolean | Include an Acceptable Use Policy (AUP) that should be displayed during login.  **Choices:**   - `false` - `true` |
| **postRegistrationRedirect**  string | After the registration submission direct the guest user to one of the following pages. Only valid if requireGuestApproval = true. Allowed Values - SELFREGISTRATIONSUCCESS, - LOGINPAGEWITHINSTRUCTIONS - URL. |
| **postRegistrationRedirectUrl**  string | URL where guest user is redirected after registration. Only valid if requireGuestApproval = true and postRegistrationRedirect = URL. |
| **registrationCode**  string | The registration code that the guest user must enter. |
| **requireApproverToAuthenticate**  boolean | When self-registered guests require approval, an approval request is e-mailed to one or more sponsor users. If the Cisco ISE Administrator chooses to include an approval link in the e-mail, a sponsor user who clicks the link will be required to enter their username and password if this attribute is true. Only valid if requireGuestApproval = true.  **Choices:**   - `false` - `true` |
| **requireAupAcceptance**  boolean | Require the portal user to accept the AUP. Only valid if includeAup = true.  **Choices:**   - `false` - `true` |
| **requireGuestApproval**  boolean | Require self-registered guests to be approved if true.  **Choices:**   - `false` - `true` |
| **requireRegistrationCode**  boolean | Self-registered guests are required to enter a registration code.  **Choices:**   - `false` - `true` |
| **selectableLocations**  list / elements=string | Guests can choose from these locations to set their time zone. |
| **selectableSMSProviders**  list / elements=string | This attribute is an array of SMS provider names. |
| **sendApprovalRequestTo**  string | Specifies where approval requests are sent. Only valid if requireGuestApproval = true. Allowed Values - SELECTEDEMAILADDRESSES, - PERSONBEINGVISITED. |
| **sponsorPortalList**  list / elements=string | Self Registered Portal’s sponsorPortalList. |
| **selfRegSuccessSettings**  dictionary | Self Registered Portal’s selfRegSuccessSettings. |
| **allowGuestLoginFromSelfregSuccessPage**  boolean | AllowGuestLoginFromSelfregSuccessPage flag.  **Choices:**   - `false` - `true` |
| **allowGuestSendSelfUsingEmail**  boolean | AllowGuestSendSelfUsingEmail flag.  **Choices:**   - `false` - `true` |
| **allowGuestSendSelfUsingPrint**  boolean | AllowGuestSendSelfUsingPrint flag.  **Choices:**   - `false` - `true` |
| **allowGuestSendSelfUsingSMS**  boolean | AllowGuestSendSelfUsingSMS flag.  **Choices:**   - `false` - `true` |
| **aupOnPage**  boolean | AupOnPage flag.  **Choices:**   - `false` - `true` |
| **includeAup**  boolean | IncludeAup flag.  **Choices:**   - `false` - `true` |
| **includeCompany**  boolean | IncludeCompany flag.  **Choices:**   - `false` - `true` |
| **includeEmailAddr**  boolean | IncludeEmailAddr flag.  **Choices:**   - `false` - `true` |
| **includeFirstName**  boolean | IncludeFirstName flag.  **Choices:**   - `false` - `true` |
| **includeLastName**  boolean | IncludeLastName flag.  **Choices:**   - `false` - `true` |
| **includeLocation**  boolean | IncludeLocation flag.  **Choices:**   - `false` - `true` |
| **includePassword**  boolean | IncludePassword flag.  **Choices:**   - `false` - `true` |
| **includePersonBeingVisited**  boolean | IncludePersonBeingVisited flag.  **Choices:**   - `false` - `true` |
| **includePhoneNo**  boolean | IncludePhoneNo flag.  **Choices:**   - `false` - `true` |
| **includeReasonForVisit**  boolean | IncludeReasonForVisit flag.  **Choices:**   - `false` - `true` |
| **includeSMSProvider**  boolean | IncludeSMSProvider flag.  **Choices:**   - `false` - `true` |
| **includeUserName**  boolean | IncludeUserName flag.  **Choices:**   - `false` - `true` |
| **requireAupAcceptance**  boolean | RequireAupAcceptance flag.  **Choices:**   - `false` - `true` |
| **requireAupScrolling**  boolean | RequireAupScrolling flag.  **Choices:**   - `false` - `true` |
| **supportInfoSettings**  dictionary | Self Registered Portal’s supportInfoSettings. |
| **defaultEmptyFieldValue**  string | The default value displayed for an empty field. Only valid when emptyFieldDisplay = DISPLAYWITHDEFAULTVALUE. |
| **emptyFieldDisplay**  string | Specifies how empty fields are handled on the Support Information Page. Allowed values - HIDE, - DISPLAYWITHNOVALUE, - DISPLAYWITHDEFAULTVALUE. |
| **includeBrowserUserAgent**  boolean | IncludeBrowserUserAgent flag.  **Choices:**   - `false` - `true` |
| **includeFailureCode**  boolean | IncludeFailureCode flag.  **Choices:**   - `false` - `true` |
| **includeIpAddress**  boolean | IncludeIpAddress flag.  **Choices:**   - `false` - `true` |
| **includeMacAddr**  boolean | IncludeMacAddr flag.  **Choices:**   - `false` - `true` |
| **includePolicyServer**  boolean | IncludePolicyServer flag.  **Choices:**   - `false` - `true` |
| **includeSupportInfoPage**  boolean | IncludeSupportInfoPage flag.  **Choices:**   - `false` - `true` |

## [Notes](self_registered_portal_module.md#id4)

> **Note:**
>
> - SDK Method used are self_registered_portal.SelfRegisteredPortal.create_self_registered_portal, self_registered_portal.SelfRegisteredPortal.delete_self_registered_portal_by_id, self_registered_portal.SelfRegisteredPortal.update_self_registered_portal_by_id,
> - Paths used are post /ers/config/selfregportal, delete /ers/config/selfregportal/{id}, put /ers/config/selfregportal/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](self_registered_portal_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for SelfRegisteredPortal](https://developer.cisco.com/docs/identity-services-engine/v1/#!selfregportal)
> :   Complete reference of the SelfRegisteredPortal API.

## [Examples](self_registered_portal_module.md#id6)

```yaml+jinja
- name: Update by id
  cisco.ise.self_registered_portal:
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
        allowGuestToUseSocialAccounts: true
        allowShowGuestForm: true
        alternateGuestPortal: string
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
      selfRegPageSettings:
        accountValidityDuration: 0
        accountValidityTimeUnits: string
        allowGraceAccess: true
        approvalEmailAddresses: string
        approveDenyLinksTimeUnits: string
        approveDenyLinksValidFor: 0
        assignGuestsToGuestType: string
        aupDisplay: string
        authenticateSponsorsUsingPortalList: true
        autoLoginSelfWait: true
        autoLoginTimePeriod: 0
        credentialNotificationUsingEmail: true
        credentialNotificationUsingSms: true
        enableGuestEmailBlacklist: true
        enableGuestEmailWhitelist: true
        fieldCompany:
          include: true
          require: true
        fieldEmailAddr:
          include: true
          require: true
        fieldFirstName:
          include: true
          require: true
        fieldLastName:
          include: true
          require: true
        fieldLocation:
          include: true
          require: true
        fieldPersonBeingVisited:
          include: true
          require: true
        fieldPhoneNo:
          include: true
          require: true
        fieldReasonForVisit:
          include: true
          require: true
        fieldSmsProvider:
          include: true
          require: true
        fieldUserName:
          include: true
          require: true
        graceAccessExpireInterval: 0
        graceAccessSendAccountExpiration: true
        guestEmailBlacklistDomains:
        - string
        guestEmailWhitelistDomains:
        - string
        includeAup: true
        postRegistrationRedirect: string
        postRegistrationRedirectUrl: string
        registrationCode: string
        requireApproverToAuthenticate: true
        requireAupAcceptance: true
        requireGuestApproval: true
        requireRegistrationCode: true
        selectableLocations:
        - string
        selectableSmsProviders:
        - string
        sendApprovalRequestTo: string
        sponsorPortalList:
        - string
      selfRegSuccessSettings:
        allowGuestLoginFromSelfregSuccessPage: true
        allowGuestSendSelfUsingEmail: true
        allowGuestSendSelfUsingPrint: true
        allowGuestSendSelfUsingSms: true
        aupOnPage: true
        includeAup: true
        includeCompany: true
        includeEmailAddr: true
        includeFirstName: true
        includeLastName: true
        includeLocation: true
        includePassword: true
        includePersonBeingVisited: true
        includePhoneNo: true
        includeReasonForVisit: true
        includeSmsProvider: true
        includeUserName: true
        requireAupAcceptance: true
        requireAupScrolling: true
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
  cisco.ise.self_registered_portal:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.self_registered_portal:
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
        allowGuestToUseSocialAccounts: true
        allowShowGuestForm: true
        alternateGuestPortal: string
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
      selfRegPageSettings:
        accountValidityDuration: 0
        accountValidityTimeUnits: string
        allowGraceAccess: true
        approvalEmailAddresses: string
        approveDenyLinksTimeUnits: string
        approveDenyLinksValidFor: 0
        assignGuestsToGuestType: string
        aupDisplay: string
        authenticateSponsorsUsingPortalList: true
        autoLoginSelfWait: true
        autoLoginTimePeriod: 0
        credentialNotificationUsingEmail: true
        credentialNotificationUsingSms: true
        enableGuestEmailBlacklist: true
        enableGuestEmailWhitelist: true
        fieldCompany:
          include: true
          require: true
        fieldEmailAddr:
          include: true
          require: true
        fieldFirstName:
          include: true
          require: true
        fieldLastName:
          include: true
          require: true
        fieldLocation:
          include: true
          require: true
        fieldPersonBeingVisited:
          include: true
          require: true
        fieldPhoneNo:
          include: true
          require: true
        fieldReasonForVisit:
          include: true
          require: true
        fieldSmsProvider:
          include: true
          require: true
        fieldUserName:
          include: true
          require: true
        graceAccessExpireInterval: 0
        graceAccessSendAccountExpiration: true
        guestEmailBlacklistDomains:
        - string
        guestEmailWhitelistDomains:
        - string
        includeAup: true
        postRegistrationRedirect: string
        postRegistrationRedirectUrl: string
        registrationCode: string
        requireApproverToAuthenticate: true
        requireAupAcceptance: true
        requireGuestApproval: true
        requireRegistrationCode: true
        selectableLocations:
        - string
        selectableSmsProviders:
        - string
        sendApprovalRequestTo: string
        sponsorPortalList:
        - string
      selfRegSuccessSettings:
        allowGuestLoginFromSelfregSuccessPage: true
        allowGuestSendSelfUsingEmail: true
        allowGuestSendSelfUsingPrint: true
        allowGuestSendSelfUsingSms: true
        aupOnPage: true
        includeAup: true
        includeCompany: true
        includeEmailAddr: true
        includeFirstName: true
        includeLastName: true
        includeLocation: true
        includePassword: true
        includePersonBeingVisited: true
        includePhoneNo: true
        includeReasonForVisit: true
        includeSmsProvider: true
        includeUserName: true
        requireAupAcceptance: true
        requireAupScrolling: true
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

## [Return Values](self_registered_portal_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"customizations": {"globalCustomizations": {"backgroundImage": {"data": "string"}, "bannerImage": {"data": "string"}, "bannerTitle": "string", "contactText": "string", "desktopLogoImage": {"data": "string"}, "footerElement": "string", "mobileLogoImage": {"data": "string"}}, "language": {"viewLanguage": "string"}, "pageCustomizations": {"data": [{"key": "string", "value": "string"}]}, "portalTheme": {"id": "string", "name": "string", "themeData": "string"}, "portalTweakSettings": {"bannerColor": "string", "bannerTextColor": "string", "pageBackgroundColor": "string", "pageLabelAndTextColor": "string"}}, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "portalTestUrl": "string", "portalType": "string", "settings": {"aupSettings": {"displayFrequency": "string", "displayFrequencyIntervalDays": 0, "includeAup": true, "requireAupScrolling": true, "requireScrolling": true, "skipAupForEmployees": true, "useDiffAupForEmployees": true}, "authSuccessSettings": {"redirectUrl": "string", "successRedirect": "string"}, "byodSettings": {"byodRegistrationSettings": {"endPointIdentityGroupId": "string", "showDeviceID": true}, "byodRegistrationSuccessSettings": {"redirectUrl": "string", "successRedirect": "string"}, "byodWelcomeSettings": {"aupDisplay": "string", "enableBYOD": true, "enableGuestAccess": true, "includeAup": true, "requireAupAcceptance": true, "requireMDM": true, "requireScrolling": true}}, "guestChangePasswordSettings": {"allowChangePasswdAtFirstLogin": true}, "guestDeviceRegistrationSettings": {"allowGuestsToRegisterDevices": true, "autoRegisterGuestDevices": true}, "loginPageSettings": {"accessCode": "string", "allowAlternateGuestPortal": true, "allowForgotPassword": true, "allowGuestToChangePassword": true, "allowGuestToCreateAccounts": true, "allowGuestToUseSocialAccounts": true, "allowShowGuestForm": true, "alternateGuestPortal": "string", "aupDisplay": "string", "includeAup": true, "maxFailedAttemptsBeforeRateLimit": 0, "requireAccessCode": true, "requireAupAcceptance": true, "socialConfigs": [{"socialMediaType": "string", "socialMediaValue": "string"}], "timeBetweenLoginsDuringRateLimit": 0}, "portalSettings": {"allowedInterfaces": ["string"], "alwaysUsedLanguage": "string", "assignedGuestTypeForEmployee": "string", "authenticationMethod": "string", "certificateGroupTag": "string", "displayLang": "string", "fallbackLanguage": "string", "httpsPort": 0}, "postAccessBannerSettings": {"includePostAccessBanner": true}, "postLoginBannerSettings": {"includePostAccessBanner": true}, "selfRegPageSettings": {"accountValidityDuration": 0, "accountValidityTimeUnits": "string", "allowGraceAccess": true, "approvalEmailAddresses": "string", "approveDenyLinksTimeUnits": "string", "approveDenyLinksValidFor": 0, "assignGuestsToGuestType": "string", "aupDisplay": "string", "authenticateSponsorsUsingPortalList": true, "autoLoginSelfWait": true, "autoLoginTimePeriod": 0, "credentialNotificationUsingEmail": true, "credentialNotificationUsingSms": true, "enableGuestEmailBlacklist": true, "enableGuestEmailWhitelist": true, "fieldCompany": {"include": true, "require": true}, "fieldEmailAddr": {"include": true, "require": true}, "fieldFirstName": {"include": true, "require": true}, "fieldLastName": {"include": true, "require": true}, "fieldLocation": {"include": true, "require": true}, "fieldPersonBeingVisited": {"include": true, "require": true}, "fieldPhoneNo": {"include": true, "require": true}, "fieldReasonForVisit": {"include": true, "require": true}, "fieldSmsProvider": {"include": true, "require": true}, "fieldUserName": {"include": true, "require": true}, "graceAccessExpireInterval": 0, "graceAccessSendAccountExpiration": true, "guestEmailBlacklistDomains": ["string"], "guestEmailWhitelistDomains": ["string"], "includeAup": true, "postRegistrationRedirect": "string", "postRegistrationRedirectUrl": "string", "registrationCode": "string", "requireApproverToAuthenticate": true, "requireAupAcceptance": true, "requireGuestApproval": true, "requireRegistrationCode": true, "selectableLocations": ["string"], "selectableSmsProviders": ["string"], "sendApprovalRequestTo": "string", "sponsorPortalList": ["string"]}, "selfRegSuccessSettings": {"allowGuestLoginFromSelfregSuccessPage": true, "allowGuestSendSelfUsingEmail": true, "allowGuestSendSelfUsingPrint": true, "allowGuestSendSelfUsingSms": true, "aupOnPage": true, "includeAup": true, "includeCompany": true, "includeEmailAddr": true, "includeFirstName": true, "includeLastName": true, "includeLocation": true, "includePassword": true, "includePersonBeingVisited": true, "includePhoneNo": true, "includeReasonForVisit": true, "includeSmsProvider": true, "includeUserName": true, "requireAupAcceptance": true, "requireAupScrolling": true}, "supportInfoSettings": {"defaultEmptyFieldValue": "string", "emptyFieldDisplay": "string", "includeBrowserUserAgent": true, "includeFailureCode": true, "includeIpAddress": true, "includeMacAddr": true, "includePolicyServer": true, "includeSupportInfoPage": true}}}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
