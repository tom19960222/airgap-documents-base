---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_switch_controller_security_policy_802_1x module – Configure 802.1x MAC Authentication Bypass (MAB) policies in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_switch_controller_security_policy_802_1x_module.html
fetched_at: 2026-07-27T17:43:45+00:00
---
# fortinet.fortios.fortios_switch_controller_security_policy_802_1x module – Configure 802.1x MAC Authentication Bypass (MAB) policies in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_security_policy_802_1x_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-security-policy-802-1x-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_security_policy_802_1x`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_security_policy_802_1x_module.md#synopsis)
- [Requirements](fortios_switch_controller_security_policy_802_1x_module.md#requirements)
- [Parameters](fortios_switch_controller_security_policy_802_1x_module.md#parameters)
- [Notes](fortios_switch_controller_security_policy_802_1x_module.md#notes)
- [Examples](fortios_switch_controller_security_policy_802_1x_module.md#examples)
- [Return Values](fortios_switch_controller_security_policy_802_1x_module.md#return-values)

## [Synopsis](fortios_switch_controller_security_policy_802_1x_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller_security_policy feature and 802_1x category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_security_policy_802_1x_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_switch_controller_security_policy_802_1x_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **switch_controller_security_policy_802_1x**  dictionary | Configure 802.1x MAC Authentication Bypass (MAB) policies. |
| **auth_fail_vlan**  string | Enable to allow limited access to clients that cannot authenticate.  Choices:   - `"disable"` - `"enable"` |
| **auth_fail_vlan_id**  string | VLAN ID on which authentication failed. Source system.interface.name. |
| **auth_fail_vlanid**  integer | VLAN ID on which authentication failed. |
| **authserver_timeout_period**  integer | Authentication server timeout period (3 - 15 sec). |
| **authserver_timeout_vlan**  string | Enable/disable the authentication server timeout VLAN to allow limited access when RADIUS is unavailable.  Choices:   - `"disable"` - `"enable"` |
| **authserver_timeout_vlanid**  string | Authentication server timeout VLAN name. Source system.interface.name. |
| **eap_auto_untagged_vlans**  string | Enable/disable automatic inclusion of untagged VLANs.  Choices:   - `"disable"` - `"enable"` |
| **eap_passthru**  string | Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass through ports for more flexible authentication.  Choices:   - `"disable"` - `"enable"` |
| **framevid_apply**  string | Enable/disable the capability to apply the EAP/MAB frame VLAN to the port native VLAN.  Choices:   - `"disable"` - `"enable"` |
| **guest_auth_delay**  integer | Guest authentication delay (1 - 900 sec). |
| **guest_vlan**  string | Enable the guest VLAN feature to allow limited access to non-802.1X-compliant clients.  Choices:   - `"disable"` - `"enable"` |
| **guest_vlan_id**  string | Guest VLAN name. Source system.interface.name. |
| **guest_vlanid**  integer | Guest VLAN ID. |
| **mac_auth_bypass**  string | Enable/disable MAB for this policy.  Choices:   - `"disable"` - `"enable"` |
| **name**  string / required | Policy name. |
| **open_auth**  string | Enable/disable open authentication for this policy.  Choices:   - `"disable"` - `"enable"` |
| **policy_type**  string | Policy type.  Choices:   - `"802.1X"` |
| **radius_timeout_overwrite**  string | Enable to override the global RADIUS session timeout.  Choices:   - `"disable"` - `"enable"` |
| **security_mode**  string | Port or MAC based 802.1X security mode.  Choices:   - `"802.1X"` - `"802.1X-mac-based"` |
| **user_group**  list / elements=dictionary | Name of user-group to assign to this MAC Authentication Bypass (MAB) policy. |
| **name**  string | Group name. Source user.group.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_switch_controller_security_policy_802_1x_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_security_policy_802_1x_module.md#id5)

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
  - name: Configure 802.1x MAC Authentication Bypass (MAB) policies.
    fortios_switch_controller_security_policy_802_1x:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_security_policy_802_1x:
        auth_fail_vlan: "disable"
        auth_fail_vlan_id: "<your_own_value> (source system.interface.name)"
        auth_fail_vlanid: "32767"
        authserver_timeout_period: "3"
        authserver_timeout_vlan: "disable"
        authserver_timeout_vlanid: "<your_own_value> (source system.interface.name)"
        eap_auto_untagged_vlans: "disable"
        eap_passthru: "disable"
        framevid_apply: "disable"
        guest_auth_delay: "30"
        guest_vlan: "disable"
        guest_vlan_id: "<your_own_value> (source system.interface.name)"
        guest_vlanid: "32767"
        mac_auth_bypass: "disable"
        name: "default_name_17"
        open_auth: "disable"
        policy_type: "802.1X"
        radius_timeout_overwrite: "disable"
        security_mode: "802.1X"
        user_group:
         -
            name: "default_name_23 (source user.group.name)"
```

## [Return Values](fortios_switch_controller_security_policy_802_1x_module.md#id6)

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
