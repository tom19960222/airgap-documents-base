---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_accessproxy6 module – Configure IPv6 access proxy."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_accessproxy6_module.html
fetched_at: 2026-07-28T02:11:09+00:00
---
# fortinet.fortimanager.fmgr_firewall_accessproxy6 module – Configure IPv6 access proxy.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_accessproxy6`.

New in fortinet.fortimanager 2.2.0

- [Synopsis](fmgr_firewall_accessproxy6_module.md#synopsis)
- [Parameters](fmgr_firewall_accessproxy6_module.md#parameters)
- [Notes](fmgr_firewall_accessproxy6_module.md#notes)
- [Examples](fmgr_firewall_accessproxy6_module.md#examples)
- [Return Values](fmgr_firewall_accessproxy6_module.md#return-values)

## [Synopsis](fmgr_firewall_accessproxy6_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_accessproxy6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_accessproxy6**  dictionary | the top level parameters set |
| **add-vhost-domain-to-dnsdb**  string | Enable/disable adding vhost/domain to dnsdb for ztna dox tunnel.  **Choices:**   - `"disable"` - `"enable"` |
| **api-gateway**  list / elements=dictionary | no description |
| **application**  any | (list) no description |
| **h2-support**  string | HTTP2 support, default=Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **h3-support**  string | HTTP3/QUIC support, default=Disable.  **Choices:**   - `"disable"` - `"enable"` |
| **http-cookie-age**  integer | Time in minutes that client web browsers should keep a cookie. |
| **http-cookie-domain**  string | Domain that HTTP cookie persistence should apply to. |
| **http-cookie-domain-from-host**  string | Enable/disable use of HTTP cookie domain from host field in HTTP.  **Choices:**   - `"disable"` - `"enable"` |
| **http-cookie-generation**  integer | Generation of HTTP cookie to be accepted. |
| **http-cookie-path**  string | Limit HTTP cookie persistence to the specified path. |
| **http-cookie-share**  string | Control sharing of cookies across API Gateway.  **Choices:**   - `"disable"` - `"same-ip"` |
| **https-cookie-secure**  string | Enable/disable verification that inserted HTTPS cookies are secure.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer | API Gateway ID. |
| **ldb-method**  string | Method used to distribute sessions to real servers.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"first-alive"` - `"http-host"` |
| **persistence**  string | Configure how to make sure that clients connect to the same server every time they make a request that is part of the s…  **Choices:**   - `"none"` - `"http-cookie"` |
| **quic**  dictionary | no description |
| **ack-delay-exponent**  integer | ACK delay exponent |
| **active-connection-id-limit**  integer | Active connection ID limit |
| **active-migration**  string | Enable/disable active migration  **Choices:**   - `"disable"` - `"enable"` |
| **grease-quic-bit**  string | Enable/disable grease QUIC bit  **Choices:**   - `"disable"` - `"enable"` |
| **max-ack-delay**  integer | Maximum ACK delay in milliseconds |
| **max-datagram-frame-size**  integer | Maximum datagram frame size in bytes |
| **max-idle-timeout**  integer | Maximum idle timeout milliseconds |
| **max-udp-payload-size**  integer | Maximum UDP payload size in bytes |
| **realservers**  list / elements=dictionary | no description |
| **addr-type**  string | Type of address.  **Choices:**   - `"fqdn"` - `"ip"` |
| **address**  string | Address or address group of the real server. |
| **domain**  string | Wildcard domain name of the real server. |
| **external-auth**  string | Enable/disable use of external browser as user-agent for SAML user authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **health-check**  string | Enable to check the responsiveness of the real server before forwarding traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **health-check-proto**  string | Protocol of the health check monitor to use when polling to determine servers connectivity status.  **Choices:**   - `"ping"` - `"http"` - `"tcp-connect"` |
| **holddown-interval**  string | Enable/disable holddown timer.  **Choices:**   - `"disable"` - `"enable"` |
| **http-host**  string | HTTP server domain name in HTTP header. |
| **id**  integer | Real server ID. |
| **ip**  string | IP address of the real server. |
| **mappedport**  any | (list or str) Port for communicating with the real server. |
| **port**  integer | Port for communicating with the real server. |
| **ssh-client-cert**  string | Set access-proxy SSH client certificate profile. |
| **ssh-host-key**  any | (list) no description |
| **ssh-host-key-validation**  string | Enable/disable SSH real server host key validation.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traf…  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **translate-host**  string | Enable/disable translation of hostname/IP from virtual server to real server.  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-encryption**  string | Tunnel encryption.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | TCP forwarding server type.  **Choices:**   - `"tcp-forwarding"` - `"ssh"` |
| **weight**  integer | Weight of the real server. |
| **saml-redirect**  string | Enable/disable SAML redirection after successful authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **saml-server**  string | SAML service provider configuration for VIP authentication. |
| **service**  string | Service.  **Choices:**   - `"http"` - `"https"` - `"tcp-forwarding"` - `"samlsp"` - `"web-portal"` - `"saas"` |
| **ssl-algorithm**  string | Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.  **Choices:**   - `"high"` - `"medium"` - `"low"` |
| **ssl-cipher-suites**  list / elements=dictionary | no description |
| **cipher**  string | Cipher suite name.  **Choices:**   - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` |
| **priority**  integer | SSL/TLS cipher suites priority. |
| **versions**  list / elements=string | no description  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-dh-bits**  string | Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.  **Choices:**   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl-max-version**  string | Highest SSL/TLS version acceptable from a server.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-min-version**  string | Lowest SSL/TLS version acceptable from a server.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-renegotiation**  string | Enable/disable secure renegotiation to comply with RFC 5746.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-vpn-web-portal**  string | SSL-VPN web portal. |
| **url-map**  string | URL pattern to match. |
| **url-map-type**  string | Type of url-map.  **Choices:**   - `"sub-string"` - `"wildcard"` - `"regex"` |
| **virtual-host**  string | Virtual host. |
| **api-gateway6**  list / elements=dictionary | no description |
| **application**  any | (list) no description |
| **h2-support**  string | HTTP2 support, default=Enable.  **Choices:**   - `"disable"` - `"enable"` |
| **h3-support**  string | HTTP3/QUIC support, default=Disable.  **Choices:**   - `"disable"` - `"enable"` |
| **http-cookie-age**  integer | Time in minutes that client web browsers should keep a cookie. |
| **http-cookie-domain**  string | Domain that HTTP cookie persistence should apply to. |
| **http-cookie-domain-from-host**  string | Enable/disable use of HTTP cookie domain from host field in HTTP.  **Choices:**   - `"disable"` - `"enable"` |
| **http-cookie-generation**  integer | Generation of HTTP cookie to be accepted. |
| **http-cookie-path**  string | Limit HTTP cookie persistence to the specified path. |
| **http-cookie-share**  string | Control sharing of cookies across API Gateway.  **Choices:**   - `"disable"` - `"same-ip"` |
| **https-cookie-secure**  string | Enable/disable verification that inserted HTTPS cookies are secure.  **Choices:**   - `"disable"` - `"enable"` |
| **id**  integer | API Gateway ID. |
| **ldb-method**  string | Method used to distribute sessions to real servers.  **Choices:**   - `"static"` - `"round-robin"` - `"weighted"` - `"first-alive"` - `"http-host"` |
| **persistence**  string | Configure how to make sure that clients connect to the same server every time they make a request that is part of the s…  **Choices:**   - `"none"` - `"http-cookie"` |
| **quic**  dictionary | no description |
| **ack-delay-exponent**  integer | ACK delay exponent |
| **active-connection-id-limit**  integer | Active connection ID limit |
| **active-migration**  string | Enable/disable active migration  **Choices:**   - `"disable"` - `"enable"` |
| **grease-quic-bit**  string | Enable/disable grease QUIC bit  **Choices:**   - `"disable"` - `"enable"` |
| **max-ack-delay**  integer | Maximum ACK delay in milliseconds |
| **max-datagram-frame-size**  integer | Maximum datagram frame size in bytes |
| **max-idle-timeout**  integer | Maximum idle timeout milliseconds |
| **max-udp-payload-size**  integer | Maximum UDP payload size in bytes |
| **realservers**  list / elements=dictionary | no description |
| **addr-type**  string | Type of address.  **Choices:**   - `"fqdn"` - `"ip"` |
| **address**  string | Address or address group of the real server. |
| **domain**  string | Wildcard domain name of the real server. |
| **external-auth**  string | Enable/disable use of external browser as user-agent for SAML user authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **health-check**  string | Enable to check the responsiveness of the real server before forwarding traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **health-check-proto**  string | Protocol of the health check monitor to use when polling to determine servers connectivity status.  **Choices:**   - `"ping"` - `"http"` - `"tcp-connect"` |
| **holddown-interval**  string | Enable/disable holddown timer.  **Choices:**   - `"disable"` - `"enable"` |
| **http-host**  string | HTTP server domain name in HTTP header. |
| **id**  integer | Real server ID. |
| **ip**  string | IPv6 address of the real server. |
| **mappedport**  any | (list or str) Port for communicating with the real server. |
| **port**  integer | Port for communicating with the real server. |
| **ssh-client-cert**  string | Set access-proxy SSH client certificate profile. |
| **ssh-host-key**  any | (list) no description |
| **ssh-host-key-validation**  string | Enable/disable SSH real server host key validation.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Set the status of the real server to active so that it can accept traffic, or on standby or disabled so no traf…  **Choices:**   - `"active"` - `"standby"` - `"disable"` |
| **translate-host**  string | Enable/disable translation of hostname/IP from virtual server to real server.  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-encryption**  string | Tunnel encryption.  **Choices:**   - `"disable"` - `"enable"` |
| **type**  string | TCP forwarding server type.  **Choices:**   - `"tcp-forwarding"` - `"ssh"` |
| **weight**  integer | Weight of the real server. |
| **saml-redirect**  string | Enable/disable SAML redirection after successful authentication.  **Choices:**   - `"disable"` - `"enable"` |
| **saml-server**  string | SAML service provider configuration for VIP authentication. |
| **service**  string | Service.  **Choices:**   - `"http"` - `"https"` - `"tcp-forwarding"` - `"samlsp"` - `"web-portal"` - `"saas"` |
| **ssl-algorithm**  string | Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.  **Choices:**   - `"high"` - `"medium"` - `"low"` |
| **ssl-cipher-suites**  list / elements=dictionary | no description |
| **cipher**  string | Cipher suite name.  **Choices:**   - `"TLS-RSA-WITH-RC4-128-MD5"` - `"TLS-RSA-WITH-RC4-128-SHA"` - `"TLS-RSA-WITH-DES-CBC-SHA"` - `"TLS-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-RSA-WITH-SEED-CBC-SHA"` - `"TLS-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-RSA-WITH-DES-CBC-SHA"` - `"TLS-DHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-RSA-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-SEED-CBC-SHA"` - `"TLS-DHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-RC4-128-SHA"` - `"TLS-ECDHE-RSA-WITH-3DES-EDE-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA"` - `"TLS-ECDHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-CHACHA20-POLY1305-SHA256"` - `"TLS-DHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-AES-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-128-GCM-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-RSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384"` - `"TLS-RSA-WITH-AES-128-GCM-SHA256"` - `"TLS-RSA-WITH-AES-256-GCM-SHA384"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA"` - `"TLS-DHE-DSS-WITH-CAMELLIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-CAMELLIA-256-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-SEED-CBC-SHA"` - `"TLS-DHE-DSS-WITH-ARIA-128-CBC-SHA256"` - `"TLS-DHE-DSS-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-RSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-RSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-128-CBC-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-ARIA-256-CBC-SHA384"` - `"TLS-DHE-DSS-WITH-3DES-EDE-CBC-SHA"` - `"TLS-DHE-DSS-WITH-DES-CBC-SHA"` - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-ECDHE-ECDSA-WITH-AES-256-CBC-SHA"` |
| **priority**  integer | SSL/TLS cipher suites priority. |
| **versions**  list / elements=string | no description  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-dh-bits**  string | Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.  **Choices:**   - `"768"` - `"1024"` - `"1536"` - `"2048"` - `"3072"` - `"4096"` |
| **ssl-max-version**  string | Highest SSL/TLS version acceptable from a server.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-min-version**  string | Lowest SSL/TLS version acceptable from a server.  **Choices:**   - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ssl-renegotiation**  string | Enable/disable secure renegotiation to comply with RFC 5746.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-vpn-web-portal**  string | SSL-VPN web portal. |
| **url-map**  string | URL pattern to match. |
| **url-map-type**  string | Type of url-map.  **Choices:**   - `"sub-string"` - `"wildcard"` - `"regex"` |
| **virtual-host**  string | Virtual host. |
| **auth-portal**  string | Enable/disable authentication portal.  **Choices:**   - `"disable"` - `"enable"` |
| **auth-virtual-host**  string | Virtual host for authentication portal. |
| **client-cert**  string | Enable/disable to request client certificate.  **Choices:**   - `"disable"` - `"enable"` |
| **decrypted-traffic-mirror**  string | Decrypted traffic mirror. |
| **empty-cert-action**  string | Action of an empty client certificate.  **Choices:**   - `"block"` - `"accept"` - `"accept-unmanageable"` |
| **http-supported-max-version**  string | Maximum supported HTTP versions.  **Choices:**   - `"http1"` - `"http2"` |
| **log-blocked-traffic**  string | Enable/disable logging of blocked traffic.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Access Proxy name. |
| **svr-pool-multiplex**  string | Enable/disable server pool multiplexing.  **Choices:**   - `"disable"` - `"enable"` |
| **svr-pool-server-max-concurrent-request**  integer | Maximum number of concurrent requests that servers in server pool could handle |
| **svr-pool-server-max-request**  integer | Maximum number of requests that servers in server pool handle before disconnecting |
| **svr-pool-ttl**  integer | Time-to-live in the server pool for idle connections to servers. |
| **user-agent-detect**  string | Enable/disable to detect device type by HTTP user-agent if no client certificate provided.  **Choices:**   - `"disable"` - `"enable"` |
| **vip**  string | Virtual IP name. |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_accessproxy6_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_accessproxy6_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: Configure IPv6 access proxy.
      fmgr_firewall_accessproxy6:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        adom: <your own value>
        state: <value in [present, absent]>
        firewall_accessproxy6:
          add-vhost-domain-to-dnsdb: <value in [disable, enable]>
          api-gateway:
            -
              application: <list or string>
              http-cookie-age: <integer>
              http-cookie-domain: <string>
              http-cookie-domain-from-host: <value in [disable, enable]>
              http-cookie-generation: <integer>
              http-cookie-path: <string>
              http-cookie-share: <value in [disable, same-ip]>
              https-cookie-secure: <value in [disable, enable]>
              id: <integer>
              ldb-method: <value in [static, round-robin, weighted, ...]>
              persistence: <value in [none, http-cookie]>
              realservers:
                -
                  addr-type: <value in [fqdn, ip]>
                  address: <string>
                  domain: <string>
                  health-check: <value in [disable, enable]>
                  health-check-proto: <value in [ping, http, tcp-connect]>
                  holddown-interval: <value in [disable, enable]>
                  http-host: <string>
                  id: <integer>
                  ip: <string>
                  mappedport: <list or string>
                  port: <integer>
                  ssh-client-cert: <string>
                  ssh-host-key: <list or string>
                  ssh-host-key-validation: <value in [disable, enable]>
                  status: <value in [active, standby, disable]>
                  type: <value in [tcp-forwarding, ssh]>
                  weight: <integer>
                  translate-host: <value in [disable, enable]>
                  external-auth: <value in [disable, enable]>
                  tunnel-encryption: <value in [disable, enable]>
              saml-redirect: <value in [disable, enable]>
              saml-server: <string>
              service: <value in [http, https, tcp-forwarding, ...]>
              ssl-algorithm: <value in [high, medium, low]>
              ssl-cipher-suites:
                -
                  cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                  priority: <integer>
                  versions:
                    - tls-1.0
                    - tls-1.1
                    - tls-1.2
                    - tls-1.3
              ssl-dh-bits: <value in [768, 1024, 1536, ...]>
              ssl-max-version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
              ssl-min-version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
              ssl-vpn-web-portal: <string>
              url-map: <string>
              url-map-type: <value in [sub-string, wildcard, regex]>
              virtual-host: <string>
              ssl-renegotiation: <value in [disable, enable]>
              h2-support: <value in [disable, enable]>
              h3-support: <value in [disable, enable]>
              quic:
                ack-delay-exponent: <integer>
                active-connection-id-limit: <integer>
                active-migration: <value in [disable, enable]>
                grease-quic-bit: <value in [disable, enable]>
                max-ack-delay: <integer>
                max-datagram-frame-size: <integer>
                max-idle-timeout: <integer>
                max-udp-payload-size: <integer>
          api-gateway6:
            -
              application: <list or string>
              http-cookie-age: <integer>
              http-cookie-domain: <string>
              http-cookie-domain-from-host: <value in [disable, enable]>
              http-cookie-generation: <integer>
              http-cookie-path: <string>
              http-cookie-share: <value in [disable, same-ip]>
              https-cookie-secure: <value in [disable, enable]>
              id: <integer>
              ldb-method: <value in [static, round-robin, weighted, ...]>
              persistence: <value in [none, http-cookie]>
              realservers:
                -
                  addr-type: <value in [fqdn, ip]>
                  address: <string>
                  domain: <string>
                  health-check: <value in [disable, enable]>
                  health-check-proto: <value in [ping, http, tcp-connect]>
                  holddown-interval: <value in [disable, enable]>
                  http-host: <string>
                  id: <integer>
                  ip: <string>
                  mappedport: <list or string>
                  port: <integer>
                  ssh-client-cert: <string>
                  ssh-host-key: <list or string>
                  ssh-host-key-validation: <value in [disable, enable]>
                  status: <value in [active, standby, disable]>
                  type: <value in [tcp-forwarding, ssh]>
                  weight: <integer>
                  translate-host: <value in [disable, enable]>
                  external-auth: <value in [disable, enable]>
                  tunnel-encryption: <value in [disable, enable]>
              saml-redirect: <value in [disable, enable]>
              saml-server: <string>
              service: <value in [http, https, tcp-forwarding, ...]>
              ssl-algorithm: <value in [high, medium, low]>
              ssl-cipher-suites:
                -
                  cipher: <value in [TLS-RSA-WITH-RC4-128-MD5, TLS-RSA-WITH-RC4-128-SHA, TLS-RSA-WITH-DES-CBC-SHA, ...]>
                  priority: <integer>
                  versions:
                    - tls-1.0
                    - tls-1.1
                    - tls-1.2
                    - tls-1.3
              ssl-dh-bits: <value in [768, 1024, 1536, ...]>
              ssl-max-version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
              ssl-min-version: <value in [tls-1.0, tls-1.1, tls-1.2, ...]>
              ssl-vpn-web-portal: <string>
              url-map: <string>
              url-map-type: <value in [sub-string, wildcard, regex]>
              virtual-host: <string>
              ssl-renegotiation: <value in [disable, enable]>
              h2-support: <value in [disable, enable]>
              h3-support: <value in [disable, enable]>
              quic:
                ack-delay-exponent: <integer>
                active-connection-id-limit: <integer>
                active-migration: <value in [disable, enable]>
                grease-quic-bit: <value in [disable, enable]>
                max-ack-delay: <integer>
                max-datagram-frame-size: <integer>
                max-idle-timeout: <integer>
                max-udp-payload-size: <integer>
          auth-portal: <value in [disable, enable]>
          auth-virtual-host: <string>
          client-cert: <value in [disable, enable]>
          decrypted-traffic-mirror: <string>
          empty-cert-action: <value in [block, accept, accept-unmanageable]>
          log-blocked-traffic: <value in [disable, enable]>
          name: <string>
          user-agent-detect: <value in [disable, enable]>
          vip: <string>
          http-supported-max-version: <value in [http1, http2]>
          svr-pool-multiplex: <value in [disable, enable]>
          svr-pool-server-max-request: <integer>
          svr-pool-ttl: <integer>
          svr-pool-server-max-concurrent-request: <integer>
```

## [Return Values](fmgr_firewall_accessproxy6_module.md#id5)

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
