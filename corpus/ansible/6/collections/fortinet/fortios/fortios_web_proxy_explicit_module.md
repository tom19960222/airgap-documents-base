---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_web_proxy_explicit module – Configure explicit Web proxy settings in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_web_proxy_explicit_module.html
fetched_at: 2026-07-27T17:46:39+00:00
---
# fortinet.fortios.fortios_web_proxy_explicit module – Configure explicit Web proxy settings in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_web_proxy_explicit_module.md#ansible-collections-fortinet-fortios-fortios-web-proxy-explicit-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_web_proxy_explicit`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_web_proxy_explicit_module.md#synopsis)
- [Requirements](fortios_web_proxy_explicit_module.md#requirements)
- [Parameters](fortios_web_proxy_explicit_module.md#parameters)
- [Notes](fortios_web_proxy_explicit_module.md#notes)
- [Examples](fortios_web_proxy_explicit_module.md#examples)
- [Return Values](fortios_web_proxy_explicit_module.md#return-values)

## [Synopsis](fortios_web_proxy_explicit_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify web_proxy feature and explicit category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_web_proxy_explicit_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_web_proxy_explicit_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **web_proxy_explicit**  dictionary | Configure explicit Web proxy settings. |
| **ftp_incoming_port**  string | Accept incoming FTP-over-HTTP requests on one or more ports (0 - 65535). |
| **ftp_over_http**  string | Enable to proxy FTP-over-HTTP sessions sent from a web browser.  Choices:   - `"enable"` - `"disable"` |
| **http_incoming_port**  string | Accept incoming HTTP requests on one or more ports (0 - 65535). |
| **https_incoming_port**  string | Accept incoming HTTPS requests on one or more ports (0 - 65535). |
| **https_replacement_message**  string | Enable/disable sending the client a replacement message for HTTPS requests.  Choices:   - `"enable"` - `"disable"` |
| **incoming_ip**  string | Restrict the explicit HTTP proxy to only accept sessions from this IP address. An interface must have this IP address. |
| **incoming_ip6**  string | Restrict the explicit web proxy to only accept sessions from this IPv6 address. An interface must have this IPv6 address. |
| **ipv6_status**  string | Enable/disable allowing an IPv6 web proxy destination in policies and all IPv6 related entries in this command.  Choices:   - `"enable"` - `"disable"` |
| **message_upon_server_error**  string | Enable/disable displaying a replacement message when a server error is detected.  Choices:   - `"enable"` - `"disable"` |
| **outgoing_ip**  list / elements=string | Outgoing HTTP requests will have this IP address as their source address. An interface must have this IP address. |
| **outgoing_ip6**  list / elements=string | Outgoing HTTP requests will leave this IPv6. Multiple interfaces can be specified. Interfaces must have these IPv6 addresses. |
| **pac_file_data**  string | PAC file contents enclosed in quotes (maximum of 256K bytes). |
| **pac_file_name**  string | Pac file name. |
| **pac_file_server_port**  string | Port number that PAC traffic from client web browsers uses to connect to the explicit web proxy (0 - 65535). |
| **pac_file_server_status**  string | Enable/disable Proxy Auto-Configuration (PAC) for users of this explicit proxy profile.  Choices:   - `"enable"` - `"disable"` |
| **pac_file_through_https**  string | Enable/disable to get Proxy Auto-Configuration (PAC) through HTTPS.  Choices:   - `"enable"` - `"disable"` |
| **pac_file_url**  string | PAC file access URL. |
| **pac_policy**  list / elements=dictionary | PAC policies. |
| **comments**  string | Optional comments. |
| **dstaddr**  list / elements=dictionary | Destination address objects. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **pac_file_data**  string | PAC file contents enclosed in quotes (maximum of 256K bytes). |
| **pac_file_name**  string | Pac file name. |
| **policyid**  integer | Policy ID. |
| **srcaddr**  list / elements=dictionary | Source address objects. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name. |
| **srcaddr6**  list / elements=dictionary | Source address6 objects. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **status**  string | Enable/disable policy.  Choices:   - `"enable"` - `"disable"` |
| **pref_dns_result**  string | Prefer resolving addresses using the configured IPv4 or IPv6 DNS server .  Choices:   - `"ipv4"` - `"ipv6"` |
| **realm**  string | Authentication realm used to identify the explicit web proxy (maximum of 63 characters). |
| **sec_default_action**  string | Accept or deny explicit web proxy sessions when no web proxy firewall policy exists.  Choices:   - `"accept"` - `"deny"` |
| **socks**  string | Enable/disable the SOCKS proxy.  Choices:   - `"enable"` - `"disable"` |
| **socks_incoming_port**  string | Accept incoming SOCKS proxy requests on one or more ports (0 - 65535). |
| **ssl_algorithm**  string | Relative strength of encryption algorithms accepted in HTTPS deep scan: high, medium, or low.  Choices:   - `"high"` - `"medium"` - `"low"` |
| **status**  string | Enable/disable the explicit Web proxy for HTTP and HTTPS session.  Choices:   - `"enable"` - `"disable"` |
| **strict_guest**  string | Enable/disable strict guest user checking by the explicit web proxy.  Choices:   - `"enable"` - `"disable"` |
| **trace_auth_no_rsp**  string | Enable/disable logging timed-out authentication requests.  Choices:   - `"enable"` - `"disable"` |
| **unknown_http_version**  string | How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.  Choices:   - `"reject"` - `"best-effort"` - `"tunnel"` |

## [Notes](fortios_web_proxy_explicit_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_web_proxy_explicit_module.md#id5)

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
  - name: Configure explicit Web proxy settings.
    fortios_web_proxy_explicit:
      vdom:  "{{ vdom }}"
      web_proxy_explicit:
        ftp_incoming_port: "<your_own_value>"
        ftp_over_http: "enable"
        http_incoming_port: "<your_own_value>"
        https_incoming_port: "<your_own_value>"
        https_replacement_message: "enable"
        incoming_ip: "<your_own_value>"
        incoming_ip6: "<your_own_value>"
        ipv6_status: "enable"
        message_upon_server_error: "enable"
        outgoing_ip: "<your_own_value>"
        outgoing_ip6: "<your_own_value>"
        pac_file_data: "<your_own_value>"
        pac_file_name: "<your_own_value>"
        pac_file_server_port: "<your_own_value>"
        pac_file_server_status: "enable"
        pac_file_through_https: "enable"
        pac_file_url: "<your_own_value>"
        pac_policy:
         -
            comments: "<your_own_value>"
            dstaddr:
             -
                name: "default_name_23 (source firewall.address.name firewall.addrgrp.name)"
            pac_file_data: "<your_own_value>"
            pac_file_name: "<your_own_value>"
            policyid: "0"
            srcaddr:
             -
                name: "default_name_28 (source firewall.address.name firewall.addrgrp.name firewall.proxy-address.name firewall.proxy-addrgrp.name)"
            srcaddr6:
             -
                name: "default_name_30 (source firewall.address6.name firewall.addrgrp6.name)"
            status: "enable"
        pref_dns_result: "ipv4"
        realm: "<your_own_value>"
        sec_default_action: "accept"
        socks: "enable"
        socks_incoming_port: "<your_own_value>"
        ssl_algorithm: "high"
        status: "enable"
        strict_guest: "enable"
        trace_auth_no_rsp: "enable"
        unknown_http_version: "reject"
```

## [Return Values](fortios_web_proxy_explicit_module.md#id6)

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
