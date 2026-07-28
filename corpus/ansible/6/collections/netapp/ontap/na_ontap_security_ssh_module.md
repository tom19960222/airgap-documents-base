---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_security_ssh module – NetApp ONTAP security ssh"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_security_ssh_module.html
fetched_at: 2026-07-28T00:13:11+00:00
---
# netapp.ontap.na_ontap_security_ssh module – NetApp ONTAP security ssh

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
> see [Requirements](na_ontap_security_ssh_module.md#ansible-collections-netapp-ontap-na-ontap-security-ssh-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_security_ssh`.

New in netapp.ontap 21.24.0

- [Synopsis](na_ontap_security_ssh_module.md#synopsis)
- [Requirements](na_ontap_security_ssh_module.md#requirements)
- [Parameters](na_ontap_security_ssh_module.md#parameters)
- [Notes](na_ontap_security_ssh_module.md#notes)
- [Examples](na_ontap_security_ssh_module.md#examples)

## [Synopsis](na_ontap_security_ssh_module.md#id1)

- Modify SSH server configuration of SVM on ONTAP

## [Requirements](na_ontap_security_ssh_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_security_ssh_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **ciphers**  list / elements=string | Ciphers for encrypting the data.  Example list [ aes256_ctr, aes192_ctr, aes128_ctr, aes256_cbc, aes192_cbc ] |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_exchange_algorithms**  list / elements=string | Key exchange algorithms.  Example list [ diffie_hellman_group_exchange_sha256, diffie_hellman_group14_sha1 ] |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **mac_algorithms**  list / elements=string | MAC algorithms.  Example list [ hmac_sha1, hmac_sha2_512_etm ] |
| **max_authentication_retry_count**  integer | Maximum authentication retries allowed before closing the connection.  Minimum value is 2 and maximum is 6.  Default value is 2. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **state**  string | SSH service is always enabled.  Choices:   - `"present"` ← (default) |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string | Name of the vserver to use for vserver scope.  If absent or null, cluster scope is assumed. |

## [Notes](na_ontap_security_ssh_module.md#id4)

> **Note:**
>
> - Removing all SSH key exchange algorithms is not supported. SSH login would fail.
> - This module is only for REST.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_security_ssh_module.md#id5)

```yaml+jinja
- name: Modify SSH algorithms
  netapp.ontap.na_ontap_security_ssh:
    vserver: vserverName
    ciphers: ["aes256_ctr", "aes192_ctr"]
    key_exchange_algorithms: ["diffie_hellman_group_exchange_sha256"]
    mac_algorithms: ["hmac_sha1"]
    max_authentication_retry_count: 6
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify SSH algorithms at cluster level
  netapp.ontap.na_ontap_security_ssh:
    vserver:
    ciphers: ["aes256_ctr", "aes192_ctr"]
    key_exchange_algorithms: ["diffie_hellman_group_exchange_sha256"]
    mac_algorithms: ["hmac_sha1"]
    max_authentication_retry_count: 6
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify SSH algorithms at cluster level
  netapp.ontap.na_ontap_security_ssh:
    ciphers: ["aes256_ctr", "aes192_ctr"]
    key_exchange_algorithms: ["diffie_hellman_group_exchange_sha256"]
    mac_algorithms: ["hmac_sha1"]
    max_authentication_retry_count: 6
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
