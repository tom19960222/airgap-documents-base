---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_switch_controller_dynamic_port_policy module – Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_switch_controller_dynamic_port_policy_module.html
fetched_at: 2026-07-27T17:43:25+00:00
---
# fortinet.fortios.fortios_switch_controller_dynamic_port_policy module – Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_dynamic_port_policy_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-dynamic-port-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_dynamic_port_policy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_dynamic_port_policy_module.md#synopsis)
- [Requirements](fortios_switch_controller_dynamic_port_policy_module.md#requirements)
- [Parameters](fortios_switch_controller_dynamic_port_policy_module.md#parameters)
- [Notes](fortios_switch_controller_dynamic_port_policy_module.md#notes)
- [Examples](fortios_switch_controller_dynamic_port_policy_module.md#examples)
- [Return Values](fortios_switch_controller_dynamic_port_policy_module.md#return-values)

## [Synopsis](fortios_switch_controller_dynamic_port_policy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and dynamic_port_policy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_dynamic_port_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_switch_controller_dynamic_port_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **switch_controller_dynamic_port_policy**  dictionary | Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device. |
| **description**  string | Description for the Dynamic port policy. |
| **fortilink**  string | FortiLink interface for which this Dynamic port policy belongs to. Source system.interface.name. |
| **name**  string / required | Dynamic port policy name. |
| **policy**  list / elements=dictionary | Port policies with matching criteria and actions. |
| **bounce_port_link**  string | Enable/disable bouncing (administratively bring the link down, up) of a switch port where this policy is applied. Helps to clear and reassign VLAN from lldp-profile.  Choices:   - `"disable"` - `"enable"` |
| **category**  string | Category of Dynamic port policy.  Choices:   - `"device"` - `"interface-tag"` |
| **description**  string | Description for the policy. |
| **family**  string | Match policy based on family. |
| **host**  string | Match policy based on host. |
| **hw_vendor**  string | Match policy based on hardware vendor. |
| **interface_tags**  list / elements=dictionary | Match policy based on the FortiSwitch interface object tags. |
| **tag_name**  string | FortiSwitch port tag name. Source switch-controller.switch-interface-tag.name. |
| **lldp_profile**  string | LLDP profile to be applied when using this policy. Source switch-controller.lldp-profile.name. |
| **mac**  string | Match policy based on MAC address. |
| **name**  string | Policy name. |
| **qos_policy**  string | QoS policy to be applied when using this policy. Source switch-controller.qos.qos-policy.name. |
| **set_802_1x**  string | 802.1x security policy to be applied when using this policy. Source switch-controller.security-policy.802-1X.name switch-controller.security-policy.captive-portal.name. |
| **status**  string | Enable/disable policy.  Choices:   - `"enable"` - `"disable"` |
| **type**  string | Match policy based on type. |
| **vlan_policy**  string | VLAN policy to be applied when using this policy. Source switch-controller.vlan-policy.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_switch_controller_dynamic_port_policy_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_dynamic_port_policy_module.md#id5)

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
  - name: Configure Dynamic port policy to be applied on the managed FortiSwitch ports through DPP device.
    fortios_switch_controller_dynamic_port_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_dynamic_port_policy:
        description: "<your_own_value>"
        fortilink: "<your_own_value> (source system.interface.name)"
        name: "default_name_5"
        policy:
         -
            set_802_1x: "<your_own_value> (source switch-controller.security-policy.802-1X.name switch-controller.security-policy.captive-portal.name)"
            bounce_port_link: "disable"
            category: "device"
            description: "<your_own_value>"
            family: "<your_own_value>"
            host: "myhostname"
            hw_vendor: "<your_own_value>"
            interface_tags:
             -
                tag_name: "<your_own_value> (source switch-controller.switch-interface-tag.name)"
            lldp_profile: "<your_own_value> (source switch-controller.lldp-profile.name)"
            mac: "<your_own_value>"
            name: "default_name_18"
            qos_policy: "<your_own_value> (source switch-controller.qos.qos-policy.name)"
            status: "enable"
            type: "<your_own_value>"
            vlan_policy: "<your_own_value> (source switch-controller.vlan-policy.name)"
```

## [Return Values](fortios_switch_controller_dynamic_port_policy_module.md#id6)

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
