---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_vpn_ssl_settings module – Configure SSL-VPN in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_vpn_ssl_settings_module.html
fetched_at: 2026-07-27T17:46:26+00:00
---
# fortinet.fortios.fortios_vpn_ssl_settings module – Configure SSL-VPN in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_vpn_ssl_settings_module.md#ansible-collections-fortinet-fortios-fortios-vpn-ssl-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_ssl_settings`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_ssl_settings_module.md#synopsis)
- [Requirements](fortios_vpn_ssl_settings_module.md#requirements)
- [Parameters](fortios_vpn_ssl_settings_module.md#parameters)
- [Notes](fortios_vpn_ssl_settings_module.md#notes)
- [Examples](fortios_vpn_ssl_settings_module.md#examples)
- [Return Values](fortios_vpn_ssl_settings_module.md#return-values)

## [Synopsis](fortios_vpn_ssl_settings_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_ssl feature and settings category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_ssl_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_vpn_ssl_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |
| **vpn_ssl_settings**  dictionary | Configure SSL-VPN. |
| **algorithm**  string | Force the SSL-VPN security level. High allows only high. Medium allows medium and high. Low allows any.  Choices:   - `"high"` - `"medium"` - `"default"` - `"low"` |
| **auth_session_check_source_ip**  string | Enable/disable checking of source IP for authentication session.  Choices:   - `"enable"` - `"disable"` |
| **auth_timeout**  integer | SSL-VPN authentication timeout (1 - 259200 sec (3 days), 0 for no timeout). |
| **authentication_rule**  list / elements=dictionary | Authentication rule for SSL-VPN. |
| **auth**  string | SSL-VPN authentication method restriction.  Choices:   - `"any"` - `"local"` - `"radius"` - `"tacacs+"` - `"ldap"` - `"peer"` |
| **cipher**  string | SSL-VPN cipher strength.  Choices:   - `"any"` - `"high"` - `"medium"` |
| **client_cert**  string | Enable/disable SSL-VPN client certificate restrictive.  Choices:   - `"enable"` - `"disable"` |
| **groups**  list / elements=dictionary | User groups. |
| **name**  string | Group name. Source user.group.name. |
| **id**  integer | ID (0 - 4294967295). |
| **portal**  string | SSL-VPN portal. Source vpn.ssl.web.portal.name. |
| **realm**  string | SSL-VPN realm. Source vpn.ssl.web.realm.url-path. |
| **source_address**  list / elements=dictionary | Source address of incoming traffic. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name system.external-resource.name. |
| **source_address6**  list / elements=dictionary | IPv6 source address of incoming traffic. |
| **name**  string | IPv6 address name. Source firewall.address6.name firewall.addrgrp6.name system.external-resource.name. |
| **source_address6_negate**  string | Enable/disable negated source IPv6 address match.  Choices:   - `"enable"` - `"disable"` |
| **source_address_negate**  string | Enable/disable negated source address match.  Choices:   - `"enable"` - `"disable"` |
| **source_interface**  list / elements=dictionary | SSL-VPN source interface of incoming traffic. |
| **name**  string | Interface name. Source system.interface.name system.zone.name. |
| **user_peer**  string | Name of user peer. Source user.peer.name. |
| **users**  list / elements=dictionary | User name. |
| **name**  string | User name. Source user.local.name. |
| **auto_tunnel_static_route**  string | Enable/disable to auto-create static routes for the SSL-VPN tunnel IP addresses.  Choices:   - `"enable"` - `"disable"` |
| **banned_cipher**  list / elements=string | Select one or more cipher technologies that cannot be used in SSL-VPN negotiations. Only applies to TLS 1.2 and below.  Choices:   - `"RSA"` - `"DHE"` - `"ECDHE"` - `"DSS"` - `"ECDSA"` - `"AES"` - `"AESGCM"` - `"CAMELLIA"` - `"3DES"` - `"SHA1"` - `"SHA256"` - `"SHA384"` - `"STATIC"` - `"CHACHA20"` - `"ARIA"` - `"AESCCM"` - `"DH"` - `"ECDH"` |
| **browser_language_detection**  string | Enable/disable overriding the configured system language based on the preferred language of the browser.  Choices:   - `"enable"` - `"disable"` |
| **check_referer**  string | Enable/disable verification of referer field in HTTP request header.  Choices:   - `"enable"` - `"disable"` |
| **ciphersuite**  list / elements=string | Select one or more TLS 1.3 ciphersuites to enable. Does not affect ciphers in TLS 1.2 and below. At least one must be enabled. To disable all, set ssl-max-proto-ver to tls1-2 or below.  Choices:   - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-AES-128-CCM-SHA256"` - `"TLS-AES-128-CCM-8-SHA256"` |
| **client_sigalgs**  string | Set signature algorithms related to client authentication. Affects TLS version <= 1.2 only.  Choices:   - `"no-rsa-pss"` - `"all"` |
| **default_portal**  string | Default SSL-VPN portal. Source vpn.ssl.web.portal.name. |
| **deflate_compression_level**  integer | Compression level (0~9). |
| **deflate_min_data_size**  integer | Minimum amount of data that triggers compression (200 - 65535 bytes). |
| **dns_server1**  string | DNS server 1. |
| **dns_server2**  string | DNS server 2. |
| **dns_suffix**  string | DNS suffix used for SSL-VPN clients. |
| **dtls_hello_timeout**  integer | SSLVPN maximum DTLS hello timeout (10 - 60 sec). |
| **dtls_max_proto_ver**  string | DTLS maximum protocol version.  Choices:   - `"dtls1-0"` - `"dtls1-2"` |
| **dtls_min_proto_ver**  string | DTLS minimum protocol version.  Choices:   - `"dtls1-0"` - `"dtls1-2"` |
| **dtls_tunnel**  string | Enable/disable DTLS to prevent eavesdropping, tampering, or message forgery.  Choices:   - `"enable"` - `"disable"` |
| **dual_stack_mode**  string | Tunnel mode: enable parallel IPv4 and IPv6 tunnel. Web mode: support IPv4 and IPv6 bookmarks in the portal.  Choices:   - `"enable"` - `"disable"` |
| **encode_2f_sequence**  string | Encode 2F sequence to forward slash in URLs.  Choices:   - `"enable"` - `"disable"` |
| **encrypt_and_store_password**  string | Encrypt and store user passwords for SSL-VPN web sessions.  Choices:   - `"enable"` - `"disable"` |
| **force_two_factor_auth**  string | Enable/disable only PKI users with two-factor authentication for SSL-VPNs.  Choices:   - `"enable"` - `"disable"` |
| **header_x_forwarded_for**  string | Forward the same, add, or remove HTTP header.  Choices:   - `"pass"` - `"add"` - `"remove"` |
| **hsts_include_subdomains**  string | Add HSTS includeSubDomains response header.  Choices:   - `"enable"` - `"disable"` |
| **http_compression**  string | Enable/disable to allow HTTP compression over SSL-VPN tunnels.  Choices:   - `"enable"` - `"disable"` |
| **http_only_cookie**  string | Enable/disable SSL-VPN support for HttpOnly cookies.  Choices:   - `"enable"` - `"disable"` |
| **http_request_body_timeout**  integer | SSL-VPN session is disconnected if an HTTP request body is not received within this time (1 - 60 sec). |
| **http_request_header_timeout**  integer | SSL-VPN session is disconnected if an HTTP request header is not received within this time (1 - 60 sec). |
| **https_redirect**  string | Enable/disable redirect of port 80 to SSL-VPN port.  Choices:   - `"enable"` - `"disable"` |
| **idle_timeout**  integer | SSL-VPN disconnects if idle for specified time in seconds. |
| **ipv6_dns_server1**  string | IPv6 DNS server 1. |
| **ipv6_dns_server2**  string | IPv6 DNS server 2. |
| **ipv6_wins_server1**  string | IPv6 WINS server 1. |
| **ipv6_wins_server2**  string | IPv6 WINS server 2. |
| **login_attempt_limit**  integer | SSL-VPN maximum login attempt times before block (0 - 10). |
| **login_block_time**  integer | Time for which a user is blocked from logging in after too many failed login attempts (0 - 86400 sec). |
| **login_timeout**  integer | SSLVPN maximum login timeout (10 - 180 sec). |
| **port**  integer | SSL-VPN access port (1 - 65535). |
| **port_precedence**  string | Enable/disable, Enable means that if SSL-VPN connections are allowed on an interface admin GUI connections are blocked on that interface.  Choices:   - `"enable"` - `"disable"` |
| **reqclientcert**  string | Enable/disable to require client certificates for all SSL-VPN users.  Choices:   - `"enable"` - `"disable"` |
| **route_source_interface**  string | Enable to allow SSL-VPN sessions to bypass routing and bind to the incoming interface.  Choices:   - `"enable"` - `"disable"` |
| **saml_redirect_port**  integer | SAML local redirect port in the machine running FortiClient (0 - 65535). 0 is to disable redirection on FGT side. |
| **servercert**  string | Name of the server certificate to be used for SSL-VPNs. Source vpn.certificate.local.name. |
| **source_address**  list / elements=dictionary | Source address of incoming traffic. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name system.external-resource.name. |
| **source_address6**  list / elements=dictionary | IPv6 source address of incoming traffic. |
| **name**  string | IPv6 address name. Source firewall.address6.name firewall.addrgrp6.name system.external-resource.name. |
| **source_address6_negate**  string | Enable/disable negated source IPv6 address match.  Choices:   - `"enable"` - `"disable"` |
| **source_address_negate**  string | Enable/disable negated source address match.  Choices:   - `"enable"` - `"disable"` |
| **source_interface**  list / elements=dictionary | SSL-VPN source interface of incoming traffic. |
| **name**  string | Interface name. Source system.interface.name system.zone.name. |
| **ssl_client_renegotiation**  string | Enable/disable to allow client renegotiation by the server if the tunnel goes down.  Choices:   - `"disable"` - `"enable"` |
| **ssl_insert_empty_fragment**  string | Enable/disable insertion of empty fragment.  Choices:   - `"enable"` - `"disable"` |
| **ssl_max_proto_ver**  string | SSL maximum protocol version.  Choices:   - `"tls1-0"` - `"tls1-1"` - `"tls1-2"` - `"tls1-3"` |
| **ssl_min_proto_ver**  string | SSL minimum protocol version.  Choices:   - `"tls1-0"` - `"tls1-1"` - `"tls1-2"` - `"tls1-3"` |
| **status**  string | Enable/disable SSL-VPN.  Choices:   - `"enable"` - `"disable"` |
| **tlsv1_0**  string | tlsv1-0  Choices:   - `"enable"` - `"disable"` |
| **tlsv1_1**  string | tlsv1-1  Choices:   - `"enable"` - `"disable"` |
| **tlsv1_2**  string | tlsv1-2  Choices:   - `"enable"` - `"disable"` |
| **tlsv1_3**  string | tlsv1-3  Choices:   - `"enable"` - `"disable"` |
| **transform_backward_slashes**  string | Transform backward slashes to forward slashes in URLs.  Choices:   - `"enable"` - `"disable"` |
| **tunnel_addr_assigned_method**  string | Method used for assigning address for tunnel.  Choices:   - `"first-available"` - `"round-robin"` |
| **tunnel_connect_without_reauth**  string | Enable/disable tunnel connection without re-authorization if previous connection dropped.  Choices:   - `"enable"` - `"disable"` |
| **tunnel_ip_pools**  list / elements=dictionary | Names of the IPv4 IP Pool firewall objects that define the IP addresses reserved for remote clients. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **tunnel_ipv6_pools**  list / elements=dictionary | Names of the IPv6 IP Pool firewall objects that define the IP addresses reserved for remote clients. |
| **name**  string | Address name. Source firewall.address6.name firewall.addrgrp6.name. |
| **tunnel_user_session_timeout**  integer | Time out value to clean up user session after tunnel connection is dropped (1 - 255 sec). |
| **unsafe_legacy_renegotiation**  string | Enable/disable unsafe legacy re-negotiation.  Choices:   - `"enable"` - `"disable"` |
| **url_obscuration**  string | Enable/disable to obscure the host name of the URL of the web browser display.  Choices:   - `"enable"` - `"disable"` |
| **user_peer**  string | Name of user peer. Source user.peer.name. |
| **web_mode_snat**  string | Enable/disable use of IP pools defined in firewall policy while using web-mode.  Choices:   - `"enable"` - `"disable"` |
| **wins_server1**  string | WINS server 1. |
| **wins_server2**  string | WINS server 2. |
| **x_content_type_options**  string | Add HTTP X-Content-Type-Options header.  Choices:   - `"enable"` - `"disable"` |
| **ztna_trusted_client**  string | Enable/disable verification of device certificate for SSLVPN ZTNA session.  Choices:   - `"enable"` - `"disable"` |

## [Notes](fortios_vpn_ssl_settings_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_ssl_settings_module.md#id5)

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
  - name: Configure SSL-VPN.
    fortios_vpn_ssl_settings:
      vdom:  "{{ vdom }}"
      vpn_ssl_settings:
        algorithm: "high"
        auth_session_check_source_ip: "enable"
        auth_timeout: "28800"
        authentication_rule:
         -
            auth: "any"
            cipher: "any"
            client_cert: "enable"
            groups:
             -
                name: "default_name_11 (source user.group.name)"
            id:  "12"
            portal: "<your_own_value> (source vpn.ssl.web.portal.name)"
            realm: "<your_own_value> (source vpn.ssl.web.realm.url-path)"
            source_address:
             -
                name: "default_name_16 (source firewall.address.name firewall.addrgrp.name system.external-resource.name)"
            source_address_negate: "enable"
            source_address6:
             -
                name: "default_name_19 (source firewall.address6.name firewall.addrgrp6.name system.external-resource.name)"
            source_address6_negate: "enable"
            source_interface:
             -
                name: "default_name_22 (source system.interface.name system.zone.name)"
            user_peer: "<your_own_value> (source user.peer.name)"
            users:
             -
                name: "default_name_25 (source user.local.name)"
        auto_tunnel_static_route: "enable"
        banned_cipher: "RSA"
        browser_language_detection: "enable"
        check_referer: "enable"
        ciphersuite: "TLS-AES-128-GCM-SHA256"
        client_sigalgs: "no-rsa-pss"
        default_portal: "<your_own_value> (source vpn.ssl.web.portal.name)"
        deflate_compression_level: "6"
        deflate_min_data_size: "300"
        dns_server1: "<your_own_value>"
        dns_server2: "<your_own_value>"
        dns_suffix: "<your_own_value>"
        dtls_hello_timeout: "10"
        dtls_max_proto_ver: "dtls1-0"
        dtls_min_proto_ver: "dtls1-0"
        dtls_tunnel: "enable"
        dual_stack_mode: "enable"
        encode_2f_sequence: "enable"
        encrypt_and_store_password: "enable"
        force_two_factor_auth: "enable"
        header_x_forwarded_for: "pass"
        hsts_include_subdomains: "enable"
        http_compression: "enable"
        http_only_cookie: "enable"
        http_request_body_timeout: "30"
        http_request_header_timeout: "20"
        https_redirect: "enable"
        idle_timeout: "300"
        ipv6_dns_server1: "<your_own_value>"
        ipv6_dns_server2: "<your_own_value>"
        ipv6_wins_server1: "<your_own_value>"
        ipv6_wins_server2: "<your_own_value>"
        login_attempt_limit: "2"
        login_block_time: "60"
        login_timeout: "30"
        port: "10443"
        port_precedence: "enable"
        reqclientcert: "enable"
        route_source_interface: "enable"
        saml_redirect_port: "8020"
        servercert: "<your_own_value> (source vpn.certificate.local.name)"
        source_address:
         -
            name: "default_name_68 (source firewall.address.name firewall.addrgrp.name system.external-resource.name)"
        source_address_negate: "enable"
        source_address6:
         -
            name: "default_name_71 (source firewall.address6.name firewall.addrgrp6.name system.external-resource.name)"
        source_address6_negate: "enable"
        source_interface:
         -
            name: "default_name_74 (source system.interface.name system.zone.name)"
        ssl_client_renegotiation: "disable"
        ssl_insert_empty_fragment: "enable"
        ssl_max_proto_ver: "tls1-0"
        ssl_min_proto_ver: "tls1-0"
        status: "enable"
        tlsv1_0: "enable"
        tlsv1_1: "enable"
        tlsv1_2: "enable"
        tlsv1_3: "enable"
        transform_backward_slashes: "enable"
        tunnel_addr_assigned_method: "first-available"
        tunnel_connect_without_reauth: "enable"
        tunnel_ip_pools:
         -
            name: "default_name_88 (source firewall.address.name firewall.addrgrp.name)"
        tunnel_ipv6_pools:
         -
            name: "default_name_90 (source firewall.address6.name firewall.addrgrp6.name)"
        tunnel_user_session_timeout: "30"
        unsafe_legacy_renegotiation: "enable"
        url_obscuration: "enable"
        user_peer: "<your_own_value> (source user.peer.name)"
        web_mode_snat: "enable"
        wins_server1: "<your_own_value>"
        wins_server2: "<your_own_value>"
        x_content_type_options: "enable"
        ztna_trusted_client: "enable"
```

## [Return Values](fortios_vpn_ssl_settings_module.md#id6)

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
