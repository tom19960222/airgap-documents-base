---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_vpn_ssl_web_host_check_software module – SSL-VPN host check software in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_vpn_ssl_web_host_check_software_module.html
fetched_at: 2026-07-27T17:46:27+00:00
---
# fortinet.fortios.fortios_vpn_ssl_web_host_check_software module – SSL-VPN host check software in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_vpn_ssl_web_host_check_software_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ssl-web-host-check-software-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ssl_web_host_check_software`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ssl_web_host_check_software_module.md#synopsis)
- [Requirements](fortios_vpn_ssl_web_host_check_software_module.md#requirements)
- [Parameters](fortios_vpn_ssl_web_host_check_software_module.md#parameters)
- [Notes](fortios_vpn_ssl_web_host_check_software_module.md#notes)
- [Examples](fortios_vpn_ssl_web_host_check_software_module.md#examples)
- [Return Values](fortios_vpn_ssl_web_host_check_software_module.md#return-values)

## [Synopsis](fortios_vpn_ssl_web_host_check_software_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_ssl_web feature and host_check_software category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ssl_web_host_check_software_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_vpn_ssl_web_host_check_software_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **vpn_ssl_web_host_check_software**  dictionary | SSL-VPN host check software. |
| **check_item_list**  list / elements=dictionary | Check item list. |
| **action**  string | Action.  Choices:   - `"require"` - `"deny"` |
| **id**  integer | ID (0 - 4294967295). |
| **md5s**  list / elements=dictionary | MD5 checksum. |
| **id**  string | Hex string of MD5 checksum. |
| **target**  string | Target. |
| **type**  string | Type.  Choices:   - `"file"` - `"registry"` - `"process"` |
| **version**  string | Version. |
| **guid**  string | Globally unique ID. |
| **name**  string / required | Name. |
| **os_type**  string | OS type.  Choices:   - `"windows"` - `"macos"` |
| **type**  string | Type.  Choices:   - `"av"` - `"fw"` |
| **version**  string | Version. |

## [Notes](fortios_vpn_ssl_web_host_check_software_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ssl_web_host_check_software_module.md#id5)

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
  - name: SSL-VPN host check software.
    fortios_vpn_ssl_web_host_check_software:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      vpn_ssl_web_host_check_software:
        check_item_list:
         -
            action: "require"
            id:  "5"
            md5s:
             -
                id:  "7"
            target: "<your_own_value>"
            type: "file"
            version: "<your_own_value>"
        guid: "<your_own_value>"
        name: "default_name_12"
        os_type: "windows"
        type: "av"
        version: "<your_own_value>"
```

## [Return Values](fortios_vpn_ssl_web_host_check_software_module.md#id6)

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
