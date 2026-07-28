---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_switch_interface module – Configure software switch interfaces by grouping physical and WiFi interfaces in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_switch_interface_module.html
fetched_at: 2026-07-28T02:29:35+00:00
---
# fortinet.fortios.fortios_system_switch_interface module – Configure software switch interfaces by grouping physical and WiFi interfaces in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortios/) (version 2.3.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_system_switch_interface_module.md#ansible-collections-fortinet-fortios-fortios-system-switch-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_switch_interface`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_switch_interface_module.md#synopsis)
- [Requirements](fortios_system_switch_interface_module.md#requirements)
- [Parameters](fortios_system_switch_interface_module.md#parameters)
- [Notes](fortios_system_switch_interface_module.md#notes)
- [Examples](fortios_system_switch_interface_module.md#examples)
- [Return Values](fortios_system_switch_interface_module.md#return-values)

## [Synopsis](fortios_system_switch_interface_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and switch_interface category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_switch_interface_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_switch_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_switch_interface**  dictionary | Configure software switch interfaces by grouping physical and WiFi interfaces. |
| **intra_switch_policy**  string | Allow any traffic between switch interfaces or require firewall policies to allow traffic between switch interfaces.  **Choices:**   - `"implicit"` - `"explicit"` |
| **mac_ttl**  integer | Duration for which MAC addresses are held in the ARP table (300 - 8640000 sec). |
| **member**  list / elements=dictionary | Names of the interfaces that belong to the virtual switch. |
| **interface_name**  string / required | Physical interface name. Source system.interface.name. |
| **name**  string / required | Interface name (name cannot be in use by any other interfaces, VLANs, or inter-VDOM links). |
| **span**  string | Enable/disable port spanning. Port spanning echoes traffic received by the software switch to the span destination port.  **Choices:**   - `"disable"` - `"enable"` |
| **span_dest_port**  string | SPAN destination port name. All traffic on the SPAN source ports is echoed to the SPAN destination port. Source system.interface.name. |
| **span_direction**  string | The direction in which the SPAN port operates, either: rx, tx, or both.  **Choices:**   - `"rx"` - `"tx"` - `"both"` |
| **span_source_port**  list / elements=dictionary | Physical interface name. Port spanning echoes all traffic on the SPAN source ports to the SPAN destination port. |
| **interface_name**  string / required | Physical interface name. Source system.interface.name. |
| **type**  string | Type of switch based on functionality: switch for normal functionality, or hub to duplicate packets to all port members.  **Choices:**   - `"switch"` - `"hub"` |
| **vdom**  string | VDOM that the software switch belongs to. Source system.vdom.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_switch_interface_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_switch_interface_module.md#id5)

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
  - name: Configure software switch interfaces by grouping physical and WiFi interfaces.
    fortios_system_switch_interface:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_switch_interface:
        intra_switch_policy: "implicit"
        mac_ttl: "300"
        member:
         -
            interface_name: "<your_own_value> (source system.interface.name)"
        name: "default_name_7"
        span: "disable"
        span_dest_port: "<your_own_value> (source system.interface.name)"
        span_direction: "rx"
        span_source_port:
         -
            interface_name: "<your_own_value> (source system.interface.name)"
        type: "switch"
        vdom: "<your_own_value> (source system.vdom.name)"
```

## [Return Values](fortios_system_switch_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  **Returned:** always  **Sample:** `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  **Returned:** always  **Sample:** `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  **Returned:** always  **Sample:** `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  **Returned:** success  **Sample:** `"id"` |
| **name**  string | Name of the table used to fulfill the request  **Returned:** always  **Sample:** `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  **Returned:** always  **Sample:** `"webfilter"` |
| **revision**  string | Internal revision number  **Returned:** always  **Sample:** `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  **Returned:** always  **Sample:** `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  **Returned:** always  **Sample:** `"success"` |
| **vdom**  string | Virtual domain used  **Returned:** always  **Sample:** `"root"` |
| **version**  string | Version of the FortiGate  **Returned:** always  **Sample:** `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
- [Homepage](https://www.fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
