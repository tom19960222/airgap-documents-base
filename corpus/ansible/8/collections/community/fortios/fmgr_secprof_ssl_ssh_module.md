---
collection: ansible
version: "8"
title: "community.fortios.fmgr_secprof_ssl_ssh module – Manage SSL and SSH security profiles in FortiManager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_secprof_ssl_ssh_module.html
fetched_at: 2026-07-28T01:44:23+00:00
---
# community.fortios.fmgr_secprof_ssl_ssh module – Manage SSL and SSH security profiles in FortiManager

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_secprof_ssl_ssh`.

- [Synopsis](fmgr_secprof_ssl_ssh_module.md#synopsis)
- [Parameters](fmgr_secprof_ssl_ssh_module.md#parameters)
- [Notes](fmgr_secprof_ssl_ssh_module.md#notes)
- [Examples](fmgr_secprof_ssl_ssh_module.md#examples)
- [Return Values](fmgr_secprof_ssl_ssh_module.md#return-values)

## [Synopsis](fmgr_secprof_ssl_ssh_module.md#id1)

- Manage SSL and SSH security profiles in FortiManager via the FMG API

## [Parameters](fmgr_secprof_ssl_ssh_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **caname**  string | CA certificate used by SSL Inspection. |
| **comment**  string | Optional comments. |
| **ftps**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **ftps_allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **ftps_client_cert_request**  string | Action based on client certificate request failure.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ftps_ports**  string | Ports to use for scanning (1 - 65535, default = 443). |
| **ftps_status**  string | Configure protocol inspection status.  choice | disable | Disable.  choice | deep-inspection | Full SSL inspection.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **ftps_unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ftps_untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  choice | allow | Allow the untrusted server certificate.  choice | block | Block the connection when an untrusted server certificate is detected.  choice | ignore | Always take the server certificate as trusted.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **https**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **https_allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **https_client_cert_request**  string | Action based on client certificate request failure.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **https_ports**  string | Ports to use for scanning (1 - 65535, default = 443). |
| **https_status**  string | Configure protocol inspection status.  choice | disable | Disable.  choice | certificate-inspection | Inspect SSL handshake only.  choice | deep-inspection | Full SSL inspection.  **Choices:**   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **https_unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **https_untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  choice | allow | Allow the untrusted server certificate.  choice | block | Block the connection when an untrusted server certificate is detected.  choice | ignore | Always take the server certificate as trusted.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **imaps**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **imaps_allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **imaps_client_cert_request**  string | Action based on client certificate request failure.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **imaps_ports**  string | Ports to use for scanning (1 - 65535, default = 443). |
| **imaps_status**  string | Configure protocol inspection status.  choice | disable | Disable.  choice | deep-inspection | Full SSL inspection.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **imaps_unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **imaps_untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  choice | allow | Allow the untrusted server certificate.  choice | block | Block the connection when an untrusted server certificate is detected.  choice | ignore | Always take the server certificate as trusted.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **mapi_over_https**  string | Enable/disable inspection of MAPI over HTTPS.  choice | disable | Disable inspection of MAPI over HTTPS.  choice | enable | Enable inspection of MAPI over HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **mode**  string | Sets one of three modes for managing the object.  Allows use of soft-adds instead of overwriting existing values  **Choices:**   - `"add"` ← (default) - `"set"` - `"delete"` - `"update"` |
| **name**  string | Name. |
| **pop3s**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **pop3s_allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **pop3s_client_cert_request**  string | Action based on client certificate request failure.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **pop3s_ports**  string | Ports to use for scanning (1 - 65535, default = 443). |
| **pop3s_status**  string | Configure protocol inspection status.  choice | disable | Disable.  choice | deep-inspection | Full SSL inspection.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **pop3s_unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **pop3s_untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  choice | allow | Allow the untrusted server certificate.  choice | block | Block the connection when an untrusted server certificate is detected.  choice | ignore | Always take the server certificate as trusted.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **rpc_over_https**  string | Enable/disable inspection of RPC over HTTPS.  choice | disable | Disable inspection of RPC over HTTPS.  choice | enable | Enable inspection of RPC over HTTPS.  **Choices:**   - `"disable"` - `"enable"` |
| **server_cert**  string | Certificate used by SSL Inspection to replace server certificate. |
| **server_cert_mode**  string | Re-sign or replace the server’s certificate.  choice | re-sign | Multiple clients connecting to multiple servers.  choice | replace | Protect an SSL server.  **Choices:**   - `"re-sign"` - `"replace"` |
| **smtps**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **smtps_allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **smtps_client_cert_request**  string | Action based on client certificate request failure.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **smtps_ports**  string | Ports to use for scanning (1 - 65535, default = 443). |
| **smtps_status**  string | Configure protocol inspection status.  choice | disable | Disable.  choice | deep-inspection | Full SSL inspection.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **smtps_unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **smtps_untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  choice | allow | Allow the untrusted server certificate.  choice | block | Block the connection when an untrusted server certificate is detected.  choice | ignore | Always take the server certificate as trusted.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **ssh**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **ssh_inspect_all**  string | Level of SSL inspection.  choice | disable | Disable.  choice | deep-inspection | Full SSL inspection.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **ssh_ports**  string | Ports to use for scanning (1 - 65535, default = 443). |
| **ssh_ssh_algorithm**  string | Relative strength of encryption algorithms accepted during negotiation.  choice | compatible | Allow a broader set of encryption algorithms for best compatibility.  choice | high-encryption | Allow only AES-CTR, AES-GCM ciphers and high encryption algorithms.  **Choices:**   - `"compatible"` - `"high-encryption"` |
| **ssh_ssh_policy_check**  string | Enable/disable SSH policy check.  choice | disable | Disable SSH policy check.  choice | enable | Enable SSH policy check.  **Choices:**   - `"disable"` - `"enable"` |
| **ssh_ssh_tun_policy_check**  string | Enable/disable SSH tunnel policy check.  choice | disable | Disable SSH tunnel policy check.  choice | enable | Enable SSH tunnel policy check.  **Choices:**   - `"disable"` - `"enable"` |
| **ssh_status**  string | Configure protocol inspection status.  choice | disable | Disable.  choice | deep-inspection | Full SSL inspection.  **Choices:**   - `"disable"` - `"deep-inspection"` |
| **ssh_unsupported_version**  string | Action based on SSH version being unsupported.  choice | block | Block.  choice | bypass | Bypass.  **Choices:**   - `"block"` - `"bypass"` |
| **ssl**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **ssl_allow_invalid_server_cert**  string | When enabled, allows SSL sessions whose server certificate validation failed.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_anomalies_log**  string | Enable/disable logging SSL anomalies.  choice | disable | Disable logging SSL anomalies.  choice | enable | Enable logging SSL anomalies.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_client_cert_request**  string | Action based on client certificate request failure.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_exempt**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **ssl_exempt_address**  string | IPv4 address object. |
| **ssl_exempt_address6**  string | IPv6 address object. |
| **ssl_exempt_fortiguard_category**  string | FortiGuard category ID. |
| **ssl_exempt_regex**  string | Exempt servers by regular expression. |
| **ssl_exempt_type**  string | Type of address object (IPv4 or IPv6) or FortiGuard category.  choice | fortiguard-category | FortiGuard category.  choice | address | Firewall IPv4 address.  choice | address6 | Firewall IPv6 address.  choice | wildcard-fqdn | Fully Qualified Domain Name with wildcard characters.  choice | regex | Regular expression FQDN.  **Choices:**   - `"fortiguard-category"` - `"address"` - `"address6"` - `"wildcard-fqdn"` - `"regex"` |
| **ssl_exempt_wildcard_fqdn**  string | Exempt servers by wildcard FQDN. |
| **ssl_exemptions_log**  string | Enable/disable logging SSL exemptions.  choice | disable | Disable logging SSL exemptions.  choice | enable | Enable logging SSL exemptions.  **Choices:**   - `"disable"` - `"enable"` |
| **ssl_inspect_all**  string | Level of SSL inspection.  choice | disable | Disable.  choice | certificate-inspection | Inspect SSL handshake only.  choice | deep-inspection | Full SSL inspection.  **Choices:**   - `"disable"` - `"certificate-inspection"` - `"deep-inspection"` |
| **ssl_server**  string | EXPERTS ONLY! KNOWLEDGE OF FMGR JSON API IS REQUIRED!  List of multiple child objects to be added. Expects a list of dictionaries.  Dictionaries must use FortiManager API parameters, not the ansible ones listed below.  If submitted, all other prefixed sub-parameters ARE IGNORED.  This object is MUTUALLY EXCLUSIVE with its options.  We expect that you know what you are doing with these list parameters, and are leveraging the JSON API Guide.  WHEN IN DOUBT, USE THE SUB OPTIONS BELOW INSTEAD TO CREATE OBJECTS WITH MULTIPLE TASKS |
| **ssl_server_ftps_client_cert_request**  string | Action based on client certificate request failure during the FTPS handshake.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_server_https_client_cert_request**  string | Action based on client certificate request failure during the HTTPS handshake.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_server_imaps_client_cert_request**  string | Action based on client certificate request failure during the IMAPS handshake.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_server_ip**  string | IPv4 address of the SSL server. |
| **ssl_server_pop3s_client_cert_request**  string | Action based on client certificate request failure during the POP3S handshake.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_server_smtps_client_cert_request**  string | Action based on client certificate request failure during the SMTPS handshake.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_server_ssl_other_client_cert_request**  string | Action based on client certificate request failure during an SSL protocol handshake.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_unsupported_ssl**  string | Action based on the SSL encryption used being unsupported.  choice | bypass | Bypass.  choice | inspect | Inspect.  choice | block | Block.  **Choices:**   - `"bypass"` - `"inspect"` - `"block"` |
| **ssl_untrusted_cert**  string | Allow, ignore, or block the untrusted SSL session server certificate.  choice | allow | Allow the untrusted server certificate.  choice | block | Block the connection when an untrusted server certificate is detected.  choice | ignore | Always take the server certificate as trusted.  **Choices:**   - `"allow"` - `"block"` - `"ignore"` |
| **untrusted_caname**  string | Untrusted CA certificate used by SSL Inspection. |
| **use_ssl_server**  string | Enable/disable the use of SSL server table for SSL offloading.  choice | disable | Don’t use SSL server configuration.  choice | enable | Use SSL server configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **whitelist**  string | Enable/disable exempting servers by FortiGuard whitelist.  choice | disable | Disable setting.  choice | enable | Enable setting.  **Choices:**   - `"disable"` - `"enable"` |

## [Notes](fmgr_secprof_ssl_ssh_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_secprof_ssl_ssh_module.md#id4)

```yaml+jinja
- name: DELETE Profile
  community.fortios.fmgr_secprof_ssl_ssh:
    name: Ansible_SSL_SSH_Profile
    mode: delete

- name: CREATE Profile
  community.fortios.fmgr_secprof_ssl_ssh:
    name: Ansible_SSL_SSH_Profile
    comment: "Created by Ansible Module TEST"
    mode: set
    mapi_over_https: enable
    rpc_over_https: enable
    server_cert_mode: replace
    ssl_anomalies_log: enable
    ssl_exemptions_log: enable
    use_ssl_server: enable
    whitelist: enable
```

## [Return Values](fmgr_secprof_ssl_ssh_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
