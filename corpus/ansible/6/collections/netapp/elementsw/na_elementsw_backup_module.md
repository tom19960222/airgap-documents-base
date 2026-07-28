---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_backup module – NetApp Element Software Create Backups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_backup_module.html
fetched_at: 2026-07-28T00:11:44+00:00
---
# netapp.elementsw.na_elementsw_backup module – NetApp Element Software Create Backups

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/netapp/elementsw) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_backup_module.md#ansible-collections-netapp-elementsw-na-elementsw-backup-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_backup`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_backup_module.md#synopsis)
- [Requirements](na_elementsw_backup_module.md#requirements)
- [Parameters](na_elementsw_backup_module.md#parameters)
- [Notes](na_elementsw_backup_module.md#notes)
- [Examples](na_elementsw_backup_module.md#examples)

## [Synopsis](na_elementsw_backup_module.md#id1)

- Create backup

## [Requirements](na_elementsw_backup_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_backup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dest_hostname**  string | hostname for the backup source cluster  will be set equal to hostname if not specified |
| **dest_password**  string | password for the backup destination cluster  will be set equal to password if not specified |
| **dest_username**  string | username for the backup destination cluster  will be set equal to username if not specified |
| **dest_volume_id**  string / required | ID of the backup destination volume |
| **format**  string | Backup format to use  Choices:   - `"native"` ← (default) - `"uncompressed"` |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **script**  string | the backup script to be executed |
| **script_parameters**  dictionary | the backup script parameters |
| **src_volume_id**  aliases: volume_id  string / required | ID of the backup source volume. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |

## [Notes](na_elementsw_backup_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_backup_module.md#id5)

```yaml+jinja
na_elementsw_backup:
  hostname: "{{ source_cluster_hostname }}"
  username: "{{ source_cluster_username }}"
  password: "{{ source_cluster_password }}"
  src_volume_id: 1
  dest_hostname: "{{ destination_cluster_hostname }}"
  dest_username: "{{ destination_cluster_username }}"
  dest_password: "{{ destination_cluster_password }}"
  dest_volume_id: 3
  format: native
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
