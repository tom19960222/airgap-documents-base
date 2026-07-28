---
collection: ansible
version: "6"
title: "cisco.ise.aci_settings module – Resource module for ACI Settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/aci_settings_module.html
fetched_at: 2026-07-27T16:56:01+00:00
---
# cisco.ise.aci_settings module – Resource module for ACI Settings

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
> see [Requirements](aci_settings_module.md#ansible-collections-cisco-ise-aci-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.aci_settings`.

New in cisco.ise 1.0.0

- [Synopsis](aci_settings_module.md#synopsis)
- [Requirements](aci_settings_module.md#requirements)
- [Parameters](aci_settings_module.md#parameters)
- [Notes](aci_settings_module.md#notes)
- [Examples](aci_settings_module.md#examples)
- [Return Values](aci_settings_module.md#return-values)

## [Synopsis](aci_settings_module.md#id1)

- Manage operation update of the resource ACI Settings.
- This API allows the client to update ACI settings.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](aci_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](aci_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aci50**  boolean | Enable 5.0 ACI Version.  Choices:   - `false` - `true` |
| **aci51**  boolean | Enable 5.1 ACI Version.  Choices:   - `false` - `true` |
| **aciipaddress**  string | ACI Domain manager Ip Address. |
| **acipassword**  string | ACI Domain manager Password. |
| **aciuserName**  string | ACI Domain manager Username. |
| **adminName**  string | ACI Cluster Admin name. |
| **adminPassword**  string | ACI Cluster Admin password. |
| **allSXPDomain**  boolean | AllSXPDomain flag.  Choices:   - `false` - `true` |
| **defaultSGtName**  string | ACI Settings’s defaultSGtName. |
| **enableACI**  boolean | Enable ACI Integration.  Choices:   - `false` - `true` |
| **enableDataPlane**  boolean | EnableDataPlane flag.  Choices:   - `false` - `true` |
| **enableElementsLimit**  boolean | EnableElementsLimit flag.  Choices:   - `false` - `true` |
| **id**  string | Resource UUID value. |
| **ipAddressHostName**  string | ACI Cluster IP Address / Host name. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **l3RouteNetwork**  string | ACI Settings’s l3RouteNetwork. |
| **maxNumIepgFromACI**  integer | ACI Settings’s maxNumIepgFromACI. |
| **maxNumSGtToACI**  integer | ACI Settings’s maxNumSGtToACI. |
| **specificSXPDomain**  boolean | SpecificSXPDomain flag.  Choices:   - `false` - `true` |
| **specifixSXPDomainList**  list / elements=string | ACI Settings’s specifixSXPDomainList. |
| **suffixToEpg**  string | ACI Settings’s suffixToEpg. |
| **suffixToSGt**  string | ACI Settings’s suffixToSGt. |
| **tenantName**  string | ACI Settings’s tenantName. |
| **untaggedPacketIepgName**  string | ACI Settings’s untaggedPacketIepgName. |

## [Notes](aci_settings_module.md#id4)

> **Note:**
>
> - SDK Method used are aci_settings.AciSettings.update_aci_settings_by_id,
> - Paths used are put /ers/config/acisettings/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](aci_settings_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.aci_settings:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    aci50: true
    aci51: true
    aciipaddress: string
    acipassword: string
    aciuserName: string
    adminName: string
    adminPassword: string
    allSxpDomain: true
    defaultSgtName: string
    enableAci: true
    enableDataPlane: true
    enableElementsLimit: true
    id: string
    ipAddressHostName: string
    l3RouteNetwork: string
    maxNumIepgFromAci: 0
    maxNumSgtToAci: 0
    specificSxpDomain: true
    specifixSxpDomainList:
    - string
    suffixToEpg: string
    suffixToSgt: string
    tenantName: string
    untaggedPacketIepgName: string
```

## [Return Values](aci_settings_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"aci50": true, "aci51": true, "aciipaddress": "string", "acipassword": "string", "aciuserName": "string", "adminName": "string", "adminPassword": "string", "allSxpDomain": true, "defaultSgtName": "string", "enableAci": true, "enableDataPlane": true, "enableElementsLimit": true, "id": "string", "ipAddressHostName": "string", "l3RouteNetwork": "string", "maxNumIepgFromAci": 0, "maxNumSgtToAci": 0, "specificSxpDomain": true, "specifixSxpDomainList": ["string"], "suffixToEpg": "string", "suffixToSgt": "string", "tenantName": "string", "untaggedPacketIepgName": "string"}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
