---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_switch_controller_lldp_profile module – Configure FortiSwitch LLDP profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_switch_controller_lldp_profile_module.html
fetched_at: 2026-07-27T17:43:30+00:00
---
# fortinet.fortios.fortios_switch_controller_lldp_profile module – Configure FortiSwitch LLDP profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_lldp_profile_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-lldp-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_lldp_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_lldp_profile_module.md#synopsis)
- [Requirements](fortios_switch_controller_lldp_profile_module.md#requirements)
- [Parameters](fortios_switch_controller_lldp_profile_module.md#parameters)
- [Notes](fortios_switch_controller_lldp_profile_module.md#notes)
- [Examples](fortios_switch_controller_lldp_profile_module.md#examples)
- [Return Values](fortios_switch_controller_lldp_profile_module.md#return-values)

## [Synopsis](fortios_switch_controller_lldp_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and lldp_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_lldp_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_switch_controller_lldp_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **switch_controller_lldp_profile**  dictionary | Configure FortiSwitch LLDP profiles. |
| **auto_isl**  string | Enable/disable auto inter-switch LAG.  Choices:   - `"disable"` - `"enable"` |
| **auto_isl_hello_timer**  integer | Auto inter-switch LAG hello timer duration (1 - 30 sec). |
| **auto_isl_port_group**  integer | Auto inter-switch LAG port group ID (0 - 9). |
| **auto_isl_receive_timeout**  integer | Auto inter-switch LAG timeout if no response is received (3 - 90 sec). |
| **auto_mclag_icl**  string | Enable/disable MCLAG inter chassis link.  Choices:   - `"disable"` - `"enable"` |
| **custom_tlvs**  list / elements=dictionary | Configuration method to edit custom TLV entries. |
| **information_string**  string | Organizationally defined information string (0 - 507 hexadecimal bytes). |
| **name**  string | TLV name (not sent). |
| **oui**  string | Organizationally unique identifier (OUI), a 3-byte hexadecimal number, for this TLV. |
| **subtype**  integer | Organizationally defined subtype (0 - 255). |
| **med_location_service**  list / elements=dictionary | Configuration method to edit Media Endpoint Discovery (MED) location service type-length-value (TLV) categories. |
| **name**  string | Location service type name. |
| **status**  string | Enable or disable this TLV.  Choices:   - `"disable"` - `"enable"` |
| **sys_location_id**  string | Location service ID. Source switch-controller.location.name. |
| **med_network_policy**  list / elements=dictionary | Configuration method to edit Media Endpoint Discovery (MED) network policy type-length-value (TLV) categories. |
| **assign_vlan**  string | Enable/disable VLAN assignment when this profile is applied on managed FortiSwitch port.  Choices:   - `"disable"` - `"enable"` |
| **dscp**  integer | Advertised Differentiated Services Code Point (DSCP) value, a packet header value indicating the level of service requested for traffic, such as high priority or best effort delivery. |
| **name**  string | Policy type name. |
| **priority**  integer | Advertised Layer 2 priority (0 - 7; from lowest to highest priority). |
| **status**  string | Enable or disable this TLV.  Choices:   - `"disable"` - `"enable"` |
| **vlan**  integer | ID of VLAN to advertise, if configured on port (0 - 4094, 0 = priority tag). |
| **vlan_intf**  string | VLAN interface to advertise; if configured on port. Source system.interface.name. |
| **med_tlvs**  list / elements=string | Transmitted LLDP-MED TLVs (type-length-value descriptions).  Choices:   - `"inventory-management"` - `"network-policy"` - `"power-management"` - `"location-identification"` |
| **name**  string / required | Profile name. |
| **tlvs_802dot1**  list / elements=string | Transmitted IEEE 802.1 TLVs.  Choices:   - `"port-vlan-id"` |
| **tlvs_802dot3**  list / elements=string | Transmitted IEEE 802.3 TLVs.  Choices:   - `"max-frame-size"` - `"power-negotiation"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_switch_controller_lldp_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_lldp_profile_module.md#id5)

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
  - name: Configure FortiSwitch LLDP profiles.
    fortios_switch_controller_lldp_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_lldp_profile:
        tlvs_802dot1: "port-vlan-id"
        tlvs_802dot3: "max-frame-size"
        auto_isl: "disable"
        auto_isl_hello_timer: "3"
        auto_isl_port_group: "0"
        auto_isl_receive_timeout: "60"
        auto_mclag_icl: "disable"
        custom_tlvs:
         -
            information_string: "<your_own_value>"
            name: "default_name_12"
            oui: "<your_own_value>"
            subtype: "0"
        med_location_service:
         -
            name: "default_name_16"
            status: "disable"
            sys_location_id: "<your_own_value> (source switch-controller.location.name)"
        med_network_policy:
         -
            assign_vlan: "disable"
            dscp: "0"
            name: "default_name_22"
            priority: "0"
            status: "disable"
            vlan: "2047"
            vlan_intf: "<your_own_value> (source system.interface.name)"
        med_tlvs: "inventory-management"
        name: "default_name_28"
```

## [Return Values](fortios_switch_controller_lldp_profile_module.md#id6)

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
