---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_ssl_setting module – SSL proxy settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_ssl_setting_module.html
fetched_at: 2026-07-27T17:41:37+00:00
---
# fortinet.fortios.fortios_firewall_ssl_setting module – SSL proxy settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_ssl_setting_module.md#ansible-collections-fortinet-fortios-fortios-firewall-ssl-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_ssl_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_ssl_setting_module.md#synopsis)
- [Requirements](fortios_firewall_ssl_setting_module.md#requirements)
- [Parameters](fortios_firewall_ssl_setting_module.md#parameters)
- [Notes](fortios_firewall_ssl_setting_module.md#notes)
- [Examples](fortios_firewall_ssl_setting_module.md#examples)
- [Return Values](fortios_firewall_ssl_setting_module.md#return-values)

## [Synopsis](fortios_firewall_ssl_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall_ssl feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_ssl_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_ssl_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_ssl_setting**  dictionary | SSL proxy settings. |
| **abbreviate_handshake**  string | Enable/disable use of SSL abbreviated handshake.  Choices:   - `"enable"` - `"disable"` |
| **cert_cache_capacity**  integer | Maximum capacity of the host certificate cache (0 - 500). |
| **cert_cache_timeout**  integer | Time limit to keep certificate cache (1 - 120 min). |
| **kxp_queue_threshold**  integer | Maximum length of the CP KXP queue. When the queue becomes full, the proxy switches cipher functions to the main CPU (0 - 512). |
| **no_matching_cipher_action**  string | Bypass or drop the connection when no matching cipher is found.  Choices:   - `"bypass"` - `"drop"` |
| **proxy_connect_timeout**  integer | Time limit to make an internal connection to the appropriate proxy process (1 - 60 sec). |
| **session_cache_capacity**  integer | Capacity of the SSL session cache (–Obsolete–) (1 - 1000). |
| **session_cache_timeout**  integer | Time limit to keep SSL session state (1 - 60 min). |
| **ssl_dh_bits**  string | Bit-size of Diffie-Hellman (DH) prime used in DHE-RSA negotiation .  Choices:   - `"768"` - `"1024"` - `"1536"` - `"2048"` |
| **ssl_queue_threshold**  integer | Maximum length of the CP SSL queue. When the queue becomes full, the proxy switches cipher functions to the main CPU (0 - 512). |
| **ssl_send_empty_frags**  string | Enable/disable sending empty fragments to avoid attack on CBC IV (for SSL 3.0 and TLS 1.0 only).  Choices:   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_ssl_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_ssl_setting_module.md#id5)

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
  - name: SSL proxy settings.
    fortios_firewall_ssl_setting:
      vdom:  "{{ vdom }}"
      firewall_ssl_setting:
        abbreviate_handshake: "enable"
        cert_cache_capacity: "200"
        cert_cache_timeout: "10"
        kxp_queue_threshold: "16"
        no_matching_cipher_action: "bypass"
        proxy_connect_timeout: "30"
        session_cache_capacity: "500"
        session_cache_timeout: "20"
        ssl_dh_bits: "768"
        ssl_queue_threshold: "32"
        ssl_send_empty_frags: "enable"
```

## [Return Values](fortios_firewall_ssl_setting_module.md#id6)

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
