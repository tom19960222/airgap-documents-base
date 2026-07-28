---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_switch_controller_snmp_community module – Configure FortiSwitch SNMP v1/v2c communities globally in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_switch_controller_snmp_community_module.html
fetched_at: 2026-07-27T17:43:49+00:00
---
# fortinet.fortios.fortios_switch_controller_snmp_community module – Configure FortiSwitch SNMP v1/v2c communities globally in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_snmp_community_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-snmp-community-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_snmp_community`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_snmp_community_module.md#synopsis)
- [Requirements](fortios_switch_controller_snmp_community_module.md#requirements)
- [Parameters](fortios_switch_controller_snmp_community_module.md#parameters)
- [Notes](fortios_switch_controller_snmp_community_module.md#notes)
- [Examples](fortios_switch_controller_snmp_community_module.md#examples)
- [Return Values](fortios_switch_controller_snmp_community_module.md#return-values)

## [Synopsis](fortios_switch_controller_snmp_community_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and snmp_community category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_snmp_community_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_switch_controller_snmp_community_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **switch_controller_snmp_community**  dictionary | Configure FortiSwitch SNMP v1/v2c communities globally. |
| **events**  list / elements=string | SNMP notifications (traps) to send.  Choices:   - `"cpu-high"` - `"mem-low"` - `"log-full"` - `"intf-ip"` - `"ent-conf-change"` |
| **hosts**  list / elements=dictionary | Configure IPv4 SNMP managers (hosts). |
| **id**  integer | Host entry ID. |
| **ip**  string | IPv4 address of the SNMP manager (host). |
| **id**  integer / required | SNMP community ID. |
| **name**  string | SNMP community name. |
| **query_v1_port**  integer | SNMP v1 query port . |
| **query_v1_status**  string | Enable/disable SNMP v1 queries.  Choices:   - `"disable"` - `"enable"` |
| **query_v2c_port**  integer | SNMP v2c query port . |
| **query_v2c_status**  string | Enable/disable SNMP v2c queries.  Choices:   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable this SNMP community.  Choices:   - `"disable"` - `"enable"` |
| **trap_v1_lport**  integer | SNMP v2c trap local port . |
| **trap_v1_rport**  integer | SNMP v2c trap remote port . |
| **trap_v1_status**  string | Enable/disable SNMP v1 traps.  Choices:   - `"disable"` - `"enable"` |
| **trap_v2c_lport**  integer | SNMP v2c trap local port . |
| **trap_v2c_rport**  integer | SNMP v2c trap remote port . |
| **trap_v2c_status**  string | Enable/disable SNMP v2c traps.  Choices:   - `"disable"` - `"enable"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_switch_controller_snmp_community_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_snmp_community_module.md#id5)

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
  - name: Configure FortiSwitch SNMP v1/v2c communities globally.
    fortios_switch_controller_snmp_community:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_snmp_community:
        events: "cpu-high"
        hosts:
         -
            id:  "5"
            ip: "<your_own_value>"
        id:  "7"
        name: "default_name_8"
        query_v1_port: "161"
        query_v1_status: "disable"
        query_v2c_port: "161"
        query_v2c_status: "disable"
        status: "disable"
        trap_v1_lport: "162"
        trap_v1_rport: "162"
        trap_v1_status: "disable"
        trap_v2c_lport: "162"
        trap_v2c_rport: "162"
        trap_v2c_status: "disable"
```

## [Return Values](fortios_switch_controller_snmp_community_module.md#id6)

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
