---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_vserver_cifs_security module – NetApp ONTAP vserver CIFS security modification"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_vserver_cifs_security_module.html
fetched_at: 2026-07-28T00:13:32+00:00
---
# netapp.ontap.na_ontap_vserver_cifs_security module – NetApp ONTAP vserver CIFS security modification

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_vserver_cifs_security_module.md#ansible-collections-netapp-ontap-na-ontap-vserver-cifs-security-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_vserver_cifs_security`.

New in netapp.ontap 2.9.0

- [Synopsis](na_ontap_vserver_cifs_security_module.md#synopsis)
- [Requirements](na_ontap_vserver_cifs_security_module.md#requirements)
- [Parameters](na_ontap_vserver_cifs_security_module.md#parameters)
- [Notes](na_ontap_vserver_cifs_security_module.md#notes)
- [Examples](na_ontap_vserver_cifs_security_module.md#examples)

## [Synopsis](na_ontap_vserver_cifs_security_module.md#id1)

- modify vserver CIFS security.

## [Requirements](na_ontap_vserver_cifs_security_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_vserver_cifs_security_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **encryption_required_for_dc_connections**  boolean  added in netapp.ontap 21.20.0 | Specifies whether encryption is required for domain controller connections.  Choices:   - `false` - `true` |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **is_aes_encryption_enabled**  boolean | Determine whether AES-128 and AES-256 encryption mechanisms are enabled for Kerberos-related CIFS communication.  Choices:   - `false` - `true` |
| **is_password_complexity_required**  boolean | Determine whether password complexity is required for local users.  Choices:   - `false` - `true` |
| **is_signing_required**  boolean | Determine whether signing is required for incoming CIFS traffic.  Choices:   - `false` - `true` |
| **is_smb_encryption_required**  boolean | Determine whether SMB encryption is required for incoming CIFS traffic.  Choices:   - `false` - `true` |
| **kerberos_clock_skew**  integer | The clock skew in minutes is the tolerance for accepting tickets with time stamps that do not exactly match the host’s system clock. |
| **kerberos_kdc_timeout**  integer | Determine the timeout value in seconds for KDC connections. |
| **kerberos_renew_age**  integer | Determine the maximum amount of time in days for which a ticket can be renewed. |
| **kerberos_ticket_age**  integer | Determine the maximum amount of time in hours that a user’s ticket may be used for the purpose of Kerberos authentication. |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **lm_compatibility_level**  string | Determine the LM compatibility level.  Choices:   - `"lm_ntlm_ntlmv2_krb"` - `"ntlm_ntlmv2_krb"` - `"ntlmv2_krb"` - `"krb"` |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **referral_enabled_for_ad_ldap**  boolean | Determine whether LDAP referral chasing is enabled or not for AD LDAP connections.  Choices:   - `false` - `true` |
| **session_security_for_ad_ldap**  string | Determine the level of security required for LDAP communications.  Choices:   - `"none"` - `"sign"` - `"seal"` |
| **smb1_enabled_for_dc_connections**  string | Determine if SMB version 1 is used for connections to domain controllers.  Choices:   - `"false"` - `"true"` - `"system_default"` |
| **smb2_enabled_for_dc_connections**  string | Determine if SMB version 2 is used for connections to domain controllers.  Choices:   - `"false"` - `"true"` - `"system_default"` |
| **use_ldaps_for_ad_ldap**  boolean  added in netapp.ontap 21.20.0 | Determine whether to use LDAPS for secure Active Directory LDAP connections.  Choices:   - `false` - `true` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **use_start_tls_for_ad_ldap**  boolean | Determine whether to use start_tls for AD LDAP connections.  Choices:   - `false` - `true` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | name of the vserver. |

## [Notes](na_ontap_vserver_cifs_security_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_vserver_cifs_security_module.md#id5)

```yaml+jinja
- name: modify cifs security
  netapp.ontap.na_ontap_vserver_cifs_security:
    hostname: "{{ hostname }}"
    username: username
    password: password
    vserver: ansible
    is_aes_encryption_enabled: false
    lm_compatibility_level: lm_ntlm_ntlmv2_krb
    smb1_enabled_for_dc_connections: system_default
    smb2_enabled_for_dc_connections: system_default
    use_start_tls_for_ad_ldap: false
    referral_enabled_for_ad_ldap: false
    session_security_for_ad_ldap: none
    is_signing_required: false
    is_password_complexity_required: false
    encryption_required_for_dc_connections: false
    use_ldaps_for_ad_ldap: false

- name: modify cifs security is_smb_encryption_required
  netapp.ontap.na_ontap_vserver_cifs_security:
    hostname: "{{ hostname }}"
    username: username
    password: password
    vserver: ansible
    is_smb_encryption_required: false

- name: modify cifs security int options
  netapp.ontap.na_ontap_vserver_cifs_security:
    hostname: "{{ hostname }}"
    username: username
    password: password
    vserver: ansible
    kerberos_clock_skew: 10
    kerberos_ticket_age: 10
    kerberos_renew_age: 5
    kerberos_kdc_timeout: 3
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
