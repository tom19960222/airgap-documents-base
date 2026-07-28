---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_authentication_setting module – Configure authentication setting in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_authentication_setting_module.html
fetched_at: 2026-07-28T02:23:26+00:00
---
# fortinet.fortios.fortios_authentication_setting module – Configure authentication setting in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_authentication_setting_module.md#ansible-collections-fortinet-fortios-fortios-authentication-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_authentication_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_authentication_setting_module.md#synopsis)
- [Requirements](fortios_authentication_setting_module.md#requirements)
- [Parameters](fortios_authentication_setting_module.md#parameters)
- [Notes](fortios_authentication_setting_module.md#notes)
- [Examples](fortios_authentication_setting_module.md#examples)
- [Return Values](fortios_authentication_setting_module.md#return-values)

## [Synopsis](fortios_authentication_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify authentication feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_authentication_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_authentication_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **authentication_setting**  dictionary | Configure authentication setting. |
| **active_auth_scheme**  string | Active authentication method (scheme name). Source authentication.scheme.name. |
| **auth_https**  string | Enable/disable redirecting HTTP user authentication to HTTPS.  **Choices:**   - `"enable"` - `"disable"` |
| **captive_portal**  string | Captive portal host name. Source firewall.address.name. |
| **captive_portal6**  string | IPv6 captive portal host name. Source firewall.address6.name. |
| **captive_portal_ip**  string | Captive portal IP address. |
| **captive_portal_ip6**  string | Captive portal IPv6 address. |
| **captive_portal_port**  integer | Captive portal port number (1 - 65535). |
| **captive_portal_ssl_port**  integer | Captive portal SSL port number (1 - 65535). |
| **captive_portal_type**  string | Captive portal type.  **Choices:**   - `"fqdn"` - `"ip"` |
| **cert_auth**  string | Enable/disable redirecting certificate authentication to HTTPS portal.  **Choices:**   - `"enable"` - `"disable"` |
| **cert_captive_portal**  string | Certificate captive portal host name. Source firewall.address.name. |
| **cert_captive_portal_ip**  string | Certificate captive portal IP address. |
| **cert_captive_portal_port**  integer | Certificate captive portal port number (1 - 65535). |
| **cookie_max_age**  integer | Persistent web portal cookie maximum age in minutes (30 - 10080 (1 week)). |
| **cookie_refresh_div**  integer | Refresh rate divider of persistent web portal cookie . Refresh value = cookie-max-age/cookie-refresh-div. |
| **dev_range**  list / elements=dictionary | Address range for the IP based device query. |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **ip_auth_cookie**  string | Enable/disable persistent cookie on IP based web portal authentication .  **Choices:**   - `"enable"` - `"disable"` |
| **persistent_cookie**  string | Enable/disable persistent cookie on web portal authentication .  **Choices:**   - `"enable"` - `"disable"` |
| **sso_auth_scheme**  string | Single-Sign-On authentication method (scheme name). Source authentication.scheme.name. |
| **update_time**  string | Time of the last update. |
| **user_cert_ca**  list / elements=dictionary | CA certificate used for client certificate verification. |
| **name**  string / required | CA certificate list. Source vpn.certificate.ca.name. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_authentication_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_authentication_setting_module.md#id5)

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
  - name: Configure authentication setting.
    fortios_authentication_setting:
      vdom:  "{{ vdom }}"
      authentication_setting:
        active_auth_scheme: "<your_own_value> (source authentication.scheme.name)"
        auth_https: "enable"
        captive_portal: "<your_own_value> (source firewall.address.name)"
        captive_portal_ip: "<your_own_value>"
        captive_portal_ip6: "<your_own_value>"
        captive_portal_port: "7830"
        captive_portal_ssl_port: "7831"
        captive_portal_type: "fqdn"
        captive_portal6: "<your_own_value> (source firewall.address6.name)"
        cert_auth: "enable"
        cert_captive_portal: "<your_own_value> (source firewall.address.name)"
        cert_captive_portal_ip: "<your_own_value>"
        cert_captive_portal_port: "7832"
        cookie_max_age: "480"
        cookie_refresh_div: "2"
        dev_range:
         -
            name: "default_name_19 (source firewall.address.name firewall.addrgrp.name)"
        ip_auth_cookie: "enable"
        persistent_cookie: "enable"
        sso_auth_scheme: "<your_own_value> (source authentication.scheme.name)"
        update_time: "<your_own_value>"
        user_cert_ca:
         -
            name: "default_name_25 (source vpn.certificate.ca.name)"
```

## [Return Values](fortios_authentication_setting_module.md#id6)

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
