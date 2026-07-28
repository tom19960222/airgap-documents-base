---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_webfilter_fortiguard module – Configure FortiGuard Web Filter service in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_webfilter_fortiguard_module.html
fetched_at: 2026-07-27T17:46:46+00:00
---
# fortinet.fortios.fortios_webfilter_fortiguard module – Configure FortiGuard Web Filter service in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_webfilter_fortiguard_module.md#ansible-collections-fortinet-fortios-fortios-webfilter-fortiguard-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_webfilter_fortiguard`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_webfilter_fortiguard_module.md#synopsis)
- [Requirements](fortios_webfilter_fortiguard_module.md#requirements)
- [Parameters](fortios_webfilter_fortiguard_module.md#parameters)
- [Notes](fortios_webfilter_fortiguard_module.md#notes)
- [Examples](fortios_webfilter_fortiguard_module.md#examples)
- [Return Values](fortios_webfilter_fortiguard_module.md#return-values)

## [Synopsis](fortios_webfilter_fortiguard_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify webfilter feature and fortiguard category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_webfilter_fortiguard_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_webfilter_fortiguard_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **webfilter_fortiguard**  dictionary | Configure FortiGuard Web Filter service. |
| **cache_mem_percent**  integer | Maximum percentage of available memory allocated to caching (1 - 15). |
| **cache_mode**  string | Cache entry expiration mode.  Choices:   - `"ttl"` - `"db-ver"` |
| **cache_prefix_match**  string | Enable/disable prefix matching in the cache.  Choices:   - `"enable"` - `"disable"` |
| **close_ports**  string | Close ports used for HTTP/HTTPS override authentication and disable user overrides.  Choices:   - `"enable"` - `"disable"` |
| **ovrd_auth_https**  string | Enable/disable use of HTTPS for override authentication.  Choices:   - `"enable"` - `"disable"` |
| **ovrd_auth_port**  integer | Port to use for FortiGuard Web Filter override authentication. |
| **ovrd_auth_port_http**  integer | Port to use for FortiGuard Web Filter HTTP override authentication. |
| **ovrd_auth_port_https**  integer | Port to use for FortiGuard Web Filter HTTPS override authentication in proxy mode. |
| **ovrd_auth_port_https_flow**  integer | Port to use for FortiGuard Web Filter HTTPS override authentication in flow mode. |
| **ovrd_auth_port_warning**  integer | Port to use for FortiGuard Web Filter Warning override authentication. |
| **request_packet_size_limit**  integer | Limit size of URL request packets sent to FortiGuard server (0 for default). |
| **warn_auth_https**  string | Enable/disable use of HTTPS for warning and authentication.  Choices:   - `"enable"` - `"disable"` |

## [Notes](fortios_webfilter_fortiguard_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_webfilter_fortiguard_module.md#id5)

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
  - name: Configure FortiGuard Web Filter service.
    fortios_webfilter_fortiguard:
      vdom:  "{{ vdom }}"
      webfilter_fortiguard:
        cache_mem_percent: "2"
        cache_mode: "ttl"
        cache_prefix_match: "enable"
        close_ports: "enable"
        ovrd_auth_https: "enable"
        ovrd_auth_port: "32767"
        ovrd_auth_port_http: "8008"
        ovrd_auth_port_https: "8010"
        ovrd_auth_port_https_flow: "8015"
        ovrd_auth_port_warning: "8020"
        request_packet_size_limit: "0"
        warn_auth_https: "enable"
```

## [Return Values](fortios_webfilter_fortiguard_module.md#id6)

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
