---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_router_policy6 module – Configure IPv6 routing policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_router_policy6_module.html
fetched_at: 2026-07-27T17:43:08+00:00
---
# fortinet.fortios.fortios_router_policy6 module – Configure IPv6 routing policies in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_router_policy6_module.md#ansible-collections-fortinet-fortios-fortios-router-policy6-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_policy6`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_policy6_module.md#synopsis)
- [Requirements](fortios_router_policy6_module.md#requirements)
- [Parameters](fortios_router_policy6_module.md#parameters)
- [Notes](fortios_router_policy6_module.md#notes)
- [Examples](fortios_router_policy6_module.md#examples)
- [Return Values](fortios_router_policy6_module.md#return-values)

## [Synopsis](fortios_router_policy6_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and policy6 category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_policy6_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_router_policy6_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **router_policy6**  dictionary | Configure IPv6 routing policies. |
| **action**  string | Action of the policy route.  Choices:   - `"deny"` - `"permit"` |
| **comments**  string | Optional comments. |
| **dst**  list / elements=dictionary | Destination IPv6 prefix. |
| **addr6**  string | IPv6 address prefix. |
| **dst_negate**  string | Enable/disable negating destination address match.  Choices:   - `"enable"` - `"disable"` |
| **dstaddr**  list / elements=dictionary | Destination address name. |
| **name**  string | Address/group name. Source . |
| **end_port**  integer | End destination port number (1 - 65535). |
| **gateway**  string | IPv6 address of the gateway. |
| **input_device**  list / elements=dictionary | Incoming interface name. Source system.interface.name. |
| **name**  string | Interface name. Source system.interface.name. |
| **input_device_negate**  string | Enable/disable negation of input device match.  Choices:   - `"enable"` - `"disable"` |
| **internet_service_custom**  list / elements=dictionary | Custom Destination Internet Service name. |
| **name**  string | Custom Destination Internet Service name. Source . |
| **internet_service_id**  list / elements=dictionary | Destination Internet Service ID. |
| **id**  integer | Destination Internet Service ID. Source . |
| **output_device**  string | Outgoing interface name. Source system.interface.name. |
| **protocol**  integer | Protocol number (0 - 255). |
| **seq_num**  integer | Sequence number(1-65535). |
| **src**  list / elements=dictionary | Source IPv6 prefix. |
| **addr6**  string | IPv6 address prefix. |
| **src_negate**  string | Enable/disable negating source address match.  Choices:   - `"enable"` - `"disable"` |
| **srcaddr**  list / elements=dictionary | Source address name. |
| **name**  string | Address/group name. Source . |
| **start_port**  integer | Start destination port number (1 - 65535). |
| **status**  string | Enable/disable this policy route.  Choices:   - `"enable"` - `"disable"` |
| **tos**  string | Type of service bit pattern. |
| **tos_mask**  string | Type of service evaluated bits. |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_router_policy6_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_policy6_module.md#id5)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure IPv6 routing policies.
    fortios_router_policy6:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      router_policy6:
        action: "deny"
        comments: "<your_own_value>"
        dst:
         -
            addr6: "<your_own_value>"
        dst_negate: "enable"
        dstaddr:
         -
            name: "default_name_9 (source )"
        end_port: "65535"
        gateway: "<your_own_value>"
        input_device:
         -
            name: "default_name_13 (source system.interface.name)"
        input_device_negate: "enable"
        internet_service_custom:
         -
            name: "default_name_16 (source )"
        internet_service_id:
         -
            id:  "18 (source )"
        output_device: "<your_own_value> (source system.interface.name)"
        protocol: "0"
        seq_num: "0"
        src:
         -
            addr6: "<your_own_value>"
        src_negate: "enable"
        srcaddr:
         -
            name: "default_name_26 (source )"
        start_port: "1"
        status: "enable"
        tos: "<your_own_value>"
        tos_mask: "<your_own_value>"
```

## [Return Values](fortios_router_policy6_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
