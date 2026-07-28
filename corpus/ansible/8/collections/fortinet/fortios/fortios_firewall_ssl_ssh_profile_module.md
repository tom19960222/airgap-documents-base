---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_firewall_ssl_ssh_profile module – Configure SSL/SSH protocol options in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_firewall_ssl_ssh_profile_module.html
fetched_at: 2026-07-28T02:25:15+00:00
---
# fortinet.fortios.fortios_firewall_ssl_ssh_profile module – Configure SSL/SSH protocol options in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_firewall_ssl_ssh_profile_module.md#ansible-collections-fortinet-fortios-fortios-firewall-ssl-ssh-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_firewall_ssl_ssh_profile`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_firewall_ssl_ssh_profile_module.md#synopsis)
- [Requirements](fortios_firewall_ssl_ssh_profile_module.md#requirements)
- [Parameters](fortios_firewall_ssl_ssh_profile_module.md#parameters)
- [Notes](fortios_firewall_ssl_ssh_profile_module.md#notes)
- [Examples](fortios_firewall_ssl_ssh_profile_module.md#examples)
- [Return Values](fortios_firewall_ssl_ssh_profile_module.md#return-values)

## [Synopsis](fortios_firewall_ssl_ssh_profile_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify firewall feature and ssl_ssh_profile category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_firewall_ssl_ssh_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_firewall_ssl_ssh_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **firewall_ssl_ssh_profile**  dictionary | Configure SSL/SSH protocol options. |
| **allowlist**  string | Enable/disable exempting servers by FortiGuard allowlist.  **Choices:**   - `"enable"` - `"disable"` |
| **block_blacklisted_certificates**  string | Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blacklist.  **Choices:**   - `"disable"` - `"enable"` |
| **block_blocklisted_certificates**  string | Enable/disable blocking SSL-based botnet communication by FortiGuard certificate blocklist.  **Choices:**   - `"disable"` - `"enable"` |
| **caname**  string | CA certificate used by SSL Inspection. Source vpn.certificate.local.name. |
| **comment**  string | Optional comments. |
| **dot**  dictionary | Configure DNS over TLS options. |
| **cert_validation_failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert_validation_timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client_certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired_server_cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  **Choices:**   - `"enable"` - `"disable"` |
| **quic**  string | Enable/disable QUIC inspection .  **Choices:**   - `"disable"` - `"enable"` |
| **revoked_server_cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni_server_cert_check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"enable"` - `"strict"` - `"disable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported_ssl_cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"allow"` - `"block"` - `"inspect"` |
| **untrusted_server_cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **ftps**  dictionary | Configure FTPS options. |
| **allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"enable"` - `"disable"` |
| **cert_validation_failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert_validation_timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client_cert_request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client_certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired_server_cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid_server_cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min_allowed_ssl_version**  string | Minimum SSL version to be allowed.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  list / elements=integer | Ports to use for scanning (1 - 65535). |
| **revoked_server_cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni_server_cert_check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"enable"` - `"strict"` - `"disable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported_ssl_cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"allow"` - `"block"` - `"inspect"` |
| **untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted_server_cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **https**  dictionary | Configure HTTPS options. |
| **allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"enable"` - `"disable"` |
| **cert_probe_failure**  string | Action based on certificate probe failure.  **Choices:**   - `"allow"` - `"block"` |
| **cert_validation_failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert_validation_timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client_cert_request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client_certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired_server_cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid_server_cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min_allowed_ssl_version**  string | Minimum SSL version to be allowed.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **ports**  list / elements=integer | Ports to use for scanning (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  **Choices:**   - `"enable"` - `"disable"` |
| **quic**  string | Enable/disable QUIC inspection .  **Choices:**   - `"disable"` - `"enable"` |
| **revoked_server_cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni_server_cert_check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"enable"` - `"strict"` - `"disable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported_ssl_cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"allow"` - `"block"` - `"inspect"` |
| **untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted_server_cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **imaps**  dictionary | Configure IMAPS options. |
| **allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"enable"` - `"disable"` |
| **cert_validation_failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert_validation_timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client_cert_request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client_certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired_server_cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid_server_cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **ports**  list / elements=integer | Ports to use for scanning (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  **Choices:**   - `"enable"` - `"disable"` |
| **revoked_server_cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni_server_cert_check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"enable"` - `"strict"` - `"disable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported_ssl_cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"allow"` - `"block"` - `"inspect"` |
| **untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted_server_cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **mapi_over_https**  string | Enable/disable inspection of MAPI over HTTPS.  **Choices:**   - `"enable"` - `"disable"` |
| **name**  string / required | Name. |
| **pop3s**  dictionary | Configure POP3S options. |
| **allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"enable"` - `"disable"` |
| **cert_validation_failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert_validation_timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client_cert_request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client_certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired_server_cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid_server_cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **ports**  list / elements=integer | Ports to use for scanning (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  **Choices:**   - `"enable"` - `"disable"` |
| **revoked_server_cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni_server_cert_check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"enable"` - `"strict"` - `"disable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported_ssl_cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"allow"` - `"block"` - `"inspect"` |
| **untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted_server_cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **rpc_over_https**  string | Enable/disable inspection of RPC over HTTPS.  **Choices:**   - `"enable"` - `"disable"` |
| **server_cert**  list / elements=dictionary | Certificate used by SSL Inspection to replace server certificate. Source vpn.certificate.local.name. |
| **name**  string / required | Certificate list. Source vpn.certificate.local.name. |
| **server_cert_mode**  string | Re-sign or replace the server”s certificate.  **Choices:**   - `"re-sign"` - `"replace"` |
| **smtps**  dictionary | Configure SMTPS options. |
| **allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"enable"` - `"disable"` |
| **cert_validation_failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert_validation_timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client_cert_request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client_certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired_server_cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **invalid_server_cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **ports**  list / elements=integer | Ports to use for scanning (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  **Choices:**   - `"enable"` - `"disable"` |
| **revoked_server_cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni_server_cert_check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"enable"` - `"strict"` - `"disable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported_ssl_cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"allow"` - `"block"` - `"inspect"` |
| **untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted_server_cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **ssh**  dictionary | Configure SSH options. |
| **inspect_all**  string | Level of SSL inspection.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **ports**  list / elements=integer | Ports to use for scanning (1 - 65535). |
| **proxy_after_tcp_handshake**  string | Proxy traffic after the TCP 3-way handshake has been established (not before).  **Choices:**   - `"enable"` - `"disable"` |
| **ssh_algorithm**  string | Relative strength of encryption algorithms accepted during negotiation.  **Choices:**   - `"compatible"` - `"high-encryption"` |
| **ssh_policy_check**  string | Enable/disable SSH policy check.  **Choices:**   - `"disable"` - `"enable"` |
| **ssh_tun_policy_check**  string | Enable/disable SSH tunnel policy check.  **Choices:**   - `"disable"` - `"enable"` |
| **status**  string | Configure protocol inspection status.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **unsupported_version**  string | Action based on SSH version being unsupported.  **Choices:**   - `"bypass"` - `"block"` |
| **ssl**  dictionary | Configure SSL options. |
| **allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  **Choices:**   - `"enable"` - `"disable"` |
| **cert_probe_failure**  string | Action based on certificate probe failure.  **Choices:**   - `"allow"` - `"block"` |
| **cert_validation_failure**  string | Action based on certificate validation failure.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **cert_validation_timeout**  string | Action based on certificate validation timeout.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **client_cert_request**  string | Action based on client certificate request.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **client_certificate**  string | Action based on received client certificate.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **expired_server_cert**  string | Action based on server certificate is expired.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **inspect_all**  string | Level of SSL inspection.  **Choices:**   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **invalid_server_cert**  string | Allow or block the invalid SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` |
| **min_allowed_ssl_version**  string | Minimum SSL version to be allowed.  **Choices:**   - `"ssl-3.0"` - `"tls-1.0"` - `"tls-1.1"` - `"tls-1.2"` - `"tls-1.3"` |
| **revoked_server_cert**  string | Action based on server certificate is revoked.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **sni_server_cert_check**  string | Check the SNI in the client hello message with the CN or SAN fields in the returned server certificate.  **Choices:**   - `"enable"` - `"strict"` - `"disable"` |
| **unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **unsupported_ssl_cipher**  string | Action based on the SSL cipher used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_negotiation**  string | Action based on the SSL negotiation used being unsupported.  **Choices:**   - `"allow"` - `"block"` |
| **unsupported_ssl_version**  string | Action based on the SSL version used being unsupported.  **Choices:**   - `"allow"` - `"block"` - `"inspect"` |
| **untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted_server_cert**  string | Action based on server certificate is not issued by a trusted CA.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **ssl_anomalies_log**  string | Enable/disable logging SSL anomalies.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_anomaly_log**  string | Enable/disable logging of SSL anomalies.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_exempt**  list / elements=dictionary | Servers to exempt from SSL inspection. |
| **address**  string | IPv4 address object. Source firewall.address.name firewall.addrgrp.name. |
| **address6**  string | IPv6 address object. Source firewall.address6.name firewall.addrgrp6.name. |
| **fortiguard_category**  integer | FortiGuard category ID. |
| **id**  integer / required | ID number. see <a href=’#notes’>Notes</a>. |
| **regex**  string | Exempt servers by regular expression. |
| **type**  string | Type of address object (IPv4 or IPv6) or FortiGuard category.  **Choices:**   - `"fortiguard-category"` - `"address"` - `"address6"` - `"wildcard-fqdn"` - `"regex"` |
| **wildcard_fqdn**  string | Exempt servers by wildcard FQDN. Source firewall.wildcard-fqdn.custom.name firewall.wildcard-fqdn.group.name. |
| **ssl_exemption_ip_rating**  string | Enable/disable IP based URL rating.  **Choices:**   - `"enable"` - `"disable"` |
| **ssl_exemption_log**  string | Enable/disable logging of SSL exemptions.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_exemptions_log**  string | Enable/disable logging SSL exemptions.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_handshake_log**  string | Enable/disable logging of TLS handshakes.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_negotiation_log**  string | Enable/disable logging of SSL negotiation events.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_server**  list / elements=dictionary | SSL server settings used for client certificate request. |
| **ftps_client_cert_request**  string | Action based on client certificate request during the FTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ftps_client_certificate**  string | Action based on received client certificate during the FTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **https_client_cert_request**  string | Action based on client certificate request during the HTTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **https_client_certificate**  string | Action based on received client certificate during the HTTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **id**  integer / required | SSL server ID. see <a href=’#notes’>Notes</a>. |
| **imaps_client_cert_request**  string | Action based on client certificate request during the IMAPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **imaps_client_certificate**  string | Action based on received client certificate during the IMAPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ip**  string | IPv4 address of the SSL server. |
| **pop3s_client_cert_request**  string | Action based on client certificate request during the POP3S handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **pop3s_client_certificate**  string | Action based on received client certificate during the POP3S handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **smtps_client_cert_request**  string | Action based on client certificate request during the SMTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **smtps_client_certificate**  string | Action based on received client certificate during the SMTPS handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_other_client_cert_request**  string | Action based on client certificate request during an SSL protocol handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_other_client_certificate**  string | Action based on received client certificate during an SSL protocol handshake.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_server_cert_log**  string | Enable/disable logging of server certificate information.  **Choices:**   - `"disable"` - `"enable"` |
| **supported_alpn**  string | Configure ALPN option.  **Choices:**   - `"http1-1"` - `"http2"` - `"all"` - `"none"` |
| **untrusted_caname**  string | Untrusted CA certificate used by SSL Inspection. Source vpn.certificate.local.name. |
| **use_ssl_server**  string | Enable/disable the use of SSL server table for SSL offloading.  **Choices:**   - `"disable"` - `"enable"` |
| **whitelist**  string | Enable/disable exempting servers by FortiGuard whitelist.  **Choices:**   - `"enable"` - `"disable"` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **state**  string / required | Indicates whether to create or remove the object.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |

## [Notes](fortios_firewall_ssl_ssh_profile_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_firewall_ssl_ssh_profile_module.md#id5)

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
  - name: Configure SSL/SSH protocol options.
    fortios_firewall_ssl_ssh_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_ssl_ssh_profile:
        allowlist: "enable"
        block_blacklisted_certificates: "disable"
        block_blocklisted_certificates: "disable"
        caname: "<your_own_value> (source vpn.certificate.local.name)"
        comment: "Optional comments."
        dot:
            cert_validation_failure: "allow"
            cert_validation_timeout: "allow"
            client_certificate: "bypass"
            expired_server_cert: "allow"
            proxy_after_tcp_handshake: "enable"
            quic: "disable"
            revoked_server_cert: "allow"
            sni_server_cert_check: "enable"
            status: "disable"
            unsupported_ssl_cipher: "allow"
            unsupported_ssl_negotiation: "allow"
            unsupported_ssl_version: "allow"
            untrusted_server_cert: "allow"
        ftps:
            allow_invalid_server_cert: "enable"
            cert_validation_failure: "allow"
            cert_validation_timeout: "allow"
            client_cert_request: "bypass"
            client_certificate: "bypass"
            expired_server_cert: "allow"
            invalid_server_cert: "allow"
            min_allowed_ssl_version: "ssl-3.0"
            ports: "<your_own_value>"
            revoked_server_cert: "allow"
            sni_server_cert_check: "enable"
            status: "disable"
            unsupported_ssl: "bypass"
            unsupported_ssl_cipher: "allow"
            unsupported_ssl_negotiation: "allow"
            unsupported_ssl_version: "allow"
            untrusted_cert: "allow"
            untrusted_server_cert: "allow"
        https:
            allow_invalid_server_cert: "enable"
            cert_probe_failure: "allow"
            cert_validation_failure: "allow"
            cert_validation_timeout: "allow"
            client_cert_request: "bypass"
            client_certificate: "bypass"
            expired_server_cert: "allow"
            invalid_server_cert: "allow"
            min_allowed_ssl_version: "ssl-3.0"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            quic: "disable"
            revoked_server_cert: "allow"
            sni_server_cert_check: "enable"
            status: "disable"
            unsupported_ssl: "bypass"
            unsupported_ssl_cipher: "allow"
            unsupported_ssl_negotiation: "allow"
            unsupported_ssl_version: "allow"
            untrusted_cert: "allow"
            untrusted_server_cert: "allow"
        imaps:
            allow_invalid_server_cert: "enable"
            cert_validation_failure: "allow"
            cert_validation_timeout: "allow"
            client_cert_request: "bypass"
            client_certificate: "bypass"
            expired_server_cert: "allow"
            invalid_server_cert: "allow"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            revoked_server_cert: "allow"
            sni_server_cert_check: "enable"
            status: "disable"
            unsupported_ssl: "bypass"
            unsupported_ssl_cipher: "allow"
            unsupported_ssl_negotiation: "allow"
            unsupported_ssl_version: "allow"
            untrusted_cert: "allow"
            untrusted_server_cert: "allow"
        mapi_over_https: "enable"
        name: "default_name_83"
        pop3s:
            allow_invalid_server_cert: "enable"
            cert_validation_failure: "allow"
            cert_validation_timeout: "allow"
            client_cert_request: "bypass"
            client_certificate: "bypass"
            expired_server_cert: "allow"
            invalid_server_cert: "allow"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            revoked_server_cert: "allow"
            sni_server_cert_check: "enable"
            status: "disable"
            unsupported_ssl: "bypass"
            unsupported_ssl_cipher: "allow"
            unsupported_ssl_negotiation: "allow"
            unsupported_ssl_version: "allow"
            untrusted_cert: "allow"
            untrusted_server_cert: "allow"
        rpc_over_https: "enable"
        server_cert:
         -
            name: "default_name_105 (source vpn.certificate.local.name)"
        server_cert_mode: "re-sign"
        smtps:
            allow_invalid_server_cert: "enable"
            cert_validation_failure: "allow"
            cert_validation_timeout: "allow"
            client_cert_request: "bypass"
            client_certificate: "bypass"
            expired_server_cert: "allow"
            invalid_server_cert: "allow"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            revoked_server_cert: "allow"
            sni_server_cert_check: "enable"
            status: "disable"
            unsupported_ssl: "bypass"
            unsupported_ssl_cipher: "allow"
            unsupported_ssl_negotiation: "allow"
            unsupported_ssl_version: "allow"
            untrusted_cert: "allow"
            untrusted_server_cert: "allow"
        ssh:
            inspect_all: "disable"
            ports: "<your_own_value>"
            proxy_after_tcp_handshake: "enable"
            ssh_algorithm: "compatible"
            ssh_policy_check: "disable"
            ssh_tun_policy_check: "disable"
            status: "disable"
            unsupported_version: "bypass"
        ssl:
            allow_invalid_server_cert: "enable"
            cert_probe_failure: "allow"
            cert_validation_failure: "allow"
            cert_validation_timeout: "allow"
            client_cert_request: "bypass"
            client_certificate: "bypass"
            expired_server_cert: "allow"
            inspect_all: "disable"
            invalid_server_cert: "allow"
            min_allowed_ssl_version: "ssl-3.0"
            revoked_server_cert: "allow"
            sni_server_cert_check: "enable"
            unsupported_ssl: "bypass"
            unsupported_ssl_cipher: "allow"
            unsupported_ssl_negotiation: "allow"
            unsupported_ssl_version: "allow"
            untrusted_cert: "allow"
            untrusted_server_cert: "allow"
        ssl_anomalies_log: "disable"
        ssl_anomaly_log: "disable"
        ssl_exempt:
         -
            address: "<your_own_value> (source firewall.address.name firewall.addrgrp.name)"
            address6: "<your_own_value> (source firewall.address6.name firewall.addrgrp6.name)"
            fortiguard_category: "0"
            id:  "160"
            regex: "<your_own_value>"
            type: "fortiguard-category"
            wildcard_fqdn: "<your_own_value> (source firewall.wildcard-fqdn.custom.name firewall.wildcard-fqdn.group.name)"
        ssl_exemption_ip_rating: "enable"
        ssl_exemption_log: "disable"
        ssl_exemptions_log: "disable"
        ssl_handshake_log: "disable"
        ssl_negotiation_log: "disable"
        ssl_server:
         -
            ftps_client_cert_request: "bypass"
            ftps_client_certificate: "bypass"
            https_client_cert_request: "bypass"
            https_client_certificate: "bypass"
            id:  "174"
            imaps_client_cert_request: "bypass"
            imaps_client_certificate: "bypass"
            ip: "<your_own_value>"
            pop3s_client_cert_request: "bypass"
            pop3s_client_certificate: "bypass"
            smtps_client_cert_request: "bypass"
            smtps_client_certificate: "bypass"
            ssl_other_client_cert_request: "bypass"
            ssl_other_client_certificate: "bypass"
        ssl_server_cert_log: "disable"
        supported_alpn: "http1-1"
        untrusted_caname: "<your_own_value> (source vpn.certificate.local.name)"
        use_ssl_server: "disable"
        whitelist: "enable"
```

## [Return Values](fortios_firewall_ssl_ssh_profile_module.md#id6)

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
