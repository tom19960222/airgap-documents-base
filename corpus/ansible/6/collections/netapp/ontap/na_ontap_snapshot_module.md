---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_snapshot module – NetApp ONTAP manage Snapshots"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_snapshot_module.html
fetched_at: 2026-07-28T00:13:15+00:00
---
# netapp.ontap.na_ontap_snapshot module – NetApp ONTAP manage Snapshots

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
> see [Requirements](na_ontap_snapshot_module.md#ansible-collections-netapp-ontap-na-ontap-snapshot-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_snapshot`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_snapshot_module.md#synopsis)
- [Requirements](na_ontap_snapshot_module.md#requirements)
- [Parameters](na_ontap_snapshot_module.md#parameters)
- [Notes](na_ontap_snapshot_module.md#notes)
- [Examples](na_ontap_snapshot_module.md#examples)

## [Synopsis](na_ontap_snapshot_module.md#id1)

- Create/Modify/Delete ONTAP snapshots

## [Requirements](na_ontap_snapshot_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_snapshot_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **async_bool**  boolean | If true, the snapshot is to be created asynchronously.  Choices:   - `false` - `true` |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **comment**  string | A human readable comment attached with the snapshot. The size of the comment can be at most 255 characters. |
| **expiry_time**  string  added in netapp.ontap 21.8.0 | Snapshot expire time, only available with REST.  format should be in the timezone configured with cluster. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_name**  string  added in netapp.ontap 2.8.0 | Name of the existing snapshot to be renamed to. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **ignore_owners**  boolean | if this field is true, snapshot will be deleted even if some other processes are accessing it.  Choices:   - `false` - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **snapmirror_label**  string | A human readable SnapMirror Label attached with the snapshot.  Size of the label can be at most 31 characters.  Supported with REST on Ontap 9.7 or higher. |
| **snapshot**  string / required | Name of the snapshot to be managed. The maximum string length is 256 characters. |
| **snapshot_instance_uuid**  string | The 128 bit unique snapshot identifier expressed in the form of UUID. |
| **state**  string | If you want to create/modify a snapshot, or delete it.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **volume**  string / required | Name of the volume on which the snapshot is to be created. |
| **vserver**  string / required | The Vserver name |

## [Notes](na_ontap_snapshot_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_snapshot_module.md#id5)

```yaml+jinja
- name: create SnapShot
  tags:
    - create
  netapp.ontap.na_ontap_snapshot:
    state: present
    snapshot: "{{ snapshot name }}"
    volume: "{{ vol name }}"
    comment: "i am a comment"
    expiry_time: "2022-02-04T14:00:00-05:00"
    vserver: "{{ vserver name }}"
    username: "{{ netapp username }}"
    password: "{{ netapp password }}"
    hostname: "{{ netapp hostname }}"
- name: delete SnapShot
  tags:
    - delete
  netapp.ontap.na_ontap_snapshot:
    state: absent
    snapshot: "{{ snapshot name }}"
    volume: "{{ vol name }}"
    vserver: "{{ vserver name }}"
    username: "{{ netapp username }}"
    password: "{{ netapp password }}"
    hostname: "{{ netapp hostname }}"
- name: modify SnapShot
  tags:
    - modify
  netapp.ontap.na_ontap_snapshot:
    state: present
    snapshot: "{{ snapshot name }}"
    comment: "New comments are great"
    volume: "{{ vol name }}"
    vserver: "{{ vserver name }}"
    username: "{{ netapp username }}"
    password: "{{ netapp password }}"
    hostname: "{{ netapp hostname }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
