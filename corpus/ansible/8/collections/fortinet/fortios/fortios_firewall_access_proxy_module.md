---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_access_proxy module – Configure IPv4 access proxy in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_access_proxy_module.html
fetched_at: 2026-07-28T02:24:10+00:00
---
# fortinet.fortios.fortios_firewall_access_proxy module – Configure IPv4 access proxy in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_access_proxy_module.md#ansible-collections-fortinet-fortios-fortios-firewall-access-proxy-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_access_proxy`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_access_proxy_module.md#synopsis)
- [Requirements](fortios_firewall_access_proxy_module.md#requirements)
- [Parameters](fortios_firewall_access_proxy_module.md#parameters)
- [Notes](fortios_firewall_access_proxy_module.md#notes)
- [Examples](fortios_firewall_access_proxy_module.md#examples)
- [Return Values](fortios_firewall_access_proxy_module.md#return-values)

## [Synopsis](fortios_firewall_access_proxy_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and access_proxy category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_access_proxy_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_access_proxy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_access_proxy**  dictionary | Configure IPv4 access proxy. |
| **add_vhost_domain_to_dnsdb**  string | Enable/disable adding vhost/domain to dnsdb for ztna dox tunnel.  **Choices:**   - `"enable"` - `"disable"` |
| **api_gateway**  list / elements=dictionary | Set IPv4 API Gateway. |
| **application**  list / elements=dictionary | SaaS application controlled by this Access Proxy. |
| **name**  string / required | SaaS application name. |
| **h2_support**  string | HTTP2 support, default=Enable.  **Choices:**   - `"enable"` - `"disable"` |
| **h3_support**  string | HTTP3/QUIC support, default=Disable.  **Choices:**   - `"enable"` - `"disable"` |
| **http_cookie_age**  integer | Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit. |
| **http_cookie_domain**  string | Domain that HTTP cookie persistence should apply to. |
| **http_cookie_domain_from_host**  string | Enable/disable use of HTTP cookie domain from host field in HTTP.  **Choices:**   - `"disable"` - `"enable"` |
| **http_cookie_generation**  integer | Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies. |
| **http_cookie_path**  string | Limit HTTP cookie persistence to the specified path. |
| **http_cookie_share**  string | Control sharing of cookies across API Gateway. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.  **Choices:**   - `"disable"` - `"same-ip"` |
| **https_cookie_secure**  string | Enable/disable verification that inserted HTTPS cookies are secure.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer / required | API Gateway ID. see <a href=’#notes’>Notes</a>. |
| **ldb_method**  string | Method used to distribute sessions to real servers.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"first-alive"` - `"http-host"` - `"least-session"` - `"least-rtt"` |
| **persistence**  string | Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.  **Choices:**   - `"none"` - `"http-cookie"` |
| **quic**  dictionary | QUIC setting. |
| **ack_delay_exponent**  integer | ACK delay exponent (1 - 20). |
| **active_connection_id_limit**  integer | Active connection ID limit (1 - 8). |
| **active_migration**  string | Enable/disable active migration .  **Choices:**   - `"enable"` - `"disable"` |
| **grease_quic_bit**  string | Enable/disable grease QUIC bit .  **Choices:**   - `"enable"` - `"disable"` |
| **max_ack_delay**  integer | Maximum ACK delay in milliseconds (1 - 16383). |
| **max_datagram_frame_size**  integer | Maximum datagram frame size in bytes (1 - 1500). |
| **max_idle_timeout**  integer | Maximum idle timeout milliseconds (1 - 60000). |
| **max_udp_payload_size**  integer | Maximum UDP payload size in bytes (1200 - 1500). |
| **realservers**  list / elements=dictionary | Select the real servers that this Access Proxy will distribute traffic to. |
| **addr_type**  string | Type of address.  **Choices:**   - `"ip"` - `"fqdn"` |
| **address**  string | Address or address group of the real server. Source firewall.address.name firewall.addrgrp.name. |
| **domain**  string | Wildcard domain name of the real server. |
| **external_auth**  string | Enable/disable use of external browser as user-agent for SAML user authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **health_check**  string | Enable to check the responsiveness of the real server before forwarding traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **health_check_proto**  string | Protocol of the health check monitor to use when polling to determine server”s connectivity status.  **Choices:**   - `"ping"` - `"http"` - `"tcp-connect"` |
| **holddown_interval**  string | Enable/disable holddown timer. Server will be considered active and reachable once the holddown period has expired (30 seconds).  **Choices:**   - `"enable"` - `"disable"` |
| **http_host**  string | HTTP server domain name in HTTP header. |
| **id**  integer / required | Real server ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | IP address of the real server. |
| **mappedport**  string | Port for communicating with the real server. |
| **port**  integer | Port for communicating with the real server. |
| **ssh_client_cert**  string | Set access-proxy SSH client certificate profile. Source firewall.access-proxy-ssh-client-cert.name. |
| **ssh_host_key**  list / elements=dictionary | One or more server host key. |
| **name**  string / required | Server host key name. Source firewall.ssh.host-key.name. |
| **ssh_host_key_validation**  string | Enable/disable SSH real server host key validation.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **translate_host**  string | Enable/disable translation of hostname/IP from virtual server to real server.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_encryption**  string | Tunnel encryption.  **Choices:**   - `"enable"` - `"disable"` |
| **type**  string | TCP forwarding server type.  **Choices:**   - `"tcp-forwarding"` - `"ssh"` |
| **weight**  integer | Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connections. |
| **saml_redirect**  string | Enable/disable SAML redirection after successful authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **saml_server**  string | SAML service provider configuration for VIP authentication. Source user.saml.name. |
| **service**  string | Service.  **Choices:**   - `"http"` - `"https"` - `"tcp-forwarding"` - `"samlsp"` - `"web-portal"` - `"saas"` |
| **ssl_algorithm**  string | Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.  **Choices:**   - `"high"` - `"medium"` - `"low"` - `"custom"` |
| **ssl_cipher_suites**  list / elements=dictionary | SSL/TLS cipher suites to offer to a server, ordered by priority. |
| **cipher**  string | Cipher suite name.  **Choices:**   - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` |
| **priority**  integer / required | SSL/TLS cipher suites priority. see <a href=’#notes’>Notes</a>. |
| **versions**  list / elements=string | SSL/TLS versions that the cipher suite can be used with.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_dh_bits**  string | Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.  **Choices:**   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl_max_version**  string | Highest SSL/TLS version acceptable from a server.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_min_version**  string | Lowest SSL/TLS version acceptable from a server.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_renegotiation**  string | Enable/disable secure renegotiation to comply with RFC 5746.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_vpn_web_portal**  string | SSL-VPN web portal. Source vpn.ssl.web.portal.name. |
| **url_map**  string | URL pattern to match. |
| **url_map_type**  string | Type of url-map.  **Choices:**   - `"sub-string"` - `"wildcard"` - `"regex"` |
| **virtual_host**  string | Virtual host. Source firewall.access-proxy-virtual-host.name. |
| **api_gateway6**  list / elements=dictionary | Set IPv6 API Gateway. |
| **application**  list / elements=dictionary | SaaS application controlled by this Access Proxy. |
| **name**  string / required | SaaS application name. |
| **h2_support**  string | HTTP2 support, default=Enable.  **Choices:**   - `"enable"` - `"disable"` |
| **h3_support**  string | HTTP3/QUIC support, default=Disable.  **Choices:**   - `"enable"` - `"disable"` |
| **http_cookie_age**  integer | Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit. |
| **http_cookie_domain**  string | Domain that HTTP cookie persistence should apply to. |
| **http_cookie_domain_from_host**  string | Enable/disable use of HTTP cookie domain from host field in HTTP.  **Choices:**   - `"disable"` - `"enable"` |
| **http_cookie_generation**  integer | Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies. |
| **http_cookie_path**  string | Limit HTTP cookie persistence to the specified path. |
| **http_cookie_share**  string | Control sharing of cookies across API Gateway. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.  **Choices:**   - `"disable"` - `"same-ip"` |
| **https_cookie_secure**  string | Enable/disable verification that inserted HTTPS cookies are secure.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer / required | API Gateway ID. see <a href=’#notes’>Notes</a>. |
| **ldb_method**  string | Method used to distribute sessions to real servers.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"first-alive"` - `"http-host"` |
| **persistence**  string | Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.  **Choices:**   - `"none"` - `"http-cookie"` |
| **quic**  dictionary | QUIC setting. |
| **ack_delay_exponent**  integer | ACK delay exponent (1 - 20). |
| **active_connection_id_limit**  integer | Active connection ID limit (1 - 8). |
| **active_migration**  string | Enable/disable active migration .  **Choices:**   - `"enable"` - `"disable"` |
| **grease_quic_bit**  string | Enable/disable grease QUIC bit .  **Choices:**   - `"enable"` - `"disable"` |
| **max_ack_delay**  integer | Maximum ACK delay in milliseconds (1 - 16383). |
| **max_datagram_frame_size**  integer | Maximum datagram frame size in bytes (1 - 1500). |
| **max_idle_timeout**  integer | Maximum idle timeout milliseconds (1 - 60000). |
| **max_udp_payload_size**  integer | Maximum UDP payload size in bytes (1200 - 1500). |
| **realservers**  list / elements=dictionary | Select the real servers that this Access Proxy will distribute traffic to. |
| **addr_type**  string | Type of address.  **Choices:**   - `"ip"` - `"fqdn"` |
| **address**  string | Address or address group of the real server. Source firewall.address6.name firewall.addrgrp6.name. |
| **domain**  string | Wildcard domain name of the real server. |
| **external_auth**  string | Enable/disable use of external browser as user-agent for SAML user authentication.  **Choices:**   - `"enable"` - `"disable"` |
| **health_check**  string | Enable to check the responsiveness of the real server before forwarding traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **health_check_proto**  string | Protocol of the health check monitor to use when polling to determine server”s connectivity status.  **Choices:**   - `"ping"` - `"http"` - `"tcp-connect"` |
| **holddown_interval**  string | Enable/disable holddown timer. Server will be considered active and reachable once the holddown period has expired (30 seconds).  **Choices:**   - `"enable"` - `"disable"` |
| **http_host**  string | HTTP server domain name in HTTP header. |
| **id**  integer / required | Real server ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | IPv6 address of the real server. |
| **mappedport**  string | Port for communicating with the real server. |
| **port**  integer | Port for communicating with the real server. |
| **ssh_client_cert**  string | Set access-proxy SSH client certificate profile. Source firewall.access-proxy-ssh-client-cert.name. |
| **ssh_host_key**  list / elements=dictionary | One or more server host key. |
| **name**  string / required | Server host key name. Source firewall.ssh.host-key.name. |
| **ssh_host_key_validation**  string | Enable/disable SSH real server host key validation.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **translate_host**  string | Enable/disable translation of hostname/IP from virtual server to real server.  **Choices:**   - `"enable"` - `"disable"` |
| **tunnel_encryption**  string | Tunnel encryption.  **Choices:**   - `"enable"` - `"disable"` |
| **type**  string | TCP forwarding server type.  **Choices:**   - `"tcp-forwarding"` - `"ssh"` |
| **weight**  integer | Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connections. |
| **saml_redirect**  string | Enable/disable SAML redirection after successful authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **saml_server**  string | SAML service provider configuration for VIP authentication. Source user.saml.name. |
| **service**  string | Service.  **Choices:**   - `"http"` - `"https"` - `"tcp-forwarding"` - `"samlsp"` - `"web-portal"` - `"saas"` |
| **ssl_algorithm**  string | Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.  **Choices:**   - `"high"` - `"medium"` - `"low"` |
| **ssl_cipher_suites**  list / elements=dictionary | SSL/TLS cipher suites to offer to a server, ordered by priority. |
| **cipher**  string | Cipher suite name.  **Choices:**   - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` |
| **priority**  integer / required | SSL/TLS cipher suites priority. see <a href=’#notes’>Notes</a>. |
| **versions**  list / elements=string | SSL/TLS versions that the cipher suite can be used with.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_dh_bits**  string | Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.  **Choices:**   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl_max_version**  string | Highest SSL/TLS version acceptable from a server.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_min_version**  string | Lowest SSL/TLS version acceptable from a server.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_renegotiation**  string | Enable/disable secure renegotiation to comply with RFC 5746.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_vpn_web_portal**  string | SSL-VPN web portal. Source vpn.ssl.web.portal.name. |
| **url_map**  string | URL pattern to match. |
| **url_map_type**  string | Type of url-map.  **Choices:**   - `"sub-string"` - `"wildcard"` - `"regex"` |
| **virtual_host**  string | Virtual host. Source firewall.access-proxy-virtual-host.name. |
| **auth_portal**  string | Enable/disable authentication portal.  **Choices:**   - `"disable"` - `"enable"` |
| **auth_virtual_host**  string | Virtual host for authentication portal. Source firewall.access-proxy-virtual-host.name. |
| **client_cert**  string | Enable/disable to request client certificate.  **Choices:**   - `"disable"` - `"enable"` |
| **decrypted_traffic_mirror**  string | Decrypted traffic mirror. Source firewall.decrypted-traffic-mirror.name. |
| **empty_cert_action**  string | Action of an empty client certificate.  **Choices:**   - `"accept"` - `"block"` - `"accept-unmanageable"` |
| **http_supported_max_version**  string | Maximum supported HTTP versions. default = HTTP2  **Choices:**   - `"http1"` - `"http2"` |
| **ldb_method**  string | Method used to distribute sessions to SSL real servers.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"least-session"` - `"least-rtt"` - `"first-alive"` |
| **log_blocked_traffic**  string | Enable/disable logging of blocked traffic.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Access Proxy name. |
| **realservers**  list / elements=dictionary | Select the SSL real servers that this Access Proxy will distribute traffic to. |
| **id**  integer / required | Real server ID. see <a href=’#notes’>Notes</a>. |
| **ip**  string | IP address of the real server. |
| **port**  integer | Port for communicating with the real server. |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **weight**  integer | Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connections. |
| **server_pubkey_auth**  string | Enable/disable SSH real server public key authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **server_pubkey_auth_settings**  dictionary | Server SSH public key authentication settings. |
| **auth_ca**  string | Name of the SSH server public key authentication CA. Source firewall.ssh.local-ca.name. |
| **cert_extension**  list / elements=dictionary | Configure certificate extension for user certificate. |
| **critical**  string | Critical option.  **Choices:**   - `"no"` - `"yes"` |
| **data**  string | Name of certificate extension. |
| **name**  string / required | Name of certificate extension. |
| **type**  string | Type of certificate extension.  **Choices:**   - `"fixed"` - `"user"` |
| **permit_agent_forwarding**  string | Enable/disable appending permit-agent-forwarding certificate extension.  **Choices:**   - `"enable"` - `"disable"` |
| **permit_port_forwarding**  string | Enable/disable appending permit-port-forwarding certificate extension.  **Choices:**   - `"enable"` - `"disable"` |
| **permit_pty**  string | Enable/disable appending permit-pty certificate extension.  **Choices:**   - `"enable"` - `"disable"` |
| **permit_user_rc**  string | Enable/disable appending permit-user-rc certificate extension.  **Choices:**   - `"enable"` - `"disable"` |
| **permit_x11_forwarding**  string | Enable/disable appending permit-x11-forwarding certificate extension.  **Choices:**   - `"enable"` - `"disable"` |
| **source_address**  string | Enable/disable appending source-address certificate critical option. This option ensure certificate only accepted from FortiGate source address.  **Choices:**   - `"enable"` - `"disable"` |
| **svr_pool_multiplex**  string | Enable/disable server pool multiplexing. Share connected server in HTTP, HTTPS, and web-portal api-gateway.  **Choices:**   - `"enable"` - `"disable"` |
| **svr_pool_server_max_concurrent_request**  integer | Maximum number of concurrent requests that servers in server pool could handle . |
| **svr_pool_server_max_request**  integer | Maximum number of requests that servers in server pool handle before disconnecting . |
| **svr_pool_ttl**  integer | Time-to-live in the server pool for idle connections to servers. |
| **user_agent_detect**  string | Enable/disable to detect device type by HTTP user-agent if no client certificate provided.  **Choices:**   - `"disable"` - `"enable"` |
| **vip**  string | Virtual IP name. Source firewall.vip.name. |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_access_proxy_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_access_proxy_module.md#id5)

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
  - name: Configure IPv4 access proxy.
    fortios_firewall_access_proxy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_access_proxy:
        add_vhost_domain_to_dnsdb: "enable"
        api_gateway:
         -
            application:
             -
                name: "default_name_6"
            h2_support: "enable"
            h3_support: "enable"
            http_cookie_age: "60"
            http_cookie_domain: "<your_own_value>"
            http_cookie_domain_from_host: "disable"
            http_cookie_generation: "0"
            http_cookie_path: "<your_own_value>"
            http_cookie_share: "disable"
            https_cookie_secure: "disable"
            id:  "16"
            ldb_method: "static"
            persistence: "none"
            quic:
                ack_delay_exponent: "3"
                active_connection_id_limit: "2"
                active_migration: "enable"
                grease_quic_bit: "enable"
                max_ack_delay: "25"
                max_datagram_frame_size: "1500"
                max_idle_timeout: "30000"
                max_udp_payload_size: "1500"
            realservers:
             -
                addr_type: "ip"
                address: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
                domain: "<your_own_value>"
                external_auth: "enable"
                health_check: "disable"
                health_check_proto: "ping"
                holddown_interval: "enable"
                http_host: "myhostname"
                id:  "37"
                ip: "<your_own_value>"
                mappedport: "<your_own_value>"
                port: "443"
                ssh_client_cert: "<your_own_value> (source firewall.access-proxy-ssh-client-cert.name)"
                ssh_host_key:
                 -
                    name: "default_name_43 (source firewall.ssh.host-key.name)"
                ssh_host_key_validation: "disable"
                status: "active"
                translate_host: "enable"
                tunnel_encryption: "enable"
                type: "tcp-forwarding"
                weight: "1"
            saml_redirect: "disable"
            saml_server: "<your_own_value> (source user.saml.name)"
            service: "http"
            ssl_algorithm: "high"
            ssl_cipher_suites:
             -
                cipher: "TLS-AES-128-GCM-SHA256"
                priority: "<you_own_value>"
                versions: "tls-1.0"
            ssl_dh_bits: "768"
            ssl_max_version: "tls-1.0"
            ssl_min_version: "tls-1.0"
            ssl_renegotiation: "enable"
            ssl_vpn_web_portal: "<your_own_value> (source vpn.ssl.web.portal.name)"
            url_map: "<your_own_value>"
            url_map_type: "sub-string"
            virtual_host: "myhostname (source firewall.access-proxy-virtual-host.name)"
        api_gateway6:
         -
            application:
             -
                name: "default_name_68"
            h2_support: "enable"
            h3_support: "enable"
            http_cookie_age: "60"
            http_cookie_domain: "<your_own_value>"
            http_cookie_domain_from_host: "disable"
            http_cookie_generation: "0"
            http_cookie_path: "<your_own_value>"
            http_cookie_share: "disable"
            https_cookie_secure: "disable"
            id:  "78"
            ldb_method: "static"
            persistence: "none"
            quic:
                ack_delay_exponent: "3"
                active_connection_id_limit: "2"
                active_migration: "enable"
                grease_quic_bit: "enable"
                max_ack_delay: "25"
                max_datagram_frame_size: "1500"
                max_idle_timeout: "30000"
                max_udp_payload_size: "1500"
            realservers:
             -
                addr_type: "ip"
                address: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
                domain: "<your_own_value>"
                external_auth: "enable"
                health_check: "disable"
                health_check_proto: "ping"
                holddown_interval: "enable"
                http_host: "myhostname"
                id:  "99"
                ip: "<your_own_value>"
                mappedport: "<your_own_value>"
                port: "443"
                ssh_client_cert: "<your_own_value> (source firewall.access-proxy-ssh-client-cert.name)"
                ssh_host_key:
                 -
                    name: "default_name_105 (source firewall.ssh.host-key.name)"
                ssh_host_key_validation: "disable"
                status: "active"
                translate_host: "enable"
                tunnel_encryption: "enable"
                type: "tcp-forwarding"
                weight: "1"
            saml_redirect: "disable"
            saml_server: "<your_own_value> (source user.saml.name)"
            service: "http"
            ssl_algorithm: "high"
            ssl_cipher_suites:
             -
                cipher: "TLS-AES-128-GCM-SHA256"
                priority: "<you_own_value>"
                versions: "tls-1.0"
            ssl_dh_bits: "768"
            ssl_max_version: "tls-1.0"
            ssl_min_version: "tls-1.0"
            ssl_renegotiation: "enable"
            ssl_vpn_web_portal: "<your_own_value> (source vpn.ssl.web.portal.name)"
            url_map: "<your_own_value>"
            url_map_type: "sub-string"
            virtual_host: "myhostname (source firewall.access-proxy-virtual-host.name)"
        auth_portal: "disable"
        auth_virtual_host: "myhostname (source firewall.access-proxy-virtual-host.name)"
        client_cert: "disable"
        decrypted_traffic_mirror: "<your_own_value> (source firewall.decrypted-traffic-mirror.name)"
        empty_cert_action: "accept"
        http_supported_max_version: "http1"
        ldb_method: "static"
        log_blocked_traffic: "enable"
        name: "default_name_136"
        realservers:
         -
            id:  "138"
            ip: "<your_own_value>"
            port: "0"
            status: "active"
            weight: "1"
        server_pubkey_auth: "disable"
        server_pubkey_auth_settings:
            auth_ca: "<your_own_value> (source firewall.ssh.local-ca.name)"
            cert_extension:
             -
                critical: "no"
                data: "<your_own_value>"
                name: "default_name_149"
                type: "fixed"
            permit_agent_forwarding: "enable"
            permit_port_forwarding: "enable"
            permit_pty: "enable"
            permit_user_rc: "enable"
            permit_x11_forwarding: "enable"
            source_address: "enable"
        svr_pool_multiplex: "enable"
        svr_pool_server_max_concurrent_request: "0"
        svr_pool_server_max_request: "0"
        svr_pool_ttl: "15"
        user_agent_detect: "disable"
        vip: "<your_own_value> (source firewall.vip.name)"
```

## [Return Values](fortios_firewall_access_proxy_module.md#id6)

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
