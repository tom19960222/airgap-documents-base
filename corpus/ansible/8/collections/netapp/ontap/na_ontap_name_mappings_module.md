---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_name_mappings module – NetApp ONTAP name mappings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_name_mappings_module.html
fetched_at: 2026-07-28T02:42:42+00:00
---
# netapp.ontap.na_ontap_name_mappings module – NetApp ONTAP name mappings

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
> see [Requirements](na_ontap_name_mappings_module.md#ansible-collections-netapp-ontap-na-ontap-name-mappings-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_name_mappings`.

New in netapp.ontap 22.0.0

- [Synopsis](na_ontap_name_mappings_module.md#synopsis)
- [Requirements](na_ontap_name_mappings_module.md#requirements)
- [Parameters](na_ontap_name_mappings_module.md#parameters)
- [Notes](na_ontap_name_mappings_module.md#notes)
- [Examples](na_ontap_name_mappings_module.md#examples)

## [Synopsis](na_ontap_name_mappings_module.md#id1)

- Create/Delete/Modify name mappings for an SVM on ONTAP.

## [Requirements](na_ontap_name_mappings_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_name_mappings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **client_match**  string | Client workstation IP Address which is matched when searching for the pattern.  Example ‘10.254.101.111/28’  Client match value can be in any of the following formats, - As an IPv4 address with a subnet mask expressed as a number of bits; for instance, 10.1.12.0/24 - As an IPv6 address with a subnet mask expressed as a number of bits; for instance, fd20:8b1e:b255:4071::/64 - As an IPv4 address with a network mask; for instance, 10.1.16.0/255.255.255.0 - As a hostname |
| **direction**  string / required | Direction in which the name mapping is applied.  The possible values are, krb_unix - Kerberos principal name to UNIX user name win_unix - Windows user name to UNIX user name unix_win - UNIX user name to Windows user name mapping s3_unix - S3 user name to UNIX user name mapping s3_win - S3 user name to Windows user name mapping  s3_unix and s3_win requires ONTAP 9.12.1 or later.  **Choices:**   - `"krb_unix"` - `"win_unix"` - `"unix_win"` - `"s3_unix"` - `"s3_win"` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_index**  integer | If no entry with index is found, it is created by reindexing the entry for from_index.  If no entry is found for index and from_index, an error is reported.  Minimum value is 1 and maximum is 2147483647.  Requires ONTAP version 9.7 or later. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **index**  integer / required | Position in the list of name mappings.  Minimum value is 1 and maximum is 2147483647. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **pattern**  string | Pattern used to match the name while searching for a name that can be used as a replacement.  The pattern is a UNIX-style regular expression.  Regular expressions are case-insensitive when mapping from Windows to UNIX, and they are case-sensitive for mappings from Kerberos to UNIX and UNIX to Windows.  Minimum length is 1 and maximum length is 256.  Pattern should be unique for each index of vserver.  Example ENGCIFS_AD_USER. |
| **replacement**  string | The name that is used as a replacement, if the pattern associated with this entry matches.  Minimum length is 1 and maximum length is 256.  Example unix_user1. |
| **state**  string | Whether the specified name mappings should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_name_mappings_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_name_mappings_module.md#id5)

```yaml+jinja
- name: create name mappings configuration
  netapp.ontap.na_ontap_name_mappings:
    vserver: vserverName
    direction: win_unix
    index: 1
    pattern: ENGCIFS_AD_USER
    replacement: unix_user
    client_match: 10.254.101.111/28
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: modify name mappings configuration
  netapp.ontap.na_ontap_name_mappings:
    vserver: vserverName
    direction: win_unix
    index: 1
    pattern: ENGCIFS_AD_USERS
    replacement: unix_user1
    client_match: 10.254.101.112/28
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Swap name mappings position
  netapp.ontap.na_ontap_name_mappings:
    vserver: vserverName
    direction: win_unix
    index: 1
    pattern: ENGCIFS_AD_USERS
    replacement: unix_user1
    from_index: 2
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete name mappings configuration
  netapp.ontap.na_ontap_name_mappings:
    vserver: vserverName
    direction: win_unix
    index: 1
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
