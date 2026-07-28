---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_switch_controller_vlan module – Configure VLANs for switch controller in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_switch_controller_vlan_module.html
fetched_at: 2026-07-28T02:27:47+00:00
---
# fortinet.fortios.fortios_switch_controller_vlan module – Configure VLANs for switch controller in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_switch_controller_vlan_module.md#ansible-collections-fortinet-fortios-fortios-switch-controller-vlan-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_switch_controller_vlan`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_switch_controller_vlan_module.md#synopsis)
- [Requirements](fortios_switch_controller_vlan_module.md#requirements)
- [Parameters](fortios_switch_controller_vlan_module.md#parameters)
- [Notes](fortios_switch_controller_vlan_module.md#notes)
- [Examples](fortios_switch_controller_vlan_module.md#examples)
- [Return Values](fortios_switch_controller_vlan_module.md#return-values)

## [Synopsis](fortios_switch_controller_vlan_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify switch_controller feature and vlan category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_switch_controller_vlan_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_switch_controller_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **switch_controller_vlan**  dictionary | Configure VLANs for switch controller. |
| **auth**  string | Authentication.  **Choices:**   - `"radius"` - `"usergroup"` |
| **color**  integer | Color of icon on the GUI. |
| **comments**  string | Comment. |
| **name**  string / required | Switch VLAN name. |
| **portal_message_override_group**  string | Specify captive portal replacement message override group. |
| **portal_message_overrides**  dictionary | Individual message overrides. |
| **auth_disclaimer_page**  string | Override auth-disclaimer-page message with message from portal-message-overrides group. |
| **auth_login_failed_page**  string | Override auth-login-failed-page message with message from portal-message-overrides group. |
| **auth_login_page**  string | Override auth-login-page message with message from portal-message-overrides group. |
| **auth_reject_page**  string | Override auth-reject-page message with message from portal-message-overrides group. |
| **radius_server**  string | Authentication radius server. Source user.radius.name. |
| **security**  string | Security.  **Choices:**   - `"open"` - `"captive-portal"` - `"8021x"` |
| **selected_usergroups**  list / elements=dictionary | Selected user group. |
| **name**  string / required | User group name. Source user.group.name. |
| **usergroup**  string | Authentication usergroup. Source user.group.name. |
| **vdom**  string | Virtual domain, |
| **vlanid**  integer | VLAN ID. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_switch_controller_vlan_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_switch_controller_vlan_module.md#id5)

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
  - name: Configure VLANs for switch controller.
    fortios_switch_controller_vlan:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      switch_controller_vlan:
        auth: "radius"
        color: "16"
        comments: "<your_own_value>"
        name: "default_name_6"
        portal_message_override_group: "<your_own_value>"
        portal_message_overrides:
            auth_disclaimer_page: "<your_own_value>"
            auth_login_failed_page: "<your_own_value>"
            auth_login_page: "<your_own_value>"
            auth_reject_page: "<your_own_value>"
        radius_server: "<your_own_value> (source user.radius.name)"
        security: "open"
        selected_usergroups:
         -
            name: "default_name_16 (source user.group.name)"
        usergroup: "<your_own_value> (source user.group.name)"
        vdom: "<your_own_value>"
        vlanid: "2047"
```

## [Return Values](fortios_switch_controller_vlan_module.md#id6)

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
