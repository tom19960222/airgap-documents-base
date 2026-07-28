---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_casb_profile module – Configure CASB profile in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_casb_profile_module.html
fetched_at: 2026-07-28T02:23:27+00:00
---
# fortinet.fortios.fortios_casb_profile module – Configure CASB profile in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_casb_profile_module.md#ansible-collections-fortinet-fortios-fortios-casb-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_casb_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_casb_profile_module.md#synopsis)
- [Requirements](fortios_casb_profile_module.md#requirements)
- [Parameters](fortios_casb_profile_module.md#parameters)
- [Notes](fortios_casb_profile_module.md#notes)
- [Examples](fortios_casb_profile_module.md#examples)
- [Return Values](fortios_casb_profile_module.md#return-values)

## [Synopsis](fortios_casb_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify casb feature and profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_casb_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_casb_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **casb_profile**  dictionary | Configure CASB profile. |
| **name**  string / required | CASB profile name. |
| **saas_application**  list / elements=dictionary | CASB profile SaaS application. |
| **access_rule**  list / elements=dictionary | CASB profile access rule. |
| **action**  string | CASB access rule action.  **Choices:**   - `"bypass"` - `"block"` - `"monitor"` |
| **bypass**  list / elements=string | CASB bypass options.  **Choices:**   - `"av"` - `"dlp"` - `"web-filter"` - `"file-filter"` - `"video-filter"` |
| **name**  string / required | CASB access rule activity name. Source casb.user-activity.name. |
| **custom_control**  list / elements=dictionary | CASB profile custom control. |
| **name**  string / required | CASB custom control user activity name. Source casb.user-activity.name. |
| **option**  list / elements=dictionary | CASB custom control option. |
| **name**  string / required | CASB custom control option name. |
| **user_input**  list / elements=dictionary | CASB custom control user input. |
| **value**  string / required | user input value. |
| **domain_control**  string | Enable/disable domain control.  **Choices:**   - `"enable"` - `"disable"` |
| **domain_control_domains**  list / elements=dictionary | CASB profile domain control domains. |
| **name**  string / required | Domain control domain name. |
| **log**  string | Enable/disable log settings.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | CASB profile SaaS application name. Source casb.saas-application.name. |
| **safe_search**  string | Enable/disable safe search.  **Choices:**   - `"enable"` - `"disable"` |
| **safe_search_control**  list / elements=dictionary | CASB profile safe search control. |
| **name**  string / required | Safe search control name. |
| **tenant_control**  string | Enable/disable tenant control.  **Choices:**   - `"enable"` - `"disable"` |
| **tenant_control_tenants**  list / elements=dictionary | CASB profile tenant control tenants. |
| **name**  string / required | Tenant control tenants name. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_casb_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_casb_profile_module.md#id5)

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
  - name: Configure CASB profile.
    fortios_casb_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      casb_profile:
        name: "default_name_3"
        saas_application:
         -
            access_rule:
             -
                action: "bypass"
                bypass: "av"
                name: "default_name_8 (source casb.user-activity.name)"
            custom_control:
             -
                name: "default_name_10 (source casb.user-activity.name)"
                option:
                 -
                    name: "default_name_12"
                    user_input:
                     -
                        value: "<your_own_value>"
            domain_control: "enable"
            domain_control_domains:
             -
                name: "default_name_17"
            log: "enable"
            name: "default_name_19 (source casb.saas-application.name)"
            safe_search: "enable"
            safe_search_control:
             -
                name: "default_name_22"
            tenant_control: "enable"
            tenant_control_tenants:
             -
                name: "default_name_25"
```

## [Return Values](fortios_casb_profile_module.md#id6)

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
