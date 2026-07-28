---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_cifs_server module – NetApp ONTAP CIFS server configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_cifs_server_module.html
fetched_at: 2026-07-28T02:41:46+00:00
---
# netapp.ontap.na_ontap_cifs_server module – NetApp ONTAP CIFS server configuration

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_cifs_server_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-server-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_cifs_server`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_cifs_server_module.md#synopsis)
- [Requirements](na_ontap_cifs_server_module.md#requirements)
- [Parameters](na_ontap_cifs_server_module.md#parameters)
- [Notes](na_ontap_cifs_server_module.md#notes)
- [Examples](na_ontap_cifs_server_module.md#examples)

## [Synopsis](na_ontap_cifs_server_module.md#id1)

- Creating / deleting and modifying the CIFS server .

## [Requirements](na_ontap_cifs_server_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_cifs_server_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_password**  string | Specifies the cifs server admin password.  When used with absent, the account will be deleted if admin_user_name is also provided. |
| **admin_user_name**  string | Specifies the cifs server admin username.  When used with absent, the account will be deleted if admin_password is also provided. |
| **aes_netlogon_enabled**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether or not an AES session key is enabled for the Netlogon channel.  Only supported with REST and requires ontap version 9.10.1 or later.  **Choices:**   - `false` - `true` |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **default_site**  string  *added in netapp.ontap 22.8.0* | Specifies the site within the Active Directory domain to associate with the CIFS server if Data ONTAP cannot determine an appropriate site.  Only supported with REST and requires ontap version 9.13.1 or later. |
| **domain**  string | The Fully Qualified Domain Name of the Windows Active Directory this CIFS server belongs to. |
| **encrypt_dc_connection**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether encryption is required for domain controller connections.  Only supported with REST and requires ontap version 9.8 or later. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `false` - `true` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force**  boolean  *added in netapp.ontap 2.7.0* | When state is present, if this is set and a machine account with the same name as specified in ‘name’ exists in the Active Directory, it will be overwritten and reused.  When state is absent, if this is set, the local CIFS configuration is deleted regardless of communication errors.  For REST, it requires ontap version 9.11.  **Choices:**   - `false` - `true` |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_name**  string  *added in netapp.ontap 21.19.0* | Specifies the existing cifs_server name.  This option is used to rename cifs_server.  Supported only in REST and requires force to be set to True.  Requires ontap version 9.11.0.  if the service is running, it will be stopped to perform the rename action, and automatically restarts.  if the service is stopped, it will be briefly restarted after the rename action, and stopped again. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **kdc_encryption**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether AES-128 and AES-256 encryption is enabled for all Kerberos-based communication with the Active Directory KDC.  Only supported with REST. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `false` - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **ldap_referral_enabled**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether or not LDAP referral chasing is enabled for AD LDAP connections.  Only supported with REST and requires ontap version 9.10.1 or later. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `false` - `true` |
| **name**  aliases: cifs_server_name  string / required | Specifies the cifs_server name. |
| **ontapi**  integer | The ontap api version to use |
| **ou**  string  *added in netapp.ontap 2.7.0* | The Organizational Unit (OU) within the Windows Active Directory this CIFS server belongs to. |
| **password**  aliases: pass  string | Password for the specified user. |
| **restrict_anonymous**  string  *added in netapp.ontap 21.20.0* | Specifies what level of access an anonymous user is granted.  Only supported with REST.  **Choices:**   - `"no_enumeration"` - `"no_restriction"` - `"no_access"` |
| **service_state**  string | CIFS Server Administrative Status.  **Choices:**   - `"stopped"` - `"started"` |
| **session_security**  string  *added in netapp.ontap 21.20.0* | Specifies client session security for AD LDAP connections.  Only supported with REST and requires ontap version 9.10.1 or later. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `"none"` - `"sign"` - `"seal"` |
| **smb_encryption**  boolean  *added in netapp.ontap 21.20.0* | Determine whether SMB encryption is required for incoming CIFS traffic.  Only supported with REST. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `false` - `true` |
| **smb_signing**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether signing is required for incoming CIFS traffic.  Only supported with REST. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `false` - `true` |
| **state**  string | Whether the specified cifs_server should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **try_ldap_channel_binding**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether or not channel binding is attempted in the case of TLS/LDAPS.  Only supported with REST and requires ontap version 9.10.1 or later. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `false` - `true` |
| **use_ldaps**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether or not to use use LDAPS for secure Active Directory LDAP connections.  Only supported with REST and requires ontap version 9.10.1 or later. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `false` - `true` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **use_start_tls**  boolean  *added in netapp.ontap 21.20.0* | Specifies whether or not to use SSL/TLS for allowing secure LDAP communication with Active Directory LDAP servers.  Only supported with REST and requires ontap version 9.10.1 or later. Use na_ontap_vserver_cifs_security with ZAPI.  **Choices:**   - `false` - `true` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | The name of the vserver to use. |
| **workgroup**  string | The NetBIOS name of the domain or workgroup this CIFS server belongs to. |

## [Notes](na_ontap_cifs_server_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_cifs_server_module.md#id5)

```yaml+jinja
- name: Create cifs_server
  netapp.ontap.na_ontap_cifs_server:
    state: present
    name: data2
    vserver: svm1
    service_state: stopped
    domain: "{{ id_domain }}"
    admin_user_name: "{{ domain_login }}"
    admin_password: "{{ domain_pwd }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete cifs_server
  netapp.ontap.na_ontap_cifs_server:
    state: absent
    name: data2
    vserver: svm1
    admin_user_name: "{{ domain_login }}"
    admin_password: "{{ domain_pwd }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Start cifs_server
  netapp.ontap.na_ontap_cifs_server:
    state: present
    name: data2
    vserver: svm1
    service_state: started
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Stop cifs_server
  netapp.ontap.na_ontap_cifs_server:
    state: present
    name: data2
    vserver: svm1
    service_state: stopped
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Rename cifs_server - REST
  netapp.ontap.na_ontap_cifs_server:
    state: present
    from_name: data2
    name: cifs
    vserver: svm1
    force: True
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify cifs_server security - REST
  netapp.ontap.na_ontap_cifs_server:
    state: present
    name: data2
    vserver: svm1
    service_state: stopped
    encrypt_dc_connection: True
    smb_encryption: True
    kdc_encryption: True
    smb_signing: True
    aes_netlogon_enabled: True
    ldap_referral_enabled: True
    session_security: seal
    try_ldap_channel_binding: False
    use_ldaps: True
    use_start_tls: True
    restrict_anonymous: no_access
    domain: "{{ id_domain }}"
    admin_user_name: "{{ domain_login }}"
    admin_password: "{{ domain_pwd }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
