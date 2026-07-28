---
collection: ansible
version: "8"
title: "fortinet.fortios.fortios_vpn_certificate_setting module – VPN certificate setting in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortios/fortios_vpn_certificate_setting_module.html
fetched_at: 2026-07-28T02:30:14+00:00
---
# fortinet.fortios.fortios_vpn_certificate_setting module – VPN certificate setting in Fortinet’s FortiOS and FortiGate.

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
> see [Requirements](fortios_vpn_certificate_setting_module.md#ansible-collections-fortinet-fortios-fortios-vpn-certificate-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_vpn_certificate_setting`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_vpn_certificate_setting_module.md#synopsis)
- [Requirements](fortios_vpn_certificate_setting_module.md#requirements)
- [Parameters](fortios_vpn_certificate_setting_module.md#parameters)
- [Notes](fortios_vpn_certificate_setting_module.md#notes)
- [Examples](fortios_vpn_certificate_setting_module.md#examples)
- [Return Values](fortios_vpn_certificate_setting_module.md#return-values)

## [Synopsis](fortios_vpn_certificate_setting_module.md#id1)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify vpn_certificate feature and setting category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_vpn_certificate_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- ansible>=2.14

## [Parameters](fortios_vpn_certificate_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  **Choices:**   - `"present"` - `"absent"` |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  **Default:** `"root"` |
| **vpn_certificate_setting**  dictionary | VPN certificate setting. |
| **cert_expire_warning**  integer | Number of days before a certificate expires to send a warning. Set to 0 to disable sending of the warning (0 - 100). |
| **certname_dsa1024**  string | 1024 bit DSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_dsa2048**  string | 2048 bit DSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_ecdsa256**  string | 256 bit ECDSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_ecdsa384**  string | 384 bit ECDSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_ecdsa521**  string | 521 bit ECDSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_ed25519**  string | 253 bit EdDSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_ed448**  string | 456 bit EdDSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_rsa1024**  string | 1024 bit RSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_rsa2048**  string | 2048 bit RSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **certname_rsa4096**  string | 4096 bit RSA key certificate for re-signing server certificates for SSL inspection. Source vpn.certificate.local.name. |
| **check_ca_cert**  string | Enable/disable verification of the user certificate and pass authentication if any CA in the chain is trusted .  **Choices:**   - `"enable"` - `"disable"` |
| **check_ca_chain**  string | Enable/disable verification of the entire certificate chain and pass authentication only if the chain is complete and all of the CAs in the chain are trusted .  **Choices:**   - `"enable"` - `"disable"` |
| **cmp_key_usage_checking**  string | Enable/disable server certificate key usage checking in CMP mode .  **Choices:**   - `"enable"` - `"disable"` |
| **cmp_save_extra_certs**  string | Enable/disable saving extra certificates in CMP mode .  **Choices:**   - `"enable"` - `"disable"` |
| **cn_allow_multi**  string | When searching for a matching certificate, allow multiple CN fields in certificate subject name .  **Choices:**   - `"disable"` - `"enable"` |
| **cn_match**  string | When searching for a matching certificate, control how to do CN value matching with certificate subject name .  **Choices:**   - `"substring"` - `"value"` |
| **crl_verification**  dictionary | CRL verification options. |
| **chain_crl_absence**  string | CRL verification option when CRL of any certificate in chain is absent .  **Choices:**   - `"ignore"` - `"revoke"` |
| **expiry**  string | CRL verification option when CRL is expired .  **Choices:**   - `"ignore"` - `"revoke"` |
| **leaf_crl_absence**  string | CRL verification option when leaf CRL is absent .  **Choices:**   - `"ignore"` - `"revoke"` |
| **interface**  string | Specify outgoing interface to reach server. Source system.interface.name. |
| **interface_select_method**  string | Specify how to select outgoing interface to reach server.  **Choices:**   - `"auto"` - `"sdwan"` - `"specify"` |
| **ocsp_default_server**  string | Default OCSP server. Source vpn.certificate.ocsp-server.name. |
| **ocsp_option**  string | Specify whether the OCSP URL is from certificate or configured OCSP server.  **Choices:**   - `"certificate"` - `"server"` |
| **ocsp_status**  string | Enable/disable receiving certificates using the OCSP.  **Choices:**   - `"enable"` - `"disable"` |
| **proxy**  string | Proxy server FQDN or IP for OCSP/CA queries during certificate verification. |
| **proxy_password**  string | Proxy server password. |
| **proxy_port**  integer | Proxy server port (1 - 65535). |
| **proxy_username**  string | Proxy server user name. |
| **source_ip**  string | Source IP address for dynamic AIA and OCSP queries. |
| **ssl_min_proto_version**  string | Minimum supported protocol version for SSL/TLS connections .  **Choices:**   - `"default"` - `"SSLv3"` - `"TLSv1"` - `"TLSv1-1"` - `"TLSv1-2"` - `"TLSv1-3"` |
| **ssl_ocsp_option**  string | Specify whether the OCSP URL is from the certificate or the default OCSP server.  **Choices:**   - `"certificate"` - `"server"` |
| **ssl_ocsp_source_ip**  string | Source IP address to use to communicate with the OCSP server. |
| **ssl_ocsp_status**  string | Enable/disable SSL OCSP.  **Choices:**   - `"enable"` - `"disable"` |
| **strict_crl_check**  string | Enable/disable strict mode CRL checking.  **Choices:**   - `"enable"` - `"disable"` |
| **strict_ocsp_check**  string | Enable/disable strict mode OCSP checking.  **Choices:**   - `"enable"` - `"disable"` |
| **subject_match**  string | When searching for a matching certificate, control how to do RDN value matching with certificate subject name .  **Choices:**   - `"substring"` - `"value"` |
| **subject_set**  string | When searching for a matching certificate, control how to do RDN set matching with certificate subject name .  **Choices:**   - `"subset"` - `"superset"` |

## [Notes](fortios_vpn_certificate_setting_module.md#id4)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_vpn_certificate_setting_module.md#id5)

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
  - name: VPN certificate setting.
    fortios_vpn_certificate_setting:
      vdom:  "{{ vdom }}"
      vpn_certificate_setting:
        cert_expire_warning: "14"
        certname_dsa1024: "<your_own_value> (source vpn.certificate.local.name)"
        certname_dsa2048: "<your_own_value> (source vpn.certificate.local.name)"
        certname_ecdsa256: "<your_own_value> (source vpn.certificate.local.name)"
        certname_ecdsa384: "<your_own_value> (source vpn.certificate.local.name)"
        certname_ecdsa521: "<your_own_value> (source vpn.certificate.local.name)"
        certname_ed25519: "<your_own_value> (source vpn.certificate.local.name)"
        certname_ed448: "<your_own_value> (source vpn.certificate.local.name)"
        certname_rsa1024: "<your_own_value> (source vpn.certificate.local.name)"
        certname_rsa2048: "<your_own_value> (source vpn.certificate.local.name)"
        certname_rsa4096: "<your_own_value> (source vpn.certificate.local.name)"
        check_ca_cert: "enable"
        check_ca_chain: "enable"
        cmp_key_usage_checking: "enable"
        cmp_save_extra_certs: "enable"
        cn_allow_multi: "disable"
        cn_match: "substring"
        crl_verification:
            chain_crl_absence: "ignore"
            expiry: "ignore"
            leaf_crl_absence: "ignore"
        interface: "<your_own_value> (source system.interface.name)"
        interface_select_method: "auto"
        ocsp_default_server: "<your_own_value> (source vpn.certificate.ocsp-server.name)"
        ocsp_option: "certificate"
        ocsp_status: "enable"
        proxy: "<your_own_value>"
        proxy_password: "<your_own_value>"
        proxy_port: "8080"
        proxy_username: "<your_own_value>"
        source_ip: "84.230.14.43"
        ssl_min_proto_version: "default"
        ssl_ocsp_option: "certificate"
        ssl_ocsp_source_ip: "<your_own_value>"
        ssl_ocsp_status: "enable"
        strict_crl_check: "enable"
        strict_ocsp_check: "enable"
        subject_match: "substring"
        subject_set: "subset"
```

## [Return Values](fortios_vpn_certificate_setting_module.md#id6)

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
