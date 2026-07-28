---
collection: ansible
version: "6"
title: "cisco.dnac.wireless_provision_ssid_create_provision module – Resource module for Wireless Provision Ssid Create Provision"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/wireless_provision_ssid_create_provision_module.html
fetched_at: 2026-07-27T16:54:55+00:00
---
# cisco.dnac.wireless_provision_ssid_create_provision module – Resource module for Wireless Provision Ssid Create Provision

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
> see [Requirements](wireless_provision_ssid_create_provision_module.md#ansible-collections-cisco-dnac-wireless-provision-ssid-create-provision-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.wireless_provision_ssid_create_provision`.

New in cisco.dnac 3.1.0

- [Synopsis](wireless_provision_ssid_create_provision_module.md#synopsis)
- [Requirements](wireless_provision_ssid_create_provision_module.md#requirements)
- [Parameters](wireless_provision_ssid_create_provision_module.md#parameters)
- [Notes](wireless_provision_ssid_create_provision_module.md#notes)
- [See Also](wireless_provision_ssid_create_provision_module.md#see-also)
- [Examples](wireless_provision_ssid_create_provision_module.md#examples)
- [Return Values](wireless_provision_ssid_create_provision_module.md#return-values)

## [Synopsis](wireless_provision_ssid_create_provision_module.md#id1)

- Manage operation create of the resource Wireless Provision Ssid Create Provision.
- Creates SSID, updates the SSID to the corresponding site profiles and provision it to the devices matching the given sites.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](wireless_provision_ssid_create_provision_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](wireless_provision_ssid_create_provision_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **enableFabric**  boolean | Enable SSID for Fabric.  Choices:   - `false` - `true` |
| **flexConnect**  dictionary | Wireless Provision Ssid Create Provision’s flexConnect. |
| **enableFlexConnect**  boolean | Enable Flex Connect.  Choices:   - `false` - `true` |
| **localToVlan**  integer | Local To Vlan (range is 1 to 4094). |
| **headers**  dictionary | Additional headers. |
| **managedAPLocations**  list / elements=string | Managed AP Locations (Enter entire Site(s) hierarchy). |
| **ssidDetails**  dictionary | Wireless Provision Ssid Create Provision’s ssidDetails. |
| **enableBroadcastSSID**  boolean | Enable Broadcast SSID.  Choices:   - `false` - `true` |
| **enableFastLane**  boolean | Enable Fast Lane.  Choices:   - `false` - `true` |
| **enableMACFiltering**  boolean | Enable MAC Filtering.  Choices:   - `false` - `true` |
| **fastTransition**  string | Fast Transition. |
| **name**  string | SSID Name. |
| **passphrase**  string | Pass Phrase ( Only applicable for SSID with PERSONAL auth type ). |
| **radioPolicy**  string | Radio Policy. Allowed values are ‘Dual band operation (2.4GHz and 5GHz)’, ‘Dual band operation with band select’, ‘5GHz only’, ‘2.4GHz only’. |
| **securityLevel**  string | Security Level(For guest SSID OPEN/WEB_AUTH, For Enterprise SSID ENTERPRISE/PERSONAL/OPEN). |
| **trafficType**  string | Traffic Type. |
| **webAuthURL**  string | Web Auth URL. |
| **ssidType**  string | SSID Type. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](wireless_provision_ssid_create_provision_module.md#id4)

> **Note:**
>
> - SDK Method used are wireless.Wireless.create_and_provision_ssid,
> - Paths used are post /dna/intent/api/v1/business/ssid,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](wireless_provision_ssid_create_provision_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Wireless CreateAndProvisionSSID](https://developer.cisco.com/docs/dna-center/#!create-and-provision-ssid)
> :   Complete reference of the CreateAndProvisionSSID API.

## [Examples](wireless_provision_ssid_create_provision_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.wireless_provision_ssid_create_provision:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    enableFabric: true
    flexConnect:
      enableFlexConnect: true
      localToVlan: 0
    headers: '{{my_headers | from_json}}'
    managedAPLocations:
    - string
    ssidDetails:
      enableBroadcastSSID: true
      enableFastLane: true
      enableMACFiltering: true
      fastTransition: string
      name: string
      passphrase: string
      radioPolicy: string
      securityLevel: string
      trafficType: string
      webAuthURL: string
    ssidType: string
```

## [Return Values](wireless_provision_ssid_create_provision_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
