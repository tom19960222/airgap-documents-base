---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_antivirus_settings module – Configure AntiVirus settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_antivirus_settings_module.html
fetched_at: 2026-07-27T17:39:53+00:00
---
# fortinet.fortios.fortios_antivirus_settings module – Configure AntiVirus settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_antivirus_settings_module.md#ansible-collections-fortinet-fortios-fortios-antivirus-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_antivirus_settings`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_antivirus_settings_module.md#synopsis)
- [Requirements](fortios_antivirus_settings_module.md#requirements)
- [Parameters](fortios_antivirus_settings_module.md#parameters)
- [Notes](fortios_antivirus_settings_module.md#notes)
- [Examples](fortios_antivirus_settings_module.md#examples)
- [Return Values](fortios_antivirus_settings_module.md#return-values)

## [Synopsis](fortios_antivirus_settings_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify antivirus feature and settings category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_antivirus_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_antivirus_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **antivirus_settings**  dictionary | Configure AntiVirus settings. |
| **cache_clean_result**  string | Enable/disable cache of clean scan results .  Choices:   - `"enable"` - `"disable"` |
| **cache_infected_result**  string | Enable/disable cache of infected scan results .  Choices:   - `"enable"` - `"disable"` |
| **default_db**  string | Select the AV database to be used for AV scanning.  Choices:   - `"normal"` - `"extended"` - `"extreme"` |
| **grayware**  string | Enable/disable grayware detection when an AntiVirus profile is applied to traffic.  Choices:   - `"enable"` - `"disable"` |
| **machine_learning_detection**  string | Use machine learning based malware detection.  Choices:   - `"enable"` - `"monitor"` - `"disable"` |
| **override_timeout**  integer | Override the large file scan timeout value in seconds (30 - 3600). Zero is the default value and is used to disable this command. When disabled, the daemon adjusts the large file scan timeout based on the file size. |
| **use_extreme_db**  string | Enable/disable the use of Extreme AVDB.  Choices:   - `"enable"` - `"disable"` |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_antivirus_settings_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_antivirus_settings_module.md#id5)

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
  - name: Configure AntiVirus settings.
    fortios_antivirus_settings:
      vdom:  "{{ vdom }}"
      antivirus_settings:
        cache_clean_result: "enable"
        cache_infected_result: "enable"
        default_db: "normal"
        grayware: "enable"
        machine_learning_detection: "enable"
        override_timeout: "0"
        use_extreme_db: "enable"
```

## [Return Values](fortios_antivirus_settings_module.md#id6)

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
