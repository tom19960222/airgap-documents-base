---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_vpn_ssl_settings module – Configure SSL VPN."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_vpn_ssl_settings_module.html
fetched_at: 2026-07-28T02:21:41+00:00
---
# fortinet.fortimanager.fmgr_vpn_ssl_settings module – Configure SSL VPN.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_vpn_ssl_settings`.

New in fortinet.fortimanager 2.1.0

- [Synopsis](fmgr_vpn_ssl_settings_module.md#synopsis)
- [Parameters](fmgr_vpn_ssl_settings_module.md#parameters)
- [Notes](fmgr_vpn_ssl_settings_module.md#notes)
- [Examples](fmgr_vpn_ssl_settings_module.md#examples)
- [Return Values](fmgr_vpn_ssl_settings_module.md#return-values)

## [Synopsis](fmgr_vpn_ssl_settings_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_vpn_ssl_settings_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **device**  string / required | the parameter (device) in requested url |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **vdom**  string / required | the parameter (vdom) in requested url |
| **vpn_ssl_settings**  dictionary | the top level parameters set |
| **algorithm**  string | Force the SSL VPN security level.  **Choices:**   - `"default"` - `"high"` - `"low"` - `"medium"` |
| **auth-session-check-source-ip**  string | Enable/disable checking of source IP for authentication session.  **Choices:**   - `"disable"` - `"enable"` |
| **auth-timeout**  integer | SSL VPN authentication timeout |
| **authentication-rule**  list / elements=dictionary | no description |
| **auth**  string | SSL VPN authentication method restriction.  **Choices:**   - `"any"` - `"local"` - `"radius"` - `"ldap"` - `"tacacs+"` - `"peer"` |
| **cipher**  string | SSL VPN cipher strength.  **Choices:**   - `"any"` - `"high"` - `"medium"` |
| **client-cert**  string | Enable/disable SSL VPN client certificate restrictive.  **Choices:**   - `"disable"` - `"enable"` |
| **groups**  any | (list or str) User groups. |
| **id**  integer | ID |
| **portal**  string | SSL VPN portal. |
| **realm**  string | SSL VPN realm. |
| **source-address**  any | (list or str) Source address of incoming traffic. |
| **source-address-negate**  string | Enable/disable negated source address match.  **Choices:**   - `"disable"` - `"enable"` |
| **source-address6**  any | (list or str) IPv6 source address of incoming traffic. |
| **source-address6-negate**  string | Enable/disable negated source IPv6 address match.  **Choices:**   - `"disable"` - `"enable"` |
| **source-interface**  any | (list or str) SSL VPN source interface of incoming traffic. |
| **user-peer**  string | Name of user peer. |
| **users**  any | (list or str) User name. |
| **auto-tunnel-static-route**  string | Enable/disable to auto-create static routes for the SSL VPN tunnel IP addresses.  **Choices:**   - `"disable"` - `"enable"` |
| **banned-cipher**  list / elements=string | no description  **Choices:**   - `"RSA"` - `"DH"` - `"DHE"` - `"ECDH"` - `"ECDHE"` - `"DSS"` - `"ECDSA"` - `"AES"` - `"AESGCM"` - `"CAMELLIA"` - `"3DES"` - `"SHA1"` - `"SHA256"` - `"SHA384"` - `"STATIC"` - `"CHACHA20"` - `"ARIA"` - `"AESCCM"` |
| **browser-language-detection**  string | Enable/disable overriding the configured system language based on the preferred language of the browser.  **Choices:**   - `"disable"` - `"enable"` |
| **check-referer**  string | Enable/disable verification of referer field in HTTP request header.  **Choices:**   - `"disable"` - `"enable"` |
| **ciphersuite**  list / elements=string | no description  **Choices:**   - `"TLS-AES-128-GCM-SHA256"` - `"TLS-AES-256-GCM-SHA384"` - `"TLS-CHACHA20-POLY1305-SHA256"` - `"TLS-AES-128-CCM-SHA256"` - `"TLS-AES-128-CCM-8-SHA256"` |
| **client-sigalgs**  string | Set signature algorithms related to client authentication.  **Choices:**   - `"no-rsa-pss"` - `"all"` |
| **default-portal**  string | Default SSL VPN portal. |
| **deflate-compression-level**  integer | Compression level |
| **deflate-min-data-size**  integer | Minimum amount of data that triggers compression |
| **dns-server1**  string | DNS server 1. |
| **dns-server2**  string | DNS server 2. |
| **dns-suffix**  string | DNS suffix used for SSL VPN clients. |
| **dtls-heartbeat-fail-count**  integer | Number of missing heartbeats before the connection is considered dropped. |
| **dtls-heartbeat-idle-timeout**  integer | Idle timeout before DTLS heartbeat is sent. |
| **dtls-heartbeat-interval**  integer | Interval between DTLS heartbeat. |
| **dtls-hello-timeout**  integer | SSLVPN maximum DTLS hello timeout |
| **dtls-max-proto-ver**  string | DTLS maximum protocol version.  **Choices:**   - `"dtls1-0"` - `"dtls1-2"` |
| **dtls-min-proto-ver**  string | DTLS minimum protocol version.  **Choices:**   - `"dtls1-0"` - `"dtls1-2"` |
| **dtls-tunnel**  string | Enable/disable DTLS to prevent eavesdropping, tampering, or message forgery.  **Choices:**   - `"disable"` - `"enable"` |
| **dual-stack-mode**  string | Tunnel mode  **Choices:**   - `"disable"` - `"enable"` |
| **encode-2f-sequence**  string | Encode 2F sequence to forward slash in URLs.  **Choices:**   - `"disable"` - `"enable"` |
| **encrypt-and-store-password**  string | Encrypt and store user passwords for SSL VPN web sessions.  **Choices:**   - `"disable"` - `"enable"` |
| **force-two-factor-auth**  string | Enable/disable only PKI users with two-factor authentication for SSL VPNs.  **Choices:**   - `"disable"` - `"enable"` |
| **header-x-forwarded-for**  string | Forward the same, add, or remove HTTP header.  **Choices:**   - `"pass"` - `"add"` - `"remove"` |
| **hsts-include-subdomains**  string | Add HSTS includeSubDomains response header.  **Choices:**   - `"disable"` - `"enable"` |
| **http-compression**  string | Enable/disable to allow HTTP compression over SSL VPN tunnels.  **Choices:**   - `"disable"` - `"enable"` |
| **http-only-cookie**  string | Enable/disable SSL VPN support for HttpOnly cookies.  **Choices:**   - `"disable"` - `"enable"` |
| **http-request-body-timeout**  integer | SSL VPN session is disconnected if an HTTP request body is not received within this time |
| **http-request-header-timeout**  integer | SSL VPN session is disconnected if an HTTP request header is not received within this time |
| **https-redirect**  string | Enable/disable redirect of port 80 to SSL VPN port.  **Choices:**   - `"disable"` - `"enable"` |
| **idle-timeout**  integer | SSL VPN disconnects if idle for specified time in seconds. |
| **ipv6-dns-server1**  string | IPv6 DNS server 1. |
| **ipv6-dns-server2**  string | IPv6 DNS server 2. |
| **ipv6-wins-server1**  string | IPv6 WINS server 1. |
| **ipv6-wins-server2**  string | IPv6 WINS server 2. |
| **login-attempt-limit**  integer | SSL VPN maximum login attempt times before block |
| **login-block-time**  integer | Time for which a user is blocked from logging in after too many failed login attempts |
| **login-timeout**  integer | SSLVPN maximum login timeout |
| **port**  integer | SSL VPN access port |
| **port-precedence**  string | Enable/disable, Enable means that if SSL VPN connections are allowed on an interface admin GUI connections are blocked on that …  **Choices:**   - `"disable"` - `"enable"` |
| **reqclientcert**  string | Enable/disable to require client certificates for all SSL VPN users.  **Choices:**   - `"disable"` - `"enable"` |
| **route-source-interface**  string | Enable/disable to allow SSL VPN sessions to bypass routing and bind to the incoming interface.  **Choices:**   - `"disable"` - `"enable"` |
| **saml-redirect-port**  integer | SAML local redirect port in the machine running FortiClient |
| **server-hostname**  string | Server hostname for HTTPS. |
| **servercert**  string | Name of the server certificate to be used for SSL VPNs. |
| **source-address**  any | (list or str) Source address of incoming traffic. |
| **source-address-negate**  string | Enable/disable negated source address match.  **Choices:**   - `"disable"` - `"enable"` |
| **source-address6**  any | (list or str) IPv6 source address of incoming traffic. |
| **source-address6-negate**  string | Enable/disable negated source IPv6 address match.  **Choices:**   - `"disable"` - `"enable"` |
| **source-interface**  any | (list or str) SSL VPN source interface of incoming traffic. |
| **ssl-big-buffer**  string | Disable using the big SSLv3 buffer feature to save memory and force higher security.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-client-renegotiation**  string | Enable/disable to allow client renegotiation by the server if the tunnel goes down.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-insert-empty-fragment**  string | Enable/disable insertion of empty fragment.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-max-proto-ver**  string | SSL maximum protocol version.  **Choices:**   - `"tls1-0"` - `"tls1-1"` - `"tls1-2"` - `"tls1-3"` |
| **ssl-min-proto-ver**  string | SSL minimum protocol version.  **Choices:**   - `"tls1-0"` - `"tls1-1"` - `"tls1-2"` - `"tls1-3"` |
| **sslv3**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Enable/disable SSL-VPN.  **Choices:**   - `"disable"` - `"enable"` |
| **tlsv1-0**  string | Enable/disable TLSv1.  **Choices:**   - `"disable"` - `"enable"` |
| **tlsv1-1**  string | Enable/disable TLSv1.  **Choices:**   - `"disable"` - `"enable"` |
| **tlsv1-2**  string | Enable/disable TLSv1.  **Choices:**   - `"disable"` - `"enable"` |
| **tlsv1-3**  string | no description  **Choices:**   - `"disable"` - `"enable"` |
| **transform-backward-slashes**  string | Transform backward slashes to forward slashes in URLs.  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-addr-assigned-method**  string | Method used for assigning address for tunnel.  **Choices:**   - `"first-available"` - `"round-robin"` |
| **tunnel-connect-without-reauth**  string | Enable/disable tunnel connection without re-authorization if previous connection dropped.  **Choices:**   - `"disable"` - `"enable"` |
| **tunnel-ip-pools**  any | (list or str) Names of the IPv4 IP Pool firewall objects that define the IP addresses reserved for remote clients. |
| **tunnel-ipv6-pools**  any | (list or str) Names of the IPv6 IP Pool firewall objects that define the IP addresses reserved for remote clients. |
| **tunnel-user-session-timeout**  integer | Time out value to clean up user session after tunnel connection is dropped |
| **unsafe-legacy-renegotiation**  string | Enable/disable unsafe legacy re-negotiation.  **Choices:**   - `"disable"` - `"enable"` |
| **url-obscuration**  string | Enable/disable to obscure the host name of the URL of the web browser display.  **Choices:**   - `"disable"` - `"enable"` |
| **user-peer**  string | Name of user peer. |
| **web-mode-snat**  string | Enable/disable use of IP pools defined in firewall policy while using web-mode.  **Choices:**   - `"disable"` - `"enable"` |
| **wins-server1**  string | WINS server 1. |
| **wins-server2**  string | WINS server 2. |
| **x-content-type-options**  string | Add HTTP X-Content-Type-Options header.  **Choices:**   - `"disable"` - `"enable"` |
| **ztna-trusted-client**  string | Enable/disable verification of device certificate for SSLVPN ZTNA session.  **Choices:**   - `"disable"` - `"enable"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_vpn_ssl_settings_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_vpn_ssl_settings_module.md#id4)

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
    - name: Configure SSL VPN.
      fmgr_vpn_ssl_settings:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        device: <your own value>
        vdom: <your own value>
        vpn_ssl_settings:
          algorithm: <value in [default, high, low, ...]>
          auth-session-check-source-ip: <value in [disable, enable]>
          auth-timeout: <integer>
          authentication-rule:
            -
              auth: <value in [any, local, radius, ...]>
              cipher: <value in [any, high, medium]>
              client-cert: <value in [disable, enable]>
              groups: <list or string>
              id: <integer>
              portal: <string>
              realm: <string>
              source-address: <list or string>
              source-address-negate: <value in [disable, enable]>
              source-address6: <list or string>
              source-address6-negate: <value in [disable, enable]>
              source-interface: <list or string>
              user-peer: <string>
              users: <list or string>
          auto-tunnel-static-route: <value in [disable, enable]>
          banned-cipher:
            - RSA
            - DH
            - DHE
            - ECDH
            - ECDHE
            - DSS
            - ECDSA
            - AES
            - AESGCM
            - CAMELLIA
            - 3DES
            - SHA1
            - SHA256
            - SHA384
            - STATIC
            - CHACHA20
            - ARIA
            - AESCCM
          check-referer: <value in [disable, enable]>
          default-portal: <string>
          deflate-compression-level: <integer>
          deflate-min-data-size: <integer>
          dns-server1: <string>
          dns-server2: <string>
          dns-suffix: <string>
          dtls-hello-timeout: <integer>
          dtls-max-proto-ver: <value in [dtls1-0, dtls1-2]>
          dtls-min-proto-ver: <value in [dtls1-0, dtls1-2]>
          dtls-tunnel: <value in [disable, enable]>
          encode-2f-sequence: <value in [disable, enable]>
          encrypt-and-store-password: <value in [disable, enable]>
          force-two-factor-auth: <value in [disable, enable]>
          header-x-forwarded-for: <value in [pass, add, remove]>
          hsts-include-subdomains: <value in [disable, enable]>
          http-compression: <value in [disable, enable]>
          http-only-cookie: <value in [disable, enable]>
          http-request-body-timeout: <integer>
          http-request-header-timeout: <integer>
          https-redirect: <value in [disable, enable]>
          idle-timeout: <integer>
          ipv6-dns-server1: <string>
          ipv6-dns-server2: <string>
          ipv6-wins-server1: <string>
          ipv6-wins-server2: <string>
          login-attempt-limit: <integer>
          login-block-time: <integer>
          login-timeout: <integer>
          port: <integer>
          port-precedence: <value in [disable, enable]>
          reqclientcert: <value in [disable, enable]>
          route-source-interface: <value in [disable, enable]>
          servercert: <string>
          source-address: <list or string>
          source-address-negate: <value in [disable, enable]>
          source-address6: <list or string>
          source-address6-negate: <value in [disable, enable]>
          source-interface: <list or string>
          ssl-client-renegotiation: <value in [disable, enable]>
          ssl-insert-empty-fragment: <value in [disable, enable]>
          ssl-max-proto-ver: <value in [tls1-0, tls1-1, tls1-2, ...]>
          ssl-min-proto-ver: <value in [tls1-0, tls1-1, tls1-2, ...]>
          tlsv1-0: <value in [disable, enable]>
          tlsv1-1: <value in [disable, enable]>
          tlsv1-2: <value in [disable, enable]>
          tlsv1-3: <value in [disable, enable]>
          transform-backward-slashes: <value in [disable, enable]>
          tunnel-connect-without-reauth: <value in [disable, enable]>
          tunnel-ip-pools: <list or string>
          tunnel-ipv6-pools: <list or string>
          tunnel-user-session-timeout: <integer>
          unsafe-legacy-renegotiation: <value in [disable, enable]>
          url-obscuration: <value in [disable, enable]>
          user-peer: <string>
          wins-server1: <string>
          wins-server2: <string>
          x-content-type-options: <value in [disable, enable]>
          sslv3: <value in [disable, enable]>
          ssl-big-buffer: <value in [disable, enable]>
          client-sigalgs: <value in [no-rsa-pss, all]>
          ciphersuite:
            - TLS-AES-128-GCM-SHA256
            - TLS-AES-256-GCM-SHA384
            - TLS-CHACHA20-POLY1305-SHA256
            - TLS-AES-128-CCM-SHA256
            - TLS-AES-128-CCM-8-SHA256
          dual-stack-mode: <value in [disable, enable]>
          tunnel-addr-assigned-method: <value in [first-available, round-robin]>
          browser-language-detection: <value in [disable, enable]>
          saml-redirect-port: <integer>
          status: <value in [disable, enable]>
          web-mode-snat: <value in [disable, enable]>
          ztna-trusted-client: <value in [disable, enable]>
          dtls-heartbeat-fail-count: <integer>
          dtls-heartbeat-idle-timeout: <integer>
          dtls-heartbeat-interval: <integer>
          server-hostname: <string>
```

## [Return Values](fmgr_vpn_ssl_settings_module.md#id5)

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
