---
collection: ansible
version: "6"
title: "cisco.ise.network_device module – Resource module for Network Device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/network_device_module.html
fetched_at: 2026-07-27T16:58:15+00:00
---
# cisco.ise.network_device module – Resource module for Network Device

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
> see [Requirements](network_device_module.md#ansible-collections-cisco-ise-network-device-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.network_device`.

New in cisco.ise 1.0.0

- [Synopsis](network_device_module.md#synopsis)
- [Requirements](network_device_module.md#requirements)
- [Parameters](network_device_module.md#parameters)
- [Notes](network_device_module.md#notes)
- [Examples](network_device_module.md#examples)
- [Return Values](network_device_module.md#return-values)

## [Synopsis](network_device_module.md#id1)

- Manage operations create, update and delete of the resource Network Device.
- This API creates a network device.
- This API deletes a network device by ID.
- This API deletes a network device by name.
- This API allows the client to update a network device by ID.
- This API allows the client to update a network device by name.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](network_device_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](network_device_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authenticationSettings**  dictionary | Network Device’s authenticationSettings. |
| **dtlsRequired**  boolean | This value enforces use of dtls.  Choices:   - `false` - `true` |
| **enabled**  boolean | Enabled flag.  Choices:   - `false` - `true` |
| **enableKeyWrap**  boolean | EnableKeyWrap flag.  Choices:   - `false` - `true` |
| **enableMultiSecret**  string | Network Device’s enableMultiSecret. |
| **keyEncryptionKey**  string | Network Device’s keyEncryptionKey. |
| **keyInputFormat**  string | Allowed values - ASCII, - HEXADECIMAL. |
| **messageAuthenticatorCodeKey**  string | Network Device’s messageAuthenticatorCodeKey. |
| **networkProtocol**  string | Allowed values - RADIUS, - TACACS_PLUS. |
| **radiusSharedSecret**  string | Network Device’s radiusSharedSecret. |
| **secondRADIUSSharedSecret**  string | Network Device’s secondRADIUSSharedSecret. |
| **coaPort**  integer | Network Device’s coaPort. |
| **description**  string | Network Device’s description. |
| **dtlsDnsName**  string | This value is used to verify the client identity contained in the X.509 RADIUS/DTLS client certificate. |
| **id**  string | Network Device’s id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **modelName**  string | Network Device’s modelName. |
| **name**  string | Network Device’s name. |
| **NetworkDeviceGroupList**  list / elements=string | List of Network Device Group names for this node. |
| **NetworkDeviceIPList**  list / elements=dictionary | List of IP Subnets for this node. |
| **getIpaddressExclude**  string | It can be either single IP address or IP range address. |
| **ipaddress**  string | Network Device’s ipaddress. |
| **mask**  integer | Network Device’s mask. |
| **profileName**  string | Network Device’s profileName. |
| **snmpsettings**  dictionary | Network Device’s snmpsettings. |
| **linkTrapQuery**  boolean | LinkTrapQuery flag.  Choices:   - `false` - `true` |
| **macTrapQuery**  boolean | MacTrapQuery flag.  Choices:   - `false` - `true` |
| **originatingPolicyServicesNode**  string | Network Device’s originatingPolicyServicesNode. |
| **pollingInterval**  integer | Network Device’s pollingInterval. |
| **roCommunity**  string | Network Device’s roCommunity. |
| **version**  string | Network Device’s version. |
| **softwareVersion**  string | Network Device’s softwareVersion. |
| **tacacsSettings**  dictionary | Network Device’s tacacsSettings. |
| **connectModeOptions**  string | Allowed values - OFF, - ON_LEGACY, - ON_DRAFT_COMPLIANT. |
| **sharedSecret**  string | Network Device’s sharedSecret. |
| **trustsecsettings**  dictionary | Network Device’s trustsecsettings. |
| **deviceAuthenticationSettings**  dictionary | Network Device’s deviceAuthenticationSettings. |
| **sgaDeviceId**  string | Network Device’s sgaDeviceId. |
| **sgaDevicePassword**  string | Network Device’s sgaDevicePassword. |
| **deviceConfigurationDeployment**  dictionary | Network Device’s deviceConfigurationDeployment. |
| **enableModePassword**  string | Network Device’s enableModePassword. |
| **execModePassword**  string | Network Device’s execModePassword. |
| **execModeUsername**  string | Network Device’s execModeUsername. |
| **includeWhenDeployingSGTUpdates**  boolean | IncludeWhenDeployingSGTUpdates flag.  Choices:   - `false` - `true` |
| **pushIdSupport**  boolean | PushIdSupport flag.  Choices:   - `false` - `true` |
| **sgaNotificationAndUpdates**  dictionary | Network Device’s sgaNotificationAndUpdates. |
| **coaSourceHost**  string | Network Device’s coaSourceHost. |
| **downlaodEnvironmentDataEveryXSeconds**  integer | Network Device’s downlaodEnvironmentDataEveryXSeconds. |
| **downlaodPeerAuthorizationPolicyEveryXSeconds**  integer | Network Device’s downlaodPeerAuthorizationPolicyEveryXSeconds. |
| **downloadSGACLListsEveryXSeconds**  integer | Network Device’s downloadSGACLListsEveryXSeconds. |
| **otherSGADevicesToTrustThisDevice**  boolean | OtherSGADevicesToTrustThisDevice flag.  Choices:   - `false` - `true` |
| **reAuthenticationEveryXSeconds**  integer | Network Device’s reAuthenticationEveryXSeconds. |
| **sendConfigurationToDevice**  boolean | SendConfigurationToDevice flag.  Choices:   - `false` - `true` |
| **sendConfigurationToDeviceUsing**  string | Allowed values - ENABLE_USING_COA, - ENABLE_USING_CLI, - DISABLE_ALL. |

## [Notes](network_device_module.md#id4)

> **Note:**
>
> - SDK Method used are network_device.NetworkDevice.create_network_device, network_device.NetworkDevice.delete_network_device_by_id, network_device.NetworkDevice.delete_network_device_by_name, network_device.NetworkDevice.update_network_device_by_id, network_device.NetworkDevice.update_network_device_by_name,
> - Paths used are post /ers/config/networkdevice, delete /ers/config/networkdevice/name/{name}, delete /ers/config/networkdevice/{id}, put /ers/config/networkdevice/name/{name}, put /ers/config/networkdevice/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](network_device_module.md#id5)

```yaml+jinja
- name: Update by name
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    NetworkDeviceGroupList:
    - string
    NetworkDeviceIPList:
    - getIpaddressExclude: string
      ipaddress: string
      mask: 0
    authenticationSettings:
      dtlsRequired: true
      enableKeyWrap: true
      enableMultiSecret: string
      enabled: true
      keyEncryptionKey: string
      keyInputFormat: string
      messageAuthenticatorCodeKey: string
      networkProtocol: string
      radiusSharedSecret: string
      secondRadiusSharedSecret: string
    coaPort: 0
    description: string
    dtlsDnsName: string
    id: string
    modelName: string
    name: string
    profileName: string
    snmpsettings:
      linkTrapQuery: true
      macTrapQuery: true
      originatingPolicyServicesNode: string
      pollingInterval: 0
      roCommunity: string
      version: string
    softwareVersion: string
    tacacsSettings:
      connectModeOptions: string
      sharedSecret: string
    trustsecsettings:
      deviceAuthenticationSettings:
        sgaDeviceId: string
        sgaDevicePassword: string
      deviceConfigurationDeployment:
        enableModePassword: string
        execModePassword: string
        execModeUsername: string
        includeWhenDeployingSGTUpdates: true
      pushIdSupport: true
      sgaNotificationAndUpdates:
        coaSourceHost: string
        downlaodEnvironmentDataEveryXSeconds: 0
        downlaodPeerAuthorizationPolicyEveryXSeconds: 0
        downloadSGACLListsEveryXSeconds: 0
        otherSGADevicesToTrustThisDevice: true
        reAuthenticationEveryXSeconds: 0
        sendConfigurationToDevice: true
        sendConfigurationToDeviceUsing: string

- name: Delete by name
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    name: string

- name: Update by id
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    NetworkDeviceGroupList:
    - string
    NetworkDeviceIPList:
    - getIpaddressExclude: string
      ipaddress: string
      mask: 0
    authenticationSettings:
      dtlsRequired: true
      enableKeyWrap: true
      enableMultiSecret: string
      enabled: true
      keyEncryptionKey: string
      keyInputFormat: string
      messageAuthenticatorCodeKey: string
      networkProtocol: string
      radiusSharedSecret: string
      secondRadiusSharedSecret: string
    coaPort: 0
    description: string
    dtlsDnsName: string
    id: string
    modelName: string
    name: string
    profileName: string
    snmpsettings:
      linkTrapQuery: true
      macTrapQuery: true
      originatingPolicyServicesNode: string
      pollingInterval: 0
      roCommunity: string
      version: string
    softwareVersion: string
    tacacsSettings:
      connectModeOptions: string
      sharedSecret: string
    trustsecsettings:
      deviceAuthenticationSettings:
        sgaDeviceId: string
        sgaDevicePassword: string
      deviceConfigurationDeployment:
        enableModePassword: string
        execModePassword: string
        execModeUsername: string
        includeWhenDeployingSGTUpdates: true
      pushIdSupport: true
      sgaNotificationAndUpdates:
        coaSourceHost: string
        downlaodEnvironmentDataEveryXSeconds: 0
        downlaodPeerAuthorizationPolicyEveryXSeconds: 0
        downloadSGACLListsEveryXSeconds: 0
        otherSGADevicesToTrustThisDevice: true
        reAuthenticationEveryXSeconds: 0
        sendConfigurationToDevice: true
        sendConfigurationToDeviceUsing: string

- name: Delete by id
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.network_device:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    NetworkDeviceGroupList:
    - string
    NetworkDeviceIPList:
    - getIpaddressExclude: string
      ipaddress: string
      mask: 0
    authenticationSettings:
      dtlsRequired: true
      enableKeyWrap: true
      enableMultiSecret: string
      enabled: true
      keyEncryptionKey: string
      keyInputFormat: string
      messageAuthenticatorCodeKey: string
      networkProtocol: string
      radiusSharedSecret: string
      secondRadiusSharedSecret: string
    coaPort: 0
    description: string
    dtlsDnsName: string
    modelName: string
    name: string
    profileName: string
    snmpsettings:
      linkTrapQuery: true
      macTrapQuery: true
      originatingPolicyServicesNode: string
      pollingInterval: 0
      roCommunity: string
      version: string
    softwareVersion: string
    tacacsSettings:
      connectModeOptions: string
      sharedSecret: string
    trustsecsettings:
      deviceAuthenticationSettings:
        sgaDeviceId: string
        sgaDevicePassword: string
      deviceConfigurationDeployment:
        enableModePassword: string
        execModePassword: string
        execModeUsername: string
        includeWhenDeployingSGTUpdates: true
      pushIdSupport: true
      sgaNotificationAndUpdates:
        coaSourceHost: string
        downlaodEnvironmentDataEveryXSeconds: 0
        downlaodPeerAuthorizationPolicyEveryXSeconds: 0
        downloadSGACLListsEveryXSeconds: 0
        otherSGADevicesToTrustThisDevice: true
        reAuthenticationEveryXSeconds: 0
        sendConfigurationToDevice: true
        sendConfigurationToDeviceUsing: string
```

## [Return Values](network_device_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"NetworkDeviceGroupList": ["string"], "NetworkDeviceIPList": [{"getIpaddressExclude": "string", "ipaddress": "string", "mask": 0}], "authenticationSettings": {"dtlsRequired": true, "enableKeyWrap": true, "enableMultiSecret": "string", "enabled": true, "keyEncryptionKey": "string", "keyInputFormat": "string", "messageAuthenticatorCodeKey": "string", "networkProtocol": "string", "radiusSharedSecret": "string", "secondRadiusSharedSecret": "string"}, "coaPort": 0, "description": "string", "dtlsDnsName": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "modelName": "string", "name": "string", "profileName": "string", "snmpsettings": {"linkTrapQuery": true, "macTrapQuery": true, "originatingPolicyServicesNode": "string", "pollingInterval": 0, "roCommunity": "string", "version": "string"}, "softwareVersion": "string", "tacacsSettings": {"connectModeOptions": "string", "sharedSecret": "string"}, "trustsecsettings": {"deviceAuthenticationSettings": {"sgaDeviceId": "string", "sgaDevicePassword": "string"}, "deviceConfigurationDeployment": {"enableModePassword": "string", "execModePassword": "string", "execModeUsername": "string", "includeWhenDeployingSGTUpdates": true}, "pushIdSupport": true, "sgaNotificationAndUpdates": {"coaSourceHost": "string", "downlaodEnvironmentDataEveryXSeconds": 0, "downlaodPeerAuthorizationPolicyEveryXSeconds": 0, "downloadSGACLListsEveryXSeconds": 0, "otherSGADevicesToTrustThisDevice": true, "reAuthenticationEveryXSeconds": 0, "sendConfigurationToDevice": true, "sendConfigurationToDeviceUsing": "string"}}}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
