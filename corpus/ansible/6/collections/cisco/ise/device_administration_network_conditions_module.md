---
collection: ansible
version: "6"
title: "cisco.ise.device_administration_network_conditions module – Resource module for Device Administration Network Conditions"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/device_administration_network_conditions_module.html
fetched_at: 2026-07-27T16:56:46+00:00
---
# cisco.ise.device_administration_network_conditions module – Resource module for Device Administration Network Conditions

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
> see [Requirements](device_administration_network_conditions_module.md#ansible-collections-cisco-ise-device-administration-network-conditions-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.device_administration_network_conditions`.

New in cisco.ise 1.0.0

- [Synopsis](device_administration_network_conditions_module.md#synopsis)
- [Requirements](device_administration_network_conditions_module.md#requirements)
- [Parameters](device_administration_network_conditions_module.md#parameters)
- [Notes](device_administration_network_conditions_module.md#notes)
- [See Also](device_administration_network_conditions_module.md#see-also)
- [Examples](device_administration_network_conditions_module.md#examples)
- [Return Values](device_administration_network_conditions_module.md#return-values)

## [Synopsis](device_administration_network_conditions_module.md#id1)

- Manage operations create, update and delete of the resource Device Administration Network Conditions.
- Device Admin- Creates network condition.
- Device Admin - Delete network condition.
- Device Admin - Update network condition.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](device_administration_network_conditions_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](device_administration_network_conditions_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **conditions**  list / elements=dictionary | Device Administration Network Conditions’s conditions. |
| **cliDnisList**  list / elements=string | <p>This field should contain a Caller ID (CLI), comma, and Called ID (DNIS).<br> Line format - Caller ID (CLI), Called ID (DNIS)</p>. |
| **conditionType**  string | This field determines the content of the conditions field. |
| **description**  string | Device Administration Network Conditions’s description. |
| **deviceGroupList**  list / elements=string | <p>This field should contain a tuple with NDG Root, comma, and an NDG (that it under the root).<br> Line format - NDG Root Name, NDG, Port</p>. |
| **deviceList**  list / elements=string | <p>This field should contain Device-Name,port-number. The device name must be the same as the name field in a Network Device object.<br> Line format - Device Name,Port</p>. |
| **id**  string | Device Administration Network Conditions’s id. |
| **ipAddrList**  list / elements=string | <p>This field should contain IP-address-or-subnet,port number<br> IP address can be IPV4 format (n.n.n.n) or IPV6 format (n n n n n n n n).<br> IP subnet can be IPV4 format (n.n.n.n/m) or IPV6 format (n n n n n n n n/m).<br> Line format - IP Address or subnet,Port</p>. |
| **link**  dictionary | Device Administration Network Conditions’s link. |
| **href**  string | Device Administration Network Conditions’s href. |
| **rel**  string | Device Administration Network Conditions’s rel. |
| **type**  string | Device Administration Network Conditions’s type. |
| **macAddrList**  list / elements=string | <p>This field should contain Endstation MAC address, comma, and Destination MAC addresses.<br> Each Max address must include twelve hexadecimal digits using formats nn nn nn nn nn nn or nn-nn-nn-nn-nn-nn or nnnn.nnnn.nnnn or nnnnnnnnnnnn.<br> Line format - Endstation MAC,Destination MAC </p>. |
| **name**  string | Network Condition name. |
| **conditionType**  string | This field determines the content of the conditions field. |
| **description**  string | Device Administration Network Conditions’s description. |
| **id**  string | Device Administration Network Conditions’s id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **link**  dictionary | Device Administration Network Conditions’s link. |
| **href**  string | Device Administration Network Conditions’s href. |
| **rel**  string | Device Administration Network Conditions’s rel. |
| **type**  string | Device Administration Network Conditions’s type. |
| **name**  string | Network Condition name. |

## [Notes](device_administration_network_conditions_module.md#id4)

> **Note:**
>
> - SDK Method used are device_administration_network_conditions.DeviceAdministrationNetworkConditions.create_device_admin_network_condition, device_administration_network_conditions.DeviceAdministrationNetworkConditions.delete_device_admin_network_condition_by_id, device_administration_network_conditions.DeviceAdministrationNetworkConditions.update_device_admin_network_condition_by_id,
> - Paths used are post /device-admin/network-condition, delete /device-admin/network-condition/{id}, put /device-admin/network-condition/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [See Also](device_administration_network_conditions_module.md#id5)

> **See also:**
>
> [Cisco ISE documentation for Device Administration - Network Conditions](https://developer.cisco.com/docs/identity-services-engine/v1/#!policy-openapi)
> :   Complete reference of the Device Administration - Network Conditions API.

## [Examples](device_administration_network_conditions_module.md#id6)

```yaml+jinja
- name: Create
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    conditionType: string
    conditions:
    - cliDnisList:
      - string
      conditionType: string
      description: string
      deviceGroupList:
      - string
      deviceList:
      - string
      id: string
      ipAddrList:
      - string
      link:
        href: string
        rel: string
        type: string
      macAddrList:
      - string
      name: string
    description: string
    id: string
    link:
      href: string
      rel: string
      type: string
    name: string

- name: Update by id
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    conditionType: string
    conditions:
    - cliDnisList:
      - string
      conditionType: string
      description: string
      deviceGroupList:
      - string
      deviceList:
      - string
      id: string
      ipAddrList:
      - string
      link:
        href: string
        rel: string
        type: string
      macAddrList:
      - string
      name: string
    description: string
    id: string
    link:
      href: string
      rel: string
      type: string
    name: string

- name: Delete by id
  cisco.ise.device_administration_network_conditions:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string
```

## [Return Values](device_administration_network_conditions_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"conditionType": "string", "conditions": [{"cliDnisList": ["string"], "conditionType": "string", "description": "string", "deviceGroupList": ["string"], "deviceList": ["string"], "id": "string", "ipAddrList": ["string"], "link": {"href": "string", "rel": "string", "type": "string"}, "macAddrList": ["string"], "name": "string"}], "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string"}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"response": {"conditionType": "string", "conditions": [{"cliDnisList": ["string"], "conditionType": "string", "description": "string", "deviceGroupList": ["string"], "deviceList": ["string"], "id": "string", "ipAddrList": ["string"], "link": {"href": "string", "rel": "string", "type": "string"}, "macAddrList": ["string"], "name": "string"}], "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
