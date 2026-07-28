---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_wireless_controller_apcfg_profile module – Configure AP local configuration profiles in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_wireless_controller_apcfg_profile_module.html
fetched_at: 2026-07-28T02:31:00+00:00
---
# fortinet.fortios.fortios_wireless_controller_apcfg_profile module – Configure AP local configuration profiles in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_wireless_controller_apcfg_profile_module.md#ansible-collections-fortinet-fortios-fortios-wireless-controller-apcfg-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_wireless_controller_apcfg_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_wireless_controller_apcfg_profile_module.md#synopsis)
- [Requirements](fortios_wireless_controller_apcfg_profile_module.md#requirements)
- [Parameters](fortios_wireless_controller_apcfg_profile_module.md#parameters)
- [Notes](fortios_wireless_controller_apcfg_profile_module.md#notes)
- [Examples](fortios_wireless_controller_apcfg_profile_module.md#examples)
- [Return Values](fortios_wireless_controller_apcfg_profile_module.md#return-values)

## [Synopsis](fortios_wireless_controller_apcfg_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify wireless_controller feature and apcfg_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_wireless_controller_apcfg_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_wireless_controller_apcfg_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **wireless_controller_apcfg_profile**  dictionary | Configure AP local configuration profiles. |
| **ac_ip**  string | IP address of the validation controller that AP must be able to join after applying AP local configuration. |
| **ac_port**  integer | Port of the validation controller that AP must be able to join after applying AP local configuration (1024 - 49150). |
| **ac_timer**  integer | Maximum waiting time for the AP to join the validation controller after applying AP local configuration (3 - 30 min). |
| **ac_type**  string | Validation controller type .  **Choices:**   - `"default"` - `"specify"` - `"apcfg"` |
| **ap_family**  string | FortiAP family type .  **Choices:**   - `"fap"` - `"fap-u"` - `"fap-c"` |
| **command_list**  list / elements=dictionary | AP local configuration command list. |
| **id**  integer / required | Command ID. see <a href=’#notes’>Notes</a>. |
| **name**  string | AP local configuration command name. |
| **passwd_value**  string | AP local configuration command password value. |
| **type**  string | The command type .  **Choices:**   - `"non-password"` - `"password"` |
| **value**  string | AP local configuration command value. |
| **comment**  string | Comment. |
| **name**  string / required | AP local configuration profile name. |

## [Notes](fortios_wireless_controller_apcfg_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_wireless_controller_apcfg_profile_module.md#id5)

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
  - name: Configure AP local configuration profiles.
    fortios_wireless_controller_apcfg_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      wireless_controller_apcfg_profile:
        ac_ip: "<your_own_value>"
        ac_port: "0"
        ac_timer: "10"
        ac_type: "default"
        ap_family: "fap"
        command_list:
         -
            id:  "9"
            name: "default_name_10"
            passwd_value: "<your_own_value>"
            type: "non-password"
            value: "<your_own_value>"
        comment: "Comment."
        name: "default_name_15"
```

## [Return Values](fortios_wireless_controller_apcfg_profile_module.md#id6)

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
