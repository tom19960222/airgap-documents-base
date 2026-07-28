---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_qtree module – NetApp ONTAP manage qtrees"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_qtree_module.html
fetched_at: 2026-07-28T00:13:00+00:00
---
# netapp.ontap.na_ontap_qtree module – NetApp ONTAP manage qtrees

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
> see [Requirements](na_ontap_qtree_module.md#ansible-collections-netapp-ontap-na-ontap-qtree-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_qtree`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_qtree_module.md#synopsis)
- [Requirements](na_ontap_qtree_module.md#requirements)
- [Parameters](na_ontap_qtree_module.md#parameters)
- [Notes](na_ontap_qtree_module.md#notes)
- [Examples](na_ontap_qtree_module.md#examples)

## [Synopsis](na_ontap_qtree_module.md#id1)

- Create/Modify/Delete Qtrees.

## [Requirements](na_ontap_qtree_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_qtree_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **export_policy**  string  added in netapp.ontap 2.9.0 | The name of the export policy to apply. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **flexvol_name**  string / required | The name of the FlexVol the qtree should exist on. |
| **force_delete**  boolean  added in netapp.ontap 20.8.0 | Whether the qtree should be deleted even if files still exist.  Note that the default of true reflect the REST API behavior.  a value of false is not supported with REST.  Choices:   - `false` - `true` ← (default) |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_name**  string  added in netapp.ontap 2.7.0 | Name of the qtree to be renamed. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **name**  string / required | The name of the qtree to manage.  With REST, this can also be a path. |
| **ontapi**  integer | The ontap api version to use |
| **oplocks**  string  added in netapp.ontap 2.9.0 | Whether the oplocks should be enabled or not for the qtree.  Choices:   - `"enabled"` - `"disabled"` |
| **password**  aliases: pass  string | Password for the specified user. |
| **security_style**  string  added in netapp.ontap 2.9.0 | The security style for the qtree.  Choices:   - `"unix"` - `"ntfs"` - `"mixed"` |
| **state**  string | Whether the specified qtree should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **time_out**  integer  added in netapp.ontap 2.9.0 | Maximum time to wait for qtree deletion in seconds when wait_for_completion is True.  Error out if task is not completed in defined time.  Default is set to 3 minutes.  Default: `180` |
| **unix_group**  string  added in netapp.ontap 21.21.0 | The group set as owner of the qtree.  Only supported with REST and ONTAP 9.9 or later. |
| **unix_permissions**  string  added in netapp.ontap 2.9.0 | File permissions bits of the qtree.  Accepts either octal or string format.  Examples 0777, 777 in octal and —rwxrwxrwx, sstrwxrwxrwx, rwxrwxrwx in string format. |
| **unix_user**  string  added in netapp.ontap 21.21.0 | The user set as owner of the qtree.  Only supported with REST and ONTAP 9.9 or later. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  string / required | The name of the vserver to use. |
| **wait_for_completion**  boolean  added in netapp.ontap 2.9.0 | Only applicable for REST. When using ZAPI, the deletion is always synchronous.  Deleting a qtree may take time if many files need to be deleted.  Set this parameter to ‘true’ for synchronous execution during delete.  Set this parameter to ‘false’ for asynchronous execution.  For asynchronous, execution exits as soon as the request is sent, and the qtree is deleted in background.  Choices:   - `false` - `true` ← (default) |

## [Notes](na_ontap_qtree_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_qtree_module.md#id5)

```yaml+jinja
- name: Create Qtrees.
  netapp.ontap.na_ontap_qtree:
    state: present
    name: ansibleQTree
    flexvol_name: ansibleVolume
    export_policy: policyName
    security_style: mixed
    oplocks: disabled
    unix_permissions: 0777
    vserver: ansibleVServer
    unix_user: user1
    unix_group: group1
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Rename Qtrees.
  netapp.ontap.na_ontap_qtree:
    state: present
    from_name: ansibleQTree
    name: ansibleQTree_rename
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: modify Qtrees unix_permissions using string format.
  netapp.ontap.na_ontap_qtree:
    state: present
    name: ansibleQTree_rename
    flexvol_name: ansibleVolume
    vserver: ansibleVServer
    unix_permissions: sstrwxrwxrwx
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: delete Qtrees.
  netapp.ontap.na_ontap_qtree:
    state: absent
    name: ansibleQTree_rename
    vserver: ansibleVServer
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
