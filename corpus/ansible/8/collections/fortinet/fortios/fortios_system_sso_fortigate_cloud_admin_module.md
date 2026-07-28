---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_system_sso_fortigate_cloud_admin module – Configure FortiCloud SSO admin users in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_system_sso_fortigate_cloud_admin_module.html
fetched_at: 2026-07-28T02:29:32+00:00
---
# fortinet.fortios.fortios_system_sso_fortigate_cloud_admin module – Configure FortiCloud SSO admin users in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_system_sso_fortigate_cloud_admin_module.md#ansible-collections-fortinet-fortios-fortios-system-sso-fortigate-cloud-admin-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_system_sso_fortigate_cloud_admin`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_system_sso_fortigate_cloud_admin_module.md#synopsis)
- [Requirements](fortios_system_sso_fortigate_cloud_admin_module.md#requirements)
- [Parameters](fortios_system_sso_fortigate_cloud_admin_module.md#parameters)
- [Notes](fortios_system_sso_fortigate_cloud_admin_module.md#notes)
- [Examples](fortios_system_sso_fortigate_cloud_admin_module.md#examples)
- [Return Values](fortios_system_sso_fortigate_cloud_admin_module.md#return-values)

## [Synopsis](fortios_system_sso_fortigate_cloud_admin_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify system feature and sso_fortigate_cloud_admin category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_system_sso_fortigate_cloud_admin_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_system_sso_fortigate_cloud_admin_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **system_sso_fortigate_cloud_admin**  dictionary | Configure FortiCloud SSO admin users. |
| **accprofile**  string | FortiCloud SSO admin user access profile. Source system.accprofile.name. |
| **name**  string / required | FortiCloud SSO admin name. |
| **vdom**  list / elements=dictionary | Virtual domain(s) that the administrator can access. |
| **name**  string / required | Virtual domain name. Source system.vdom.name. |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_system_sso_fortigate_cloud_admin_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_system_sso_fortigate_cloud_admin_module.md#id5)

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
  - name: Configure FortiCloud SSO admin users.
    fortios_system_sso_fortigate_cloud_admin:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_sso_fortigate_cloud_admin:
        accprofile: "<your_own_value> (source system.accprofile.name)"
        name: "default_name_4"
        vdom:
         -
            name: "default_name_6 (source system.vdom.name)"
```

## [Return Values](fortios_system_sso_fortigate_cloud_admin_module.md#id6)

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
