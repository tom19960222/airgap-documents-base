---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_web_proxy_global module – Configure Web proxy global settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_web_proxy_global_module.html
fetched_at: 2026-07-28T02:30:45+00:00
---
# fortinet.fortios.fortios_web_proxy_global module – Configure Web proxy global settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_web_proxy_global_module.md#ansible-collections-fortinet-fortios-fortios-web-proxy-global-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_web_proxy_global`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_web_proxy_global_module.md#synopsis)
- [Requirements](fortios_web_proxy_global_module.md#requirements)
- [Parameters](fortios_web_proxy_global_module.md#parameters)
- [Notes](fortios_web_proxy_global_module.md#notes)
- [Examples](fortios_web_proxy_global_module.md#examples)
- [Return Values](fortios_web_proxy_global_module.md#return-values)

## [Synopsis](fortios_web_proxy_global_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify web_proxy feature and global category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_web_proxy_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_web_proxy_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **web_proxy_global**  dictionary | Configure Web proxy global settings. |
| **fast_policy_match**  string | Enable/disable fast matching algorithm for explicit and transparent proxy policy.  **Choices:**   - `"enable"` - `"disable"` |
| **forward_proxy_auth**  string | Enable/disable forwarding proxy authentication headers.  **Choices:**   - `"enable"` - `"disable"` |
| **forward_server_affinity_timeout**  integer | Period of time before the source IP”s traffic is no longer assigned to the forwarding server (6 - 60 min). |
| **ldap_user_cache**  string | Enable/disable LDAP user cache for explicit and transparent proxy user.  **Choices:**   - `"enable"` - `"disable"` |
| **learn_client_ip**  string | Enable/disable learning the client”s IP address from headers.  **Choices:**   - `"enable"` - `"disable"` |
| **learn_client_ip_from_header**  list / elements=string | Learn client IP address from the specified headers.  **Choices:**   - `"true-client-ip"` - `"x-real-ip"` - `"x-forwarded-for"` |
| **learn_client_ip_srcaddr**  list / elements=dictionary | Source address name (srcaddr or srcaddr6 must be set). |
| **name**  string / required | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **learn_client_ip_srcaddr6**  list / elements=dictionary | IPv6 Source address name (srcaddr or srcaddr6 must be set). |
| **name**  string / required | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **log_forward_server**  string | Enable/disable forward server name logging in forward traffic log.  **Choices:**   - `"enable"` - `"disable"` |
| **max_message_length**  integer | Maximum length of HTTP message, not including body (16 - 256 Kbytes). |
| **max_request_length**  integer | Maximum length of HTTP request line (2 - 64 Kbytes). |
| **max_waf_body_cache_length**  integer | Maximum length of HTTP messages processed by Web Application Firewall (WAF) (10 - 1024 Kbytes). |
| **proxy_fqdn**  string | Fully Qualified Domain Name (FQDN) that clients connect to to connect to the explicit web proxy. |
| **src_affinity_exempt_addr**  list / elements=string | IPv4 source addresses to exempt proxy affinity. |
| **src_affinity_exempt_addr6**  list / elements=string | IPv6 source addresses to exempt proxy affinity. |
| **ssl_ca_cert**  string | SSL CA certificate for SSL interception. Source vpn.certificate.local.name. |
| **ssl_cert**  string | SSL certificate for SSL interception. Source vpn.certificate.local.name. |
| **strict_web_check**  string | Enable/disable strict web checking to block web sites that send incorrect headers that don”t conform to HTTP 1.1.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_non_http**  string | Enable/disable allowing non-HTTP traffic. Allowed non-HTTP traffic is tunneled.  **Choices:**   - `"enable"` - `"disable"` |
| **unknown_http_version**  string | Action to take when an unknown version of HTTP is encountered: reject, allow (tunnel), or proceed with best-effort.  **Choices:**   - `"reject"` - `"tunnel"` - `"best-effort"` |
| **webproxy_profile**  string | Name of the web proxy profile to apply when explicit proxy traffic is allowed by default and traffic is accepted that does not match an explicit proxy policy. Source web-proxy.profile.name. |

## [Notes](fortios_web_proxy_global_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_web_proxy_global_module.md#id5)

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
  - name: Configure Web proxy global settings.
    fortios_web_proxy_global:
      vdom:  "{{ vdom }}"
      web_proxy_global:
        fast_policy_match: "enable"
        forward_proxy_auth: "enable"
        forward_server_affinity_timeout: "30"
        ldap_user_cache: "enable"
        learn_client_ip: "enable"
        learn_client_ip_from_header: "true-client-ip"
        learn_client_ip_srcaddr:
         -
            name: "default_name_10 (source firewall.address.name firewall.addrgrp.name)"
        learn_client_ip_srcaddr6:
         -
            name: "default_name_12 (source firewall.address6.name firewall.addrgrp6.name)"
        log_forward_server: "enable"
        max_message_length: "32"
        max_request_length: "8"
        max_waf_body_cache_length: "32"
        proxy_fqdn: "<your_own_value>"
        src_affinity_exempt_addr: "<your_own_value>"
        src_affinity_exempt_addr6: "<your_own_value>"
        ssl_ca_cert: "<your_own_value> (source vpn.certificate.local.name)"
        ssl_cert: "<your_own_value> (source vpn.certificate.local.name)"
        strict_web_check: "enable"
        tunnel_non_http: "enable"
        unknown_http_version: "reject"
        webproxy_profile: "<your_own_value> (source web-proxy.profile.name)"
```

## [Return Values](fortios_web_proxy_global_module.md#id6)

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
