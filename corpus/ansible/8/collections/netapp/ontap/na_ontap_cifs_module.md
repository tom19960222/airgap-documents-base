---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_cifs module – NetApp ONTAP Manage cifs-share"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_cifs_module.html
fetched_at: 2026-07-28T02:41:40+00:00
---
# netapp.ontap.na_ontap_cifs module – NetApp ONTAP Manage cifs-share

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
> see [Requirements](na_ontap_cifs_module.md#ansible-collections-netapp-ontap-na-ontap-cifs-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_cifs`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_cifs_module.md#synopsis)
- [Requirements](na_ontap_cifs_module.md#requirements)
- [Parameters](na_ontap_cifs_module.md#parameters)
- [Notes](na_ontap_cifs_module.md#notes)
- [Examples](na_ontap_cifs_module.md#examples)

## [Synopsis](na_ontap_cifs_module.md#id1)

- Create or destroy or modify(path) cifs-share on ONTAP.

## [Requirements](na_ontap_cifs_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_cifs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_based_enumeration**  boolean  *added in netapp.ontap 22.3.0* | If enabled, all folders inside this share are visible to a user based on that individual user access right; prevents the display of folders or other shared resources that the user does not have access to.  This option only supported with REST.  **Choices:**   - `false` - `true` |
| **allow_unencrypted_access**  boolean  *added in netapp.ontap 22.3.0* | Specifies whether or not the SMB2 clients are allowed to access the encrypted share.  This option requires REST and ONTAP 9.11.0 or later.  **Choices:**   - `false` - `true` |
| **browsable**  boolean  *added in netapp.ontap 22.5.0* | Specifies whether or not the Windows clients can browse the share.  This option requires REST and ONTAP 9.13.1 or later.  **Choices:**   - `false` - `true` |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **change_notify**  boolean  *added in netapp.ontap 22.3.0* | Specifies whether CIFS clients can request for change notifications for directories on this share.  This option only supported with REST.  **Choices:**   - `false` - `true` |
| **comment**  string  *added in netapp.ontap 21.7.0* | The CIFS share description. |
| **continuously_available**  boolean  *added in netapp.ontap 22.3.0* | Specifies whether or not the clients connecting to this share can open files in a persistent manner.  Files opened in this way are protected from disruptive events, such as, failover and giveback.  This option requires REST and ONTAP 9.10.1 or later.  **Choices:**   - `false` - `true` |
| **encryption**  boolean  *added in netapp.ontap 22.3.0* | Specifies that SMB encryption must be used when accessing this share. Clients that do not support encryption are not able to access this share.  This option only supported with REST.  **Choices:**   - `false` - `true` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **home_directory**  boolean  *added in netapp.ontap 22.3.0* | Specifies whether or not the share is a home directory share, where the share and path names are dynamic.  ONTAP home directory functionality automatically offer each user a dynamic share to their home directory without creating an individual SMB share for each user.  This feature enable us to configure a share that maps to different directories based on the user that connects to it  Instead of creating a separate shares for each user, a single share with a home directory parameters can be created.  In a home directory share, ONTAP dynamically generates the share-name and share-path by substituting %w, %u, and %d variables with the corresponding Windows user name, UNIX user name, and domain name, respectively.  This option only supported with REST and cannot modify.  **Choices:**   - `false` - `true` |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **name**  aliases: share_name  string / required | The name of the CIFS share. The CIFS share name is a UTF-8 string with the following characters being illegal; control characters from 0x00 to 0x1F, both inclusive, 0x22 (double quotes) |
| **namespace_caching**  boolean  *added in netapp.ontap 22.3.0* | Specifies whether or not the SMB clients connecting to this share can cache the directory enumeration results returned by the CIFS servers.  This option requires REST and ONTAP 9.10.1 or later.  **Choices:**   - `false` - `true` |
| **ontapi**  integer | The ontap api version to use |
| **oplocks**  boolean  *added in netapp.ontap 22.3.0* | Specify whether opportunistic locks are enabled on this share. “Oplocks” allow clients to lock files and cache content locally, which can increase performance for file operations.  Only supported with REST.  **Choices:**   - `false` - `true` |
| **password**  aliases: pass  string | Password for the specified user. |
| **path**  string | The file system path that is shared through this CIFS share. The path is the full, user visible path relative to the vserver root, and it might be crossing junction mount points. The path is in UTF8 and uses forward slash as directory separator. |
| **share_properties**  list / elements=string  *added in netapp.ontap 2.8.0* | The list of properties for the CIFS share.  Not supported with REST.  share-properties are separate fields in the REST API.  You can achieve this functionality by setting `access_based_enumeration`, `change_notify`, `encryption`, `home_directory`, `oplocks`, `show_snapshot`, `continuously_available` and `namespace_caching`. |
| **show_previous_versions**  boolean  *added in netapp.ontap 22.5.0* | Specifies that the previous version can be viewed and restored from the client.  This option requires REST and ONTAP 9.13.1 or later.  **Choices:**   - `false` - `true` |
| **show_snapshot**  boolean  *added in netapp.ontap 22.3.0* | Specifies whether or not the Snapshot copies can be viewed and traversed by clients.  This option requires REST and ONTAP 9.10.1 or later.  **Choices:**   - `false` - `true` |
| **state**  string | Whether the specified CIFS share should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **symlink_properties**  list / elements=string  *added in netapp.ontap 2.8.0* | The list of symlink properties for this CIFS share.  Not supported with REST, this option is replaced with `unix_symlink` in REST. |
| **unix_symlink**  string  *added in netapp.ontap 21.19.0* | The list of unix_symlink properties for this CIFS share  This option only supported with REST.  **Choices:**   - `"local"` - `"widelink"` - `"disable"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vscan_fileop_profile**  string  *added in netapp.ontap 2.9.0* | Profile_set of file_ops to which vscan on access scanning is applicable.  Not supported with REST.  **Choices:**   - `"no_scan"` - `"standard"` - `"strict"` - `"writes_only"` |
| **vserver**  string / required | Vserver containing the CIFS share. |

## [Notes](na_ontap_cifs_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_cifs_module.md#id5)

```yaml+jinja
- name: Create CIFS share - ZAPI
  netapp.ontap.na_ontap_cifs:
    state: present
    name: cifsShareName
    path: /
    vserver: vserverName
    share_properties: browsable,oplocks
    symlink_properties: read_only,enable
    comment: CIFS share description
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete CIFS share - ZAPI
  netapp.ontap.na_ontap_cifs:
    state: absent
    name: cifsShareName
    vserver: vserverName
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify path CIFS share - ZAPI
  netapp.ontap.na_ontap_cifs:
    state: present
    name: pb_test
    vserver: vserverName
    path: /
    share_properties: show_previous_versions
    symlink_properties: disable
    vscan_fileop_profile: no_scan
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create CIFS share - REST
  netapp.ontap.na_ontap_cifs:
    state: present
    name: cifsShareName
    path: /
    vserver: vserverName
    oplocks: true
    change_notify: true
    unix_symlink: disable
    comment: CIFS share description
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Modify CIFS share - REST
  netapp.ontap.na_ontap_cifs:
    state: present
    name: cifsShareName
    path: /
    vserver: vserverName
    oplocks: true
    change_notify: true
    unix_symlink: local
    comment: CIFS share description
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
