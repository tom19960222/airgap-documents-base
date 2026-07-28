---
collection: ansible
version: "8"
title: "cisco.ise.authorization_profile module – Resource module for Authorization Profile"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/authorization_profile_module.html
fetched_at: 2026-07-28T01:27:23+00:00
---
# cisco.ise.authorization_profile module – Resource module for Authorization Profile

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
> see [Requirements](authorization_profile_module.md#ansible-collections-cisco-ise-authorization-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.authorization_profile`.

New in cisco.ise 1.0.0

- [Synopsis](authorization_profile_module.md#synopsis)
- [Requirements](authorization_profile_module.md#requirements)
- [Parameters](authorization_profile_module.md#parameters)
- [Notes](authorization_profile_module.md#notes)
- [Examples](authorization_profile_module.md#examples)
- [Return Values](authorization_profile_module.md#return-values)

## [Synopsis](authorization_profile_module.md#id1)

- Manage operations create, update and delete of the resource Authorization Profile.
- This API creates an authorization profile.
- This API deletes an authorization profile.
- This API allows the client to update an authorization profile.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](authorization_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](authorization_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accessType**  string | Allowed Values - ACCESS_ACCEPT, - ACCESS_REJECT. |
| **acl**  string | Authorization Profile’s acl. |
| **advancedAttributes**  list / elements=dictionary | Authorization Profile’s advancedAttributes. |
| **leftHandSideDictionaryAttribue**  dictionary | Authorization Profile’s leftHandSideDictionaryAttribue. |
| **AdvancedAttributeValueType**  string | Authorization Profile’s AdvancedAttributeValueType. |
| **attributeName**  string | Authorization Profile’s attributeName. |
| **dictionaryName**  string | Authorization Profile’s dictionaryName. |
| **value**  string | Authorization Profile’s value. |
| **rightHandSideAttribueValue**  dictionary | Attribute value can be of type AttributeValue or AdvancedDictionaryAttribute. For AttributeValue the value is String, For AdvancedDictionaryAttribute the value is dictionaryName and attributeName properties. |
| **AdvancedAttributeValueType**  string | Authorization Profile’s AdvancedAttributeValueType. |
| **attributeName**  string | Authorization Profile’s attributeName. |
| **dictionaryName**  string | Authorization Profile’s dictionaryName. |
| **value**  string | Authorization Profile’s value. |
| **agentlessPosture**  boolean | AgentlessPosture flag.  **Choices:**   - `false` - `true` |
| **airespaceACL**  string | Authorization Profile’s airespaceACL. |
| **airespaceIPv6ACL**  string | Authorization Profile’s airespaceIPv6ACL. |
| **asaVpn**  string | Authorization Profile’s asaVpn. |
| **authzProfileType**  string | Allowed Values - SWITCH, - TRUSTSEC, - TACACS SWITCH is used for Standard Authorization Profiles. |
| **autoSmartPort**  string | Authorization Profile’s autoSmartPort. |
| **avcProfile**  string | Authorization Profile’s avcProfile. |
| **daclName**  string | Authorization Profile’s daclName. |
| **description**  string | Authorization Profile’s description. |
| **easywiredSessionCandidate**  boolean | EasywiredSessionCandidate flag.  **Choices:**   - `false` - `true` |
| **id**  string | Resource UUID value. |
| **interfaceTemplate**  string | Authorization Profile’s interfaceTemplate. |
| **ipv6ACLFilter**  string | Authorization Profile’s ipv6ACLFilter. |
| **ipv6DaclName**  string | Authorization Profile’s ipv6DaclName. |
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
| **macSecPolicy**  string | Allowed Values - MUST_SECURE, - MUST_NOT_SECURE, - SHOULD_SECURE. |
| **name**  string | Resource Name. |
| **neat**  boolean | Neat flag.  **Choices:**   - `false` - `true` |
| **profileName**  string | Authorization Profile’s profileName. |
| **reauth**  dictionary | Authorization Profile’s reauth. |
| **connectivity**  string | Allowed Values - DEFAULT, - RADIUS_REQUEST. |
| **timer**  integer | Valid range is 1-65535. |
| **serviceTemplate**  boolean | ServiceTemplate flag.  **Choices:**   - `false` - `true` |
| **trackMovement**  boolean | TrackMovement flag.  **Choices:**   - `false` - `true` |
| **vlan**  dictionary | Authorization Profile’s vlan. |
| **nameID**  string | Authorization Profile’s nameID. |
| **tagID**  integer | Valid range is 0-31. |
| **voiceDomainPermission**  boolean | VoiceDomainPermission flag.  **Choices:**   - `false` - `true` |
| **webAuth**  boolean | WebAuth flag.  **Choices:**   - `false` - `true` |
| **webRedirection**  dictionary | Authorization Profile’s webRedirection. |
| **acl**  string | Authorization Profile’s acl. |
| **displayCertificatesRenewalMessages**  boolean | The displayCertificatesRenewalMessages is mandatory when ‘WebRedirectionType’ value is ‘CentralizedWebAuth’. For all other ‘WebRedirectionType’ values the field must be ignored.  **Choices:**   - `false` - `true` |
| **portalName**  string | A portal that exist in the DB and fits the WebRedirectionType. |
| **staticIPHostNameFQDN**  string | Authorization Profile’s staticIPHostNameFQDN. |
| **WebRedirectionType**  string | Value MUST be one of the following CentralizedWebAuth, HotSpot, NativeSupplicanProvisioning, ClientProvisioning. The WebRedirectionType must fit the portalName. |

## [Notes](authorization_profile_module.md#id4)

> **Note:**
>
> - SDK Method used are authorization_profile.AuthorizationProfile.create_authorization_profile, authorization_profile.AuthorizationProfile.delete_authorization_profile_by_id, authorization_profile.AuthorizationProfile.update_authorization_profile_by_id,
> - Paths used are post /ers/config/authorizationprofile, delete /ers/config/authorizationprofile/{id}, put /ers/config/authorizationprofile/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](authorization_profile_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.authorization_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accessType: string
    acl: string
    advancedAttributes:
    - leftHandSideDictionaryAttribue:
        AdvancedAttributeValueType: string
        attributeName: string
        dictionaryName: string
        value: string
      rightHandSideAttribueValue:
        AdvancedAttributeValueType: string
        attributeName: string
        dictionaryName: string
        value: string
    agentlessPosture: true
    airespaceACL: string
    airespaceIPv6ACL: string
    asaVpn: string
    authzProfileType: string
    autoSmartPort: string
    avcProfile: string
    daclName: string
    description: string
    easywiredSessionCandidate: true
    id: string
    interfaceTemplate: string
    ipv6ACLFilter: string
    ipv6DaclName: string
    macSecPolicy: string
    name: string
    neat: true
    profileName: string
    reauth:
      connectivity: string
      timer: 0
    serviceTemplate: true
    trackMovement: true
    vlan:
      nameID: string
      tagID: 0
    voiceDomainPermission: true
    webAuth: true
    webRedirection:
      WebRedirectionType: string
      acl: string
      displayCertificatesRenewalMessages: true
      portalName: string
      staticIPHostNameFQDN: string

- name: Delete by id
  cisco.ise.authorization_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.authorization_profile:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    accessType: string
    acl: string
    advancedAttributes:
    - leftHandSideDictionaryAttribue:
        AdvancedAttributeValueType: string
        attributeName: string
        dictionaryName: string
        value: string
      rightHandSideAttribueValue:
        AdvancedAttributeValueType: string
        attributeName: string
        dictionaryName: string
        value: string
    agentlessPosture: true
    airespaceACL: string
    airespaceIPv6ACL: string
    asaVpn: string
    authzProfileType: string
    autoSmartPort: string
    avcProfile: string
    daclName: string
    description: string
    easywiredSessionCandidate: true
    id: string
    interfaceTemplate: string
    ipv6ACLFilter: string
    ipv6DaclName: string
    macSecPolicy: string
    name: string
    neat: true
    profileName: string
    reauth:
      connectivity: string
      timer: 0
    serviceTemplate: true
    trackMovement: true
    vlan:
      nameID: string
      tagID: 0
    voiceDomainPermission: true
    webAuth: true
    webRedirection:
      WebRedirectionType: string
      acl: string
      displayCertificatesRenewalMessages: true
      portalName: string
      staticIPHostNameFQDN: string
```

## [Return Values](authorization_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"accessType": "string", "acl": "string", "advancedAttributes": [{"leftHandSideDictionaryAttribue": {"AdvancedAttributeValueType": "string", "attributeName": "string", "dictionaryName": "string", "value": "string"}, "rightHandSideAttribueValue": {"AdvancedAttributeValueType": "string", "attributeName": "string", "dictionaryName": "string", "value": "string"}}], "agentlessPosture": true, "airespaceACL": "string", "airespaceIPv6ACL": "string", "asaVpn": "string", "authzProfileType": "string", "autoSmartPort": "string", "avcProfile": "string", "daclName": "string", "description": "string", "easywiredSessionCandidate": true, "id": "string", "interfaceTemplate": "string", "ipv6ACLFilter": "string", "ipv6DaclName": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "macSecPolicy": "string", "name": "string", "neat": true, "profileName": "string", "reauth": {"connectivity": "string", "timer": 0}, "serviceTemplate": true, "trackMovement": true, "vlan": {"nameID": "string", "tagID": 0}, "voiceDomainPermission": true, "webAuth": true, "webRedirection": {"WebRedirectionType": "string", "acl": "string", "displayCertificatesRenewalMessages": true, "portalName": "string", "staticIPHostNameFQDN": "string"}}` |
| **ise_update_response**  dictionary  *added in cisco.ise 1.1.0* | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
