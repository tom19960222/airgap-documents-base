---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_firewall_vip module – Configure virtual IP for IPv4 in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_firewall_vip_module.html
fetched_at: 2026-07-27T17:41:41+00:00
---
# fortinet.fortios.fortios_firewall_vip module – Configure virtual IP for IPv4 in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_vip_module.md#ansible-collections-fortinet-fortios-fortios-firewall-vip-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_vip`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_vip_module.md#synopsis)
- [Requirements](fortios_firewall_vip_module.md#requirements)
- [Parameters](fortios_firewall_vip_module.md#parameters)
- [Notes](fortios_firewall_vip_module.md#notes)
- [Examples](fortios_firewall_vip_module.md#examples)
- [Return Values](fortios_firewall_vip_module.md#return-values)

## [Synopsis](fortios_firewall_vip_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and vip category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_vip_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_firewall_vip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **firewall_vip**  dictionary | Configure virtual IP for IPv4. |
| **add_nat46_route**  string | Enable/disable adding NAT46 route.  Choices:   - `"disable"` - `"enable"` |
| **arp_reply**  string | Enable to respond to ARP requests for this virtual IP address. Enabled by default.  Choices:   - `"disable"` - `"enable"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  string | Comment. |
| **dns_mapping_ttl**  integer | DNS mapping TTL (Set to zero to use TTL in DNS response). |
| **extaddr**  list / elements=dictionary | External FQDN address name. |
| **name**  string | Address name. Source firewall.address.name firewall.addrgrp.name. |
| **extintf**  string | Interface connected to the source network that receives the packets that will be forwarded to the destination network. Source system .interface.name. |
| **extip**  string | IP address or address range on the external interface that you want to map to an address or address range on the destination network. |
| **extport**  string | Incoming port number range that you want to map to a port number range on the destination network. |
| **gratuitous_arp_interval**  integer | Enable to have the VIP send gratuitous ARPs. 0=disabled. Set from 5 up to 8640000 seconds to enable. |
| **http_cookie_age**  integer | Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit. |
| **http_cookie_domain**  string | Domain that HTTP cookie persistence should apply to. |
| **http_cookie_domain_from_host**  string | Enable/disable use of HTTP cookie domain from host field in HTTP.  Choices:   - `"disable"` - `"enable"` |
| **http_cookie_generation**  integer | Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies. |
| **http_cookie_path**  string | Limit HTTP cookie persistence to the specified path. |
| **http_cookie_share**  string | Control sharing of cookies across virtual servers. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.  Choices:   - `"disable"` - `"same-ip"` |
| **http_ip_header**  string | For HTTP multiplexing, enable to add the original client IP address in the XForwarded-For HTTP header.  Choices:   - `"enable"` - `"disable"` |
| **http_ip_header_name**  string | For HTTP multiplexing, enter a custom HTTPS header name. The original client IP address is added to this header. If empty, X-Forwarded-For is used. |
| **http_multiplex**  string | Enable/disable HTTP multiplexing.  Choices:   - `"enable"` - `"disable"` |
| **http_redirect**  string | Enable/disable redirection of HTTP to HTTPS.  Choices:   - `"enable"` - `"disable"` |
| **https_cookie_secure**  string | Enable/disable verification that inserted HTTPS cookies are secure.  Choices:   - `"disable"` - `"enable"` |
| **id**  integer | Custom defined ID. |
| **ipv6_mappedip**  string | Range of mapped IPv6 addresses. Specify the start IPv6 address followed by a space and the end IPv6 address. |
| **ipv6_mappedport**  string | IPv6 port number range on the destination network to which the external port number range is mapped. |
| **ldb_method**  string | Method used to distribute sessions to real servers.  Choices:   - `"static"` - `"round-robin"` - `"weighted"` - `"least-session"` - `"least-rtt"` - `"first-alive"` - `"http-host"` |
| **mapped_addr**  string | Mapped FQDN address name. Source firewall.address.name. |
| **mappedip**  list / elements=dictionary | IP address or address range on the destination network to which the external IP address is mapped. |
| **range**  string | Mapped IP range. |
| **mappedport**  string | Port number range on the destination network to which the external port number range is mapped. |
| **max_embryonic_connections**  integer | Maximum number of incomplete connections. |
| **monitor**  list / elements=dictionary | Name of the health check monitor to use when polling to determine a virtual server”s connectivity status. |
| **name**  string | Health monitor name. Source firewall.ldb-monitor.name. |
| **name**  string / required | Virtual IP name. |
| **nat44**  string | Enable/disable NAT44.  Choices:   - `"disable"` - `"enable"` |
| **nat46**  string | Enable/disable NAT46.  Choices:   - `"disable"` - `"enable"` |
| **nat_source_vip**  string | Enable/disable forcing the source NAT mapped IP to the external IP for all traffic.  Choices:   - `"disable"` - `"enable"` |
| **outlook_web_access**  string | Enable to add the Front-End-Https header for Microsoft Outlook Web Access.  Choices:   - `"disable"` - `"enable"` |
| **persistence**  string | Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.  Choices:   - `"none"` - `"http-cookie"` - `"ssl-session-id"` |
| **portforward**  string | Enable/disable port forwarding.  Choices:   - `"disable"` - `"enable"` |
| **portmapping_type**  string | Port mapping type.  Choices:   - `"1-to-1"` - `"m-to-n"` |
| **protocol**  string | Protocol to use when forwarding packets.  Choices:   - `"tcp"` - `"udp"` - `"sctp"` - `"icmp"` |
| **realservers**  list / elements=dictionary | Select the real servers that this server load balancing VIP will distribute traffic to. |
| **address**  string | Dynamic address of the real server. Source firewall.address.name. |
| **client_ip**  string | Only clients in this IP range can connect to this real server. |
| **healthcheck**  string | Enable to check the responsiveness of the real server before forwarding traffic.  Choices:   - `"disable"` - `"enable"` - `"vip"` |
| **holddown_interval**  integer | Time in seconds that the health check monitor continues to monitor and unresponsive server that should be active. |
| **http_host**  string | HTTP server domain name in HTTP header. |
| **id**  integer | Real server ID. |
| **ip**  string | IP address of the real server. |
| **max_connections**  integer | Max number of active connections that can be directed to the real server. When reached, sessions are sent to other real servers. |
| **monitor**  list / elements=dictionary | Name of the health check monitor to use when polling to determine a virtual server”s connectivity status. Source firewall .ldb-monitor.name. |
| **name**  string | Health monitor name. Source firewall.ldb-monitor.name. |
| **port**  integer | Port for communicating with the real server. Required if port forwarding is enabled. |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.  Choices:   - `"active"` - `"standby"` - `"disable"` |
| **type**  string | Type of address.  Choices:   - `"ip"` - `"address"` |
| **weight**  integer | Weight of the real server. If weighted load balancing is enabled, the server with the highest weight gets more connections. |
| **server_type**  string | Protocol to be load balanced by the virtual server (also called the server load balance virtual IP).  Choices:   - `"http"` - `"https"` - `"imaps"` - `"pop3s"` - `"smtps"` - `"ssl"` - `"tcp"` - `"udp"` - `"ip"` - `"ssh"` |
| **service**  list / elements=dictionary | Service name. |
| **name**  string | Service name. Source firewall.service.custom.name firewall.service.group.name. |
| **src_filter**  list / elements=dictionary | Source address filter. Each address must be either an IP/subnet (x.x.x.x/n) or a range (x.x.x.x-y.y.y.y). Separate addresses with spaces. |
| **range**  string | Source-filter range. |
| **srcintf_filter**  list / elements=dictionary | Interfaces to which the VIP applies. Separate the names with spaces. |
| **interface_name**  string | Interface name. Source system.interface.name. |
| **ssl_accept_ffdhe_groups**  string | Enable/disable FFDHE cipher suite for SSL key exchange.  Choices:   - `"enable"` - `"disable"` |
| **ssl_algorithm**  string | Permitted encryption algorithms for SSL sessions according to encryption strength.  Choices:   - `"high"` - `"medium"` - `"low"` - `"custom"` |
| **ssl_certificate**  string | The name of the certificate to use for SSL handshake. Source vpn.certificate.local.name. |
| **ssl_cipher_suites**  list / elements=dictionary | SSL/TLS cipher suites acceptable from a client, ordered by priority. |
| **cipher**  string | Cipher suite name.  Choices:   - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` |
| **priority**  integer | SSL/TLS cipher suites priority. |
| **versions**  list / elements=string | SSL/TLS versions that the cipher suite can be used with.  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_client_fallback**  string | Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507).  Choices:   - `"disable"` - `"enable"` |
| **ssl_client_rekey_count**  integer | Maximum length of data in MB before triggering a client rekey (0 = disable). |
| **ssl_client_renegotiation**  string | Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746.  Choices:   - `"allow"` - `"deny"` - `"secure"` |
| **ssl_client_session_state_max**  integer | Maximum number of client to FortiGate SSL session states to keep. |
| **ssl_client_session_state_timeout**  integer | Number of minutes to keep client to FortiGate SSL session state. |
| **ssl_client_session_state_type**  string | How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate.  Choices:   - `"disable"` - `"time"` - `"count"` - `"both"` |
| **ssl_dh_bits**  string | Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.  Choices:   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl_hpkp**  string | Enable/disable including HPKP header in response.  Choices:   - `"disable"` - `"enable"` - `"report-only"` |
| **ssl_hpkp_age**  integer | Number of seconds the client should honor the HPKP setting. |
| **ssl_hpkp_backup**  string | Certificate to generate backup HPKP pin from. Source vpn.certificate.local.name vpn.certificate.ca.name. |
| **ssl_hpkp_include_subdomains**  string | Indicate that HPKP header applies to all subdomains.  Choices:   - `"disable"` - `"enable"` |
| **ssl_hpkp_primary**  string | Certificate to generate primary HPKP pin from. Source vpn.certificate.local.name vpn.certificate.ca.name. |
| **ssl_hpkp_report_uri**  string | URL to report HPKP violations to. |
| **ssl_hsts**  string | Enable/disable including HSTS header in response.  Choices:   - `"disable"` - `"enable"` |
| **ssl_hsts_age**  integer | Number of seconds the client should honor the HSTS setting. |
| **ssl_hsts_include_subdomains**  string | Indicate that HSTS header applies to all subdomains.  Choices:   - `"disable"` - `"enable"` |
| **ssl_http_location_conversion**  string | Enable to replace HTTP with HTTPS in the reply”s Location HTTP header field.  Choices:   - `"enable"` - `"disable"` |
| **ssl_http_match_host**  string | Enable/disable HTTP host matching for location conversion.  Choices:   - `"enable"` - `"disable"` |
| **ssl_max_version**  string | Highest SSL/TLS version acceptable from a client.  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_min_version**  string | Lowest SSL/TLS version acceptable from a client.  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_mode**  string | Apply SSL offloading between the client and the FortiGate (half) or from the client to the FortiGate and from the FortiGate to the server (full).  Choices:   - `"half"` - `"full"` |
| **ssl_pfs**  string | Select the cipher suites that can be used for SSL perfect forward secrecy (PFS). Applies to both client and server sessions.  Choices:   - `"require"` - `"deny"` - `"allow"` |
| **ssl_send_empty_frags**  string | Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3.0 & TLS 1.0 only). May need to be disabled for compatibility with older systems.  Choices:   - `"enable"` - `"disable"` |
| **ssl_server_algorithm**  string | Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.  Choices:   - `"high"` - `"medium"` - `"low"` - `"custom"` - `"client"` |
| **ssl_server_cipher_suites**  list / elements=dictionary | SSL/TLS cipher suites to offer to a server, ordered by priority. |
| **cipher**  string | Cipher suite name.  Choices:   - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` |
| **priority**  integer | SSL/TLS cipher suites priority. |
| **versions**  list / elements=string | SSL/TLS versions that the cipher suite can be used with.  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl_server_max_version**  string | Highest SSL/TLS version acceptable from a server. Use the client setting by default.  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` - `"client"` |
| **ssl_server_min_version**  string | Lowest SSL/TLS version acceptable from a server. Use the client setting by default.  Choices:   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` - `"client"` |
| **ssl_server_session_state_max**  integer | Maximum number of FortiGate to Server SSL session states to keep. |
| **ssl_server_session_state_timeout**  integer | Number of minutes to keep FortiGate to Server SSL session state. |
| **ssl_server_session_state_type**  string | How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate.  Choices:   - `"disable"` - `"time"` - `"count"` - `"both"` |
| **status**  string | Enable/disable VIP.  Choices:   - `"disable"` - `"enable"` |
| **type**  string | Configure a static NAT, load balance, server load balance, access proxy, DNS translation, or FQDN VIP.  Choices:   - `"static-nat"` - `"load-balance"` - `"server-load-balance"` - `"dns-translation"` - `"fqdn"` - `"access-proxy"` |
| **uuid**  string | Universally Unique Identifier (UUID; automatically assigned but can be manually reset). |
| **weblogic_server**  string | Enable to add an HTTP header to indicate SSL offloading for a WebLogic server.  Choices:   - `"disable"` - `"enable"` |
| **websphere_server**  string | Enable to add an HTTP header to indicate SSL offloading for a WebSphere server.  Choices:   - `"disable"` - `"enable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  Choices:   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_firewall_vip_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_vip_module.md#id5)

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
  - name: Configure virtual IP for IPv4.
    fortios_firewall_vip:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_vip:
        add_nat46_route: "disable"
        arp_reply: "disable"
        color: "0"
        comment: "Comment."
        dns_mapping_ttl: "0"
        extaddr:
         -
            name: "default_name_9 (source firewall.address.name firewall.addrgrp.name)"
        extintf: "<your_own_value> (source system.interface.name)"
        extip: "<your_own_value>"
        extport: "<your_own_value>"
        gratuitous_arp_interval: "0"
        http_cookie_age: "60"
        http_cookie_domain: "<your_own_value>"
        http_cookie_domain_from_host: "disable"
        http_cookie_generation: "0"
        http_cookie_path: "<your_own_value>"
        http_cookie_share: "disable"
        http_ip_header: "enable"
        http_ip_header_name: "<your_own_value>"
        http_multiplex: "enable"
        http_redirect: "enable"
        https_cookie_secure: "disable"
        id:  "25"
        ipv6_mappedip: "<your_own_value>"
        ipv6_mappedport: "<your_own_value>"
        ldb_method: "static"
        mapped_addr: "<your_own_value> (source firewall.address.name)"
        mappedip:
         -
            range: "<your_own_value>"
        mappedport: "<your_own_value>"
        max_embryonic_connections: "1000"
        monitor:
         -
            name: "default_name_35 (source firewall.ldb-monitor.name)"
        name: "default_name_36"
        nat_source_vip: "disable"
        nat44: "disable"
        nat46: "disable"
        outlook_web_access: "disable"
        persistence: "none"
        portforward: "disable"
        portmapping_type: "1-to-1"
        protocol: "tcp"
        realservers:
         -
            address: "<your_own_value> (source firewall.address.name)"
            client_ip: "<your_own_value>"
            healthcheck: "disable"
            holddown_interval: "300"
            http_host: "myhostname"
            id:  "51"
            ip: "<your_own_value>"
            max_connections: "0"
            monitor:
             -
                name: "default_name_55 (source firewall.ldb-monitor.name)"
            port: "0"
            status: "active"
            type: "ip"
            weight: "1"
        server_type: "http"
        service:
         -
            name: "default_name_62 (source firewall.service.custom.name firewall.service.group.name)"
        src_filter:
         -
            range: "<your_own_value>"
        srcintf_filter:
         -
            interface_name: "<your_own_value> (source system.interface.name)"
        ssl_accept_ffdhe_groups: "enable"
        ssl_algorithm: "high"
        ssl_certificate: "<your_own_value> (source vpn.certificate.local.name)"
        ssl_cipher_suites:
         -
            cipher: "TLS-AES-128-GCM-SHA256"
            priority: "0"
            versions: "ssl-3.0"
        ssl_client_fallback: "disable"
        ssl_client_rekey_count: "0"
        ssl_client_renegotiation: "allow"
        ssl_client_session_state_max: "1000"
        ssl_client_session_state_timeout: "30"
        ssl_client_session_state_type: "disable"
        ssl_dh_bits: "768"
        ssl_hpkp: "disable"
        ssl_hpkp_age: "5184000"
        ssl_hpkp_backup: "<your_own_value> (source vpn.certificate.local.name vpn.certificate.ca.name)"
        ssl_hpkp_include_subdomains: "disable"
        ssl_hpkp_primary: "<your_own_value> (source vpn.certificate.local.name vpn.certificate.ca.name)"
        ssl_hpkp_report_uri: "<your_own_value>"
        ssl_hsts: "disable"
        ssl_hsts_age: "5184000"
        ssl_hsts_include_subdomains: "disable"
        ssl_http_location_conversion: "enable"
        ssl_http_match_host: "enable"
        ssl_max_version: "ssl-3.0"
        ssl_min_version: "ssl-3.0"
        ssl_mode: "half"
        ssl_pfs: "require"
        ssl_send_empty_frags: "enable"
        ssl_server_algorithm: "high"
        ssl_server_cipher_suites:
         -
            cipher: "TLS-AES-128-GCM-SHA256"
            priority: "0"
            versions: "ssl-3.0"
        ssl_server_max_version: "ssl-3.0"
        ssl_server_min_version: "ssl-3.0"
        ssl_server_session_state_max: "100"
        ssl_server_session_state_timeout: "60"
        ssl_server_session_state_type: "disable"
        status: "disable"
        type: "static-nat"
        uuid: "<your_own_value>"
        weblogic_server: "disable"
        websphere_server: "disable"
```

## [Return Values](fortios_firewall_vip_module.md#id6)

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
