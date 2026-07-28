---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_vip module – Configure virtual IP for IPv4."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_vip_module.html
fetched_at: 2026-07-28T02:13:04+00:00
---
# fortinet.fortimanager.fmgr_firewall_vip module – Configure virtual IP for IPv4.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_vip`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_vip_module.md#synopsis)
- [Parameters](fmgr_firewall_vip_module.md#parameters)
- [Notes](fmgr_firewall_vip_module.md#notes)
- [Examples](fmgr_firewall_vip_module.md#examples)
- [Return Values](fmgr_firewall_vip_module.md#return-values)

## [Synopsis](fmgr_firewall_vip_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_vip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_vip**  dictionary | the top level parameters set |
| **add-nat46-route**  string | Enable/disable adding NAT46 route.  **Choices:**   - `"disable"` - `"enable"` |
| **arp-reply**  string | Enable to respond to ARP requests for this virtual IP address.  **Choices:**   - `"disable"` - `"enable"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  string | Comment. |
| **dns-mapping-ttl**  integer | DNS mapping TTL |
| **dynamic_mapping**  list / elements=dictionary | Dynamic_Mapping. |
| **_scope**  list / elements=dictionary | _Scope. |
| **name**  string | Name. |
| **vdom**  string | Vdom. |
| **add-nat46-route**  string | Enable/disable adding NAT46 route.  **Choices:**   - `"disable"` - `"enable"` |
| **arp-reply**  string | Enable to respond to ARP requests for this virtual IP address.  **Choices:**   - `"disable"` - `"enable"` |
| **color**  integer | Color of icon on the GUI. |
| **comment**  string | Comment. |
| **dns-mapping-ttl**  integer | DNS mapping TTL |
| **extaddr**  any | (list or str) External FQDN address name. |
| **extintf**  string | Interface connected to the source network that receives the packets that will be forwarded to the destination network. |
| **extip**  string | IP address or address range on the external interface that you want to map to an address or address range on the destin… |
| **extport**  string | Incoming port number range that you want to map to a port number range on the destination network. |
| **gratuitous-arp-interval**  integer | Enable to have the VIP send gratuitous ARPs. |
| **h2-support**  string | Enable/disable HTTP2 support  **Choices:**   - `"disable"` - `"enable"` |
| **h3-support**  string | Enable/disable HTTP3/QUIC support  **Choices:**   - `"disable"` - `"enable"` |
| **http-cookie-age**  integer | Time in minutes that client web browsers should keep a cookie. |
| **http-cookie-domain**  string | Domain that HTTP cookie persistence should apply to. |
| **http-cookie-domain-from-host**  string | Enable/disable use of HTTP cookie domain from host field in HTTP.  **Choices:**   - `"disable"` - `"enable"` |
| **http-cookie-generation**  integer | Generation of HTTP cookie to be accepted. |
| **http-cookie-path**  string | Limit HTTP cookie persistence to the specified path. |
| **http-cookie-share**  string | Control sharing of cookies across virtual servers.  **Choices:**   - `"disable"` - `"same-ip"` |
| **http-ip-header**  string | For HTTP multiplexing, enable to add the original client IP address in the XForwarded-For HTTP header.  **Choices:**   - `"disable"` - `"enable"` |
| **http-ip-header-name**  string | For HTTP multiplexing, enter a custom HTTPS header name. |
| **http-multiplex**  string | Enable/disable HTTP multiplexing.  **Choices:**   - `"disable"` - `"enable"` |
| **http-multiplex-max-concurrent-request**  integer | Maximum number of concurrent requests that a multiplex server can handle |
| **http-multiplex-max-request**  integer | Maximum number of requests that a multiplex server can handle before disconnecting sessions |
| **http-multiplex-ttl**  integer | Time-to-live for idle connections to servers. |
| **http-redirect**  string | Enable/disable redirection of HTTP to HTTPS  **Choices:**   - `"disable"` - `"enable"` |
| **http-supported-max-version**  string | Maximum supported HTTP versions.  **Choices:**   - `"http1"` - `"http2"` |
| **https-cookie-secure**  string | Enable/disable verification that inserted HTTPS cookies are secure.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer | Custom defined ID. |
| **ipv6-mappedip**  string | Range of mapped IPv6 addresses. |
| **ipv6-mappedport**  string | IPv6 port number range on the destination network to which the external port number range is mapped. |
| **ldb-method**  string | Method used to distribute sessions to real servers.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"least-session"` - `"least-rtt"` - `"first-alive"` - `"http-host"` |
| **mapped-addr**  string | Mapped FQDN address name. |
| **mappedip**  any | (list) IP address or address range on the destination network to which the external IP address is mapped. |
| **mappedport**  string | Port number range on the destination network to which the external port number range is mapped. |
| **max-embryonic-connections**  integer | Maximum number of incomplete connections. |
| **monitor**  any | (list or str) Name of the health check monitor to use when polling to determine a virtual servers connectivity status. |
| **nat-source-vip**  string | Enable/disable forcing the source NAT mapped IP to the external IP for all traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **nat44**  string | Enable/disable NAT44.  **Choices:**   - `"disable"` - `"enable"` |
| **nat46**  string | Enable/disable NAT46.  **Choices:**   - `"disable"` - `"enable"` |
| **outlook-web-access**  string | Enable to add the Front-End-Https header for Microsoft Outlook Web Access.  **Choices:**   - `"disable"` - `"enable"` |
| **persistence**  string | Configure how to make sure that clients connect to the same server every time they make a request that is part of the s…  **Choices:**   - `"none"` - `"http-cookie"` - `"ssl-session-id"` |
| **portforward**  string | Enable/disable port forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **portmapping-type**  string | Port mapping type.  **Choices:**   - `"1-to-1"` - `"m-to-n"` |
| **protocol**  string | Protocol to use when forwarding packets.  **Choices:**   - `"tcp"` - `"udp"` - `"sctp"` - `"icmp"` |
| **realservers**  list / elements=dictionary | Realservers. |
| **address**  string | Address. |
| **client-ip**  any | (list) Only clients in this IP range can connect to this real server. |
| **health-check-proto**  string | no description  **Choices:**   - `"ping"` - `"http"` |
| **healthcheck**  string | Enable to check the responsiveness of the real server before forwarding traffic.  **Choices:**   - `"disable"` - `"enable"` - `"vip"` |
| **holddown-interval**  integer | Time in seconds that the health check monitor continues to monitor and unresponsive server that should be active. |
| **http-host**  string | HTTP server domain name in HTTP header. |
| **id**  integer | Real server ID. |
| **ip**  string | IP address of the real server. |
| **max-connections**  integer | Max number of active connections that can be directed to the real server. |
| **monitor**  any | (list or str) Name of the health check monitor to use when polling to determine a virtual servers connectivity … |
| **port**  integer | Port for communicating with the real server. |
| **seq**  integer | Seq. |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traf…  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **translate-host**  string | Enable/disable translation of hostname/IP from virtual server to real server.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | Type.  **Choices:**   - `"ip"` - `"address"` |
| **weight**  integer | Weight of the real server. |
| **server-type**  string | Protocol to be load balanced by the virtual server  **Choices:**   - `"http"` - `"https"` - `"ssl"` - `"tcp"` - `"udp"` - `"ip"` - `"imaps"` - `"pop3s"` - `"smtps"` - `"ssh"` |
| **service**  any | (list or str) Service name. |
| **src-filter**  any | (list) Source address filter. |
| **srcintf-filter**  any | (list) Interfaces to which the VIP applies. |
| **ssl-accept-ffdhe-groups**  string | Enable/disable FFDHE cipher suite for SSL key exchange.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-algorithm**  string | Permitted encryption algorithms for SSL sessions according to encryption strength.  **Choices:**   - `"high"` - `"medium"` - `"low"` - `"custom"` |
| **ssl-certificate**  string | The name of the SSL certificate to use for SSL acceleration. |
| **ssl-cipher-suites**  list / elements=dictionary | Ssl-Cipher-Suites. |
| **cipher**  string | Cipher suite name.  **Choices:**   - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` |
| **id**  integer | Id. |
| **priority**  integer | SSL/TLS cipher suites priority. |
| **versions**  list / elements=string | SSL/TLS versions that the cipher suite can be used with.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-client-fallback**  string | Enable/disable support for preventing Downgrade Attacks on client connections  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-client-rekey-count**  integer | Maximum length of data in MB before triggering a client rekey |
| **ssl-client-renegotiation**  string | Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746.  **Choices:**   - `"deny"` - `"allow"` - `"secure"` |
| **ssl-client-session-state-max**  integer | Maximum number of client to FortiGate SSL session states to keep. |
| **ssl-client-session-state-timeout**  integer | Number of minutes to keep client to FortiGate SSL session state. |
| **ssl-client-session-state-type**  string | How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate.  **Choices:**   - `"disable"` - `"time"` - `"count"` - `"both"` |
| **ssl-dh-bits**  string | Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.  **Choices:**   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl-hpkp**  string | Enable/disable including HPKP header in response.  **Choices:**   - `"disable"` - `"enable"` - `"report-only"` |
| **ssl-hpkp-age**  integer | Number of seconds the client should honour the HPKP setting. |
| **ssl-hpkp-backup**  string | Certificate to generate backup HPKP pin from. |
| **ssl-hpkp-include-subdomains**  string | Indicate that HPKP header applies to all subdomains.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-hpkp-primary**  string | Certificate to generate primary HPKP pin from. |
| **ssl-hpkp-report-uri**  string | URL to report HPKP violations to. |
| **ssl-hsts**  string | Enable/disable including HSTS header in response.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-hsts-age**  integer | Number of seconds the client should honour the HSTS setting. |
| **ssl-hsts-include-subdomains**  string | Indicate that HSTS header applies to all subdomains.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-http-location-conversion**  string | Enable to replace HTTP with HTTPS in the replys Location HTTP header field.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-http-match-host**  string | Enable/disable HTTP host matching for location conversion.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-max-version**  string | Highest SSL/TLS version acceptable from a client.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-min-version**  string | Lowest SSL/TLS version acceptable from a client.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-mode**  string | Apply SSL offloading between the client and the FortiGate  **Choices:**   - `"half"` - `"full"` |
| **ssl-pfs**  string | Select the cipher suites that can be used for SSL perfect forward secrecy  **Choices:**   - `"require"` - `"deny"` - `"allow"` |
| **ssl-send-empty-frags**  string | Enable/disable sending empty fragments to avoid CBC IV attacks  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server-algorithm**  string | Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.  **Choices:**   - `"high"` - `"low"` - `"medium"` - `"custom"` - `"client"` |
| **ssl-server-max-version**  string | Highest SSL/TLS version acceptable from a server.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"client"` - `"tls-1.3"` |
| **ssl-server-min-version**  string | Lowest SSL/TLS version acceptable from a server.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"client"` - `"tls-1.3"` |
| **ssl-server-renegotiation**  string | Enable/disable secure renegotiation to comply with RFC 5746.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server-session-state-max**  integer | Maximum number of FortiGate to Server SSL session states to keep. |
| **ssl-server-session-state-timeout**  integer | Number of minutes to keep FortiGate to Server SSL session state. |
| **ssl-server-session-state-type**  string | How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate.  **Choices:**   - `"disable"` - `"time"` - `"count"` - `"both"` |
| **status**  string | Enable/disable VIP.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | Configure a static NAT, load balance, server load balance, DNS translation, or FQDN VIP.  **Choices:**   - `"static-nat"` - `"load-balance"` - `"server-load-balance"` - `"dns-translation"` - `"fqdn"` - `"access-proxy"` |
| **uuid**  string | Universally Unique Identifier |
| **weblogic-server**  string | Enable to add an HTTP header to indicate SSL offloading for a WebLogic server.  **Choices:**   - `"disable"` - `"enable"` |
| **websphere-server**  string | Enable to add an HTTP header to indicate SSL offloading for a WebSphere server.  **Choices:**   - `"disable"` - `"enable"` |
| **extaddr**  any | (list or str) External FQDN address name. |
| **extintf**  string | Interface connected to the source network that receives the packets that will be forwarded to the destination network. |
| **extip**  string | IP address or address range on the external interface that you want to map to an address or address range on the destination ne… |
| **extport**  string | Incoming port number range that you want to map to a port number range on the destination network. |
| **gratuitous-arp-interval**  integer | Enable to have the VIP send gratuitous ARPs. |
| **h2-support**  string | Enable/disable HTTP2 support  **Choices:**   - `"disable"` - `"enable"` |
| **h3-support**  string | Enable/disable HTTP3/QUIC support  **Choices:**   - `"disable"` - `"enable"` |
| **http-cookie-age**  integer | Time in minutes that client web browsers should keep a cookie. |
| **http-cookie-domain**  string | Domain that HTTP cookie persistence should apply to. |
| **http-cookie-domain-from-host**  string | Enable/disable use of HTTP cookie domain from host field in HTTP.  **Choices:**   - `"disable"` - `"enable"` |
| **http-cookie-generation**  integer | Generation of HTTP cookie to be accepted. |
| **http-cookie-path**  string | Limit HTTP cookie persistence to the specified path. |
| **http-cookie-share**  string | Control sharing of cookies across virtual servers.  **Choices:**   - `"disable"` - `"same-ip"` |
| **http-ip-header**  string | For HTTP multiplexing, enable to add the original client IP address in the XForwarded-For HTTP header.  **Choices:**   - `"disable"` - `"enable"` |
| **http-ip-header-name**  string | For HTTP multiplexing, enter a custom HTTPS header name. |
| **http-multiplex**  string | Enable/disable HTTP multiplexing.  **Choices:**   - `"disable"` - `"enable"` |
| **http-multiplex-max-concurrent-request**  integer | Maximum number of concurrent requests that a multiplex server can handle |
| **http-multiplex-max-request**  integer | Maximum number of requests that a multiplex server can handle before disconnecting sessions |
| **http-multiplex-ttl**  integer | Time-to-live for idle connections to servers. |
| **http-redirect**  string | Enable/disable redirection of HTTP to HTTPS  **Choices:**   - `"disable"` - `"enable"` |
| **http-supported-max-version**  string | Maximum supported HTTP versions.  **Choices:**   - `"http1"` - `"http2"` |
| **https-cookie-secure**  string | Enable/disable verification that inserted HTTPS cookies are secure.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer | Custom defined ID. |
| **ipv6-mappedip**  string | Range of mapped IPv6 addresses. |
| **ipv6-mappedport**  string | IPv6 port number range on the destination network to which the external port number range is mapped. |
| **ldb-method**  string | Method used to distribute sessions to real servers.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"least-session"` - `"least-rtt"` - `"first-alive"` - `"http-host"` |
| **mapped-addr**  string | Mapped FQDN address name. |
| **mappedip**  any | (list) IP address or address range on the destination network to which the external IP address is mapped. |
| **mappedport**  string | Port number range on the destination network to which the external port number range is mapped. |
| **max-embryonic-connections**  integer | Maximum number of incomplete connections. |
| **monitor**  any | (list or str) Name of the health check monitor to use when polling to determine a virtual servers connectivity status. |
| **name**  string / required | Virtual IP name. |
| **nat-source-vip**  string | Enable/disable forcing the source NAT mapped IP to the external IP for all traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **nat44**  string | Enable/disable NAT44.  **Choices:**   - `"disable"` - `"enable"` |
| **nat46**  string | Enable/disable NAT46.  **Choices:**   - `"disable"` - `"enable"` |
| **outlook-web-access**  string | Enable to add the Front-End-Https header for Microsoft Outlook Web Access.  **Choices:**   - `"disable"` - `"enable"` |
| **persistence**  string | Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.  **Choices:**   - `"none"` - `"http-cookie"` - `"ssl-session-id"` |
| **portforward**  string | Enable/disable port forwarding.  **Choices:**   - `"disable"` - `"enable"` |
| **portmapping-type**  string | Port mapping type.  **Choices:**   - `"1-to-1"` - `"m-to-n"` |
| **protocol**  string | Protocol to use when forwarding packets.  **Choices:**   - `"tcp"` - `"udp"` - `"sctp"` - `"icmp"` |
| **quic**  dictionary | no description |
| **ack-delay-exponent**  integer | ACK delay exponent |
| **active-connection-id-limit**  integer | Active connection ID limit |
| **active-migration**  string | Enable/disable active migration  **Choices:**   - `"disable"` - `"enable"` |
| **grease-quic-bit**  string | Enable/disable grease QUIC bit  **Choices:**   - `"disable"` - `"enable"` |
| **max-ack-delay**  integer | Maximum ACK delay in milliseconds |
| **max-datagram-frame-size**  integer | Maximum datagram frame size in bytes |
| **max-idle-timeout**  integer | Maximum idle timeout milliseconds |
| **max-udp-payload-size**  integer | Maximum UDP payload size in bytes |
| **realservers**  list / elements=dictionary | Realservers. |
| **address**  string | Dynamic address of the real server. |
| **client-ip**  any | (list) Only clients in this IP range can connect to this real server. |
| **healthcheck**  string | Enable to check the responsiveness of the real server before forwarding traffic.  **Choices:**   - `"disable"` - `"enable"` - `"vip"` |
| **holddown-interval**  integer | Time in seconds that the health check monitor continues to monitor and unresponsive server that should be active. |
| **http-host**  string | HTTP server domain name in HTTP header. |
| **id**  integer | Real server ID. |
| **ip**  string | IP address of the real server. |
| **max-connections**  integer | Max number of active connections that can be directed to the real server. |
| **monitor**  any | (list or str) Name of the health check monitor to use when polling to determine a virtual servers connectivity status. |
| **port**  integer | Port for communicating with the real server. |
| **seq**  integer | Seq. |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traffic is sent.  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **translate-host**  string | Enable/disable translation of hostname/IP from virtual server to real server.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | Type of address.  **Choices:**   - `"ip"` - `"address"` |
| **weight**  integer | Weight of the real server. |
| **server-type**  string | Protocol to be load balanced by the virtual server  **Choices:**   - `"http"` - `"https"` - `"ssl"` - `"tcp"` - `"udp"` - `"ip"` - `"imaps"` - `"pop3s"` - `"smtps"` - `"ssh"` |
| **service**  any | (list or str) Service name. |
| **src-filter**  any | (list) Source address filter. |
| **srcintf-filter**  any | (list or str) Interfaces to which the VIP applies. |
| **ssl-accept-ffdhe-groups**  string | Enable/disable FFDHE cipher suite for SSL key exchange.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-algorithm**  string | Permitted encryption algorithms for SSL sessions according to encryption strength.  **Choices:**   - `"high"` - `"medium"` - `"low"` - `"custom"` |
| **ssl-certificate**  string | The name of the SSL certificate to use for SSL acceleration. |
| **ssl-cipher-suites**  list / elements=dictionary | Ssl-Cipher-Suites. |
| **cipher**  string | Cipher suite name.  **Choices:**   - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` |
| **id**  integer | Id. |
| **priority**  integer | SSL/TLS cipher suites priority. |
| **versions**  list / elements=string | SSL/TLS versions that the cipher suite can be used with.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-client-fallback**  string | Enable/disable support for preventing Downgrade Attacks on client connections  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-client-rekey-count**  integer | Maximum length of data in MB before triggering a client rekey |
| **ssl-client-renegotiation**  string | Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746.  **Choices:**   - `"deny"` - `"allow"` - `"secure"` |
| **ssl-client-session-state-max**  integer | Maximum number of client to FortiGate SSL session states to keep. |
| **ssl-client-session-state-timeout**  integer | Number of minutes to keep client to FortiGate SSL session state. |
| **ssl-client-session-state-type**  string | How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate.  **Choices:**   - `"disable"` - `"time"` - `"count"` - `"both"` |
| **ssl-dh-bits**  string | Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.  **Choices:**   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl-hpkp**  string | Enable/disable including HPKP header in response.  **Choices:**   - `"disable"` - `"enable"` - `"report-only"` |
| **ssl-hpkp-age**  integer | Number of seconds the client should honour the HPKP setting. |
| **ssl-hpkp-backup**  string | Certificate to generate backup HPKP pin from. |
| **ssl-hpkp-include-subdomains**  string | Indicate that HPKP header applies to all subdomains.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-hpkp-primary**  string | Certificate to generate primary HPKP pin from. |
| **ssl-hpkp-report-uri**  string | URL to report HPKP violations to. |
| **ssl-hsts**  string | Enable/disable including HSTS header in response.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-hsts-age**  integer | Number of seconds the client should honour the HSTS setting. |
| **ssl-hsts-include-subdomains**  string | Indicate that HSTS header applies to all subdomains.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-http-location-conversion**  string | Enable to replace HTTP with HTTPS in the replys Location HTTP header field.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-http-match-host**  string | Enable/disable HTTP host matching for location conversion.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-max-version**  string | Highest SSL/TLS version acceptable from a client.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-min-version**  string | Lowest SSL/TLS version acceptable from a client.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-mode**  string | Apply SSL offloading between the client and the FortiGate  **Choices:**   - `"half"` - `"full"` |
| **ssl-pfs**  string | Select the cipher suites that can be used for SSL perfect forward secrecy  **Choices:**   - `"require"` - `"deny"` - `"allow"` |
| **ssl-send-empty-frags**  string | Enable/disable sending empty fragments to avoid CBC IV attacks  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server-algorithm**  string | Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.  **Choices:**   - `"high"` - `"low"` - `"medium"` - `"custom"` - `"client"` |
| **ssl-server-cipher-suites**  list / elements=dictionary | Ssl-Server-Cipher-Suites. |
| **cipher**  string | Cipher suite name.  **Choices:**   - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` |
| **priority**  integer | SSL/TLS cipher suites priority. |
| **versions**  list / elements=string | SSL/TLS versions that the cipher suite can be used with.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-server-max-version**  string | Highest SSL/TLS version acceptable from a server.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"client"` - `"tls-1.3"` |
| **ssl-server-min-version**  string | Lowest SSL/TLS version acceptable from a server.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"client"` - `"tls-1.3"` |
| **ssl-server-renegotiation**  string | Enable/disable secure renegotiation to comply with RFC 5746.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server-session-state-max**  integer | Maximum number of FortiGate to Server SSL session states to keep. |
| **ssl-server-session-state-timeout**  integer | Number of minutes to keep FortiGate to Server SSL session state. |
| **ssl-server-session-state-type**  string | How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate.  **Choices:**   - `"disable"` - `"time"` - `"count"` - `"both"` |
| **status**  string | Enable/disable VIP.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | Configure a static NAT, load balance, DNS translation, or FQDN VIP.  **Choices:**   - `"static-nat"` - `"load-balance"` - `"server-load-balance"` - `"dns-translation"` - `"fqdn"` - `"access-proxy"` |
| **uuid**  string | Universally Unique Identifier |
| **weblogic-server**  string | Enable to add an HTTP header to indicate SSL offloading for a WebLogic server.  **Choices:**   - `"disable"` - `"enable"` |
| **websphere-server**  string | Enable to add an HTTP header to indicate SSL offloading for a WebSphere server.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_vip_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_vip_module.md#id4)

```yaml+jinja
- name: gathering fortimanager facts
  hosts: fortimanager00
  gather_facts: no
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
   - name: retrieve all the virtual IPs for IPv4
     fmgr_fact:
       facts:
           selector: 'firewall_vip'
           params:
               adom: 'ansible'
               vip: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure virtual IP for IPv4.
     fmgr_firewall_vip:
        bypass_validation: True
        adom: ansible
        state: present
        firewall_vip:
           arp-reply: disable #<value in [disable, enable]>
           color: 1
           comment: 'ansible-comment'
           id: 1
           name: 'ansible-test-vip'
           protocol: tcp #<value in [tcp, udp, sctp, ...]>
           type: load-balance #<value in [static-nat, load-balance, server-load-balance, ...]>

- name: Demo of cloning objects in FortiManager
  hosts: fortimanager00
  connection: httpapi
  collections:
    - fortinet.fortimanager
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
    initial_vip_object: 'vip_object0'
    cloned_vip_objects:
        - name: 'vip_object1'
          comment: 'vip_object1 is cloned!'
        - name: 'vip_object2'
          comment: 'vip_object2 is cloned!'
  tasks:
    - name: Create An VIP object
      fmgr_firewall_vip:
        adom: 'root'
        state: 'present'
        firewall_vip:
            arp-reply: 'disable'
            comment: 'The VIP is created via Ansible'
            name: '{{ initial_vip_object }}'
            protocol: 'tcp'
            type: 'load-balance'
    - name: Clone an VIP object using fmgr_clone module.
      fmgr_clone:
        rc_succeeded: [-2]
        clone:
         selector: 'firewall_vip'
         self:
           adom: 'root'
           vip: '{{ initial_vip_object }}'
         target:
           name: '{{ item.name }}'
           comment: '{{ item.comment }}'
      with_items: '{{ cloned_vip_objects }}'
```

## [Return Values](fmgr_firewall_vip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
