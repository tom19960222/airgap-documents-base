---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_endpoint_control_settings module – Configure endpoint control settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_endpoint_control_settings_module.html
fetched_at: 2026-07-28T02:23:57+00:00
---
# fortinet.fortios.fortios_endpoint_control_settings module – Configure endpoint control settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_endpoint_control_settings_module.md#ansible-collections-fortinet-fortios-fortios-endpoint-control-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_endpoint_control_settings`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_endpoint_control_settings_module.md#synopsis)
- [Requirements](fortios_endpoint_control_settings_module.md#requirements)
- [Parameters](fortios_endpoint_control_settings_module.md#parameters)
- [Notes](fortios_endpoint_control_settings_module.md#notes)
- [Examples](fortios_endpoint_control_settings_module.md#examples)
- [Return Values](fortios_endpoint_control_settings_module.md#return-values)

## [Synopsis](fortios_endpoint_control_settings_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify endpoint_control feature and settings category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_endpoint_control_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_endpoint_control_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **endpoint_control_settings**  dictionary | Configure endpoint control settings. |
| **download_custom_link**  string | Customized URL for downloading FortiClient. |
| **download_location**  string | FortiClient download location (FortiGuard or custom).  **Choices:**   - `"fortiguard"` - `"custom"` |
| **forticlient_avdb_update_interval**  integer | Period of time between FortiClient AntiVirus database updates (0 - 24 hours). |
| **forticlient_dereg_unsupported_client**  string | Enable/disable deregistering unsupported FortiClient endpoints.  **Choices:**   - `"enable"` - `"disable"` |
| **forticlient_disconnect_unsupported_client**  string | Enable/disable disconnecting of unsupported FortiClient endpoints.  **Choices:**   - `"enable"` - `"disable"` |
| **forticlient_ems_rest_api_call_timeout**  integer | FortiClient EMS call timeout in milliseconds (500 - 30000 milliseconds). |
| **forticlient_keepalive_interval**  integer | Interval between two KeepAlive messages from FortiClient (20 - 300 sec). |
| **forticlient_offline_grace**  string | Enable/disable grace period for offline registered clients.  **Choices:**   - `"enable"` - `"disable"` |
| **forticlient_offline_grace_interval**  integer | Grace period for offline registered FortiClient (60 - 600 sec). |
| **forticlient_reg_key**  string | FortiClient registration key. |
| **forticlient_reg_key_enforce**  string | Enable/disable requiring or enforcing FortiClient registration keys.  **Choices:**   - `"enable"` - `"disable"` |
| **forticlient_reg_timeout**  integer | FortiClient registration license timeout (days, min = 1, max = 180, 0 means unlimited). |
| **forticlient_sys_update_interval**  integer | Interval between two system update messages from FortiClient (30 - 1440 min). |
| **forticlient_user_avatar**  string | Enable/disable uploading FortiClient user avatars.  **Choices:**   - `"enable"` - `"disable"` |
| **forticlient_warning_interval**  integer | Period of time between FortiClient portal warnings (0 - 24 hours). |
| **override**  string | Override global EMS table for this VDOM.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_endpoint_control_settings_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_endpoint_control_settings_module.md#id5)

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
  - name: Configure endpoint control settings.
    fortios_endpoint_control_settings:
      vdom:  "{{ vdom }}"
      endpoint_control_settings:
        download_custom_link: "<your_own_value>"
        download_location: "fortiguard"
        forticlient_avdb_update_interval: "12"
        forticlient_dereg_unsupported_client: "enable"
        forticlient_disconnect_unsupported_client: "enable"
        forticlient_ems_rest_api_call_timeout: "15000"
        forticlient_keepalive_interval: "150"
        forticlient_offline_grace: "enable"
        forticlient_offline_grace_interval: "300"
        forticlient_reg_key: "<your_own_value>"
        forticlient_reg_key_enforce: "enable"
        forticlient_reg_timeout: "90"
        forticlient_sys_update_interval: "720"
        forticlient_user_avatar: "enable"
        forticlient_warning_interval: "12"
        override: "enable"
```

## [Return Values](fortios_endpoint_control_settings_module.md#id6)

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
