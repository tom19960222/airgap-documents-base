---
collection: ansible
version: "6"
title: "cisco.dnac.wireless_enterprise_ssid module – Resource module for Wireless Enterprise Ssid"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/wireless_enterprise_ssid_module.html
fetched_at: 2026-07-27T16:54:50+00:00
---
# cisco.dnac.wireless_enterprise_ssid module – Resource module for Wireless Enterprise Ssid

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](wireless_enterprise_ssid_module.md#ansible-collections-cisco-dnac-wireless-enterprise-ssid-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_enterprise_ssid`.

New in cisco.dnac 3.1.0

- [Synopsis](wireless_enterprise_ssid_module.md#synopsis)
- [Requirements](wireless_enterprise_ssid_module.md#requirements)
- [Parameters](wireless_enterprise_ssid_module.md#parameters)
- [Notes](wireless_enterprise_ssid_module.md#notes)
- [See Also](wireless_enterprise_ssid_module.md#see-also)
- [Examples](wireless_enterprise_ssid_module.md#examples)
- [Return Values](wireless_enterprise_ssid_module.md#return-values)

## [Synopsis](wireless_enterprise_ssid_module.md#id1)

- Manage operations create, update and delete of the resource Wireless Enterprise Ssid.
- Creates enterprise SSID.
- Deletes given enterprise SSID.
- Update enterprise SSID.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_enterprise_ssid_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_enterprise_ssid_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **basicServiceSetClientIdleTimeout**  integer | Basic Service Set Client Idle Timeout. |
| **clientExclusionTimeout**  integer | Client Exclusion Timeout. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **enableBasicServiceSetMaxIdle**  boolean | Enable Basic Service Set Max Idle.  Choices:   - `false` - `true` |
| **enableBroadcastSSID**  boolean | Enable Broadcase SSID.  Choices:   - `false` - `true` |
| **enableClientExclusion**  boolean | Enable Client Exclusion.  Choices:   - `false` - `true` |
| **enableDirectedMulticastService**  boolean | Enable Directed Multicast Service.  Choices:   - `false` - `true` |
| **enableFastLane**  boolean | Enable FastLane.  Choices:   - `false` - `true` |
| **enableMACFiltering**  boolean | Enable MAC Filtering.  Choices:   - `false` - `true` |
| **enableNeighborList**  boolean | Enable Neighbor List.  Choices:   - `false` - `true` |
| **enableSessionTimeOut**  boolean | Enable Session Timeout.  Choices:   - `false` - `true` |
| **fastTransition**  string | Fast Transition. |
| **mfpClientProtection**  string | Management Frame Protection Client. |
| **name**  string | SSID NAME. |
| **nasOptions**  list / elements=string | Nas Options. |
| **passphrase**  string | Passphrase. |
| **radioPolicy**  string | Radio Policy Enum (enum Triple band operation (2.4GHz, 5GHz and 6GHz), Triple band operation with band select, 5GHz only, 2.4GHz only, 6GHz only). |
| **securityLevel**  string | Security Level. |
| **sessionTimeOut**  integer | Session Time Out. |
| **ssidName**  string | SsidName path parameter. Enter the SSID name to be deleted. |
| **trafficType**  string | Traffic Type Enum (voicedata or data ). |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](wireless_enterprise_ssid_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.create_enterprise_ssid, wireless.Wireless.delete_enterprise_ssid, wireless.Wireless.update_enterprise_ssid,
> - Paths used are post /dna/intent/api/v1/enterprise-ssid, delete /dna/intent/api/v1/enterprise-ssid/{ssidName}, put /dna/intent/api/v1/enterprise-ssid,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_enterprise_ssid_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless CreateEnterpriseSSID](https://developer.cisco.com/docs/dna-center/#!create-enterprise-ssid)
> :   Complete reference of the CreateEnterpriseSSID API.
>
> [Cisco DNA Center documentation for Wireless DeleteEnterpriseSSID](https://developer.cisco.com/docs/dna-center/#!delete-enterprise-ssid)
> :   Complete reference of the DeleteEnterpriseSSID API.
>
> [Cisco DNA Center documentation for Wireless UpdateEnterpriseSSID](https://developer.cisco.com/docs/dna-center/#!update-enterprise-ssid)
> :   Complete reference of the UpdateEnterpriseSSID API.

## [Examples](wireless_enterprise_ssid_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.wireless_enterprise_ssid:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    basicServiceSetClientIdleTimeout: 0
    clientExclusionTimeout: 0
    enableBasicServiceSetMaxIdle: true
    enableBroadcastSSID: true
    enableClientExclusion: true
    enableDirectedMulticastService: true
    enableFastLane: true
    enableMACFiltering: true
    enableNeighborList: true
    enableSessionTimeOut: true
    fastTransition: string
    mfpClientProtection: string
    name: string
    nasOptions:
    - string
    passphrase: string
    radioPolicy: string
    securityLevel: string
    sessionTimeOut: 0
    trafficType: string

- name: Update all
  cisco.dnac.wireless_enterprise_ssid:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    basicServiceSetClientIdleTimeout: 0
    clientExclusionTimeout: 0
    enableBasicServiceSetMaxIdle: true
    enableBroadcastSSID: true
    enableClientExclusion: true
    enableDirectedMulticastService: true
    enableFastLane: true
    enableMACFiltering: true
    enableNeighborList: true
    enableSessionTimeOut: true
    fastTransition: string
    mfpClientProtection: string
    name: string
    nasOptions:
    - string
    passphrase: string
    radioPolicy: string
    securityLevel: string
    sessionTimeOut: 0
    trafficType: string

- name: Delete by name
  cisco.dnac.wireless_enterprise_ssid:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    ssidName: string
```

## [Return Values](wireless_enterprise_ssid_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
