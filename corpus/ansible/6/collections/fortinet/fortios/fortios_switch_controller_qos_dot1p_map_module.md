---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_switch_controller_qos_dot1p_map module – Configure FortiSwitch QoS 802.1p in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_switch_controller_qos_dot1p_map_module.html
fetched_at: 2026-07-27T17:43:39+00:00
---
# fortinet.fortios.fortios_switch_controller_qos_dot1p_map module – Configure FortiSwitch QoS 802.1p in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_qos_dot1p_map_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-qos-dot1p-map-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_qos_dot1p_map`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_qos_dot1p_map_module.md#synopsis)
- [Requirements](fortios_switch_controller_qos_dot1p_map_module.md#requirements)
- [Parameters](fortios_switch_controller_qos_dot1p_map_module.md#parameters)
- [Notes](fortios_switch_controller_qos_dot1p_map_module.md#notes)
- [Examples](fortios_switch_controller_qos_dot1p_map_module.md#examples)
- [Return Values](fortios_switch_controller_qos_dot1p_map_module.md#return-values)

## [Synopsis](fortios_switch_controller_qos_dot1p_map_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller_qos feature and dot1p_map category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_qos_dot1p_map_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_switch_controller_qos_dot1p_map_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **switch_controller_qos_dot1p_map**  dictionary | Configure FortiSwitch QoS 802.1p. |
| **description**  string | Description of the 802.1p name. |
| **egress_pri_tagging**  string | Enable/disable egress priority-tag frame.  Choices:   - `"disable"` - `"enable"` |
| **name**  string / required | Dot1p map name. |
| **priority_0**  string | COS queue mapped to dot1p priority number.  Choices:   - `"queue-0"` - `"queue-1"` - `"queue-2"` - `"queue-3"` - `"queue-4"` - `"queue-5"` - `"queue-6"` - `"queue-7"` |
| **priority_1**  string | COS queue mapped to dot1p priority number.  Choices:   - `"queue-0"` - `"queue-1"` - `"queue-2"` - `"queue-3"` - `"queue-4"` - `"queue-5"` - `"queue-6"` - `"queue-7"` |
| **priority_2**  string | COS queue mapped to dot1p priority number.  Choices:   - `"queue-0"` - `"queue-1"` - `"queue-2"` - `"queue-3"` - `"queue-4"` - `"queue-5"` - `"queue-6"` - `"queue-7"` |
| **priority_3**  string | COS queue mapped to dot1p priority number.  Choices:   - `"queue-0"` - `"queue-1"` - `"queue-2"` - `"queue-3"` - `"queue-4"` - `"queue-5"` - `"queue-6"` - `"queue-7"` |
| **priority_4**  string | COS queue mapped to dot1p priority number.  Choices:   - `"queue-0"` - `"queue-1"` - `"queue-2"` - `"queue-3"` - `"queue-4"` - `"queue-5"` - `"queue-6"` - `"queue-7"` |
| **priority_5**  string | COS queue mapped to dot1p priority number.  Choices:   - `"queue-0"` - `"queue-1"` - `"queue-2"` - `"queue-3"` - `"queue-4"` - `"queue-5"` - `"queue-6"` - `"queue-7"` |
| **priority_6**  string | COS queue mapped to dot1p priority number.  Choices:   - `"queue-0"` - `"queue-1"` - `"queue-2"` - `"queue-3"` - `"queue-4"` - `"queue-5"` - `"queue-6"` - `"queue-7"` |
| **priority_7**  string | COS queue mapped to dot1p priority number.  Choices:   - `"queue-0"` - `"queue-1"` - `"queue-2"` - `"queue-3"` - `"queue-4"` - `"queue-5"` - `"queue-6"` - `"queue-7"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_switch_controller_qos_dot1p_map_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_qos_dot1p_map_module.md#id5)

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
  - name: Configure FortiSwitch QoS 802.1p.
    fortios_switch_controller_qos_dot1p_map:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_qos_dot1p_map:
        description: "<your_own_value>"
        egress_pri_tagging: "disable"
        name: "default_name_5"
        priority_0: "queue-0"
        priority_1: "queue-0"
        priority_2: "queue-0"
        priority_3: "queue-0"
        priority_4: "queue-0"
        priority_5: "queue-0"
        priority_6: "queue-0"
        priority_7: "queue-0"
```

## [Return Values](fortios_switch_controller_qos_dot1p_map_module.md#id6)

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
