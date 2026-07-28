---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_proxy_address module – Configure web proxy address in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_proxy_address_module.html
fetched_at: 2026-07-28T02:24:59+00:00
---
# fortinet.fortios.fortios_firewall_proxy_address module – Configure web proxy address in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_proxy_address_module.md#ansible-collections-fortinet-fortios-fortios-firewall-proxy-address-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_proxy_address`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_proxy_address_module.md#synopsis)
- [Requirements](fortios_firewall_proxy_address_module.md#requirements)
- [Parameters](fortios_firewall_proxy_address_module.md#parameters)
- [Notes](fortios_firewall_proxy_address_module.md#notes)
- [Examples](fortios_firewall_proxy_address_module.md#examples)
- [Return Values](fortios_firewall_proxy_address_module.md#return-values)

## [Synopsis](fortios_firewall_proxy_address_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and proxy_address category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_proxy_address_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_proxy_address_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_proxy_address**  dictionary | Configure web proxy address. |
| **application**  list / elements=dictionary | SaaS application. |
| **name**  string / required | SaaS application name. |
| **case_sensitivity**  string | Enable to make the pattern case sensitive.  **Choices:**   - `"disable"` - `"enable"` |
| **category**  list / elements=dictionary | FortiGuard category ID. |
| **id**  integer / required | FortiGuard category ID. see <a href=’#notes’>Notes</a>. |
| **color**  integer | Integer value to determine the color of the icon in the GUI (1 - 32). |
| **comment**  string | Optional comments. |
| **header**  string | HTTP header name as a regular expression. |
| **header_group**  list / elements=dictionary | HTTP header group. |
| **case_sensitivity**  string | Case sensitivity in pattern.  **Choices:**   - `"disable"` - `"enable"` |
| **header**  string | HTTP header regular expression. |
| **header_name**  string | HTTP header. |
| **id**  integer / required | ID. see <a href=’#notes’>Notes</a>. |
| **header_name**  string | Name of HTTP header. |
| **host**  string | Address object for the host. Source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name. |
| **host_regex**  string | Host name as a regular expression. |
| **method**  list / elements=string | HTTP request methods to be used.  **Choices:**   - `"get"` - `"post"` - `"put"` - `"head"` - `"connect"` - `"trace"` - `"options"` - `"delete"` |
| **name**  string / required | Address name. |
| **path**  string | URL path as a regular expression. |
| **query**  string | Match the query part of the URL as a regular expression. |
| **referrer**  string | Enable/disable use of referrer field in the HTTP header to match the address.  **Choices:**   - `"enable"` - `"disable"` |
| **tagging**  list / elements=dictionary | Config object tagging. |
| **category**  string | Tag category. Source system.object-tagging.category. |
| **name**  string / required | Tagging entry name. |
| **tags**  list / elements=dictionary | Tags. |
| **name**  string / required | Tag name. Source system.object-tagging.tags.name. |
| **type**  string | Proxy address type.  **Choices:**   - `"host-regex"` - `"url"` - `"category"` - `"method"` - `"ua"` - `"header"` - `"src-advanced"` - `"dst-advanced"` - `"saas"` |
| **ua**  list / elements=string | Names of browsers to be used as user agent.  **Choices:**   - `"chrome"` - `"ms"` - `"firefox"` - `"safari"` - `"ie"` - `"edge"` - `"other"` |
| **ua_max_ver**  string | Maximum version of the user agent specified in dotted notation. For example, use 120 with the ua field set to “chrome” to require Google Chrome”s maximum version must be 120. |
| **ua_min_ver**  string | Minimum version of the user agent specified in dotted notation. For example, use 90.0.1 with the ua field set to “chrome” to require Google Chrome”s minimum version must be 90.0.1. |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **visibility**  string | Enable/disable visibility of the object in the GUI.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_proxy_address_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_proxy_address_module.md#id5)

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
  - name: Configure web proxy address.
    fortios_firewall_proxy_address:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_proxy_address:
        application:
         -
            name: "default_name_4"
        case_sensitivity: "disable"
        category:
         -
            id:  "7"
        color: "0"
        comment: "Optional comments."
        header: "<your_own_value>"
        header_group:
         -
            case_sensitivity: "disable"
            header: "<your_own_value>"
            header_name: "<your_own_value>"
            id:  "15"
        header_name: "<your_own_value>"
        host: "myhostname (source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name)"
        host_regex: "myhostname"
        method: "get"
        name: "default_name_20"
        path: "<your_own_value>"
        query: "<your_own_value>"
        referrer: "enable"
        tagging:
         -
            category: "<your_own_value> (source system.object-tagging.category)"
            name: "default_name_26"
            tags:
             -
                name: "default_name_28 (source system.object-tagging.tags.name)"
        type: "host-regex"
        ua: "chrome"
        ua_max_ver: "<your_own_value>"
        ua_min_ver: "<your_own_value>"
        uuid: "<your_own_value>"
        visibility: "enable"
```

## [Return Values](fortios_firewall_proxy_address_module.md#id6)

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
