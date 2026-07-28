---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_firewall_sslsshprofile module – Configure SSL/SSH protocol options."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_firewall_sslsshprofile_module.html
fetched_at: 2026-07-28T02:12:54+00:00
---
# fortinet.fortimanager.fmgr_firewall_sslsshprofile module – Configure SSL/SSH protocol options.

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
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_firewall_sslsshprofile`.

New in fortinet.fortimanager 1.0.0

- [Synopsis](fmgr_firewall_sslsshprofile_module.md#synopsis)
- [Parameters](fmgr_firewall_sslsshprofile_module.md#parameters)
- [Notes](fmgr_firewall_sslsshprofile_module.md#notes)
- [Examples](fmgr_firewall_sslsshprofile_module.md#examples)
- [Return Values](fmgr_firewall_sslsshprofile_module.md#return-values)

## [Synopsis](fmgr_firewall_sslsshprofile_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_firewall_sslsshprofile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **adom**  string / required | the parameter (adom) in requested url |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_sslsshprofile**  dictionary | the top level parameters set |
| **allowlist**  string | Enable/disable exempting servers by FortiGuard allowlist.  **Choices:**   - `"disable"` - `"enable"` |
| **block-blacklisted-certificates**  string | Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blacklist.  **Choices:**   - `"disable"` - `"enable"` |
| **block-blocklisted-certificates**  string | Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blocklist.  **Choices:**   - `"disable"` - `"enable"` |
| **caname**  string | CA certificate used by SSL Inspection. |
| **certname**  string | Certificate containing the key to use when re-signing server certificates for SSL inspection. |
| **comment**  string | Optional comments. |
| **dot**  dictionary | no description |
| **cert-validation-failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client-certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **min-allowed-ssl-version**  string | no description  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **quic**  string | Enable/disable QUIC inspection  **Choices:**   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"enable"` - `"strict"` - `"disable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl-cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"block"` - `"allow"` |
| **unsupported-ssl-negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"block"` - `"allow"` |
| **unsupported-ssl-version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-server-cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **ftps**  dictionary | no description |
| **allow-invalid-server-cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"disable"` - `"enable"` |
| **cert-validation-failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client-cert-request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client-certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid-server-cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min-allowed-ssl-version**  string | Minimum SSL version to be allowed.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  any | (list) Ports to use for scanning |
| **revoked-server-cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported-ssl-cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted-server-cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **https**  dictionary | no description |
| **allow-invalid-server-cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"disable"` - `"enable"` |
| **cert-probe-failure**  string | Action based on certificate probe failure.  **Choices:**   - `"block"` - `"allow"` |
| **cert-validation-failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client-cert-request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client-certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid-server-cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min-allowed-ssl-version**  string | Minimum SSL version to be allowed.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  any | (list) Ports to use for scanning |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **quic**  string | Enable/disable QUIC inspection  **Choices:**   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **unsupported-ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported-ssl-cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted-server-cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **imaps**  dictionary | no description |
| **allow-invalid-server-cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"disable"` - `"enable"` |
| **cert-validation-failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client-cert-request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client-certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid-server-cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min-allowed-ssl-version**  string | no description  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  any | (list) Ports to use for scanning |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported-ssl-cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted-server-cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **mapi-over-https**  string | Enable/disable inspection of MAPI over HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **name**  string / required | Name. |
| **pop3s**  dictionary | no description |
| **allow-invalid-server-cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"disable"` - `"enable"` |
| **cert-validation-failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client-cert-request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client-certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid-server-cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min-allowed-ssl-version**  string | no description  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  any | (list) Ports to use for scanning |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported-ssl-cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted-server-cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **rpc-over-https**  string | Enable/disable inspection of RPC over HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **server-cert**  any | (list or str) Certificate used by SSL Inspection to replace server certificate. |
| **server-cert-mode**  string | Re-sign or replace the servers certificate.  **Choices:**   - `"re-sign"` - `"replace"` |
| **smtps**  dictionary | no description |
| **allow-invalid-server-cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"disable"` - `"enable"` |
| **cert-validation-failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client-cert-request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client-certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid-server-cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min-allowed-ssl-version**  string | no description  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  any | (list) Ports to use for scanning |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **revoked-server-cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"disable"` - `"enable"` - `"strict"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported-ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported-ssl-cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted-server-cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **ssh**  dictionary | no description |
| **block**  list / elements=string | no description  **Choices:**   - `"x11-filter"` - `"ssh-shell"` - `"exec"` - `"port-forward"` |
| **inspect-all**  string | Level of SSL inspection.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **log**  list / elements=string | no description  **Choices:**   - `"x11-filter"` - `"ssh-shell"` - `"exec"` - `"port-forward"` |
| **ports**  any | (list) Ports to use for scanning |
| **proxy-after-tcp-handshake**  string | Proxy traffic after the TCP 3-way handshake has been established  **Choices:**   - `"disable"` - `"enable"` |
| **ssh-algorithm**  string | Relative strength of encryption algorithms accepted during negotiation.  **Choices:**   - `"compatible"` - `"high-encryption"` |
| **ssh-policy-check**  string | Enable/disable SSH policy check.  **Choices:**   - `"disable"` - `"enable"` |
| **ssh-tun-policy-check**  string | Enable/disable SSH tunnel policy check.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported-version**  string | Action based on SSH version being unsupported.  **Choices:**   - `"block"` - `"bypass"` |
| **ssl**  dictionary | no description |
| **allow-invalid-server-cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"disable"` - `"enable"` |
| **cert-probe-failure**  string | Action based on certificate probe failure.  **Choices:**   - `"block"` - `"allow"` |
| **cert-validation-failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert-validation-timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client-cert-request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client-certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired-server-cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **inspect-all**  string | Level of SSL inspection.  **Choices:**   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **invalid-server-cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min-allowed-ssl-version**  string | Minimum SSL version to be allowed.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **revoked-server-cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni-server-cert-check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"disable"` - `"enable"` - `"strict"` |
| **unsupported-ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported-ssl-cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported-ssl-version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"block"` - `"allow"` - `"inspect"` |
| **untrusted-cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted-server-cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **ssl-anomalies-log**  string | Enable/disable logging SSL anomalies.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-anomaly-log**  string | Enable/disable logging of SSL anomalies.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-exempt**  list / elements=dictionary | Ssl-Exempt. |
| **address**  string | IPv4 address object. |
| **address6**  string | IPv6 address object. |
| **fortiguard-category**  string | FortiGuard category ID. |
| **id**  integer | ID number. |
| **regex**  string | Exempt servers by regular expression. |
| **type**  string | Type of address object  **Choices:**   - `"fortiguard-category"` - `"address"` - `"address6"` - `"wildcard-fqdn"` - `"regex"` - `"finger-print"` |
| **wildcard-fqdn**  string | Exempt servers by wildcard FQDN. |
| **ssl-exemption-ip-rating**  string | Enable/disable IP based URL rating.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-exemption-log**  string | Enable/disable logging SSL exemptions.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-exemptions-log**  string | Enable/disable logging SSL exemptions.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-handshake-log**  string | Enable/disable logging of TLS handshakes.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-invalid-server-cert-log**  string | Enable/disable SSL server certificate validation logging.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-negotiation-log**  string | Enable/disable logging SSL negotiation.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl-server**  list / elements=dictionary | Ssl-Server. |
| **ftps-client-cert-request**  string | Action based on client certificate request during the FTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ftps-client-certificate**  string | Action based on received client certificate during the FTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **https-client-cert-request**  string | Action based on client certificate request during the HTTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **https-client-certificate**  string | Action based on received client certificate during the HTTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **id**  integer | SSL server ID. |
| **imaps-client-cert-request**  string | Action based on client certificate request during the IMAPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **imaps-client-certificate**  string | Action based on received client certificate during the IMAPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ip**  string | IPv4 address of the SSL server. |
| **pop3s-client-cert-request**  string | Action based on client certificate request during the POP3S handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **pop3s-client-certificate**  string | Action based on received client certificate during the POP3S handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **smtps-client-cert-request**  string | Action based on client certificate request during the SMTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **smtps-client-certificate**  string | Action based on received client certificate during the SMTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl-other-client-cert-request**  string | Action based on client certificate request during an SSL protocol handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl-other-client-certificate**  string | Action based on received client certificate during an SSL protocol handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl-server-cert-log**  string | Enable/disable logging of server certificate information.  **Choices:**   - `"disable"` - `"enable"` |
| **supported-alpn**  string | Configure ALPN option.  **Choices:**   - `"none"` - `"http1-1"` - `"http2"` - `"all"` |
| **untrusted-caname**  string | Untrusted CA certificate used by SSL Inspection. |
| **use-ssl-server**  string | Enable/disable the use of SSL server table for SSL offloading.  **Choices:**   - `"disable"` - `"enable"` |
| **whitelist**  string | Enable/disable exempting servers by FortiGuard whitelist.  **Choices:**   - `"disable"` - `"enable"` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **state**  string / required | The directive to create, update or delete an object.  **Choices:**   - `"present"` - `"absent"` |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_firewall_sslsshprofile_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_firewall_sslsshprofile_module.md#id4)

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
   - name: retrieve all the SSL/SSH protocol options
     fmgr_fact:
       facts:
           selector: 'firewall_sslsshprofile'
           params:
               adom: 'ansible'
               ssl-ssh-profile: 'your_value'
- hosts: fortimanager00
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
     ansible_httpapi_use_ssl: True
     ansible_httpapi_validate_certs: False
     ansible_httpapi_port: 443
  tasks:
   - name: Configure SSL/SSH protocol options.
     fmgr_firewall_sslsshprofile:
        bypass_validation: False
        adom: ansible
        state: present
        firewall_sslsshprofile:
           comment: 'ansible-comment1'
           mapi-over-https: disable #<value in [disable, enable]>
           name: 'ansible-test'
           use-ssl-server: disable #<value in [disable, enable]>
           whitelist: enable #<value in [disable, enable]>
```

## [Return Values](fmgr_firewall_sslsshprofile_module.md#id5)

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
