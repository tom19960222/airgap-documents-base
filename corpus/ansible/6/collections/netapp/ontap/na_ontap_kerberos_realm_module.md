---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_kerberos_realm module – NetApp ONTAP vserver nfs kerberos realm"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_kerberos_realm_module.html
fetched_at: 2026-07-28T00:12:34+00:00
---
# netapp.ontap.na_ontap_kerberos_realm module – NetApp ONTAP vserver nfs kerberos realm

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
> see [Requirements](na_ontap_kerberos_realm_module.md#ansible-collections-netapp-ontap-na-ontap-kerberos-realm-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_kerberos_realm`.

New in netapp.ontap 2.9.0

- [Synopsis](na_ontap_kerberos_realm_module.md#synopsis)
- [Requirements](na_ontap_kerberos_realm_module.md#requirements)
- [Parameters](na_ontap_kerberos_realm_module.md#parameters)
- [Notes](na_ontap_kerberos_realm_module.md#notes)
- [Examples](na_ontap_kerberos_realm_module.md#examples)

## [Synopsis](na_ontap_kerberos_realm_module.md#id1)

- Create, modify or delete vserver kerberos realm configuration

## [Requirements](na_ontap_kerberos_realm_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_kerberos_realm_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ad_server_ip**  string  added in netapp.ontap 20.4.0 | IP Address of the Active Directory Domain Controller (DC). This is a mandatory parameter if the kdc-vendor is ‘microsoft’. |
| **ad_server_name**  string  added in netapp.ontap 20.4.0 | Host name of the Active Directory Domain Controller (DC). This is a mandatory parameter if the kdc-vendor is ‘microsoft’. |
| **admin_server_ip**  string | IP address of the host where the Kerberos administration daemon is running. This is usually the master KDC.  If this parameter is omitted, the address specified in kdc_ip is used.  This option is not supported with REST. |
| **admin_server_port**  string | The TCP port on the Kerberos administration server where the Kerberos administration service is running.  The default for this parmater is ‘749’.  This option is not supported with REST. |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **clock_skew**  string | The clock skew in minutes is the tolerance for accepting tickets with time stamps that do not exactly match the host’s system clock.  The default for this parameter is ‘5’ minutes.  This option is not supported with REST. |
| **comment**  string | Optional comment |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **kdc_ip**  string | IP address of the Key Distribution Centre (KDC) server  Required if *state=present* |
| **kdc_port**  integer | TCP port on the KDC to be used for Kerberos communication.  The default for this parameter is 88. |
| **kdc_vendor**  string | The vendor of the Key Distribution Centre (KDC) server  Required if *state=present*  Choices:   - `"other"` - `"microsoft"` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **pw_server_ip**  string | IP address of the host where the Kerberos password-changing server is running.  Typically, this is the same as the host indicated in the adminserver-ip.  If this parameter is omitted, the IP address in kdc-ip is used.  This option is not supported with REST. |
| **pw_server_port**  string | The TCP port on the Kerberos password-changing server where the Kerberos password-changing service is running.  The default for this parameter is ‘464’.  This option is not supported with REST. |
| **realm**  string / required | Kerberos realm name |
| **state**  string | Whether the Kerberos realm is present or absent.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | vserver/svm with kerberos realm configured |

## [Notes](na_ontap_kerberos_realm_module.md#id4)

> **Note:**
>
> - supports ZAPI and REST. REST requires ONTAP 9.6 or later.
> - supports check mode.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_kerberos_realm_module.md#id5)

```yaml+jinja
- name: Create kerberos realm other kdc vendor
  netapp.ontap.na_ontap_kerberos_realm:
    state: present
    realm: 'EXAMPLE.COM'
    vserver: 'vserver1'
    kdc_ip: '1.2.3.4'
    kdc_vendor: 'other'
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create kerberos realm Microsoft kdc vendor
  netapp.ontap.na_ontap_kerberos_realm:
    state: present
    realm: 'EXAMPLE.COM'
    vserver: 'vserver1'
    kdc_ip: '1.2.3.4'
    kdc_vendor: 'microsoft'
    ad_server_ip: '0.0.0.0'
    ad_server_name: 'server'
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- Milan Zink (@zeten30) ,

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
