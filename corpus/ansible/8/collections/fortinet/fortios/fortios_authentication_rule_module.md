---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_authentication_rule module – Configure Authentication Rules in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_authentication_rule_module.html
fetched_at: 2026-07-28T02:23:24+00:00
---
# fortinet.fortios.fortios_authentication_rule module – Configure Authentication Rules in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_authentication_rule_module.md#ansible-collections-fortinet-fortios-fortios-authentication-rule-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_authentication_rule`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_authentication_rule_module.md#synopsis)
- [Requirements](fortios_authentication_rule_module.md#requirements)
- [Parameters](fortios_authentication_rule_module.md#parameters)
- [Notes](fortios_authentication_rule_module.md#notes)
- [Examples](fortios_authentication_rule_module.md#examples)
- [Return Values](fortios_authentication_rule_module.md#return-values)

## [Synopsis](fortios_authentication_rule_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify authentication feature and rule category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_authentication_rule_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_authentication_rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **authentication_rule**  dictionary | Configure Authentication Rules. |
| **active_auth_method**  string | Select an active authentication method. Source authentication.scheme.name. |
| **comments**  string | Comment. |
| **cors_depth**  integer | Depth to allow CORS access . |
| **cors_stateful**  string | Enable/disable allowance of CORS access .  **Choices:**   - `"enable"` - `"disable"` |
| **dstaddr**  list / elements=dictionary | Select an IPv4 destination address from available options. Required for web proxy authentication. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name system .external-resource.name. |
| **dstaddr6**  list / elements=dictionary | Select an IPv6 destination address from available options. Required for web proxy authentication. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **ip_based**  string | Enable/disable IP-based authentication. When enabled, previously authenticated users from the same IP address will be exempted.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Authentication rule name. |
| **protocol**  string | Authentication is required for the selected protocol .  **Choices:**   - `"http"` - `"ftp"` - `"socks"` - `"ssh"` |
| **srcaddr**  list / elements=dictionary | Authentication is required for the selected IPv4 source address. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name system .external-resource.name. |
| **srcaddr6**  list / elements=dictionary | Authentication is required for the selected IPv6 source address. |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **srcintf**  list / elements=dictionary | Incoming (ingress) interface. |
| **name**  string / required | Interface name. Source system.interface.name system.zone.name system.sdwan.zone.name. |
| **sso_auth_method**  string | Select a single-sign on (SSO) authentication method. Source authentication.scheme.name. |
| **status**  string | Enable/disable this authentication rule.  **Choices:**   - `"enable"` - `"disable"` |
| **transaction_based**  string | Enable/disable transaction based authentication .  **Choices:**   - `"enable"` - `"disable"` |
| **web_auth_cookie**  string | Enable/disable Web authentication cookies .  **Choices:**   - `"enable"` - `"disable"` |
| **web_portal**  string | Enable/disable web portal for proxy transparent policy .  **Choices:**   - `"enable"` - `"disable"` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_authentication_rule_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_authentication_rule_module.md#id5)

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
  - name: Configure Authentication Rules.
    fortios_authentication_rule:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      authentication_rule:
        active_auth_method: "<your_own_value> (source authentication.scheme.name)"
        comments: "<your_own_value>"
        cors_depth: "3"
        cors_stateful: "enable"
        dstaddr:
         -
            name: "default_name_8 (source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name system
              .external-resource.name)"
        dstaddr6:
         -
            name: "default_name_10 (source firewall.address6.name firewall.addrgrp6.name)"
        ip_based: "enable"
        name: "default_name_12"
        protocol: "http"
        srcaddr:
         -
            name: "default_name_15 (source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name system
              .external-resource.name)"
        srcaddr6:
         -
            name: "default_name_17 (source firewall.address6.name firewall.addrgrp6.name)"
        srcintf:
         -
            name: "default_name_19 (source system.interface.name system.zone.name system.sdwan.zone.name)"
        sso_auth_method: "<your_own_value> (source authentication.scheme.name)"
        status: "enable"
        transaction_based: "enable"
        web_auth_cookie: "enable"
        web_portal: "enable"
```

## [Return Values](fortios_authentication_rule_module.md#id6)

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
